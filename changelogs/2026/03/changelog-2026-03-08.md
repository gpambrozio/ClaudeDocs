# [Claude docs changes for March 8th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/63d47be5385e2c5f41c433e7cf19fa6111f96e8c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/63d47be5385e2c5f41c433e7cf19fa6111f96e8c)]

## Executive Summary
- The `Task` tool has been renamed to `Agent` across the entire Agent SDK (introduced in Claude Code v2.1.63); `Task` remains accepted as an alias for backwards compatibility
- Python SDK gains `list_sessions()` and `get_session_messages()` functions, plus new `add_mcp_server()` / `remove_mcp_server()` methods on `ClaudeSDKClient`
- New task lifecycle message types added to Python SDK: `TaskStartedMessage`, `TaskProgressMessage`, and `TaskNotificationMessage` for tracking background task progress
- Hook inputs (`PreToolUseHookInput`, `PostToolUseHookInput`, `PostToolUseFailureHookInput`) now include `agent_id` and `agent_type` fields when firing inside a subagent
- TypeScript SDK adds `getSessionMessages()` function and a new `toolConfig.askUserQuestion.previewFormat` option enabling rich HTML/Markdown previews in `AskUserQuestion` options

-----

## Claude Code changes

### Changed documents

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* List of available remote MCP servers reordered and updated with new entries (Vibe Prospecting, Magic Patterns, Midpage Legal Research, Clerk, Postman added; listing order of existing servers changed).

-----

## API changes

### Changed documents

#### [agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/agent-loop.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/agent-loop)]

* The orchestration tool `Task` has been renamed to `Agent` in the built-in tools table. [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/agent-loop.md?plain=1#L84)] [[Source](https://platform.claude.com/docs/en/agent-sdk/agent-loop)]

#### [claude-code-features](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/claude-code-features.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/claude-code-features)]

* Reference to `allowedTools: ["Task"]` updated to `allowedTools: ["Agent"]` in the subagent delegation row of the feature configuration table. [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/claude-code-features.md?plain=1#L165)] [[Source](https://platform.claude.com/docs/en/agent-sdk/claude-code-features)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/hooks.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks)]

* Matcher description updated: built-in tool list now shows `Agent` instead of `Task`. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/hooks.md?plain=1#L148)] [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks)]
* Guidance for discovering tool names updated to point to the TypeScript SDK reference for the full list. [[line 154](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/hooks.md?plain=1#L154)] [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks)]
* Hook callback arguments reformatted to bullet list; new `agent_id` and `agent_type` fields documented on all hook inputs — these are populated when the hook fires inside a subagent. [[lines 161-172](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/hooks.md?plain=1#L161-L172)] [[Source](https://platform.claude.com/docs/en/agent-sdk/hooks)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/mcp.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp)]

* `bypassPermissions` description updated: propagation now refers to the `Agent` tool instead of `Task`. [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/mcp.md?plain=1#L116)] [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp)]

#### [python](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* New `list_sessions()` function documented with parameters (`directory`, `limit`, `include_worktrees`), `SDKSessionInfo` return type, and example. [[lines 199-260](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md?plain=1#L199-L260)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* New `get_session_messages()` function documented with parameters (`session_id`, `directory`, `limit`, `offset`), `SessionMessage` return type, and example. [[lines 262-292](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md?plain=1#L262-L292)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* `ClaudeSDKClient.get_mcp_status()` return type changed from `dict` to `list[McpServerStatus]`. [[line 314](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md?plain=1#L314)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* New `add_mcp_server(name, config)` and `remove_mcp_server(name)` methods added to `ClaudeSDKClient`. [[lines 315-316](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md?plain=1#L315-L316)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* New `McpServerStatus` type documented (returned by `get_mcp_status()`), with fields for `name`, `status`, `serverInfo`, `error`, `config`, `scope`, and `tools`. [[lines 1048-1079](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md?plain=1#L1048-L1079)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* New `TaskStartedMessage`, `TaskUsage`, `TaskProgressMessage`, and `TaskNotificationMessage` types documented for tracking background task lifecycle events (subagents, backgrounded Bash commands, remote agents). [[lines 1224-1318](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md?plain=1#L1224-L1318)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* `agent_id` and `agent_type` optional fields added to `PreToolUseHookInput`, `PostToolUseHookInput`, and `PostToolUseFailureHookInput` — populated when the hook fires inside a subagent. [[lines 1551-1615](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md?plain=1#L1551-L1615)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* `Task` tool section renamed to `Agent` (with note that `Task` is still accepted as an alias). [[line 1884](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/python.md?plain=1#L1884)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Several MCP servers reordered in the listing; new servers added: Airtable, Vibe Prospecting, Magic Patterns, Gusto, SignNow, PagerDuty, Clerk, Postman, Base44, and lastminute.com.

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/sessions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/sessions)]

* Updated to mention both SDKs now expose session listing and message retrieval: `list_sessions()` / `get_session_messages()` in Python, and `listSessions()` / `getSessionMessages()` in TypeScript (previously only TypeScript was mentioned). [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/sessions.md?plain=1#L233)] [[Source](https://platform.claude.com/docs/en/agent-sdk/sessions)]

#### [subagents](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/subagents.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]

* `Task` tool renamed to `Agent` throughout; `allowedTools` examples updated accordingly. [[lines 52-68](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/subagents.md?plain=1#L52-L68)] [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]
* Compatibility note added: the rename from `Task` to `Agent` happened in v2.1.63; current SDK emits `"Agent"` in `tool_use` blocks but still uses `"Task"` in `system:init` and `permission_denials`. Checking both values is recommended. [[lines 197-200](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/subagents.md?plain=1#L197-L200)] [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]
* Detection example updated to match on both `"Task"` and `"Agent"` in `tool_use` blocks for cross-version compatibility. [[lines 221-228](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/subagents.md?plain=1#L221-L228)] [[Source](https://platform.claude.com/docs/en/agent-sdk/subagents)]

#### [typescript](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* `listSessions()` updated: `options.dir` description clarified; new `options.includeWorktrees` parameter documented (default `true`, controls whether worktree sessions are included when `dir` is inside a git repo). [[lines 93-112](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/typescript.md?plain=1#L93-L112)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* New `getSessionMessages()` function documented with parameters (`sessionId`, `dir`, `limit`, `offset`), `SessionMessage` return type, and example. [[lines 130-176](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/typescript.md?plain=1#L130-L176)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* New `toolConfig` option added to `ClaudeAgentOptions` — see `ToolConfig` type. [[line 226](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/typescript.md?plain=1#L226)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* New `ToolConfig` type documented: `askUserQuestion.previewFormat` (`"markdown"` or `"html"`) enables a `preview` field on `AskUserQuestion` options for visual mockups. [[lines 498-512](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/typescript.md?plain=1#L498-L512)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* `AskUserQuestionInput` and `AskUserQuestionOutput` updated: each option now has an optional `preview` field (string). [[lines 1241-1583](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/typescript.md?plain=1#L1241-L1583)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* `BaseHookInput` updated with optional `agent_id` and `agent_type` fields (present when hook fires inside a subagent). [[lines 893-894](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/typescript.md?plain=1#L893-L894)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* `ModelInfo` updated with new `supportsFastMode` boolean field. [[line 2056](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/typescript.md?plain=1#L2056)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]
* `Task` tool sections renamed to `Agent` (with note that `Task` is still accepted as an alias).

#### [user-input](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/user-input.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/user-input)]

* New "Option previews (TypeScript)" section documents the `toolConfig.askUserQuestion.previewFormat` option, explaining `"markdown"` and `"html"` modes, how Claude decides when to include previews, and SDK-side sanitization of HTML. [[lines 325-371](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/user-input.md?plain=1#L325-L371)] [[Source](https://platform.claude.com/docs/en/agent-sdk/user-input)]
* Limitation note updated to reference `Agent` tool instead of `Task`. [[line 488](https://github.com/gpambrozio/ClaudeDocs/blob/63d47be5385e2c5f41c433e7cf19fa6111f96e8c/docs-md/api/agent-sdk/user-input.md?plain=1#L488)] [[Source](https://platform.claude.com/docs/en/agent-sdk/user-input)]
