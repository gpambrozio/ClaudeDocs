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

`SKIP_URLS` holds pages deliberately left out of the mirror. The Claude Code
changelog is generated from the same `CHANGELOG.md` that `sync_changelog.py`
splits into `versions/`, so mirroring it would duplicate every release entry
within a single sync commit.

### MDX Conversion

The served source is MDX, so `sync_docs.py` reduces it to plain Markdown:

- Strips the documentation-index preamble every page carries
- Unwraps components (`<Note>`, `<CodeGroup>`, `<Steps>`, ...), keeping their
  content and removing the indentation they added; a `title` attribute becomes
  a bold line
- Turns `<Update>` into a `##` heading from its `label`, since the release notes
  pages carry the version or week only in that attribute
- Converts `<img>` tags to Markdown image syntax
- Drops Mintlify's `theme={null}` from code fence info strings

Code blocks are masked before any of this runs, so angle brackets inside them
(generics, literal markup) are never mistaken for MDX components.

### Link Rewriting

In-site links are repointed at the local `.md` files, but only after every
site has been crawled: whether a link can be rewritten depends on whether its
target was mirrored, and links cross between the two sites.

- The path emitted is relative to the **linking file**, which is how a Markdown
  viewer resolves it. A cross-site link reaches across the sibling mirror
  directories (`../api/about-claude/pricing.md`).
- Renamed pages are followed through the `{requested -> final}` map that
  `fetch_markdown` records whenever a request redirects. The docs keep linking
  to the pre-rename path long after the page has moved.
- `#fragments` are preserved, so a link into a section still lands there.
- A target that is not mirrored -- it 404s upstream, or it is in `SKIP_URLS` --
  keeps an absolute URL, so the reader reaches the real site rather than a path
  that will never exist.
- Links inside code blocks are left alone. There they are sample content, not
  navigation. An href that already ends in `.md` is left alone for the same
  reason: the docs use those to name a file bundled with a skill.

`check_links` audits the finished mirror the way a reader does, resolving each
relative link against the directory of the file holding it. A local link is
only ever emitted for a page that was mirrored, so a broken one means the
resolution is wrong and the sync fails rather than publishing it.

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
