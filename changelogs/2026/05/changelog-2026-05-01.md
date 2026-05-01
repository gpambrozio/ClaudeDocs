# [Claude docs changes for May 1st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/68994d0eb02c9cbcf6d3394f411e398ab24623cd) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/68994d0eb02c9cbcf6d3394f411e398ab24623cd)]

## Executive Summary
- **New `claude project purge` command** cleans up all local Claude Code state (transcripts, tasks, history) for a project with dry-run and interactive options
- **`bypassPermissions` mode now truly bypasses all paths** including `.git`, `.claude`, `.vscode`; previously-protected paths now only retain a circuit breaker for root/home directory removals like `rm -rf /`
- **LLM gateway model auto-discovery**: when `ANTHROPIC_BASE_URL` points at a compatible gateway, Claude Code automatically populates the `/model` picker from the gateway's `/v1/models` endpoint (requires v2.1.126+)
- **`max_tokens=0` now supported** in the Messages API to pre-warm the prompt cache without generating a response
- **1M token context window beta retired** for Claude Sonnet 4.5 and Claude Sonnet 4; migrate to Claude Sonnet 4.6 or Opus 4.6 where it's generally available

## New Claude Code versions

### [2.1.126](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/versions/2.1.126.md)

#### New features

* `/model` picker now lists models from a gateway's `/v1/models` endpoint when `ANTHROPIC_BASE_URL` points at an Anthropic-compatible gateway
* Added `claude project purge [path]` command to delete all Claude Code state for a project (transcripts, tasks, debug logs, file-edit history, prompt history, config entry); supports `--dry-run`, `-y/--yes`, `-i/--interactive`, and `--all`
* `claude auth login` now accepts the OAuth code pasted into the terminal when the browser callback can't reach localhost (WSL2, SSH, containers)
* `claude_code.skill_activated` OpenTelemetry event now fires for user-typed slash commands and carries a new `invocation_trigger` attribute (`"user-slash"`, `"claude-proactive"`, or `"nested-skill"`)

#### Existing feature improvements

* `--dangerously-skip-permissions` now bypasses prompts for writes to `.claude/`, `.git/`, `.vscode/`, shell config files, and other previously-protected paths (catastrophic removal commands like `rm -rf /` still prompt as a safety net)
* Auto mode: the spinner now turns red when a permission check stalls, instead of looking like the tool is running
* Host-managed deployments (`CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST`) no longer auto-disable analytics on Bedrock/Vertex/Foundry
* Windows: PowerShell 7 installed via the Microsoft Store, MSI without PATH, or `.NET global tool` is now detected
* Windows: when the PowerShell tool is enabled, Claude now treats PowerShell as the primary shell instead of defaulting to Bash
* Read tool: removed the per-file malware-assessment reminder that could cause spurious refusals on legacy models

#### Major bug fixes

* **Security:** Fixed `allowManagedDomainsOnly` / `allowManagedReadPathsOnly` being ignored when a higher-priority managed-settings source lacked a `sandbox` block
* Fixed pasting an image larger than 2000px breaking the session — images are now downscaled on paste, and oversized images in history are automatically removed and the request retried
* Fixed OAuth login failing with timeout on slow or proxied connections, in IPv6-only devcontainers, and when the browser callback can't reach localhost
* Fixed "Stream idle timeout" error after waking Mac from sleep mid-request
* Fixed background and remote sessions falsely aborting with "Stream idle timeout" during long model thinking pauses
* Fixed a hang where the assistant could finish thinking but show no output after a run of empty turns
* Fixed overly fast trackpad scrolling in Cursor and VS Code 1.92–1.104 integrated terminals
* Fixed Japanese/Korean/Chinese text rendering as garbled characters on Windows in no-flicker mode
* Fixed `Ctrl+L` clearing the prompt input — it now only forces a screen redraw, matching readline behavior
* Fixed deferred tools (WebSearch, WebFetch, etc.) not being available to skills with `context: fork` and other subagents on their first turn
* Fixed plan-mode tools being unavailable in interactive sessions launched with `--channels`
* Fixed Agent SDK hang when the model emits a malformed tool name in a parallel tool call batch
* Windows: clipboard writes no longer expose copied content in process command-line arguments visible to EDR/SIEM telemetry; also fixes >22KB selections not reaching the clipboard

-----

## Claude Code changes

### Changed documents

#### [Agent SDK - TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added new `SDKMessageOrigin` type documenting the provenance of user-role messages (`human`, `channel`, `peer`, `task-notification`, `coordinator`). [[line 1007](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1007)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkpermissiondenial)]
* Added `origin` field to `SDKUserMessage`, `SDKUserMessageReplay`, and `SDKResultMessage` types, with explanation that `origin: { kind: "task-notification" }` identifies synthetic turns from background tasks. [[line 844](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L844)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkusermessage)]
* Added `oauth_org_not_allowed` to the `SDKAssistantMessageError` union type. [[line 828](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L828)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkassistantmessage)]

#### [Analytics](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Added note that per-user token counts and cost estimates require configuring OpenTelemetry export. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/analytics.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/analytics#access-analytics-for-team-and-enterprise)]

#### [Authentication](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Clarified that the OAuth code-paste flow occurs specifically when the browser can't reach Claude Code's local callback server (common in WSL2, SSH sessions, and containers). [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/authentication.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/authentication#log-in-to-claude-code)]

#### [Auto Mode Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* Added explicit note that auto mode is available on Max, Team, Enterprise, and API plans only — not on Pro or on Bedrock/Vertex/Foundry. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/auto-mode-config.md?plain=1#L10)] [[Source](https://code.claude.com/docs/en/auto-mode-config)]

#### [Claude Directory](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Added comprehensive documentation for the new `claude project purge` command, including what it deletes, all flag options (`--dry-run`, `--yes`, `-i`, `--all`), and what it leaves untouched. [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/claude-directory.md?plain=1#L222)] [[Source](https://code.claude.com/docs/en/claude-directory#clear-local-data)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `claude project purge [path]` to the CLI command table with full flag documentation. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/cli-reference.md?plain=1#L31)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Added clarification that a command is only recognized at the start of a message; text following the command name is passed as arguments. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/commands.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/commands)]

#### [Data Usage](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Added note that as of v2.1.126, when `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` is set, Statsig metrics default to on for Vertex/Bedrock/Foundry and follow the standard `DISABLE_TELEMETRY` opt-out. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/data-usage.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/data-usage#default-behaviors-by-api-provider)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_PROVIDER_MANAGED_BY_HOST` variable: set by host platforms to manage provider routing and skip automatic telemetry opt-outs. [[line 128](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/env-vars.md?plain=1#L128)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Added `DISABLE_GROWTHBOOK` variable to disable GrowthBook feature-flag fetching and use code defaults. [[line 173](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/env-vars.md?plain=1#L173)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Updated `CLAUDE_STREAM_IDLE_TIMEOUT_MS`: default and minimum is now `300000` (5 min) for both byte-level and event-level watchdogs. [[line 164](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/env-vars.md?plain=1#L164)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Updated `Ctrl+L` description: the first press now redraws the screen (no longer clears input) and shows a hint; the second press clears the conversation. [[line 108](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/fullscreen.md?plain=1#L108)] [[Source](https://code.claude.com/docs/en/fullscreen#clear-the-conversation)]

#### [Headless Mode](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Added `oauth_org_not_allowed` to the error category enum in the system/api-retry event. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/headless.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/headless#stream-responses)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `oauth_org_not_allowed` as a new error type for the `StopFailure` hook event. [[line 201](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/hooks.md?plain=1#L201)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added `oauth_org_not_allowed` as a new error type for the `StopFailure` hook event matcher. [[line 561](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/hooks-guide.md?plain=1#L561)] [[Source](https://code.claude.com/docs/en/hooks-guide#filter-hooks-with-matchers)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated `Ctrl+L` description: now only redraws screen, input and history are preserved. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/interactive-mode.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* Added `Ctrl+S` shortcut to cycle history search scope between session, project, and all projects. [[line 214](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/interactive-mode.md?plain=1#L214)] [[Source](https://code.claude.com/docs/en/interactive-mode#reverse-search-with-ctrl+r)]

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Updated `chat:clearInput` (`Ctrl+L`) description: now forces a screen redraw while preserving input. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/keybindings.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/keybindings#chat-actions)]
* Added `historySearch:cycleScope` action (`Ctrl+S`) to cycle between session, project, and everywhere scopes. [[line 173](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/keybindings.md?plain=1#L173)] [[Source](https://code.claude.com/docs/en/keybindings#history-search-actions)]

#### [LLM Gateway](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/llm-gateway.md) [[Source](https://code.claude.com/docs/en/llm-gateway)]

* Documented new automatic model discovery: when `ANTHROPIC_BASE_URL` points at an Anthropic-format gateway, Claude Code queries `/v1/models` at startup and adds results to the `/model` picker labeled "From gateway". Results are cached to `~/.claude/cache/gateway-models.json`. Requires v2.1.126+. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/llm-gateway.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/llm-gateway#model-selection)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Clarified CLAUDE.md load order: content is ordered from filesystem root down to working directory, so instructions closer to the launch directory are read last (higher priority). [[line 126](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/memory.md?plain=1#L126)] [[Source](https://code.claude.com/docs/en/memory#how-claude-md-files-load)]

#### [Model Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Updated `ANTHROPIC_CUSTOM_MODEL_OPTION` description: clarified it's mainly for models not returned by gateway auto-discovery; for LLM gateways, the picker is now auto-populated. [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/model-config.md?plain=1#L232)] [[Source](https://code.claude.com/docs/en/model-config#add-a-custom-model-option)]

#### [Monitoring Usage](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Added `invocation_trigger` attribute to the `claude_code.skill_activated` OTel event, indicating how the skill was triggered (`"user-slash"`, `"claude-proactive"`, or `"nested-skill"`). [[line 686](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/monitoring-usage.md?plain=1#L686)] [[Source](https://code.claude.com/docs/en/monitoring-usage#skill-activated-event)]

#### [Permission Modes](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Updated `bypassPermissions` mode description: as of v2.1.126 it now bypasses all paths including previously-protected ones; only root/home directory removals still prompt as a circuit breaker. [[line 213](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/permission-modes.md?plain=1#L213)] [[Source](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)]
* Updated protected paths section to clarify they apply in every mode except `bypassPermissions`. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/permission-modes.md?plain=1#L225)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]
* Added that `acceptEdits` mode auto-approves PowerShell file-write cmdlets (`Set-Content`, `Add-Content`, etc.) on in-scope paths when the PowerShell tool is enabled. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/permission-modes.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/permission-modes#auto-approve-file-edits-with-acceptedits-mode)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Updated `bypassPermissions` mode table entry and description to reflect that it now skips all prompts; removals of root/home still prompt as a circuit breaker. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/permissions.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]
* Added new PowerShell permission rules section documenting wildcard matching, alias canonicalization, and AST-based compound command parsing. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/permissions.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/permissions#powershell)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `preferredNotifChannel` setting to control notification method (`"auto"`, `"terminal_bell"`, `"iterm2"`, `"iterm2_with_bell"`, `"kitty"`, `"ghostty"`, or `"notifications_disabled"`). [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/settings.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Added note that if `claude` still runs after uninstall, it may be a second installation or leftover shell alias from an older installer, with a link to the troubleshooting guide. [[line 429](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/setup.md?plain=1#L429)] [[Source](https://code.claude.com/docs/en/setup#uninstall-claude-code)]

#### [Sub-Agents](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added note that `permissionMode`, `mcpServers`, and `hooks` frontmatter fields are ignored for plugin subagents. [[line 234](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/sub-agents.md?plain=1#L234)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* Updated `bypassPermissions` caution note: it now skips all prompts including `.git`/`.claude`/`.vscode`/`.idea`/`.husky`; root/home removals still prompt. [[line 361](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/sub-agents.md?plain=1#L361)] [[Source](https://code.claude.com/docs/en/sub-agents#permission-modes)]

#### [Terminal Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Updated notification section: referenced new `preferredNotifChannel` setting as an alternative to hooks for terminals that don't receive desktop notifications. [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/terminal-config.md?plain=1#L54)] [[Source](https://code.claude.com/docs/en/terminal-config#get-a-terminal-bell-or-notification)]

#### [Tools Reference](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Updated Windows PowerShell tool description: when enabled, Claude now treats PowerShell as the primary shell; Bash remains available for POSIX scripts when Git Bash is installed. [[line 108](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/tools-reference.md?plain=1#L108)] [[Source](https://code.claude.com/docs/en/tools-reference#enable-the-powershell-tool)]

#### [Troubleshoot Installation](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Expanded OAuth troubleshooting section (renamed from "WSL2" to "WSL2, SSH, or containers") to cover SSH sessions and containers. Improved guidance for pasting the OAuth code and using `claude auth login` as a fallback. [[line 681](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/claude-code/troubleshoot-install.md?plain=1#L681)] [[Source](https://code.claude.com/docs/en/troubleshoot-install#oauth-login-fails-in-wsl2-ssh-or-containers)]

-----

## API changes

### Changed documents

#### [API Beta Reference](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Added `user-profiles-2026-03-24` to the list of recognized beta header values (now 20+ members). [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta.md?plain=1#L63)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* Added `xhigh` effort level to `BetaEffortCapability`, expanding the capability from 2 to 3 additional members. [[line 295](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta.md?plain=1#L295)] [[Source](https://platform.claude.com/docs/en/api/beta)]

#### [Beta Messages Create](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* `max_tokens` minimum changed from `1` to `0`; added documentation that `max_tokens: 0` populates the prompt cache without generating a response. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta/messages/create.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Added `encrypted_content` field to `BetaCompactionBlockParam` for round-tripping opaque metadata from prior compaction. [[line 2501](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta/messages/create.md?plain=1#L2501)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Added `xhigh` effort level to the `output_config.effort` enum. [[line 2841](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta/messages/create.md?plain=1#L2841)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

#### [Beta Models](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta/models.md) [[Source](https://platform.claude.com/docs/en/api/beta/models)]

* Added `xhigh` effort level to `BetaEffortCapability` in model capability info. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/beta/models.md?plain=1#L59)] [[Source](https://platform.claude.com/docs/en/api/beta/models)]

#### [Messages Create (TypeScript)](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/typescript/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/typescript/messages/create)]

* `max_tokens` minimum changed from `1` to `0` with added documentation for cache pre-warming use case. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/typescript/messages/create.md?plain=1#L31)] [[Source](https://platform.claude.com/docs/en/api/typescript/messages/create)]
* Added `xhigh` to the `effort` enum in `output_config`. [[line 2280](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/api/typescript/messages/create.md?plain=1#L2280)] [[Source](https://platform.claude.com/docs/en/api/typescript/messages/create)]

#### [Pricing](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Removed "Long context premium" from the list of pricing modifiers that do not apply to Claude Managed Agents — long context pricing now applies to Managed Agents sessions. [[line 304](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/about-claude/pricing.md?plain=1#L304)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [Release Notes Overview](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added April 30, 2026 entry: the 1M token context window beta (`context-1m-2025-08-07`) is retired for Claude Sonnet 4.5 and Claude Sonnet 4. Requests exceeding 200k tokens now return an error. Users should migrate to Claude Sonnet 4.6 or Claude Opus 4.6 where 1M context is GA at standard pricing. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/68994d0eb02c9cbcf6d3394f411e398ab24623cd/docs-md/api/release-notes/overview.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
