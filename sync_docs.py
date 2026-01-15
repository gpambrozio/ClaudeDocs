#!/usr/bin/env python3
"""
Sync Claude documentation from code.claude.com and platform.claude.com.
Uses Playwright to render JavaScript content before extracting.

Usage:
    uv run sync_docs.py
"""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "playwright>=1.40",
#     "beautifulsoup4>=4.12",
#     "markdownify>=0.11",
#     "lxml>=5.0",
#     "httpx>=0.27",
# ]
# ///

import asyncio
import re
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree

import httpx
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from playwright.async_api import async_playwright


OUTPUT_DIR = Path("docs-md")

# URLs to skip (e.g., pages that always timeout or fail)
SKIP_URLS = {
    "https://code.claude.com/docs/en/changelog",
}

# Documentation sites to crawl
SITES = [
    {
        "name": "claude-code",
        "start_url": "https://code.claude.com/docs/en/",
        "url_pattern": r"^https://code\.claude\.com/docs/en",
        "use_sitemap": False,
    },
    {
        "name": "api",
        "start_url": "https://platform.claude.com/docs/en/",
        "url_pattern": r"^https://platform\.claude\.com/docs/en",
        "sitemap_url": "https://platform.claude.com/sitemap.xml",
        "use_sitemap": True,
    },
]


def extract_main_content(soup: BeautifulSoup) -> str:
    """Extract the main documentation content from the HTML."""
    content = None

    # Look for specific IDs used by Claude docs
    content = soup.find(id="content")
    if not content:
        content = soup.find(id="content-area")
    if not content:
        content = soup.find(class_=re.compile(r"mdx-content", re.I))

    # Fallback to common patterns
    if not content:
        content = soup.find("article")
    if not content:
        content = soup.find("main")
    if not content:
        content = soup.find(class_=re.compile(r"^prose$", re.I))
    if not content:
        content = soup.find(attrs={"role": "main"})

    # Fallback: look for the largest text block
    if not content:
        body = soup.find("body")
        if body:
            # Find div with most text content
            divs = body.find_all("div", recursive=True)
            best_div = None
            best_len = 0
            for div in divs:
                text = div.get_text(strip=True)
                if len(text) > best_len and "Loading..." not in text[:100]:
                    best_len = len(text)
                    best_div = div
            content = best_div or body

    if content:
        # Remove unwanted elements
        for tag in ["nav", "aside", "footer", "header", "script", "style", "noscript"]:
            for el in content.find_all(tag):
                el.decompose()

        for pattern in [r"sidebar", r"nav(?!igation)", r"menu", r"toc", r"breadcrumb", r"feedback", r"footer"]:
            for el in content.find_all(class_=re.compile(pattern, re.I)):
                el.decompose()

        return str(content)

    return ""


def convert_links(content: str, base_url: str) -> str:
    """Convert HTML links to Markdown-friendly relative links."""
    soup = BeautifulSoup(content, "lxml")

    for link in soup.find_all("a", href=True):
        href = link["href"]

        # Skip anchors and special links
        if href.startswith(("#", "mailto:", "javascript:")):
            continue

        # Convert relative to absolute first
        if not href.startswith(("http://", "https://")):
            href = urljoin(base_url, href)

        # Check if it's a docs link we should convert to relative
        if "/docs/en/" in href:
            match = re.search(r"/docs/en/(.+?)(?:#.*)?$", href)
            if match:
                path = match.group(1).rstrip("/")
                if not path:
                    path = "index"
                link["href"] = f"{path}.md"

    return str(soup)


def html_to_markdown(html_content: str) -> str:
    """Convert HTML content to Markdown."""
    return md(
        html_content,
        heading_style="atx",
        bullets="-",
        code_language_callback=lambda el: (
            el.get("class", [""])[0].replace("language-", "")
            if el.get("class")
            else ""
        ),
    )


def get_title(soup: BeautifulSoup, url: str) -> str:
    """Extract the page title."""
    h1 = soup.find("h1")
    if h1:
        title = h1.get_text().strip()
        if title and title.lower() not in ("loading...", ""):
            return title

    title_tag = soup.find("title")
    if title_tag:
        title = title_tag.get_text().strip()
        title = re.sub(r"\s*[|\-–—]\s*(Claude|Anthropic).*$", "", title, flags=re.I)
        if title and title.lower() not in ("loading...", ""):
            return title

    # Fallback to URL path
    path = urlparse(url).path.rstrip("/").split("/")[-1] or "index"
    return path.replace("-", " ").replace("_", " ").title()


def url_to_filepath(url: str, site_name: str) -> Path:
    """Convert a URL to a local file path."""
    parsed = urlparse(url)
    path = parsed.path

    # Extract path after /docs/en/
    match = re.search(r"/docs/en/(.*)$", path)
    if match:
        rel_path = match.group(1).strip("/")
    else:
        rel_path = "index"

    if not rel_path:
        rel_path = "index"

    # Clean up
    rel_path = re.sub(r"\.html?$", "", rel_path)

    return OUTPUT_DIR / site_name / f"{rel_path}.md"


async def get_sitemap_urls(sitemap_url: str, url_pattern: str) -> list[str]:
    """Fetch and parse sitemap to get all matching URLs."""
    pattern = re.compile(url_pattern)
    urls = []

    async with httpx.AsyncClient() as client:
        response = await client.get(sitemap_url, timeout=30)
        response.raise_for_status()

        # Parse XML
        root = ElementTree.fromstring(response.content)

        # Handle both sitemap index and urlset
        ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}

        # Check for sitemap index
        sitemaps = root.findall(".//sm:sitemap/sm:loc", ns)
        if sitemaps:
            # It's a sitemap index, fetch each sub-sitemap
            for sitemap in sitemaps:
                sub_url = sitemap.text
                if sub_url:
                    try:
                        sub_response = await client.get(sub_url, timeout=30)
                        sub_root = ElementTree.fromstring(sub_response.content)
                        for loc in sub_root.findall(".//sm:url/sm:loc", ns):
                            if loc.text and pattern.match(loc.text):
                                urls.append(loc.text)
                    except Exception as e:
                        print(f"  Error fetching sub-sitemap {sub_url}: {e}")
        else:
            # It's a regular urlset
            for loc in root.findall(".//sm:url/sm:loc", ns):
                if loc.text and pattern.match(loc.text):
                    urls.append(loc.text)

    return urls


async def crawl_site(site: dict, browser) -> list[tuple[str, str, str]]:
    """Crawl a documentation site and return list of (url, title, markdown) tuples."""
    results = []
    visited = set()
    pattern = re.compile(site["url_pattern"])

    print(f"\nCrawling {site['name']}...")

    # Get URLs to visit
    if site.get("use_sitemap") and site.get("sitemap_url"):
        print(f"  Fetching URLs from sitemap...")
        to_visit = await get_sitemap_urls(site["sitemap_url"], site["url_pattern"])
        print(f"  Found {len(to_visit)} URLs in sitemap")
    else:
        to_visit = [site["start_url"]]

    page = await browser.new_page()

    while to_visit:
        url = to_visit.pop(0)

        # Normalize URL (remove fragment, trailing slash)
        url = url.split("#")[0].rstrip("/")
        if not url:
            continue

        if url in SKIP_URLS:
            continue

        if url in visited or not pattern.match(url):
            continue

        visited.add(url)

        try:
            # Navigate and wait for network idle
            response = await page.goto(url, wait_until="networkidle", timeout=30000)

            if not response or response.status >= 400:
                continue

            # Wait for content to render
            await page.wait_for_timeout(2000)

            # Get rendered HTML
            html = await page.content()
            soup = BeautifulSoup(html, "lxml")

            # Skip pages that didn't load
            body_text = soup.body.get_text() if soup.body else ""
            if body_text.count("Loading...") > 5:
                continue

            # Extract content
            title = get_title(soup, url)
            main_content = extract_main_content(soup)

            if not main_content or len(main_content) < 100:
                continue

            main_content = convert_links(main_content, url)
            markdown = html_to_markdown(main_content)

            # Clean up markdown
            markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip()

            # Skip very short content
            if len(markdown) < 100:
                continue

            # Add title if not present
            if not markdown.startswith("#"):
                markdown = f"# {title}\n\n{markdown}"

            results.append((url, title, markdown))
            print(f"  {title}")

            # If not using sitemap, discover more links
            if not site.get("use_sitemap"):
                for link in soup.find_all("a", href=True):
                    href = link["href"]
                    if href.startswith(("#", "mailto:", "javascript:")):
                        continue

                    if not href.startswith(("http://", "https://")):
                        href = urljoin(url, href)

                    href = href.split("#")[0].rstrip("/")

                    if href and href not in visited and pattern.match(href):
                        to_visit.append(href)

        except Exception as e:
            print(f"  Error: {url} - {e}")

    await page.close()
    return results


async def main():
    print("=== Claude Docs Sync ===")
    print(f"Output: {OUTPUT_DIR}")

    # Install Playwright browsers
    print("\nInstalling Playwright browsers...")
    subprocess.run(
        [sys.executable, "-m", "playwright", "install", "chromium"],
        check=True,
        capture_output=True,
    )

    # Clean output
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    total = 0

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        for site in SITES:
            results = await crawl_site(site, browser)

            # Write files
            for url, title, markdown in results:
                filepath = url_to_filepath(url, site["name"])
                filepath.parent.mkdir(parents=True, exist_ok=True)
                filepath.write_text(markdown, encoding="utf-8")

            print(f"  Saved {len(results)} files to {site['name']}/")
            total += len(results)

        await browser.close()

    print(f"\nTotal: {total} files saved to {OUTPUT_DIR}/")


if __name__ == "__main__":
    asyncio.run(main())
