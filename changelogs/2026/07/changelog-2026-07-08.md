# [Claude docs changes for July 8th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7c706393bba7bba07ddafbe2f60ac00443b95234) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7c706393bba7bba07ddafbe2f60ac00443b95234)]

## Executive Summary
- Compliance API: [List chats](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/apps/chats/list.md) can now run organization-wide (no need to enumerate every user first) and gained an `order_by=updated_at` mode — the new recommended way to run and keep an eDiscovery export current.
- Compliance API: organization owners (not just the parent's primary owner) can now [create Compliance Access Keys](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/compliance-api-access.md), scoped to their own organization instead of the whole tenant.
- Compliance API: the Code Artifacts endpoints moved to `/v1/compliance/apps/code/artifacts` and no longer require the `organization_uuid` query parameter; the Activity Feed schema grew by roughly 40 new activity types (RBAC, SSO, GHE, Marketplace, Design, Cowork, LTI, tunnels, Claude Code security scanning) plus a new `SystemActor` for automated background processing.
- [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/structured-outputs.md) docs now warn that Claude may return enum/const string values that differ from your schema only in capitalization — compare case-insensitively.
- Claude Code 2.1.203 shipped a very large batch of reliability fixes for background sessions, worktrees, and the daemon, plus a login-expiry warning and a footer badge for manual permission mode; 2.1.204 followed with a fix for hooks going idle-reaped in headless sessions.

-----

## New Claude Code versions

### [2.1.203](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/versions/2.1.203.md)

#### New features

* Added a warning when your login is about to expire, so you can re-authenticate before background sessions are interrupted
* Added a grey ⏸ badge to the footer when in manual permission mode, making the active mode always visible
* Added the session's additional working directories to MCP `roots/list`, with `notifications/roots/list_changed` sent when the set changes
* [VSCode] Added a Settings toggle for "Enable Remote Control for all sessions"

#### Existing feature improvements

* Improved responsiveness while long responses stream: live-preview updates no longer re-render the whole screen
* Improved subagent behavior: agents are now less likely to re-delegate their entire task to another subagent
* Reduced binary size by ~7 MB and startup memory by ~7 MB by loading a large bundled dependency lazily instead of inlining it
* Changed left arrow to no longer close the background tasks, diff, and workflow detail views — press Esc instead
* Changed the empty `claude agents` view to always show the organized sections (Needs input / Working / Completed) with descriptions
* Removed the startup "claude command missing or broken" warnings — they now appear in `/doctor` and `/status` instead

#### Major bug fixes

* Fixed opening or switching background agent sessions on macOS stalling for 15–20 seconds due to a false low-memory detection (regression in 2.1.196)
* Fixed background sessions becoming permanently unresponsive to attach, replies, and stop when the daemon's session token went stale — the session now recovers automatically
* Fixed returning to `claude agents` silently stopping running subagents and re-running the prompt from scratch — their work now carries over
* Fixed a memory and per-turn CPU regression in interactive sessions: the context-usage indicator no longer re-analyzes the entire transcript after every turn
* Fixed background agents inheriting a stale `PATH` from the daemon instead of the dispatching shell, causing missing tools on Windows
* Fixed background and agent-view sessions dropping a shell-exported `ANTHROPIC_BASE_URL`, which sent API keys to the default endpoint and failed with 401
* Fixed Bash failing with "argument list too long" in repos with many git worktrees
* Fixed worktree-isolated subagents sometimes running shell commands in the parent checkout instead of their own worktree
* Fixed worktree creation rejecting nested repositories in multi-repo workspaces, leaving background sessions unable to isolate and edit
* Fixed background agents crash-looping when their working directory was deleted, replaced by a file, or became an invalid path — they now fail once with a clear error
* Fixed a background daemon auto-upgrade failure silently killing all running background sessions
* Fixed `TaskStop` and `TaskOutput` failing to find background agents spawned by another agent — errors now list running agents by id and description
* Fixed the `claude agents` composer discarding your typed message when a slash command isn't available there
* Fixed the agent list crashing when opening a stopped session whose conversation was already open in another session
* Fixed background sessions showing "Needs input" in the agent list after the question was already answered
* Fixed background agent startup failures showing only "exit_with_message" instead of the actual error
* Fixed background sessions ignoring `effortLevel` changes in settings.json when forked through the daemon
* Fixed attached background sessions ignoring `CLAUDE_CODE_DISABLE_MOUSE` and `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` opt-outs
* Fixed `/exit` incorrectly warning about running background agents after all named agents had completed
* Fixed background sessions started from a non-git directory unable to edit files when a `WorktreeCreate` hook was configured
* Fixed the `@` directory picker in `claude agents` not showing registered git worktrees
* Fixed background task output on Windows being permanently replaced by an empty file after `/clear`
* Fixed content jumping when scrolling up through long transcript history
* Fixed the terminal flickering and jumping while typing in bash mode when a shell-history suggestion was shown
* Fixed literal `^[[I` / `^[[O` escape codes being printed when reattaching to a background session
* Fixed LSP-only plugins being incorrectly flagged for disuse when their language servers deliver diagnostics or answer navigation requests

### [2.1.204](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/versions/2.1.204.md)

#### Major bug fixes

* Fixed hook events not streaming during SessionStart hooks in headless sessions, which could cause remote workers to be idle-reaped mid-hook

-----

## Claude Code changes

### Changed documents

#### [Agent loop](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* The `"auto"` permission mode is no longer marked TypeScript-only in the permission-mode table. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L172)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

#### [Custom tools](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* Clarified error handling: an uncaught handler exception no longer stops the agent loop — the SDK's in-process MCP server catches it and returns the raw exception message to Claude, so returning `isError: true` yourself only changes what message Claude reads, not whether the query survives. [[lines 231-236](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L231-L236)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]
* Documented that the Python SDK drops audio blocks and binary (`resource.blob`) resources from tool results with a logged warning, instead of saving them like the TypeScript SDK does. [[line 285](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L285)] [[line 335](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L335)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

#### [Hooks (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* `agent_id`/`agent_type` are now documented as populated on more Python hook input types: optional on `PreToolUse`, `PostToolUse`, `PostToolUseFailure`, and `PermissionRequest`, and required on `SubagentStart`/`SubagentStop`. [[line 177](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L177)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

#### [Permissions (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* The `auto` permission mode is no longer marked TypeScript-only. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

#### [Python SDK reference](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Added `"auto"` to the `PermissionMode` literal type, matching the mode's TypeScript-parity change. [[line 1041](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/python.md?plain=1#L1041)] [[Source](https://code.claude.com/docs/en/agent-sdk/python)]
* Added optional `agent_id`/`agent_type` fields to `PermissionRequestHookInput`. [[line 2105](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/python.md?plain=1#L2105)] [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

#### [Quickstart (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/quickstart.md) [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

* The `auto` permission mode row no longer says "TypeScript only". [[line 279](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/quickstart.md?plain=1#L279)] [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

#### [Handling user input](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/user-input.md) [[Source](https://code.claude.com/docs/en/agent-sdk/user-input)]

* Clarified when `can_use_tool` needs a keep-alive hook: with a finite message stream (`query(prompt=generator)` or `connect(prompt=async_iterable)`), the SDK closes the input stream after the last message unless a hook or in-process MCP server keeps it open; connecting with no prompt and sending via `ClaudeSDKClient.query()` keeps the stream open on its own. [[line 122](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/agent-sdk/user-input.md?plain=1#L122)] [[Source](https://code.claude.com/docs/en/agent-sdk/user-input)]

#### [Claude Code on Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Re-added the "Deploying Claude Code across your organization? Talk to sales..." enterprise promo banner at the top of the page. [[lines 1-4](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L1-L4)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [Hooks how-to guide](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Noted that tools from a plugin-bundled MCP server use a scoped name, such as `mcp__plugin_my-plugin_db__query`, when writing a hook matcher. [[line 631](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/hooks-guide.md?plain=1#L631)] [[Source](https://code.claude.com/docs/en/hooks-guide)]

#### [Hooks reference](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Documented that a matcher written against the bare server key never fires for a plugin-bundled MCP server: the tool name is scoped as `mcp__plugin_<plugin-name>_<server-name>__<tool>`. [[line 255](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/hooks.md?plain=1#L255)] [[Source](https://code.claude.com/docs/en/hooks)]
* Documented that an `mcp_tool` hook's `server` field must use the scoped name `plugin:<plugin-name>:<server-name>` for a plugin-bundled server, not the bare server key. [[line 408](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/hooks.md?plain=1#L408)] [[Source](https://code.claude.com/docs/en/hooks)]
* Noted that `transcript_path` is written asynchronously and may lag the in-memory conversation; hooks that need the current turn's final assistant text should read `last_assistant_message` on `Stop`/`SubagentStop` instead. [[line 560](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/hooks.md?plain=1#L560)] [[line 2004](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/hooks.md?plain=1#L2004)] [[Source](https://code.claude.com/docs/en/hooks)]

#### [Connect Claude Code to tools via MCP](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Documented short flag forms for `claude mcp add`: `-s`/`--scope`, `-e`/`--env`, and new `-t`/`--transport` and `-H`/`--header` short forms. [[lines 171-176](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/mcp.md?plain=1#L171-L176)] [[Source](https://code.claude.com/docs/en/mcp)]
* Clarified that a plugin-bundled MCP server registers under the scoped name `plugin:<plugin-name>:<server-name>`, needed for hook matchers and `mcp_tool` hooks' `server` field. [[lines 249-250](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/mcp.md?plain=1#L249-L250)] [[Source](https://code.claude.com/docs/en/mcp)]

#### [Plugins reference](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Added a note that hooks targeting a plugin's own bundled MCP server must use its scoped tool name and `server` field, since a bare-server-key matcher never fires. [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/claude-code/plugins-reference.md?plain=1#L134)] [[Source](https://code.claude.com/docs/en/plugins-reference)]

### Minor edits (not itemized individually)

* `channels-reference.md` had two CDN image URLs updated for the architecture and permission-relay diagrams (same images, new hosting path).

-----

## API changes

### Changed documents

#### [Agent Skills overview](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/agent-skills/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

* The API prerequisites no longer list `code-execution-2025-08-25` as a required beta header — Skills now just need the code execution tool plus `skills-2025-10-02` and `files-api-2025-04-14`. [[line 174](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/agent-skills/overview.md?plain=1#L174)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

#### [Agent Skills quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* All examples switched from `code_execution_20250825` (with the `code-execution-2025-08-25` beta header) to the newer, generally-available `code_execution_20260521` tool version, which needs no code-execution beta header — only `skills-2025-10-02`. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/agent-skills/quickstart.md?plain=1#L58)] [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/agent-skills/quickstart.md?plain=1#L81)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

#### [Deploy MCP tunnels with Docker Compose](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/mcp-tunnels/deploy-compose.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)]

* Bumped the `mcp-proxy` image digest referenced in the `docker-compose.yaml` example (setup and proxy containers). [[line 89](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/mcp-tunnels/deploy-compose.md?plain=1#L89)] [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/mcp-tunnels/deploy-compose.md?plain=1#L133)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-compose)]

#### [Deploy MCP tunnels with Helm](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/mcp-tunnels/deploy-helm.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)]

* Bumped the referenced `mcp-tunnel` Helm chart version from `2.0.0` to `2.0.1` throughout the install/upgrade examples. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/mcp-tunnels/deploy-helm.md?plain=1#L131)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/deploy-helm)]

#### [MCP tunnels quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/mcp-tunnels/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/quickstart)]

* Bumped the `mcp-proxy` image digest in the two-container `docker-compose.yaml` example. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/mcp-tunnels/quickstart.md?plain=1#L149)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/quickstart)]

#### [Advisor tool](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Added Java to the SDK tabs for the quick-start example and the two follow-up code samples. [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L54)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [Tool combinations](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/tool-use/tool-combinations.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-combinations)]

* The web-search-plus-code-execution example now uses the `code_execution_20260521` tool version instead of `code_execution_20250825`. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/agents-and-tools/tool-use/tool-combinations.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-combinations)]

#### [List chats](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/apps/chats/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/list)]

* Added an `order_by` parameter (`created_at` default, or `updated_at` for org-wide queries) that determines the sort key and which time-filter bounds are valid. [[lines 53-65](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/apps/chats/list.md?plain=1#L53-L65)] [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/list)]
* The `updated_at.*` time filters no longer require `user_ids[]` — org-wide queries can now filter and sort by update time directly. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/apps/chats/list.md?plain=1#L76)] [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/list)]
* Noted that `before_id` backward pagination is only supported for per-user queries (`user_ids[]` set); org-wide queries can't page backward. [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/apps/chats/list.md?plain=1#L165)] [[Source](https://platform.claude.com/docs/en/api/compliance/apps/chats/list)]

#### [Code Artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/code/artifacts.md), [List](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/code/artifacts/list.md), [Delete](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/code/artifacts/delete.md), [Download version](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/code/artifacts/retrieve_version.md) [[Source](https://platform.claude.com/docs/en/api/compliance/code/artifacts)]

* All three Code Artifact endpoints moved from `/v1/compliance/code/artifacts` to `/v1/compliance/apps/code/artifacts`. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/code/artifacts.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/api/compliance/code/artifacts)]
* Removed the `organization_uuid` query parameter (previously "strongly recommended" to avoid a 400 on wide child-organization scans) from the delete and download-version endpoints, and dropped the deprecated `organization_id` field from Artifact objects in favor of `organization_uuid`. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/code/artifacts/delete.md?plain=1#L30)] [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/code/artifacts.md?plain=1#L34)] [[Source](https://platform.claude.com/docs/en/api/compliance/code/artifacts)]
* List Code Artifacts is now sorted by identifier across the whole result set rather than "within each batch of child organizations" — the pagination and freshness caveats are unchanged. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/code/artifacts/list.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/api/compliance/code/artifacts/list)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/organizations/settings.md), [Get effective organization settings](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/organizations/settings/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/settings)]

* Added `expires_at` to Compliance API key objects (`null` when the key doesn't expire). [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/organizations/settings.md?plain=1#L60)] [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/settings)]
* Added a dozen new boolean setting names to track (`chat_enabled`, `claude_ai_chat_sharing_enabled`, `claude_ai_integration_sharing_enabled`, `claude_code_desktop_enabled`, `claude_code_metrics_logging_enabled`, `claude_code_security_enabled`, `claude_code_web_enabled`, `claude_code_workflows_enabled`, `claude_design_enabled`, `inline_visualizations_enabled`, `member_usage_dashboard_visible`, `work_across_apps_enabled`), a new **String**-typed setting (`claude_code_default_worker_environment_id` / `..._pool_id`), and a new `disabled_admin_request_types` string-list setting. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/organizations/settings.md?plain=1#L91)] [[line 194](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/organizations/settings.md?plain=1#L194)] [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/settings)]

#### [Activities](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/activities.md), [Query compliance activities](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/activities/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities)]

* Added a new `SystemActor` actor type for automated background processing performed by Anthropic systems without a user or customer credential, replacing what was previously described only as `FederatedIdentityActor`-style workload auth in this slot. [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/activities.md?plain=1#L90)] [[Source](https://platform.claude.com/docs/en/api/compliance/activities)]
* Expanded `activity_types` from 342 to 384 documented values, adding roughly 40 new activity types across Claude Code agent proxy (CCR) credentials/profiles/Slack bindings, Claude Code security scanning, RBAC roles, SSO/SCIM/GHE directory sync, marketplaces and plugin directory submissions, design projects, Cowork settings, LTI integrations, and tunnels. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/activities.md?plain=1#L21)] [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/api/compliance/activities/list.md?plain=1#L25)] [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)]

#### [Claude in Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* Added Go and Ruby SDK support and an Azure RBAC role prerequisite (**Foundry User** or **Cognitive Services User**) alongside the existing Azure CLI note. [[lines 29-34](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L29-L34)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]
* Noted the C# SDK always builds its base URL from the resource name and ignores `ANTHROPIC_FOUNDRY_BASE_URL`. [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L134)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]
* Added "Next steps" (Features overview, Pricing, Model deprecations) and expanded "Additional resources" cards at the bottom of the page. [[line 340](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L340)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

#### [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

* Updated example model IDs to the current lineup (`claude-sonnet-5` in the quickstart, data-zone, and raw-response examples; `anthropic.claude-haiku-4-5` in the Bedrock-migration comparison table, replacing `claude-sonnet-4-6`/`claude-opus-4-6`). [[line 320](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L320)] [[line 555](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L555)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]
* Added a "Next steps" section and expanded "Additional resources" cards. [[line 663](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/claude-platform-on-aws.md?plain=1#L663)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

#### [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Added an "Enum value casing" note: Claude may return an `enum`/`const` string value that differs from the schema only in capitalization (typically the first letter after a space), with no error and no special `stop_reason` — compare case-insensitively and avoid enum values that differ only by case. [[lines 452-467](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L452-L467)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

#### [Admin API keys](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/admin-api-keys.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]

* Documented that a Claude Enterprise **organization owner** (not just the parent's primary owner) can now create a key — restricted to Compliance API scopes and their own organization, while the primary owner can still create a key spanning every linked organization with any scope combination. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/admin-api-keys.md?plain=1#L16)] [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/admin-api-keys.md?plain=1#L47)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]

#### [Set up the Compliance API](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/compliance-api-access.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

* Renamed from "Get access to the Compliance API" and restructured around a single "Set up the Compliance API" flow: enable the API, then decide the key's scope (parent-organization-wide vs. single organization) before signing in with the matching role — an organization owner can now create a Compliance Access Key restricted to their own organization, in addition to the primary owner's parent-wide key. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/compliance-api-access.md?plain=1#L1)] [[lines 44-60](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/compliance-api-access.md?plain=1#L44-L60)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

#### [Retrieve and delete chats, files, and projects](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/compliance-content-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)]

* Rewrote the chat-listing guidance to recommend the new organization-wide, `order_by=updated_at` query (no `user_ids[]` enumeration needed) as the way to run and keep an export current, moving the older per-user `user_ids[]` + `created_at.gte` example to a "scope to specific users" subsection for legal holds on named custodians. [[lines 487-549](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/compliance-content-data.md?plain=1#L487-L549)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)]

#### [API and data retention](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Reworded the policy-violation retention carve-out: Anthropic may retain flagged inputs/outputs for up to 2 years when content is "flagged by Anthropic's automated trust and safety systems," rather than specifically "flagged for a Usage Policy violation or malicious use." [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L208)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [Self-hosted sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Clarified that the worker's bash tool invokes `/bin/bash` directly without consulting `PATH`; the TypeScript SDK needs `unzip`/`tar` on `PATH`, while Python and now Go SDKs use their standard libraries for archive extraction. [[line 54](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L54)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]
* Documented that CLI/SDK workers now preserve executable permissions recorded in a skill bundle at extraction time, rather than marking every downloaded skill file executable. [[line 586](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L586)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]
* Added Linux release-binary curl install instructions alongside the Homebrew option, with a link to the CLI's GitHub releases page. [[lines 121-152](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L121-L152)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]
* Clarified `EnvironmentWorker.handle_item()` now handles one claimed work item using either explicit IDs or the `ANTHROPIC_*` variables set by `ant beta:worker poll --on-work`, and that `reclaim_older_than_ms` re-claims work claimed but never acknowledged within that window. [[line 639](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L639)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

#### [Handle streaming refusals](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

* A streaming-classifier refusal now includes a `stop_details` object with a `category` and a human-readable `explanation` you can surface to users (delivered on the `message_delta` event when streaming); `stop_details` can still be `null`, so branch on `stop_reason` and keep your own fallback messaging. [[lines 26-42](https://github.com/gpambrozio/ClaudeDocs/blob/7c706393bba7bba07ddafbe2f60ac00443b95234/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L26-L42)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

### Minor edits (not itemized individually)

* Roughly 35 Compliance API pages (`api/compliance.md`, `api/compliance/apps*.md`, `api/compliance/groups*.md`, `api/compliance/organizations*.md`, `manage-claude/compliance-errors.md`, `compliance-org-data.md`, `compliance-activity-feed.md`, `compliance-api.md`, `compliance-faq.md`, `compliance-integration-patterns.md`, `admin-api.md`, `analytics-api.md`) had their "Get access to the Compliance API" links renamed to "Set up the Compliance API", matching the renamed page.
* `api/api/compliance/apps/chats/messages.md` and `.../messages/list.md` reworded the `truncated` field descriptions for `tool_use`/`tool_result` blocks to speak generically about "the endpoint's max parameter" instead of naming specific query-parameter names.
* `adaptive-thinking.md`, `extended-thinking.md`, and `build-with-claude/files.md` had their obfuscated "contact sales/us" email-protection hashes regenerated (same visible mailto links).
