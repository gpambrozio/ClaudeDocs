# [Claude docs changes for May 15th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/50b56e94b7ff731c63b9c2ab7aec019b0c16f541) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/50b56e94b7ff731c63b9c2ab7aec019b0c16f541)]

## Executive Summary
- New `terminalSequence` hook output field lets hooks safely emit desktop notifications, window titles, and bells without `/dev/tty` access — works on all platforms including Windows and inside tmux/screen
- Task tool types (`TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate`) are now fully exported from the TypeScript SDK, eliminating the need to define them locally
- New "Summarize up to here" rewind option lets you compress early conversation context while keeping recent messages fully intact
- Fast mode now defaults to Opus 4.7 (was Opus 4.6); pin to Opus 4.6 with `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`
- `claude agents` gains a `--cwd <path>` flag to scope the session list to a single project, and `--name` for naming background sessions at dispatch time

## New Claude Code versions

### [2.1.142](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/versions/2.1.142.md)

#### New features

* Added new `claude agents` flags: `--add-dir`, `--settings`, `--mcp-config`, `--plugin-dir`, `--permission-mode`, `--model`, `--effort`, and `--dangerously-skip-permissions` to configure dispatched background sessions
* Fast mode now uses Opus 4.7 by default (previously Opus 4.6); set `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1` to pin fast mode to Opus 4.6
* Plugins with a root-level `SKILL.md` and no `skills/` subdirectory are now surfaced as a skill
* The `/plugin` details pane and `claude plugin details` now show LSP servers a plugin provides
* `/web-setup` warns before replacing an existing GitHub App connection

#### Existing feature improvements

* Improved reactive compaction: the first summarize attempt now seeds from the original request's overflow size, avoiding a wasted near-full-context retry
* Improved hook configuration error: configuring a prompt- or agent-type hook for `SessionStart`/`Setup`/`SubagentStart` now shows a clear "use a command-type hook instead" error
* Removed stale `/model claude-sonnet-4-20250514` suggestion from Usage Policy refusal messages

#### Major bug fixes

* Fixed `MCP_TOOL_TIMEOUT` not raising the per-request fetch timeout for remote HTTP and SSE MCP servers, which capped tool calls at 60 seconds regardless of the configured value
* Fixed background sessions not recognizing pre-existing git worktrees, blocking Edit while EnterWorktree refused to create a duplicate
* Fixed background sessions disappearing and daemon reconnect failing after macOS sleep/wake — the daemon now detects clock jumps instead of treating them as elapsed idle time
* Fixed daemon not exiting cleanly after binary upgrade (e.g. `brew upgrade`), causing dispatched agents to crash-loop on the deleted path
* Fixed background agents crash-looping when the Claude-in-Chrome extension is connected without a shared tab
* Fixed `claude agents` "v to open in editor" using the daemon's default editor instead of `$EDITOR`/`$VISUAL`
* Fixed `claude agents` deadlocking on Windows with network-drive working directories; Ctrl+C now works during startup
* Fixed `claude --bg --dangerously-skip-permissions` not persisting across retire/wake
* Fixed session titles being derived from the URL when the first message is a link
* Fixed plugins using `skills: ["./"]` showing a false "path escapes plugin directory" error
* Fixed plugin cache cleanup deleting the active plugin version directory when no installation metadata is present

-----

## Claude Code changes

### New Documents

#### [Desktop changelog](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

New file tracking Claude Code Desktop app-specific changes (separate from the CLI changelog). Covers versions 1.5186.0 through 1.7196.0 (April 28 – May 12, 2026). Notable entries include: multi-tab terminal pane, OS notifications when a Code session finishes, `list_sessions`/`search_session_transcripts`/`archive_session` MCP tools, `update_scheduled_task` MCP tool for self-rescheduling tasks, per-plugin auto-install for org-provisioned plugins, and an organization banner for 3P managed deployments.

### Changed documents

#### [Agent SDK - Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Clarified that `systemMessage` shows a message **to the user**, not to the model; to pass context to the model, use `additionalContext` instead. [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#outputs)]
* Updated the "block a tool" example to use `permissionDecisionReason` (tells the model why) alongside `systemMessage` (tells the user). [[lines 248-264](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L248-L264)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#add-context-and-block-a-tool)]
* Fixed troubleshooting section: `systemMessage` is not visible by default; set `includeHookEvents` (`include_hook_events` in Python) to surface it in the stream. [[line 545](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L545)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#recursive-hook-loops-with-subagents)]

#### [Agent SDK - Python](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Updated `systemMessage` description in `HookJSONOutput` from "system message to add to the transcript" to "warning message shown to the user". [[line 1827](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/python.md?plain=1#L1827)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#hookcallback)]

#### [Agent SDK - TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `includeHookEvents` option to `query()` config — when `true`, includes hook lifecycle events (`SDKHookStartedMessage`, `SDKHookProgressMessage`, `SDKHookResponseMessage`) in the message stream. [[line 386](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L386)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]
* `TaskCreate`, `TaskGet`, `TaskList`, and `TaskUpdate` input/output types are now exported from the SDK — the "not yet exported from the SDK; define locally" comments have been removed. [[lines 1582-1395](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1582)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#toolinputschemas)]

#### [Agent view](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Added `--cwd <path>` flag to `claude agents` to scope the view to sessions started under a specific directory. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-view.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/agent-view#monitor-sessions-with-agent-view)]
* Added `--name` flag for `claude --bg` to set the session's display name in agent view instead of the auto-generated one. [[lines 248-252](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-view.md?plain=1#L248-L252)] [[Source](https://code.claude.com/docs/en/agent-view#from-your-shell)]
* Clarified permission mode inheritance: backgrounding an existing session preserves its current mode; dispatching from agent view uses `defaultMode` from settings. [[lines 282-295](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-view.md?plain=1#L282-L295)] [[Source](https://code.claude.com/docs/en/agent-view#permission-mode-model-and-effort)]
* Added note that `--permission-mode`, `--model`, and `--effort` on `claude agents` require v2.1.142 or later. [[line 293](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/agent-view.md?plain=1#L293)] [[Source](https://code.claude.com/docs/en/agent-view#permission-mode-model-and-effort)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Clarified distinct trigger conditions: `awsAuthRefresh` only runs when credentials are expired; `awsCredentialExport` runs at session start and on every credential reload, even when credentials are still valid — use it for cross-account Bedrock credentials. [[lines 106-109](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/amazon-bedrock.md?plain=1#L106-L109)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#advanced-credential-configuration)]

#### [Best practices](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added mention of the new "Summarize up to here" rewind option alongside "Summarize from here", with a link to the checkpointing docs. [[line 367](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/best-practices.md?plain=1#L367)] [[Source](https://code.claude.com/docs/en/best-practices#manage-context-aggressively)]
* Clarified checkpoint semantics: a checkpoint is created per prompt sent, and Claude snapshots files before each edit. [[lines 391-394](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/best-practices.md?plain=1#L391-L394)] [[Source](https://code.claude.com/docs/en/best-practices#rewind-with-checkpoints)]

#### [Checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* Added new **"Summarize up to here"** rewind option: compresses messages before the selected point while keeping later messages intact, leaving you at the end of the conversation. [[lines 31-40](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/checkpointing.md?plain=1#L31-L40)] [[Source](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)]
* Expanded "Restore vs. summarize" section to document both summarize modes side-by-side with use case guidance. [[lines 44-50](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/checkpointing.md?plain=1#L44-L50)] [[Source](https://code.claude.com/docs/en/checkpointing#restore-vs-summarize)]

#### [CLI reference](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated `claude agents` description to document the new `--cwd <path>` flag. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/cli-reference.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Updated `/rewind` description to mention that it can also summarize part of the conversation, not only restore it. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/commands.md?plain=1#L21)] [[Source](https://code.claude.com/docs/en/commands#commands-across-a-typical-workflow)]

#### [Desktop scheduled tasks](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* Delete dialog now includes an **"Also delete files on disk"** checkbox that removes the task's `SKILL.md` file and data from `~/.claude/scheduled-tasks/`. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)]
* A scheduled task can now modify its own schedule or prompt during a run using the `update_scheduled_task` MCP tool. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L86)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Documented multi-tab terminal pane: click **+** in the terminal header or right-click a folder to open a second tab. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/desktop.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/desktop#run-commands-in-the-terminal)]
* Added that the Desktop app sends an OS notification when a Code session finishes and you aren't viewing it. [[line 268](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/desktop.md?plain=1#L268)] [[Source](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions)]
* Added `managedMcpServers` to the managed settings table: allows pushing MCP server configs to all users in 3P Desktop deployments, with per-tool policy restrictions. [[line 549](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/desktop.md?plain=1#L549)] [[Source](https://code.claude.com/docs/en/desktop#managed-settings)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `ANTHROPIC_WORKSPACE_ID`: workspace ID for workload identity federation when a rule is scoped to more than one workspace. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/env-vars.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Added `CLAUDE_CODE_PLUGIN_PREFER_HTTPS`: set to `1` to clone GitHub plugins over HTTPS instead of SSH — useful in CI/containers without SSH keys. [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/env-vars.md?plain=1#L141)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Updated `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT` to apply to any model (not only Opus 4.7) and document the opt-out values (`0`, `false`, `no`, `off`). [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/env-vars.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Added `DEBUG` env var: set to `1` to enable debug mode (equivalent to `--debug`); namespace patterns like `DEBUG=express:*` do not trigger it. [[line 187](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/env-vars.md?plain=1#L187)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Added `plugin_marketplaces` and `plugins` action inputs for installing plugins before execution. [[lines 593-594](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/github-actions.md?plain=1#L593-L594)] [[Source](https://code.claude.com/docs/en/github-actions#action-parameters)]
* Added documentation and example for invoking skills via the `prompt` input, including both repo skills and plugin-namespaced skills. [[lines 143-168](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/github-actions.md?plain=1#L143-L168)] [[Source](https://code.claude.com/docs/en/github-actions#using-skills)]

#### [Glossary](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* Updated "Checkpoint" definition: checkpoints are created per prompt sent (not per edit), and now also cover the summarize-from-checkpoint capability. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/glossary.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/glossary#checkpoint)]

#### [Goal](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/goal.md) [[Source](https://code.claude.com/docs/en/goal)]

* Added version requirement: `/goal` requires Claude Code v2.1.139 or later. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/goal.md?plain=1#L8)] [[Source](https://code.claude.com/docs/en/goal)]
* Added Desktop app to the list of supported non-interactive environments for `/goal`. [[line 104](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/goal.md?plain=1#L104)] [[Source](https://code.claude.com/docs/en/goal#run-non-interactively)]

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Updated hook timeout documentation with per-type defaults: `command`/`http`/`mcp_tool` default to 10 minutes (30 seconds for `UserPromptSubmit`); `prompt` defaults to 30 seconds; `agent` defaults to 60 seconds. [[lines 821-824](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/hooks-guide.md?plain=1#L821-L824)] [[Source](https://code.claude.com/docs/en/hooks-guide#limitations)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added new `terminalSequence` JSON output field: hooks can now return terminal escape sequences (OSC notifications, window titles, BEL) for Claude Code to emit on their behalf — replaces writing directly to `/dev/tty`, which is unavailable to hooks as of v2.1.139. Restricted to an allowlist of safe sequences that cannot move the cursor or alter colors. [[lines 659-700](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/hooks.md?plain=1#L659-L700)] [[Source](https://code.claude.com/docs/en/hooks#json-output)]
* Documented that command hooks on macOS and Linux now run without a controlling terminal (as of v2.1.139). [[line 528](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/hooks.md?plain=1#L528)] [[Source](https://code.claude.com/docs/en/hooks#hook-input-and-output)]
* `UserPromptSubmit` hooks have a 30-second default timeout for `command`/`http`/`mcp_tool` types (shorter than the 600-second default for other events). [[line 964](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/hooks.md?plain=1#L964)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit)]
* Documented `PostToolUse` response fields for completed Agent calls: `status`, `agentId`, `content`, `totalTokens`, `totalDurationMs`, `totalToolUseCount`, and `usage` — enabling per-subagent cost tracking from a hook. [[lines 1162-1177](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/hooks.md?plain=1#L1162-L1177)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-input)]
* Clarified that in async hooks, `systemMessage` is shown to the user (not Claude); use `additionalContext` to pass context to the model. Updated the async example accordingly. [[lines 2535-2570](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/hooks.md?plain=1#L2535-L2570)] [[Source](https://code.claude.com/docs/en/hooks#how-async-hooks-execute)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* MCP OAuth authentication now triggers on both `401 Unauthorized` and `403 Forbidden` responses (previously only `401`). [[line 420](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/mcp.md?plain=1#L420)] [[Source](https://code.claude.com/docs/en/mcp#authenticate-with-remote-mcp-servers)]

#### [Remote control](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added Desktop app Settings toggle for enabling remote control by default: **Settings → Claude Code → Enable remote control by default**. [[line 115](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/remote-control.md?plain=1#L115)] [[Source](https://code.claude.com/docs/en/remote-control#enable-remote-control-for-all-sessions)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Improved `/status` description: the Status tab now shows a `Setting sources` line listing each loaded layer; a layer only appears when it has at least one key; the Config tab is a toggle editor, not a view of `settings.json`. [[line 511](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/settings.md?plain=1#L511)] [[Source](https://code.claude.com/docs/en/settings#verify-active-settings)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `.claude/agents/` and `~/.claude/agents/` are now scanned recursively, allowing subfolders like `agents/review/`; identity still comes from the `name` frontmatter field only. [[lines 177-179](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/sub-agents.md?plain=1#L177-L179)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]
* Plugin `agents/` directories are also scanned recursively; a subfolder inside a plugin's `agents/` directory becomes part of the scoped identifier (e.g. `my-plugin:review:security`). [[line 180](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/sub-agents.md?plain=1#L180)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]
* Updated `@`-mention typeahead and `--agent` flag documentation to reflect the new subfolder-based scoped identifiers for plugin agents. [[lines 612-624](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/sub-agents.md?plain=1#L612-L624)] [[Source](https://code.claude.com/docs/en/sub-agents#invoke-subagents-explicitly)]

#### [Voice dictation](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/voice-dictation.md) [[Source](https://code.claude.com/docs/en/voice-dictation)]

* Clarified WSLg availability: WSLg is included with WSL2 when installed from the Microsoft Store on Windows 10 or 11 (not only Windows 11). [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/voice-dictation.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/voice-dictation#requirements)]
* Added troubleshooting entry for `Voice mode could not find a working audio recorder in WSL`: WSLg routes through PulseAudio, so you need `sudo apt install sox libsox-fmt-pulse` rather than just `sox`. [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/50b56e94b7ff731c63b9c2ab7aec019b0c16f541/docs-md/claude-code/voice-dictation.md?plain=1#L144)] [[Source](https://code.claude.com/docs/en/voice-dictation#troubleshooting)]

-----

## API changes

### Changed documents

No significant documentation changes today (only internal email obfuscation URL updates).
