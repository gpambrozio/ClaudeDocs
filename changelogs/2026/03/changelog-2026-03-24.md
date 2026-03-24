# [Claude docs changes for March 24th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e1f6613bbfe25e9a6689f3251abc2efcfe955908) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e1f6613bbfe25e9a6689f3251abc2efcfe955908)]

## Executive Summary
- **Computer Use on Desktop (macOS):** Claude can now open apps and control your screen on macOS (Pro/Max plans). New documentation covers enabling it, per-app permission tiers, and safety boundaries.
- **Cloud Scheduled Tasks:** New cloud-based scheduled tasks run on Anthropic infrastructure and keep running even when your machine is off. Create them from the web, Desktop app, or CLI via `/schedule`.
- **Dispatch Integration:** Desktop now supports Dispatch — send a task from your phone's Claude app and a Desktop Code session spawns automatically.
- **New Platforms & Integrations overview:** New dedicated page comparing all Claude Code surfaces (CLI, Desktop, Web, IDE extensions) and remote access options.
- **Agent SDK Tool Search:** New dedicated guide for MCP tool search, which is now on by default and supports up to 10,000 tools.

-----

## Claude Code changes

### New Documents

#### [Platforms and integrations](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/platforms.md) [[Source](https://code.claude.com/docs/en/platforms)]

New overview page comparing all Claude Code surfaces (CLI, Desktop, VS Code, JetBrains, Web) and integrations (Chrome, GitHub Actions, GitLab, Code Review, Slack). Includes a table for remote access options (Dispatch, Remote Control, Channels, Slack, Scheduled tasks) with trigger, runtime, setup, and best-use-case columns.

#### [Schedule tasks on the web](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/web-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/web-scheduled-tasks)]

New documentation for cloud scheduled tasks that run on Anthropic-managed infrastructure. Covers creating tasks from the web, Desktop app, or CLI (`/schedule`), selecting repositories and environments, configuring MCP connectors, frequency options (hourly, daily, weekdays, weekly), branch permissions, and task management. Cloud tasks require no machine to be on and are available to Pro, Max, Team, and Enterprise users.

### Changed documents

#### [Claude Code on the web](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Added a new "Schedule recurring tasks" section linking to the cloud scheduled tasks guide. [[line ~173](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L173)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Added `/schedule [description]` command for creating, updating, listing, or running cloud scheduled tasks conversationally. [[line ~59](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/commands.md?plain=1#L59)]

#### [Common workflows](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Added a new "Run Claude on a schedule" workflow section with a comparison table of cloud tasks, Desktop tasks, GitHub Actions, and `/loop`, plus guidance on writing effective prompts for autonomous runs. [[line ~1290](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/common-workflows.md?plain=1#L1290)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added **Computer Use** feature section: lets Claude open apps and control your screen on macOS (Pro/Max only, research preview). Covers enabling it, required macOS permissions (Accessibility + Screen Recording), per-app permission tiers (view-only for browsers, click-only for terminals/IDEs, full control for everything else), and denied-apps configuration. [[line ~106](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/desktop.md?plain=1#L106)]
* Added **Dispatch integration** section: Dispatch (in the Cowork tab) can spawn Desktop Code sessions from a phone message; sessions appear with a "Dispatch" badge in the sidebar and send push notifications on completion. [[line ~199](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/desktop.md?plain=1#L199)]
* Added a **scheduling options comparison table** showing cloud vs. Desktop vs. `/loop` across dimensions like machine requirements, local file access, MCP servers, and minimum interval. [[line ~376](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/desktop.md?plain=1#L376)]
* Clarified that the Schedule page now supports both **local** and **remote** task types; creating a local task now requires choosing "New local task" from the modal. [[line ~406](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/desktop.md?plain=1#L406)]
* Updated the CLI comparison and capability tables to include Computer Use and Dispatch as Desktop-only features. [[line ~546](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/desktop.md?plain=1#L546)]

#### [Index](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Added a "Schedule recurring tasks" section describing cloud tasks, Desktop tasks, and `/loop`. [[line ~194](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/index.md?plain=1#L194)]
* Added Dispatch to the "Work from anywhere" section and a "Run Claude on a recurring schedule" row to the platform comparison table. [[line ~206](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/index.md?plain=1#L206)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* MCP server listing reordered (no new servers, ordering changes only).

#### [Remote control](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added a "Choose the right approach" comparison table covering Dispatch, Remote Control, Channels, Slack, and Scheduled Tasks — with trigger, runtime, setup, and best-for columns. [[line ~186](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/remote-control.md?plain=1#L186)]

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Added a "What sandboxing does not cover" section noting that built-in file tools (Read/Edit/Write) bypass the sandbox and use permissions directly, and that computer use on Desktop runs on the actual desktop rather than in an isolated environment. [[line ~317](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/sandboxing.md?plain=1#L317)]

#### [Scheduled tasks](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Added a scheduling options comparison table (Cloud vs. Desktop vs. `/loop`) at the top of the document. [[line ~6](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/scheduled-tasks.md?plain=1#L6)]
* Updated references to point to cloud scheduled tasks alongside Desktop tasks as the recommended durable scheduling alternative to session-scoped `/loop`. [[line ~143](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/claude-code/scheduled-tasks.md?plain=1#L143)]

-----

## API changes

### New Documents

#### [Scale to many tools with tool search](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/tool-search.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/tool-search)]

New dedicated guide for MCP tool search. Tool search is now **on by default** — tool definitions are withheld from context and loaded on demand. Supports up to 10,000 tools, returns 3-5 most relevant per search. Requires Claude Sonnet 4 or Opus 4 (no Haiku). Documents the `ENABLE_TOOL_SEARCH` environment variable (`true`/`auto`/`auto:N`/`false`), optimization tips for tool naming and descriptions, and limits.

### Changed documents

#### [Custom tools](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/custom-tools.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/custom-tools)]

* Major rewrite with improved structure: added a quick reference table at the top, separated tool definition from calling/registration, added Python examples alongside TypeScript throughout, and clarified handler return value requirements. [[line ~1](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/custom-tools.md?plain=1#L1)]
* Added guidance on making parameters optional in both Python and TypeScript. [[line ~62](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/custom-tools.md?plain=1#L62)]

#### [MCP (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/mcp.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp)]

* Removed the "Alternative: Change the permission mode" section and replaced it with a note clarifying that `acceptEdits` does **not** auto-approve MCP tools (only file edits), and that `bypassPermissions` is broader than necessary — recommending `allowedTools` wildcards instead. [[line ~111](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/mcp.md?plain=1#L111)]
* Tool search configuration details moved to the new dedicated [tool-search.md](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/tool-search.md) page. [[line ~199](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/mcp.md?plain=1#L199)]
* Fixed a code example bug: changed `message.content` to `message.message.content` when iterating assistant message blocks. [[line ~329](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/mcp.md?plain=1#L329)]

#### [Python SDK reference](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* Added a full `ToolAnnotations` reference table (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`, `title`) with defaults and a code example. [[line ~150](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/python.md?plain=1#L150)]
* Added a `@dataclass` vs `TypedDict` runtime behavior note clarifying attribute access vs key access, with a `ThinkingConfigEnabled` example. [[line ~544](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/python.md?plain=1#L544)]
* Added `max_output_tokens` as a new `AssistantMessageError` literal type. [[line ~1213](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/python.md?plain=1#L1213)]
* Noted that TypeScript supports additional hook events not yet in Python: `SessionStart`, `SessionEnd`, `Setup`, `TeammateIdle`, `TaskCompleted`, `ConfigChange`, `WorktreeCreate`, `WorktreeRemove`. [[line ~1510](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/python.md?plain=1#L1510)]
* Improved the interrupt example: added draining of the interrupted task's `ResultMessage` before sending a new query, and added a note explaining buffer behavior after `interrupt()`. [[line ~477](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/python.md?plain=1#L477)]

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added new MCP servers: Google Cloud BigQuery, Zapier, Windsor.ai, Jotform, Aiwyn Tax, Brex, G2, Base44, Intuit TurboTax, Metaview. Various reorderings of existing entries.

#### [TypeScript SDK reference](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Added a full `ToolAnnotations` reference table with defaults and a code example. [[line ~62](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/typescript.md?plain=1#L62)]
* Added `SDKLocalCommandOutputMessage` type (emitted for local slash commands like `/voice` or `/cost`). [[line ~2517](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/typescript.md?plain=1#L2517)]
* Added `fast_mode_state` field (`"off" | "cooldown" | "on"`) to `SDKControlInitializeResponse`. [[line ~319](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/typescript.md?plain=1#L319)]
* Added `max_output_tokens` as a new `SDKAssistantMessageError` literal type. [[line ~680](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/typescript.md?plain=1#L680)]
* `supportedAgents()` return type now documented as `AgentInfo[]`. [[line ~297](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/typescript.md?plain=1#L297)]

#### [User input](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/user-input.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/user-input)]

* `canUseTool` callback now documented as receiving **three** arguments: `toolName`, `input`, and a new `options`/`context` parameter containing permission suggestions and a cancellation signal. [[line ~35](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/user-input.md?plain=1#L35)]
* Updated code examples to use `isinstance(message, ResultMessage) and message.subtype == "success"` instead of `hasattr(message, "result")`. [[line ~113](https://github.com/gpambrozio/ClaudeDocs/blob/e1f6613bbfe25e9a6689f3251abc2efcfe955908/docs-md/api/agent-sdk/user-input.md?plain=1#L113)]
