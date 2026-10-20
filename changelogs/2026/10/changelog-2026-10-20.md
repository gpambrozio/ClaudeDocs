# [Claude docs changes for October 20th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc)]

## Executive Summary
- Claude Code 2.1.304 adds `/auto-mode-setup`, a guided setup that teaches auto mode about your environment. It also adds a warning before resuming an inactive conversation that would use a noticeable share of your 5-hour usage limit.
- `claude -p` and Agent SDK runs with no permission mode set now start in Manual mode (v2.1.302+). Calls that need approval are denied unless you add allow rules or pass `--permission-mode auto`. Auto mode also gains a configurable classifier model (`CLAUDE_CODE_AUTO_MODE_MODEL`).
- Routines were renamed "scheduled tasks" across the Claude Code docs. The Desktop app now has one Scheduled tasks page covering both local and cloud tasks, with step-by-step setup for local tasks.
- A recursive `rm` on a mounted drive (`/Volumes`, `/media`, WSL `/mnt/c`) now gets a safety prompt. `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT=1` turns it off.
- The API web fetch tool gets a `url_sources` parameter for limiting which URLs Claude may fetch. The Compliance API gains a user preferences endpoint and about 8 new activity types.

## New Claude Code versions

### [2.1.304](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/versions/2.1.304.md)

#### New features

* Added `/auto-mode-setup`, a guided setup that reads your project and recent sessions to teach auto mode about your environment. It is now also available on Bedrock, Vertex, Foundry, Claude apps gateway and telemetry-disabled sessions.
* Added `/claude-api managed-agents-secure`, which compares a Managed Agents agent's settings with Anthropic's published security guide without changing anything
* Added a warning on Pro and Max plans when resuming an inactive conversation would use a noticeable share of your 5-hour usage limit
* Mods: added `decider: "person"` to a `tool.check` answer, added `e.isReadOnly` to the `tool.check` event, and added a transcript line when an earlier-running plugin skips one of your mod's hooks
* Added the names of earlier-called tools to the compaction summary in the transcript view (Ctrl+O)
* Code Review: owners can choose Quick, Standard (the default) or Deep review levels per organization or per repository, and can review every repository in a GitHub organization, including ones added later
* [VSCode] Added mod drawing in the chat panel for sessions on Bedrock, Vertex AI and Foundry, behind an LLM gateway, or with telemetry turned off

#### Existing feature improvements

* Tool search is now on by default behind a custom `ANTHROPIC_BASE_URL`; a 400 or 422 from the gateway is retried without it
* `CLAUDE_CODE_AUTO_COMPACT_WINDOW` now accepts `k` and `M` suffixes, and warns when a value is out of range or ignored
* Compaction now sends Claude the skill list again afterwards, and `/reload-skills` sends only new or changed skills
* Skills from one source can register at most 1,024 hooks and 16,384 matcher characters per session
* Mods' `settings.read` hooks now receive each settings layer and can rewrite the merged settings, so a managed mod can make an organization's setting a ceiling
* `/usage` now says when a rate limit on usage data ends
* In cloud sessions, a new conversation's first turn no longer waits for local (stdio) MCP servers of plugins synced from claude.ai, unless the server sets `alwaysLoad: true`
* Better responsiveness with many concurrent subagents, lower memory use in long conversations, and faster first request when resuming large compacted sessions in SDK and headless mode
* Smaller session files in auto mode, because the safety classifier's context is no longer stored with every request
* The `/artifacts` delete confirmation now shows numbered choices
* The `/claude-api` skill uses the `ant` CLI on Claude Platform on AWS
* [VSCode] Background sub-agents now show as one status line under their Agent card instead of streaming every step into the chat

#### Major bug fixes

* Fixed `rm -r` of a mounted drive or top-level mount folder (`/Volumes`, `/media`, `/mnt/c`) not getting the safety prompt
* Fixed `claude --worktree` removing the worktree and branch without asking at exit when HEAD was detached or on another branch, which could lose commits
* Fixed sandboxed commands failing on Linux when a `sandbox.filesystem.denyRead` glob contains brackets that aren't a character class
* Fixed `CLAUDE_CODE_TRANSCRIPT_LOCAL_GC` dropping messages from the saved transcript when the disk filled up
* Fixed a plugin keeping a headless run going past `--max-turns`, Stop, or ended input
* Fixed `context_management: Extra inputs are not permitted` errors behind LLM gateways
* Fixed OpenTelemetry settings from server-managed settings being ignored for the session after first-run sign-in or `/logout`
* Fixed a PreToolUse hook's deny reason being replaced by a timeout error when an Agent SDK callback hook on the same call timed out
* Fixed "Context limit reached" / "Prompt is too long" errors after stopping a turn during compaction
* Fixed subagents sometimes forgetting their most recent work when messaged or resumed right after finishing
* Fixed Remote Control failing to start from Claude Desktop with `DISABLE_TELEMETRY` or `DO_NOT_TRACK` set on a paid plan
* Fixed unsandboxed Bash commands in Claude Desktop Code tab sessions not seeing environment variables exported in shell startup files
* Fixed agent teams: approving a shutdown request from the main session no longer exits the whole CLI
* [VSCode] Fixed sessions failing to start with "Subprocess initialization did not complete within 60000ms" because of slow SessionStart hooks
* [Code Review] Fixed pull requests opened right after Code Review was turned on being silently skipped

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [Automate work with scheduled tasks (routines)](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Routines were renamed "scheduled tasks" (formerly routines). The page keeps the same cloud schedule, API and GitHub triggers. [[lines 1-7](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/routines.md?plain=1#L1-L7)] [[Source](https://code.claude.com/docs/en/routines#automate-work-with-scheduled-tasks)]
* `web-scheduled-tasks.md` received the same changes.

#### [Desktop scheduled tasks](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* The Scheduled tasks page now lists both local and cloud tasks. [[lines 7-12](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L7-L12)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#schedule-recurring-tasks-in-claude-code-desktop)]
* Added a step-by-step guide to creating a local task. It covers the **Only on this computer** switch, picking a local folder, the schedule, and the permission mode and model. [[lines 36-95](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L36-L95)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#create-a-scheduled-task)]
* Added a **Manual** schedule option, which runs only when you click **Run now**. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L102)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#schedule-options)]

#### [Desktop and Desktop changelog](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Roughly 270 lines were added to the Desktop changelog (mirrored in `desktop.md`) with new Claude Desktop releases.

#### [Env vars](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `API_TIMEOUT_MS` now describes a per-attempt timeout for response headers, and how it applies to non-streaming requests. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/env-vars.md?plain=1#L179)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_AUTO_COMPACT_WINDOW` now accepts suffixed values such as `200k` (v2.1.304+). [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/env-vars.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added `CLAUDE_CODE_AUTO_MODE_MODEL` and `CLAUDE_CODE_DISABLE_MOUNTED_DRIVE_RM_PROMPT`.

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Added `CLAUDE_CODE_OTEL_CONTENT_MAX_LENGTH` to limit content-bearing attributes. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/monitoring-usage.md?plain=1#L124)] [[Source](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)]
* Added `message.uuid` and `client_request_id` attributes to events, with correlation details. [[lines 745-747](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/monitoring-usage.md?plain=1#L745-L747)] [[Source](https://code.claude.com/docs/en/monitoring-usage#event-correlation-attributes)]
* Tool decisions can now be `cancelled`. Tool decision events carry a `tool_source` attribute listing the decision sources. [[lines 305-308](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/monitoring-usage.md?plain=1#L305-L308)] [[lines 964-980](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/monitoring-usage.md?plain=1#L964-L980)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]

#### [Mods API](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* Added a section on calls and background work after the user interrupts a turn. It covers which calls are refused, how to retry them from a `turn.complete` hook, and what happens to queued prompts, commands, scheduled jobs and monitors (v2.1.304+). [[lines 217-299](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/plugins/mods/api.md?plain=1#L217-L299)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#calls-and-background-work-after-the-user-interrupts-a-turn)]

#### [Permission modes](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* `claude -p` and Agent SDK runs with no mode set now start in Manual mode (v2.1.302+). Calls needing approval are denied unless allowed by a rule, hook, callback or `--permission-prompt-tool`. The page gives CLI, TypeScript and Python examples for auto mode. [[lines 81-130](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/permission-modes.md?plain=1#L81-L130)] [[Source](https://code.claude.com/docs/en/permission-modes#common-setups)]
* Added a "Default classifier model" section: Sonnet 5 by default, with a table of overrides. Also added how to set `CLAUDE_CODE_AUTO_MODE_MODEL`, when your model is not used, and how to check the model in the debug log. [[lines 383-441](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/permission-modes.md?plain=1#L383-L441)] [[Source](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)]
* Added "The mounted drive prompt": which paths trigger it, how to turn it off, and which removals still prompt. [[lines 824-870](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/permission-modes.md?plain=1#L824-L870)] [[Source](https://code.claude.com/docs/en/permission-modes#the-mounted-drive-prompt)]
* Clarified that a mod can still approve calls in `dontAsk` mode, and that mod approval doesn't bypass your rules and hooks. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/permission-modes.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Updated for the new background sub-agent display and related behavior (about 84 lines changed).

#### [Tools reference](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Updated tool behavior details (about 52 lines changed).

#### Other Claude Code pages

* About 70 other pages received smaller edits: `routines` renaming links, `errors`, `ide-integrations`, `vs-code`, `corporate-launcher`, `claude-projects`, `cloud-environments` and `settings-reference`. A new `/auto-mode-setup` command is covered in `commands` and `slash-commands`.

-----

## API changes

### New Documents

#### [List organization members' personal preferences](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/api/compliance/organizations/user_preferences/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/organizations/user_preferences/list)]

Compliance API endpoint `GET /v1/compliance/organizations/{org_uuid}/user_preferences`. It returns each current member's "Instructions for Claude" and Cowork "Global instructions", oldest member first. It is paginated with `limit`, `page` and `next_page`, and a page may be short or empty without being the last. It has an `include_unset` option. The parent page `user_preferences.md` is also new, and `organizations.md` links to it.

### Changed documents

#### [Build a tool-using agent](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/agents-and-tools/tool-use/build-a-tool-using-agent.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)]

* Large rewrite: roughly 800 lines of cURL shell scripting were removed.

#### [Compliance API (activities)](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/api/compliance.md) [[Source](https://platform.claude.com/docs/en/api/compliance)]

* Eight new activity types (525 to 533), also in `activities.md` and `activities/list.md`: `claude_plugin_served_version_updated`, `claude_plugin_version_created`, `org_hipaa_claude_code_cowork_restrictions_deferred`, `org_hipaa_claude_code_cowork_restrictions_enabled`, `org_library_submission_created`, `org_library_submission_resolved`, `org_library_submission_withdrawn` and `org_member_avatar_removed`.

#### [MCP connector](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* The pinned-toolset example was simplified. Instead of shell scripts that capture and re-inject the `mcp_tool_listing`, it now shows two explicit requests, with a pinned `echo` tool in the second. [[lines 575-700](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/agents-and-tools/mcp-connector.md?plain=1#L575-L700)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector#pin-an-mcp-servers-tool-list-beta)]

#### [Multiagent orchestration](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/managed-agents/multiagent-orchestration.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multiagent-orchestration)]

* Examples and text were reworked (about 70 lines changed). The Managed Agents `quickstart` and `github` pages were also updated.

#### [Vault credentials (all SDK and CLI variants)](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/api/beta/vaults/credentials.md) [[Source](https://platform.claude.com/docs/en/api/beta/vaults/credentials)]

* Reference text was rewritten (same changes in the TypeScript, Python, Ruby, Java, Go, C#, PHP and CLI variants).
  * Titles now read "Create a Credential", "Retrieve a Credential", and so on.
  * `expires_at` must be in the future. When you send a new `access_token`, send its `expires_at` too, or the token keeps the old expiry.
  * `mcp_oauth` client secret updates must match the credential's current `token_endpoint_auth` type.
  * An empty scope string clears the stored scope.
  * Secret host lists accept up to 16 entries. A `*.example.com` entry matches subdomains only, not `example.com` itself.

#### [Web fetch tool](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Added an optional `url_sources` parameter to turn off any of three allowed URL sources: `user_input`, `client_tool_results` and `server_tool_results`. Each takes `all`, `none`, or an `only`/`except` tool filter, and it works with `web_fetch_20250910` and later versions. It is offered as an anti-exfiltration measure. [[lines 25-34](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L25-L34)] [[lines 418-422](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L418-L422)] [[lines 641-685](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L641-L685)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool#web-fetch-tool)]
* The `url_not_in_prior_context` error also covers URLs that appear only in sources `url_sources` excludes. [[line 622](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L622)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool#errors)]

#### [CLI models](https://github.com/gpambrozio/ClaudeDocs/blob/f91bed5045c8e08bf8d74712e29f7ae24aa30fbc/docs-md/api/api/cli/models.md) [[Source](https://platform.claude.com/docs/en/api/cli/models)]

* About 55 lines of new CLI reference content (mirrored in `cli/beta/models.md`).
