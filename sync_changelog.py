#!/usr/bin/env python3
"""
Download and parse Claude Code CHANGELOG.md into individual version files.

Usage:
    uv run sync_changelog.py
"""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx>=0.27",
# ]
# ///

import re
from pathlib import Path

import httpx

CHANGELOG_URL = "https://raw.githubusercontent.com/anthropics/claude-code/refs/heads/main/CHANGELOG.md"
OUTPUT_DIR = Path("versions")

COPYRIGHT_NOTICE = "\n\n---\n\n*Copyright © Anthropic. All rights reserved.*\n"


def download_changelog() -> str:
    """Download the CHANGELOG.md file from GitHub."""
    print(f"Downloading {CHANGELOG_URL}...")
    response = httpx.get(CHANGELOG_URL, timeout=30, follow_redirects=True)
    response.raise_for_status()
    print(f"  Downloaded {len(response.text)} bytes")
    return response.text


def parse_versions(content: str) -> list[tuple[str, str]]:
    """Parse changelog content into individual versions.

    Returns a list of (version, content) tuples.
    """
    versions = []

    # Split by version headers (## [x.y.z] or ## x.y.z)
    # Pattern matches lines like "## [1.0.0]" or "## 1.0.0" with optional date
    version_pattern = re.compile(r"^## \[?(\d+\.\d+\.\d+)\]?", re.MULTILINE)

    matches = list(version_pattern.finditer(content))

    if not matches:
        print("  No version headers found in changelog")
        return versions

    for i, match in enumerate(matches):
        version = match.group(1)
        start = match.start()

        # End is either the next version header or end of file
        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(content)

        version_content = content[start:end].strip()
        versions.append((version, version_content))

    return versions


def save_versions(versions: list[tuple[str, str]]) -> int:
    """Save each version to its own file in the output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    saved = 0
    for version, content in versions:
        filepath = OUTPUT_DIR / f"{version}.md"
        filepath.write_text(content + COPYRIGHT_NOTICE, encoding="utf-8")
        print(f"  Saved {filepath}")
        saved += 1

    return saved


def main():
    print("=== Claude Code Changelog Sync ===")
    print(f"Output: {OUTPUT_DIR}/")

    # Download changelog
    content = download_changelog()

    # Parse versions
    print("\nParsing versions...")
    versions = parse_versions(content)
    print(f"  Found {len(versions)} versions")

    if not versions:
        print("\nNo versions to save.")
        return

    # Save individual version files
    print("\nSaving version files...")
    saved = save_versions(versions)

    print(f"\nTotal: {saved} version files saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
