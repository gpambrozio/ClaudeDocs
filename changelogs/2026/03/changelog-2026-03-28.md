# [Claude docs changes for March 28th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9c76419274c4beb678ca0741727833673e10c384) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9c76419274c4beb678ca0741727833673e10c384)]

## Executive Summary
- Hooks gain a new `if` field for fine-grained filtering by tool name and arguments, letting hooks skip spawning when the tool call doesn't match
- Agent SDK (Python and TypeScript) adds session management functions: `get_session_info()`, `rename_session()`, and `tag_session()`, plus new `RateLimitEvent` type for monitoring rate limit status
- Healthcare MCP servers (bioRxiv, ChEMBL, Clinical Trials, CMS Coverage, ICD-10 Codes, NPI Registry) migrated to new `hcls.mcp.claude.com` URLs; Zoho Desk MCP server added
- New `--tmux` CLI flag creates a tmux session alongside a worktree, and `disableDeepLinkRegistration` setting controls `claude-cli://` protocol handler registration
- MCP tool search behavior changed: all MCP tools are now deferred by default (previously only enabled for first-party hosts)

## New Claude Code versions

### [2.1.86](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/versions/2.1.86.md)

#### New features

* Added `X-Claude-Code-Session-Id` header to API requests so proxies can aggregate requests by session without parsing the body
* Added `.jj` and `.sl` to VCS directory exclusion lists so Grep and file autocomplete don't descend into Jujutsu or Sapling metadata

#### Existing feature improvements

* Read tool now uses compact line-number format and deduplicates unchanged re-reads, reducing token usage
* Reduced token overhead when mentioning files with `@` — raw string content no longer JSON-escaped
* Improved prompt cache hit rate for Bedrock, Vertex, and Foundry users by removing dynamic content from tool descriptions
* Memory filenames in the "Saved N memories" notice now highlight on hover and open on click
* Skill descriptions in `/skills` listing are now capped at 250 characters to reduce context usage
* `/skills` menu now sorts alphabetically for easier scanning
* Auto mode now shows "unavailable for your plan" when disabled by plan restrictions (was "temporarily unavailable")
* Reduced startup event-loop stalls when many claude.ai MCP connectors are configured (macOS keychain cache extended from 5s to 30s)

#### Major bug fixes

* Fixed `--resume` failing with "tool_use ids were found without tool_result blocks" on sessions created before v2.1.85
* Fixed Write/Edit/Read failing on files outside the project root (e.g., `~/.claude/CLAUDE.md`) when conditional skills or rules are configured
* Fixed unnecessary config disk writes on every skill invocation that could cause performance issues and config corruption on Windows
* Fixed potential out-of-memory crash when using `/feedback` on very long sessions with large transcript files
* Fixed `--bare` mode dropping MCP tools in interactive sessions and silently discarding messages enqueued mid-turn
* Fixed the `c` shortcut copying only ~20 characters of the OAuth login URL instead of the full URL
* Fixed masked input leaking the start of the token when wrapping across multiple lines on narrow terminals
* Fixed official marketplace plugin scripts failing with "Permission denied" on macOS/Linux since v2.1.83
* Fixed statusline showing another session's model when running multiple Claude Code instances
* Fixed scroll not following new messages after wheel scroll or click-to-select at the bottom of a long conversation
* Fixed `/plugin` uninstall dialog: pressing `n` now correctly uninstalls the plugin while preserving its data directory
* Fixed memory growth in long sessions from markdown/highlight render caches retaining full content strings
* [VSCode] Fixed extension incorrectly showing "Not responding" during long-running operations
* [VSCode] Fixed extension defaulting Max plan users to Sonnet after OAuth token refresh (8 hours after login)

-----

## Claude Code changes

### Changed documents

#### [Agent teams](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Clarified that `teammateMode` is now set in the global config (`~/.claude.json`) rather than `settings.json`. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/agent-teams.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/agent-teams#choose-a-display-mode)]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--tmux` flag added: creates a tmux session for the worktree (requires `--worktree`), using iTerm2 native panes when available or pass `--tmux=classic` for traditional tmux. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/cli-reference.md?plain=1#L86)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Claude directory](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* `.worktreeinclude` file added to the project file explorer and reference table, documenting it as the mechanism for copying gitignored files into new worktrees. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/claude-directory.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/claude-directory)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added explanation of how `origin/HEAD` determines the worktree base branch, including how to re-sync it after a remote default branch change (`git remote set-head origin -a`). [[lines 678-688](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/common-workflows.md?plain=1#L678-L688)] [[Source](https://code.claude.com/docs/en/common-workflows#run-parallel-claude-code-sessions-with-git-worktrees)]
* Clarified that `.worktreeinclude` is not processed when a custom `WorktreeCreate` hook is configured — copy local config files inside the hook script instead. [[line 744](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/common-workflows.md?plain=1#L744)] [[Source](https://code.claude.com/docs/en/common-workflows#non-git-version-control)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `ENABLE_TOOL_SEARCH` description updated: all MCP tools are now deferred by default (not just for first-party hosts); `true` always defers; `auto` is now threshold mode (load upfront if within 10% of context); `false` loads all upfront. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/env-vars.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New section "Filter by tool name and arguments with the `if` field" added, with a full example showing how to filter a `PreToolUse` hook to only git commands using `"if": "Bash(git *)"`. Requires Claude Code v2.1.85+. [[lines 574-604](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/hooks-guide.md?plain=1#L574-L604)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-by-tool-name-and-arguments-with-the-if-field)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `if` field added to common hook fields table: uses permission rule syntax (e.g. `"Bash(git *)"`, `"Edit(*.ts)"`) to filter when a handler runs; only evaluated on tool events. [[line 270](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/hooks.md?plain=1#L270)] [[Source](https://code.claude.com/docs/en/hooks#common-fields)]
* `AskUserQuestion` and `ExitPlanMode` added to the list of tool names supported by `PreToolUse` matchers. [[line 800](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/hooks.md?plain=1#L800)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse)]
* `AskUserQuestion` tool input documented: fields `questions` (array) and `answers` (object), with guidance on how hooks can programmatically answer questions in non-interactive mode by returning `updatedInput`. [[lines 900-910](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/hooks.md?plain=1#L900-L910)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-input)]
* `updatedInput` clarified to replace the entire input object — include unchanged fields alongside modified ones. Applies to both `PreToolUse` and `PermissionRequest`. [[line 917](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/hooks.md?plain=1#L917)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]
* WorktreeCreate hook: added note that `.worktreeinclude` is not processed when a hook replaces the default behavior — handle file copying inside the hook script. [[line 1592](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/hooks.md?plain=1#L1592)] [[Source](https://code.claude.com/docs/en/hooks#worktreecreate)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Removed the note that syntax highlighting is only available in the native build of Claude Code (now available in all builds).

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Six healthcare MCP servers (bioRxiv, ChEMBL, Clinical Trials, CMS Coverage, ICD-10 Codes, NPI Registry) migrated from `mcp.deepsense.ai` to `hcls.mcp.claude.com` URLs and moved to a new grouped section. [[lines 785-840](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/mcp.md?plain=1#L785-L840)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* New Zoho Desk MCP server added; Zoho Books, CRM, and Projects now include direct HTTP install commands. [[lines 841-860](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/mcp.md?plain=1#L841-L860)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* `headersHelper` documentation updated: two new environment variables (`CLAUDE_CODE_MCP_SERVER_NAME`, `CLAUDE_CODE_MCP_SERVER_URL`) are now set when the helper runs, enabling a single script to serve multiple MCP servers. [[lines 1367-1373](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/mcp.md?plain=1#L1367-L1373)] [[Source](https://code.claude.com/docs/en/mcp#use-dynamic-headers-for-custom-authentication)]
* OAuth metadata discovery clarified: Claude Code now checks RFC 9728 Protected Resource Metadata first, then falls back to RFC 8414 authorization server metadata. [[line 1311](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/mcp.md?plain=1#L1311)] [[Source](https://code.claude.com/docs/en/mcp#override-oauth-metadata-discovery)]
* `ENABLE_TOOL_SEARCH` table updated to reflect new default behavior (all tools deferred, not just first-party). [[lines 1641-1648](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/mcp.md?plain=1#L1641-L1648)] [[Source](https://code.claude.com/docs/en/mcp#configure-tool-search)]

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `none` added as a valid value for `OTEL_METRICS_EXPORTER` and `OTEL_LOGS_EXPORTER` to explicitly disable those exporters. [[lines 13-14](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/monitoring-usage.md?plain=1#L13-L14)] [[Source](https://code.claude.com/docs/en/monitoring-usage#quick-start)]
* `tool_input` truncation behavior clarified: individual values over 512 characters are truncated before the overall ~4K cap is applied. [[line 360](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/monitoring-usage.md?plain=1#L360)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]

#### [Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Added installation UI snippet showing tabs for Terminal, Desktop, VS Code, and JetBrains, plus macOS/Linux/Windows/Homebrew/WinGet options and the one-line curl install command. [[lines 5-18](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/quickstart.md?plain=1#L5-L18)] [[Source](https://code.claude.com/docs/en/quickstart)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `disableDeepLinkRegistration` setting: set to `"disable"` to prevent Claude Code from registering the `claude-cli://` protocol handler with the OS on startup. [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/settings.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `teammateMode` moved from project settings to global config settings (`~/.claude.json`). [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/settings.md?plain=1#L210)] [[Source](https://code.claude.com/docs/en/settings#global-config-settings)]
* Worktree settings section now references `.worktreeinclude` as the mechanism for copying gitignored files into worktrees. [[line 221](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/settings.md?plain=1#L221)] [[Source](https://code.claude.com/docs/en/settings#worktree-settings)]
* Plugin managed settings note added: managed settings can block plugin installation at all scopes and hide plugins from the marketplace. [[line 513](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/claude-code/settings.md?plain=1#L513)] [[Source](https://code.claude.com/docs/en/settings#enabledplugins)]

-----

## API changes

### Changed documents

#### [Agent SDK overview](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/overview.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/overview)]

* Skills location corrected from `.claude/skills/SKILL.md` to `.claude/skills/*/SKILL.md`. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/overview.md?plain=1#L161)] [[Source](https://platform.claude.com/docs/en/agent-sdk/overview)]

#### [Agent SDK - Python](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* New `get_session_info()` function: reads metadata for a single session by ID without scanning the full project directory. [[lines 314-345](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L314-L345)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* New `rename_session()` function: sets a custom title on a session; repeated calls are safe, last title wins. [[lines 347-378](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L347-L378)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* New `tag_session()` function: attaches a tag string to a session; pass `None` to clear. [[lines 380-423](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L380-L423)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* `SDKSessionInfo` gains two new fields: `tag` (user-set session tag) and `created_at` (creation timestamp in ms). [[lines 257-259](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L257-L259)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* `ClaudeSDKClient.get_mcp_status()` now returns `McpStatusResponse` (not a plain list). `add_mcp_server` and `remove_mcp_server` replaced by `reconnect_mcp_server`, `toggle_mcp_server`, and `stop_task`. [[lines 444-455](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L444-L455)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* `AgentDefinition` gains three new fields: `skills`, `memory`, and `mcpServers` for controlling subagent resources. [[lines 956-968](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L956-L968)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* New `McpServerStatusConfig` and `McpStatusResponse` types documented. [[lines 1215-1235](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L1215-L1235)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* New `RateLimitEvent` and `RateLimitInfo` types: emitted when rate limit status changes (e.g. `"allowed"` → `"allowed_warning"` → `"rejected"`). Added to the `Message` union type. [[lines 1426-1482](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L1426-L1482)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* `AssistantMessage` gains a `usage` field for per-message token counts. [[line 1348](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/python.md?plain=1#L1348)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

#### [Agent SDK - Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/sessions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/sessions)]

* Added mention of new session management functions (`get_session_info`, `rename_session`, `tag_session` in Python; `getSessionInfo`, `renameSession`, `tagSession` in TypeScript) for organizing sessions by tag or giving them human-readable titles. [[line 235](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/sessions.md?plain=1#L235)] [[Source](https://platform.claude.com/docs/en/agent-sdk/sessions)]

#### [Agent SDK - Subagents](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/subagents.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]

* `AgentDefinition` now supports three new fields: `skills` (list of skill names), `memory` (memory source), and `mcpServers` (MCP servers by name or inline config). [[lines 114-116](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/subagents.md?plain=1#L114-L116)] [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]
* `AgentDefinition.skills` now works in both Python and TypeScript (previously TypeScript only). [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/subagents.md?plain=1#L133)] [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]

#### [Agent SDK - TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* New `getSessionInfo()` function: reads metadata for a single session by ID. [[lines 202-220](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/typescript.md?plain=1#L202-L220)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* New `renameSession()` function: sets a custom title on a session. [[lines 222-240](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/typescript.md?plain=1#L222-L240)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* New `tagSession()` function: attaches a tag string to a session; pass `null` to clear. [[lines 242-260](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/typescript.md?plain=1#L242-L260)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* `SDKSessionInfo` gains two new fields: `tag` (user-set session tag) and `createdAt` (creation timestamp in ms). [[lines 136-137](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agent-sdk/typescript.md?plain=1#L136-L137)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

#### [Compaction](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Clarified that top-level `input_tokens`/`output_tokens` match the `message` iteration exactly when there is only one non-compaction iteration. [[line 389](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/build-with-claude/compaction.md?plain=1#L389)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]
* Link updated to a specific session memory compaction cookbook showing background threading and prompt caching. [[line 540](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/build-with-claude/compaction.md?plain=1#L540)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Clarified that cache failures below the minimum token threshold are silent — the request succeeds but both `cache_creation_input_tokens` and `cache_read_input_tokens` will be `0`. [[lines 268-271](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L268-L271)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* New guidance: if a prompt is just below the minimum, expanding cached content to reach the threshold is often worth the effort given the cost difference between cached and uncached tokens. [[lines 271-272](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L271-L272)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/9c76419274c4beb678ca0741727833673e10c384/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Postman MCP server added. ICD-10 Codes server URL updated to `hcls.mcp.claude.com`. Zoho Desk MCP server added. Various listing order changes.
