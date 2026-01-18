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
1. Installs Playwright browsers if needed
2. Clears the `docs-md/` directory
3. Crawls both documentation sources
4. Saves converted Markdown files

## Architecture

### Documentation Sources

Two sites are crawled with different strategies:

| Site | URL | Strategy |
|------|-----|----------|
| Claude Code | code.claude.com | Link discovery (follows anchor links) |
| Claude API | platform.claude.com | Sitemap-based (fetches from /sitemap.xml) |

### Content Extraction Fallback Order

The crawler tries these selectors in sequence to find main content:
1. ID-based (`#content`, `#content-area`)
2. Class-based (`.mdx-content`)
3. Semantic HTML (`<article>`, `<main>`)
4. Attribute-based (`role="main"`)
5. Largest text block heuristic

### Output Structure

```
docs-md/
├── claude-code/    # Claude Code documentation (~50 files)
└── api/            # Claude API documentation (~530 files)
    ├── about-claude/
    ├── agents-and-tools/
    ├── api/
    ├── build-with-claude/
    └── ...
```

## Changelog Site

The project includes a static changelog site deployed to GitHub Pages.

**Live site:** https://gpambrozio.github.io/ClaudeDocs/

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
- playwright - Browser automation for JS-rendered pages
- beautifulsoup4 - HTML parsing
- markdownify - HTML to Markdown conversion
- lxml - XML parsing for sitemaps
- httpx - Async HTTP client

Declared inline in site/build_site.py:
- jinja2 - HTML templating
- markdown - Markdown to HTML conversion
- feedgen - RSS feed generation
