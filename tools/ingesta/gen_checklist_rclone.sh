#!/usr/bin/env bash
set -euo pipefail
REMOTE="${1:?REMOTE:path}"
OUT="${2:?out file}"
mkdir -p "$(dirname "$OUT")"
rclone lsjson "$REMOTE" --files-only --recursive \
 | jq -r '.[] | .Path' \
 | grep -Ei '\.(txt|md|docx)$' \
 | sort -f \
 | awk -F/ '{file=$NF; $NF=""; path=$0; sub(/^[ ]*/, "", path); sub(/[ ]*$/, "", path); print "[ ] " file " - " path }' \
 > "$OUT"
