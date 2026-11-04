# [Claude docs changes for November 4th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/3f37ab9a8b405571f1ca931c2b686f2a23ae8508) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/3f37ab9a8b405571f1ca931c2b686f2a23ae8508)]

## Executive Summary
- Claude Code 2.1.318 hardens `~/.claude.json` and login storage on shared network home directories, and adds login-expiry reporting to `claude auth status` and `claude -p`.
- The Agent SDK and command/http hooks gain `onFailure: "block"`, so a crashing or timed-out policy hook can block an action instead of letting it through.
- Anthropic's text watermark is documented (new page), including the Sonnet 4.6 caveat for non-default `temperature`/`top_p`/`top_k`.
- The API docs now show `anthropic-version: 2026-10-21` in Managed Agents and compaction examples. Compaction can also return a `null` summary, and the sample code was updated to handle that.
- The Agent SDK permissions docs were rewritten to explain how hooks, deny rules, `bypassPermissions` and `plan` mode interact. New docs also cover Windows SSH host commands in Desktop and a sandbox AppArmor/bubblewrap fix.

## New Claude Code versions

### [2.1.318](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/versions/2.1.318.md)

#### New features

* `assume_role` on `mantle` upstreams of the Claude apps gateway, for roles in another AWS account and per-developer cost attribution
* `effort` option on a mod's `$.model.fork`
* `claude auth status` (`loginExpiresAt`) and `claude -p` JSON results (`credential_expires_at`) report when a stored claude.ai sign-in ends. `claude -p` text output warns on stderr 10 days beforehand
* Cloud sessions: "No repository" option, Chrome names (`google-chrome`, `CHROME_PATH`) for the built-in Chromium, and a New session button when the environment was deleted
* Self-hosted runner: `CLAUDE_RUNNER_SPAWN_REASON` in the spawn-runner hook environment

#### Existing feature improvements

* `~/.claude.json`, settings files and the stored login survive saves on shared network home directories much better, and sessions re-check when the config is wrongly reported missing
* Unattended runs (`claude -p`, SDK) no longer rewrite `~/.claude.json` when nothing changed
* MCP tool errors for a call made before the tool is loaded now return the input schema
* More reliable git commits and PR creation under macOS `/bin/bash`; clearer Create PR failure messages in cloud and Remote Control sessions
* Faster remote session reconnects after sleep; auto-update retries brief network failures right away
* Changed: Claude Code no longer installs or updates the IDE extension when started in an IDE terminal (use `/ide` from an outside terminal)
* Changed: background subagents move shell commands to the background after 3 minutes on all providers
* Changed: `deniedMcpServers` URL entries also block matching Anthropic-provided servers and connectors in cloud sessions and on self-hosted runners
* Changed: `/claude-api managed-agents-onboard` defaults new agents' built-in tools and quickstart MCP tools to the `auto` permission policy
* Changed: what a mod attaches at `prompt.submit` stays in the user's turn instead of going out as a system message
* Changed: subagents stop instead of switching models when "Switch models when a message is flagged" is "Ask each time"

#### Major bug fixes

* Fixed `--continue` losing earlier conversation after a malformed tool call's retries ran out (regression in 2.1.314)
* Fixed `/logout`, `claude auth logout` and `claude mcp remove` silently failing, and settings being dropped, on shared network home directories
* Fixed `claude mcp add`/`remove` writing config without a lock
* Fixed non-interactive launches replacing an invalid `~/.claude.json` with defaults; the start now fails with restore instructions
* Fixed jobs exiting with `Not logged in` when another terminal or host signs in to the same account
* Fixed every connection failing when the `NODE_EXTRA_CA_CERTS` file is empty, not PEM, or starts with a damaged certificate
* Fixed permission prompts being answered by keys typed just after sending a message
* Fixed macOS sessions with many running Bash commands stalling while memory grew
* Fixed `claude remote-control` hosts, the daemon and self-hosted runners failing with `spawn ENOENT` after an update removed a running binary
* Fixed version cleanup deleting the binary of a process owned by another user
* Fixed idle compaction replacing a conversation with a non-summary reply
* Fixed `claude -p`/SDK sessions reporting success when an API error cut off a reply while a mod hooked `turn.step`

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Minor wording updates only.

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* New `onFailure` matcher option (`on_failure` in Python) with `"block"` to block the action when a hook callback throws or fails validation. It requires TypeScript SDK v0.3.317+ or Python SDK v0.2.177+. [[line 220](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L220)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#matchers)]
* New section "Block the action when a callback fails", with examples, how to test it, and the events that behave differently (`Stop`, `SubagentStop`, `TaskCompleted`, `TeammateIdle`, `PermissionRequest`, `PostToolUse`). It also covers startup errors for `onFailure`. [[lines 280-326](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L280-L326)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#block-the-action-when-a-callback-fails)]
* Hook timeouts on `PreCompact`, `Elicitation` and `WorktreeCreate` also block when `onFailure: "block"` is set. [[line 816](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L816)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#hook-timeout)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* The permission evaluation order was rewritten. A hook returning `allow` doesn't skip deny and ask rules, and deny rules apply even in `bypassPermissions`. Tools that require user interaction always reach `canUseTool`. [[lines 13-45](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L13-L45)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)]
* Warning that `allowed_tools` does not constrain `bypassPermissions`. Use `disallowed_tools` to block specific tools. [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L123)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)]
* New "Path patterns in rules" section: `Edit(path)` covers Write and NotebookEdit, `//path` means absolute and `/path` is relative to the working directory. [[lines 129-141](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L129-L141)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)]
* Plan mode documentation expanded: edits reach `canUseTool`, and with auto mode available, shell commands, web fetches and searches go to the classifier (`useAutoModeDuringPlan`). A table shows which calls reach the callback. [[lines 310-347](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L310-L347)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#bypass-permissions-mode-bypasspermissions)]
* `acceptEdits` clarified: protected paths aren't auto-approved, and the working directory plus added directories are covered. [[line 280](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L280)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#accept-edits-mode-acceptedits)]

#### [agent-sdk/secure-deployment](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/secure-deployment.md) [[Source](https://code.claude.com/docs/en/agent-sdk/secure-deployment)]

* Added notes on critical-path removals and Bash rule limitations. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/secure-deployment.md?plain=1#L21)] [[Source](https://code.claude.com/docs/en/agent-sdk/secure-deployment#built-in-security-features)]
* Sandbox runtime network behavior was described, along with the lack of TLS inspection (domain fronting) and a warning about credentials for allowed domains. [[lines 82-95](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/secure-deployment.md?plain=1#L82-L95)] [[Source](https://code.claude.com/docs/en/agent-sdk/secure-deployment#sandbox-runtime)]
* Docker `--network none` section now explains how to run a host proxy through a mounted Unix socket for allowlists and credential injection. [[lines 132-147](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/secure-deployment.md?plain=1#L132-L147)] [[Source](https://code.claude.com/docs/en/agent-sdk/secure-deployment#containers)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)] and [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-sdk/typescript.md)

* Reference updates for the new `on_failure` / `onFailure` hook matcher option and related message types.

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Teammates on the lead's model inherit the lead's effort level (split-pane from v2.1.186). [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-teams.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/agent-teams#specify-teammates-and-models)]
* Plan approval: when a teammate whose permission mode hasn't changed finishes planning, the plan is approved automatically on arrival. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-teams.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/agent-teams#have-teammates-plan-before-implementing)]
* Cycling a teammate's permission mode with Shift+Tab. In-process teammates may run in the lead's mode, and per-teammate modes can't be set at spawn. [[lines 287-295](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-teams.md?plain=1#L287-L295)] [[Source](https://code.claude.com/docs/en/agent-teams#permissions)]
* New limitation listed: no per-teammate permission modes at spawn. [[line 495](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/agent-teams.md?plain=1#L495)] [[Source](https://code.claude.com/docs/en/agent-teams#limitations)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* `assume_role` is now supported on `mantle` upstreams. It requires SigV4 credentials and isn't allowed with `aws_bearer_token`. [[lines 493-565](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L493-L565)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#bedrock-in-another-aws-account)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)] / [memory](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/memory.md)

* Use `/context all` and check **Memory files** to confirm CLAUDE.md loaded. `/memory` also lists CLAUDE.md locations that don't exist yet. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/memory.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/memory#set-up-a-project-claudemd)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)] / [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/desktop-changelog.md)

* SSH host commands now work on Windows, with a new "Write the command on Windows" section covering full `.exe`/`.cmd`/`.bat` paths and quoting. It includes a batch-file wrapper example. [[lines 1684-1729](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/desktop-changelog.md?plain=1#L1684-L1729)] [[Source](https://code.claude.com/docs/en/desktop-changelog#write-the-command-on-windows)]
* Version requirements for connections from a command: Desktop v3.6556.0+ on macOS/Linux and v4.16336.0+ on Windows. Quoted paths with spaces also need v4.16336.0+. [[line 1601](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/desktop-changelog.md?plain=1#L1601)] [[Source](https://code.claude.com/docs/en/desktop-changelog#create-an-ssh-connection-from-a-command)]
* Host key verification guidance, `sshHostCommands` managed-settings rollout advice (per-platform entries), and new reasons an entry is unavailable. [[lines 1734-1820](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/desktop-changelog.md?plain=1#L1734-L1820)] [[Source](https://code.claude.com/docs/en/desktop-changelog#connect-to-a-new-host)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_BG_STABLE_PATH` (macOS) to run background session hosts from the installed binary. [[line 237](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/env-vars.md?plain=1#L237)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_IDE_SKIP_AUTO_INSTALL` to stop `/ide` from installing the IDE extension. [[line 312](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/env-vars.md?plain=1#L312)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries for "Scheduled tasks/Routines are off for your organization" and the org toggle that controls them. [[line 1210](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/errors.md?plain=1#L1210)] [[Source](https://code.claude.com/docs/en/errors#scheduled-tasks-are-off-for-your-organization)]
* New remote managed settings messages (fail-closed, still loading, did not load) and how they show in the Desktop Code tab. [[line 5822](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/errors.md?plain=1#L5822)] [[Source](https://code.claude.com/docs/en/errors#remote-managed-settings-failed-to-load)]
* New auto mode denial "a hook changed this call's input after auto mode reviewed it", with remedies. [[lines 781-795](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/errors.md?plain=1#L781-L795)] [[Source](https://code.claude.com/docs/en/errors#a-hook-changed-this-calls-input-after-auto-mode-reviewed-it)]
* New Ubuntu AppArmor / bubblewrap sandbox errors with links to the fix. [[line 456](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/errors.md?plain=1#L456)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `"onFailure": "block"` for `command` and `http` hooks, so a failing or timed-out policy hook blocks the action. [[line 900](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/hooks.md?plain=1#L900)] [[Source](https://code.claude.com/docs/en/hooks#block-the-action-when-a-hook-fails)]
* `updatedInput` now replaces the whole input and is re-evaluated against permission rules. In auto mode, changing input after review can cause a denial. [[lines 1959-2002](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/hooks.md?plain=1#L1959-L2002)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)] / [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/vs-code.md)

* Starting `claude` in the integrated terminal no longer installs the extension. Install it yourself, or run `/ide` from an external terminal, which installs it unless `autoInstallIdeExtension` is `false`. [[line 817](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/ide-integrations.md?plain=1#L817)] [[Source](https://code.claude.com/docs/en/ide-integrations#run-cli-in-vs-code)]

#### [model-config](https://github.com/gpambrozo/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New "Effort level of subagents and teammates" section, and a pointer to the effort level after a fallback. [[line 699](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/model-config.md?plain=1#L699)] [[Source](https://code.claude.com/docs/en/model-config#effort-level-of-subagents-and-teammates)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Warning to use `ENABLE_BETA_TRACING_DETAILED` only for debugging, because of its high export volume and unstable content attributes. [[line 329](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/monitoring-usage.md?plain=1#L329)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* `agent.spawn` now also fires for teammates (`e.isTeammate`) and when a finished subagent is resumed, for example via `SendMessage`. A hook can return `{ deny: reason }` to refuse a resumed run (v2.1.299+). [[lines 153-162](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/plugins/mods/reference.md?plain=1#L153-L162)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#subagents)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* Note on the auto mode denial when a hook or mod changes a call's input. [[line 198](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L198)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#a-hook-changed-this-calls-input-after-the-model-wrote-it)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)] / [web-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/web-scheduled-tasks.md)

* Team and Enterprise Owners can turn off scheduled tasks org-wide via the **Scheduled tasks (Was Routines)** / **Routines** toggle. A new troubleshooting section covers the resulting error. [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/routines.md?plain=1#L30)] [[Source](https://code.claude.com/docs/en/routines#automate-work-with-scheduled-tasks)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Clarified the Dependencies tab: if it's the only tab, the sandbox can't start. Restart Claude Code after installing dependencies. [[lines 70-137](https://github.com/gpambrozo/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/sandboxing.md?plain=1#L70-L137)] [[Source](https://code.claude.com/docs/en/sandboxing#get-started)]
* New "Add an AppArmor profile for bubblewrap" section for Ubuntu's user namespace restriction. [[lines 145-175](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/sandboxing.md?plain=1#L145-L175)] [[Source](https://code.claude.com/docs/en/sandboxing#add-an-apparmor-profile-for-bubblewrap)]
* Documented `sandbox.failIfUnavailable` to exit at startup instead of running unsandboxed. [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/sandboxing.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/sandboxing#get-started)]
* Additional container guidance for unprivileged containers where bubblewrap can't mount. [[lines 911-932](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/sandboxing.md?plain=1#L911-L932)] [[Source](https://code.claude.com/docs/en/sandboxing#ubuntus-apparmor-restriction-stops-bubblewrap)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* Wrapper script guidance: use cases such as scoped credentials, secrets and resource limits. The runner starts it on every session start, resume or requeue, and it should `exec` into `$CLAUDE_RUNNER_CLAUDE_BIN`. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)]
* The checkout hook now runs on every start, resume or requeue. The post-session hook is your only chance to save uncommitted work, with per-capacity behavior. [[lines 145-193](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L145-L193)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#checkout)]
* Wrapper-exported credentials aren't renewed during long sessions. [[line 536](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L536)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#send-model-requests-to-bedrock-or-agent-platform)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Claude Code now warns in interactive sessions and the Desktop Code tab when the managed-settings fetch fails or a cached policy is in effect. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/server-managed-settings.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/server-managed-settings#fetch-and-caching-behavior)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `autoInstallIdeExtension` setting. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/settings-reference.md?plain=1#L39)] [[Source](https://code.claude.com/docs/en/settings-reference#settings-index)]
* `sandbox.failIfUnavailable` description expanded. [[line 1266](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/settings-reference.md?plain=1#L1266)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxfailifunavailable)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added guidance on choosing and inheriting a subagent's effort level.

-----

## API changes

### New Documents

#### [text-watermark](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/build-with-claude/text-watermark.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/text-watermark)]

Describes Anthropic's text watermark on text from supported Claude models. It adds no tokens or hidden characters, carries no information about you, and needs no request changes. On Claude Sonnet 4.6, requests with non-default `temperature`, `top_p` or `top_k` might not carry the watermark, so omit all three if you rely on it.

### Changed documents

#### [about-claude/models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* Introduced beta message threads, which stop resending the conversation within a thread. They lower time to first token, not cost, so keep `cache_control` on every request. They can't be combined with batching. [[lines 58-60](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L58-L60), [line 294](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L294)]

#### [build-with-claude/compaction-threshold](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/build-with-claude/compaction-threshold.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold)]

* The API can pause for compaction without generating a summary. The `compaction` block's `content` is then `null`, the block is ignored, and you should keep the original messages. If safeguards block the summary, the stop reason is `refusal`. [[line 1067](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/build-with-claude/compaction-threshold.md?plain=1#L1067), [line 1643](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/build-with-claude/compaction-threshold.md?plain=1#L1643)]
* Sample code in all languages now looks for the compaction block instead of checking `stop_reason == "compaction"`, and replaces history only if a summary exists. [[lines 2778-2830](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/build-with-claude/compaction-threshold.md?plain=1#L2778-L2830)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction-threshold#examples)]

#### [managed-agents/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/managed-agents/quickstart.md) [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart)]

* Restructured setup into "Before you begin", offering CLI sign-in (`ant auth login`, recommended for local development) or an API key. Installation steps for the CLI (Homebrew, curl, `go install`) were reorganized, and Maven was added alongside Gradle for Java. [[lines 57-200](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/managed-agents/quickstart.md?plain=1#L57-L200)] [[Source](https://platform.claude.com/docs/en/managed-agents/quickstart#before-you-begin)]

#### [managed-agents/webhooks](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/managed-agents/webhooks.md) [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks)]

* The C# SDK has no `Unwrap()`. Verify with a Standard Webhooks library and deserialize into `UnwrapWebhookEvent`. The Python example now uses `standardwebhooks.WebhookVerificationError`. [[lines 138-198](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/managed-agents/webhooks.md?plain=1#L138-L198)] [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks#verify-the-signature)]
* If an endpoint is auto-disabled after a 3xx redirect, create a new endpoint with the same event types and delete the old one. The new endpoint has its own signing secret. [[line 427](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/managed-agents/webhooks.md?plain=1#L427)] [[Source](https://platform.claude.com/docs/en/managed-agents/webhooks#delivery-behavior)]

#### Managed Agents, compaction, context-editing and other pages with curl examples

* Examples now send `anthropic-version: 2026-10-21` instead of `2023-06-01` across the Managed Agents pages (agent-setup, environments, memory, sessions, vaults, skills and others), compaction, context editing and cost-optimization pages.

#### [models/opus-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/models/opus-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/migration-guide)]

* Mid-conversation system messages are now listed as supported on Claude Platform on AWS and Claude Models on Google Cloud (Anthropic managed), in addition to the API, Bedrock and Google managed. [[docs-md/api/models/opus-5-5/migration-guide.md](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/models/opus-5-5/migration-guide.md)]

#### [models/opus-5-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/models/opus-5-5/overview.md) [[Source](https://platform.claude.com/docs/en/models/opus-5-5/overview)] / [models/sonnet-5-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/models/sonnet-5-5/overview.md)

* The breaking-changes lists were removed from the overviews, which now describe typical use cases instead. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/models/opus-5-5/overview.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/models/opus-5-5/overview#overview)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added a November 3, 2026 entry: Claude Mythos 5, Opus 4.7 and Sonnet 4.6 text now carries the text watermark. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/release-notes/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-3-2026)]
* The browser use and computer use tool classes are now tied to Python SDK 1.12.0 and TypeScript SDK 0.132.0. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/3f37ab9a8b405571f1ca931c2b686f2a23ae8508/docs-md/api/release-notes/overview.md?plain=1#L87)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-7-2026)]
