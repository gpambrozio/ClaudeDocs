# [Claude docs changes for April 28th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/4f94886b44af8729bd453da7db0279cfeabf9bde) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/4f94886b44af8729bd453da7db0279cfeabf9bde)]

## Executive Summary
- Windows: Git for Windows is no longer required — Claude Code now falls back to PowerShell as the shell tool when Git Bash is absent, simplifying Windows installation
- `claude ultrareview [target]` subcommand lets you run ultrareview non-interactively from CI or scripts, printing findings to stdout and exiting with a status code
- PostToolUse hooks can now replace tool output for **all** tools (not just MCP) via the new `updatedToolOutput` field; `updatedMCPToolOutput` is deprecated
- Two critical memory leak fixes in 2.1.121: multi-GB RSS growth when processing many images, and up to ~2GB leak in `/usage` on machines with large transcript histories
- MCP servers now get a new `alwaysLoad` config option to bypass tool-search deferral, ensuring specific tools are always available in context

## New Claude Code versions

### [2.1.120](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/versions/2.1.120.md)

#### New features

* Windows: Git for Windows (Git Bash) is no longer required — when absent, Claude Code uses PowerShell as the shell tool
* Added `claude ultrareview [target]` subcommand to run `/ultrareview` non-interactively from CI or scripts — prints findings to stdout (`--json` for raw output) and exits 0 on completion or 1 on failure
* Skills can now reference the current effort level with `${CLAUDE_EFFORT}` in their content
* Set `AI_AGENT` environment variable for subprocesses so `gh` can attribute traffic to Claude Code

#### Existing feature improvements

* Auto-compact in auto mode now displays `auto` (lowercase, no token count) instead of a misleading token value
* Faster session start when you have many claude.ai connectors configured but not authorized
* Spinner tips recommending the desktop app or creating skills/agents are hidden when you already have them

#### Major bug fixes

* Fixed pressing Esc during a stdio MCP tool call closing the entire server connection (regression in 2.1.105)
* Fixed `/rewind` and other interactive overlays not responding to keyboard input after launching with `claude --resume`
* Fixed terminal scrollback duplication in non-fullscreen mode (resize, dialog dismiss, long sessions)
* Fixed `DISABLE_TELEMETRY` / `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` not suppressing usage metrics telemetry for API and enterprise users
* Fixed false-positive "Dangerous rm operation" permission prompts in auto mode for multi-line bash commands containing both a pipe and a redirect
* Fixed `find` in the Bash tool exhausting open file descriptors on large directory trees, causing host-wide crashes (macOS/Linux native builds)

### [2.1.121](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/versions/2.1.121.md)

#### New features

* Added `alwaysLoad` option to MCP server config — when `true`, all tools from that server skip tool-search deferral and are always available in context
* Added `claude plugin prune` to remove orphaned auto-installed plugin dependencies; `plugin uninstall --prune` cascades
* Added a type-to-filter search box to `/skills` so you can find a skill in long lists without scrolling
* PostToolUse hooks can now replace tool output for all tools via `hookSpecificOutput.updatedToolOutput` (previously MCP-only)
* `CLAUDE_CODE_FORK_SUBAGENT=1` now works in non-interactive sessions and via the SDK

#### Existing feature improvements

* MCP servers that hit a transient error during startup now auto-retry up to 3 times instead of staying disconnected
* Vertex AI: support for X.509 certificate-based Workload Identity Federation (mTLS ADC)
* Fullscreen mode: typing into the prompt no longer jumps scroll back to the bottom after you've scrolled up
* Dialogs that overflow the terminal are now scrollable with arrow keys, PgUp/PgDn, and mouse wheel
* OpenTelemetry: added `stop_reason`, `gen_ai.response.finish_reasons`, and `user_system_prompt` (gated behind `OTEL_LOG_USER_PROMPTS`) to LLM request spans

#### Major bug fixes

* Fixed unbounded memory growth (multi-GB RSS) when processing many images in a session
* Fixed `/usage` leaking up to ~2GB of memory on machines with large transcript histories
* Fixed Bash tool becoming permanently unusable when the directory Claude was started in is deleted or moved mid-session
* Fixed `--resume` crashing on startup in external builds
* Fixed `--resume` failing on large sessions when a transcript line was corrupted by an unclean shutdown
* Fixed Microsoft 365 MCP OAuth failing with duplicate or unsupported `prompt` parameter
* Fixed `NO_PROXY` not being respected for all HTTP clients when set via `managed-settings.json` under the native build
* Fixed "Always allow" rules for built-in tools in remote sessions not surviving worker restarts

-----

## Claude Code changes

### New Documents

#### [whats-new/2026-w16](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/whats-new/2026-w16.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w16)]

Week 16 (April 13–17) release digest covering v2.1.105–v2.1.113: Claude Opus 4.7 becomes the default model on Max and Team Premium with a new `xhigh` effort level and interactive `/effort` slider; Routines let you run templated cloud agents on a schedule or GitHub event; `/usage` now shows a breakdown of what's driving your limits; `/ultrareview` launches parallel multi-agent code review in the cloud; and the CLI moves to native per-platform binaries.

#### [whats-new/2026-w17](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/whats-new/2026-w17.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w17)]

Week 17 (April 20–24) release digest covering v2.1.114–v2.1.119: `/ultrareview` enters public research preview; session recap shows a one-line summary when you return to a terminal; custom themes can be built and shipped from `/theme` or a plugin; and Claude Code on the web gets a redesign with a new sessions sidebar and drag-and-drop layout.

### Changed documents

#### [agent-sdk/tool-search](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/agent-sdk/tool-search.md) [[Source](https://code.claude.com/docs/en/agent-sdk/tool-search)]

Previously an error page (HTTP 500); now contains the full documentation for tool search in the Agent SDK. Covers how tool search works, the `ENABLE_TOOL_SEARCH` environment variable with all its values (`true`, `auto`, `auto:N`, `false`), how to optimize tool discovery via naming and system prompts, and limits (max 10,000 tools, 3–5 results per search, requires Claude Sonnet 4+ or Opus 4+). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/agent-sdk/tool-search.md?plain=1#L1)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* The `PostToolUse` hook output type now includes `updatedToolOutput` (works for all tools) alongside `updatedMCPToolOutput` (now deprecated). [[line 1364](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1364)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#synchookjsonoutput)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Added `bedrock:GetInferenceProfile` to the required IAM policy, allowing Claude Code to resolve application inference profile ARNs to their backing foundation models. Without this permission, Claude Code recovers automatically but with an extra round-trip per new model. [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/amazon-bedrock.md?plain=1#L222)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#iam-configuration)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* New note: cloud sessions (ultrareview, routines, Code Review) originate from Anthropic-managed infrastructure, not your network. If your organization has IP allowlisting enabled, every cloud session will fail with an authentication error; contact Anthropic support to exempt Anthropic-hosted services. [[line 740](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L740)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#limitations)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `claude ultrareview [target]` subcommand — runs ultrareview non-interactively, blocks until the review finishes, prints findings to stdout, and exits 0 on success or 1 on failure. Supports `--json` and `--timeout <minutes>` flags. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/cli-reference.md?plain=1#L24)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Expanded the session quality survey section: after the rating prompt, a new optional follow-up can ask to upload your session transcript to Anthropic. Selecting "Yes" uploads conversation transcripts and raw session logs (with API key patterns redacted), retained for up to 6 months. Selecting "No" or "Don't ask again" uploads nothing. Organizations with zero data retention or policy-disabled feedback never see this follow-up. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/data-usage.md?plain=1#L17)] [[Source](https://code.claude.com/docs/en/data-usage#session-quality-surveys)]

#### [devcontainer](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/devcontainer.md) [[Source](https://code.claude.com/docs/en/devcontainer)]

Comprehensive rewrite of the dev containers page. The new structure covers: adding Claude Code via the official Dev Container Feature, persisting authentication and settings across rebuilds with named volumes, enforcing organization policy via `managed-settings.json` in the Dockerfile or `containerEnv`, restricting network egress, running without permission prompts, and a guided walkthrough of the reference container. Also adds an architecture diagram and links to the full org setup guide. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/devcontainer.md?plain=1#L1)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_FORK_SUBAGENT` description updated: the variable now works in interactive mode **and** via the SDK or `claude -p` (previously documented as interactive-only). [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/env-vars.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/env-vars)]
* `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT` description updated: now documented as Opus 4.7-specific — it uses a shorter system prompt and abbreviated tool descriptions only on that model; has no effect on other models. [[line 127](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/env-vars.md?plain=1#L127)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Added tips for native text selection in fullscreen: hold `Option` (iTerm2) or `Shift` (most Linux/Windows terminals) as a bypass modifier so the terminal handles click-and-drag directly. Also noted that iTerm2 blocks OSC 52 clipboard access by default until you enable it in Settings → General → Selection. [[line 112](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/fullscreen.md?plain=1#L112)] [[Source](https://code.claude.com/docs/en/fullscreen#keep-native-text-selection)]

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Added support for X.509 certificate-based Workload Identity Federation (mTLS ADC) via the standard Application Default Credentials chain (requires v2.1.121+). Set `GOOGLE_APPLICATION_CREDENTIALS` to the credential configuration file path. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/google-vertex-ai.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#3-configure-gcp-credentials)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `updatedToolOutput` is now the preferred field for replacing tool output in PostToolUse hooks — it works for **all** tools, not just MCP tools. `updatedMCPToolOutput` is kept for backward compatibility. A new example shows replacing `Bash` tool output (stdout/stderr/interrupted/isImage shape). Added clarification that `updatedToolOutput` only changes what Claude sees; the tool has already run and the original output is captured in telemetry. [[line 1208](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/hooks.md?plain=1#L1208)] [[Source](https://code.claude.com/docs/en/hooks#posttooluse-decision-control)]

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Windows: Git for Windows is now described as **recommended** (not required) — if absent, Claude Code uses PowerShell as the shell tool instead. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/index.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/index#get-started)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* "Bash mode" renamed to "Shell mode" throughout the document to reflect that PowerShell is now a supported shell on Windows. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/interactive-mode.md?plain=1#L67)] [[Source](https://code.claude.com/docs/en/interactive-mode#quick-commands)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Auto-retry on startup: as of v2.1.121, HTTP/SSE MCP servers that fail their initial connection now retry up to 3 times on transient errors (5xx, connection refused, timeout) before being marked as failed. Authentication and not-found errors are not retried. [[line 1020](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/mcp.md?plain=1#L1020)] [[Source](https://code.claude.com/docs/en/mcp#automatic-reconnection)]
* New `alwaysLoad` server config option: set to `true` to exempt a server from tool-search deferral — all its tools load into context at session start regardless of `ENABLE_TOOL_SEARCH`. Also works at the individual tool level via `"anthropic/alwaysLoad": true` in the tool's `_meta` object. Requires v2.1.121+. [[line 1802](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/mcp.md?plain=1#L1802)] [[Source](https://code.claude.com/docs/en/mcp#configure-tool-search)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Three new attributes added to `claude_code.llm_request` OpenTelemetry spans: `stop_reason` (e.g. `end_turn`, `tool_use`, `max_tokens`), `gen_ai.response.finish_reasons` (same value as a string array, per GenAI semantic conventions), and `user_system_prompt` (gated behind `OTEL_LOG_USER_PROMPTS=1`, truncated at 60 KB, emitted once per session). [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/monitoring-usage.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Windows: Git for Windows is now described as **recommended** (not required) — if absent, Claude Code uses PowerShell as the shell tool instead. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/overview.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/overview#get-started)]

#### [plugin-dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/plugin-dependencies.md) [[Source](https://code.claude.com/docs/en/plugin-dependencies)]

* New section documenting `claude plugin prune`: lists and removes auto-installed plugin dependencies that no longer have any installed plugin requiring them. Supports `--scope`, `--dry-run`, and `-y` flags. Also documents `claude plugin uninstall --prune` for cascading cleanup. Requires v2.1.121+. [[line 97](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/plugin-dependencies.md?plain=1#L97)] [[Source](https://code.claude.com/docs/en/plugin-dependencies#how-constraints-interact)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Marketplace manifest now supports top-level `$schema`, `description`, and `version` fields (previously only under `metadata`); the old `metadata.description` and `metadata.version` paths remain for backward compatibility. `claude plugin validate` now accepts these top-level fields without warnings. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/plugin-marketplaces.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#optional-fields)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `$schema` field added to the plugin manifest (`plugin.json`) schema — allows editor autocomplete and validation; ignored by Claude Code at load time. [[line 373](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/plugins-reference.md?plain=1#L373)] [[Source](https://code.claude.com/docs/en/plugins-reference#metadata-fields)]
* New `plugin prune` command documented with full options table (`--scope`, `--dry-run`, `-y`). Also added `--prune` and `-y` flags to `plugin uninstall`. [[line 705](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/plugins-reference.md?plain=1#L705)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-uninstall)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Windows: Git for Windows is now described as **recommended** (not required) — if absent, Claude Code uses PowerShell as the shell tool instead. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/quickstart.md?plain=1#L53)] [[Source](https://code.claude.com/docs/en/quickstart#step-1-install-claude-code)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Bypass condition expanded: server-managed settings are now documented as bypassed by **any** third-party provider configuration, not just a non-default `ANTHROPIC_BASE_URL`. This explicitly includes `CLAUDE_CODE_USE_BEDROCK`, `CLAUDE_CODE_USE_MANTLE`, `CLAUDE_CODE_USE_VERTEX`, and `CLAUDE_CODE_USE_FOUNDRY`. [[line 191](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/server-managed-settings.md?plain=1#L191)] [[Source](https://code.claude.com/docs/en/server-managed-settings#security-considerations)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Shell requirements updated: Git for Windows is now **recommended** on native Windows with PowerShell as a fallback; the Windows setup table and instructions reflect that Claude Code no longer requires Git Bash to start. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/setup.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/setup#system-requirements)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New `${CLAUDE_EFFORT}` substitution placeholder: expands to the current effort level (`low`, `medium`, `high`, `xhigh`, or `max`), allowing skill instructions to adapt to the active effort setting. [[line 200](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/skills.md?plain=1#L200)] [[Source](https://code.claude.com/docs/en/skills#available-string-substitutions)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* New optional `hideVimModeIndicator` field: set to `true` to suppress the built-in `-- INSERT --` text when your status line script already renders the vim mode itself. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/statusline.md?plain=1#L56)] [[Source](https://code.claude.com/docs/en/statusline#manually-configure-a-status-line)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Forked subagents are no longer limited to interactive sessions: `CLAUDE_CODE_FORK_SUBAGENT=1` now enables fork mode in non-interactive mode and via the Agent SDK as well. [[lines 718–763](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/sub-agents.md?plain=1#L718-L763)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Added note for iTerm2: running `/terminal-setup` now also enables "Applications in terminal may access clipboard" (Settings → General → Selection), which is required for `/copy` to write to the system clipboard, including from inside tmux. Restart iTerm2 for the change to take effect. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/terminal-config.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/terminal-config#enable-option-key-shortcuts-on-macos)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Removed the PowerShell tool limitation stating "Git Bash is still required to start Claude Code on Windows" — PowerShell now works as a standalone shell. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/tools-reference.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/tools-reference#preview-limitations)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Updated Windows shell error: the error message changed from `"Claude Code on Windows requires git-bash"` to `"Claude Code on Windows requires either Git for Windows (for bash) or PowerShell"`. The troubleshooting section now explains both options (Git for Windows or PowerShell 7). [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/troubleshooting.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/troubleshooting#troubleshoot-installation-issues)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* New section documenting the `claude ultrareview` non-interactive subcommand: reviews current branch vs. default branch, a PR by number, or a diff against a named branch. Blocks until done, prints findings to stdout, exits 0 on success or 1 on failure/timeout/error. Progress and session URL go to stderr. Supports `--json` and `--timeout <minutes>` flags. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/ultrareview.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/ultrareview#track-a-running-review)]

#### [voice-dictation](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* In the VS Code extension, if the Claude Code `language` setting is empty, voice dictation now falls back to VS Code's `accessibility.voice.speechLanguage` setting before defaulting to English. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/claude-code/voice-dictation.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/voice-dictation#tap-to-record-and-send)]

-----

## API changes

### Changed documents

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Clarified that the `clear_thinking` default `keep: {type: "thinking_turns", value: 1}` applies to earlier Opus/Sonnet models and all Haiku models; Opus 4.5+ and Sonnet 4.6+ default to keeping all turns. Recommends setting `keep: "all"` explicitly to preserve advisor cache stability across model tiers. [[line 320](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L320)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [api/sdks/go](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/api/sdks/go.md) [[Source](https://platform.claude.com/docs/en/api/sdks/go)]

* Installation instructions updated: the install command changed from `go get -u 'github.com/anthropics/anthropic-sdk-go@v1.38.0'` to `go get github.com/anthropics/anthropic-sdk-go` (no pinned version, no `-u` flag). [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/api/sdks/go.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/api/sdks/go)]

#### [build-with-claude/adaptive-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Removed the workaround note for the `display` field — it is now natively supported across SDKs (no more need for type assertions or raw HTTP requests).
* Thinking block preservation cost clarified: on Opus 4.5+ and Sonnet 4.6+, all prior turns are kept (not just the last one), so input token costs reflect more blocks being billed. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L178)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [build-with-claude/context-editing](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* `clear_thinking_20251015` default behavior is now model-specific: Opus 4.5+ and Sonnet 4.6+ keep **all** prior thinking blocks by default; earlier Opus/Sonnet and all Haiku models keep only the last turn. The `keep` configuration table now says "Model-specific" instead of `{type: "thinking_turns", value: 1}`. Recommends setting `keep` explicitly when code runs across multiple model tiers. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/context-editing.md?plain=1#L35)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

#### [build-with-claude/extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Claude Opus 4.7 added to the model comparison table with adaptive thinking, summarized thinking output, automatic interleaved thinking, and thinking block preservation by default. [[line 588](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L588)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* "Thinking block preservation in Claude Opus 4.5 and later" section renamed to "Thinking block preservation by model" and updated to document per-class defaults: Opus 4.5+ keeps all, Sonnet 4.6+ keeps all, earlier Opus/Sonnet and all Haiku keep only the last turn. [[line 591](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L591)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Removed SDK workaround note for the `display: "omitted"` field — now natively supported across SDKs. [[line 112](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L112)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Context window usage clarification: on Opus 4.5+ and Sonnet 4.6+, thinking blocks from prior turns are kept and **count** toward context window usage; on earlier models they are stripped and do not count. [[line 506](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L506)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [build-with-claude/prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Cache invalidation table updated: the "Non-tool results passed to extended thinking requests" row is now marked "Model-specific" — on Opus 4.5+ and Sonnet 4.6+, thinking blocks are preserved so the cache remains valid; on earlier models/Haiku, they are stripped and the cache is invalidated. [[line 303](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L303)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Cache invalidation patterns section updated with the same model-specific clarification. [[line 349](https://github.com/gpambrozio/ClaudeDocs/blob/4f94886b44af8729bd453da7db0279cfeabf9bde/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L349)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
