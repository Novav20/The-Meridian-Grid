# TMG Scripts & Automation

Utility scripts to automate the Evidence-Based Software Engineering (EBSE) literature review workflow and enforce ISO/IEC 29110 traceability.

## Directory Structure
* `docs/01-PM-Project-Management/Search-Log.xlsx`: Master tracking spreadsheet.
* `docs/01-PM-Project-Management/Search-Exports/`: Raw CSV exports from academic databases.
* `docs/02-SI-Requirements/Domain-Research/raw-sources/<Query_ID>/`: Downloaded source PDFs.
* `docs/02-SI-Requirements/Domain-Research/extractions/`: Individual, normalized markdown extraction files.

---

## 1. `ingest-scopus-csv.py`
Enriches the `Filtered_Results` sheet in `Search-Log.xlsx`. It takes titles approved during LLM screening, fuzzy-matches them against raw Scopus CSV exports (single file or a directory containing split batches), generates collision-proof semantic IDs (`Author_et_al_Year`), prevents cross-query duplicate enrichment, and populates bibliographic metadata.

**Usage:**
```bash
# 1. Standard usage (implicitly resolves to docs/01-PM-Project-Management/Search-Exports/<Query_ID>/)
python scripts/ingest-scopus-csv.py Q03

# 2. Explicit custom file or directory (backward-compatible)
python scripts/ingest-scopus-csv.py docs/01-PM-Project-Management/Search-Exports/Q01/scopus_q01.csv Q01
python scripts/ingest-scopus-csv.py Q03 --source path/to/custom_dir/
```

---

## 2. `split-extractions.py`
Parses a bulk markdown extraction file from Gemini Notebook. It matches each extraction block's title against `Search-Log.xlsx`, injects authoritative bibliographic metadata into YAML frontmatter, maps the local PDF file path, and writes atomic notes named `<Paper_ID>.md`.

**Prerequisites:**
1. Relevant records must be present in `Search-Log.xlsx` under the specified `Query_ID`.
2. Raw extractions must delimit papers using:
   ```markdown
   ---
   title: "Complete Title of Paper"
   ---
   <Extraction content>
   ```

**Usage:**
```bash
# 1. Dry-run mode (Inspect matching without writing files)
python scripts/split-extractions.py docs/02-SI-Requirements/Domain-Research/extractions/Q01-raw.md Q01

# 2. Execution mode (Writes files and creates .bak backup)
python scripts/split-extractions.py docs/02-SI-Requirements/Domain-Research/extractions/Q01-raw.md Q01 --write

# Direct filename (resolves automatically to docs/02-SI-Requirements/Domain-Research/extractions/Q01-raw.md)
python scripts/split-extractions.py Q01-raw.md Q01 --write

# Full relative path (still supported)
python scripts/split-extractions.py docs/02-SI-Requirements/Domain-Research/extractions/Q01-raw.md Q01 --write
```

---

## 3. `sync-prompts.py`
Provides bidirectional synchronization between individual Markdown prompt files (`docs/01-PM-Project-Management/prompts/*.md`) and the master tracking log (`docs/01-PM-Project-Management/LLM-Prompt-Log.xlsx`).

### Markdown Prompt File Format:
```markdown
---
date: "YYYY-MM-DD"
name: "Prompt Name"
description: "Brief summary of the prompt's purpose."
---

Actual prompt content goes here...
```

### Usage:
```bash
# 1. Update the Excel log from local Markdown files
python scripts/sync-prompts.py --to-excel

# 2. Re-generate local Markdown files from an existing Excel log (e.g., after a fresh clone)
python scripts/sync-prompts.py --to-md
```

## 4. `update-stage2-status.py`
Synchronizes the `Selection_Status` column from `Search-Log.xlsx` to the YAML frontmatter (`selection_status: "..."`) of individual `<Paper_ID>.md` notes. Run this after performing Stage 2 full-text evaluations.

**Usage:**
```bash
python scripts/update-stage2-status.py Q01
```