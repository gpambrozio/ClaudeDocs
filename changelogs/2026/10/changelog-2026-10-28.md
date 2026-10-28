# [Claude docs changes for October 28th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/2d174233063f37a33c3f7630171cee8c3a04f481) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/2d174233063f37a33c3f7630171cee8c3a04f481)]

## Executive Summary
- New `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS` environment variable (v2.1.311+) lets `bypassPermissions` mode run `rm`/`rmdir` on critical paths with no prompt, with startup notices and troubleshooting for when it has no effect
- Claude Code 2.1.312 adds `oidc.user_id_claim` for the Claude apps gateway, click-to-send for queued messages, and caps concurrent prompt/agent hooks at 24 per session
- Managed machines can now stop offering the keyless Console sign-in by deploying `forceLoginOrgUUID`; `forceLoginMethod: "claudeai"` also removes it
- Mods docs gain `Button` `variant`, `role` and `children`, multi-line `Input` `rows`, and clearer `settings.read` hook guidance
- Claude Desktop and claude.ai settings paths are now documented as **Settings > Code** or **Settings > Claude Code**, and cloud routines can pick an effort level

## New Claude Code versions

### [2.1.312](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/versions/2.1.312.md)

#### New features

* Added `oidc.user_id_claim` to the Claude apps gateway, to identify people by an id_token claim other than `sub` (such as Microsoft Entra ID's `oid`)
* Added click to send: in fullscreen, clicking the "to send now" hint under a queued message sends it right away
* [Cloud sessions] Added an effort level to the model picker when creating or editing a cloud routine
* [Cloud sessions] Added a Bash editor with colors, line numbers and a Copy button for the setup script in cloud environment settings

#### Existing feature improvements

* Improved the prompt's effort indicator: a mid-task change now says it may wait for your next message
* Improved WebFetch errors in cloud sessions: an unresolvable host is explained as possibly outside the allowed network domains
* Bedrock, Vertex, Foundry and Mantle now use the shorter system prompt for unrecognized model names (custom deployments, inference profile ARNs); set `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT=0` to keep the full prompt
* Automatic model switches after a flagged message now also cover unrecognized model names; set `CLAUDE_CODE_DISABLE_REFUSAL_FALLBACK=1` to turn them off
* Prompt and agent hooks now run at most 24 at a time per session (sub-agents included), plus at most 12 that have waited longer than their event's timeout; a `timeout` under 1 second counts as 1 second
* A subagent's `autoCompactWindow` now lowers the window set by `CLAUDE_CODE_AUTO_COMPACT_WINDOW`
* OpenTelemetry `mcp_server.name` now reports the real name of fixed-URL remote MCP servers declared by official-marketplace plugins; the `claude_code.safety_event` event is no longer sent
* Usage limit messages now say "5-hour limit" instead of "session limit"
* [Cloud sessions] Cloud sessions started from the CLI get names and branch names from the server
* [Claude Tag] Slack retry notices now name the model in use or say rate limits were hit

#### Major bug fixes

* Fixed managed settings and organization policy not being fetched after signing in from the VS Code extension
* Fixed Claude overwriting a very large CLAUDE.md, rules file or @-included file after seeing only its start; Write now asks Claude to read it all or edit in place
* Fixed per-directory and `paths:` skills not being found after a Bash `cd` deeper into a git repository
* Fixed a command with an invalid name stopping all commands from loading, which could leave `claude -p` with no output
* Fixed the Read tool sometimes failing on PDF pages ("pdftoppm failed") during old session file clean-up
* Fixed the spinner, OpenTelemetry `effort` values and transcripts naming a newly picked effort level before the model applied it
* [Code Review] Fixed Code Review reviewing an outdated commit when GitHub delivered a push event late
* [Cloud sessions] Fixed resending an unchanged message after a failed send sometimes running it twice
* [Claude Tag] Fixed Claude in Slack not replying in channels whose environment has network access set to None, and a channel's switch/settings resetting when a private channel goes public

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Added a link to the new "Manage plugins for your organization" page for installing shared plugins through managed settings. [[line 190](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/admin-setup.md?plain=1#L190)] [[Source](https://code.claude.com/docs/en/admin-setup#next-steps)]

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* `max_turns` now explained as counting each tool-call turn plus one for the final text-only response; otherwise the run ends with an `error_max_turns` result and no final reply. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#turns-and-messages)]

#### [agent-sdk/configuration](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/configuration.md) [[Source](https://code.claude.com/docs/en/agent-sdk/configuration)]

* Switching to a model auto mode doesn't support moves the session to `default` mode. [[line 160](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/configuration.md?plain=1#L160)] [[Source](https://code.claude.com/docs/en/agent-sdk/configuration#change-configuration-mid-session)]

#### [agent-sdk/hosting](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/hosting.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hosting)]

* Node.js requirement for the TypeScript SDK raised to 18.14+. [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/hosting.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/agent-sdk/hosting#runtime-dependencies)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Pointer to the new section on turning off the critical-path removal prompt. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `Task` alias for the `Agent` tool is accepted only when the tool is available to the session. [[line 2523](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/python.md?plain=1#L2523)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#agent)]
* `allowAllUnixSockets` also allows VM sockets (`AF_VSOCK`) on Linux. [[line 3592](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/python.md?plain=1#L3592)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#sandboxnetworkconfig)]

#### [agent-sdk/streaming-output](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/streaming-output.md) [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-output)]

* Clarified what a cut-off stream delivers: `message_stop` always arrives, `content_block_stop` arrives except for open tool calls, and `message_delta` may be missing after a dropped connection or non-streaming fallback. [[lines 115-118](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/streaming-output.md?plain=1#L115-L118)] [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-output#handle-a-stream-thats-cut-off)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `startup()` keeps only the newest `hook_progress` message from `SessionStart`/`Setup` hooks and delivers held messages once you call `.query()`. [[lines 104-105](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L104-L105)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#returns)]
* Returning `allow` with more than 4,096 `updatedPermissions` items is treated as invalid and denied. [[line 1404](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1404)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#permissionresult)]
* `agent_id` behavior for nested subagents expanded. [[line 1695](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1695)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkassistantmessage)]
* `maxTurns` now links to the definition of a turn. [[line 525](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L525)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* `/resume` in agent view no longer documented as needing v2.1.212+. [[line 319](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-view.md?plain=1#L319)] [[Source](https://code.claude.com/docs/en/agent-view#bring-back-a-past-session)]
* `/fork` section split into subsections: prompting the copy, where the copy runs, and sessions that can't be forked. [[lines 453-472](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/agent-view.md?plain=1#L453-L472)] [[Source](https://code.claude.com/docs/en/agent-view#prompt-the-copy-and-open-its-session)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* `forceLoginMethod: "claudeai"` (or `forceLoginOrgUUID`) removes the keyless sign-in; `"console"` alone still allows it after a failed sign-in. [[lines 126-127](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/authentication.md?plain=1#L126-L127)] [[Source](https://code.claude.com/docs/en/authentication#sign-in-without-an-api-key)]
* New section "Stop offering the keyless sign-in on managed machines", covering migration of keyless, environment/helper and claude.ai logins. [[lines 140-149](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/authentication.md?plain=1#L140-L149)] [[Source](https://code.claude.com/docs/en/authentication#stop-offering-the-keyless-sign-in-on-managed-machines)]

#### [iam](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/iam.md) [[Source](https://code.claude.com/docs/en/iam)]

* Same keyless sign-in changes as in authentication. [[lines 126-149](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/iam.md?plain=1#L126-L149)] [[Source](https://code.claude.com/docs/en/iam#sign-in-without-an-api-key)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* New troubleshooting section for files missing from the diff view (unpushed command-made changes, changes after the last push). [[lines 263-271](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L263-L271)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#troubleshoot-a-missing-file-in-the-diff-view)]
* `/config` and sharing settings now point to **Settings > Code** or **Settings > Claude Code** (or **Privacy**). [[lines 278-348](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L278-L348)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#manage-context)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* Notes that the diff against the base branch can leave out unpushed changes. [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/web-quickstart.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/web-quickstart#review-and-iterate)]

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* **Move to project** renamed **Continue in project** throughout. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/claude-projects.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/claude-projects#create-a-project)]
* New **Keep this computer awake for Remote Control** option and restructured recovery steps for a lost folder connection. [[lines 274-278](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/claude-projects.md?plain=1#L274-L278)] [[Source](https://code.claude.com/docs/en/claude-projects#run-a-thread-on-your-own-computer)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Network secrets: on every plan you can add and delete secrets on your own environments; without an organization admin role, Team and Enterprise users get the shorter single-host form. [[lines 98-135](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/cloud-environments.md?plain=1#L98-L135)] [[Source](https://code.claude.com/docs/en/cloud-environments#requirements)]

#### [cross-session-messaging](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/cross-session-messaging.md) [[Source](https://code.claude.com/docs/en/cross-session-messaging)]

* Messages Claude hasn't received yet appear under `Waiting to be delivered` at the end of the transcript (v2.1.309+). [[lines 173-175](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/cross-session-messaging.md?plain=1#L173-L175)] [[Source](https://code.claude.com/docs/en/cross-session-messaging#what-a-message-looks-like)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Settings paths updated to **Settings > Code** or **Settings > Claude Code** across the page. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/desktop#accept-a-suggested-prompt)]
* Computer use is enabled under **This computer > System** or **Capabilities**, depending on the Settings menu. [[lines 351-359](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop.md?plain=1#L351-L359)] [[Source](https://code.claude.com/docs/en/desktop#enable-computer-use)]
* Connectors are managed via **Customize > Connectors**. [[line 584](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop.md?plain=1#L584)] [[Source](https://code.claude.com/docs/en/desktop#connect-external-tools)]
* Cloud diffs can leave out unpushed changes. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/desktop#review-changes-with-diff-view)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Mirrors the desktop page updates (settings paths, computer use, connectors, cloud diff caveat). [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop-changelog.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/desktop-changelog#accept-a-suggested-prompt)]

#### [desktop-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* **Keep computer awake** is under **Settings > Desktop app** or **Settings > This computer > System**. [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L134)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#how-scheduled-tasks-run)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS`: runs dangerous `rm` commands with no prompt in `bypassPermissions` mode. [[line 290](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/env-vars.md?plain=1#L290)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_RESUME_SHOWS_CUT_OFF_CALLS`: keeps interrupted tool calls, marked as cut off, when a resumed turn continues. [[line 368](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/env-vars.md?plain=1#L368)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entry "Feedback payload too large" with the fix (set **Send transcript** to `no`). [[lines 2211-2222](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/errors.md?plain=1#L2211-L2222)] [[Source](https://code.claude.com/docs/en/errors#feedback-payload-too-large)]
* New entry "A command-line deny rule cannot be handed to a teammate intact" for split-pane agent teams; switch Teammate mode to `in-process`. [[lines 4691-4703](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/errors.md?plain=1#L4691-L4703)] [[Source](https://code.claude.com/docs/en/errors#a-command-line-deny-rule-cannot-be-handed-to-a-teammate-intact)]
* "Couldn't send feedback" now means the service didn't confirm receipt; treat the report as not received. [[line 2191](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/errors.md?plain=1#L2191)] [[Source](https://code.claude.com/docs/en/errors#couldnt-send-feedback)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Clarified WorktreeCreate path resolution and rejection rules (relative paths, `.`/`..` segments, symlinks). [[lines 3195-3197](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/hooks.md?plain=1#L3195-L3197)] [[Source](https://code.claude.com/docs/en/hooks#worktreecreate-output)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Reorganized the `mcp_server_errors` / stderr warning explanation. [[lines 283-287](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/headless.md?plain=1#L283-L287)] [[Source](https://code.claude.com/docs/en/headless#fail-ci-when-a-plugin-or-mcp-server-doesnt-load)]

#### [large-codebases](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/large-codebases.md) [[Source](https://code.claude.com/docs/en/large-codebases)]

* Local deny rules like `Read(./**/vendor/**/*)` anchor at the working directory; use `//`-absolute paths if you start from subdirectories. [[lines 157-161](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/large-codebases.md?plain=1#L157-L161)] [[Source](https://code.claude.com/docs/en/large-codebases#block-reads-of-generated-and-vendored-code)]
* Plugins can be installed for everyone through managed settings. [[line 377](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/large-codebases.md?plain=1#L377)] [[Source](https://code.claude.com/docs/en/large-codebases#centralize-conventions-when-layering-stops-scaling)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Connection failures and unconfigured servers" subsection; failure details are redacted and never include the expanded server URL. [[lines 277-283](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/mcp.md?plain=1#L277-L283)] [[Source](https://code.claude.com/docs/en/mcp#connection-failures-and-unconfigured-servers)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* New section "Turn off the critical-path removal prompt in bypassPermissions mode" with per-shell examples, a danger warning, and scope limits (not plan mode; Bash and Monitor only). [[lines 959-1015](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/permission-modes.md?plain=1#L959-L1015)] [[Source](https://code.claude.com/docs/en/permission-modes#turn-off-the-critical-path-removal-prompt-in-bypasspermissions-mode)]
* Startup notices explain whether the variable is active, and "Why the critical-path removal prompt stays on" lists causes (permission-prompt tools, `PermissionRequest` hooks, VS Code/Desktop, deny/ask rules). [[lines 982-1015](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/permission-modes.md?plain=1#L982-L1015)] [[Source](https://code.claude.com/docs/en/permission-modes#turn-off-the-critical-path-removal-prompt-in-bypasspermissions-mode)]
* Other sections now cross-reference the opt-out. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/permission-modes.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/permission-modes#actions-no-mode-auto-approves)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Compound commands: every subcommand must be allowed to run without a prompt (Bash and PowerShell). [[line 215](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/permissions.md?plain=1#L215)] [[Source](https://code.claude.com/docs/en/permissions#compound-commands)]
* Windows network shares: example `claude --add-dir Z:\`. [[line 521](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/permissions.md?plain=1#L521)] [[Source](https://code.claude.com/docs/en/permissions#network-paths)]
* New "Where output styles, hooks, and local settings load from" section; `settings.local.json` loads from the git repository root. [[lines 708-712](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/permissions.md?plain=1#L708-L712)] [[Source](https://code.claude.com/docs/en/permissions#where-output-styles-hooks-and-local-settings-load-from)]

#### [plugins/mods/events](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/events.md) [[Source](https://code.claude.com/docs/en/plugins/mods/events)]

* New "Send a request to a different model": aliases like `haiku` in `turn.step` need v2.1.309+, and `next({ ...e, model: 'haiku' })` redirects a request. [[lines 312-317](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/events.md?plain=1#L312-L317)] [[Source](https://code.claude.com/docs/en/plugins/mods/events#send-a-request-to-a-different-model)]
* Reworked `settings.read` hook explanation: when it first runs, how to detect origin, and what returns do. [[lines 320-381](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/events.md?plain=1#L320-L381)] [[Source](https://code.claude.com/docs/en/plugins/mods/events#change-or-refuse-a-settings-read)]

#### [plugins/mods/gallery](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/gallery.md) [[Source](https://code.claude.com/docs/en/plugins/mods/gallery)]

* `Input` `rows` set to 2 or more makes a multi-line field; requires v2.1.301+, ignored in the VS Code extension, and keyboard rules apply to the terminal. [[lines 245-288](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/gallery.md?plain=1#L245-L288)] [[Source](https://code.claude.com/docs/en/plugins/mods/gallery#input)]

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* `rows` and Up/Down behavior in `Input` now scoped to the terminal. [[lines 420-545](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/interface.md?plain=1#L420-L545)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#build-a-tree-from-elements)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* `Button` gains `children` (v2.1.295+), `variant` (`primary`/`secondary`) and `role` (`dismiss`). [[lines 266-293](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/reference.md?plain=1#L266-L293)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#elements)]
* New limits: `$.process.run` output capped at 4 MiB with truncation flags, and 28,000-level nesting depth for API call arguments, `next` events and hook return values (v2.1.299+). [[lines 372-394](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/reference.md?plain=1#L372-L394)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#limits)]
* `$.ui.toast` in the classic renderer can replace an older toast. [[line 390](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/reference.md?plain=1#L390)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#limits)]
* `settings.read` requirements consolidated into the events table. [[line 115](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/reference.md?plain=1#L115)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#commands-and-configuration)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* `settings.read` refusal messages may come from another mod; added step-by-step procedure to find the offending mod with `--debug-file`. [[lines 363-385](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L363-L385)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#the-answer-for-key-is-no-value-the-key-can-hold)]
* Returned permission rules and `env` on Claude Code's own settings read are not applied. [[line 340](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L340)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#a-key-your-settingsread-hook-returns-doesnt-take-effect)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* New step "Select a model and effort level" for cloud tasks, and the effort level is selectable in the CLI instructions box. [[lines 114-139](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/routines.md?plain=1#L114-L139)] [[Source](https://code.claude.com/docs/en/routines#create-from-the-web)]

#### [web-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/web-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/web-scheduled-tasks)]

* Same model and effort level step as in routines. [[lines 114-139](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/web-scheduled-tasks.md?plain=1#L114-L139)] [[Source](https://code.claude.com/docs/en/web-scheduled-tasks#create-from-the-web)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* A `git clone` naming an absolute, `~` or `..` path isn't covered by an entry; use a relative path. [[line 319](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/sandboxing.md?plain=1#L319)] [[Source](https://code.claude.com/docs/en/sandboxing#run-commands-outside-the-sandbox-with-excludedcommands)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Non-interactive runs apply approval-requiring settings for that run only and re-fetch them at each startup until approved interactively. [[lines 287-290](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/server-managed-settings.md?plain=1#L287-L290)] [[Source](https://code.claude.com/docs/en/server-managed-settings#approval-memory)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Resumed sessions: interrupted tool calls aren't rerun (details moved to `CLAUDE_CODE_RESUME_SHOWS_CUT_OFF_CALLS`). [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/sessions.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/sessions#what-a-resumed-session-restores)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `forceLoginMethod: "claudeai"` also removes the keyless Console sign-in. [[line 5172](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/settings-reference.md?plain=1#L5172)] [[Source](https://code.claude.com/docs/en/settings-reference#forceloginmethod)]
* `CLAUDE_CODE_EVEN_MORE_DANGEROUSLY_SKIP_PERMISSIONS` is ignored in every settings file. [[line 2391](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/settings-reference.md?plain=1#L2391)] [[Source](https://code.claude.com/docs/en/settings-reference#variables-claude-code-ignores-in-env)]
* A `<<EOF` heredoc counts as a redirection that keeps a Bash call sandboxed. [[line 1292](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/settings-reference.md?plain=1#L1292)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxexcludedcommands)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* The claude-api skill's `upgrade` subcommand now described as upgrading the Anthropic SDK to a new major version and updating code for breaking changes (not just Python 0.x to 1.x). [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/skills.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/skills#work-on-claude-api-projects)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Same `upgrade` subcommand update as in skills. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/slash-commands.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/slash-commands#work-on-claude-api-projects)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* The per-invocation `model` parameter on the Agent tool takes only an alias (`sonnet`, `opus`, `haiku`, `fable`), not a full model ID or `inherit`. [[line 351](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/sub-agents.md?plain=1#L351)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-a-model)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* `"fresh"` base falls back to local `HEAD` when there's no remote or `origin/HEAD` can't be fetched. [[lines 159-163](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/worktrees.md?plain=1#L159-L163)] [[Source](https://code.claude.com/docs/en/worktrees#choose-the-base-branch)]
* New "Worktree locks and manual removal" heading. [[line 138](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/worktrees.md?plain=1#L138)] [[Source](https://code.claude.com/docs/en/worktrees#worktree-locks-and-manual-removal)]
* New troubleshooting entry: with `git replace`, created worktrees hold the original objects' content; create the worktree manually instead. [[lines 327-332](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/worktrees.md?plain=1#L327-L332)] [[Source](https://code.claude.com/docs/en/worktrees#a-worktree-claude-code-created-has-the-original-content-of-replaced-objects)]

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Save-dialog and symlink-check wording tightened. [[lines 197-203](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/claude-code/workflows.md?plain=1#L197-L203)] [[Source](https://code.claude.com/docs/en/workflows#save-the-workflow-for-reuse)]

-----

## API changes

### New Documents

None.

### Changed documents

#### [about-claude/models/overview](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/models/overview.md) [[Source](https://platform.claude.com/docs/en/models/overview)]

* Models API capability fields now link to the API reference; a pointer to the full List Models response was added. [[lines 67-81](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/models/overview.md?plain=1#L67-L81)] [[Source](https://platform.claude.com/docs/en/models/overview#using-the-models-api)]

#### [api/claude-platform-on-aws-iam-actions](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/api/claude-platform-on-aws-iam-actions.md) [[Source](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions)]

* Added the `DeleteUserProfile` action (`DELETE /v1/user_profiles/{id}`) to the action list and route table. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/api/claude-platform-on-aws-iam-actions.md?plain=1#L175)] [[Source](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#user-profiles)]
* Noted that `*File` wildcards also over-match `DeleteUserProfile`. [[line 180](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/api/claude-platform-on-aws-iam-actions.md?plain=1#L180)] [[Source](https://platform.claude.com/docs/en/api/claude-platform-on-aws-iam-actions#user-profiles)]

#### [build-with-claude/batch-processing](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* `request_counts` is now described as counting requests still processing plus requests with each result type; field references link to the API reference. [[lines 704-706](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/build-with-claude/batch-processing.md?plain=1#L704-L706)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing#retrieving-batch-results)]

#### [build-with-claude/claude-models-on-google-cloud/anthropic-managed](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)]

* The workspace-less base URL also applies to the user profile routes under `/v1/user_profiles`. [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md?plain=1#L218)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#making-requests)]

#### [build-with-claude/refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* `fallback` content blocks now include a `trigger` object (`type: "refusal"` and `category`, which can be `null`); the example now shows Claude Fable 5 declining a request whose `fallbacks` list names Claude Opus 4.8. [[lines 633-651](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L633-L651)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback#what-the-response-contains)]

#### [cli-sdks-libraries/overview](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/cli-sdks-libraries/overview.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)]

* `ant` CLI and Go SDK versions bumped from 2.3.0 to 2.4.0 (also in the CLI quickstart and Managed Agents quickstart/worker docs). [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/cli-sdks-libraries/overview.md?plain=1#L59)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview#latest-versions)]

#### [manage-claude/cmek-coverage-claude-enterprise](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/cmek-coverage-claude-enterprise.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise)]

* Removed the "Chat search" and "Project knowledge search" rows from the CMEK coverage list. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/cmek-coverage-claude-enterprise.md?plain=1#L31)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-coverage-claude-enterprise#turned-off-or-changed)]

#### [manage-claude/compliance-activity-feed](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/compliance-activity-feed.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed)]

* `organization_id` is `null` for events not tied to an organization; the examples of such events (sign-in, sign-out, Compliance API calls) were removed. [[line 141](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/compliance-activity-feed.md?plain=1#L141)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-activity-feed#understand-the-activity-object)]

#### [manage-claude/inference-hooks-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/inference-hooks-configuration.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration)]

* A `DlpWebhookStatusError` entry can show the HTTP status returned and the request body size (such as `HTTP 413` · `1.3 MB`). [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/inference-hooks-configuration.md?plain=1#L124)] [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks-configuration#monitor-your-ai-security-server)]

#### [manage-claude/user-profiles](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/user-profiles.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-profiles)]

* User profiles are now supported on Claude Models on Google Cloud (Anthropic managed): create, retrieve, list and update, with the `anthropic-user-profile-id` header. Profile IDs are checked on every request there. [[lines 41-373](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/user-profiles.md?plain=1#L41-L373)] [[Source](https://platform.claude.com/docs/en/manage-claude/user-profiles#before-you-start)]

#### [manage-claude/workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* Workspace Limited Developer role now documented as unable to open or start Claude Managed Agents sessions, open memory stores, manage deployments, or download/delete files in the Console (Console only, not API). [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/manage-claude/workspaces.md?plain=1#L42)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces#workspace-roles-and-permissions)]

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* `ant` CLI install: Homebrew instructions moved up, and a new `go install github.com/anthropics/anthropic-cli/v2/cmd/ant@latest` option (Go 1.25+) with `PATH` setup. [[lines 180-215](https://github.com/gpambrozio/ClaudeDocs/blob/2d174233063f37a33c3f7630171cee8c3a04f481/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L180-L215)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#run-your-first-session)]
