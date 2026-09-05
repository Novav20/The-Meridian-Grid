#!/usr/bin/env python3
"""
Extraction Splitter Script — The Meridian Grid (TMG)
Correlates raw Gemini Notebook extraction blocks with Search-Log.xlsx,
injects authoritative bibliographic frontmatter, and writes <Paper_ID>.md notes.

Usage:
  python scripts/split-extractions.py <raw_file_path> <query_id> [options]
"""

import os
import re
import sys
import argparse
import difflib
from datetime import datetime
import pandas as pd
import openpyxl

DEFAULT_OUTPUT_DIR = "docs/02-SI-Requirements/Domain-Research/extractions"
DEFAULT_RAW_SOURCES_BASE = "docs/02-SI-Requirements/Domain-Research/raw-sources"
DEFAULT_EXCEL_PATH = "docs/01-PM-Project-Management/Search-Log.xlsx"
TARGET_SHEET_NAME = "Filtered_Results"


def load_log_metadata(excel_path: str, query_id: str) -> pd.DataFrame:
    if not os.path.exists(excel_path):
        print(f"[ERROR] Excel log not found at: {excel_path}", file=sys.stderr)
        sys.exit(1)

    wb = openpyxl.load_workbook(excel_path, data_only=True)
    if TARGET_SHEET_NAME not in wb.sheetnames:
        print(
            f"[ERROR] Sheet '{TARGET_SHEET_NAME}' not found in {excel_path}",
            file=sys.stderr,
        )
        sys.exit(1)

    sheet = wb[TARGET_SHEET_NAME]
    data = list(sheet.values)
    if not data:
        print(f"[ERROR] Sheet '{TARGET_SHEET_NAME}' is empty.", file=sys.stderr)
        sys.exit(1)

    headers = [str(h).strip() if h is not None else "" for h in data[0]]
    df = pd.DataFrame(data[1:], columns=headers)
    df = df[df["Query_ID"].astype(str).str.strip() == query_id.strip()]

    if df.empty:
        print(
            f"[ERROR] No records found in '{TARGET_SHEET_NAME}' for Query_ID '{query_id}'.",
            file=sys.stderr,
        )
        sys.exit(1)

    return df


def parse_raw_blocks(content: str) -> list[dict]:
    # Splits on standard markdown delimiter (---)
    chunks = re.split(r"(?m)^---\s*$", content)
    blocks = []

    for i in range(1, len(chunks), 2):
        frontmatter = chunks[i].strip()
        body = chunks[i + 1].strip() if i + 1 < len(chunks) else ""

        # Extract title key from block header
        title_match = re.search(
            r'^title:\s*["\']?(.*?)["\']?\s*$',
            frontmatter,
            re.MULTILINE | re.IGNORECASE,
        )
        if title_match:
            blocks.append({"title": title_match.group(1).strip(), "body": body})
    return blocks


def match_paper(title: str, df: pd.DataFrame) -> pd.Series:
    known_titles = df["Title"].dropna().astype(str).tolist()
    matches = difflib.get_close_matches(title, known_titles, n=1, cutoff=0.65)
    if matches:
        return df[df["Title"] == matches[0]].iloc[0]
    return None


def find_source_pdf(raw_sources_dir: str, title: str) -> str:
    if not os.path.exists(raw_sources_dir):
        return ""

    files = [f for f in os.listdir(raw_sources_dir) if f.lower().endswith(".pdf")]
    matches = difflib.get_close_matches(f"{title}.pdf", files, n=1, cutoff=0.55)
    return matches[0] if matches else ""


def build_frontmatter(
    row: pd.Series, query_id: str, source_pdf: str, today: str
) -> str:
    paper_id = str(row.get("Paper_ID", "")).strip()
    title = str(row.get("Title", "")).strip().replace('"', '\\"')
    authors = str(row.get("Authors", "")).strip().replace('"', '\\"')
    year = str(row.get("Year", "")).strip()
    doi = str(row.get("DOI", "")).strip()

    # Parse delimited keywords (semicolon or comma) into a clean YAML list
    raw_kw = str(row.get("Keywords", "")).strip()
    kw_list = []
    if raw_kw and raw_kw.lower() != "nan":
        delimiter = ";" if ";" in raw_kw else ","
        kw_list = [
            k.strip().replace('"', '\\"')
            for k in raw_kw.split(delimiter)
            if k.strip()
        ]

    kw_yaml = "[" + ", ".join(f'"{k}"' for k in kw_list) + "]"

    yaml = [
        "---",
        f'paper_id: "{paper_id}"',
        f'query_id: "{query_id}"',
        f'title: "{title}"',
        f'authors: "{authors}"',
        f"year: {year}",
        f'doi: "{doi}"',
        f"keywords: {kw_yaml}",
        f'source_pdf: "{source_pdf}"',
        f'extraction_date: "{today}"',
        "---\n",
    ]
    return "\n".join(yaml)


def main():
    parser = argparse.ArgumentParser(
        description="Correlate LLM extractions with Search-Log.xlsx and output canonical Markdown notes."
    )
    parser.add_argument("raw_file", help="Raw extraction markdown filename or full path.")
    parser.add_argument("query_id", help="The Query ID (e.g., Q01).")
    parser.add_argument(
        "-o",
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help=f"Target directory (default: {DEFAULT_OUTPUT_DIR})",
    )
    parser.add_argument(
        "--excel",
        default=DEFAULT_EXCEL_PATH,
        help=f"Path to Search-Log.xlsx (default: {DEFAULT_EXCEL_PATH})",
    )
    parser.add_argument(
        "-w",
        "--write",
        action="store_true",
        help="Execute write operations (default is Dry-Run)",
    )
    args = parser.parse_args()

    output_dir = os.path.normpath(args.output_dir)
    raw_input = args.raw_file.strip()

    # Resolve filename inside output_dir if not found as direct path
    if os.path.exists(raw_input):
        raw_file = os.path.normpath(raw_input)
    else:
        raw_file = os.path.normpath(os.path.join(output_dir, raw_input))
    raw_sources_dir = os.path.join(DEFAULT_RAW_SOURCES_BASE, args.query_id)
    today = datetime.now().strftime("%Y-%m-%d")

    if not os.path.exists(raw_file):
        print(f"[ERROR] Raw extraction file not found: {raw_file}", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Loading metadata from: {args.excel} (Query: {args.query_id})")
    df_meta = load_log_metadata(args.excel, args.query_id)

    with open(raw_file, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = parse_raw_blocks(content)
    if not blocks:
        print(
            f'[ERROR] No valid blocks parsed. Ensure blocks begin with:\n---\ntitle: "..."\n---',
            file=sys.stderr,
        )
        sys.exit(1)

    planned_files = []
    unmatched = []

    for block in blocks:
        matched_row = match_paper(block["title"], df_meta)
        if matched_row is not None:
            paper_id = str(matched_row["Paper_ID"]).strip()
            source_pdf = find_source_pdf(raw_sources_dir, str(matched_row["Title"]))
            frontmatter = build_frontmatter(
                matched_row, args.query_id, source_pdf, today
            )

            full_content = f"{frontmatter}\n{block['body']}\n"
            target_path = os.path.join(output_dir, f"{paper_id}.md")

            planned_files.append(
                {
                    "paper_id": paper_id,
                    "title": matched_row["Title"],
                    "path": target_path,
                    "content": full_content,
                }
            )
        else:
            unmatched.append(block["title"])

    mode = (
        "[EXECUTION MODE]" if args.write else "[DRY-RUN MODE] (Use --write to commit)"
    )
    print("\n" + "=" * 90 + f"\n TMG Extraction Splitter — {mode}\n" + "=" * 90)
    print(f"Blocks Found:    {len(blocks)}")
    print(f"Matches Aligned: {len(planned_files)}")
    print(f"Unmatched:       {len(unmatched)}")
    print("-" * 90)

    for item in planned_files:
        print(f"[MATCH] {item['paper_id']} <-- {item['title'][:60]}...")

    if unmatched:
        print("\n[WARNING] Could not align the following titles with Search-Log.xlsx:")
        for u in unmatched:
            print(f"  [!] {u}")

    if not args.write:
        print("\n[+] Dry-run completed. No files created.")
        return

    os.makedirs(output_dir, exist_ok=True)
    for item in planned_files:
        with open(item["path"], "w", encoding="utf-8") as f:
            f.write(item["content"])

    bak_path = f"{raw_file}.bak"
    if os.path.exists(bak_path):
        os.remove(bak_path)
    os.rename(raw_file, bak_path)
    print(f"\n[SUCCESS] Wrote {len(planned_files)} markdown notes to '{output_dir}'.")
    print(f"[SUCCESS] Archived raw input to '{bak_path}'.")


if __name__ == "__main__":
    main()
