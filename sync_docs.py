#!/usr/bin/env python3
"""
Sync Claude documentation from code.claude.com and platform.claude.com.

Both sites serve the Markdown source of every documentation page: append
".md" to a page URL (the URLs are extensionless) and the server responds with
"text/markdown". This is an officially supported path -- each site's llms.txt
indexes those same ".md" URLs -- so there is no HTML rendering or conversion
step here.

Usage:
    uv run sync_docs.py
"""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "httpx>=0.27",
# ]
# ///

import asyncio
import re
from pathlib import Path
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree

import httpx


OUTPUT_DIR = Path("docs-md")

COPYRIGHT_NOTICE = "\n\n---\n\n*Copyright © Anthropic. All rights reserved.*\n"

# URLs to skip (e.g., pages that are mirrored by another script)
SKIP_URLS: set[str] = set()

# Documentation sites to crawl
SITES = [
    {
        "name": "claude-code",
        "start_url": "https://code.claude.com/docs/en",
        "url_pattern": r"^https://code\.claude\.com/docs/en",
        "sitemap_url": "https://code.claude.com/sitemap.xml",
        "llms_url": "https://code.claude.com/docs/llms.txt",
    },
    {
        "name": "api",
        "start_url": "https://platform.claude.com/docs/en",
        "url_pattern": r"^https://platform\.claude\.com/docs/en",
        "sitemap_url": "https://platform.claude.com/sitemap.xml",
        "llms_url": "https://platform.claude.com/llms.txt",
    },
]

MAX_RETRIES = 2
CONCURRENCY = 8
REQUEST_TIMEOUT = 60

# Every served .md file opens with a pointer to the documentation index.
# It is boilerplate, identical on every page, so it is stripped.
PREAMBLE_RE = re.compile(
    r"\A(?:>[^\n]*\n)+\s*",
)

# Fenced code block delimiter, e.g. ``` or ~~~ with optional indent
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")

# Mintlify tags its code fences with `theme={null}`, which is presentation
# metadata rather than a language.
FENCE_THEME_RE = re.compile(r"^(\s*(?:`{3,}|~{3,}).*?)\s+theme=\{null\}\s*$")

# A tag's attribute list. Quoted values are matched as a unit because they may
# themselves contain angle brackets, as in title="JsonField<T> vs plain T".
_ATTRS = r"""(?:\s(?:"[^"]*"|'[^']*'|[^<>"'])*)?"""

# An MDX component or HTML wrapper alone on its own line: <Note>, <div ...>
OPEN_TAG_RE = re.compile(rf"^(\s*)<([A-Z][A-Za-z0-9]*|div|span)({_ATTRS})>\s*$")
CLOSE_TAG_RE = re.compile(r"^\s*</([A-Z][A-Za-z0-9]*|div|span)>\s*$")

# Self-closing component with no content: <Icon name="x" />
SELF_CLOSING_RE = re.compile(rf"^\s*<([A-Z][A-Za-z0-9]*|br|hr){_ATTRS}/?>\s*$")

# Single-line component wrapping inline content: <Note>text</Note>
INLINE_TAG_RE = re.compile(
    rf"<([A-Z][A-Za-z0-9]*|div|span){_ATTRS}>(.*?)</\1>",
    re.DOTALL,
)

# <img src="..." alt="..." /> -> ![alt](src)
IMG_RE = re.compile(r"<img\s[^<>]*?/?>", re.DOTALL)
ATTR_RE = re.compile(r'(\w[\w-]*)\s*=\s*"([^"]*)"')

# Components whose `title` attribute carries content worth keeping
TITLED_TAGS = {"Step", "Tab", "Accordion", "Card", "Expandable", "Frame"}

# A Markdown link. The label allows one level of nested brackets so that links
# labelled with code such as [`_meta["key"]`](...) are matched whole.
LINK_RE = re.compile(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\(([^)]+)\)")


def split_code_fences(text: str) -> list[tuple[str, bool]]:
    """Split text into (segment, is_code) chunks so code blocks stay untouched.

    Angle brackets inside code blocks are generics or literal markup, not MDX
    components, so every transform below must skip them.
    """
    segments: list[tuple[str, bool]] = []
    buf: list[str] = []
    fence: str | None = None

    for line in text.split("\n"):
        match = FENCE_RE.match(line)
        if fence is None and match:
            if buf:
                segments.append(("\n".join(buf), False))
                buf = []
            fence = match.group(1)
            buf.append(line)
        elif fence is not None and match and match.group(1)[0] == fence[0] and len(match.group(1)) >= len(fence):
            buf.append(line)
            segments.append(("\n".join(buf), True))
            buf = []
            fence = None
        else:
            buf.append(line)

    if buf:
        segments.append(("\n".join(buf), fence is not None))

    return segments


def mask_code_blocks(text: str) -> tuple[str, list[str]]:
    """Replace each code block with a one-line placeholder.

    Components wrap code blocks, so the tags around one must stay in the same
    text the unwrapper sees. Masking keeps the document intact while hiding
    code from every transform below.
    """
    blocks: list[str] = []
    lines = []

    for segment, is_code in split_code_fences(text):
        if not is_code:
            lines.append(segment)
            continue

        first = segment.split("\n")[0]
        indent = first[: len(first) - len(first.lstrip())]
        lines.append(f"{indent}\x00CODE:{len(blocks)}\x00")
        blocks.append(segment)

    return "\n".join(lines), blocks


def restore_code_blocks(text: str, blocks: list[str]) -> str:
    """Put code blocks back, matching the indentation their placeholder ended at."""

    def restore(line: str) -> str:
        match = re.match(r"^(\s*)\x00CODE:(\d+)\x00\s*$", line)
        if not match:
            return line

        block_lines = clean_fence_info(blocks[int(match.group(2))]).split("\n")
        first = block_lines[0]
        shift = (len(first) - len(first.lstrip())) - len(match.group(1))
        if shift > 0:
            block_lines = [
                line[shift:] if line.strip() else line for line in block_lines
            ]

        return "\n".join(block_lines)

    return "\n".join(restore(line) for line in text.split("\n"))


def clean_fence_info(text: str) -> str:
    """Drop Mintlify's `theme={null}` from code fence info strings."""
    return "\n".join(
        FENCE_THEME_RE.sub(r"\1", line) if FENCE_RE.match(line) else line
        for line in text.split("\n")
    )


def convert_images(text: str) -> str:
    """Convert <img> tags to Markdown image syntax."""

    def replace(match: re.Match) -> str:
        attrs = dict(ATTR_RE.findall(match.group(0)))
        src = attrs.get("src", "")
        if not src:
            return ""
        return f"![{attrs.get('alt', '')}]({src})"

    return IMG_RE.sub(replace, text)


def dedent_block(lines: list[str], target_indent: int) -> list[str]:
    """Remove the extra indentation a component added to its children.

    Left as-is if it would under-indent, since 4+ spaces of leftover indent
    would otherwise turn prose into a code block.
    """
    indents = [
        len(line) - len(line.lstrip()) for line in lines if line.strip()
    ]
    if not indents:
        return lines

    shift = min(indents) - target_indent
    if shift <= 0:
        return lines

    return [line[shift:] if line.strip() else line for line in lines]


def unwrap_block_tags(text: str) -> str:
    """Strip MDX component wrappers, keeping and de-indenting their children."""
    lines = text.split("\n")

    # Scan forward once, unwrapping each component in place. After an unwrap the
    # position is held, not reset, so nested components are handled on the next
    # iteration without rescanning the whole document.
    i = 0
    while i < len(lines):
        match = OPEN_TAG_RE.match(lines[i])
        if not match:
            i += 1
            continue

        indent, name, attrs = match.group(1), match.group(2), match.group(3) or ""

        # Find this tag's matching close, accounting for nesting of the same name
        depth = 0
        close_at = None
        for j in range(i + 1, len(lines)):
            open_match = OPEN_TAG_RE.match(lines[j])
            close_match = CLOSE_TAG_RE.match(lines[j])
            if open_match and open_match.group(2) == name:
                depth += 1
            elif close_match and close_match.group(1) == name:
                if depth == 0:
                    close_at = j
                    break
                depth -= 1

        if close_at is None:
            # Unbalanced tag: leave it alone rather than dropping content
            i += 1
            continue

        inner = dedent_block(lines[i + 1 : close_at], len(indent))

        title = dict(ATTR_RE.findall(attrs)).get("title")
        if title and name in TITLED_TAGS:
            inner = [f"{indent}**{title}**", ""] + inner

        lines[i : close_at + 1] = inner

    return "\n".join(lines)


def unwrap_inline_tags(text: str) -> str:
    """Strip single-line component wrappers, keeping their inline content."""
    for _ in range(10):
        new_text = INLINE_TAG_RE.sub(lambda m: m.group(2), text)
        if new_text == text:
            break
        text = new_text

    return "\n".join(
        "" if SELF_CLOSING_RE.match(line) else line for line in text.split("\n")
    )


def mdx_to_markdown(text: str) -> str:
    """Reduce the served MDX source to plain Markdown."""
    masked, blocks = mask_code_blocks(text)
    masked = convert_images(masked)
    masked = unwrap_block_tags(masked)
    masked = unwrap_inline_tags(masked)

    return restore_code_blocks(masked, blocks)


def convert_links(text: str, base_url: str) -> str:
    """Rewrite in-site documentation links to point at the local .md files."""

    def replace(match: re.Match) -> str:
        label, href = match.group(1), match.group(2).strip()

        if href.startswith(("#", "mailto:", "javascript:")):
            return match.group(0)

        absolute = href if href.startswith(("http://", "https://")) else urljoin(base_url, href)

        path_match = re.search(r"/docs/en/(.+?)(?:#.*)?$", absolute)
        if not path_match:
            return match.group(0)

        path = path_match.group(1).rstrip("/") or "index"
        return f"[{label}]({path}.md)"

    return LINK_RE.sub(replace, text)


def extract_links(text: str, base_url: str, pattern: re.Pattern) -> set[str]:
    """Find in-site documentation URLs referenced by a page."""
    found = set()

    for _, href in LINK_RE.findall(text):
        href = href.strip()
        if href.startswith(("#", "mailto:", "javascript:")):
            continue

        absolute = href if href.startswith(("http://", "https://")) else urljoin(base_url, href)
        absolute = absolute.split("#")[0].split("?")[0].rstrip("/")

        if absolute and pattern.match(absolute):
            found.add(absolute)

    return found


def get_title(markdown: str, url: str) -> str:
    """Extract the page title from its first heading."""
    match = re.search(r"^#\s+(.+)$", markdown, re.MULTILINE)
    if match:
        return match.group(1).strip()

    path = urlparse(url).path.rstrip("/").split("/")[-1] or "index"
    return path.replace("-", " ").replace("_", " ").title()


def url_to_filepath(url: str, site_name: str) -> Path:
    """Convert a URL to a local file path."""
    path = urlparse(url).path

    match = re.search(r"/docs/en/(.*)$", path)
    rel_path = match.group(1).strip("/") if match else "index"

    if not rel_path:
        rel_path = "index"

    rel_path = re.sub(r"\.md$", "", rel_path)

    return OUTPUT_DIR / site_name / f"{rel_path}.md"


def filepath_to_url(filepath: Path, site: dict) -> str:
    """Convert a stored file back to its source URL (inverse of url_to_filepath)."""
    rel = filepath.relative_to(OUTPUT_DIR / site["name"]).with_suffix("")
    return f"{site['start_url']}/{rel.as_posix()}"


async def get_sitemap_urls(client: httpx.AsyncClient, sitemap_url: str, pattern: re.Pattern) -> set[str]:
    """Fetch and parse a sitemap (or sitemap index) for matching URLs."""
    urls: set[str] = set()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

    try:
        response = await client.get(sitemap_url, timeout=30)
        response.raise_for_status()
        root = ElementTree.fromstring(response.content)
    except Exception as e:
        print(f"  Error fetching sitemap {sitemap_url}: {e}")
        return urls

    sub_sitemaps = [el.text for el in root.findall(".//sm:sitemap/sm:loc", ns) if el.text]
    if sub_sitemaps:
        for sub_url in sub_sitemaps:
            try:
                sub_response = await client.get(sub_url, timeout=30)
                sub_root = ElementTree.fromstring(sub_response.content)
                for loc in sub_root.findall(".//sm:url/sm:loc", ns):
                    if loc.text and pattern.match(loc.text):
                        urls.add(loc.text.rstrip("/"))
            except Exception as e:
                print(f"  Error fetching sub-sitemap {sub_url}: {e}")
        return urls

    for loc in root.findall(".//sm:url/sm:loc", ns):
        if loc.text and pattern.match(loc.text):
            urls.add(loc.text.rstrip("/"))

    return urls


async def get_llms_urls(client: httpx.AsyncClient, llms_url: str, pattern: re.Pattern) -> set[str]:
    """Parse llms.txt, which indexes the .md URLs directly."""
    try:
        response = await client.get(llms_url, timeout=30)
        response.raise_for_status()
    except Exception as e:
        print(f"  Error fetching {llms_url}: {e}")
        return set()

    urls = set()
    for match in re.findall(r"https://[^\s)\]]+", response.text):
        url = re.sub(r"\.md$", "", match.rstrip(".,;")).rstrip("/")
        if pattern.match(url):
            urls.add(url)

    return urls


async def fetch_markdown(client: httpx.AsyncClient, url: str) -> tuple[str, str | None, bool]:
    """Fetch a page's Markdown source.

    Returns (url, markdown, is_gone). `is_gone` distinguishes a 404 -- meaning
    the page was removed upstream and its local file should go too -- from a
    transient failure, where the local file is kept.
    """
    for attempt in range(MAX_RETRIES + 1):
        try:
            response = await client.get(f"{url}.md", timeout=REQUEST_TIMEOUT)
        except Exception as e:
            if attempt == MAX_RETRIES:
                print(f"  Error: {url} - {e}")
                return url, None, False
            continue

        if response.status_code == 404:
            return url, None, True

        if response.status_code >= 400:
            if attempt == MAX_RETRIES:
                print(f"  Error: {url} - HTTP {response.status_code}")
                return url, None, False
            continue

        # A page that has moved redirects to its new location, and a
        # cross-site redirect drops the ".md" suffix and answers with the
        # rendered HTML page. Either way this URL no longer has a source of
        # its own, so the local file should go.
        if "markdown" not in response.headers.get("content-type", ""):
            return url, None, True

        if re.sub(r"\.md$", "", str(response.url)).rstrip("/") != url:
            return url, None, True

        return url, response.text, False

    return url, None, False


async def seed_urls(client: httpx.AsyncClient, site: dict, pattern: re.Pattern) -> set[str]:
    """Collect starting URLs from the sitemap, llms.txt, and existing files.

    Neither index lists every live page (the per-language SDK reference pages
    are absent from both), so previously mirrored files seed the crawl too and
    404s prune whatever has since been removed.
    """
    sitemap_urls, llms_urls = await asyncio.gather(
        get_sitemap_urls(client, site["sitemap_url"], pattern),
        get_llms_urls(client, site["llms_url"], pattern),
    )
    print(f"  Sitemap: {len(sitemap_urls)} URLs, llms.txt: {len(llms_urls)} URLs")

    existing = set()
    site_dir = OUTPUT_DIR / site["name"]
    if site_dir.exists():
        for filepath in site_dir.rglob("*.md"):
            existing.add(filepath_to_url(filepath, site))
        print(f"  Previously mirrored: {len(existing)} pages")

    return {site["start_url"]} | sitemap_urls | llms_urls | existing


async def crawl_site(client: httpx.AsyncClient, site: dict) -> tuple[list[tuple[str, str, str]], set[str]]:
    """Crawl a documentation site.

    Returns (results, valid_urls), where results is a list of
    (url, title, markdown) and valid_urls is every URL whose local file should
    survive cleanup.
    """
    pattern = re.compile(site["url_pattern"])
    results: list[tuple[str, str, str]] = []
    valid_urls: set[str] = set()
    seen: set[str] = set()

    print(f"\nCrawling {site['name']}...")

    pending = {
        url for url in await seed_urls(client, site, pattern) if url not in SKIP_URLS
    }
    semaphore = asyncio.Semaphore(CONCURRENCY)

    async def fetch(url: str):
        async with semaphore:
            return await fetch_markdown(client, url)

    while pending:
        batch = sorted(pending)
        seen |= pending
        pending = set()

        for url, raw, is_gone in await asyncio.gather(*(fetch(url) for url in batch)):
            if raw is None:
                # Keep the local file on transient failures; drop it on 404
                if not is_gone:
                    valid_urls.add(url)
                continue

            valid_urls.add(url)

            body = PREAMBLE_RE.sub("", raw)
            markdown = mdx_to_markdown(body)
            markdown = convert_links(markdown, url)
            markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

            if len(markdown) < 100:
                continue

            title = get_title(markdown, url)
            if not markdown.startswith("#"):
                markdown = f"# {title}\n\n{markdown}"

            results.append((url, title, markdown))

            for link in extract_links(body, url, pattern):
                if link not in seen and link not in SKIP_URLS:
                    pending.add(link)

        print(f"  {len(results)} pages fetched, {len(pending)} newly discovered")

    return results, valid_urls


async def main():
    print("=== Claude Docs Sync ===")
    print(f"Output: {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    total = 0
    all_valid_filepaths = set()

    headers = {"User-Agent": "ClaudeDocs-sync (+https://github.com/marvin-ambrozio/ClaudeDocs)"}
    async with httpx.AsyncClient(follow_redirects=True, headers=headers) as client:
        for site in SITES:
            results, valid_urls = await crawl_site(client, site)

            for url in valid_urls:
                all_valid_filepaths.add(url_to_filepath(url, site["name"]))

            for url, title, markdown in results:
                filepath = url_to_filepath(url, site["name"])
                filepath.parent.mkdir(parents=True, exist_ok=True)
                filepath.write_text(markdown + COPYRIGHT_NOTICE, encoding="utf-8")

            print(f"  Saved {len(results)} files to {site['name']}/")
            total += len(results)

    # Remove files that are no longer in the docs
    removed = 0
    for filepath in OUTPUT_DIR.rglob("*.md"):
        if filepath not in all_valid_filepaths:
            filepath.unlink()
            removed += 1
            print(f"  Removed: {filepath.relative_to(OUTPUT_DIR)}")

    # Clean up empty directories
    for dirpath in sorted(OUTPUT_DIR.rglob("*"), reverse=True):
        if dirpath.is_dir() and not any(dirpath.iterdir()):
            dirpath.rmdir()

    print(f"\nTotal: {total} files saved, {removed} removed from {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(main())
