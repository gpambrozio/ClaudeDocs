# [Claude docs changes for May 7th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e22d481) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e22d481)]

## Executive Summary
- **Dreams (Research Preview):** New Managed Agents API feature for memory consolidation — asynchronously reads memory stores and past session transcripts to produce a deduplicated, reorganized memory store.
- **Webhooks for Managed Agents:** New guide and CLI API reference for subscribing to session and vault lifecycle events via webhooks.
- **Hooks now run in parallel (Agent SDK):** SDK hooks fire concurrently rather than sequentially; for permission decisions, the most restrictive result wins.
- **`plan` mode redefined:** Now allows read-only tools to run (file reads, grep, etc.) rather than blocking all tool execution.
- **Multi-agent API graduated:** `callable_agents` renamed to `multiagent` with new coordinator/thread event model; no longer a Research Preview.

## New Claude Code versions

### [2.1.132](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/versions/2.1.132.md)

#### New features

* Added `CLAUDE_CODE_SESSION_ID` environment variable automatically set in Bash and PowerShell tool subprocesses, matching the `session_id` passed to hooks
* Added `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1` env var to opt out of the fullscreen alternate-screen renderer and keep the conversation in the terminal's native scrollback

#### Existing feature improvements

* Updated the `/tui fullscreen` startup banner to describe additional renderer benefits (lower memory usage, mouse support, auto-copy on select)
* Improved visual consistency in slash command dialogs and `/login`, `/upgrade`, `/extra-usage` spacing

#### Major bug fixes

* Fixed external SIGINT (e.g. IDE stop button, `kill -INT`) not running graceful shutdown — terminal modes are now restored and the `--resume` hint is printed
* Fixed `--permission-mode` flag being ignored when resuming a plan-mode session with `-p --continue`/`--resume`, and plan mode not being re-applied after `ExitPlanMode`
* Fixed fullscreen mode showing a blank screen after laptop sleep/wake or Ctrl+Z/`fg` until the next keystroke
* Fixed unbounded memory growth (10GB+ RSS) when a stdio MCP server writes non-protocol data to stdout
* Fixed MCP servers that connect but fail `tools/list` silently showing 0 tools — they now retry once and show "connected · tools fetch failed"
* Fixed unauthorized claude.ai MCP connectors showing as "failed" instead of "needs auth"
* Fixed statusline `context_window` token counts reflecting cumulative session totals instead of current context usage
* Fixed Alt+T (thinking toggle) not working on macOS terminals without "Option as Meta" enabled (iTerm2, Terminal.app defaults)
* Fixed scroll-wheel handling in JetBrains IDE 2025.2 terminals (spurious arrow keys, wrong-direction events, runaway acceleration)
* Fixed `--resume` failing with `no low surrogate in string` when a tool error truncation split an emoji
* Fixed pasting text starting with `/` silently swallowing the input or triggering an unknown-command reply
* Fixed Bedrock and Vertex 400 errors when `ENABLE_PROMPT_CACHING_1H` is set

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* Clarified that `readOnlyHint` (not `readOnly`) is the correct annotation field name for enabling parallel execution on custom tools in both TypeScript and Python SDKs [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L121)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#parallel-tool-execution)]
* `effort` can now be set per-subagent via the `effort` field on `AgentDefinition`, overriding the session-level setting [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#effort-level)]
* `plan` mode redefined: read-only tools now run in plan mode; Claude can explore files without editing source files [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#permission-mode)]

#### [agent-sdk/custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* New "Return structured data" section documenting the `structuredContent` field — an optional JSON object on the tool result that allows returning machine-readable data alongside image/resource content [[line 363](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L363)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#resources)]
* Note that Python SDK `@tool` decorator does not forward `structuredContent`; use a standalone MCP server instead

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Hooks now run in **parallel**, not sequentially. For permission decisions, the most restrictive result wins: a single `deny` blocks the call regardless of other hooks [[line 294](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L294)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#auto-approve-specific-tools)]
* Section renamed from "Chain multiple hooks" to "Register multiple hooks" reflecting the parallel execution model

#### [agent-sdk/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/migration-guide.md) [[Source](https://code.claude.com/docs/en/agent-sdk/migration-guide)]

* Settings sources default clarified: the v0.1.0 change to not load filesystem settings was reverted — no migration action needed. Current default loads user, project, and local filesystem settings [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/migration-guide.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/agent-sdk/migration-guide#system-prompt-no-longer-default)]

#### [agent-sdk/observability](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/observability.md) [[Source](https://code.claude.com/docs/en/agent-sdk/observability)]

* New "Attribute actions to your end users" section: inject `enduser.id` and `tenant.id` as `OTEL_RESOURCE_ATTRIBUTES` on each `query()` call to create a per-user audit trail of tool calls and MCP activity [[line 138](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/observability.md?plain=1#L138)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#tag-telemetry-from-your-agent)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* `plan` mode redefined: read-only tools run; Claude can read files and explore the codebase but does not edit source files [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L86)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#available-modes)]
* Clarified that a hook returning `allow` does not bypass deny and ask rules — those are evaluated regardless [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)]
* Python code example updated to use `ClaudeSDKClient` context manager pattern

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* New `ClaudeAgentOptions` fields: `strict_mcp_config` (ignore project/user MCP config), `include_hook_events` (expose hook lifecycle in message stream), `session_store_flush` (`batched` or `eager`)
* New effort level `xhigh` added to `effort` type literals
* New `ToolPermissionContext` fields: `blocked_path`, `decision_reason`, `title`, `display_name`, `description`
* New `permissionDecision` value `"defer"` added to `PreToolUseHookSpecificOutput`
* New `updatedToolOutput` field on `PostToolUseHookSpecificOutput`
* New `deferred_tool_use` field on `ResultMessage`
* New "Handle slow or stalled API responses" section documenting `API_TIMEOUT_MS`, `CLAUDE_CODE_MAX_RETRIES`, `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS`, and `CLAUDE_ENABLE_STREAM_WATCHDOG` env vars

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `settings` option for inline settings object or path to a settings file (flag-settings layer)
* New `applyFlagSettings()` method on the Query object for changing settings on a running session without restarting (TypeScript-only)
* `structuredContent` field added to `CallToolResult` type
* New "Handle slow or stalled API responses" section (same env vars as Python)

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Inference profile ID prefix changed from `global.` to `us.` in the example `ANTHROPIC_MODEL` value

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Credential storage location expanded into per-platform bullet points; Windows path now explicitly documented as `%USERPROFILE%\.claude\.credentials.json`

#### [channels](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/channels.md) [[Source](https://code.claude.com/docs/en/channels)]

* Channels now support Console API key authentication (previously claude.ai login only); not available on Bedrock, Vertex, or Foundry
* Enterprise controls section expanded: default behavior now differs by auth method — claude.ai Team/Enterprise blocks channels by default; Console API key authentication permits them by default

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--plugin-url` flag: fetch a plugin `.zip` archive from a URL for the session [[line ~103](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/cli-reference.md?plain=1#L103)]
* `--add-dir` clarified: to persist directories across sessions, set `permissions.additionalDirectories` in settings
* `--effort` clarified: overrides the `effortLevel` setting for the session
* `--settings` clarified: values override the same keys in `settings.json` files for the session

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/skills` command: press `Space` to hide a skill from Claude or the `/` menu, then `Enter` to save
* `/team-onboarding`: for claude.ai Pro, Max, Team, and Enterprise subscribers, now also returns a share link teammates can open directly in Claude Code
* `/color`: can now run with no argument to pick a random color

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New split-pane view: hold Cmd (macOS) or Ctrl (Windows) and click a session in the sidebar to open it alongside the current session. Press Cmd+\ or Ctrl+\ to close the focused pane

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS`: stall timeout for background subagents (default 10 minutes)
* New `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN`: set to `1` to force classic main-screen renderer
* New `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY`: set to `1` to populate `/model` picker from gateway's `/v1/models` endpoint (opt-in)
* New `CLAUDE_CODE_FORCE_SYNC_OUTPUT`: set to `1` to force-enable DEC private mode 2026 synchronized output
* New `CLAUDE_CODE_PACKAGE_MANAGER_AUTO_UPDATE`: set to `1` to enable background auto-updates for Homebrew and WinGet
* New `CLAUDE_CODE_SESSION_ID`: automatically set in Bash/PowerShell subprocesses to the current session ID
* `CLAUDE_CODE_ENABLE_FINE_GRAINED_TOOL_STREAMING` behavior updated: now enabled by default for direct Anthropic API; set to `0` to opt out

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Added note that `skillOverrides` in settings can hide a skill from Claude without editing the skill's file

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* New "Scroll in the JetBrains IDE terminal" subsection documenting Claude Code's override of JetBrains scroll handling and scroll bugs in 2025.2
* New tmux caveat: synchronized output is not supported in tmux, which may cause flicker — recommend running outside tmux especially over SSH
* Turn-off instructions updated to include `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN=1`

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New `--plugin-url <url>` flag documented for loading plugins from URL archives
* Piped stdin now capped at 10MB as of v2.1.128; exceeding the cap exits with an error

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `PostToolUse` hook: `decision: "block"` adds the reason next to the tool result; Claude still sees original output. Use `updatedToolOutput` to replace it [[line 1293](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/hooks.md?plain=1#L1293)] [[Source](https://code.claude.com/docs/en/hooks#posttooluse-decision-control)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Alt+T` / `Option+T` thinking toggle now works on macOS without configuring "Option as Meta" (as of v2.1.132)
* `Shift+Enter` for newline now natively supported in Windows Terminal
* Ctrl+R history search now defaults to all projects scope; press `Ctrl+S` to cycle through session → project → all projects

#### [llm-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/llm-gateway.md) [[Source](https://code.claude.com/docs/en/llm-gateway)]

* Gateway model discovery is now opt-in: set `CLAUDE_CODE_ENABLE_GATEWAY_MODEL_DISCOVERY=1` to populate the `/model` picker from the gateway's `/v1/models` endpoint (was previously automatic)
* Minimum version requirement bumped from v2.1.126 to v2.1.129

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* `/mcp` panel now shows tool count per server and flags servers that advertise the tools capability but expose zero tools
* Server name `workspace` is reserved; Claude Code skips and warns if a config uses it
* `alwaysLoad: true` blocks startup until the server connects (capped at 5s) even when `MCP_CONNECTION_NONBLOCKING=1` is set

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New mTLS authentication section documenting cert configuration by OTLP protocol: `http/protobuf`/`http/json` use `CLAUDE_CODE_CLIENT_CERT` vars; `grpc` uses `OTEL_EXPORTER_OTLP_CLIENT_KEY` vars
* New "Audit security events" section: identity attributes, MCP activity auditing, security question-to-event mapping table, and SIEM forwarding example
* Note added: `OTEL_*` env vars are not passed to subprocesses (Bash tool, hooks, MCP servers)

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `plan` mode description updated: Claude reads files and runs read-only shell commands to explore but does not edit source files
* `disableRemoteControl` managed setting added: disables Remote Control per device

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Plugin skills are now namespaced with the plugin name (e.g., `/plugin-name:skill-name`)
* New `pathPattern` marketplace source type for filesystem-based path restrictions
* Note added: exact URL matching for allowlists is not normalized; use `hostPattern` for organizations with multiple URL forms

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* New `--plugin-url` flag documented: loads a plugin from a `.zip` archive URL for the session duration (useful for CI build artifacts)

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `rust-lsp` renamed to `rust-analyzer-lsp` in the built-in LSP table
* `themes` and `monitors` keys moved under `experimental` in `plugin.json`; top-level still works but warns — will require `experimental.*` in a future release
* Note added: a `CLAUDE.md` at the plugin root is not loaded as project context; use skills instead
* `--plugin-url` added alongside `--plugin-dir` references

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Claude mobile app navigation updated: tap "Code" in the navigation to reach the session list
* New `disableRemoteControl` managed setting cause added to the error message troubleshooting section

#### [scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Jitter range updated: recurring tasks now fire up to **30 minutes** after scheduled time (was up to 15 minutes, or 10% of interval)

#### [security](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Accept Edits mode now explicitly lists auto-approved commands: `mkdir`, `touch`, `rm`, `mv`, `cp`, `sed`; other Bash commands and out-of-scope paths still prompt

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `autoMemoryEnabled` setting: disable auto memory entirely or force it on even when `--bare` mode would disable it
* New `disableRemoteControl` setting: blocks Remote Control at the device level (requires v2.1.128+)
* New `skillOverrides` setting: per-skill visibility control with states `on`, `name-only`, `user-invocable-only`, `off` (requires v2.1.129+)
* New `pathPattern` marketplace source type for `extraKnownMarketplaces`
* Note added: on Windows, `~/.claude` resolves to `%USERPROFILE%\.claude`
* Plugin precedence note: project settings take precedence over user settings; to opt out of a project-enabled plugin, set it to `false` in `.claude/settings.local.json`

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New "Override skill visibility from settings" section documenting the `skillOverrides` setting with four visibility states
* Note added: skill body content incurs recurring token cost across turns; keep SKILL.md files concise

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* `context_window.total_input_tokens` and `total_output_tokens` now reflect **current context window usage** (not cumulative session totals) as of v2.1.132; includes cache reads/writes for input
* Script now also triggers after `/compact` finishes
* `current_usage` is `null` immediately after `/compact` until the next API call

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Windows Terminal moved to "Works without setup" row — Shift+Enter for newline is now natively supported

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New `ShareOnboardingGuide` tool: uploads `ONBOARDING.md` and returns a share link; available to claude.ai Pro, Max, Team, and Enterprise subscribers; called from `/team-onboarding`

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* New error documented: "Voice input is failing repeatedly and has been paused" — explains auto-pause behavior after repeated failures and how to re-enable

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* New troubleshooting section: "New sessions hang or time out during setup" — explains the ~5-minute environment cache budget and recommends parallel installs and moving large downloads to a SessionStart hook

-----

## API changes

### New Documents

#### [api/api/cli/beta/webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/api/cli/beta/webhooks.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta/webhooks)]

CLI API reference for beta webhooks. Documents the `unwrap` helper for verifying webhook signatures and lists all 22 possible `data.type` values for session and vault events.

#### [managed-agents/dreams](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/managed-agents/dreams.md) [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]

New Research Preview feature for memory consolidation. A dream reads an existing memory store and up to 100 past session transcripts, then produces a new reorganized memory store with duplicates merged and stale entries replaced. The input store is never modified. Documents the full dream lifecycle (pending → running → completed/failed/canceled), polling, output usage, cancellation, archiving, and billing. Requires both `managed-agents-2026-04-01` and `dreaming-2026-04-21` beta headers.

#### [managed-agents/webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/managed-agents/webhooks.md) [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]

New guide for subscribing to Managed Agents session and vault lifecycle events via webhooks. Covers supported event types (session status changes, thread events, outcome evaluation, vault credential events), endpoint registration in Console, signature verification using `unwrap()`, event payload structure, and delivery behavior (no ordering guarantee, auto-disable after ~20 consecutive failures).

### Changed documents

#### [api/api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* BetaWebhooks section now includes a descriptive intro and full list of 22 `data.type` values (replaces the previous empty stub)
* `session.status_scheduled` event type renamed to `session.status_rescheduled` throughout (affects all SDK language variants)
* BetaUser Profiles section reordered to appear before BetaWebhooks

#### [api/api/cli/beta](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/api/cli/beta.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta)]

* Same BetaWebhooks and `session.status_rescheduled` rename changes as `api/api/beta.md`

#### [api/api/go/beta](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/api/go/beta.md) [[Source](https://platform.claude.com/docs/en/api/go/beta)]

* Same BetaWebhooks and `session.status_rescheduled` rename changes as `api/api/beta.md`

#### [api/api/java/beta](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/api/java/beta.md) [[Source](https://platform.claude.com/docs/en/api/java/beta)]

* Same BetaWebhooks and `session.status_rescheduled` rename changes as `api/api/beta.md`

#### [api/api/python/beta](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/api/python/beta.md) [[Source](https://platform.claude.com/docs/en/api/python/beta)]

* Same BetaWebhooks and `session.status_rescheduled` rename changes as `api/api/beta.md`

#### [api/api/ruby/beta](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/api/ruby/beta.md) [[Source](https://platform.claude.com/docs/en/api/ruby/beta)]

* Same BetaWebhooks and `session.status_rescheduled` rename changes as `api/api/beta.md`

#### [api/api/typescript/beta](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/api/typescript/beta.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta)]

* Same BetaWebhooks and `session.status_rescheduled` rename changes as `api/api/beta.md`

#### [managed-agents/agent-setup](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* `callable_agents` field renamed to `multiagent` in the agent configuration; now described as "a coordinator declaration listing the agents this agent can delegate to"
* Update behavior docs updated: `multiagent` is replaced as a whole (pass `null` to clear it)

#### [managed-agents/define-outcomes](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/managed-agents/define-outcomes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/define-outcomes)]

* Research Preview notice and additional beta header requirement removed — feature is now generally available under the standard `managed-agents-2026-04-01` header
* Code tab coverage expanded to all SDK languages (curl, CLI, Python, TypeScript, C#, Go, Java, PHP, Ruby)

#### [managed-agents/events-and-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* `stop_reason.requires_action.event_ids` path simplified to `stop_reason.event_ids` (2 occurrences)
* CLI tab added to several code examples

#### [managed-agents/multi-agent](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/managed-agents/multi-agent.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multi-agent)]

* Research Preview notice removed — multi-agent is now generally available
* `callable_agents` renamed to `multiagent` with `type: coordinator` and an `agents` array throughout
* `multiagent.agents` now supports `{"type": "self"}` and omitting `version` (defaults to latest)
* Limits clarified: max 20 unique agents in `multiagent.agents`, max 25 concurrent threads
* New thread event types documented: `session.thread_status_running`, `session.thread_status_idle`, `session.thread_status_terminated`, `agent.thread_message_received`, `agent.thread_message_sent`
* `client.beta.sessions.threads.stream(...)` updated to `client.beta.sessions.threads.events.stream(...)`

#### [managed-agents/vaults](https://github.com/gpambrozio/ClaudeDocs/blob/e22d481/docs-md/api/managed-agents/vaults.md) [[Source](https://platform.claude.com/docs/en/managed-agents/vaults)]

* New "Credential refresh" section documenting periodic re-resolution behavior and webhook events for vault/credential lifecycle (`vault.archived`, `vault.deleted`, `vault_credential.*`)
* New "Diagnose an OAuth refresh failure" subsection with the `/mcp_oauth_validate` endpoint, status values (`valid`, `invalid`, `unknown`), and full JSON response example
