#!/usr/bin/env python3
"""
Bidirectional Prompt Synchronization Script — The Meridian Grid (TMG)
Syncs YAML-frontmatter Markdown prompt files with LLM-Prompt-Log.xlsx.

Usage:
  python scripts/sync-prompts.py --to-excel   # Markdown -> Excel
  python scripts/sync-prompts.py --to-md      # Excel -> Markdown
"""

import os
import re
import sys
import argparse
import unicodedata
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

DEFAULT_PROMPTS_DIR = "docs/01-PM-Project-Management/Prompts"
DEFAULT_EXCEL_PATH = "docs/01-PM-Project-Management/LLM-Prompt-Log.xlsx"
SHEET_NAME = "Prompt_Log"


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf-8")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[-\s]+", "-", text)


def parse_md_prompt(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not match:
        return None

    raw_frontmatter, body = match.group(1), match.group(2).strip()
    data = {"date": "", "name": "", "description": "", "body": body}

    for line in raw_frontmatter.splitlines():
        kv = line.split(":", 1)
        if len(kv) == 2:
            key = kv[0].strip().lower()
            val = kv[1].strip().strip('"').strip("'")
            if key in data:
                data[key] = val

    return data


def sync_md_to_excel(prompts_dir: str, excel_path: str):
    if not os.path.exists(prompts_dir):
        print(f"[ERROR] Prompts directory '{prompts_dir}' not found.", file=sys.stderr)
        sys.exit(1)

    md_files = [f for f in os.listdir(prompts_dir) if f.endswith(".md")]
    if not md_files:
        print(f"[WARNING] No .md files found in '{prompts_dir}'.")
        return

    records = []
    for fname in sorted(md_files):
        fpath = os.path.join(prompts_dir, fname)
        parsed = parse_md_prompt(fpath)
        if parsed:
            records.append({
                "File": fname,
                "Date": parsed["date"],
                "Name": parsed["name"],
                "Description": parsed["description"],
                "Prompt": parsed["body"]
            })
        else:
            print(f"  [!] Skipped invalid prompt format: {fname}")

    # Initialize / Load Workbook
    if os.path.exists(excel_path):
        wb = openpyxl.load_workbook(excel_path)
    else:
        wb = openpyxl.Workbook()
        if "Sheet" in wb.sheetnames:
            wb.remove(wb["Sheet"])

    if SHEET_NAME in wb.sheetnames:
        del wb[SHEET_NAME]

    ws = wb.create_sheet(title=SHEET_NAME)

    headers = ["Date", "Name", "Description", "Filename", "Prompt"]
    ws.append(headers)

    # Style Header
    header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    for col_num, _ in enumerate(headers, 1):
        cell = ws.cell(row=1, column=col_num)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center", vertical="center")

    for rec in records:
        ws.append([rec["Date"], rec["Name"], rec["Description"], rec["File"], rec["Prompt"]])

    # Layout adjustments
    ws.column_dimensions["A"].width = 14
    ws.column_dimensions["B"].width = 30
    ws.column_dimensions["C"].width = 45
    ws.column_dimensions["D"].width = 25
    ws.column_dimensions["E"].width = 80

    for row in ws.iter_rows(min_row=2, max_col=5):
        for cell in row:
            cell.alignment = Alignment(vertical="top", wrap_text=True)

    os.makedirs(os.path.dirname(excel_path) or ".", exist_ok=True)
    wb.save(excel_path)
    print(f"[SUCCESS] Exported {len(records)} prompts from Markdown to '{excel_path}'.")


def sync_excel_to_md(excel_path: str, prompts_dir: str):
    if not os.path.exists(excel_path):
        print(f"[ERROR] Excel file '{excel_path}' not found.", file=sys.stderr)
        sys.exit(1)

    wb = openpyxl.load_workbook(excel_path, data_only=True)
    if SHEET_NAME not in wb.sheetnames:
        print(f"[ERROR] Sheet '{SHEET_NAME}' not found in '{excel_path}'.", file=sys.stderr)
        sys.exit(1)

    ws = wb[SHEET_NAME]
    headers = {cell.value: idx for idx, cell in enumerate(ws[1]) if cell.value}

    required = ["Date", "Name", "Description", "Prompt"]
    for req in required:
        if req not in headers:
            print(f"[ERROR] Missing required column '{req}' in sheet.", file=sys.stderr)
            sys.exit(1)

    os.makedirs(prompts_dir, exist_ok=True)
    count = 0

    for row in ws.iter_rows(min_row=2, values_only=True):
        if not any(row):
            continue

        date_val = str(row[headers["Date"]] or "").strip()
        if " " in date_val:
            date_val = date_val.split(" ")[0]

        name_val = str(row[headers["Name"]] or "").strip()
        desc_val = str(row[headers["Description"]] or "").strip()
        prompt_val = str(row[headers["Prompt"]] or "").strip()

        if not name_val:
            continue

        # Use Filename column if available, otherwise generate slug
        if "Filename" in headers and row[headers["Filename"]]:
            filename = str(row[headers["Filename"]]).strip()
        else:
            filename = f"{slugify(name_val)}.md"

        target_path = os.path.join(prompts_dir, filename)

        import json

        md_content = (
            "---\n"
            f"date: {json.dumps(date_val)}\n"
            f"name: {json.dumps(name_val, ensure_ascii=False)}\n"
            f"description: {json.dumps(desc_val, ensure_ascii=False)}\n"
            "---\n\n"
            f"{prompt_val}\n"
        )

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(md_content)
        count += 1
        print(f"  [+] Generated: {filename}")

    print(f"\n[SUCCESS] Extracted {count} Markdown prompt files into '{prompts_dir}'.")


def main():
    parser = argparse.ArgumentParser(
        description="Bidirectional sync between prompt Markdown files and LLM-Prompt-Log.xlsx."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--to-excel", action="store_true", help="Sync Markdown files to Excel log.")
    group.add_argument("--to-md", action="store_true", help="Extract Markdown files from Excel log.")
    parser.add_argument("--prompts-dir", default=DEFAULT_PROMPTS_DIR, help="Path to prompts directory.")
    parser.add_argument("--excel", default=DEFAULT_EXCEL_PATH, help="Path to Excel log file.")

    args = parser.parse_args()

    if args.to_excel:
        sync_md_to_excel(args.prompts_dir, args.excel)
    elif args.to_md:
        sync_excel_to_md(args.excel, args.prompts_dir)


if __name__ == "__main__":
    main()