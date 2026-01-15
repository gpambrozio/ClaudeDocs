#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Claude Docs Sync ==="
echo "Date: $(date)"
echo ""

# Run the Playwright-based crawler (unbuffered for real-time output with tee)
PYTHONUNBUFFERED=1 uv run sync_docs.py

echo ""
echo "=== Sync Complete ==="

# Show changes if git is initialized
if [ -d ".git" ]; then
    echo ""
    echo "Changes detected:"
    git status --short docs-md/ 2>/dev/null || true
fi
