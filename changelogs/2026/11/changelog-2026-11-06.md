# [Claude docs changes for November 6th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/082c52c713258c02f8e419e7fdd753460adeb7ef) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/082c52c713258c02f8e419e7fdd753460adeb7ef)]

## Executive Summary
- Claude Code 2.1.319 adds a `permissions.denyInsteadOfPrompting` setting, background handling of MCP tasks, and a `/claude-api latency-optimize` command. It also fixes several permission bypasses (Bash env prefix, `sed`, worktree sandbox escape).
- Hooks: `Bash` matchers now also fire for Monitor commands on `PreToolUse` and `PermissionRequest` (deny only, no allow). `PreCompact` hook stdout now becomes instructions for the compaction summary. There is a new `auth_storage_failure` notification type.
- Claude Code no longer installs or updates the IDE extension when `claude` starts in a VS Code, Cursor, or Devin Desktop terminal (v2.1.318). Only `/ide` from an external terminal installs it.
- Code Review: subdirectory `REVIEW.md` files are ignored under test, example, generated, and vendor-style directories. The remaining ones share a 150,000-byte limit.
- Claude Projects gains an "Auto-continue when usage limits reset" setting. Claude apps gateway docs add load-test mode notes and spend-limit management in Claude Desktop.

## New Claude Code versions

### [2.1.319](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/versions/2.1.319.md)

#### New features

* Added the `permissions.denyInsteadOfPrompting` setting: a tool call that would wait on a permission prompt is denied and the turn continues (terminal sessions, subagents, teammates)
* MCP tasks now work in the terminal: a tool call that runs as a task moves to the background right away, and Claude is told the result when it finishes. Set `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND` to wait inside the tool call, or `CLAUDE_CODE_DISABLE_MCP_TASKS=1` to turn tasks off
* Added `/claude-api latency-optimize` to find where your Claude API code makes people wait and try faster settings against your eval
* Added the `CLAUDE_CODE_DISABLE_FEATURE_FLAGS` environment variable, which stops feature-flag fetching without turning off telemetry
* Added an "Earlier in this session" row to `/tasks` listing finished subagents, so you can reopen and message them
* Added a warning and a startup line when Claude Code runs on an `ant auth login` sign-in that bills to a Claude Console organization
* Claude apps gateway: added `admin.pooled_conflict_rule` and `admin.pooled_priority_order`, an optional `login_notice`, `CLAUDE_GATEWAY_LOG_FORMAT=json`, spend for today, this week and this month in `/usage`, and several new startup warnings

#### Existing feature improvements

* Auto mode behind LLM gateways or with telemetry off now asks or denies calls the server can't check instead of using the built-in classifier. Set `CLAUDE_CODE_AUTO_MODE_SERVER=0` to keep the old behavior
* `/model` picker groups older models under a "More models" row
* `/context` keeps the table Claude reads short and no longer re-sends its visual grid every turn
* PostToolUse hooks now run, with up to 10 seconds, for tool calls that finish after a new message interrupts the turn
* Monitor's WebSocket watch now follows deny and ask rules on every Bash command
* Self-paced `/loop` ends when a turn finishes without rescheduling. Set `CLAUDE_CODE_LOOP_KEEPALIVE=1` for the old behavior
* Bash now asks before running `which` with flags outside a lookup/display set
* Nested skills under `.claude/skills` below the start folder load only if you start or `/cd` there when the Bash sandbox is on
* Removed `shortcuts_list` and `shortcuts_execute` from the built-in Claude in Chrome tools
* Improved contrast of faint secondary text, config save reliability on Windows, and Claude in Chrome reconnect behavior

#### Major bug fixes

* Fixed a Bash permission bypass where a crafted environment prefix could hide part of a command from permission checks
* Fixed a `sed` command skipping the permission check in accept-edits and auto mode
* Fixed Bash deny and ask rules missing commands with quoted words
* Fixed a sandbox escape when creating a worktree
* Fixed `/rewind` restoring or deleting a file through a directory symlink
* Fixed `claude -p` exiting 0 in auto mode when actions were refused for lack of a safety check
* Fixed `~/.claude.json`, settings, and edited files ending up empty or truncated when the disk fills during a save
* Fixed MCP servers on the older handshake failing to connect or returning empty results
* Fixed slash commands typed after a leading space, tab, or newline being sent to Claude as plain text
* Fixed `/diff` failing when a repository has a file or folder named `HEAD`, and opening blank after 64 or more edit turns
* Fixed `/clear` killing running commands of background agents, teammates, and workflows

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* On v2.1.314 or later, `Bash` matcher callbacks also run on `PreToolUse` and `PermissionRequest` for Monitor commands, which they can deny but not approve. [[line 222](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L222)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#matchers)]

#### [agent-sdk/plugins](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/plugins.md) [[Source](https://code.claude.com/docs/en/agent-sdk/plugins)]

* New "Reload plugins in a running session" section: TypeScript `Query.reloadPlugins()`, or send `/reload-plugins` as a prompt in Python. [[lines 67-70](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/plugins.md?plain=1#L67-L70)] [[Source](https://code.claude.com/docs/en/agent-sdk/plugins#reload-plugins-in-a-running-session)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `SandboxIgnoreViolations` is now a `dict[str, list[str]]` mapping command substrings (or `*`) to violation text to hide, instead of `file`/`network` lists. [[lines 3616-3621](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/python.md?plain=1#L3616-L3621)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#sandboxignoreviolations)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* The result message's `origin` is now documented as the origin Claude Code assigned, not a copy of the one you sent. It is absent when none was assigned. [[lines 1930-1943](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1930-L1943)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkresultmessage)]
* Added guidance on which `origin` kinds an app may set (`human`, scheduled-trigger). To send text the user didn't write, use `isSynthetic: true` with `client_composed: true`. [[lines 2464-2476](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2464-L2476)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessageorigin)]
* Updated the `human`, `peer`, and `unclassified` origin descriptions. [[lines 2475-2505](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2475-L2505)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessageorigin)]
* Clarified `sandbox.ignoreViolations` semantics. [[line 6053](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L6053)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sandboxsettings)]

#### [agent-sdk/cost-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/cost-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking)]

* Removed the paragraph about reading `usage` from `message_delta` stream events with partial messages. [[line 297](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/agent-sdk/cost-tracking.md?plain=1#L297)] [[Source](https://code.claude.com/docs/en/agent-sdk/cost-tracking#read-output-tokens-from-the-result-message)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* In auto mode, the classifier can approve or block an artifact read instead of asking you. [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/artifacts.md?plain=1#L140)] [[Source](https://code.claude.com/docs/en/artifacts#read-an-artifact-shared-with-you)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* The Chat-tab opt-in paragraph was removed from "Connect Claude Desktop", and the Desktop feature row was shortened. [[lines 349-522](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway.md?plain=1#L349-L522)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#deliver-policy-to-claude-desktop-sessions)]
* The Admin UI is now "Spend limits only": members of `admin.admin_groups` can manage spend limits from Claude Desktop 4.23118.0 or later. [[line 537](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway.md?plain=1#L537)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#availability-and-limitations)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* Load-test mode doesn't cover the wait at each replica's concurrent upstream request limit. A replica still logs the `client requests are open` warning. [[line 1650](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1650)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#load_test_mode)]

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* Load-test mode requests don't wait at the concurrency limit. [[line 201](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L201)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#concurrent-upstream-requests)]

#### [claude-apps-gateway-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-on-aws)] and [claude-apps-gateway-on-gcp](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway-on-gcp.md)

* Added a "Load-test mode" link to the related reading. [[aws line 627](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway-on-aws.md?plain=1#L627)] [[gcp line 315](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-apps-gateway-on-gcp.md?plain=1#L315)]

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* New project setting "Auto-continue when usage limits reset" (on by default). It controls whether threads and the project conversation continue on their own after a usage limit. [[line 387](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-projects.md?plain=1#L387)] [[Source](https://code.claude.com/docs/en/claude-projects#project-settings-reference)]
* The usage-limit section was rewritten around that setting. With it off, send a message after the reset to continue. [[lines 403-486](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-projects.md?plain=1#L403-L486)] [[Source](https://code.claude.com/docs/en/claude-projects#usage-and-cost)]
* New-project goal field renamed "What do you want to work on?", and "Setup script failed" recovery now asks the project conversation to run the task in a new thread. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-projects.md?plain=1#L94)] [[line 509](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/claude-projects.md?plain=1#L509)] [[Source](https://code.claude.com/docs/en/claude-projects#start-a-new-project-from-scratch)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Secret form fields updated: the Name field was removed, "Header name" and "Token" fields are described, and non-`Authorization` headers need the Header changed. [[lines 118-135](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/cloud-environments.md?plain=1#L118-L135)] [[Source](https://code.claude.com/docs/en/cloud-environments#add-a-secret)]
* A failing setup script can now either fail the session or leave it started without what the script failed to install. [[line 442](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/cloud-environments.md?plain=1#L442)] [[Source](https://code.claude.com/docs/en/cloud-environments#script-requirements)]

#### [code-review-customize](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/code-review-customize.md) [[Source](https://code.claude.com/docs/en/code-review-customize)]

* Subdirectory `REVIEW.md` files only apply on a protected branch. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/code-review-customize.md?plain=1#L24)] [[Source](https://code.claude.com/docs/en/code-review-customize#use-reviewmd-for-review-only-rules)]
* New section "When a subdirectory REVIEW.md doesn't apply": it lists excluded directory names (tests, examples, generated, vendor and third-party). The remaining files share a 150,000-byte limit. [[lines 45-57](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/code-review-customize.md?plain=1#L45-L57)] [[Source](https://code.claude.com/docs/en/code-review-customize#when-a-subdirectory-reviewmd-doesnt-apply)]

#### [deep-links](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/deep-links.md) [[Source](https://code.claude.com/docs/en/deep-links)]

* Prerequisite changed: the `claude-cli://` handler must be registered and `claude` must have been run in the local clone or worktree. [[line 103](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/deep-links.md?plain=1#L103)] [[Source](https://code.claude.com/docs/en/deep-links#embed-a-link-in-a-runbook)]

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

* Sessions no longer get a separate simulator each. Claude uses an already-running simulator unless the prompt names another. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator#how-sessions-manage-devices)]
* If you decline Claude's request, the device doesn't attach. New steps (Attach simulator, Continue, Cancel) let you use it yourself. [[lines 101-107](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L101-L107)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator#allow-a-device-the-first-time)]

#### [desktop-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* Permission guidance revised: "always allow" skips most prompts, and an "always allow" on a file edit moves only that session to Accept edits. [[lines 159-161](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L159-L161)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#permissions-for-scheduled-tasks)]
* A task can change its own schedule with `update_scheduled_task` only after you click Run now and approve the call each time. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#manage-scheduled-tasks)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_EXTRA_BODY` doesn't apply to some non-conversation requests such as `/model` checks. [[line 294](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/env-vars.md?plain=1#L294)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` also stops the install on `claude` start for versions before v2.1.318. [[line 312](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/env-vars.md?plain=1#L312)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* The single "didn't send your claude.ai login" message was replaced by three: "Your organization's settings need an update", "Couldn't load your organization's settings", and "Restart Claude Code to finish signing in". Each has its own remedy. [[lines 60-62](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/errors.md?plain=1#L60-L62)] [[lines 1116-1134](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/errors.md?plain=1#L1116-L1134)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Setting `fastMode: true` on an unsupported model leaves you on that model with fast mode off, and persistence applies only on a supported model. [[lines 34-36](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/fast-mode.md?plain=1#L34-L36)] [[Source](https://code.claude.com/docs/en/fast-mode#toggle-fast-mode)]
* The out-of-credits notification text changed to "Fast mode disabled · Out of usage credits". [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/fast-mode.md?plain=1#L220)] [[Source](https://code.claude.com/docs/en/fast-mode#handle-rate-limits)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New "Match Monitor commands" section (v2.1.314+). A `Bash` matcher also runs on Monitor commands for `PreToolUse` and `PermissionRequest`, but `allow` and `updatedInput` have no effect. Use a matcher that includes Monitor, such as `Bash|Monitor`, to allow or rewrite. [[lines 384-392](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/hooks.md?plain=1#L384-L392)] [[Source](https://code.claude.com/docs/en/hooks#match-monitor-commands)]
* New `auth_storage_failure` Notification type (v2.1.288+): sign-in completes but credentials can't be saved. [[line 293](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/hooks.md?plain=1#L293)] [[line 2492](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/hooks.md?plain=1#L2492)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]
* `PreCompact` stdout now becomes instructions for the compaction summary (capped at 10,000 characters per hook) and is exempt from the output-file spill. [[lines 819-822](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/hooks.md?plain=1#L819-L822)] [[line 3340](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/hooks.md?plain=1#L3340)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-0)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added the `auth_storage_failure` notification matcher. [[line 183](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/hooks-guide.md?plain=1#L183)] [[Source](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)] and [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/vs-code.md)

* Claude Code v2.1.318+ doesn't install the IDE extension when `claude` starts in an integrated terminal. Until you install it, `/ide` reports "No available IDEs detected". [[ide line 821](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/ide-integrations.md?plain=1#L821)]
* An uninstalled extension returns if you run `/ide` externally or start `claude` on a version before v2.1.318. Three ways to stop that are listed. [[ide lines 1090-1099](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/ide-integrations.md?plain=1#L1090-L1099)] [[vs-code lines 1090-1099](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/vs-code.md?plain=1#L1090-L1099)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New "Subagents switch or fail without asking" section. With **Ask each time**, an Agent-tool subagent fails with `Agent terminated early due to an API error`. With **Switch automatically**, it re-runs on the fallback model. [[lines 565-577](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/model-config.md?plain=1#L565-L577)] [[Source](https://code.claude.com/docs/en/model-config#ask-before-switching)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `Grep(path)` joins `Write` and `Glob` among the path rules that are accepted but never match. A `Grep(docs/**)` deny doesn't stop searching. Use `Read(...)` or `Edit(...)` instead. [[lines 354-361](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/permissions.md?plain=1#L354-L361)] [[Source](https://code.claude.com/docs/en/permissions#writepath-globpath-and-greppath-rules-dont-match)]
* Clarified that the best-effort `Read` deny coverage is for `Read(path)` rules. [[line 337](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/permissions.md?plain=1#L337)] [[Source](https://code.claude.com/docs/en/permissions#what-read-and-edit-rules-cover)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)] and [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/web-quickstart.md)

* In cloud sessions, Auto appears unless your organization turns it off. On claude.ai/code it is grayed out until you pick a supported model. [[permission-modes line 252](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/permission-modes.md?plain=1#L252)] [[web-quickstart line 137](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/web-quickstart.md?plain=1#L137)]
* A failing setup script can leave the session started but missing what failed to install. Start a new session, or click Run now for scheduled tasks. [[web-quickstart lines 241-251](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/web-quickstart.md?plain=1#L241-L251)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* A wrapper that rebuilds the child's environment must carry over `CLAUDE_CODE_REMOTE_MCP_CONFIG`, `CLAUDE_CODE_REMOTE`, and `CLAUDE_CODE_ENVIRONMENT_KIND`. [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L45)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)]
* Split into "Pin a permission mode from your wrapper" and "Pre-approve specific tools" sections. A pinned auto mode applies only until a client such as claude.ai/code sets a mode. [[lines 827-854](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L827-L854)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#pin-a-permission-mode-from-your-wrapper)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `fastMode`: only Opus 5.5, Opus 5, and Opus 4.8 support it. `/fast` from another model switches you to Opus, and switching to an unsupported model turns it off. [[lines 445-447](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/settings-reference.md?plain=1#L445-L447)] [[Source](https://code.claude.com/docs/en/settings-reference#fastmode)]
* `autoInstallIdeExtension`: Claude Code no longer installs or updates the extension on start. Before v2.1.318 it did. [[line 5828](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/settings-reference.md?plain=1#L5828)] [[Source](https://code.claude.com/docs/en/settings-reference#autoinstallideextension)]
* `preferredNotifChannel` `"auto"` sends desktop notifications only when it detects iTerm2, Ghostty, or Kitty. [[line 4987](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/settings-reference.md?plain=1#L4987)] [[Source](https://code.claude.com/docs/en/settings-reference#preferrednotifchannel)]

#### [slack](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/slack.md) [[Source](https://code.claude.com/docs/en/slack)]

* Context gathering clarified. In threads, Claude reads your messages and its own. In channels, it reads your recent messages and its own plus the channel name, topic, and description. To share a teammate's text, paste it into the message. [[lines 89-93](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/slack.md?plain=1#L89-L93)] [[Source](https://code.claude.com/docs/en/slack#context-gathering)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Over SSH from outside tmux, set `preferredNotifChannel` to the local terminal's value so notifications reach your machine. [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/terminal-config.md?plain=1#L85)] [[Source](https://code.claude.com/docs/en/terminal-config#get-a-terminal-bell-or-notification)]
* tmux: the progress bar claim was dropped, and the sample config sends none from a pane in a window you aren't viewing. It also needs `preferredNotifChannel`. [[lines 130-139](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/claude-code/terminal-config.md?plain=1#L130-L139)] [[Source](https://code.claude.com/docs/en/terminal-config#configure-tmux)]

-----

## API changes

### Changed documents

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* The retired Claude Haiku 3.5 rows were removed from the pricing, batch, and tool-use token tables. The same removal was made in prompt caching. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/about-claude/pricing.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#model-pricing)]

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* `max_uses` now applies to a whole turn, not one request. A turn spans requests that resume after `pause_turn` or that end with only `tool_result` blocks. [[lines 309-320](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L309-L320)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#tool-parameters)]
* You can drop the advisor tool from `tools` in a follow-up request only if no advisor call is still pending. [[line 739](https://github.com/gpambrozo/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L739)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#multi-turn-conversations)]
* The "not currently available" platform caveat was removed. [[line 1983](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L1983)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool#platform-availability)]

#### [agents-and-tools/tool-use/server-tools](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/agents-and-tools/tool-use/server-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]

* Examples now set `max_tokens`. A new note explains how a mixed server and client tool response differs from `pause_turn`: send the assistant content plus a user message with only the `tool_result` blocks. [[line 495](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/agents-and-tools/tool-use/server-tools.md?plain=1#L495)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools#mixing-server-tools-and-client-tools-in-one-turn)]

#### [api/rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Rate-limit tables were reorganized and now include Claude Haiku 5.5, Sonnet 5.5, and Opus 5.5 rows. Rate limits are shared across `inference_geo` values. The page was also reworded. [[lines 119-171](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/api/rate-limits.md?plain=1#L119-L171)] [[Source](https://platform.claude.com/docs/en/api/rate-limits#cache-aware-itpm)]

#### [build-with-claude/prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* A request that reads an entry cached with a 5-minute TTL restarts its 5-minute lifetime, even if it now sets `"ttl": "1h"`. [[lines 859-863](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L859-L863)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#mixing-different-ttls)]
* Pre-warming "can reduce" the cache-miss latency. `max_tokens: 0` is preferred over `max_tokens: 1` warm-ups. [[line 1516](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L1516)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#replacing-the-max_tokens1-workaround)]
* Java examples were rewritten as unnamed-class `void main()`, and Ruby examples use `system_:`.

#### [manage-claude/user-management](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

* The note that group and custom-role requests don't need the `ce-user-management-2026-07-13` beta header was removed. The scopes explanation was rewritten. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/manage-claude/user-management.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/manage-claude/user-management#which-endpoints-can-your-organization-use)]

#### [manage-claude/wif-reference](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/manage-claude/wif-reference.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-reference)]

* Mostly editorial rewording of the Workload Identity Federation pages (reference, admin API, and the AWS, Azure, GCP, GitHub Actions, Kubernetes, Okta, and SPIFFE provider guides).

#### [managed-agents/dreams](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/managed-agents/dreams.md) [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]

* Links the "Dreaming with a dynamic workflow" cookbook recipe for building your own dream with your own prompts and models. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/managed-agents/dreams.md?plain=1#L31)] [[Source](https://platform.claude.com/docs/en/managed-agents/dreams#output_store_id-is-the-memory_store_id-of-the-completed-dreams-memory_store-output)]

#### [managed-agents/environments](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/managed-agents/environments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/environments)]

* Archiving an environment now blocks new sessions, and the "only if no sessions reference it" deletion caveat was removed. [[line 660](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/managed-agents/environments.md?plain=1#L660)] [[Source](https://platform.claude.com/docs/en/managed-agents/environments#manage-environments)]

#### [managed-agents/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/managed-agents/quickstart.md) [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart)]

* `ant` CLI install example bumped to 2.7.1, `go install` requires Go 1.26.10 or later, and the Java SDK is 3.6.0. [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/managed-agents/quickstart.md?plain=1#L84)] [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart#before-you-begin)]

#### [models/haiku-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/models/haiku-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide)]

* Claude Haiku 3.5 is now listed as retired on the Claude API, Amazon Bedrock, and Claude Models on Google Cloud (Google managed). [[line 147](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/models/haiku-5-5/migration-guide.md?plain=1#L147)] [[Source](https://platform.claude.com/docs/en/models/haiku-5-5/migration-guide#migrating-to-claude-haiku-55-from-claude-haiku-35-and-earlier-haiku-models)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* The entry on signing a Claude Enterprise member out everywhere via the Admin API (beta) was reworded. Date headings were normalized (for example "April 9th" became "April 9"). [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/082c52c713258c02f8e419e7fdd753460adeb7ef/docs-md/api/release-notes/overview.md?plain=1#L18)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-5-2026)]

#### SDK reference pages (Go, Java, Ruby)

* The Go, Java, and Ruby API reference pages under `docs-md/api/api/` (messages, batches, sessions, agents, and others) were regenerated. These are mostly formatting and example churn.
