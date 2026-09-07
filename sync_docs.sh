#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

echo "=== Claude Docs Sync ==="
echo "Date: $(date)"
echo ""

# Fetch the Markdown sources (unbuffered for real-time output with tee)
PYTHONUNBUFFERED=1 uv run sync_docs.py

# Sync changelog versions
echo ""
PYTHONUNBUFFERED=1 uv run sync_changelog.py

echo ""
echo "=== Sync Complete ==="

if [ -d ".git" ]; then
    # Revert files whose only changes are blank lines. git diff's own +++/---
    # headers are dropped here, so the count is of content lines alone and the
    # threshold is zero. It used to be a count that still included those two
    # headers, compared against two -- the same behaviour, but written so that
    # tightening the header pattern would have started discarding files with a
    # real one-line change, such as a single corrected link.
    for file in $(git diff --name-only docs-md/ versions/ 2>/dev/null); do
        changes=$(git diff "$file" \
            | grep -E '^[+-]' \
            | grep -Ev '^(\+\+\+|---)' \
            | grep -Ev '^[+-][[:space:]]*$' \
            | wc -l)
        if [ "$changes" -eq 0 ]; then
            git checkout -- "$file"
        fi
    done

    # Show changes if git is initialized
    echo ""
    echo "Changes detected:"
    git status --short docs-md/ versions/ 2>/dev/null || true
fi
