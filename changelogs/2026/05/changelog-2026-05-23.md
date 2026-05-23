# [Claude docs changes for May 23rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/1718a147850aa5fc31c0cf81650488f3dab05fd6) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/1718a147850aa5fc31c0cf81650488f3dab05fd6)]

## Executive Summary
- Claude Code 2.1.149 adds per-category usage breakdowns in `/usage` (skills, subagents, plugins, per-MCP-server cost) and keyboard scrolling in `/diff` detail view
- Claude Code 2.1.149 fixes a critical PowerShell permission bypass where built-in `cd` functions could change the working directory undetected, allowing commands to read outside the workspace
- Claude Code 2.1.149 fixes `find` in the Bash tool exhausting the macOS system file/vnode table and crashing the host on large directory trees
- New PHP SDK API reference documentation added covering all standard and beta API endpoints

## New Claude Code versions

### [2.1.149](https://github.com/gpambrozio/ClaudeDocs/blob/1718a147850aa5fc31c0cf81650488f3dab05fd6/versions/2.1.149.md)

#### New features

* `/usage` now shows a per-category breakdown of what's driving limits usage — skills, subagents, plugins, and per-MCP-server cost
* `/diff` detail view can now be scrolled with the keyboard (arrows, `j`/`k`, `PgUp`/`PgDn`, `Space`, `Home`/`End`)
* Markdown output now renders GFM task list checkboxes (`- [ ] todo` / `- [x] done`) instead of plain bullets
* Enterprise: added the `allowAllClaudeAiMcps` managed setting to load claude.ai cloud MCP connectors alongside `managed-mcp.json`

#### Major bug fixes

* Fixed a PowerShell permission bypass: built-in `cd` functions (`cd..`, `cd\`, `cd~`, `X:`) changed the working directory undetected, letting a later command read outside the workspace
* Fixed the sandbox write allowlist in git worktrees covering the entire main repository root instead of only the shared `.git` directory (with `hooks/` and `config` denied)
* Fixed PowerShell prefix/wildcard allow rules (e.g. `PowerShell(dotnet.exe build *)`) not pre-approving native executables and scripts
* Fixed a permission-analysis gap where the parser trusted stale variable-tracking values for `PWD`/`OLDPWD`/`DIRSTACK` across `cd`/`pushd`/`popd`
* Fixed `find` in the Bash tool exhausting the macOS system file/vnode table and crashing the host on large directory trees
* Fixed the managed-settings approval dialog leaving the terminal frozen after accepting at startup
* Fixed `/ultraplan` and remote session creation failing with "Could not capture uncommitted changes" when the working tree has no real changes
* Fixed `otelHeadersHelper` failing silently when the script path contains spaces
* Fixed the thinking spinner staying amber across tool calls and onto fresh thinking bursts
* Fixed collapsed Bash output reporting the wrong hidden-line count for outputs with many short lines
* Fixed slash-command argument-hint clipping trailing typed characters when the hint overflows the input box
* Fixed argument-hint and progressive arg suggestions not appearing after Tab-completing a skill whose frontmatter `name:` differs from its directory basename
* Fixed the status bar showing the user's baseline `/effort` setting instead of the effort level applied by skill/agent `effort:` frontmatter
* Fixed Ctrl+O transcript view freezing at the moment it was opened instead of tailing new messages
* Fixed editing a recalled prompt-history entry losing the edit when navigating further up/down with arrow keys
* Fixed `/config` exit summary reporting phantom changes to auto-compact and theme when toggling unrelated settings
* Fixed `/insights` crashing when cached session-meta files are missing optional fields
* Fixed malformed PowerShell and History tool calls with missing input being misclassified as reads in transcript collapsing
* Fixed renaming a Remote Control session from claude.ai or the Claude mobile app not updating the local session name for `claude --resume`
* Fixed a race where a just-submitted prompt could appear twice in the up-arrow history
* Fixed tapping the "Jump to bottom" pill in fullscreen mode not dismissing it immediately
* Improved `/feedback` reports to include the conversation that happened before context compaction

### [2.1.150](https://github.com/gpambrozio/ClaudeDocs/blob/1718a147850aa5fc31c0cf81650488f3dab05fd6/versions/2.1.150.md)

Internal infrastructure improvements (no user-facing changes).

-----

## Claude Code changes

No significant changes.

-----

## API changes

### New Documents

#### [api/php/beta](https://github.com/gpambrozio/ClaudeDocs/blob/1718a147850aa5fc31c0cf81650488f3dab05fd6/docs-md/api/api/php/beta.md) [[Source](https://platform.claude.com/docs/en/api/php/beta)]

New PHP SDK API reference documentation covering all beta endpoints. Includes complete type definitions and method signatures for agents, environments, files, memory stores, messages, models, sessions, skills, user profiles, vaults, and webhooks using PHP syntax (e.g., `$client->beta->messages->create(...)`).

#### [api/php/messages](https://github.com/gpambrozio/ClaudeDocs/blob/1718a147850aa5fc31c0cf81650488f3dab05fd6/docs-md/api/api/php/messages.md) [[Source](https://platform.claude.com/docs/en/api/php/messages)]

New PHP SDK API reference for standard (non-beta) messages endpoints, including message creation, token counting, and batch operations.

#### [api/php/models](https://github.com/gpambrozio/ClaudeDocs/blob/1718a147850aa5fc31c0cf81650488f3dab05fd6/docs-md/api/api/php/models.md) [[Source](https://platform.claude.com/docs/en/api/php/models)]

New PHP SDK API reference for the standard models endpoint, covering model listing and retrieval.

### Changed documents

No significant changes (bulk reformatting only: `= object { }` → `object { }` and `Accepts one of the following:` → `One of the following:` across ~860 API reference files).
