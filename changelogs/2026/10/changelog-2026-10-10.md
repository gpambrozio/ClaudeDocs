# [Claude docs changes for October 10th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/528985d6bf3f7f572f3ec8df91bcf0f277720677) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/528985d6bf3f7f572f3ec8df91bcf0f277720677)]

## Executive Summary
- Claude Code 2.1.296 adds a `code` key to Claude apps gateway policies (also applied in Claude Desktop's Code tab), `autoCompactWindow` for subagents, and new environment variables for workflow subagent models and overloaded-retry delays
- Hooks now have an `onFailure: "block"` option so a crashing, missing, or timed-out policy hook blocks the action instead of letting it through, and the hooks reference documents exit codes and stdout combinations in detail
- The Managed Agents API reference gains a new `multiagent_20261001` configuration (separately enabled advisor, subagents, and workflows) and full workflow run event types
- The Agent SDK exposes a structured `usage_report` (`SDKUsageReport`) for `/usage`, and mods can call models directly with `$.model.complete` / `$.model.fork`, including prompt caching
- New guidance on the output-token cost of `drop_block` in preserved thinking (up to +67% at max effort), and a Compliance API addition for downloading Claude Docs documents

## New Claude Code versions

### [2.1.296](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/versions/2.1.296.md)

#### New features

* Added a `code` key to the Claude apps gateway's `managed.policies[]`: same settings as `cli`, also applied in Claude Desktop's Code tab
* Added `autoCompactWindow` to subagent frontmatter and `--agents` definitions
* Added `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` to run every workflow agent on one model
* Added `CLAUDE_CODE_OVERLOADED_RETRY_MAX_DELAY_MS` to set a longer maximum backoff for overloaded (529) retries
* Added an `allow_large` option to the Read tool for reading a whole large text file in one call
* Added a `/plugin` note when a plugin's hooks are left out because another enabled plugin has the same name
* [Cloud sessions] Added a status filter to the Sessions and Runners lists on a self-hosted environment's Activity tab
* [Claude Tag] Added creating, editing and deleting workspace and channel memory files on the Activity page's Memory tab

#### Existing feature improvements

* Fullscreen mode underlines the link under the mouse pointer
* Faster transcript toggle (ctrl+o) in code-heavy conversations via cached syntax highlighting
* `--debug` now names unrecognized frontmatter fields in custom agent files and logs command hook command, plugin, outcome and duration
* Auto mode shows a dim "Not run" row instead of a red error when its check had no usable answer
* Clearer errors for refused cloud sessions and in Code Review admin settings
* Sonnet 5.5 cache reads now priced at $0.10 per million tokens (was $0.20) in `/cost`, status line, `--max-budget-usd` and SDK cost figures
* Default limit on MCP tool descriptions and server instructions raised from 2,048 to 4,096 characters
* `←` now stops a turn or `!` command started while the session moves to the background
* [VSCode] Claude in Chrome now asks before browser actions in every session, including `@browser`

#### Major bug fixes

* Fixed managed-settings `PreToolUse` hooks denying with `"continue": false` and managed `prompt` hooks not ending the turn, and PostToolUse hooks not applying `updatedMCPToolOutput`
* Fixed Bash permission checks auto-approving some commands that use `BASH_ARGV0`
* Fixed Edit and NotebookEdit corrupting non-UTF-8 files (Windows-1252, Shift-JIS, GBK); such edits are now refused
* Fixed a saved Claude apps gateway sign-in being ignored when `forceLoginMethod` is `gateway` with no `forceLoginGatewayUrl` (regression in 2.1.295)
* Fixed headless sessions starting MCP servers that were switched off for the folder
* Fixed Esc/interrupt during `UserPromptSubmit` hooks ending headless sessions or letting the unchecked prompt through
* Fixed `/code-review` ending on a raw JSON array in cloud sessions, the Agent SDK and IDE integrations
* Fixed `$.agent.register` succeeding from a stale mod hook after reload or removal
* Fixed secret redaction missing some values in shared transcripts and debug logs
* Windows: Fixed long PowerShell commands always prompting, stdio MCP servers being force-killed at shutdown, and `plugin install` failing for GitHub sources without an SSH key

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `usage_report` on `SDKAssistantMessage` and a new `SDKUsageReport` type: a structured copy of the `/usage` report (session cost totals, rate-limit meters, extra usage), experimental, requires Agent SDK v0.3.273+. [[line 1435](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1435)] [[lines 2060-2130](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2060-L2130)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkassistantmessage)]
* Documented size limits for `pasted_content` (1,000 entries) and `inline_pastes` (first 100 non-blank). [[lines 1470-1474](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1470-L1474)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkusermessage)]
* Interrupted-turn wording changed from "re-run" to "continues" for `CLAUDE_CODE_RESUME_INTERRUPTED_TURN` and `resume_reason`. [[line 1691](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1691)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#resume_reason)]
* Added `reason: "worker_restart"` to `SDKTaskNotificationMessage`. [[line 5188](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L5188)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdktasknotificationmessage)]
* Workflow `scriptPath` is rejected when the session's tools don't include `Read`. [[line 3240](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L3240)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#workflow)]

#### [chrome](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* VS Code sessions show browser-action permission prompts as chat cards, with an option to allow the site. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/chrome.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/chrome#permission-prompts-in-vs-code-sessions)]
* Uploads: Claude refuses credential-named files (`.env`, `.pem`, `.key`, `.ssh`), v2.1.293+. [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/chrome.md?plain=1#L171)] [[Source](https://code.claude.com/docs/en/chrome#upload-files-to-web-pages)]
* New troubleshooting: project settings can't turn on Chrome via `CLAUDE_CODE_ENABLE_CFC`, extension signed in to a different organization, and `/chrome` "Reconnect extension". [[lines 260-290](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/chrome.md?plain=1#L260-L290)] [[Source](https://code.claude.com/docs/en/chrome#project-settings-cant-turn-on-chrome)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New `code` policy key (recommended) versus legacy `cli`; requires v2.1.296+ gateway and can't be mixed with `cli`/`settings` in one file. [[lines 891-920](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L891-L920)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#choose-cli-or-code)]
* New section on applying `code` settings in Claude Desktop's Code tab (requirements: `desktop` key, Desktop 2.9939.2+, client-side managed settings, HTTPS on a private network). [[lines 1047-1070](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1047-L1070)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#settings-the-gateway-derives-for-claude-desktop)]
* Telemetry: user identity attributes stamped from the gateway JWT, and handling `user.groups` changes during an open session. [[line 1180](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1180)] [[lines 1286-1303](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1286-L1303)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#telemetry)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_ENABLE_CFC` to start a CLI session with Chrome integration on or off. [[line 280](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/env-vars.md?plain=1#L280)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Installation errors section moved to troubleshoot-install; index links updated. [[line 184](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/errors.md?plain=1#L184)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New entries: "Claude Code couldn't restart", invalid marketplace name, settings file that "does not load", "Plugin directory does not exist", and a `/loop` wakeup missed after restart. [[line 3610](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/errors.md?plain=1#L3610)] [[Source](https://code.claude.com/docs/en/errors#cannot-switch-renderers-in-this-session)]
* Added `CLAUDE_CODE_RETRY_WATCHDOG_MAX_WAIT_MS` retry variable. [[line 430](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/errors.md?plain=1#L430)] [[Source](https://code.claude.com/docs/en/errors#tune-retry-behavior)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `onFailure` field (`"continue"` or `"block"`) for command and HTTP hooks, v2.1.295+, with a new section "Block the action when a hook fails". [[line 443](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md?plain=1#L443)] [[lines 850-899](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md?plain=1#L850-L899)] [[Source](https://code.claude.com/docs/en/hooks#command-hook-fields)]
* Rewrote exit code output: success, blocking, and non-blocking outcomes, with a table by stdout type and exit code plus per-event exceptions. [[lines 754-776](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md?plain=1#L754-L776)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-output)]
* Exit 2 blocks even when JSON is printed; "allow" cannot override it. [[lines 796-803](https://github.com/gpambrozo/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md?plain=1#L796-L803)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2)]
* A timed-out `command`, `http`, or `mcp_tool` hook doesn't block the tool call. [[line 847](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md?plain=1#L847)] [[Source](https://code.claude.com/docs/en/hooks#timeouts)]
* HTTP hooks: a non-2xx status is a non-blocking error; block via a 2xx response body. [[line 953](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md?plain=1#L953)] [[Source](https://code.claude.com/docs/en/hooks#http-response-handling)]
* PermissionRequest hook exiting 2 without a `decision` leaves the flow unchanged; TaskCreated can block via exit 2 or JSON. [[line 2010](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md?plain=1#L2010)] [[line 2518](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks.md?plain=1#L2518)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-decision-control)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New "Check what a hook did" section describing how success and errors appear in the transcript. [[lines 1027-1038](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks-guide.md?plain=1#L1027-L1038)] [[Source](https://code.claude.com/docs/en/hooks-guide#check-what-a-hook-did)]
* HTTP hook response status handling and `onFailure: "block"`. [[line 916](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/hooks-guide.md?plain=1#L916)] [[Source](https://code.claude.com/docs/en/hooks-guide#http-hooks)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Vim mode: documented `f`/`F`/`t`/`T` character jumps and `df`/`dt` deletes. [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/interactive-mode.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/interactive-mode#navigation-normal-mode)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Documented `claude mcp login <name>` to run a server's OAuth flow from the shell. [[line 786](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/mcp.md?plain=1#L786)] [[Source](https://code.claude.com/docs/en/mcp#authenticate-from-the-command-line)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Mention-resolution events capped at 100 per prompt for `agent` and `mcp_resource`. [[line 1087](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/monitoring-usage.md?plain=1#L1087)] [[Source](https://code.claude.com/docs/en/monitoring-usage#at-mention-event)]

#### [plugins/mods/api](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* New docs for mods calling models: `$.model.complete` versus `$.model.fork`, request contents comparison, sending one prompt, and prompt caching with `cache: true` blocks (v2.1.292+). [[lines 68-166](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/plugins/mods/api.md?plain=1#L68-L166)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#call-a-model)]

#### [plugins/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/plugins/troubleshooting.md) [[Source](https://code.claude.com/docs/en/plugins/troubleshooting)]

* New sections: invalid marketplace name, "does not load, so Claude Code ignores the whole file", and "Plugin directory does not exist". [[line 230](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L230)] [[line 786](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L786)] [[line 898](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L898)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#add-a-marketplace)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New section "Authorize a connector again from your shell" using `claude mcp login "<connector>" --no-browser` and `/mcp reconnect`. [[lines 347-375](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/remote-control.md?plain=1#L347-L375)] [[Source](https://code.claude.com/docs/en/remote-control#authorize-a-connector-again-from-your-shell)]

#### [scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Explained recurring-task jitter: a fixed per-task delay up to 30 minutes (table by frequency), and one-shot tasks at `:00`/`:30` running up to 90 seconds early. [[lines 164-182](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/scheduled-tasks.md?plain=1#L164-L182)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#jitter)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New wrapper environment variables: `CCR_SESSION_ACCOUNT_EMAIL`, `CLAUDE_RUNNER_CLIENT_PLATFORM`, `CLAUDE_CODE_REMOTE_SLACK_THREAD_URL`/`_TS`, with guidance on defaults and quoting. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L26)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)]
* Warning that backgrounding the child with a bare `&` severs stdin and breaks the session after ~30 minutes; fd 3 and stderr handling. [[lines 55-69](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L55-L69)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#keep-stdin-and-file-descriptor-3-attached)]
* Checkout hook: `CLAUDE_RUNNER_REPO_REF`, `.git` verification, getting git credentials, and failure behavior by repository type. [[lines 109-140](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L109-L140)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#checkout)]
* Session-end hook statuses `completed` and `interrupted` detailed. [[lines 163-174](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L163-L174)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#post-session)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* Absorbed the installation error sections (install killed by OOM, connection dropped while downloading) moved from the errors page.

-----

## API changes

### Changed documents

#### [api/beta/agents](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/api/beta/agents.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents)]

* New `multiagent_20261001` configuration with independently enabled `advisor`, subagents (`predefined_agents`), and `workflows` members, merged level by level on update. The same change appears in the Go, Python, TypeScript, Ruby, Java, C#, CLI and PHP SDK references. [[lines 29-140](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/api/beta/agents.md?plain=1#L29-L140)] [[Source](https://platform.claude.com/docs/en/api/beta/agents#headers)]
* The existing `coordinator` topology is now documented as `BetaManagedAgentsMultiagentCoordinatorParams`.

#### [api/beta/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/api/beta/sessions.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions)]

* Large regeneration of the Managed Agents sessions, events, threads and thread events references (all SDK languages and CLI), adding workflow run events (created, phase started/ended, status running/idle/ended, errors and results), inline agent and session thread types, and session refusal and retries-exhausted stop details.

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* New section "Output-token cost of `drop_block`": output tokens rose 2.5%-20.1% when dropping once per session and 4.6%-67.1% when dropping on every turn (low to max effort). Recommends running your own evals and fixing the prefix edit. [[lines 99-131](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L99-L131)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#what-the-api-does-with-an-invalid-block)]

#### [manage-claude/compliance-content-data](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/manage-claude/compliance-content-data.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data)]

* Claude Docs documents are listed via List code artifacts with `artifact_type` `claude_docs`, and downloaded as a ZIP using `multi_file_format=zip`. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/manage-claude/compliance-content-data.md?plain=1#L209)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-content-data#retrieve-files-and-artifacts)]

#### [manage-claude/user-management](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

* Custom roles: read the name from `display_name`; the `name` field is deprecated and equal to it. Store the role `id` for lasting references. [[line 435](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/manage-claude/user-management.md?plain=1#L435)] [[Source](https://platform.claude.com/docs/en/manage-claude/user-management#custom-roles)]

#### [managed-agents/budgets](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/managed-agents/budgets.md) [[Source](https://platform.claude.com/docs/en/managed-agents/budgets)]

* A `user.interrupt` can pause open workflow runs, and a run paused by an interrupt does not resume when the budget changes; send a `user.message` asking the agent to continue its runs. The same clarification is in events-and-streaming, multiagent-orchestration and workflow-runs. [[lines 188-196](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/managed-agents/budgets.md?plain=1#L188-L196)] [[Source](https://platform.claude.com/docs/en/managed-agents/budgets#events-accepted-at-the-cap)]

#### [managed-agents/session-threads](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/managed-agents/session-threads.md) [[Source](https://platform.claude.com/docs/en/managed-agents/session-threads)]

* C# examples updated; `from_agent_name` is now described as absent rather than `null` for workflow prompts. [[line 405](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/managed-agents/session-threads.md?plain=1#L405)] [[Source](https://platform.claude.com/docs/en/managed-agents/session-threads#session-thread-events)]

#### [managed-agents/workflow-runs](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/managed-agents/workflow-runs.md) [[Source](https://platform.claude.com/docs/en/managed-agents/workflow-runs)]

* A paused run's lifetime keeps passing, so it can end with `timeout_error` while paused. [[line 758](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/managed-agents/workflow-runs.md?plain=1#L758)] [[Source](https://platform.claude.com/docs/en/managed-agents/workflow-runs#interrupt-a-session-with-runs-open)]

#### [models/fable-5-1/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/models/fable-5-1/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)]

* Checklist now says responses can start with `thinking` blocks (select content by `type`), and notes thinking tokens bill as output tokens. [[lines 1582-1588](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/models/fable-5-1/migration-guide.md?plain=1#L1582-L1588)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide#migration-checklist)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* New entry: the Compliance API can download Claude Docs documents as Word files, in beta. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/528985d6bf3f7f572f3ec8df91bcf0f277720677/docs-md/api/release-notes/overview.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-8-2026)]
