import os
import glob
import pandas as pd
from difflib import SequenceMatcher
import openpyxl

# Configuration Paths
QUERY_RESULTS_DIR = "docs/00-domain-research/raw-sources/query-results/"
EXCEL_PATH = "docs/00-domain-research/search-log.xlsx"
FUZZY_MATCH_THRESHOLD = 0.85  # 85% title similarity match

def load_all_scopus_csvs(directory_path: str) -> pd.DataFrame:
    """Load and concatenate all Scopus CSV export files into a single DataFrame."""
    csv_files = glob.glob(os.path.join(directory_path, "*.csv"))
    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in {directory_path}")
    
    dfs = []
    for f in csv_files:
        try:
            # Handle UTF-8 BOM encoding from Scopus exports
            df = pd.read_csv(f, encoding="utf-8-sig")
            dfs.append(df)
        except Exception as e:
            print(f"[!] Warning: Could not read {f}: {e}")
            
    combined_df = pd.concat(dfs, ignore_index=True)
    combined_df.drop_duplicates(subset=["Title"], inplace=True)
    return combined_df

def fuzzy_match_ratio(str1: str, str2: str) -> float:
    """Calculate string similarity ratio between two titles."""
    if not isinstance(str1, str) or not isinstance(str2, str):
        return 0.0
    return SequenceMatcher(None, str1.lower().strip(), str2.lower().strip()).ratio()

def is_cell_empty(cell_value) -> bool:
    """Check if a cell value is None, empty string, or whitespace."""
    if cell_value is None:
        return True
    if isinstance(cell_value, str) and cell_value.strip() == "":
        return True
    return False

def populate_selected_sources():
    print("[*] Loading Scopus CSV exports...")
    scopus_db = load_all_scopus_csvs(QUERY_RESULTS_DIR)
    print(f"[+] Loaded {len(scopus_db)} unique records from CSV pool.")

    print(f"[*] Opening Excel workbook: {EXCEL_PATH}")
    wb = openpyxl.load_workbook(EXCEL_PATH)
    
    if "Selected_Sources" not in wb.sheetnames:
        raise ValueError("Sheet 'Selected_Sources' not found in workbook.")
        
    sheet = wb["Selected_Sources"]
    
    headers = [cell.value for cell in sheet[1]]
    header_map = {name: idx + 1 for idx, name in enumerate(headers) if name}

    required_cols = ["Title", "Authors", "Year", "Document_Type", "DOI", "Abstract"]
    for col in required_cols:
        if col not in header_map:
            raise KeyError(f"Column '{col}' missing from 'Selected_Sources' header row.")

    updated_count = 0
    skipped_count = 0

    for row_idx in range(2, sheet.max_row + 1):
        target_title = sheet.cell(row=row_idx, column=header_map["Title"]).value
        
        if not target_title:
            continue

        # PRESERVATION CHECK: Skip if DOI and Abstract are already populated
        current_doi = sheet.cell(row=row_idx, column=header_map["DOI"]).value
        current_abstract = sheet.cell(row=row_idx, column=header_map["Abstract"]).value
        
        if not is_cell_empty(current_doi) and not is_cell_empty(current_abstract):
            print(f"[-] Row {row_idx}: Skipped '{target_title[:30]}...' (Already populated)")
            skipped_count += 1
            continue

        best_match_ratio = 0.0
        best_match_row = None
        
        for _, scopus_row in scopus_db.iterrows():
            csv_title = scopus_row.get("Title", "")
            ratio = fuzzy_match_ratio(target_title, csv_title)
            
            if ratio > best_match_ratio:
                best_match_ratio = ratio
                best_match_row = scopus_row
                
        if best_match_ratio >= FUZZY_MATCH_THRESHOLD and best_match_row is not None:
            sheet.cell(row=row_idx, column=header_map["Authors"], value=str(best_match_row.get("Authors", "")))
            sheet.cell(row=row_idx, column=header_map["Year"], value=int(best_match_row.get("Year", 0)))
            sheet.cell(row=row_idx, column=header_map["Document_Type"], value=str(best_match_row.get("Document Type", "")))
            sheet.cell(row=row_idx, column=header_map["DOI"], value=str(best_match_row.get("DOI", "")))
            sheet.cell(row=row_idx, column=header_map["Abstract"], value=str(best_match_row.get("Abstract", "")))
            
            print(f"[+] Row {row_idx}: Updated '{target_title[:30]}...' ({best_match_ratio*100:.1f}% confidence)")
            updated_count += 1
        else:
            print(f"[!] Row {row_idx}: No match found in CSV pool for '{target_title[:30]}...'")

    wb.save(EXCEL_PATH)
    print(f"[SUCCESS] Updated {updated_count} records, skipped {skipped_count} already-populated records.")

if __name__ == "__main__":
    populate_selected_sources()