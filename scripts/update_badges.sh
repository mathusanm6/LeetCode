#!/bin/bash
# Update README badges with current problem counts

set -e

# Get the directory of this script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# Change to repository root
cd "$REPO_ROOT"

# Run the Python script
python3 scripts/update_badges.py
