#!/bin/sh
set -eu
exec python3 "$(dirname "$0")/seed_os.py" "$@"
