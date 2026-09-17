#!/usr/bin/env python3
"""
Stage 2 Status Sync Script — The Meridian Grid (TMG)
Reads Stage2_Status from Search-Log.xlsx and updates the YAML frontmatter
in docs/02-SI-Requirements/Domain-Research/extractions/<Paper_ID>.md files.

Usage:
  python scripts/update-stage2-status.py <query_id>
"""

import os
import re
import sys
import argparse
import pandas as pd
import openpyxl

DEFAULT_EXCEL_PATH = "docs/01-PM-Project-Management/Search-Log.xlsx"
DEFAULT_EXTRACTIONS_DIR = "docs/02-SI-Requirements/Domain-Research/extractions"
TARGET_SHEET_NAME = "Filtered_Results"


def update_md_frontmatter(md_path: str, status: str):
    if not os.path.exists(md_path):
        print(f"  [!] Extraction file not found: {md_path}")
        return False

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to match YAML frontmatter
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not fm_match:
        print(f"  [!] Invalid frontmatter format in: {md_path}")
        return False

    frontmatter_text = fm_match.group(1)
    body_text = fm_match.group(2)

    # Check if stage2_status key already exists in frontmatter
    if re.search(r"^stage2_status:", frontmatter_text, re.MULTILINE):
        new_fm = re.sub(
            r"^stage2_status:.*$",
            f'stage2_status: "{status}"',
            frontmatter_text,
            flags=re.MULTILINE,
        )
    else:
        new_fm = frontmatter_text.strip() + f'\nstage2_status: "{status}"'

    new_content = f"---\n{new_fm}\n---\n\n{body_text}\n"

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)

    return True


def sync_stage2_status(query_id: str, excel_path: str, extractions_dir: str):
    if not os.path.exists(excel_path):
        print(f"[ERROR] Excel log not found: {excel_path}", file=sys.stderr)
        sys.exit(1)

    wb = openpyxl.load_workbook(excel_path, data_only=True)
    sheet = wb[TARGET_SHEET_NAME]
    data = list(sheet.values)
    headers = [str(h).strip() if h is not None else "" for h in data[0]]

    if "Stage2_Status" not in headers:
        print(
            f"[ERROR] Column 'Stage2_Status' not found in '{TARGET_SHEET_NAME}'.",
            file=sys.stderr,
        )
        sys.exit(1)

    df = pd.DataFrame(data[1:], columns=headers)

    df_filtered = df[df["Query_ID"].astype(str).str.strip() == query_id.strip()]
    if df_filtered.empty:
        print(f"[ERROR] No records found for Query_ID: {query_id}", file=sys.stderr)
        sys.exit(1)

    print(f"[*] Syncing Stage 2 status for Query '{query_id}'...")
    updated_count = 0

    for _, row in df_filtered.iterrows():
        paper_id = str(row.get("Paper_ID", "")).strip()
        status = str(row.get("Stage2_Status", "")).strip()

        # Skip if Paper_ID is empty or Stage2_Status is empty/NaN
        if not paper_id or paper_id.lower() == "none":
            continue
        if not status or status.lower() == "nan":
            continue

        md_file = os.path.join(extractions_dir, f"{paper_id}.md")
        if update_md_frontmatter(md_file, status):
            print(f"  [+] Updated {paper_id}.md -> stage2_status: '{status}'")
            updated_count += 1

    print(f"\n[SUCCESS] Updated frontmatter in {updated_count} extraction notes.")


def main():
    parser = argparse.ArgumentParser(
        description="Sync Stage2_Status from Search-Log.xlsx to extraction .md YAML frontmatter."
    )
    parser.add_argument("query_id", help="Query ID to sync (e.g., Q01).")
    parser.add_argument(
        "--excel", default=DEFAULT_EXCEL_PATH, help="Path to Search-Log.xlsx"
    )
    parser.add_argument(
        "--extractions-dir",
        default=DEFAULT_EXTRACTIONS_DIR,
        help="Path to extractions directory",
    )

    args = parser.parse_args()
    sync_stage2_status(args.query_id, args.excel, args.extractions_dir)


if __name__ == "__main__":
    main()