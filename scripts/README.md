# TMG Scripts & Automation

Utility scripts to automate the Evidence-Based Software Engineering (EBSE) literature review workflow and enforce ISO/IEC 29110 traceability.

## Directory Structure
* `docs/01-PM-Project-Management/Search-Log.xlsx`: Master tracking spreadsheet.
* `docs/01-PM-Project-Management/Search-Exports/`: Raw CSV exports from academic databases.
* `docs/02-SI-Requirements/Domain-Research/raw-sources/<Query_ID>/`: Downloaded source PDFs.
* `docs/02-SI-Requirements/Domain-Research/extractions/`: Individual, normalized markdown extraction files.

---

## 1. `ingest-scopus-csv.py`
Enriches the `Filtered_Results` sheet in `Search-Log.xlsx`. It takes titles approved during LLM screening, fuzzy-matches them against the raw Scopus CSV, generates collision-proof semantic IDs (`Author_et_al_Year`), and populates bibliographic metadata.

**Usage:**
```bash
python scripts/ingest-scopus-csv.py <path_to_csv> <Query_ID>
```

**Example:**
```bash
python scripts/ingest-scopus-csv.py docs/01-PM-Project-Management/Search-Exports/scopus_q01.csv Q01
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
```