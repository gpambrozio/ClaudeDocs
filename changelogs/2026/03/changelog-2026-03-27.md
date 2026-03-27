# [Claude docs changes for March 27th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/3d15ee0) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/3d15ee0)]

## Executive Summary
- Major expansion of tool use API documentation: 14 new guides covering how tool use works, building agents, strict mode, parallel calls, server tools, the Tool Runner SDK, and more
- New `TaskCreated` and `TaskCompleted` hooks for agent teams, enabling enforcement of naming conventions and completion criteria
- `budget_tokens` for extended thinking is now deprecated on both Opus 4.6 and Sonnet 4.6 — migrate to adaptive thinking with the `effort` parameter
- New `.worktreeinclude` file support for automatically copying gitignored files (like `.env`) to git worktrees
- New `@claude review once` command for one-off code reviews without subscribing to future push-triggered reviews

## New Claude Code versions

### [2.1.85](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/versions/2.1.85.md)

#### New features

* Added `CLAUDE_CODE_MCP_SERVER_NAME` and `CLAUDE_CODE_MCP_SERVER_URL` environment variables to MCP `headersHelper` scripts, allowing one helper to serve multiple servers
* Added conditional `if` field for hooks using permission rule syntax (e.g., `Bash(git *)`) to filter when they run, reducing process spawning overhead
* Added timestamp markers in transcripts when scheduled tasks (`/loop`, `CronCreate`) fire
* Deep link queries (`claude-cli://open?q=…`) now support up to 5,000 characters, with a "scroll to review" warning for long pre-filled prompts
* MCP OAuth now follows RFC 9728 Protected Resource Metadata discovery to find the authorization server
* Plugins blocked by organization policy (`managed-settings.json`) can no longer be installed or enabled, and are hidden from marketplace views
* `PreToolUse` hooks can now satisfy `AskUserQuestion` by returning `updatedInput` alongside `permissionDecision: "allow"`, enabling headless integrations that collect answers via their own UI
* `tool_parameters` in OpenTelemetry tool_result events are now gated behind `OTEL_LOG_TOOL_DETAILS=1`

#### Existing feature improvements

* Improved @-mention file autocomplete performance on large repositories
* Improved PowerShell dangerous command detection
* Improved scroll performance with large transcripts by replacing WASM yoga-layout with a pure TypeScript implementation
* Reduced UI stutter when compaction triggers on large sessions

#### Major bug fixes

* Fixed `/compact` failing with "context exceeded" when the conversation has grown too large for the compact request itself to fit
* Fixed `/plugin enable` and `/plugin disable` failing when a plugin's install location differs from where it's declared in settings
* Fixed `--worktree` exiting with an error in non-git repositories before the `WorktreeCreate` hook could run
* Fixed `deniedMcpServers` setting not blocking claude.ai MCP servers
* Fixed `switch_display` in the computer-use tool returning "not available in this session" on multi-monitor setups
* Fixed crash when `OTEL_LOGS_EXPORTER`, `OTEL_METRICS_EXPORTER`, or `OTEL_TRACES_EXPORTER` is set to `none`
* Fixed diff syntax highlighting not working in non-native builds
* Fixed MCP step-up authorization failing when a refresh token exists — servers requesting elevated scopes via `403 insufficient_scope` now correctly trigger the re-authorization flow
* Fixed memory leak in remote sessions when a streaming response is interrupted
* Fixed persistent ECONNRESET errors during edge connection churn by using a fresh TCP connection on retry
* Fixed prompts getting stuck in the queue after running certain slash commands, with up-arrow unable to retrieve them
* Fixed Python Agent SDK: `type:'sdk'` MCP servers passed via `--mcp-config` are no longer dropped during startup
* Fixed raw key sequences appearing in the prompt when running over SSH or in the VS Code integrated terminal
* Fixed Remote Control session status staying stuck on "Requires Action" after a permission is resolved
* Fixed shift+enter and meta+enter being intercepted by typeahead suggestions instead of inserting newlines
* Fixed stale content bleeding through when scrolling up during streaming
* Fixed terminal left in enhanced keyboard mode after exit in Ghostty, Kitty, WezTerm, and other terminals supporting the Kitty keyboard protocol

-----

## Claude Code changes

### New Documents

#### [Explore the .claude directory](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

An interactive explorer for the `.claude` directory structure, documenting every configuration file Claude Code reads — `CLAUDE.md`, `settings.json`, `rules/`, `skills/`, `commands/`, `agents/`, and more. Includes a file reference table with scope, commit status, and purpose for each entry, plus commands like `/context`, `/memory`, `/hooks`, and `/permissions` for inspecting what actually loaded in the current session.

#### [Explore the context window](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

An interactive timeline walkthrough showing what loads into the context window at each phase of a session — system prompt, CLAUDE.md, memory, skills, MCP tools, file reads, hooks — with representative token counts. Explains what loads silently before the first prompt, how subagents isolate their own context, and how `/compact` restructures the conversation. Use `/context` for a live breakdown.

### Changed documents

#### [Agent teams](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Added `TaskCreated` hook reference: runs when a task is being created, allowing enforcement or prevention via exit code 2. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/agent-teams.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/agent-teams#choose-a-display-mode)]

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added link to the new interactive context window walkthrough for understanding how context fills during a session. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/best-practices.md?plain=1#L1)]

#### [Code review](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Added `@claude review once` command for a one-shot review without subscribing the PR to future push-triggered reviews. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/code-review.md?plain=1#L113)] [[Source](https://code.claude.com/docs/en/code-review#manually-trigger-reviews)]
* Added Check run output section: each review populates a **Claude Code Review** check run with a severity table (Important/Nit/Pre-existing) and annotations directly on diff lines. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/code-review.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/code-review#check-run-output)]
* Added machine-readable severity JSON in the check run output, parseable with `gh` and `jq` for CI-based merge gating. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/code-review.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/code-review#check-run-output)]
* Added Auto-fix pull requests section: Claude can watch a PR and automatically push fixes for CI failures and review comments. [[line ~80](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/code-review.md?plain=1#L80)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added `.worktreeinclude` file support: list gitignored files (e.g., `.env`, `.env.local`) to automatically copy them into new worktrees created by `--worktree`, subagent worktrees, and parallel desktop sessions. [[line 696](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/common-workflows.md?plain=1#L696)] [[Source](https://code.claude.com/docs/en/common-workflows#copy-gitignored-files-to-worktrees)]
* Added section on managing worktrees manually via `git` for more control over location and branch configuration. [[line ~710](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/common-workflows.md?plain=1#L710)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_STREAM_IDLE_TIMEOUT_MS` — configures the streaming idle watchdog timeout in milliseconds (default: 90000). Useful for long-running tools or slow networks that trigger premature timeout errors. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/env-vars.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Features overview](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Added MCP server context cost details: tool names load at session start with full schemas deferred until needed, and added a reliability note about silent MCP disconnections. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/features-overview.md?plain=1#L1)]
* Added link to the new interactive context window visualization.

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `TaskCreated` hook: fires when a task is being created via the `TaskCreate` tool. Exit with code 2 to prevent creation; return `{"continue": false}` to stop the teammate entirely. [[line 1216](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/hooks.md?plain=1#L1216)] [[Source](https://code.claude.com/docs/en/hooks#taskcreated)]
* Added `TaskCompleted` hook: fires when a task is being marked as completed (via `TaskUpdate` or when a teammate finishes with in-progress tasks). Can enforce completion criteria like passing tests. [[line ~1260](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/hooks.md?plain=1#L1260)]
* Updated lifecycle diagram and event table to include `TaskCreated` and `TaskCompleted`. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/hooks.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Atlassian Rovo, Workato, and Port IO as new remote MCP server providers. [[lines 50, 546, 698](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/mcp.md?plain=1#L50)]
* Added documentation that MCP tool search is enabled by default: tool definitions are deferred until Claude needs them, keeping context usage low as more servers are added. [[line 1596](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/claude-code/mcp.md?plain=1#L1596)] [[Source](https://code.claude.com/docs/en/mcp#scale-with-mcp-tool-search)]

-----

## API changes

### New Documents

#### [API and data retention](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/build-with-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]

New reference document covering Anthropic's data retention policies and Zero Data Retention (ZDR) eligibility across all API features. Includes a comprehensive ZDR eligibility table for every feature (Messages API, token counting, web search, code execution, Files API, agent skills, MCP connector, etc.) with retention details and footnotes, plus guidance on CORS limitations and FAQ.

#### [Claude API skill](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]

Documents the `claude-api` open-source Agent Skill bundled with Claude Code. It provides Claude with up-to-date API reference material and SDK documentation for 8 programming languages (Python, TypeScript, Java, Go, Ruby, C#, PHP, cURL). Covers when it auto-activates (on detecting Anthropic SDK imports), how to invoke it manually with `/claude-api`, supported language features table, and installation from the Anthropic skills repository.

#### [Build a tool-using agent (tutorial)](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/build-a-tool-using-agent.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)]

Step-by-step tutorial building a calendar-management agent across five "rings": (1) single tool single turn, (2) the agentic loop, (3) multiple tools with parallel calls, (4) error handling with `is_error`, and (5) the Tool Runner SDK abstraction. Each ring is a complete runnable Python program with annotated code.

#### [Define tools](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/define-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)]

Reference guide for specifying tool schemas: name, description, `input_schema`, `input_examples`, and optional properties. Covers model selection guidance, `tool_choice` modes (auto/any/tool/none), best practices for descriptions and schema design, and how the tools system prompt is constructed.

#### [Handle tool calls](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]

Reference for the tool-call lifecycle: reading `tool_use` blocks, formatting `tool_result` responses, ordering requirements (tool results must come first in the content array), and signaling errors with `is_error`. Covers differences between client and server tools and common formatting errors.

#### [How tool use works](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/how-tool-use-works.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)]

Conceptual overview explaining the three execution categories (user-defined client tools, Anthropic-schema client tools, server-executed tools), the agentic loop mechanics, the server-side loop and `pause_turn`, and when to use tools vs. when not to. Includes a comparison table of approaches.

#### [Manage tool context](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/manage-tool-context.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context)]

Guide for managing context window pressure from tool definitions and accumulated results. Covers four approaches: tool search (defer large toolsets), programmatic tool calling (collapse round-trips), prompt caching (amortize definition costs), and context editing (trim stale results). Includes a recommended starting sequence for high-volume agents.

#### [Parallel tool use](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)]

Covers parallel tool calls: how Claude sends multiple `tool_use` blocks in one response, the requirement to return all results in a single user message, how to disable parallel calls via `disable_parallel_tool_use`, and troubleshooting tips including model-specific behavior for Claude 4 vs earlier models.

#### [Server tools](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/server-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]

Documents shared mechanics of server-executed tools: the `server_tool_use` block, handling `pause_turn` continuation for long-running server-side loops, ZDR considerations and `allowed_callers`, domain filtering with allow/block lists and wildcard support, dynamic filtering with code execution, streaming server-tool events, and batch request support.

#### [Strict tool use](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/strict-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)]

Documents `strict: true` on tool definitions: uses grammar-constrained sampling to guarantee Claude's tool inputs match the JSON Schema exactly. Explains why this matters for agents (type-safe parameters, no retry loops), quick start example, and common use cases for validated tool inputs and agentic workflows.

#### [Tool combinations](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/tool-combinations.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-combinations)]

Documents common patterns for pairing Anthropic-provided tools: research agent (`web_search` + `code_execution`), coding agent (`text_editor` + `bash`), cite-then-fetch (`web_search` + `web_fetch`), long-running agent (`memory` + any toolset), and all-in-one (`computer_use`).

#### [Tool reference](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/tool-reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)]

Directory of all Anthropic-provided tools with their `type` strings, execution location, and GA status. Also documents optional properties available on any tool definition: `cache_control`, `strict`, `defer_loading`, `allowed_callers`, `input_examples`, and `eager_input_streaming`, with links to each feature's guide. Explains tool versioning conventions (capability-keyed, model-keyed, variants, legacy).

#### [Tool Runner (SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/tool-runner.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner)]

Documents the SDK abstraction that handles the agentic loop automatically (Python, TypeScript, Ruby). Covers the `@beta_tool` decorator for Python, iterating over the runner, `until_done()`, advanced usage (inspecting/modifying tool results, `set_messages_params`, `append_messages`), debugging with `ANTHROPIC_LOG`, intercepting tool errors, modifying tool results for prompt caching, and streaming.

#### [Tool use with prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/tool-use-with-prompt-caching.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)]

Reference for placing `cache_control` breakpoints on tool definitions, how `defer_loading` preserves the prompt cache when tools are discovered dynamically, what changes invalidate the cache (tool definitions, `tool_choice`, `disable_parallel_tool_use`, images, thinking parameters), and a per-tool caching interaction table.

#### [Troubleshooting tool use](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

Symptom-to-fix tables for common tool use issues: wrong tool called, invented parameters, parallel calls not working, cache invalidation, request-time errors, and JSON escaping differences introduced in Opus 4.6+.

### Changed documents

#### [Agent skills overview](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/agent-skills/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

* Added the `claude-api` open-source skill to the list of Anthropic-published skills, with a reference to its dedicated documentation page. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/agent-skills/overview.md?plain=1#L1)]
* Added data retention section: Agent Skills is not covered by ZDR arrangements, with a link to the new API and data retention reference. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/agent-skills/overview.md?plain=1#L1)]

#### [Migration guide](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* Updated interleaved thinking migration: adaptive thinking now automatically enables interleaved thinking on **both** Opus 4.6 and Sonnet 4.6 (previously only Opus 4.6). [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/about-claude/models/migration-guide.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]
* Added comprehensive adaptive thinking migration section for Sonnet 4.6 with use-case guidance for autonomous multi-step agents, computer use agents, and bimodal workloads, with recommended effort levels. [[line 262](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/about-claude/models/migration-guide.md?plain=1#L262)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]
* Added `budget_tokens` deprecation guidance with migration path and temporary migration patterns for coding/agentic vs. chat use cases. [[line 298](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/about-claude/models/migration-guide.md?plain=1#L298)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

#### [Release notes](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added note that code execution tool, web fetch tool, tool search tool, tool use examples, and memory tool are now generally available (no beta header required). [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/release-notes/overview.md?plain=1#L34)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
* Added note about citable documents support in client-side tool results. [[line 146](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/release-notes/overview.md?plain=1#L146)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
* Added note about `disable_parallel_tool_use` in the `tool_choice` field. [[line 366](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/release-notes/overview.md?plain=1#L366)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

#### [Ruby SDK](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/api/sdks/ruby.md) [[Source](https://platform.claude.com/docs/en/api/sdks/ruby)]

* Added reference to the Tool Runner (SDK) documentation for structured data classes and tool use patterns. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/api/sdks/ruby.md?plain=1#L1)]

#### [Tool use overview](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Rewrote introduction to explain the client/server tool distinction upfront with a minimal server tool example. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L1)]
* Added navigation section linking to new sub-pages: how-tool-use-works, build-a-tool-using-agent, and tool-reference. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L1)]
* Added note promoting strict tool use with a link to the new strict-tool-use page. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L1)]

#### [What's new in Claude 4.6](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/about-claude/models/whats-new-claude-4-6.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]

* Added tool use examples as a new capability reference. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L1)]
* Added deprecation notice: `thinking: {type: "enabled", budget_tokens: N}` is deprecated on Opus 4.6 and Sonnet 4.6; Sonnet 4.6 interleaved thinking beta header is still functional but manual mode is deprecated. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/3d15ee0/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L1)]
