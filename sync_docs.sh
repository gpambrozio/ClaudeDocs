#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Claude Docs Sync ==="
echo "Date: $(date)"
echo ""

# Run the Playwright-based crawler (unbuffered for real-time output with tee)
PYTHONUNBUFFERED=1 uv run sync_docs.py

# Sync changelog versions
echo ""
PYTHONUNBUFFERED=1 uv run sync_changelog.py

echo ""
echo "=== Sync Complete ==="

if [ -d ".git" ]; then
    # Revert files with only trivial changes (e.g., extra blank lines)
    for file in $(git diff --name-only docs-md/ versions/ 2>/dev/null); do
        changes=$(git diff "$file" | grep -E '^[+-]' | grep -v '^[+-]{3}' | grep -v '^[+-]$' | grep -v '^[+-][[:space:]]*$' | wc -l)
        if [ "$changes" -le 2 ]; then
            git checkout -- "$file"
        fi
    done

    # Show changes if git is initialized
    echo ""
    echo "Changes detected:"
    git status --short docs-md/ versions/ 2>/dev/null || true
fi
