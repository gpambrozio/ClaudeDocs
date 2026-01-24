#!/usr/bin/env python3
"""
Build static changelog site from markdown files.

Usage:
    uv run site/build_site.py
"""
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "jinja2>=3.1",
#     "markdown>=3.5",
#     "feedgen>=1.0",
# ]
# ///

import os
import re
import shutil
from calendar import Calendar
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import markdown
from feedgen.feed import FeedGenerator
from jinja2 import Environment, FileSystemLoader

# Configuration
CHANGELOGS_DIR = Path("changelogs")
SITE_DIR = Path("site")
OUTPUT_DIR = Path("_site")

# Detect URLs for GitHub Pages
def get_urls() -> tuple[str, str]:
    """Get base URL path and full site URL for GitHub Pages."""
    # Check for explicit overrides
    if base := os.environ.get("BASE_URL"):
        site_url = os.environ.get("SITE_URL", "")
        return base.rstrip("/"), site_url.rstrip("/")

    # Check for custom domain via CNAME file
    cname_file = Path("CNAME")
    if cname_file.exists():
        custom_domain = cname_file.read_text().strip()
        if custom_domain:
            return "", f"https://{custom_domain}"

    # GitHub Actions: project pages are at /<repo-name>/
    if repo := os.environ.get("GITHUB_REPOSITORY"):
        owner, repo_name = repo.split("/")
        base_url = f"/{repo_name}"
        site_url = f"https://{owner}.github.io/{repo_name}"
        return base_url, site_url
    return "", ""

BASE_URL, SITE_URL = get_urls()


@dataclass
class ChangelogEntry:
    """Represents a single changelog entry."""

    date: date
    filepath: Path
    title: str
    content: str
    html_content: str
    has_new_version: bool

    @property
    def url(self) -> str:
        """Generate the URL path for this changelog."""
        return f"/{self.date.year}/{self.date.month:02d}/{self.date.day:02d}.html"


def discover_changelogs() -> list[ChangelogEntry]:
    """Scan the changelogs directory and parse all entries."""
    entries = []
    pattern = re.compile(r"changelog-(\d{4})-(\d{2})-(\d{2})\.md")
    md_converter = markdown.Markdown(extensions=["tables", "fenced_code"])

    for md_file in CHANGELOGS_DIR.rglob("changelog-*.md"):
        match = pattern.search(md_file.name)
        if not match:
            continue

        year, month, day = map(int, match.groups())
        entry_date = date(year, month, day)

        content = md_file.read_text(encoding="utf-8")
        html_content = md_converter.convert(content)
        md_converter.reset()

        # Extract title from first H1
        title_match = re.search(r"^#\s+(.+?)(?:\[|$)", content, re.MULTILINE)
        if title_match:
            title = title_match.group(1).strip()
            # Clean up markdown links in title
            title = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", title)
        else:
            title = f"Changelog for {entry_date.strftime('%B %d, %Y')}"

        # Check if changelog contains a new version release
        has_new_version = bool(
            re.search(r"^##\s+New Claude Code versions", content, re.MULTILINE)
        )

        entries.append(
            ChangelogEntry(
                date=entry_date,
                filepath=md_file,
                title=title,
                content=content,
                html_content=html_content,
                has_new_version=has_new_version,
            )
        )

    return sorted(entries, key=lambda e: e.date, reverse=True)


def build_month_grid(year: int, month: int, changelog_dates: dict, viewing_date: date) -> list:
    """Build calendar grid for a specific month."""
    cal = Calendar(firstweekday=6)
    weeks = []
    for week in cal.monthdatescalendar(year, month):
        week_data = []
        for day in week:
            if day.month != month:
                week_data.append({"number": None, "has_changelog": False})
            else:
                changelog = changelog_dates.get(day)
                has_changelog = changelog is not None
                has_version = has_changelog and changelog.has_new_version
                week_data.append(
                    {
                        "number": day.day,
                        "has_changelog": has_changelog,
                        "has_version": has_version,
                        "is_current": day == viewing_date,
                        "url": f"/{day.year}/{day.month:02d}/{day.day:02d}.html"
                        if has_changelog
                        else None,
                    }
                )
        weeks.append(week_data)
    return weeks


def build_calendar_data(
    changelogs: list[ChangelogEntry], viewing_date: date
) -> dict:
    """Build calendar display data for templates."""
    # Index changelogs by date for O(1) lookup
    changelog_dates = {cl.date: cl for cl in changelogs}

    # Get all unique months that have changelogs
    all_months = set()
    for cl in changelogs:
        all_months.add((cl.date.year, cl.date.month))

    # Sort months chronologically (oldest first for navigation)
    sorted_months = sorted(all_months)

    # Build calendar data for all months
    months_data = []
    current_month_index = 0
    for i, (year, month) in enumerate(sorted_months):
        month_date = date(year, month, 1)
        if year == viewing_date.year and month == viewing_date.month:
            current_month_index = i
        months_data.append({
            "year": year,
            "month": month,
            "name": month_date.strftime("%B"),
            "weeks": build_month_grid(year, month, changelog_dates, viewing_date),
        })

    return {
        "months": months_data,
        "current_index": current_month_index,
    }


def get_navigation(
    changelogs: list[ChangelogEntry], current_date: date
) -> tuple[dict | None, dict | None]:
    """Get previous and next changelog navigation data."""
    sorted_logs = sorted(changelogs, key=lambda x: x.date)
    dates = [cl.date for cl in sorted_logs]

    try:
        idx = dates.index(current_date)
    except ValueError:
        return (None, None)

    prev_entry = sorted_logs[idx - 1] if idx > 0 else None
    next_entry = sorted_logs[idx + 1] if idx < len(sorted_logs) - 1 else None

    prev_nav = (
        {
            "url": prev_entry.url,
            "date": prev_entry.date.strftime("%B %d, %Y"),
        }
        if prev_entry
        else None
    )

    next_nav = (
        {
            "url": next_entry.url,
            "date": next_entry.date.strftime("%B %d, %Y"),
        }
        if next_entry
        else None
    )

    return (prev_nav, next_nav)


def generate_rss(changelogs: list[ChangelogEntry], site_url: str, output_dir: Path):
    """Generate RSS feed for changelogs."""
    fg = FeedGenerator()
    feed_url = site_url or "https://example.com"
    fg.id(feed_url)
    fg.title("ClaudeCodeChanges")
    fg.description("Daily changes to Claude Code documentation")
    fg.link(href=feed_url, rel="alternate")
    fg.link(href=f"{feed_url}/feed.xml", rel="self")
    fg.language("en")

    # Add last 20 changelogs
    for cl in changelogs[:20]:
        fe = fg.add_entry()
        entry_url = f"{feed_url}{cl.url}"
        fe.id(entry_url)
        fe.title(cl.title)
        fe.link(href=entry_url)
        fe.published(datetime.combine(cl.date, datetime.min.time()).isoformat() + "Z")
        fe.content(cl.html_content, type="html")

    fg.rss_file(str(output_dir / "feed.xml"))


def build_site():
    """Main site builder."""
    print("Discovering changelogs...")
    changelogs = discover_changelogs()
    print(f"Found {len(changelogs)} changelogs")

    if not changelogs:
        print("No changelogs found. Exiting.")
        return

    # Set up Jinja2
    env = Environment(
        loader=FileSystemLoader(SITE_DIR / "templates"),
        autoescape=True,
    )

    # Clean and create output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True)

    # Copy static files
    static_src = SITE_DIR / "static"
    static_dst = OUTPUT_DIR / "static"
    if static_src.exists():
        shutil.copytree(static_src, static_dst)
        print("Copied static files")

    # Copy CNAME file for custom domain
    cname_file = Path("CNAME")
    if cname_file.exists():
        shutil.copy(cname_file, OUTPUT_DIR / "CNAME")
        print("Copied CNAME file")

    # Load templates
    changelog_template = env.get_template("changelog.html")

    # Generate individual changelog pages
    for i, cl in enumerate(changelogs):
        prev_nav, next_nav = get_navigation(changelogs, cl.date)
        calendar_data = build_calendar_data(changelogs, cl.date)

        html = changelog_template.render(
            title=cl.title,
            content=cl.html_content,
            current_date=cl.date.strftime("%B %d, %Y"),
            prev=prev_nav,
            next=next_nav,
            calendar=calendar_data,
            base_url=BASE_URL,
        )

        # Create output path
        out_path = OUTPUT_DIR / str(cl.date.year) / f"{cl.date.month:02d}"
        out_path.mkdir(parents=True, exist_ok=True)
        (out_path / f"{cl.date.day:02d}.html").write_text(html, encoding="utf-8")

    print(f"Generated {len(changelogs)} changelog pages")

    # Generate index.html (copy of latest changelog)
    latest = changelogs[0]
    prev_nav, next_nav = get_navigation(changelogs, latest.date)
    calendar_data = build_calendar_data(changelogs, latest.date)

    index_html = changelog_template.render(
        title=latest.title,
        content=latest.html_content,
        current_date=latest.date.strftime("%B %d, %Y"),
        prev=prev_nav,
        next=next_nav,
        calendar=calendar_data,
        base_url=BASE_URL,
        is_index=True,
    )
    (OUTPUT_DIR / "index.html").write_text(index_html, encoding="utf-8")
    print("Generated index.html")

    # Generate RSS feed
    generate_rss(changelogs, SITE_URL, OUTPUT_DIR)
    print("Generated RSS feed")

    print(f"\nSite built successfully in {OUTPUT_DIR}/")


if __name__ == "__main__":
    build_site()
