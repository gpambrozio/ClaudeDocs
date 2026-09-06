# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

ClaudeDocs is a documentation synchronization tool that crawls and converts Claude API and Claude Code documentation from Anthropic's official sources into locally-stored Markdown files. It maintains an offline, version-controlled archive of documentation.

## Commands

### Run Documentation Sync

```bash
# Using the wrapper script
./sync_docs.sh

# Or directly with uv
uv run sync_docs.py
```

The sync process:
1. Collects the URLs to fetch for each site
2. Fetches each page's Markdown source
3. Converts MDX to plain Markdown and saves the files
4. Deletes local files whose pages returned 404

## Architecture

### Fetching Markdown Directly

Both sites serve the Markdown source of every page: append `.md` to a page URL
and the server responds with `text/markdown`. The URLs are extensionless, so
this appends rather than replaces a suffix (`/docs/en/hooks.html` is a 404).
Each site's `llms.txt` indexes these same `.md` URLs.

There is therefore no browser or HTML-to-Markdown conversion step. This is both
much faster (no page rendering) and more complete: the API reference pages are
rendered client side, so extracting them from HTML previously yielded near-empty
stubs.

### Documentation Sources

| Site | URL | Output |
|------|-----|--------|
| Claude Code | code.claude.com | `docs-md/claude-code/` |
| Claude API | platform.claude.com | `docs-md/api/` |

### URL Discovery

Each site is seeded from three sources, then crawled by following links:

1. `sitemap.xml`
2. `llms.txt`
3. Files already in `docs-md/`

Neither index lists every live page -- the per-language SDK reference pages
(`api/go/...`, `api/python/...`) are absent from both, which is why previously
mirrored files seed the crawl too. Pages that 404 are deleted locally; pages
that fail transiently keep their existing file.

A request is also treated as a 404 when it redirects elsewhere or answers with
a non-Markdown content type. A cross-site redirect drops the `.md` suffix and
returns a rendered HTML page, which must not be written to disk as if it were
Markdown.

### MDX Conversion

The served source is MDX, so `sync_docs.py` reduces it to plain Markdown:

- Strips the documentation-index preamble every page carries
- Unwraps components (`<Note>`, `<CodeGroup>`, `<Steps>`, ...), keeping their
  content and removing the indentation they added; a `title` attribute becomes
  a bold line
- Converts `<img>` tags to Markdown image syntax
- Rewrites in-site links to point at the local `.md` files
- Drops Mintlify's `theme={null}` from code fence info strings

Code blocks are masked before any of this runs, so angle brackets inside them
(generics, literal markup) are never mistaken for MDX components.

### Output Structure

```
docs-md/
├── claude-code/    # Claude Code documentation (~200 files)
└── api/            # Claude API documentation (~1900 files)
    ├── about-claude/
    ├── agents-and-tools/
    ├── api/
    ├── build-with-claude/
    └── ...
```

## Changelog Site

The project includes a static changelog site deployed to GitHub Pages.

**Live site:** https://ccc.gustavo.eng.br/

### Build Locally

```bash
uv run site/build_site.py
```

Output is generated in `_site/` (gitignored).

### Site Structure

```
site/
├── build_site.py              # Main build script (PEP 723 dependencies)
├── templates/
│   ├── base.html              # Base layout with theme toggle, calendar
│   ├── changelog.html         # Single changelog page
│   └── partials/
│       ├── calendar.html      # Month calendar with navigation
│       └── nav.html           # Prev/next navigation
└── static/
    └── style.css              # Styles with dark/light mode
```

### Deployment

GitHub Actions workflow (`.github/workflows/pages.yml`) automatically builds and deploys on push to main when files change in:
- `changelogs/**`
- `site/**`
- `.github/workflows/pages.yml`

### Features

- Home page shows latest changelog
- Calendar dropdown with clickable days that have changelogs
- Prev/next navigation between changelog entries
- Dark/light mode with auto detection and manual toggle
- RSS feed at `/feed.xml`

## Dependencies

Declared inline in sync_docs.py using PEP 723 format:
- httpx - Async HTTP client

Declared inline in site/build_site.py:
- jinja2 - HTML templating
- markdown - Markdown to HTML conversion
- feedgen - RSS feed generation
