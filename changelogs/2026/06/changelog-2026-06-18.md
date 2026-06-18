# [Claude docs changes for June 18th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/dbf3ffb5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/dbf3ffb5)]

## Executive Summary
- Claude Code 2.1.181 adds `/config key=value` syntax to set any setting directly from the prompt, plus a new `CLAUDE_CLIENT_PRESENCE_FILE` env var to suppress mobile push notifications when you're at the machine
- Version 2.1.181 fixes critical file corruption (0-byte/truncated writes on network drives), multiple startup issues (15s blocking on slow networks, macOS TUI freeze, crash on corrupted `.claude.json`), and prompt caching failures on custom base URLs and Foundry
- CLAUDE.md import parsing now explicitly skips code spans and fenced code blocks, letting you reference a path with backticks without triggering an import
- Sub-agents documentation gained a concrete example showing how to block an entire MCP server's tools with a single `disallowedTools: mcp__<server>` entry
- Analytics API docs clarified that both Claude Code and Claude Enterprise Analytics APIs share the Admin API reference but require separate key types

## New Claude Code versions

### [2.1.179](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/versions/2.1.179.md)

#### Major bug fixes

* Fixed mid-stream connection drops: partial responses are now preserved instead of showing a raw error, and the spinner no longer gets stuck at "running tool"
* Fixed mouse-wheel scrolling in WSL2 under Windows Terminal and VS Code (regression in 2.1.172)
* Fixed sandbox `denyRead`/`allowRead` glob over a large directory tree making the Bash tool description enormous and the session unusable on Linux
* Fixed Ctrl+O not showing the subagent's transcript when viewing a subagent; fixed clicking the prompt input not returning focus from the subagent/footer panel
* Fixed remote session background tasks appearing stuck as "still running" between turns
* Improved plugin loading performance in remote sessions

### [2.1.181](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/versions/2.1.181.md)

#### New features

* Added `/config key=value` syntax to set any setting from the prompt (e.g. `/config thinking=false`) — works in interactive, `-p`, and Remote Control modes
* Added `sandbox.allowAppleEvents` opt-in setting that lets sandboxed commands send Apple Events on macOS
* Added `CLAUDE_CLIENT_PRESENCE_FILE` environment variable: point it at a marker file to suppress mobile push notifications while you're at the machine

#### Existing feature improvements

* Upgraded the bundled Bun runtime to 1.4
* Improved streaming of long paragraphs: text now appears line-by-line instead of waiting for the first line break
* Improved auto-retry: API connection drops mid-thinking now automatically retry instead of showing "Connection closed while thinking"
* Improved the subagent panel: idle subagents auto-hide after 30s, the list caps at 5 rows with scroll hints, and keyboard hints now show in the footer
* Improved the MCP OAuth browser page to match Claude Code's visual style and auto-close on success
* Changed fullscreen mode URL opening to require Cmd+click (macOS) / Ctrl+click, matching native terminal behavior
* Changed the `Improved N memories` line to no longer list individual files outside verbose mode

#### Major bug fixes

* Fixed prompt caching not reading on custom `ANTHROPIC_BASE_URL` and on Foundry due to a per-request attestation token changing every turn
* Fixed Write/Edit producing 0-byte or truncated files on network drives and cloud-synced folders
* Fixed `open`, `osascript`, and browser-based auth flows failing with error -600 on macOS by adding the Apple Events entitlement
* Fixed a startup regression (~120ms per launch, introduced in 2.1.169): first prompt no longer waits for managed-settings fetch when no MCP servers are configured
* Fixed startup blocking with a blank terminal for up to 15 seconds when the account settings fetch is slow on a degraded network
* Fixed startup crash (`TypeError: Cannot read properties of null`) when `.claude.json` contains corrupted null project entries
* Fixed macOS TUI freezing at session start (Ctrl+C unresponsive) when Spotlight is busy reindexing
* Fixed long-running idle sessions losing their history when another Claude Code process ran the 30-day transcript cleanup
* Fixed foreground subagents spawning unbounded nested chains; they now respect the same 5-level depth limit as background subagents
* Fixed `/recap` and conversation forks using the previous model immediately after a model switch
* Fixed AWS `awsCredentialExport` credentials with a short remaining lifetime causing credential refreshes every minute
* Fixed `claude mcp get`/`list` showing `✓ Connected` when tools/list fails; now shows `! Connected · tools fetch failed` with the error detail
* Fixed settings changes (such as `/effort` or `/model`) failing with ENOENT when `~/.claude/settings.json` is a relative symlink under a symlinked `~/.claude`
* Fixed AskUserQuestion multi-select questions silently dropping a typed "Other" free-text answer when submitting
* Fixed `/stats` "Most active day" and daily token chart dates showing one day early in UTC-negative timezones

-----

## Claude Code changes

### Changed documents

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Added an enterprise CTA at the top of the page directing users to sales for enterprise plans, SSO, and centralized billing. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Import parsing now explicitly skips Markdown code spans and fenced code blocks. Wrapping a path in backticks (`` `@README` ``) keeps it literal, while `@README` outside backticks imports the file. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/memory.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/memory#import-additional-files)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added a new row to the command name table documenting how nested `.claude/skills/` directories are handled when a name clashes with another skill: the command name becomes the subdirectory path relative to the working directory plus the skill directory name (e.g. `apps/web/.claude/skills/deploy/SKILL.md` → `/apps/web:deploy`). [[line 224](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/skills.md?plain=1#L224)] [[Source](https://code.claude.com/docs/en/skills#how-a-skill-gets-its-command-name)]
* Updated the `/doctor` description to specify it shows how many skill descriptions are being shortened or dropped (not just which skills are affected). [[line 750](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/skills.md?plain=1#L750)] [[Source](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added a code example demonstrating how to use `disallowedTools: mcp__github` to remove every tool from the `github` MCP server while keeping all other built-in and MCP tools. [[lines 316-325](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/claude-code/sub-agents.md?plain=1#L316-L325)] [[Source](https://code.claude.com/docs/en/sub-agents#available-tools)]

-----

## API changes

### Changed documents

#### [analytics-api](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/api/manage-claude/analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

* Added clarification that both the Claude Code Analytics API and the Claude Enterprise Analytics API appear under the Admin API reference, but are separate APIs requiring separate key types. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/api/manage-claude/analytics-api.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]
* Updated Claude Enterprise Analytics API reference links from external support.claude.com articles to the internal `api/admin/analytics.md` reference page. [[lines 75, 84, 94](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/api/manage-claude/analytics-api.md?plain=1#L75)]

#### [claude-code-analytics-api](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/api/manage-claude/claude-code-analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)]

* Updated the Claude Code Analytics API reference link to the new path `api/admin/usage_report/retrieve_claude_code.md`. [[line 73](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/api/manage-claude/claude-code-analytics-api.md?plain=1#L73)] [[Source](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)]

#### [usage-cost-api](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/api/manage-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

* Updated the Claude Enterprise Analytics API link to the new internal reference path `api/admin/analytics.md`. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/dbf3ffb5/docs-md/api/manage-claude/usage-cost-api.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]
