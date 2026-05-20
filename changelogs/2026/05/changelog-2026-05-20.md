# [Claude docs changes for May 20th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5e2bafa17c80342ea4215ff487cfe1f272f11db6) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5e2bafa17c80342ea4215ff487cfe1f272f11db6)]

## Executive Summary
- New comprehensive `prompt-caching.md` guide for Claude Code explains how caching works, what actions invalidate the cache, and how to monitor and optimize cache performance
- Major Compliance API expansion: `ActivityListResponse` now documents 300+ activity types; 8 new download/metadata endpoints added for artifacts, generated files, chat messages, and project attachments
- `/model` command now applies to the current session only (v2.1.144 behavior change); press `d` in the model picker to save a default for new sessions
- New `/run`, `/verify`, and `/run-skill-generator` skills in Claude Code (v2.1.145) enable building and confirming changes work in the actual running app
- Stop and SubagentStop hooks now receive `background_tasks` and `session_crons` fields, and `claude agents --json` enables scripting over live sessions

## New Claude Code versions

### [2.1.145](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/versions/2.1.145.md)

#### New features

* Added `claude agents --json` to list live Claude sessions as JSON for scripting (tmux-resurrect, status bars, session pickers)
* Added `agent_id` and `parent_agent_id` attributes to `claude_code.tool` OTEL spans, and fixed trace parenting so background subagent spans nest under the dispatching Agent tool span
* Status line JSON input now includes GitHub repo and PR information when detected
* `/plugin` Discover and Browse screens now show a plugin's commands, agents, skills, hooks, and MCP/LSP servers before installation
* `claude agents` terminal tab title now shows the awaiting-input count so an alt-tabbed window tells you when an agent needs attention
* Slash command and @-mention suggestion list now supports mouse hover and click in fullscreen mode
* Stop and SubagentStop hook input now includes `background_tasks` and `session_crons` fields

#### Existing feature improvements

* Improved the Read tool to return a truncated first page with a "PARTIAL view" notice instead of a hard error when a whole-file read exceeds the token limit

#### Major bug fixes

* Fixed a permission-prompt bypass where bare variable assignments to non-allowlisted environment variables in Bash commands were auto-approved
* Fixed MCP prompt slash commands showing raw server validation errors when a required argument is omitted — the error now names the missing argument and shows expected usage
* Fixed Agent Teams teammates with non-ASCII names failing every API call due to invalid header encoding
* Fixed an infinite loop where a skill using `context: fork` could repeatedly re-invoke itself instead of running
* Fixed task lists rendering in random order when several tasks are created at once
* Fixed the PR badge in the footer not updating immediately after `gh pr create` and other PR-state-changing commands run in-session
* Fixed `/review` using a deprecated `projectCards` GraphQL query that errored on repos with Classic Projects
* Fixed `claude plugin validate` not flagging `skills:` entries that point at a file instead of a directory
* Fixed voice push-to-talk not working in the agent view's reply pane

-----

## Claude Code changes

### New Documents

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

New comprehensive guide explaining how Claude Code uses prompt caching. Covers how the cache is organized (system prompt, project context, conversation layers), which actions invalidate the cache (model switches, MCP connects/disconnects, bare tool deny rules, compaction, upgrades), which actions preserve it (file edits, CLAUDE.md edits mid-session, output style changes, permission mode changes, skills/commands, `/rewind`), cache lifetime and TTL options (5-minute vs 1-hour), per-authentication-method behavior, how to check cache performance via statusline, subagent caching behavior, and how to disable caching per-model with environment variables.

#### [whats-new/2026-w20](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/whats-new/2026-w20.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w20)]

What's new for week 20 (May 11–15, 2026), covering releases v2.1.139–v2.1.142. Highlights: `claude agents` view (one screen for all running sessions, dispatch/attach/background), `/goal` command (Claude keeps working toward a verifiable condition across turns), fast mode on Opus 4.7 by default, and other improvements including new hook fields, `continueOnBlock` for PostToolUse hooks, and `terminalSequence` hook output field.

### Changed documents

#### [agent-sdk/custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* Clarified that bare tool names in `disallowedTools` (e.g., `"Bash"`) remove the tool from Claude's context entirely, while scoped rules (e.g., `"Bash(rm *)"`) leave the tool available and only deny matching calls

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Corrected TypeScript SDK guidance: `outputStyle` is not a top-level `Options` field; it must be set inside the inline `settings` object passed to `query()` or in a settings file

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Updated evaluation flow: bare tool name deny rules (e.g., `Bash`) remove the tool from Claude's context before evaluation; only scoped rules (e.g., `Bash(rm *)`) reach the deny-rule check step
* Expanded allow/deny rule table to distinguish bare-name entries (tool definition removed from request) from scoped rules (tool stays available, matching calls denied)

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Updated `disallowed_tools` option description to distinguish bare names (remove tool from context) from scoped rules (deny matching calls in every permission mode including `bypassPermissions`)

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New section "Compile to a single executable" documents a `bun build --compile` workaround using `extractFromBunfs()` (requires SDK v0.3.144+) to extract the bundled CLI binary at startup and pass it via `pathToClaudeCodeExecutable`
* New `Options` fields added: `agentProgressSummaries`, `forwardSubagentText`, `loadTimeoutMs`, `managedSettings`, `onElicitation`, `planModeInstructions`, `sessionStoreFlush`, `taskBudget`, `title`, `toolAliases`
* `outputStyle` corrected: no longer an `Options` field; must be set in the inline `settings` object or a settings file
* New `SDKMessage` union types: `SDKSessionStateChangedMessage`, `SDKNotificationMessage`, `SDKMemoryRecallMessage`, `SDKElicitationCompleteMessage`, `SDKAPIRetryMessage`, `SDKMirrorErrorMessage`
* New `SDKResultMessage` fields: `api_error_status`, `ttft_ms`, `terminal_reason` (12-value enum: `"completed"`, `"max_turns"`, etc.), `fast_mode_state`
* `StopHookInput` and `SubagentStopHookInput` updated with new `background_tasks` and `session_crons` fields
* `Usage` type updated: `input_tokens` and `output_tokens` now non-nullable; new fields `cache_creation`, `server_tool_use`, `service_tier`, `speed`, `inference_geo`, `iterations`
* `parent_tool_use_id` changed from `null` (reserved) to `string | null`, now the `tool_use_id` of the spawning `Agent` tool call

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* New `claude agents --json` command documented — prints live sessions as a JSON array for scripting and exits
* `claude rm` behavior clarified: removing a session from agent view leaves the conversation transcript on disk and available via `claude --resume`
* `/add-dir` directories now carry through when backgrounding a session
* `claude agents` terminal tab title now shows awaiting-input count
* Worktree skip condition updated: "not a git repo" now also applies when no `WorktreeCreate` hook is configured; suggests configuring one for non-git VCS

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Prompt caching note updated: added pointer to Bedrock docs for supported models, regions, and limits when cache token counts stay at zero

#### [channels-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/channels-reference.md) [[Source](https://code.claude.com/docs/en/channels-reference)]

* Clarified that in-app submission forms add plugins to the community marketplace (`anthropics/claude-plugins-community`), not the official marketplace (`claude-plugins-official`); official marketplace is curated by Anthropic at its discretion via partner contact

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `claude agents --json` flag documented: prints live sessions as a JSON array and exits (does not require an interactive terminal)
* `--disallowedTools` description updated to distinguish bare names (remove from context) from scoped rules
* `claude rm` updated: transcript stays on local machine, available via `claude --resume`
* `--resume` updated: background sessions appear in the picker marked with `bg` (as of v2.1.144)

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New commands added: `/run` (launch and drive the project app to see a change working, v2.1.145+), `/verify` (confirm a code change works by building and running the app, v2.1.145+), and `/run-skill-generator` (teach `/run` and `/verify` how to build/launch/drive the app)
* `/model` updated: pressing `d` on a row saves that model as the default for new sessions
* `/resume` updated: background sessions appear in the picker marked with `bg` (v2.1.144+)
* `/feedback` updated: added `/share` as an alias

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* New "Community marketplace" section documents `anthropics/claude-plugins-community` — how to add it (`/plugin marketplace add anthropics/claude-plugins-community`), automated safety screening, commit SHA pinning, and how to install from it
* Plugin details pane now shows "Last updated" date (v2.1.144+) and a "Will install" section listing commands, agents, skills, hooks, and MCP/LSP servers before install (v2.1.145+)
* Official marketplace description corrected: submission forms go to community marketplace, not the official one

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New "Set environment variables" section with platform-specific tabs (macOS/Linux/WSL, Windows PowerShell, Windows CMD) and shell profile persistence instructions
* New "In settings files" subsection explains the `env` key in `settings.json` with a scope table (user-global, project, project-local, managed)
* New "Precedence" section: env vars take precedence over settings fields; explains interaction with CLI flags and in-session commands
* `CLAUDECODE` now set in ALL subprocesses including hooks and status-line commands
* New variable `CLAUDE_CODE_ALT_SCREEN_FULL_REPAINT` documented
* `DISABLE_TELEMETRY` updated: now also disables feature-flag fetching (same effect as `DISABLE_GROWTHBOOK`)
* `ENABLE_PROMPT_CACHING_1H` description updated: "Subscription users within included usage" replaces "Subscription users"

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* "Code intelligence" added as a new extension type: connects Claude to a language server for symbol-level navigation and live type errors; loading strategy is "After file edits and on demand"; suited for typed languages and large codebases where grep is slow

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Added: clicking a suggestion in the `/` command or `@` file list now accepts it; hovering highlights the row

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New `model_not_found` error category added to the `system/api_retry` event table

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added `model_not_found` to the `StopFailure` matcher error type list

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `Stop` hook input now includes `background_tasks` and `session_crons` fields (v2.1.145+): full documentation with field-by-field tables and example JSON showing an in-flight shell task and a recurring cron
* `SubagentStop` hook now also receives `background_tasks` and `session_crons` arrays (v2.1.145+), scoped to the parent session
* `StopFailure` error field updated to include `model_not_found`

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* PR badge: removed "Purple: merged" status — badge now disappears once a PR merges or closes
* PR badge now refreshes immediately after `gh pr` or `git push` commands run in-session (previously only every 60 seconds)

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New `ModelPicker` action: `modelPicker:setAsDefault` (key `d`) — sets the highlighted model as default for new sessions

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Clarified that Claude.ai connectors are only fetched when authenticated via a Claude.ai subscription; not loaded when `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `apiKeyHelper`, or a third-party provider is active

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Major behavior change (v2.1.144): `/model` now applies to the current session only and is no longer written to settings; press `d` in the picker to save a model as default for new sessions
* Resumed sessions (`--resume`, `--continue`, `/resume`) now keep the model from the transcript, preventing another session's `/model` choice from affecting it; if that model is retired, falls through to normal precedence

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* When connected to the Anthropic API directly, model requests now carry a W3C `traceparent` header tied to the `claude_code.llm_request` span; the API's `traceresponse` header is recorded as a span link (not sent to third-party providers)
* New span attributes `agent_id` and `parent_agent_id` added to tool span fields
* New event type `claude_code.hook_plugin_metrics` documented: logged when an official-marketplace plugin hook emits per-invocation metrics; includes `plugin_id`, `hook_event`, and up to 20 plugin-emitted metric keys

#### [output-styles](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Proactive style description updated: it now provides "stronger autonomous-execution guidance than auto mode applies" rather than "the same guidance as auto mode"
* Cache/timing clarification: output style changes take effect after `/clear` or a new session (not just a new session), with a link to the prompt caching doc

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Auto mode description revised: "nudges Claude to keep working without stopping for clarifying questions"; Proactive output style provides "stronger autonomous behavior"

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* New paragraph: bare tool name deny rules (e.g., `Bash` or `Bash(*)`) remove the tool from Claude's context entirely; scoped rules (e.g., `Bash(rm *)`) leave the tool available and block only matching calls

#### [plugin-hints](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/plugin-hints.md) [[Source](https://code.claude.com/docs/en/plugin-hints)]

* Clarified that `CLAUDECODE=1` is set in hook commands, but the hint tag is stripped/ignored in hooks — only Bash and PowerShell tool output triggers the install prompt
* Official marketplace section rewritten: the hint protocol applies only to `claude-plugins-official` (Anthropic-curated); submission forms go to the community marketplace, not the official one

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New "Unrecognized fields" section: Claude Code ignores unrecognized top-level `plugin.json` fields (useful for multi-ecosystem manifests); `claude plugin validate` reports them as warnings; pass `--strict` to treat warnings as errors

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* "Submit to official marketplace" renamed to "Submit to community marketplace"
* Anthropic now has two public marketplaces: `claude-plugins-official` (always included, Anthropic-curated) and `claude-community` (community submissions, user-added)
* Approved community plugins are pinned to a commit SHA in `anthropics/claude-plugins-community`; CI auto-bumps pins and catalog syncs nightly

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* New troubleshooting section: `/schedule` returns "Unknown command" — lists causes: wrong auth method (API key or cloud provider active), telemetry-disabling env vars, web session, or CLI older than v2.1.81

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New "When edits take effect" section: most settings reload live without restart; `model` and `outputStyle` are read once at session start and require `/clear` or a restart to apply
* `env` setting clarified (v2.1.143): `NO_COLOR` and `FORCE_COLOR` set here are passed to subprocesses but do not change Claude Code's own interface colors

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New "Run and verify your app" subsection documents three bundled skills available in v2.1.145+: `/run` (launch and drive the project app), `/verify` (confirm a change works), and `/run-skill-generator` (teach `/run`/`/verify` how to build and launch the app)
* Inline `!`-command substitution clarified: `!` must appear at the start of a line or after whitespace; `KEY=!`cmd`` leaves the placeholder as literal text

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* New workspace status fields: `workspace.repo.host`, `workspace.repo.owner`, `workspace.repo.name` (parsed from the `origin` remote)
* New PR status fields: `pr.number`, `pr.url`, `pr.review_state` (mirrors the PR badge; absent after merge/close)

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Edit tool: `cat`, `head`, `tail`, and `sed -n 'X,Yp'` on a single file (no pipes/redirects) all satisfy the read-before-edit requirement (previously only `cat` and `sed -n` were listed)
* Read tool: whole-file reads that exceed the token limit now return the first page with a "PARTIAL view" notice instead of a hard error; only explicit `offset`/`limit` reads that exceed the limit return an error

#### [whats-new](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/claude-code/whats-new.md) [[Source](https://code.claude.com/docs/en/whats-new)]

* New Week 20 entry added (v2.1.139–v2.1.142, May 11–15, 2026): `claude agents` view, `/goal` command, fast mode on Opus 4.7, and Rewind "Summarize up to here"

-----

## API changes

### New Documents

#### [api/compliance/apps/artifacts/download](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/artifacts/download.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/download)]

New endpoint `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content` — downloads the full text content of an artifact version for compliance purposes.

#### [api/compliance/apps/artifacts/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/artifacts/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/artifacts/retrieve)]

New endpoint `GET /v1/compliance/apps/artifacts/{artifact_version_id}` — returns artifact metadata (id, artifact_type, chat, timestamps, MD5 hash, size_bytes, title, version_id) without the content body, enabling DLP hash-matching without downloading every artifact.

#### [api/compliance/apps/chats/files/download](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/files/download.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/download)]

New endpoint `GET /v1/compliance/apps/chats/files/{claude_file_id}/content` — downloads binary content of a file referenced in chat messages.

#### [api/compliance/apps/chats/generated_files/download](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/generated_files/download.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/download)]

New endpoint `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content` — downloads binary content of a file the assistant created via tool use.

#### [api/compliance/apps/chats/generated_files/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/generated_files/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files/retrieve)]

New endpoint `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}` — returns metadata for assistant-generated files (id, chat, timestamps, filename, MD5, MIME type, size_bytes) without downloading the content.

#### [api/compliance/apps/chats/messages/list](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/messages/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages/list)]

New endpoint `GET /v1/compliance/apps/chats/{claude_chat_id}/messages` — retrieves paginated message history for a chat with filtering by `created_at` and `updated_at` range, sort order (`asc`/`desc`), and cursor-based pagination. Each message includes content blocks, file attachments, assistant-generated files, and artifacts.

#### [api/compliance/apps/projects/attachments/list](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/projects/attachments/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments/list)]

New endpoint `GET /v1/compliance/apps/projects/{project_id}/attachments` — lists files and documents attached to a project, with pagination. Returns a union of `project_file` (binary file references) and `project_doc` (plain-text document references) items.

#### [api/compliance/apps/projects/documents/metadata](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/projects/documents/metadata.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents/metadata)]

New endpoint `GET /v1/compliance/apps/projects/documents/{document_id}/metadata` — returns project document metadata (id, project, timestamps, filename, MD5, MIME type, size_bytes, user) without downloading content, enabling DLP hash-matching.

### Changed documents

#### [agents-and-tools/agent-skills/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* `max_tokens` raised from `4096` to `16000` in all skill creation examples (PowerPoint, spreadsheet, Word, PDF)
* File extraction logic updated to check for `code_execution_tool_result` and `bash_code_execution_tool_result` block types
* Language tabs expanded to include C#, Go, Java, PHP, Ruby throughout

#### [agents-and-tools/tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* `sampling_loop` example simplified: made synchronous (was `async def`), parameters reduced, tool configuration externalized to a `TOOLS` constant, tool call processing extracted to a `process_tool_calls` helper, dynamic beta flag selection removed (hardcoded to `"computer-use-2025-11-24"`)
* Language tabs expanded throughout to include C#, Go, Java, PHP, Ruby

#### [api/compliance](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* `ActivityListResponse` massively expanded: from an empty placeholder (`map[unknown]`) to 300+ fully-documented activity variants covering account management, API keys, billing, artifacts, chats, code reviews, compliance, connectors, invitations, projects, and more

#### [api/compliance/activities](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/activities.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities)]

* Same `ActivityListResponse` expansion as `compliance.md` — comprehensive union type with all activity variants fully documented

#### [api/compliance/activities/list](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/activities/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)]

* Same `ActivityListResponse` expansion — complete activity type reference in the list endpoint docs

#### [api/compliance/apps](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps)]

* `ArtifactRetrieveResponse` replaces the `ArtifactContentResponse = unknown` placeholder, with full field documentation
* `GeneratedFileRetrieveResponse` replaces `GeneratedFileContentResponse = unknown` with complete schema
* `DocumentMetadataResponse` new model added for project document metadata
* `ProjectListResponse` and `ProjectRetrieveResponse` updated: `deleted_at` and `organization_uuid` added, `organization_id` deprecated
* `FileRetrieveResponse` updated: new `md5` field added

#### [api/compliance/apps/artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/artifacts.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/artifacts)]

* `ArtifactRetrieveResponse` schema replaces `ArtifactContentResponse = unknown`; new metadata endpoint documented

#### [api/compliance/apps/chats](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats)]

* `GeneratedFileRetrieveResponse` replaces `GeneratedFileContentResponse = unknown`
* `FileRetrieveResponse` updated with new `md5` field
* Download links updated from `content.md` to `download.md` for files and generated files

#### [api/compliance/apps/chats/files](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/files.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/files)]

* New `md5` field added to `FileRetrieveResponse`; download link updated to `download.md`

#### [api/compliance/apps/chats/files/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/files/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/files/retrieve)]

* New `md5` field (lowercase hex MD5 of the file content) added to schema and response examples

#### [api/compliance/apps/chats/generated_files](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/generated_files.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/generated_files)]

* `GeneratedFileRetrieveResponse` replaces `GeneratedFileContentResponse = unknown` with full schema including `id`, `claude_chat_id`, `created_at`, `filename`, `md5`, `mime_type`, `size_bytes`

#### [api/compliance/apps/chats/list](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/list)]

* `organization_id` field on `ChatListResponse` marked as deprecated

#### [api/compliance/apps/chats/messages](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/chats/messages.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/messages)]

* Page restructured: old monolithic `ChatMessagesResponse` (bundling chat metadata + messages) replaced with `MessageListResponse` per-message schema; detailed endpoint documentation moved to the new `messages/list.md`

#### [api/compliance/apps/projects](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/projects.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects)]

* `ProjectListResponse` and `ProjectRetrieveResponse` updated with `deleted_at` and `organization_uuid` fields; `organization_id` deprecated
* `DocumentMetadataResponse` new model added

#### [api/compliance/apps/projects/attachments](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/projects/attachments.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/attachments)]

* Page restructured: `AttachmentListResponse` replaces the old `ProjectAttachmentsResponse`; detailed endpoint documentation moved to new `attachments/list.md`

#### [api/compliance/apps/projects/documents](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/projects/documents.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/documents)]

* New `DocumentMetadataResponse` schema added; new `GET /v1/compliance/apps/projects/documents/{document_id}/metadata` metadata endpoint documented

#### [api/compliance/apps/projects/list](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/projects/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/list)]

* `ProjectListResponse` updated: `deleted_at` field added, `organization_uuid` added, `organization_id` deprecated; response examples updated

#### [api/compliance/apps/projects/retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/apps/projects/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/projects/retrieve)]

* `ProjectRetrieveResponse` updated: `deleted_at` and `organization_uuid` fields added, `organization_id` deprecated; response examples updated

#### [api/compliance/organizations](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/organizations.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations)]

* `UserListResponse` updated: new `organization_role` field with enum values (`admin`, `billing`, `claude_code_user`, `developer`, `managed`, `membership_admin`, `owner`, `primary_owner`, `user`) documented as distinct from custom RBAC roles

#### [api/compliance/organizations/users](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/organizations/users.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/users)]

* Same `organization_role` field addition as organizations.md

#### [api/compliance/organizations/users/list](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/api/compliance/organizations/users/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/users/list)]

* `organization_role` field added to schema and response examples
* Sort order description updated: "sorted by organization join date ascending" (was "account creation date ascending")

#### [build-with-claude/claude-in-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

* New callout added directing users to run `/claude-api migrate` in Claude Code to apply model ID swaps and breaking parameter changes when upgrading Claude models

#### [build-with-claude/claude-in-microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* Same `/claude-api migrate` callout added after the deployment names section

#### [build-with-claude/claude-on-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Same `/claude-api migrate` callout added after the model IDs table

#### [build-with-claude/claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* Same `/claude-api migrate` callout added after the model IDs section

#### [manage-claude/compliance-content-data](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/manage-claude/compliance-content-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)]

* Messages endpoint link updated from `messages.md` to `messages/list.md`
* Messages endpoint expanded with new filtering parameters: `created_at.*` and `updated_at.*` range bounds (`gt`, `gte`, `lt`, `lte`) and `order` parameter (`asc`/`desc`)
* Distinction between `files`, `generated_files`, and `artifacts` clarified: artifacts are versioned documents with `version_id` revisions across turns
* Retrieve files table expanded with new rows for generated file metadata, artifact version metadata, and project document metadata endpoints
* New `Content-MD5` response header documented (base64-encoded MD5 per RFC 1864) on download endpoints
* Project attachment list link updated from `attachments.md` to `attachments/list.md`

#### [manage-claude/compliance-org-data](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/manage-claude/compliance-org-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-org-data)]

* New `organization_role` field documented with all valid enum values; clarified as independent of custom RBAC roles
* User list sort order corrected: "sorted by organization join date ascending" (was "account creation date ascending")

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/5e2bafa17c80342ea4215ff487cfe1f272f11db6/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* GitHub org name corrected in Modal guide URL: `modal-projects` → `modal-labs`
* `ant` CLI version bumped from `1.9.0` to `1.9.1` in the install command and Dockerfile
