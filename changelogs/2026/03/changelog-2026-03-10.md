# [Claude docs changes for March 10th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/98882097a20acbe87ea963376493c18b46879b05) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/98882097a20acbe87ea963376493c18b46879b05)]

## Executive Summary
- **Code Review** is now a managed service (research preview for Teams/Enterprise) that automatically reviews PRs using a fleet of specialized agents, posting inline comments with severity levels
- **`CLAUDE.local.md` removed**: The local project-specific CLAUDE.md file format is no longer supported; use home-directory imports instead for personal preferences
- **Claude Code 2.1.72**: Major release with ExitWorktree tool, effort level simplification (low/medium/high), restored `model` parameter on the Agent tool, and a fix that reduces prompt cache costs up to 12x in SDK `query()` calls
- **`/review` command deprecated**: The built-in `/review` slash command is deprecated; users should install the `code-review` plugin from the marketplace instead
- **Settings doc updated** with many new tools now available to Claude: Cron tools for scheduled tasks, Worktree entry/exit tools, TodoWrite, ToolSearch, and more

## New Claude Code versions

### [2.1.72](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/versions/2.1.72.md)

#### New features

* Added `w` key in `/copy` to write the focused selection directly to a file, bypassing the clipboard (useful over SSH)
* Added optional description argument to `/plan` (e.g., `/plan fix the auth bug`) that enters plan mode and immediately starts
* Added `ExitWorktree` tool to leave an `EnterWorktree` session
* Added `CLAUDE_CODE_DISABLE_CRON` environment variable to immediately stop scheduled cron jobs mid-session
* Added `lsof`, `pgrep`, `tput`, `ss`, `fd`, and `fdfind` to the bash auto-approval allowlist, reducing permission prompts for common read-only operations
* Restored the `model` parameter on the Agent tool for per-invocation model overrides
* Added support for marketplace git URLs without `.git` suffix (Azure DevOps, AWS CodeCommit)
* VSCode: Added effort level indicator on the input border
* VSCode: Added `vscode://anthropic.claude-code/open` URI handler to open a new Claude Code tab programmatically, with optional `prompt` and `session` query parameters

#### Existing feature improvements

* Simplified effort levels to low/medium/high (removed max) with new symbols (○ ◐ ●) and a brief notification instead of a persistent icon; use `/effort auto` to reset to default
* Improved `/config` — Escape now cancels changes, Enter saves and closes, Space toggles settings
* Improved up-arrow history to show current session's messages first when running multiple concurrent sessions
* Improved voice input transcription accuracy for repo names and common dev terms (regex, OAuth, JSON)
* Improved bash command parsing by switching to a native module — faster initialization and no memory leak
* Reduced bundle size by ~510 KB
* Changed CLAUDE.md HTML comments (`<!-- ... -->`) to be hidden from Claude when auto-injected (comments remain visible when read with the Read tool)
* Fixed tool search to activate even with `ANTHROPIC_BASE_URL` as long as `ENABLE_TOOL_SEARCH` is set

#### Major bug fixes

* Fixed prompt cache invalidation in SDK `query()` calls, reducing input token costs up to 12x
* Fixed slow exits when background tasks or hooks were slow to respond
* Fixed `--continue` not resuming from the most recent point after `--compact`
* Fixed skill hooks firing twice per event when a hooks-enabled skill is invoked by the model
* Fixed several voice mode issues: occasional input lag, false "No speech detected" errors, and stale transcripts re-filling the prompt after submission
* Fixed `/clear` killing background agent/bash tasks — only foreground tasks are now cleared
* Fixed worktree isolation issues: Task tool resume not restoring cwd, and background task notifications missing `worktreePath` and `worktreeBranch`
* Fixed parallel tool calls where a failed Read/WebFetch/Glob would cancel its siblings — only Bash errors now cascade
* Fixed double Ctrl+C not exiting when background agents or tasks are running
* Fixed several hooks issues including `transcript_path` pointing to the wrong directory and async hooks not receiving stdin
* Fixed several permission rule matching issues including wildcard rules not matching commands with heredocs and deny rules not applying to all command forms
* Fixed several plugin issues including installation failing on Windows and marketplace blocking user-scope installs

-----

## Claude Code changes

### New Documents

#### [Code Review](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

New document covering the Code Review managed service (research preview for Teams and Enterprise). A fleet of specialized agents automatically reviews GitHub pull requests, posting inline comments with severity levels (Normal/Nit/Pre-existing). Setup is done once by an admin and runs automatically on PR open/update. Reviews can be customized via `CLAUDE.md` and a new `REVIEW.md` file. Reviews average $15–25 and activity can be monitored via the analytics dashboard.

### Changed documents

#### [Best Practices](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Removed the mention of `CLAUDE.local.md` as an alternative for local project instructions; project root `CLAUDE.md` is now the only listed option. [[line 217](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/best-practices.md?plain=1#L217)] [[Source](https://code.claude.com/docs/en/best-practices#write-an-effective-claude-md)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Removed reference to `CLAUDE.local.md`; only `CLAUDE.md` files are mentioned as shared between Desktop and CLI. [[line 480](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/desktop.md?plain=1#L480)] [[Source](https://code.claude.com/docs/en/desktop#shared-configuration)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Added a reference to the new GitHub Code Review page at the top of the document. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/github-actions.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/github-actions)]
* PR review example changed from using `/review` skill to an explicit full-text review prompt. [[line 174](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/github-actions.md?plain=1#L174)] [[Source](https://code.claude.com/docs/en/github-actions#using-skills)]
* "Commands" section renamed to "Skills" and updated to reference installed skills directly from the prompt. [[line 286](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/github-actions.md?plain=1#L286)] [[Source](https://code.claude.com/docs/en/github-actions#configuration-examples)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* The `/review` command is now marked as deprecated; users are directed to install the `code-review` plugin from the marketplace instead. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/interactive-mode.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Removed the `Local instructions` row (`CLAUDE.local.md`) from the CLAUDE.md locations table. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/memory.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/memory#choose-where-to-put-claude-md-files)]
* Updated guidance for private per-project preferences: no longer recommends `CLAUDE.local.md`; instead suggests importing a file from your home directory. [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/memory.md?plain=1#L85)] [[Source](https://code.claude.com/docs/en/memory#import-additional-files)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Added new entry "Get automatic code review on every PR" linking to the new Code Review page. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/overview.md?plain=1#L213)] [[Source](https://code.claude.com/docs/en/overview#use-claude-code-everywhere)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Local scope definition updated: now specifically names `.claude/settings.local.json` instead of the generic `.claude/*.local.*` pattern. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/settings.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/settings#available-scopes)]
* CLAUDE.md local scope removed from the scopes feature table (no more `CLAUDE.local.md`). [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/settings.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/settings#what-uses-scopes)]
* Tools table significantly expanded with many new entries: `CronCreate`, `CronDelete`, `CronList` (scheduled tasks), `EnterPlanMode`, `EnterWorktree`, `ExitWorktree`, `ListMcpResourcesTool`, `ReadMcpResourceTool`, `TaskStop`, `TodoWrite`, `ToolSearch`; `KillShell` and `MCPSearch` removed. [[lines 1021-1051](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/claude-code/settings.md?plain=1#L1021-L1051)] [[Source](https://code.claude.com/docs/en/settings#tools-available-to-claude)]

-----

## API changes

### Changed documents

#### [Data Residency](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/api/build-with-claude/data-residency.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]

* Removed Microsoft Foundry from the list of third-party platforms with their own regional pricing; only AWS Bedrock and Google Vertex AI are now listed. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/api/build-with-claude/data-residency.md?plain=1#L86)] [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]

#### [Pricing](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Removed Microsoft Foundry from the list of third-party platforms with regional pricing details. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/98882097a20acbe87ea963376493c18b46879b05/docs-md/api/about-claude/pricing.md?plain=1#L83)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
