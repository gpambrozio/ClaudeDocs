# [Claude docs changes for March 25th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e98523a) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e98523a)]

## Executive Summary
- **Auto mode launched (research preview)**: A new permission mode where a background classifier model reviews actions and blocks only risky ones (scope escalation, unknown infrastructure, prompt-injection-driven commands), eliminating most permission prompts while maintaining safety oversight. Available on Team plans with Sonnet 4.6 or Opus 4.6.
- **iMessage channel added**: Claude Code can now receive and reply to iMessages directly from your local session — no bot token required, macOS only.
- **Security warning for LiteLLM**: Versions 1.82.7 and 1.82.8 of the LiteLLM PyPI package were compromised with credential-stealing malware. Users should remove affected versions and rotate credentials.
- **New `permission-modes.md` guide**: Comprehensive new document covering all six permission modes, how to switch between them across CLI/VS Code/Desktop/Web, and deep coverage of auto mode configuration.
- **`managed-settings.d/` drop-in directory**: Teams can now deploy independent policy fragments that merge alphabetically instead of maintaining a monolithic `managed-settings.json`.

-----

## New Claude Code versions

### [2.1.83](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/versions/2.1.83.md)

#### New features

* Added `managed-settings.d/` drop-in directory alongside `managed-settings.json`, letting separate teams deploy independent policy fragments that merge alphabetically
* Added `CwdChanged` and `FileChanged` hook events for reactive environment management (e.g., direnv integration)
* Added `sandbox.failIfUnavailable` setting to exit with an error when sandbox is enabled but cannot start
* Added `disableDeepLinkRegistration` setting to prevent `claude-cli://` protocol handler registration
* Added `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB=1` to strip Anthropic and cloud provider credentials from subprocess environments (Bash tool, hooks, MCP stdio servers)
* Added transcript search — press `/` in transcript mode (`Ctrl+O`) to search, `n`/`N` to step through matches
* Added `Ctrl+X Ctrl+E` as an alias for opening the external editor (readline-native binding; `Ctrl+G` still works)
* Pasted images now insert an `[Image #N]` chip at the cursor so you can reference them positionally in your prompt
* Agents can now declare `initialPrompt` in frontmatter to auto-submit a first turn
* `chat:killAgents` and `chat:fastMode` are now rebindable via `~/.claude/keybindings.json`
* Plugin options (`manifest.userConfig`) now available externally — plugins can prompt for configuration at enable time, with `sensitive: true` values stored in keychain (macOS) or protected credentials file (other platforms)
* Claude can now reference the on-disk path of clipboard-pasted images for file operations
* `Ctrl+L` now clears the screen and forces a full redraw
* Added `CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK` env var to disable the non-streaming fallback when streaming fails
* [VSCode] Added Esc-twice (or `/rewind`) to open a keyboard-navigable rewind picker

#### Existing feature improvements

* Improved Bedrock SDK cold-start latency by overlapping profile fetch with other boot work
* Improved `--resume` memory usage and startup latency on large sessions
* Improved plugin startup — commands, skills, and agents now load from disk cache without re-fetching
* Improved Remote Control session titles: AI-generated titles now appear within seconds of the first message
* Improved `WebFetch` to identify as `Claude-User` so site operators can recognize and allowlist Claude Code traffic via `robots.txt`
* Reduced `WebFetch` peak memory usage for large pages
* Reduced scrollback resets in long sessions from once per turn to once per ~50 messages
* Faster `claude -p` startup with unauthenticated HTTP/SSE MCP servers (~600ms saved)
* Increased non-streaming fallback token cap (21k → 64k) and timeout (120s → 300s local) so fallback requests are less likely to be truncated
* Interrupting a prompt before any response now automatically restores your input so you can edit and resubmit
* `/status` now works while Claude is responding, instead of being queued until the turn finishes
* Changed "stop all background agents" keybinding from `Ctrl+F` to `Ctrl+X Ctrl+K` to stop shadowing readline forward-char
* `--bare -p` (SDK pattern) is ~14% faster to the API request
* `MEMORY.md` index now truncates at 25KB as well as 200 lines
* Deprecated `TaskOutput` tool in favor of using `Read` on the background task's output file path
* [VSCode] Spinner now turns red with "Not responding" when the backend hasn't responded for 60 seconds

#### Major bug fixes

* Fixed Claude Code hanging on exit on macOS
* Fixed a 1–8 second UI freeze on startup when voice input was enabled, caused by eagerly loading the native audio module
* Fixed a startup regression where Claude Code would wait ~3s for claude.ai MCP config fetch before proceeding
* Fixed `--mcp-config` CLI flag bypassing `allowedMcpServers`/`deniedMcpServers` managed policy enforcement
* Fixed background subagents becoming invisible after context compaction, which could cause duplicate agents to be spawned
* Fixed `rg ... | wc -l` and similar piped commands hanging and returning `0` in sandbox mode on Linux
* Fixed tool result files never being cleaned up, ignoring the `cleanupPeriodDays` setting
* Fixed remote sessions forgetting conversation history after a container restart due to progress-message gaps in the resumed transcript chain
* Fixed `--worktree` hanging silently when the worktree name contained a forward slash
* Fixed claude.ai MCP connectors (Slack, Gmail, etc.) not being available in single-turn `--print` mode
* Fixed `caffeinate` process not properly terminating when Claude Code exits, preventing Mac from sleeping
* [VSCode] Fixed session history not loading correctly when reopening a session via URL or after restart
* [VSCode] Fixed "Fork conversation from here" and rewind actions failing silently after the session cache goes stale

-----

## Claude Code changes

### New Documents

#### [Permission modes](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

Comprehensive new guide covering all six permission modes (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`). Explains how to switch modes at runtime, startup, and as defaults across CLI, JetBrains, VS Code, Desktop, and Web/mobile. Deep coverage of the new auto mode (research preview): how the classifier model evaluates actions, what it blocks and allows by default, how subagents inherit it, and fallback behavior when the classifier blocks too many actions. Also covers `dontAsk` mode for locked-down CI environments.

### Changed documents

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added auto mode as a third option for reducing interruptions alongside permission allowlists and sandboxing. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/best-practices.md?plain=1#L225)] [[Source](https://code.claude.com/docs/en/best-practices#configure-permissions)]
* Added new "Run autonomously with auto mode" section for non-interactive `-p` runs using `--permission-mode auto`. [[line 582](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/best-practices.md?plain=1#L582)] [[Source](https://code.claude.com/docs/en/best-practices#run-autonomously-with-auto-mode)]

#### [Channels](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Added iMessage as a supported channel. Full setup instructions covering Full Disk Access grant, plugin installation, restart, self-text pairing, and how to allow additional senders by handle. [[line 231](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/channels.md?plain=1#L231)] [[Source](https://code.claude.com/docs/en/channels#supported-channels)]

#### [Channels reference](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/channels-reference.md) [[Source](https://code.claude.com/docs/en/channels-reference)]

* Added iMessage to the list of channels included in the research preview. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/channels-reference.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/channels-reference)]
* Added note that iMessage detects the user's own addresses from the Messages database automatically, with other senders added by handle. [[line 509](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/channels-reference.md?plain=1#L509)] [[Source](https://code.claude.com/docs/en/channels-reference#gate-inbound-messages)]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `claude auto-mode defaults` command to print built-in auto mode classifier rules as JSON (also covers `claude auto-mode config`). [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/cli-reference.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]
* Added `--enable-auto-mode` flag to unlock auto mode in the `Shift+Tab` cycle (requires Team plan and Sonnet 4.6 or Opus 4.6). [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/cli-reference.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added auto mode to the Desktop permission modes table (research preview, requires Team plan and Sonnet/Opus 4.6). [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/desktop.md?plain=1#L56)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]
* Added `disableAutoMode` and `autoMode` to the managed settings table; clarified that `autoMode` is not read from shared project settings. [[line 507](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/desktop.md?plain=1#L507)] [[Source](https://code.claude.com/docs/en/desktop#managed-settings)]
* Noted that @mention files is not available in remote Desktop sessions. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/desktop.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/desktop#add-files-and-context-to-prompts)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `auto` to the list of valid `permission_mode` field values in hook event JSON. [[line 489](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/hooks.md?plain=1#L489)] [[Source](https://code.claude.com/docs/en/hooks#common-input-fields)]

#### [How Claude Code works](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Added auto mode to the list of permission modes accessible via `Shift+Tab`. [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/how-claude-code-works.md?plain=1#L141)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#control-what-claude-can-do)]

#### [IDE integrations](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Updated `initialPermissionMode` to include `auto` as a valid value. [[line 230](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/ide-integrations.md?plain=1#L230)] [[Source](https://code.claude.com/docs/en/ide-integrations#extension-settings)]
* Clarified that `allowDangerouslySkipPermissions` now also adds Auto mode to the mode selector (not just bypass permissions), and that Auto requires a Team plan. [[line 240](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/ide-integrations.md?plain=1#L240)] [[Source](https://code.claude.com/docs/en/ide-integrations#extension-settings)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated `Shift+Tab` description to clarify it cycles through all enabled modes including `auto` and `bypassPermissions`. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/interactive-mode.md?plain=1#L28)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Added `Ctrl+M` to the list of hardcoded shortcuts (identical to Enter in terminals). [[line 377](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/keybindings.md?plain=1#L377)] [[Source](https://code.claude.com/docs/en/keybindings#reserved-shortcuts)]

#### [LLM gateway](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/llm-gateway.md) [[Source](https://code.claude.com/docs/en/llm-gateway)]

* Added security warning: LiteLLM PyPI versions 1.82.7 and 1.82.8 were compromised with credential-stealing malware. Instructs users to remove the package, rotate all credentials, and follow remediation steps. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/llm-gateway.md?plain=1#L37)] [[Source](https://code.claude.com/docs/en/llm-gateway#litellm-configuration)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added new MCP servers: Zapier, Postman, Pendo, DevRev, Cloudinary (reordered), Zoho Projects, Zoho Books, and Zoho CRM.
* Added `headersHelper` support for dynamic headers with custom authentication schemes (Kerberos, short-lived tokens, internal SSO). Command runs at each connection with a 10-second timeout and its output merges into connection headers. [[line 1509](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/mcp.md?plain=1#L1509)] [[Source](https://code.claude.com/docs/en/mcp#use-dynamic-headers-for-custom-authentication)]
* Fixed plugin MCP server config JSON example (missing `mcpServers` wrapper key). [[line 970](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/mcp.md?plain=1#L970)] [[Source](https://code.claude.com/docs/en/mcp#plugin-provided-mcp-servers)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Added `auto` mode to the permission modes table. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/permissions.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]
* Added `disableAutoMode` and updated `disableBypassPermissionsMode` to note they work in any settings scope, not just managed settings. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/permissions.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]
* Added comprehensive new "Configure the auto mode classifier" section covering the `autoMode.environment`, `autoMode.allow`, and `autoMode.soft_deny` settings, scope/precedence, templates, and CLI inspection commands (`auto-mode defaults`, `auto-mode config`, `auto-mode critique`). [[line 241](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/permissions.md?plain=1#L241)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]

#### [Server-managed settings](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Added `autoMode` configuration example showing how to define trusted repos, buckets, and internal domains for the auto mode classifier. [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/server-managed-settings.md?plain=1#L84)] [[Source](https://code.claude.com/docs/en/server-managed-settings#configure-server-managed-settings)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `autoMode` setting (with `environment`, `allow`, `soft_deny` arrays) to customize the auto mode classifier. [[line 151](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/settings.md?plain=1#L151)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `disableAutoMode` setting to prevent auto mode from being activated. [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/settings.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarified that when the parent session uses auto mode, subagents inherit it and any `permissionMode` in their frontmatter is ignored — the classifier evaluates subagent tool calls independently. [[line 392](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/sub-agents.md?plain=1#L392)] [[Source](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Same updates as IDE integrations: `initialPermissionMode` now includes `auto`; `allowDangerouslySkipPermissions` now also adds Auto mode to the selector.

-----

## API changes

### Changed documents

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/e98523a/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added new MCP connectors: tldraw (sketch, draw, and diagram), Calendly (event types and bookings), Intuit TurboTax (tax estimates), Zoho Projects, Zoho Books, Zoho CRM, Granted (grant opportunity discovery), Clarity AI (SFDR 2.0 fund classification), Common Room (GTM copilot), PagerDuty (incident management), DevRev (knowledge graph), Omni Analytics (natural language data queries), and Brex (finance automation).
