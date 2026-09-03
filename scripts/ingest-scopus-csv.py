#!/usr/bin/env python3
"""
Scopus CSV Enrichment Script — The Meridian Grid (TMG)
Reads Titles from Search-Log.xlsx, fuzzy-matches them against a Scopus CSV export,
generates Semantic Paper IDs, and populates the missing metadata.
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
TARGET_SHEET_NAME = "Filtered_Results"


def normalize_author_name(authors_str: str) -> tuple[str, bool]:
    if not authors_str or pd.isna(authors_str):
        return "Unknown", False
    authors_str = str(authors_str).strip()
    first_author_block = authors_str.split(",")[0].strip()
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


def fuzzy_match_row(target_title: str, csv_df: pd.DataFrame):
    titles = csv_df["Title"].dropna().astype(str).tolist()
    matches = difflib.get_close_matches(target_title, titles, n=1, cutoff=0.85)
    if matches:
        matched_title = matches[0]
        return csv_df[csv_df["Title"] == matched_title].iloc[0]
    return None


def enrich_excel(csv_path: str, query_id: str, excel_path: str):
    print(f"[*] Reading Scopus export: {csv_path}")
    try:
        df = pd.read_csv(csv_path, encoding="utf-8-sig")
    except Exception as e:
        print(f"[ERROR] Failed to read CSV: {e}")
        sys.exit(1)

    print(f"[*] Opening Excel tracking log: {excel_path}")
    if not os.path.exists(excel_path):
        print(f"[ERROR] Excel file not found: {excel_path}")
        sys.exit(1)

    wb = openpyxl.load_workbook(excel_path)
    sheet = wb[TARGET_SHEET_NAME]
    headers = {cell.value: idx + 1 for idx, cell in enumerate(sheet[1]) if cell.value}

    # Ensure expected columns exist (add Keywords to your Excel file)
    for expected in [
        "Paper_ID",
        "Query_ID",
        "Authors",
        "Year",
        "DOI",
        "Selection_Status",
        "Keywords",
    ]:
        if expected not in headers:
            print(
                f"[ERROR] Column '{expected}' not found in sheet '{TARGET_SHEET_NAME}'. Please add it to row 1."
            )
            sys.exit(1)

    existing_ids = set()
    for row in range(2, sheet.max_row + 1):
        pid = sheet.cell(row=row, column=headers["Paper_ID"]).value
        if pid:
            existing_ids.add(str(pid))

    updated_count = 0

    for row in range(2, sheet.max_row + 1):
        title_val = sheet.cell(row=row, column=headers["Title"]).value
        author_val = sheet.cell(row=row, column=headers["Authors"]).value

        # If row has a Title but Authors is empty, it needs enrichment
        if title_val and not author_val:
            match = fuzzy_match_row(str(title_val), df)
            if match is not None:
                authors = str(match.get("Authors", "")).strip()
                year = match.get("Year", "")
                doi = str(match.get("DOI", "")).strip()
                doi = "" if doi.lower() == "nan" else doi

                # Handle Scopus keyword column variations
                keywords = ""
                if "Author Keywords" in match:
                    keywords = str(match["Author Keywords"]).strip()
                elif "Keywords" in match:
                    keywords = str(match["Keywords"]).strip()
                keywords = "" if keywords.lower() == "nan" else keywords

                paper_id = generate_paper_id(authors, year, existing_ids)

                sheet.cell(row=row, column=headers["Paper_ID"], value=paper_id)
                sheet.cell(row=row, column=headers["Query_ID"], value=query_id)
                sheet.cell(row=row, column=headers["Authors"], value=authors)
                sheet.cell(row=row, column=headers["Year"], value=year)
                sheet.cell(row=row, column=headers["DOI"], value=doi)
                sheet.cell(row=row, column=headers["Keywords"], value=keywords)

                if not sheet.cell(row=row, column=headers["Selection_Status"]).value:
                    sheet.cell(
                        row=row,
                        column=headers["Selection_Status"],
                        value="Included_Stage1",
                    )

                updated_count += 1
                print(f"  [+] Enriched: {paper_id} - {title_val[:50]}...")
            else:
                print(f"  [!] No CSV match found for: {title_val[:50]}...")

    wb.save(excel_path)
    print(f"\n[SUCCESS] Enriched {updated_count} rows in '{TARGET_SHEET_NAME}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Enrich LLM-filtered Excel log with Scopus CSV data."
    )
    parser.add_argument("csv_file", help="Path to the raw Scopus CSV export file.")
    parser.add_argument(
        "query_id", help="The Query ID to tag these records with (e.g., Q01)."
    )
    parser.add_argument(
        "--excel",
        default=DEFAULT_EXCEL_PATH,
        help=f"Path to Excel file (default: {DEFAULT_EXCEL_PATH})",
    )

    args = parser.parse_args()
    enrich_excel(args.csv_file, args.query_id, args.excel)
