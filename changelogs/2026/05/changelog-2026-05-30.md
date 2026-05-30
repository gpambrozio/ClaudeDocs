# [Claude docs changes for May 30th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/faf9833043db19e98e3d355d823a5f889830ad7d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/faf9833043db19e98e3d355d823a5f889830ad7d)]

## Executive Summary
- Skills-directory plugins now auto-load from `.claude/skills/` without a marketplace install, and a new `claude plugin init` command scaffolds them in place
- WebSocket (`type: "ws"`) added as a fourth MCP server transport type for persistent bidirectional connections
- Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8 (opt in with `CLAUDE_CODE_ENABLE_AUTO_MODE=1`)
- `EnterWorktree` can now switch between Claude-managed worktrees mid-session without returning to the canonical repo root
- Memory stores documented with a 2,000-memory limit and new best practices section for staying under it

## New Claude Code versions

### [2.1.157](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/versions/2.1.157.md)

#### New features

* Plugins in `.claude/skills` directories are now automatically loaded — no marketplace or install step required
* Added `claude plugin init <name>` to scaffold a new plugin directly in `.claude/skills`
* Added autocomplete for `/plugin` arguments: subcommands, installed plugin names, and plugins from known marketplaces
* `claude agents`: the `agent` field in `settings.json` is now honored for dispatched sessions; pass `--agent <name>` to override it per session
* `EnterWorktree` can now switch between Claude-managed worktrees mid-session
* `tool_decision` telemetry events now include `tool_parameters` (bash commands, MCP/skill names) when `OTEL_LOG_TOOL_DETAILS=1`
* Added a "Workflow keyword trigger" setting in `/config` to stop the word "workflow" in a prompt from triggering a dynamic workflow
* Pressing Backspace immediately after a workflow trigger keyword now dismisses the workflow request (same as `alt+w`)

#### Existing feature improvements

* Worktrees managed by Claude are now left unlocked when the agent finishes, so `git worktree remove`/`prune` can clean them up
* `/terminal-setup` now disables GPU acceleration in VS Code, Cursor, and Windsurf integrated terminals to prevent garbled-text rendering
* Feature of the Week credit-claim status now appears as a notification in the status area instead of a line above the prompt
* `claude agents`: slash-command autocomplete in the dispatch input now matches substrings
* Removed the "bash commands will be sandboxed" startup banner — sandbox status still visible in `/status` and when a command is blocked
* Removed the "/ide for …" startup hint toast
* Improved performance of long and resumed conversations by eliminating redundant message-rendering recomputations

#### Major bug fixes

* Fixed unprocessable images (zero-byte, corrupt) attached via paste, MCP, or dialog crashing the request instead of becoming a text placeholder
* Fixed sandbox network permission prompts appearing in auto and bypass-permissions mode when using the desktop app, IDE extensions, or SDK
* Fixed `claude agents` completed sessions not retiring when an idle subagent was still parked or had leaked a backgrounded shell
* Fixed `claude agents` pressing Esc not cancelling a slow "opening…", leaving the list unresponsive
* Fixed background agent worktrees under `.claude/worktrees/` being orphaned after the 30-day job retention sweep
* Fixed background sessions re-attached after a sleep/wake not telling the model the correct date
* Fixed copy-on-select in `claude agents` not reaching the system clipboard inside tmux with `set-clipboard on` (regression in 2.1.153)
* Fixed `--resume` not reporting background subagents that were running when the previous Claude Code process exited
* Fixed `--worktree` returning to the canonical repo root instead of the current linked worktree
* Fixed the `/model` picker showing an incorrect "Newer version available" hint when the selected model is already the newest in its family
* Fixed literal markdown markers (backticks, asterisks) appearing in in-progress message text in fullscreen mode
* Fixed the terminal freezing after approving the managed-settings security dialog at startup
* Fixed right-click paste duplicating the clipboard in VS Code, Cursor, and Windsurf integrated terminals
* WSL: fixed image paste (`alt+v` keybinding), screenshot paste on Windows 11, and added support for dragging images from Windows Explorer
* [IDE] Fixed clicking Stop while a background subagent is running not actually stopping it
* [VSCode] Fixed the fast mode indicator not appearing on Opus 4.8

### [2.1.158](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/versions/2.1.158.md)

#### New features

* Auto mode is now available on Bedrock, Vertex, and Foundry for Opus 4.7 and Opus 4.8 — opt in by setting `CLAUDE_CODE_ENABLE_AUTO_MODE=1`

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/hosting](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-sdk/hosting.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hosting)]

* Major rewrite: page expanded from a brief FAQ into a comprehensive self-hosting guide. New sections cover the subprocess model, session patterns (ephemeral, long-running, hybrid, multi-agent container), container provisioning, and production concerns (persistence, observability, auth/secrets, scaling, cost, multi-tenant isolation). [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-sdk/hosting.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/agent-sdk/hosting)]
* Multi-tenant isolation options documented: `settingSources: []`, `CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`, per-tenant `CLAUDE_CONFIG_DIR`, and per-tenant `cwd`
* Known limitations table added: no session timeout, memory growth, rate limit fanouts, no per-subagent wall-clock deadline

#### [agent-sdk/overview](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* Python SDK now requires Python 3.10+; troubleshooting tip added for `No matching distribution found` pip error

#### [agent-sdk/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-sdk/quickstart.md) [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

* Windows-specific installation instructions added: `py -m venv .venv`, `.venv\Scripts\Activate.ps1`, and a note on PowerShell execution policy

#### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* New section "Scale up with dynamic workflows" recommends the `Workflow` tool for dozens-to-hundreds of agents; notes availability in TypeScript Agent SDK v0.3.149+

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `Workflow` tool input schema documented: `script`, `name`, `scriptPath`, `args`, `resumeFromRunId` fields
* New `WorkflowOutput` schema documented: `status`, `taskId`, `runId`, `summary`, `transcriptDir`, `scriptPath`, `error` fields
* `AskUserQuestionOutput`: new `response` field for freeform user replies that bypass structured questions
* `applyFlagSettings()` documentation clarifies which settings take effect mid-session vs. require a new session

#### [agent-sdk/user-input](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-sdk/user-input.md) [[Source](https://code.claude.com/docs/en/agent-sdk/user-input)]

* `AskUserQuestionOutput.response`: new optional field documented; when set, Claude receives "The user responded: …" instead of per-question answers

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* `claude agents` now accepts `--agent` flag to set the default subagent for dispatched sessions. [[line 344](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-view.md?plain=1#L344)] [[Source](https://code.claude.com/docs/en/agent-view#permission-mode-model-and-effort)]
* Version compatibility table expanded: `--agent` and honoring the `agent` setting requires v2.1.157+. [[line 358](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/agent-view.md?plain=1#L358)] [[Source](https://code.claude.com/docs/en/agent-view#permission-mode-model-and-effort)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `claude agents` now accepts `--agent` flag to set the default subagent for dispatched sessions

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Clarified multi-agent limitation: parallel session orchestration is CLI-only, but dynamic workflows (available in Desktop) support multi-agent work within one session

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_DISABLE_TERMINAL_TITLE`: also skips the background Haiku request that generates the session title in Agent SDK and `claude -p` sessions
* `CLAUDE_EFFORT`: "ultra" removed as a distinct level; ultracode reports as `xhigh`

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New fix documented for "thinking blocks cannot be modified" error: run `claude update` first if using Opus 4.7 or Opus 4.8 — versions before v2.1.156 can trigger this error during normal tool use

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `effort.level` field: "ultra" removed as a distinct level; ultracode reports as `"xhigh"` instead

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Image paste shortcut updated: `Alt+V` now applies to both Windows and WSL; both `Ctrl+V` and `Alt+V` are bound by default on WSL

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* `chat:imagePaste` binding updated: `Alt+V` now applies to Windows and WSL

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Option 4: Add a remote WebSocket server" — `type: "ws"` entries with `url`, `headers`, `headersHelper`, `timeout`, `alwaysLoad` fields; authentication is header-only; `claude mcp add --transport` does not accept `ws`. [[line 114](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/mcp.md?plain=1#L114)] [[Source](https://code.claude.com/docs/en/mcp#option-4-add-a-remote-websocket-server)]
* Plugin MCP transport support updated: WebSocket added alongside stdio, SSE, and HTTP
* New behavior: if `headers.Authorization` is configured and the server rejects it, Claude reports connection failure instead of falling back to OAuth

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* `autoMemoryDirectory`: now accepted from any settings scope (user, project, local, policy, `--settings`); when set in project/local settings, requires workspace trust dialog acceptance

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `tool_parameters` attribute added to `tool_decision` (permission decision) event when `OTEL_LOG_TOOL_DETAILS=1`; documents shape per tool type including new `WorkspaceBash`. [[line 533](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/monitoring-usage.md?plain=1#L533)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* MCP monitoring: `tool_decision` now includes `mcp_server_name` and `mcp_tool_name` in `tool_parameters`. [[line 969](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/monitoring-usage.md?plain=1#L969)] [[Source](https://code.claude.com/docs/en/monitoring-usage#audit-mcp-activity)]
* Security use-case table updated: "rejected commands" now queries `tool_decision` event

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* `.cargo` added to the list of protected directories in default permission mode

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `bypassPermissions` mode now also skips prompts for writes to `.cargo` (added alongside `.git`, `.vscode`, `.idea`, `.husky`). [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/permissions.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Clarified that each user can register only one marketplace per name; adding a second with the same name replaces the first

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* New section "Develop a plugin in your skills directory" — documents `claude plugin init` scaffolding a plugin in `~/.claude/skills/<name>/` that auto-loads as `<name>@skills-dir` without a marketplace install step

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New major section "Skills-directory plugins" — documents auto-loading from skills directories, scope/trust rules, project-scope restrictions, and `/reload-plugins`. [[line 330](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/plugins-reference.md?plain=1#L330)] [[Source](https://code.claude.com/docs/en/plugins-reference#skills-directory-plugins)]
* New CLI command `plugin init` documented with full options table (`--description`, `--author`, `--author-email`, `--with`, `--force`) and examples. [[line 763](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/plugins-reference.md?plain=1#L763)] [[Source](https://code.claude.com/docs/en/plugins-reference#plugin-init)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `agent` setting now also sets the default agent for sessions dispatched from `claude agents`
* `autoMemoryDirectory`: now accepted from any settings scope; requires workspace trust dialog when set in project/local settings
* New `workflowKeywordTriggerEnabled` setting: controls whether typing "workflow" in a prompt triggers a dynamic workflow (default `true`). [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/settings.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New note: adding `.claude-plugin/plugin.json` to a skill folder loads it as a plugin named `<name>@skills-dir`
* Live change detection clarification: covers `SKILL.md` text only; hooks/MCP/agents/output-styles inside a plugin require `/reload-plugins`
* `${CLAUDE_EFFORT}` substitution: "ultra" removed as a distinct value; ultracode reports as `xhigh`

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* `effort.level` field: "ultra" removed; ultracode reports as `xhigh`

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `bypassPermissions` mode: `.cargo` added to the list of directories where prompts are skipped

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* `/terminal-setup` behavior change in VS Code, Cursor, and Windsurf: now also sets `terminal.integrated.gpuAcceleration` to `"off"` to prevent garbled text; documented how to undo this change

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* `EnterWorktree`: from within a worktree or a subagent with pinned working directory, only the `path` form is available and the target must be under `.claude/worktrees/`
* New `Workflow` tool documented: runs a dynamic workflow script that orchestrates many subagents in the background; requires permission approval. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/tools-reference.md?plain=1#L53)] [[Source](https://code.claude.com/docs/en/tools-reference)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* New way to cancel a workflow keyword trigger: press Backspace while the cursor is immediately after the highlighted word (in addition to `alt+w`)
* Documented `workflowKeywordTriggerEnabled` setting in `/config` to permanently disable the keyword trigger

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* `EnterWorktree`: from within a worktree, Claude can now switch directly to another worktree under `.claude/worktrees/` by calling `EnterWorktree` with the target path. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/claude-code/worktrees.md?plain=1#L33)] [[Source](https://code.claude.com/docs/en/worktrees#start-claude-in-a-worktree)]
* Cleanup behavior clarified: automatic cleanup sweep covers both subagent and background-session worktrees

-----

## API changes

### Changed documents

#### [agents-and-tools/mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* New section "When Claude uses MCP tools" — explains trigger conditions (explicit/implicit requests vs. general knowledge) and guidance on steering tool-use frequency via system prompt
* Denylist section: added recommendation to denylist write/destructive tools for read-only assistants or human-confirmation workflows
* Multi-server section: new note that clear, specific tool descriptions improve selection accuracy; recommendation to use `defer_loading` with Tool Search for large tool sets

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Cross-reference added linking to the new "When Claude uses MCP tools" section in mcp-connector.md

#### [agents-and-tools/tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* New tip #7: when using `computer_20251124` with `enable_zoom: true`, Claude zooms in on small text or specific UI elements; guidance on how to trigger zoom behavior

#### [agents-and-tools/tool-use/overview](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* New section "When Claude uses tools" — explains the default `auto` tool_choice behavior, when Claude calls tools vs. responds directly, and how to steer behavior via system prompt or `tool_choice`

#### [agents-and-tools/tool-use/web-fetch-tool](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* New section "When Claude fetches" — documents when Claude triggers a fetch (specific URL or named resource) vs. responds directly (general knowledge)
* New combined search+fetch note: when both tools are enabled, Claude uses search to find a URL for a named resource, then fetches it

#### [build-with-claude/adaptive-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* `high` effort level description changed from "always thinks" to "almost always thinks"
* New guidance on system prompt phrases to encourage thinking (e.g., "Think carefully before responding")
* New per-message thinking steering from the user turn: appending "Please think hard before responding." encourages thinking; "Answer directly without deliberating." suppresses it. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L163)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [build-with-claude/context-windows](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* New note: Claude's tool selection is designed to work with 100K+ token contexts; references tool context management and Tool Search for large tool sets

#### [managed-agents/agent-setup](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* New behavior note: updating an agent does not automatically update coordinator rosters that reference it — coordinators keep the version pinned at their last create/update; must update the coordinator explicitly to delegate to a newer version

#### [managed-agents/memory](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/managed-agents/memory.md) [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]

* Memory store cap documented: a store holds a maximum of 2,000 memories; writes to new memories fail when the limit is reached (existing memories remain readable/editable). [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/managed-agents/memory.md?plain=1#L46)] [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]
* "Limits" section replaced with "Best practices for memory management": guidance on focused stores, condensing/pruning before hitting the limit, attaching a new store, and limiting write access

#### [managed-agents/multi-agent](https://github.com/gpambrozio/ClaudeDocs/blob/faf9833043db19e98e3d355d823a5f889830ad7d/docs-md/api/managed-agents/multi-agent.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multi-agent)]

* Version pinning clarified: `{"type": "agent", "id": ...}` without a version pins to the latest version at coordinator creation time, not the agent's future latest version
* New explicit note: coordinator configuration (including `multiagent.agents` roster) is snapshotted at create/update time and does not automatically pick up later agent updates
