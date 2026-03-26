# [Claude docs changes for March 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/bd6d3a7614b3508941402391311ad1dc1a8cef8d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/bd6d3a7614b3508941402391311ad1dc1a8cef8d)]

## Executive Summary
- PowerShell tool added for Windows as an opt-in preview, enabling Claude to run PowerShell commands natively instead of routing through Git Bash
- Two new hook events: `CwdChanged` (fires on directory changes) and `FileChanged` (fires on watched file changes), both with `CLAUDE_ENV_FILE` support for environment reloading via tools like direnv
- New `allowedChannelPlugins` managed setting lets Team/Enterprise admins restrict which channel plugins can deliver messages
- Model configuration expanded for third-party providers: new env vars let admins customize display names and declare capabilities for pinned Bedrock/Vertex/Foundry models
- VS Code extension gains a URI handler (`vscode://anthropic.claude-code/open`) to open Claude Code tabs from external tooling

## New Claude Code versions

### [2.1.84](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/versions/2.1.84.md)

#### New features

* Added PowerShell tool for Windows as an opt-in preview (`CLAUDE_CODE_USE_POWERSHELL_TOOL=1`)
* Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_SUPPORTS` env vars to override capability detection for pinned third-party provider models, plus `_MODEL_NAME`/`_DESCRIPTION` to customize the `/model` picker label
* Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` env var to configure the streaming idle watchdog threshold (default 90s)
* Added `TaskCreated` hook that fires when a task is created via `TaskCreate`
* Added `WorktreeCreate` hook support for `type: "http"` — return the created worktree path via `hookSpecificOutput.worktreePath`
* Added `allowedChannelPlugins` managed setting for Team/Enterprise admins to define a channel plugin allowlist
* Added `x-client-request-id` header to API requests for debugging timeouts
* Added idle-return prompt that nudges users returning after 75+ minutes to `/clear`
* Deep links (`claude-cli://`) now open in your preferred terminal
* Rules and skills `paths:` frontmatter now accepts a YAML list of globs

#### Existing feature improvements

* MCP tool descriptions and server instructions are now capped at 2KB to prevent OpenAPI-generated servers from bloating context
* MCP servers configured both locally and via claude.ai connectors are now deduplicated — the local config wins
* Background bash tasks that appear stuck on an interactive prompt now surface a notification after ~45 seconds
* Token counts ≥1M now display as "1.5m" instead of "1512.6k"
* Global system-prompt caching now works when `ToolSearch` is enabled, including for users with MCP tools configured
* Stats screenshot (Ctrl+S in /stats) is now 16× faster and works in all builds
* Changed issue/PR references to only become clickable links when written as `owner/repo#123` — bare `#123` is no longer auto-linked
* Slash commands unavailable for the current auth setup are now hidden instead of shown
* [VSCode] Added rate limit warning banner with usage percentage and reset time

#### Major bug fixes

* Fixed voice push-to-talk: holding the voice key no longer leaks characters into the text input
* Fixed up/down arrow keys being unresponsive when a footer item is focused
* Fixed `Ctrl+U` (kill-to-line-start) being a no-op at line boundaries in multiline input
* Fixed null-unbinding a default chord binding still entering chord-wait mode
* Fixed workflow subagents failing with API 400 when the outer session uses `--json-schema`
* Fixed the "allow Claude to edit its own settings" permission option not sticking
* Fixed MCP tool/resource cache leak on server reconnect
* Fixed a startup performance issue with partial clone repositories (Scalar/GVFS)
* Fixed native terminal cursor not tracking the text input caret (IME/CJK input)
* Fixed spurious "Not logged in" errors on macOS from transient keychain failures
* Fixed cold-start race where core tools could fail with `InputValidationError` on typed parameters

-----

## Claude Code changes

### Changed documents

#### [channels-reference](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/channels-reference.md) [[Source](https://code.claude.com/docs/en/channels-reference)]

* Added note that Team/Enterprise admins can use `allowedChannelPlugins` as an alternative to the official Anthropic allowlist for organization-specific channel plugins. [[line 873](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/channels-reference.md?plain=1#L873)] [[Source](https://code.claude.com/docs/en/channels-reference#package-as-a-plugin)]

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Rewrote enterprise controls section: channels now off by default for Team/Enterprise, with a two-setting model (`channelsEnabled` + `allowedChannelPlugins`). [[lines 384-410](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/channels.md?plain=1#L384-L410)] [[Source](https://code.claude.com/docs/en/channels#security)]
* New section documenting how to restrict which channel plugins can run via `allowedChannelPlugins`, including configuration example. [[lines 415-430](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/channels.md?plain=1#L415-L430)] [[Source](https://code.claude.com/docs/en/channels#restrict-which-channel-plugins-can-run)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `claude plugin` command entry (manages Claude Code plugins; alias `claude plugins`). [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/cli-reference.md?plain=1#L21)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_NAME`, `_DESCRIPTION`, and `_SUPPORTED_CAPABILITIES` env vars for customizing pinned model display and capability declarations on third-party providers. [[lines 14-24](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/env-vars.md?plain=1#L14-L24)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Added `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK` to disable fallback when streaming fails mid-stream (useful when a proxy causes duplicate tool execution). [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/env-vars.md?plain=1#L56)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` to strip credentials from subprocess environments (Bash, hooks, MCP stdio), reducing prompt-injection exfiltration risk. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/env-vars.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Added `CLAUDE_CODE_USE_POWERSHELL_TOOL` to enable the PowerShell tool on Windows (opt-in preview). [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/env-vars.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Updated `CLAUDE_ENV_FILE` description to mention `CwdChanged` and `FileChanged` hooks in addition to `SessionStart`. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/env-vars.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New example section "Reload environment when directory or files change" showing how to use `CwdChanged` and `FileChanged` hooks with direnv. [[lines 325-385](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks-guide.md?plain=1#L325-L385)] [[Source](https://code.claude.com/docs/en/hooks-guide#audit-configuration-changes)]
* Added `CwdChanged` and `FileChanged` to the event reference table. [[lines 460-461](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks-guide.md?plain=1#L460-L461)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `CwdChanged` hook event: fires when working directory changes (e.g., via `cd`), useful for reactive environment management with direnv. [[lines 31-32](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md?plain=1#L31-L32)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* Added `FileChanged` hook event: fires when a watched file changes on disk; `matcher` specifies which basenames to watch. [[lines 31-32](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md?plain=1#L31-L32)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* Added `shell` field to command hooks, accepting `"bash"` (default) or `"powershell"`, to run individual hooks via PowerShell on Windows. [[line 309](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md?plain=1#L309)] [[Source](https://code.claude.com/docs/en/hooks#command-hook-fields)]
* Updated `WorktreeCreate` to support HTTP hooks: HTTP hooks return the worktree path via `hookSpecificOutput.worktreePath` instead of stdout. [[lines 1637-1648](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md?plain=1#L1637-L1648)] [[Source](https://code.claude.com/docs/en/hooks#configchange)]
* `CLAUDE_ENV_FILE` is now available for `CwdChanged` and `FileChanged` hooks, allowing hooks to persist environment variables into subsequent Bash commands. [[line 819](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md?plain=1#L819)] [[Source](https://code.claude.com/docs/en/hooks#persist-environment-variables)]
* New full reference sections for `CwdChanged` and `FileChanged` including input schemas, `watchPaths` output field, and usage examples. [[lines 1714-1800](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md?plain=1#L1714-L1800)] [[Source](https://code.claude.com/docs/en/hooks#configchange-decision-control)]
* New section "Windows PowerShell tool" with example for running hooks via PowerShell using `"shell": "powershell"`. [[lines 2469-2499](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md?plain=1#L2469-L2499)] [[Source](https://code.claude.com/docs/en/hooks#security-best-practices)]
* `SessionStart` now documented as supporting only `command` hooks (previously listed alongside events that also support `http`/`prompt`/`agent`). [[line 2206](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/hooks.md?plain=1#L2206)] [[Source](https://code.claude.com/docs/en/hooks#prompt-hook-configuration)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* New section documenting the VS Code URI handler `vscode://anthropic.claude-code/open`, including `prompt` and `session` query parameters for pre-filling prompts or resuming conversations from external tooling. [[lines 216-253](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/ide-integrations.md?plain=1#L216-L253)] [[Source](https://code.claude.com/docs/en/ide-integrations#launch-a-vs-code-tab-from-other-tools)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Ctrl+F` (kill all background agents) replaced by `Ctrl+X Ctrl+K`. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/interactive-mode.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* `Ctrl+G` now also has `Ctrl+X Ctrl+E` as the readline-native binding for opening external editor. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/interactive-mode.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* New `Option+O` / `Alt+O` shortcut to toggle fast mode. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/interactive-mode.md?plain=1#L31)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* New "Transcript viewer" shortcuts section documenting `Ctrl+E` and exit keys. [[lines 72-80](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/interactive-mode.md?plain=1#L72-L80)] [[Source](https://code.claude.com/docs/en/interactive-mode#transcript-viewer)]
* Background task output is now written to a file and retrieved via the `Read` tool (previously buffered and retrieved via `TaskOutput`). [[line 203](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/interactive-mode.md?plain=1#L203)] [[Source](https://code.claude.com/docs/en/interactive-mode#how-backgrounding-works)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Added `chat:killAgents` action (default `Ctrl+X Ctrl+K`). [[line 100](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/keybindings.md?plain=1#L100)] [[Source](https://code.claude.com/docs/en/keybindings#chat-actions)]
* Added `chat:fastMode` action (default `Meta+O`). [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/keybindings.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/keybindings#chat-actions)]
* `chat:externalEditor` now has two default bindings: `Ctrl+G` and `Ctrl+X Ctrl+E`. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/keybindings.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/keybindings#chat-actions)]
* Added `footer:up` and `footer:down` actions for navigating the footer. [[lines 219-220](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/keybindings.md?plain=1#L219-L220)] [[Source](https://code.claude.com/docs/en/keybindings#footer-actions)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added new remote MCP servers: Gainsight (Staircase AI), pg-aiguide (TimescaleDB/Tiger docs), and CB Insights.

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* New `AGENTS.md` section explaining how to import an existing `AGENTS.md` into `CLAUDE.md` for cross-agent compatibility. [[lines 100-115](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/memory.md?plain=1#L100-L115)] [[Source](https://code.claude.com/docs/en/memory#import-additional-files)]
* Block-level HTML comments in CLAUDE.md files are now stripped before context injection, allowing maintainer notes without spending tokens. [[line 128](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/memory.md?plain=1#L128)] [[Source](https://code.claude.com/docs/en/memory#how-claude-md-files-load)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Updated effort level documentation: `max` now persists only via `CLAUDE_CODE_EFFORT_LEVEL` env var (not across sessions via `/effort`); Sonnet 4.6 also defaults to medium effort; added guidance that medium is recommended for most coding tasks. [[lines 144-154](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/model-config.md?plain=1#L144-L154)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]
* New section "Customize pinned model display and capabilities" documenting `ANTHROPIC_DEFAULT_{OPUS,SONNET,HAIKU}_MODEL_NAME`, `_DESCRIPTION`, and `_SUPPORTED_CAPABILITIES` env vars for third-party providers, with a capability values table. [[lines 266-308](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/model-config.md?plain=1#L266-L308)] [[Source](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `OTEL_LOG_TOOL_DETAILS` now also logs tool input arguments (file paths, URLs, search patterns, etc.) as a `tool_input` attribute, bounded to ~4K characters. [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/monitoring-usage.md?plain=1#L89)] [[Source](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Added `CwdChanged` and `FileChanged` to the plugin hook events table. [[lines 127-128](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/plugins-reference.md?plain=1#L127-L128)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]
* New `userConfig` field: declares values Claude Code prompts users for at plugin enable time, stored in settings or system keychain. [[lines 370-395](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/plugins-reference.md?plain=1#L370-L395)] [[Source](https://code.claude.com/docs/en/plugins-reference#user-configuration)]
* New `channels` field: lets a plugin declare message channels bound to an MCP server, with per-channel `userConfig`. [[lines 397-420](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/plugins-reference.md?plain=1#L397-L420)] [[Source](https://code.claude.com/docs/en/plugins-reference#channels)]
* Corrected path behavior: custom `commands`, `agents`, `skills`, and `outputStyles` paths now replace (not supplement) the default directory. [[lines 422-430](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/plugins-reference.md?plain=1#L422-L430)] [[Source](https://code.claude.com/docs/en/plugins-reference#path-behavior-rules)]
* Added `output-styles/` directory to the plugin structure and file locations reference. [[lines 592-593](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/plugins-reference.md?plain=1#L592-L593)] [[Source](https://code.claude.com/docs/en/plugins-reference#standard-plugin-layout)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Added note about `sandbox.failIfUnavailable` setting: when `true`, Claude Code fails at startup if sandbox cannot start, intended for managed deployments requiring sandboxing as a security gate. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/sandboxing.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/sandboxing#enable-sandboxing)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `useAutoModeDuringPlan` setting to control whether plan mode uses auto mode semantics. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/settings.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `defaultShell` setting (`"bash"` or `"powershell"`) for routing `!` commands through PowerShell on Windows. [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/settings.md?plain=1#L160)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `allowedChannelPlugins` managed setting (Team/Enterprise): allowlist of channel plugins that can push messages, replacing the Anthropic default list when set. [[line 184](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/settings.md?plain=1#L184)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `sandbox.failIfUnavailable` setting to make sandbox startup failures a hard error. [[line 258](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/settings.md?plain=1#L258)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]
* Documented drop-in directory support for managed settings: `managed-settings.d/*.json` files are alphabetically sorted and merged on top of `managed-settings.json`. [[lines 91-96](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/settings.md?plain=1#L91-L96)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Added note about PowerShell tool opt-in preview for native Windows usage. [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/setup.md?plain=1#L133)] [[Source](https://code.claude.com/docs/en/setup#set-up-on-windows)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Updated `/debug` description: it now enables debug logging mid-session (logs are off by default unless started with `--debug`). [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/skills.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/skills#bundled-skills)]
* Added `shell` frontmatter field (`bash` or `powershell`) for running inline shell commands in skills via PowerShell on Windows. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/skills.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added `initialPrompt` frontmatter field: auto-submitted as the first user turn when the agent runs as the main session agent. [[line 255](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/sub-agents.md?plain=1#L255)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* Documented subagent model resolution order: `CLAUDE_CODE_SUBAGENT_MODEL` env var > per-invocation `model` parameter > subagent frontmatter `model` > main conversation's model. [[lines 265-271](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/sub-agents.md?plain=1#L265-L271)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-a-model)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Added `PowerShell` tool entry (Windows opt-in preview, requires `CLAUDE_CODE_USE_POWERSHELL_TOOL=1`). [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/tools-reference.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/tools-reference)]
* `TaskOutput` tool marked as deprecated; prefer `Read` on the task's output file path. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/tools-reference.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/tools-reference)]
* New "PowerShell tool" section documenting how to enable, shell selection settings, and current preview limitations. [[lines 47-90](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/tools-reference.md?plain=1#L47-L90)] [[Source](https://code.claude.com/docs/en/tools-reference#bash-tool-behavior)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* New section documenting the VS Code URI handler `vscode://anthropic.claude-code/open` with `prompt` and `session` query parameters. [[lines 216-253](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/claude-code/vs-code.md?plain=1#L216-L253)] [[Source](https://code.claude.com/docs/en/vs-code#launch-a-vs-code-tab-from-other-tools)]

-----

## API changes

### Changed documents

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/bd6d3a7614b3508941402391311ad1dc1a8cef8d/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added new remote MCP servers: tldraw (sketch/draw/diagram), Intuit QuickBooks (business finances), CB Insights (private company intelligence), Gainsight Staircase AI (customer context), pg-aiguide (PostgreSQL/Tiger docs), and MSCI (updated URL and description).
