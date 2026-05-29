# [Claude docs changes for May 29th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/879fe70d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/879fe70d)]

## Executive Summary
- **Claude Opus 4.8 launches** as the new flagship model with adaptive-only thinking, `xhigh`/`high` effort defaults, fast mode at 2x the standard rate, and 1M-token context window
- **Dynamic Workflows** (research preview) let Claude orchestrate tens to hundreds of background subagents for large tasks; a new `ultracode` effort level uses `xhigh` reasoning + automatic workflow planning
- **Mid-conversation system messages** (Opus 4.8, Claude API only): insert `{"role": "system"}` messages mid-conversation to add instructions without invalidating the prompt-cache prefix
- **New `MessageDisplay` hook** in Claude Code lets hooks intercept and reformat assistant text as it renders on screen, without modifying the transcript
- **Batch processing** gains a documented table of unsupported parameters and new server-tool/web-search behavior notes

## New Claude Code versions

### [2.1.153](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/versions/2.1.153.md)

#### New features

* Added `skipLfs` option to `github`/`git` plugin marketplace sources to skip Git LFS downloads during clone and update
* Status line commands now receive `COLUMNS` and `LINES` environment variables so scripts can size output to the terminal width
* `/bg` while Claude is responding now continues the response in the background session instead of dropping it
* `/model` now saves the selection as the default for new sessions; press `s` in the picker to switch for the current session only (replaces the `d` key)

#### Existing feature improvements

* `claude agents`: autocomplete in the dispatch input now suggests native slash commands and bundled skills
* `claude agents`: PR column now shows `PR #N` for a single PR or `N PRs` for multiple
* `claude doctor` now shows the result of the most recent update attempt
* Combined separate MCP authentication startup notifications into a single message
* macOS: background agents now appear as "Claude Code" in Privacy & Security across upgrades

#### Major bug fixes

* Fixed stateful MCP servers without the optional GET SSE stream reconnect-looping on `tools/list` (regression in v2.1.147)
* Fixed regression where a custom API gateway could receive the user's Anthropic OAuth credential instead of the gateway's own token
* Fixed subagent frontmatter MCP servers ignoring `--strict-mcp-config`, `--bare`, remote mode, enterprise managed MCP, and managed-settings allow/deny policies
* Fixed excessive memory usage (multiple GB) when resuming a session by transcript file path on machines with many stored sessions
* Fixed `Agent` tool with `subagent_type: 'claude'` silently discarding outputs written to gitignored paths via a temporary worktree

### [2.1.154](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/versions/2.1.154.md)

#### New features

* **Claude Opus 4.8** is now available; defaults to `high` effort; use `/effort xhigh` for hardest tasks
* **Dynamic workflows**: ask Claude to write a workflow and it orchestrates tens to hundreds of background agents; use `/workflows` to view runs
* **Fast mode on Opus 4.8** available at 2x the standard rate (vs 3x for 4.6/4.7) with 2.5x the speed
* `claude agents`: type `! <command>` to run a shell command as a background session you can attach to and detach from; also available as `claude --bg --exec '<command>'`
* Plugins can now declare `defaultEnabled: false` in `plugin.json` or a marketplace entry; users opt in with `claude plugin enable`
* Stdio MCP server subprocesses now receive `CLAUDE_CODE_SESSION_ID` and `CLAUDECODE=1` in their environment
* `claude mcp list`/`get` now show unapproved `.mcp.json` servers as `⏸ Pending approval` instead of auto-approving when output is piped
* Streaming tool execution is now always enabled, including when telemetry is disabled or on Bedrock/Vertex/Foundry

#### Existing feature improvements

* The lean system prompt is now the default for all models except Haiku, Sonnet, and Opus 4.7 and earlier
* Claude now reserves multiple-choice questions for decisions it genuinely cannot make itself
* `/simplify` now runs a cleanup-only review (reuse, simplification, efficiency) instead of the full bug-hunting review
* `/plugin` Discover tab now pins plugins matching the current directory with a "suggested for this directory" annotation
* Renamed `/effort` slider labels from "Speed"/"Intelligence" to "Faster"/"Smarter"
* Claude in Chrome: pick which connected browser to use via `/chrome` or in-chat when multiple browsers are connected
* Deprecated `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` (will be removed 06/01)
* Improved auto-mode classifier's detection of data exfiltration, particularly bulk repository transfers

#### Major bug fixes

* Fixed `rm -rf $HOME` not being blocked as a dangerous path when `HOME` has a trailing slash
* Fixed background-agent completion notifications triggering premature "out of context" behavior on some 1M-context models
* Fixed orphaned `claude --bg-pty-host` processes spinning at 100% CPU after the daemon exits on macOS
* Fixed `worktree.baseRef: "head"` resolving to the main checkout's HEAD instead of the current worktree's HEAD when spawning subagents or calling `EnterWorktree` from inside a linked worktree
* Fixed a single invalid `allowedMcpServers`/`deniedMcpServers` entry in managed settings discarding all managed-settings policy

### [2.1.156](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/versions/2.1.156.md)

#### Major bug fixes

* Fixed an issue when using Opus 4.8 where thinking blocks were modified, leading to API errors

-----

## Claude Code changes

### New Documents

#### [Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

New document covering dynamic workflows (research preview, requires v2.1.154+). Workflows are JavaScript scripts Claude writes to orchestrate subagents at scale — dozens to hundreds of agents running in the background while the session stays responsive. Covers when to use workflows vs subagents/skills, running the bundled `/deep-research` command, having Claude write a custom workflow, the `ultracode` effort level that auto-plans workflows for every substantive task, and how to manage, pause, resume, and save runs.

### Changed documents

#### [Agent SDK / Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* New `MessageDisplay` hook added to the SDK hooks table: fires when an assistant message with text completes, for redacting or reformatting displayed text without changing the transcript [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L116)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#available-hooks)]

#### [Agent SDK / Python](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `MessageDisplay` hook added to the list of events supported by the Python SDK
* New note: on Linux, sandbox `failIfUnavailable` defaults to `False` in the Python SDK (unlike TypeScript where it defaults to `true`); commands run unsandboxed with a warning when the sandbox can't start unless `"failIfUnavailable": True` is set explicitly

#### [Agent SDK / TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `MessageDisplay` hook event type and `MessageDisplayHookInput` interface added, with `turn_id`, `message_id`, `index`, `final`, and `delta` fields
* New `failIfUnavailable` field documented on `SandboxSettings` (default `true` in TypeScript): stops at startup when the sandbox can't start; set to `false` to fall back to unsandboxed execution with a warning

#### [Agent View](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* New feature: type `! <command>` in the dispatch input to run a shell command as a background session; also available as `claude --bg --exec '<command>'`
* PR status indicator changed from a colored dot to labeled `PR #N` text (or `N PRs` for multiple)
* `/bg` while Claude is mid-response now continues the response in the background session
* `/model` picker: `s` key now switches session-only; `d` key removed

#### [Agents](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/agents.md) [[Source](https://code.claude.com/docs/en/agents)]

* "Worktrees" replaced with "Dynamic workflows" (`workflows.md`) as one of the four parallelism approaches in the comparison table

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--exec` flag: runs a shell command as a PTY-backed background job instead of a Claude session; use with `--bg`
* New `--prompt-suggestions` flag: emits a `prompt_suggestion` message in `--output-format stream-json --verbose` mode (off by default)
* `--fallback-model` now also covers retired or unavailable models in addition to overloaded ones

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New `/deep-research <question>` command: a bundled workflow that fans out web searches across several angles and returns a cited report
* New `/reload-skills` command: re-scans skill directories mid-session without restarting
* New `/simplify [target]` command: cleanup-only review (reuse, simplification, efficiency); use `/code-review` for bug hunting
* New `/workflows` command: opens a progress view for running and completed workflows
* `/code-review` updated: now accepts `ultra` level and `--fix` flag; `ultra` is the preferred alias for `/ultrareview`
* `/effort` now includes `ultracode` as a new level
* `/model` behavior changed: `Enter` saves as default; `s` applies session-only

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_WORKFLOWS`: disables dynamic workflows entirely
* New `CLAUDE_CODE_PROPAGATE_TRACEPARENT`: propagates W3C trace context to custom proxies
* New `OTEL_METRICS_INCLUDE_ENTRYPOINT`: includes session entrypoint in OpenTelemetry metrics attributes
* `CLAUDECODE` and `CLAUDE_CODE_SESSION_ID` now also set in stdio MCP server subprocesses
* `CLAUDE_EFFORT` now reports `ultra` value for ultracode sessions
* `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE` documented as deprecated

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `MessageDisplay` hook event: fires while assistant message text streams, delivering text in batches via a `delta` field; returns `displayContent` to replace what's rendered on screen without modifying the transcript
* `effort` field in hook input now reports `"ultra"` as a value (for ultracode sessions)
* `SessionStart` hook can now return `sessionTitle` (to name the session automatically) and `reloadSkills` (to trigger a skill re-scan after the hook installs new skills)
* `SessionStart` input now includes `session_title` so hooks can avoid overwriting a title the user set explicitly
* `${CLAUDE_PROJECT_DIR}` is now also set in the environment of stdio MCP servers and plugin LSP servers
* Updated hooks lifecycle diagram to include `MessageDisplay` as a display-only event

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `/btw` side-question overlay now supports `f` key to fork into a new full session, `x` to clear earlier exchanges, and `Up`/`Down` to scroll
* Prompt suggestions in print mode: off by default, enabled via `--prompt-suggestions` flag

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* `/` in vim normal mode now opens reverse history search (same as `Ctrl+R`)
* `modelPicker:setAsDefault` (key `d`) replaced with `modelPicker:thisSessionOnly` (key `s`)

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Pending approval servers from `.mcp.json` now appear in `claude mcp list` as `Pending approval`; `claude mcp get` also shows rejected status

#### [Model Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Claude Opus 4.8 is now the default `opus` alias on the Anthropic API (requires v2.1.154+); default effort is `high`
* New `ultracode` effort level: combines `xhigh` reasoning with automatic dynamic workflow orchestration; session-only, cannot be set via `effortLevel` or `--effort` in config
* `/model` now saves as default by default; `s` key applies to the current session only

#### [Plugin Marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* New `defaultEnabled` field in marketplace entries (takes precedence over `plugin.json`): ships plugins disabled by default, requiring user opt-in
* `claude plugin marketplace remove` now supports `--scope` option to remove from a specific settings scope without uninstalling
* `claude plugin marketplace list --json` now includes source-specific fields in output

#### [Plugins Reference](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New `defaultEnabled` field in `plugin.json`: ships a plugin disabled by default; users opt in with `/plugin` or `claude plugin enable` (requires v2.1.154+)
* `MessageDisplay` hook event type added to plugin hook events

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* `claude doctor` now shows the result of the most recent update attempt and lists fixes when the npm global directory isn't writable

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New `disallowed-tools` frontmatter field: removes specific tools from Claude's available pool while a skill is active (useful for background loops to prevent `AskUserQuestion`)
* `${CLAUDE_EFFORT}` substitution now also reports the `ultra` value (for ultracode)
* `allowed-tools` now accepts comma-separated strings in addition to space-separated

#### [Status Line](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* `COLUMNS` and `LINES` environment variables are now set before status line scripts run, enabling terminal-width-aware output (requires v2.1.153+)
* `effort.level` field now reports `ultra` value for ultracode sessions

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* MCP restrictions (`--strict-mcp-config`, `--bare`, enterprise managed MCP, `allowedMcpServers`/`deniedMcpServers`) now apply to MCP servers declared in subagent frontmatter as of v2.1.153

#### [Voice Dictation](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* Voice dictation is now unavailable when HIPAA compliance is enabled for the organization

-----

## API changes

### New Documents

#### [Build with Claude / Mid-Conversation Effort Example](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/mid-conversation-effort-example.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example)]

New guide showing how to build an orchestration mode using mid-conversation system messages. Demonstrates a full agentic loop that toggles `xhigh` effort and automatic workflow use via system messages appended mid-conversation, with parallel subagent fan-out and structured `report_findings` results. Available on Claude Opus 4.8 only.

#### [Build with Claude / Mid-Conversation System Messages](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

New guide for the mid-conversation system message feature (Claude Opus 4.8, Claude API only). Explains how appending `{"role": "system"}` messages mid-conversation allows adding instructions without invalidating the prompt-cache prefix. Covers placement constraints, caching interaction, use cases (mode switches, per-turn context injections, policy changes), and limitations.

#### [Managed Agents / Cloud Sandboxes Reference](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/managed-agents/cloud-sandboxes-reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/cloud-sandboxes-reference)]

New reference page documenting the specifications of cloud sandboxes for Managed Agents. Lists pre-installed languages (Python 3.12+, Node.js 20+, Go 1.22+, Rust, Java, Ruby, PHP, C/C++), databases (SQLite local, PostgreSQL/Redis clients), system utilities, and development tools.

### Changed documents

#### [Agents and Tools / Agent Skills / Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Code examples updated to `claude-opus-4-8`

#### [Agents and Tools / MCP Connector](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* MCP connector now supports Message Batches API requests; MCP tool calls via the Batches API are priced the same as regular requests

#### [Agents and Tools / Tool Use / Advisor Tool](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Claude Opus 4.8 added as a supported advisor and executor model
* New `stop_reason` field on `BetaAdvisorResultBlock` and `BetaAdvisorRedactedResultBlock`: reports the advisor sub-inference's stop reason (same values as top-level `stop_reason`); `max_tokens` indicates the advisor's output was truncated

#### [Agents and Tools / Tool Use / Code Execution Tool](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Claude Opus 4.8 added to the supported model table for both `code_execution_20250825` and `code_execution_20260120` tool versions

#### [Agents and Tools / Tool Use / Overview](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Tool use system prompt token counts updated for all models; Claude Opus 4.8 added (290 tokens for `auto`/`none`, 410 for `any`/`tool`)
* Token counts for existing models changed significantly (e.g., Opus 4.7 updated from 346/313 to 675/804)

#### [Agents and Tools / Tool Use / Web Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Claude Opus 4.8 added to the dynamic filtering support list for `web_search_20260209`
* New note: the Batches API throttles web search per organization for large batches; links to the Claude Console Limits page to view or request rate limit increases

#### [API / Beta](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Two new beta header values added: `thinking-token-count-2026-05-13` and `mid-conversation-system-2026-04-07`
* Claude Opus 4.8 (`"claude-opus-4-8"`) added to the model enum with description "Frontier intelligence for long-running agents and coding"
* `BetaAdvisorResultBlock` and `BetaAdvisorRedactedResultBlock` now include `stop_reason` field

#### [API / Messages](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/api/messages.md) [[Source](https://platform.claude.com/docs/en/api/messages)]

* New `MidConversationSystemBlockParam` type added: represents system instructions that appear mid-conversation instead of via the top-level `system` parameter; type is `"mid_conv_system"`
* New `url_not_in_prior_context` error code added to the web fetch error enum
* `ContentBlockParam` union expanded to include `MidConversationSystemBlockParam` (now 14 variants)

#### [API / Messages / Create](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

* `role` field now accepts `"system"` in addition to `"user"` and `"assistant"` to support mid-conversation system messages
* `MidConversationSystemBlockParam` documented as a new content block type
* Claude Opus 4.8 added to the model enum

#### [Build with Claude / Batch Processing](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* New pricing row for Claude Opus 4.8: $2.50/MTok batch input, $12.50/MTok batch output
* New table documenting unsupported parameters in batch requests (e.g., `stream`, `speed`, `store`, `cache_hint`, `max_tokens: 0`, `research_preview_2026_02`) with reasons for each
* New "Server tools and the agentic loop" section: all server tools work in batches; the batch loop runs more iterations per turn before returning `pause_turn`; `web_search` is throttled per organization in batch mode
* Extended output beta (`output-300k-2026-03-24`) now includes Claude Opus 4.8

#### [Build with Claude / Context Windows](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Claude Opus 4.8 added to the 1M-token context window group; note added that on Microsoft Foundry, Opus 4.8 has a 200k-token context window
* Compaction beta support list updated to include Claude Opus 4.8

#### [Build with Claude / Effort](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Claude Opus 4.8 added to supported models for `max` and `xhigh` effort levels
* New "Recommended effort levels for Claude Opus 4.8" section: recommends `xhigh` for coding/agentic use, `high` as default; links to the new orchestration mode guide
* New note clarifying that Claude Code's `ultracode` mode is not an API effort level — it pairs `xhigh` effort with multi-agent permissions via mid-conversation system messages

#### [Build with Claude / Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Claude Opus 4.8 added: manual extended thinking (`budget_tokens`) not supported (returns 400); adaptive thinking only, with `display` defaulting to `"omitted"`
* New `usage.output_tokens_details.thinking_tokens` field documented for tracking how many billed output tokens were spent on reasoning
* Model comparison table expanded with Claude Opus 4.8 column

#### [Build with Claude / Fast Mode](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Claude Opus 4.8 added to supported fast mode models at $10/$50 per MTok (vs $30/$150 for 4.6/4.7) — 2x the standard rate
* Fast mode for Opus 4.6 is now deprecated; will be removed approximately 30 days after the Opus 4.8 launch
* Fast mode for Opus 4.8 is Claude API only (not available on Bedrock, Vertex, or Foundry)

#### [Build with Claude / Prompt Caching](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* New pricing row for Claude Opus 4.8: $5/MTok input, $0.50/MTok cache hits, $25/MTok output; added to 1,024-token minimum cacheable prompt length group
* New note: on Opus 4.8, you can append a `{"role": "system"}` message mid-conversation without invalidating cached prefixes

#### [Build with Claude / Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Claude Opus 4.8 added to the supported model list for structured outputs on the Claude API, Amazon Bedrock, and Vertex AI

#### [Build with Claude / Task Budgets](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/task-budgets.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/task-budgets)]

* Task budgets now listed as available in beta on Claude Opus 4.8 (previously only Opus 4.7)
* Code examples updated to use the streaming pattern (`client.beta.messages.stream`)

#### [Build with Claude / Working with Messages](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/build-with-claude/working-with-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]

* New note: `temperature`, `top_p`, and `top_k` are not supported on Claude Opus 4.7 and later (including 4.8); setting them returns a 400 error
* New note: refusal responses (`stop_reason: "refusal"`) on Opus 4.7+ include a `stop_details` object identifying the policy category
* New "System role in messages" section documenting mid-conversation system messages for Opus 4.8

#### [Get Started](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/get-started.md) [[Source](https://platform.claude.com/docs/en/get-started)]

* Prerequisites section now explicitly lists having an API key
* Quickstart steps expanded to include more language tabs (C#, Go, PHP, Ruby)
* Step 2 now includes creating a virtualenv before installing the SDK
* Example output simplified to show a condensed response format

#### [Intro](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/intro.md) [[Source](https://platform.claude.com/docs/en/intro)]

* Featured "latest model" updated to Claude Opus 4.8, described as Anthropic's most capable model for complex reasoning and agentic coding

#### [Managed Agents / Agent Setup](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* Note added: fast mode for Opus 4.6 is deprecated as of the Opus 4.8 launch and will be removed approximately 30 days later

#### [Managed Agents / Environments](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/managed-agents/environments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/environments)]

* Terminology updated throughout: "cloud container" renamed to "cloud sandbox"; broken link updated from `cloud-containers.md` to `cloud-sandboxes-reference.md`

#### [Managed Agents / Overview](https://github.com/gpambrozio/ClaudeDocs/blob/879fe70d/docs-md/api/managed-agents/overview.md) [[Source](https://platform.claude.com/docs/en/managed-agents/overview)]

* "Container" terminology replaced with "sandbox" throughout; code examples updated to `claude-opus-4-8`
