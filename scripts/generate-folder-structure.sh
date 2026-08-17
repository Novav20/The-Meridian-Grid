#!/usr/bin/env bash

# Output file path
OUTPUT_FILE="temp/folder-structure.md"

# Create temp directory if it doesn't exist
mkdir -p temp

# Define patterns to ignore (separated by | for regex matching)
IGNORE_DIRS="\.git|\.venv|node_modules|__pycache__|\.pytest_cache|\.vscode|\.idea|\.DS_Store"

# Write Markdown header to output file
cat << 'EOF' > "$OUTPUT_FILE"
# Project Folder Structure

```text
EOF

# Generate directory tree and append to Markdown file
# Uses 'find' to locate all non-hidden files/dirs while filtering out ignored ones
find . -mindepth 1 \
  \( -type d -o -type f \) \
  ! -path '*/.*' \
  | grep -v -E "^\./($IGNORE_DIRS)" \
  | sort \
  | sed -e 's/^\.\///' \
        -e 's/[^/]*\//  /g' \
        -e 's/  \([^ ]\)/├── \1/' >> "$OUTPUT_FILE"

# Close code block in Markdown
echo '```' >> "$OUTPUT_FILE"

echo "Folder structure successfully generated at: $OUTPUT_FILE"