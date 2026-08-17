#!/usr/bin/env python3
"""
Extraction Splitter Script — The Meridian Grid (TMG)
Splits raw Gemini Notebook markdown extractions into individual, normalized .md files.

Usage:
  python scripts/split-extractions.py <raw_file_path> [options]

Examples:
  # Dry-run mode:
  python scripts/split-extractions.py docs/00-domain-research/extractions/Q01-scada-and-isa95.md

  # Execute write and generate .bak backup:
  python scripts/split-extractions.py docs/00-domain-research/extractions/Q01-scada-and-isa95.md --write
"""

import os
import re
import sys
import argparse
import unicodedata
from datetime import datetime

DEFAULT_OUTPUT_DIR = "docs/00-domain-research/extractions"
DEFAULT_RAW_SOURCES_BASE = "docs/00-domain-research/raw-sources"


def normalize_unicode_id(id_str: str) -> str:
    """
    Normalizes a string by converting diacritics/accents to ASCII equivalent.
    Example: 'Šverko_et_al_2022' -> 'Sverko_et_al_2022'
    """
    nfkd_form = unicodedata.normalize('NFKD', id_str)
    ascii_bytes = nfkd_form.encode('ASCII', 'ignore')
    ascii_str = ascii_bytes.decode('utf-8')
    cleaned_id = re.sub(r'[^a-zA-Z0-9_\-]', '', ascii_str)
    return cleaned_id


def extract_yaml_id(block_text: str) -> str:
    """Extracts the 'id' field from YAML frontmatter."""
    match = re.search(r'^id:\s*["\']?(.*?)["\']?\s*$', block_text, re.MULTILINE)
    if match:
        return match.group(1).strip()
    return "unknown_source"


def apply_suffix_to_year(id_str: str, suffix_char: str) -> str:
    """
    Appends a letter suffix to the 4-digit year in an ID string.
    Example: 'Boyer_2004', 'a' -> 'Boyer_2004a'
    """
    pattern = r'^(.*?)(\d{4})(.*)$'
    match = re.match(pattern, id_str)
    if match:
        prefix, year, postfix = match.groups()
        return f"{prefix}{year}{suffix_char}{postfix}"
    return f"{id_str}_{suffix_char}"


def resolve_source_path(raw_file_path: str, raw_sources_base: str, user_source_path: str) -> tuple[str, str]:
    """
    Validates and resolves the source_path by matching the raw file name against 
    directories inside raw-sources/.
    """
    raw_filename = os.path.basename(raw_file_path)
    raw_stem, _ = os.path.splitext(raw_filename)

    available_dirs = []
    if os.path.exists(raw_sources_base):
        available_dirs = [
            d for d in os.listdir(raw_sources_base)
            if os.path.isdir(os.path.join(raw_sources_base, d)) and not d.startswith('.')
        ]

    # Check 1: Auto-match raw file stem against raw-sources/ folder names
    matched_dir = None
    for d in available_dirs:
        if d == raw_stem or d in raw_stem or raw_stem in d:
            matched_dir = d
            break

    if matched_dir:
        resolved = os.path.join(raw_sources_base, matched_dir).replace("\\", "/") + "/"
        return resolved, f"Auto-matched ({matched_dir})"

    # Check 2: Fallback to user-provided --source-path
    if user_source_path:
        norm_user = os.path.normpath(user_source_path).replace("\\", "/") + "/"
        return norm_user, "Explicitly provided via CLI"

    # Error: Validation failed
    dirs_formatted = ", ".join([f"'{d}'" for d in available_dirs]) if available_dirs else "None"
    print("=" * 80, file=sys.stderr)
    print("[ERROR] Source Path Validation Failed!", file=sys.stderr)
    print("=" * 80, file=sys.stderr)
    print(f"Raw File Name:       {raw_filename}", file=sys.stderr)
    print(f"Available Folders:   {dirs_formatted}", file=sys.stderr)
    print("-" * 80, file=sys.stderr)
    print("Fix options:", file=sys.stderr)
    print(f" 1. Rename your raw file to match a folder in '{raw_sources_base}/' (e.g. 'Q01-scada-and-isa95.md').", file=sys.stderr)
    print(" 2. Pass --source-path explicitly (e.g. --source-path docs/00-domain-research/raw-sources/Q01-scada-and-isa95/).", file=sys.stderr)
    print("=" * 80, file=sys.stderr)
    sys.exit(1)


def parse_raw_blocks(content: str) -> list[str]:
    """
    Extracts individual markdown extraction blocks from raw content.
    Robustly handles:
      - Multiple ```markdown ... ``` blocks
      - Inner code fences inside the document
      - Files with or without outer code block fences
    """
    # Split on YAML frontmatter start that contains an 'id:' field
    pattern = r'(?m)(?=^---\s*\n(?:\s*#.*?\n)*\s*id:)'
    chunks = re.split(pattern, content)
    
    blocks = []
    for chunk in chunks:
        chunk = chunk.strip()
        if not chunk or not re.search(r'^---\s*\n', chunk):
            continue
        
        # Strip trailing outer code fences (e.g., trailing ``` or ```markdown)
        chunk = re.sub(r'\n```[a-zA-Z0-9_-]*\s*$', '', chunk).strip()
        
        if "id:" in chunk:
            blocks.append(chunk)
            
    return blocks


def update_frontmatter(block_content: str, new_id: str, source_path: str, extraction_date: str) -> str:
    """
    Updates 'id', 'source_path', and 'extraction_date' in the YAML frontmatter.
    """
    lines = block_content.splitlines()
    updated_lines = []
    in_frontmatter = False
    frontmatter_count = 0
    source_path_added = False
    date_added = False

    for line in lines:
        if line.strip() == "---":
            frontmatter_count += 1
            in_frontmatter = (frontmatter_count == 1)
            
            # Inject properties before closing frontmatter
            if frontmatter_count == 2:
                if not source_path_added:
                    updated_lines.append(f'source_path: "{source_path}"')
                if not date_added:
                    updated_lines.append(f'extraction_date: "{extraction_date}"')
            
            updated_lines.append(line)
            continue

        if in_frontmatter:
            if re.match(r'^id:\s*', line):
                updated_lines.append(f'id: "{new_id}"')
                continue
            if re.match(r'^source_path:\s*', line):
                updated_lines.append(f'source_path: "{source_path}"')
                source_path_added = True
                continue
            if re.match(r'^extraction_date:\s*', line):
                updated_lines.append(f'extraction_date: "{extraction_date}"')
                date_added = True
                continue

        updated_lines.append(line)

    return "\n".join(updated_lines) + "\n"


def main():
    parser = argparse.ArgumentParser(
        description="Split raw Gemini extraction markdown blocks into normalized, individual source files.",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument(
        "raw_file",
        metavar="RAW_FILE_PATH",
        help="Path to the raw extractions markdown file (e.g. docs/00-domain-research/extractions/Q01-scada-and-isa95.md)"
    )
    parser.add_argument(
        "-o", "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help=f"Target directory for generated .md files (default: {DEFAULT_OUTPUT_DIR})"
    )
    parser.add_argument(
        "-s", "--source-path",
        default=None,
        help="Optional override path to raw PDF source folder. If omitted, script auto-matches raw file name to raw-sources/ directories."
    )
    parser.add_argument(
        "-w", "--write",
        action="store_true",
        help="Execute file creation and rename the raw input file to .bak (default is Dry-Run mode)"
    )

    args = parser.parse_args()

    raw_file_path = os.path.normpath(args.raw_file)
    output_dir = os.path.normpath(args.output_dir)

    if not os.path.exists(raw_file_path):
        print(f"[ERROR] File not found: {raw_file_path}", file=sys.stderr)
        sys.exit(1)

    # Validate and resolve source_path
    resolved_source_path, match_status = resolve_source_path(
        raw_file_path=raw_file_path,
        raw_sources_base=DEFAULT_RAW_SOURCES_BASE,
        user_source_path=args.source_path
    )

    today_date = datetime.now().strftime("%Y-%m-%d")

    with open(raw_file_path, "r", encoding="utf-8") as f:
        content = f.read()

    blocks = parse_raw_blocks(content)
    if not blocks:
        print(f"[!] No valid extraction blocks found in {raw_file_path}")
        sys.exit(0)

    # First Pass: Normalize IDs & Detect Collisions
    parsed_extractions = []
    id_counts = {}

    for block in blocks:
        raw_id = extract_yaml_id(block)
        norm_id = normalize_unicode_id(raw_id)
        id_counts[norm_id] = id_counts.get(norm_id, 0) + 1
        parsed_extractions.append({
            "raw_id": raw_id,
            "norm_id": norm_id,
            "block": block
        })

    # Second Pass: Resolve Collision Suffixes
    id_occurrences = {}
    planned_files = []

    for item in parsed_extractions:
        base_id = item["norm_id"]
        total_count = id_counts[base_id]

        if total_count > 1:
            curr_idx = id_occurrences.get(base_id, 0)
            suffix_letter = chr(ord('a') + curr_idx)
            resolved_id = apply_suffix_to_year(base_id, suffix_letter)
            id_occurrences[base_id] = curr_idx + 1
        else:
            resolved_id = base_id

        final_filename = f"{resolved_id}.md"
        final_filepath = os.path.join(output_dir, final_filename)
        updated_content = update_frontmatter(
            block_content=item["block"],
            new_id=resolved_id,
            source_path=resolved_source_path,
            extraction_date=today_date
        )

        planned_files.append({
            "orig_id": item["raw_id"],
            "final_id": resolved_id,
            "filename": final_filename,
            "filepath": final_filepath,
            "content": updated_content
        })

    # Output Execution Mode Summary
    mode_str = "[DRY-RUN MODE] (Pass --write to apply changes)" if not args.write else "[EXECUTION MODE] (Writing files)"
    print("=" * 85)
    print(f" TMG Extraction Splitter — {mode_str}")
    print("=" * 85)
    print(f"Target Raw File:   {raw_file_path}")
    print(f"Output Directory:  {output_dir}")
    print(f"Resolved Source:   {resolved_source_path} ({match_status})")
    print(f"Extraction Date:   {today_date}")
    print(f"Blocks Found:      {len(planned_files)}")
    print("-" * 85)
    print(f"{'Original ID':<25} -> {'Normalized / Suffix ID':<25} -> {'Output File'}")
    print("-" * 85)

    for item in planned_files:
        print(f"{item['orig_id']:<25} -> {item['final_id']:<25} -> {item['filename']}")

    print("-" * 85)

    if not args.write:
        print("\n[+] Dry-run complete. No files were written or renamed.")
        print("[+] Run with --write to create files and generate .bak backup.")
        return

    # Execute Writes
    os.makedirs(output_dir, exist_ok=True)
    written_count = 0

    for item in planned_files:
        with open(item["filepath"], "w", encoding="utf-8") as f:
            f.write(item["content"])
        written_count += 1

    # Backup original raw file
    bak_path = f"{raw_file_path}.bak"
    if os.path.exists(bak_path):
        os.remove(bak_path)
    os.rename(raw_file_path, bak_path)

    print(f"\n[SUCCESS] Successfully wrote {written_count} extraction files.")
    print(f"[SUCCESS] Renamed {raw_file_path} -> {bak_path}")


if __name__ == "__main__":
    main()