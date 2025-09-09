#!/usr/bin/env bash
set -euo pipefail
SRC="${1:?gdrive:path/file}"; DST="${2:?dst}"
rclone copyto "$SRC" "$DST"
