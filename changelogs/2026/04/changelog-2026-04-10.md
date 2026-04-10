# [Claude docs changes for April 10th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/0c6c99c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/0c6c99c)]

## Executive Summary

- **New Advisor Tool (Beta):** A new API-level server tool lets a faster executor model consult a more powerful advisor model (e.g., Opus) mid-generation for strategic guidance, enabling near-advisor-quality output at lower token cost for agentic workloads.
- **Monitor Tool added to Agent SDK:** A new `Monitor` built-in tool lets Claude run a background script and react to each stdout line as an event, replacing polling loops in background task management.
- **Claude Code 2.1.98:** Major release with a Google Vertex AI interactive setup wizard, `claude setup-token` for CI authentication, subprocess sandboxing on Linux, Perforce write-protection mode, and dozens of permission/Bash bug fixes.
- **New Agent SDK Hooks Guide:** A comprehensive new guide explains how to intercept and control agent behavior with hooks in both Python and TypeScript SDKs.
- **New Remote MCP Servers:** Six new remote MCP servers added (Sybill, Tines, MoSPI, incident.io, Unthread, Zoom); Microsoft 365 connector removed.

---

## New Claude Code versions

### [2.1.98](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/versions/2.1.98.md)

#### New features

* Added interactive Google Vertex AI setup wizard, accessible from the login screen when selecting "3rd-party platform", guiding through GCP authentication, project/region configuration, credential verification, and model pinning
* Added `CLAUDE_CODE_PERFORCE_MODE` environment variable: when set, Edit/Write/NotebookEdit fail on read-only files with a `p4 edit` hint instead of silently overwriting them
* Added `Monitor` tool for streaming events from background scripts (each stdout line delivered to Claude as an event)
* Added subprocess sandboxing with PID namespace isolation on Linux when `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` is set; added `CLAUDE_CODE_SCRIPT_CAPS` env var to limit per-session script invocations
* Added `--exclude-dynamic-system-prompt-sections` flag to print mode for improved cross-user prompt caching by moving per-machine sections into the first user message
* Added `workspace.git_worktree` to the status line JSON input, set whenever the current directory is inside a linked git worktree
* Added `claude setup-token` command to generate long-lived OAuth tokens for CI pipelines and automated environments
* Added W3C `TRACEPARENT` env var to Bash tool subprocesses when OTEL tracing is enabled, so child-process spans correctly parent to Claude Code's trace tree
* LSP: Claude Code now identifies itself to language servers via `clientInfo` in the initialize request

#### Existing feature improvements

* Improved `/resume` filter hint labels and added project/worktree/branch names in the filter indicator
* Improved `/agents` with a tabbed layout: a Running tab shows live subagents, and the Library tab adds Run agent and View running instance actions
* Improved `/reload-plugins` to pick up plugin-provided skills without requiring a restart
* Improved Accept Edits mode to auto-approve filesystem commands prefixed with safe environment variables (e.g., `LANG=C`) or process wrappers (e.g., `timeout`, `nice`)
* Improved Vim mode: `j`/`k` in NORMAL mode now navigate history and select the footer pill at the input boundary
* Improved hook errors in the transcript to include the first line of stderr for self-diagnosis without `--debug`
* Improved OTEL tracing: interaction spans now correctly wrap full turns under concurrent SDK calls

#### Major bug fixes

* Fixed a Bash tool permission bypass where a backslash-escaped flag could be auto-allowed as read-only and lead to arbitrary code execution
* Fixed compound Bash commands bypassing forced permission prompts for safety checks and explicit ask rules in auto and bypass-permissions modes
* Fixed 429 retries burning all attempts in ~13s when the server returns a small `Retry-After` — exponential backoff now applies as a minimum
* Fixed MCP OAuth `oauth.authServerMetadataUrl` config override not being honored on token refresh after restart
* Fixed capital letters being dropped to lowercase on xterm and VS Code integrated terminal when the kitty keyboard protocol is active
* Fixed `--dangerously-skip-permissions` being silently downgraded to accept-edits mode after approving a write to a protected path via Bash
* Fixed managed-settings allow rules remaining active after an admin removed them, until process restart
* Fixed `permissions.additionalDirectories` changes not applying mid-session
* Fixed stale subagent worktree cleanup removing worktrees that contain untracked files
* Fixed `Bash(cmd:*)` and `Bash(git commit *)` wildcard permission rules failing to match commands with extra spaces or tabs
* Fixed false Bash permission prompts for `cut -d /`, `paste -d /`, `column -s /`, `awk '{print $1}' file`, and filenames containing `%`
* Fixed agent team members not inheriting the leader's permission mode when using `--dangerously-skip-permissions`
* Fixed several `/resume` picker issues including empty list swallowing arrow keys and transient task-status text replacing conversation summaries
* Fixed `/export` not honoring absolute paths and `~`, and silently rewriting user-supplied extensions to `.txt`
* Fixed macOS text replacements deleting the trigger word instead of inserting the substitution

-----

## Claude Code changes

### New Documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

New comprehensive guide for intercepting and controlling agent behavior with hooks in the Agent SDK. Covers all available hook events (PreToolUse, PostToolUse, Stop, SubagentStart/Stop, Notification, etc.), how to configure callback functions, matchers, async outputs, and practical examples including blocking dangerous operations, modifying tool inputs, auto-approving tools, chaining hooks, making HTTP requests, and forwarding notifications to Slack.

### Changed documents

#### [agent-sdk/overview](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* Added `Monitor` tool to the built-in tools table — watches a background script and reacts to each output line as an event. [[line ~118](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/agent-sdk/overview.md?plain=1#L118)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added full `Monitor` tool documentation including input schema (`command`, `description`, `timeout_ms`, `persistent`) and output schema (`taskId`, `timeoutMs`, `persistent`).
* Updated `TaskStartedMessage` and `TaskNotificationMessage` to mention Monitor watches as a background task type.

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `Monitor` tool with `MonitorInput` and `MonitorOutput` types to the TypeScript SDK reference.
* Updated `SDKTaskStartedMessage` and `SDKTaskNotificationMessage` to note that Monitor watches use `task_type: "local_bash"`.

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Improved "Sign in with Bedrock" section with a new step-by-step wizard flow (wizard detects credentials, region, available models, and writes settings automatically).
* Restructured setup into "Sign in with Bedrock" (for individuals) vs "Set up manually" (for CI/enterprise rollouts).
* Added new "Startup model checks" section: Claude Code verifies model accessibility at startup and can fall back to the previous version when the latest is unavailable in Bedrock.

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Added `CLAUDE_CODE_OAUTH_TOKEN` as a new credential priority tier (between `apiKeyHelper` and subscription OAuth).
* Added new "Generate a long-lived token" section documenting `claude setup-token` for CI environments — generates a one-year OAuth token without saving it.

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `claude setup-token` command for generating long-lived OAuth tokens.
* Added `--exclude-dynamic-system-prompt-sections` flag that moves per-machine sections to the first user message for better prompt-cache reuse in multi-user workloads.

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Renamed from "Built-in commands" to "Commands" and updated description to distinguish built-in commands from bundled skills.
* Added `/batch` skill for orchestrating large-scale parallel codebase changes.
* Added `/claude-api` skill for loading Claude API reference material.
* Added `/debug` skill for enabling debug logging and troubleshooting mid-session.
* Added `/loop` skill for running prompts on a recurring interval.
* Added `/setup-vertex` command for configuring Google Vertex AI interactively.
* Added `/simplify` skill for reviewing changed code for quality and efficiency.

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Subagent worktree cleanup now requires no uncommitted changes, no untracked files, and no unpushed commits (previously only checked modifications to tracked files).

#### [context-window](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

* Added new "What survives compaction" section with a detailed table showing what happens to each context mechanism (system prompt, CLAUDE.md, skills, hooks, path-scoped rules) after `/compact`.

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Added note that for organizations with custom rate limits, Claude Code traffic counts toward API rate limits, and a workspace rate limit can be set in the Claude Console to cap Claude Code's share.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_PERFORCE_MODE` for Perforce-aware write protection on read-only files.
* Added `CLAUDE_CODE_SCRIPT_CAPS` for limiting per-session script invocations by command substring.
* Updated `CLAUDE_CODE_SUBPROCESS_ENV_SCRUB` to document new Linux PID namespace isolation behavior.
* Updated `CLAUDE_CODE_OAUTH_TOKEN` to reference `claude setup-token` for generation.

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Added new "Build your setup over time" section with a trigger table guiding when to add CLAUDE.md, skills, MCP servers, subagents, hooks, or plugins.

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Added note that scroll actions are rebindable and a reference to the Scroll actions section in keybindings.

#### [google-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Added new "Sign in with Vertex AI" section with a step-by-step wizard flow requiring v2.1.98 or later.
* Restructured into "Sign in" (individuals) vs "Set up manually" (CI/enterprise).
* Added new "Startup model checks" section: Claude Code verifies model accessibility at startup with fallback and pin-update prompting.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Updated hook lifecycle description to clarify event cadences: once per session, once per turn, and per tool call.
* Improved matcher pattern documentation with a table distinguishing exact-string matchers (`Edit|Write`) from regex matchers (containing special characters).
* Hook error display now shows the first line of stderr in the transcript (not just the hook name), aiding self-diagnosis without `--debug`.
* Clarified `FileChanged` matcher behavior: watch list is built from literal filenames split on `|`, not regex patterns.
* MCP tool matcher guidance updated: `mcp__memory` (letters/underscores only) matches as exact string, so `.*` suffix is required for prefix matching.

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Updated exit code documentation: non-blocking errors now display hook name plus first line of stderr in transcript.
* Updated `FileChanged` matcher description to clarify literal filename watch list vs regex filtering.

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Added documentation for two Homebrew casks: `claude-code` (stable channel, ~1 week behind) and `claude-code@latest` (latest channel, immediate updates).

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Updated Vim mode documentation: `j`/`k` now navigate history in NORMAL mode, in addition to arrow keys.

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Added new `Scroll` keybinding context for fullscreen mode with 12 scroll and selection actions (line up/down, page up/down, half/full page, top, bottom, copy selection, clear selection).

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Sybill MCP server (sales calls and pipeline AI).
* Removed Microsoft 365 MCP connector.
* Updated Slack MCP connection command to include `--client-id` and `--callback-port` parameters.

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added "When to add to CLAUDE.md" guidance with specific triggers (repeated mistakes, code review findings, recurring corrections).
* Updated compaction behavior: nested CLAUDE.md files in subdirectories are not re-injected automatically after `/compact`; only the project-root file is.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Updated third-party deployment pin documentation: Bedrock and Vertex AI now fall back to the previous model version at startup when the latest is unavailable (Foundry still errors without pinning).

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Updated `attempt` attribute definition: now represents total attempts made (1 = no retries).
* Added new "Detect retry exhaustion" section explaining how to use `attempt` to distinguish transient errors from non-retryable ones.

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Added documentation for two Homebrew casks: `claude-code` (stable) and `claude-code@latest` (latest).

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Updated `acceptEdits` mode: now auto-approves filesystem commands prefixed with safe env vars (`LANG`, `NO_COLOR`, etc.) or process wrappers (`timeout`, `nice`, `nohup`).

-----

## API changes

### New Documents

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

New documentation for the Advisor tool (beta: `advisor-tool-2026-03-01`). The advisor tool lets a faster executor model consult a more powerful advisor model mid-generation for strategic guidance. The advisor reads the full conversation transcript and returns a plan (typically 400–700 text tokens); the executor continues with the task at its lower rate. Documents model compatibility table (Haiku/Sonnet/Opus as executors, Opus as advisor), the `advisor_20260301` tool type, response structure with `advisor_result` and `advisor_redacted_result` variants, multi-turn usage, streaming behavior, usage and billing via `usage.iterations`, two-layer prompt caching (executor-side and advisor-side), combining with other tools, best practices for system prompt design, and cost control.

### Changed documents

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Sybill MCP server (`https://mcp.sybill.ai/mcp`) for sales calls, deals, and pipeline AI.
* Added Tines MCP server (user-specific URL) for workflow automation.
* Added MoSPI MCP server (`https://mcp.mospi.gov.in/`) for India's official statistics.
* Added incident.io MCP server (`https://mcp.incident.io/mcp`) for incident management.
* Added Unthread MCP server (`https://app.unthread.io/api/mcp`) for support ticket automation.
* Added Zoom for Claude MCP server (`https://mcp.zoom.us/mcp/zoom/streamable`) for meeting search and recaps.
* Removed Microsoft 365 MCP connector.
* Updated Aiwyn Tax description.

#### [agents-and-tools/tool-use/tool-reference](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/api/agents-and-tools/tool-use/tool-reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)]

* Added Advisor tool (`advisor_20260301`) to the server tools table with Beta status.

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Added `advisor-tool-2026-03-01` to the list of valid `AnthropicBeta` values.
* Added `BetaAdvisorMessageIterationUsage` model for advisor sub-inference token usage tracking.

#### [api/beta/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/0c6c99c/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* Added `advisor-tool-2026-03-01` beta header option.
* Added `advisor` to server tool names and documented `BetaAdvisorToolResultBlockParam` with `advisor_tool_result_error`, `advisor_result`, and `advisor_redacted_result` content variants.
