# [Claude docs changes for November 20th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9)]

## Executive Summary
- Claude Code 2.1.329 adds the tasks, `/mcp` and `/status` improvements below. It also makes Code Mode start when telemetry is off, and it fixes many Code Mode and memory problems.
- The Code Mode docs now explain how permission modes, `ask` rules and `PreToolUse` hooks apply to code that Claude writes, and how to require approval for it.
- `claude auth status --text` shows when a stored claude.ai login ends. Claude Code warns before the login expires.
- The admin docs describe a new way to limit which GitHub accounts can be linked to a Claude organization. A new `claude plugin restore-set-aside` command restores plugin options and secrets that were set aside when an organization replaced a marketplace.
- Subagent effort levels now follow a documented order, and there is a new `CLAUDE_CODE_SUBAGENT_EFFORT` variable.

## New Claude Code versions

### [2.1.329](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/versions/2.1.329.md)

#### New features

* The trust dialog now warns where a folder's hooks are declared. A warning also appears when hooks in managed settings fail to load in non-interactive hosts.
* `/tasks` now lists this session's scheduled tasks, `/loop` wakeups, the goal and the conversation's forks. Pressing x stops one after asking.
* `/mcp` has a "Server message" row that shows the JSON-RPC error from a remote HTTP MCP server that refuses the connection.
* `/status` has a "Marketplace auto-update" row that names managed marketplaces that get no automatic updates, and why.
* Code Mode can now be turned on while OpenTelemetry events and metrics are enabled. Each tool call the code makes sends its events. Tracing still keeps it off.
* VS Code: after you decline the trust prompt, a line above the message box offers "Review trust" to bring the prompt back.

#### Existing feature improvements

* Code Mode now also starts when telemetry, nonessential traffic or feature flags are off. An administrator can keep it off in managed settings.
* A `PreToolUse` hook that errors no longer refuses a Code Mode script's tool call, as outside Code Mode. Set `"onFailure": "block"` on a hook that must refuse.
* Code Mode scripts can now declare their own `log`, `preview` or `sleep`. The terminal freezes for far less time after thousands of tool calls.
* Code Mode now waits up to ten minutes on long MCP calls and then returns an error, instead of passing "moved to the background" through as data.
* Code Mode refuses reads of a line range over 256 MiB.
* `/code-review` with no target now reviews the whole branch against the default branch. `/code-review <pr number>` reads the pull request with `gh pr diff` and stops if that fails.
* The `/tasks` header and the footer's background count are now one number covering shells, monitors, MCP calls, agents, workflows and scheduled tasks.
* Stop and SubagentStop hooks list a Monitor's script as `monitor` rather than `shell` in `background_tasks`.
* Memory use is better in long sessions, in idle Claude Desktop and SDK sessions, and after `--resume` or `--continue`.
* Auto mode runs `git status` less often. It also handles a short reply such as "yes" better when telemetry is off or behind a gateway.
* Cloud sessions retry plugins that failed to download at startup.
* Saved scheduled tasks: in new signed-in sessions, most tasks saved by earlier versions need scheduling again. `--resume` of their own session still runs them.
* Removed 2.1.326's automatic retry at the limit named in a `max_tokens` error. Behind a gateway, set `CLAUDE_CODE_MAX_OUTPUT_TOKENS`.
* Self-hosted runner and gateway: changes to clone folders, `--repository-folder` behavior, and the `access_control.allow_cidrs` startup notice.
* Computer use on macOS follows newer safety rules, so some actions are refused and some apps have less access.

#### Major bug fixes

* Fixed `~/.claude.json` being reset to defaults after a network stall or file lock made it unreadable.
* Fixed repeated sign-outs on macOS when Claude Code could read the Keychain but not save to it.
* Fixed `/terminal-setup` corrupting VS Code settings or keybindings files.
* Fixed files accepted through the IDE diff losing their last newline or BOM.
* Fixed `/teleport` replacing the open conversation. It now starts a new session.
* Fixed `/usage` and `/usage-credits` problems for Pro and Max users.
* Fixed a status line script with endless output freezing the prompt and using gigabytes of memory.
* Fixed an MCP server being signed in again after its authentication was cleared.
* Fixed PDFs, images and Office files sent as `application/octet-stream` being saved as `.bin`.
* Fixed a runaway Code Mode loop filling the machine's memory. It is now stopped at a limit.
* Fixed a background agent that kept running after being stopped while it was resumed.
* Fixed `claude mcp login` and `/mcp` wrongly saying a service doesn't accept sign-ins when its client registration was retired (HTTP 410).
* Fixed auto mode asking for approval to `rm` a symlink that points outside the working directory.
* Fixed many terminal UI problems, including fullscreen cut-offs, key hints ignoring `keybindings.json`, and prompt text corruption.
* Many VS Code fixes, including IME handling, drag-and-drop of folders, and permission prompt focus.

-----

## Claude Code changes

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* New section "Limit which GitHub accounts can be linked". It lets admins allow only approved github.com organizations and accounts, and turn on "Only allowed accounts can be linked". [[lines 145-174](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/admin-setup.md?plain=1#L145-L174)] [[Source](https://code.claude.com/docs/en/admin-setup#limit-which-github-accounts-can-be-linked)]
* Unlinking an account no longer always relinks it. It is relinked only unless the allow list is used. [[lines 130-142](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/admin-setup.md?plain=1#L130-L142)] [[Source](https://code.claude.com/docs/en/admin-setup#connected-github-accounts)]

#### [authentication](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* New section "Check when a stored login ends". `claude auth status --text` shows a `Sign-in ends` line (v2.1.318 or later). `claude -p` warns on stderr when the end is under 10 days away. Claude Code shows a startup warning from the earlier end date. [[lines 228-239](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/authentication.md?plain=1#L228-L239)] [[Source](https://code.claude.com/docs/en/authentication#check-when-a-stored-login-ends)]

#### [code-mode](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/code-mode.md) [[Source](https://code.claude.com/docs/en/code-mode)]

* Expanded permissions explanation. In auto and `bypassPermissions` modes code can run without prompts. Each tool call still goes through `deny` and `ask` rules and `PreToolUse` hooks. In auto mode the classifier reviews the code, not each call. [[lines 147-155](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/code-mode.md?plain=1#L147-L155)] [[Source](https://code.claude.com/docs/en/code-mode#permission-checks)]
* New sections on requiring approval for a command with an `ask` rule, approving each piece of code first with an `ask` rule for `REPL`, and answering a permission prompt while code runs. [[lines 162-205](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/code-mode.md?plain=1#L162-L205)] [[Source](https://code.claude.com/docs/en/code-mode#require-approval-for-a-command)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_DISABLE_DEFERRED_TOOL_RESUME`. [[line 249](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/env-vars.md?plain=1#L249)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added `CLAUDE_CODE_LOOP_KEEPALIVE` for self-paced `/loop`. [[line 327](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/env-vars.md?plain=1#L327)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added `CLAUDE_CODE_SUBAGENT_EFFORT` and `CLAUDE_CODE_SUBAGENT_HISTORY`. [[lines 411-412](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/env-vars.md?plain=1#L411-L412)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_DISABLE_THINKING` now also covers subagent turns and the compaction summary. [[line 278](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/env-vars.md?plain=1#L278)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries: usage credits running out mid-response, `Session failed: program not found:`, `Warning: this sign-in`, the `CLAUDE_CODE_OAUTH_REFRESH_TOKEN` refusal, cloud-session `ENOTFOUND`, organization effort limits, the Zed keymap symlink, and managed marketplace errors. [[lines 45-363](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/errors.md?plain=1#L45-L363)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* Remote Control reconnect errors now link to the Remote Control troubleshooting page. [[line 168](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/errors.md?plain=1#L168)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* MCP tool hooks accept an `onFailure` field (`continue` or `block`). [[line 546](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/hooks.md?plain=1#L546)] [[Source](https://code.claude.com/docs/en/hooks#mcp-tool-hook-fields)]
* Clarified the "Block the action when a hook fails" section and added a pointer to Agent SDK callback hooks. [[lines 936-940](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/hooks.md?plain=1#L936-L940)] [[Source](https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* The CLI accepts `manual` as an alias for `default`, for example `--permission-mode manual`. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/permission-modes.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]
* The `default` mode description now says which actions need no approval. The list of calls denied in `dontAsk` mode was expanded. [[lines 649-655](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/permission-modes.md?plain=1#L649-L655)] [[Source](https://code.claude.com/docs/en/permission-modes#allow-only-pre-approved-tools-with-dontask-mode)]

#### [plugins/cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/plugins/cli-reference.md) [[Source](https://code.claude.com/docs/en/plugins/cli-reference)]

* New `claude plugin restore-set-aside` command, with a `--discard` flag. It restores or deletes options and secrets set aside when an organization replaced a plugin marketplace. [[lines 418-433](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/plugins/cli-reference.md?plain=1#L418-L433)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#plugin-restore-set-aside)]
* In a terminal, success lines no longer include "Successfully". They keep it when output isn't a terminal. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/plugins/cli-reference.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/plugins/cli-reference#claude-plugin-commands)]

#### [plugins/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/plugins/troubleshooting.md) [[Source](https://code.claude.com/docs/en/plugins/troubleshooting)]

* Expanded the archive `sha256` mismatch explanation with likely causes. [[lines 421-428](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L421-L428)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#plugin-archive-integrity-check-failed)]
* Updated the success messages shown in a terminal. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#plugin-isnt-available-in-this-environment)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* The auto-connect values are now `on` and `off`. [[lines 201-202](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/remote-control.md?plain=1#L201-L202)] [[Source](https://code.claude.com/docs/en/remote-control#enable-remote-control-for-all-sessions)]
* Documented the `Session failed: program not found:` error and what happens when a previous session is gone on reconnect. [[lines 529-545](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/remote-control.md?plain=1#L529-L545)] [[Source](https://code.claude.com/docs/en/remote-control#the-program-file-this-remote-control-started-from-is-gone)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Notes that retries in auto mode work differently under Code Mode. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sandboxing.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/sandboxing#the-unsandboxed-retry-escape-hatch)]
* A newer `objects` or `refs` folder is now renamed to `<name>.claude-sandbox-quarantine-<hex>` instead of being deleted. [[line 570](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sandboxing.md?plain=1#L570)] [[Source](https://code.claude.com/docs/en/sandboxing#when-the-sandbox-deletes-head-objects-or-refs)]
* New troubleshooting section on usernames and passwords in proxy variables: the `srt` username on `127.0.0.1` or `localhost` is the sandbox proxy's own login. [[lines 652-658](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sandboxing.md?plain=1#L652-L658)] [[Source](https://code.claude.com/docs/en/sandboxing#usernames-and-passwords-in-proxy-variables)]

#### [sessions](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* Resuming does not carry over `--tools`, `--allowedTools` and `--disallowedTools`, so pass them again. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sessions.md?plain=1#L67)] [[Source](https://code.claude.com/docs/en/sessions#flags-to-pass-again-when-you-resume)]
* The resume picker no longer documents the grouped-session expand/collapse keys or the `1` to `9` shortcuts. [[lines 185-197](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sessions.md?plain=1#L185-L197)] [[Source](https://code.claude.com/docs/en/sessions#use-the-session-picker)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Documented the order that sets a subagent's effort: `CLAUDE_CODE_EFFORT_LEVEL`, then the spawning agent's or turn's effort, then `CLAUDE_CODE_SUBAGENT_EFFORT`. [[lines 430-437](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sub-agents.md?plain=1#L430-L437)] [[Source](https://code.claude.com/docs/en/sub-agents#when-a-subagent-has-no-effort-field-or-parameter)]
* A first agent file in a new `agents` directory no longer needs a restart. Added `propose_skills` to the list of subagent tools. [[line 244](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/sub-agents.md?plain=1#L244)] [[Source](https://code.claude.com/docs/en/sub-agents#write-subagent-files)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* The `disableRemotePreviewScripts` setting is now described as applying to the Browser pane. The SSH connection form was updated, and the name is now optional. [[lines 1035-1042](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/desktop.md?plain=1#L1035-L1042)] [[Source](https://code.claude.com/docs/en/desktop#ssh-sessions)]
* Computer use tier "Full control" was renamed "Full access". [[line 434](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/claude-code/desktop.md?plain=1#L434)] [[Source](https://code.claude.com/docs/en/desktop#app-permissions)]

-----

## API changes

### Changed documents

#### [cli-sdks-libraries/overview](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/api/cli-sdks-libraries/overview.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)]

* Current SDK versions bumped, for example `ant` CLI 2.12.1 and Java SDK 3.12.0. The install snippets in the quickstarts and cloud-provider pages were updated to match. [[lines 59-66](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/api/cli-sdks-libraries/overview.md?plain=1#L59-L66)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview#latest-versions)]

#### [test-and-evaluate/strengthen-guardrails/reduce-latency](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-latency.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency)]

* Added a Claude Cookbook latency-optimization notebook and the `/claude-api latency-optimize` skill command. [[lines 233-248](https://github.com/gpambrozio/ClaudeDocs/blob/a5c05bbd011f768cf47f127d3c66fe0b40f74dc9/docs-md/api/test-and-evaluate/strengthen-guardrails/reduce-latency.md?plain=1#L233-L248)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency#next-steps)]
