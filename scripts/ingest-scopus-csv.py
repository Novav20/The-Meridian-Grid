#!/usr/bin/env python3
"""
Scopus CSV Enrichment Script — The Meridian Grid (TMG)
Reads Titles from Search-Log.xlsx, fuzzy-matches them against one or multiple Scopus CSV exports,
generates Semantic Paper IDs, and populates bibliographic metadata.

Usage:
  python scripts/ingest-scopus-csv.py Q03
  python scripts/ingest-scopus-csv.py <custom_path> Q03
"""

import os
import re
import sys
import argparse
import unicodedata
import pandas as pd
import openpyxl
import difflib

DEFAULT_EXCEL_PATH = "docs/01-PM-Project-Management/Search-Log.xlsx"
DEFAULT_EXPORTS_BASE = "docs/01-PM-Project-Management/Search-Exports"
TARGET_SHEET_NAME = "Filtered_Results"


def normalize_title(title_str: str) -> str:
    if not title_str or pd.isna(title_str):
        return ""
    clean = re.sub(r"[^\w\s]", "", str(title_str).lower())
    return " ".join(clean.split())


def normalize_author_name(authors_str: str) -> tuple[str, bool]:
    if not authors_str or pd.isna(authors_str):
        return "Unknown", False
    authors_str = str(authors_str).strip()
    first_author_block = authors_str.split(";")[0].split(",")[0].strip()
    first_author_name = first_author_block.split(" ")[0]
    clean_name = (
        unicodedata.normalize("NFKD", first_author_name)
        .encode("ASCII", "ignore")
        .decode("utf-8")
    )
    base_author = re.sub(r"[^a-zA-Z]", "", clean_name)
    if not base_author:
        base_author = "Unknown"
    is_et_al = ";" in authors_str or authors_str.count(",") > 1
    return base_author.capitalize(), is_et_al


def generate_paper_id(authors_str: str, year: any, existing_ids: set) -> str:
    base_author, is_et_al = normalize_author_name(authors_str)
    try:
        year_str = str(int(float(year)))
    except (ValueError, TypeError):
        year_str = "ND"
    et_al_str = "_et_al" if is_et_al else ""
    base_id = f"{base_author}{et_al_str}_{year_str}"

    final_id = base_id
    suffix_idx = 0
    while final_id in existing_ids:
        suffix_char = chr(ord("a") + suffix_idx)
        final_id = f"{base_id}{suffix_char}"
        suffix_idx += 1
    existing_ids.add(final_id)
    return final_id


def resolve_scopus_path(
    primary_arg: str, secondary_arg: str, source_flag: str
) -> tuple[str, str]:
    if secondary_arg:
        target_path = primary_arg
        query_id = secondary_arg
    else:
        query_id = primary_arg
        if source_flag:
            target_path = source_flag
        else:
            default_dir = os.path.join(DEFAULT_EXPORTS_BASE, query_id)
            default_file = os.path.join(DEFAULT_EXPORTS_BASE, f"{query_id}.csv")
            if os.path.isdir(default_dir):
                target_path = default_dir
            elif os.path.isfile(default_file):
                target_path = default_file
            else:
                target_path = default_dir  # let load_scopus_data handle error

    return os.path.normpath(target_path), query_id.strip()


def load_scopus_data(target_path: str) -> pd.DataFrame:
    files_to_load = []
    if os.path.isdir(target_path):
        for root, _, files in os.walk(target_path):
            for f in files:
                if f.lower().endswith(".csv"):
                    files_to_load.append(os.path.join(root, f))
    elif os.path.isfile(target_path):
        files_to_load.append(target_path)
    else:
        print(f"[ERROR] Scopus export path not found: {target_path}", file=sys.stderr)
        sys.exit(1)

    if not files_to_load:
        print(f"[ERROR] No CSV files found at: {target_path}", file=sys.stderr)
        sys.exit(1)

    dfs = []
    for fpath in files_to_load:
        try:
            temp_df = pd.read_csv(fpath, encoding="utf-8-sig")
            dfs.append(temp_df)
            print(f"  [+] Loaded: {os.path.basename(fpath)} ({len(temp_df)} records)")
        except Exception as e:
            print(f"  [!] Failed to read {fpath}: {e}", file=sys.stderr)

    if not dfs:
        sys.exit(1)

    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.drop_duplicates(subset=["Title"], inplace=True)
    print(f"[*] Total unique source records in pool: {len(combined_df)}")
    return combined_df


def fuzzy_match_row(target_title: str, csv_df: pd.DataFrame):
    titles = csv_df["Title"].dropna().astype(str).tolist()
    matches = difflib.get_close_matches(target_title, titles, n=1, cutoff=0.80)
    if matches:
        matched_title = matches[0]
        return csv_df[csv_df["Title"] == matched_title].iloc[0]
    return None


def enrich_excel(target_path: str, query_id: str, excel_path: str):
    print(f"[*] Ingesting Scopus dataset for Query '{query_id}' from: {target_path}")
    df_pool = load_scopus_data(target_path)

    print(f"[*] Opening Excel master log: {excel_path}")
    if not os.path.exists(excel_path):
        print(f"[ERROR] Excel file not found: {excel_path}", file=sys.stderr)
        sys.exit(1)

    wb = openpyxl.load_workbook(excel_path)
    sheet = wb[TARGET_SHEET_NAME]
    headers = {cell.value: idx + 1 for idx, cell in enumerate(sheet[1]) if cell.value}

    expected_columns = [
        "Paper_ID",
        "Query_ID",
        "Title",
        "Authors",
        "Abstract",
        "Keywords",
        "Year",
        "DOI",
        "Selection_Status",
        "Justification",
    ]
    for col in expected_columns:
        if col not in headers:
            print(f"[ERROR] Required column '{col}' missing in sheet.", file=sys.stderr)
            sys.exit(1)

    existing_ids = set()
    enriched_titles = {}

    for row_idx in range(2, sheet.max_row + 1):
        pid = sheet.cell(row=row_idx, column=headers["Paper_ID"]).value
        t_val = sheet.cell(row=row_idx, column=headers["Title"]).value
        q_val = sheet.cell(row=row_idx, column=headers["Query_ID"]).value
        a_val = sheet.cell(row=row_idx, column=headers["Authors"]).value

        if pid:
            existing_ids.add(str(pid))
        if t_val and a_val:
            enriched_titles[normalize_title(t_val)] = (row_idx, pid, q_val)

    updated_count = 0

    for row in range(2, sheet.max_row + 1):
        title_val = sheet.cell(row=row, column=headers["Title"]).value
        author_val = sheet.cell(row=row, column=headers["Authors"]).value
        abstract_val = sheet.cell(row=row, column=headers["Abstract"]).value

        if title_val and (not author_val or not abstract_val):
            norm_t = normalize_title(title_val)

            if norm_t in enriched_titles:
                orig_row, orig_pid, orig_qid = enriched_titles[norm_t]
                print(
                    f"  [!] Duplicate detected at row {row}: Already enriched at row {orig_row} as '{orig_pid}' under {orig_qid}. Skipping."
                )
                sheet.cell(
                    row=row,
                    column=headers["Selection_Status"],
                    value="Excluded_Duplicate",
                )
                sheet.cell(
                    row=row,
                    column=headers["Justification"],
                    value=f"Duplicate of {orig_pid} ({orig_qid})",
                )
                continue

            match = fuzzy_match_row(str(title_val), df_pool)
            if match is not None:
                authors = str(match.get("Authors", "")).strip()
                year = match.get("Year", "")
                doi = str(match.get("DOI", "")).strip()
                doi = "" if doi.lower() == "nan" else doi

                abstract = str(match.get("Abstract", "")).strip()
                abstract = "" if abstract.lower() == "nan" else abstract

                keywords = ""
                if "Author Keywords" in match:
                    keywords = str(match["Author Keywords"]).strip()
                elif "Keywords" in match:
                    keywords = str(match["Keywords"]).strip()
                keywords = "" if keywords.lower() == "nan" else keywords

                current_pid = sheet.cell(row=row, column=headers["Paper_ID"]).value
                if current_pid:
                    paper_id = current_pid
                else:
                    paper_id = generate_paper_id(authors, year, existing_ids)
                    sheet.cell(row=row, column=headers["Paper_ID"], value=paper_id)

                sheet.cell(row=row, column=headers["Query_ID"], value=query_id)
                sheet.cell(row=row, column=headers["Authors"], value=authors)
                sheet.cell(row=row, column=headers["Abstract"], value=abstract)
                sheet.cell(row=row, column=headers["Year"], value=year)
                sheet.cell(row=row, column=headers["DOI"], value=doi)
                sheet.cell(row=row, column=headers["Keywords"], value=keywords)

                if not sheet.cell(row=row, column=headers["Selection_Status"]).value:
                    sheet.cell(
                        row=row,
                        column=headers["Selection_Status"],
                        value="Included_Stage1",
                    )

                enriched_titles[norm_t] = (row, paper_id, query_id)
                updated_count += 1
                print(f"  [+] Enriched: {paper_id} - {title_val[:45]}...")
            else:
                print(f"  [!] No pool match found for: {title_val[:45]}...")

    wb.save(excel_path)
    print(f"\n[SUCCESS] Enriched {updated_count} rows in '{TARGET_SHEET_NAME}'.")


def main():
    parser = argparse.ArgumentParser(
        description="Enrich LLM-filtered Excel log with Scopus CSV data (supports directory or file)."
    )
    parser.add_argument(
        "arg1", help="Query ID (e.g. Q03) OR explicit path to CSV file/dir."
    )
    parser.add_argument(
        "arg2", nargs="?", default=None, help="Query ID if arg1 was an explicit path."
    )
    parser.add_argument(
        "--source",
        default=None,
        help="Explicit override path to CSV file or directory.",
    )
    parser.add_argument(
        "--excel",
        default=DEFAULT_EXCEL_PATH,
        help=f"Path to Excel file (default: {DEFAULT_EXCEL_PATH})",
    )

    args = parser.parse_args()
    target_path, query_id = resolve_scopus_path(args.arg1, args.arg2, args.source)
    enrich_excel(target_path, query_id, args.excel)


if __name__ == "__main__":
    main()
