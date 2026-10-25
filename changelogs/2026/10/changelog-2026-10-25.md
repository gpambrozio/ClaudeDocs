# [Claude docs changes for October 25th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e774639fb83880cef79be92e86373673ddbec055) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e774639fb83880cef79be92e86373673ddbec055)]

## Executive Summary
- Mods get a new `settings.read` hook that can change or refuse Claude Code's merged settings, plus `$.settings.read({ source, key })`, new `key` rules for controls, and `claude -p` refusal reasons
- Code Review's `REVIEW.md` can now `@`-include a repository skill's `SKILL.md`, with detailed rules for what a review does and doesn't take from a skill
- The Agent SDK adds `setMcpPermissionModeOverride()`, `seedReadState()`, and `backgroundTasks()` on `Query`, plus new model-refusal and control-request progress messages
- Self-hosted environments gain guidance on memory and process limits, releasing idle sessions, proxy handling of the session event stream, and fixes for re-opened sessions that stay queued
- Desktop SSH remote sessions now support the Windows OpenSSH client and `MaxSessions 1` servers, and cloud sessions and scheduled tasks have new UI flows (Changes card, archived tab, full-page form, "The last run" warnings)

## New Claude Code versions

No new Claude Code versions in this update.

-----

## Claude Code changes

### New Documents

No new documents.

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* A timed-out `PreToolUse` callback no longer hides a deny from another hook: the tool result carries that hook's reason, and the timeout text can follow it. [[lines 760-762](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L760-L762)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#hook-timeout)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `getSessionMessages` has a new `options.includeSystemMessages` option, and returned messages can have `type: "system"`. [[lines 308-314](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L308-L314)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#parameters)]
* New `Query` method `setMcpPermissionModeOverride(serverName, mode)` applies a stricter permission mode (`'default'` or `'auto'`) to one MCP server's tools. It works only in `bypassPermissions` or `auto` sessions and in streaming input mode. [[lines 683-704](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L683-L704)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#setmcppermissionmodeoverride)]
* New `seedReadState(path, mtime)` marks a file as already read so a later Edit doesn't fail with `File has not been read yet`. [[lines 706-712](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L706-L712)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#seedreadstate)]
* New `backgroundTasks(toolUseId?)` moves running Bash commands and subagents to the background, like Ctrl+B. [[lines 714-725](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L714-L725)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#backgroundtasks)]
* `SDKMessage` adds `SDKControlRequestProgressMessage`, `SDKModelRefusalFallbackMessage`, and `SDKModelRefusalNoFallbackMessage`. [[lines 1518-1531](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1518-L1531)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessage)]
* Success results gain a `time_to_request_ms` field. [[line 1757](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1757)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkresultmessage)]

#### [channels-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/channels-reference.md) [[Source](https://code.claude.com/docs/en/channels-reference)]

* Added a third reason a remote permission reply is ignored: an earlier prompt in the session used the same ID, so Claude Code drops any channel verdict carrying it. [[lines 581-585](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/channels-reference.md?plain=1#L581-L585)] [[Source](https://code.claude.com/docs/en/channels-reference#add-relay-to-a-chat-bridge)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* Reworked the explanation of `disableAllHooks: true` in `managedSettings`: lists which hooks stop and which keep running, and states that `hooks`, `allowedHttpHookUrls`, and `httpHookAllowedEnvVars` are ignored there. [[lines 457-469](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-apps-gateway.md?plain=1#L457-L469)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#how-hook-and-skill-keys-in-parent-settings-take-effect)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Diff review now starts from the **Changes** card in the session panel, which appears after Claude pushes to a branch. The panel can be reopened from the title bar. [[lines 246-255](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L246-L255)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#review-changes)]
* Archiving, finding archived sessions (new **Archived** tab at claude.ai/code/sessions), unarchiving, and deleting were rewritten for the new menus. [[lines 318-330](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L318-L330)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#archive-sessions)]
* Auto-fix is now toggled from the pull request's **⋮** menu in the **Changes** card. [[lines 344-349](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L344-L349)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#auto-fix-pull-requests)]
* New troubleshooting entries: "Your new session couldn't start" and "Can't rewind to this message" (self-hosted runners before v2.1.246). [[lines 389-394](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L389-L394)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#your-new-session-couldnt-start)]
* Custom-role note clarified: the cloud sessions permission is needed to start sessions from the browser, apps, or terminal. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L7)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#use-claude-code-in-the-cloud)]

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* A local session connected through Remote Control can now be brought into a project from the claude.ai/code sidebar menu, with caveats for **Require trusted devices**. [[lines 110-125](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/claude-projects.md?plain=1#L110-L125)] [[Source](https://code.claude.com/docs/en/claude-projects#start-from-an-existing-session)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* Setup scripts run before the environment's variables are set, so they must set any values they need themselves (now four constraints). [[lines 442-447](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/cloud-environments.md?plain=1#L442-L447)] [[Source](https://code.claude.com/docs/en/cloud-environments#script-requirements)]

#### [code-review-customize](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/code-review-customize.md) [[Source](https://code.claude.com/docs/en/code-review-customize)]

* New section "Include a skill file": `@.claude/skills/<folder>/SKILL.md` in the root `REVIEW.md` includes a skill. Covers path, size (30,000 bytes), count (eight), symlink and protected-branch rules, what a review gets from a skill (body only, no `!` commands, substitutions, or supporting files), and character substitutions. [[lines 129-188](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/code-review-customize.md?plain=1#L129-L188)] [[Source](https://code.claude.com/docs/en/code-review-customize#include-a-skill-file)]
* Exclusions and Nit caps must live in `REVIEW.md` or a file beside it, not in an included skill. [[line 199](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/code-review-customize.md?plain=1#L199)] [[Source](https://code.claude.com/docs/en/code-review-customize#which-branch-reviewmd-is-read-from)]

#### [code-review-pull-requests](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/code-review-pull-requests.md) [[Source](https://code.claude.com/docs/en/code-review-pull-requests)]

* Explains the two sentences a re-review uses to count findings it left out. [[lines 151-154](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/code-review-pull-requests.md?plain=1#L151-L154)] [[Source](https://code.claude.com/docs/en/code-review-pull-requests#what-a-later-review-covers)]

#### [code-review-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/code-review-troubleshooting.md) [[Source](https://code.claude.com/docs/en/code-review-troubleshooting)]

* Added the "include line(s) in the root REVIEW.md were skipped" check run message, and a note about left-out findings when a review finds no issues. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/code-review-troubleshooting.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/code-review-troubleshooting#the-check-run-mentions-reviewmd)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* SSH remote sessions: servers with `MaxSessions 1` now work on macOS/Linux with Desktop v3.1623.0 or later and with the Windows OpenSSH client, with notes on login prompts and `!` commands. [[lines 983-988](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/desktop.md?plain=1#L983-L988)] [[Source](https://code.claude.com/docs/en/desktop#remote-machine-requirements-for-ssh-sessions)]
* Windows can now use `%USERPROFILE%\.ssh\config` through the OpenSSH client (Desktop v2.2553.0+, OpenSSH 9.4+, non-Store install). New section on connecting on Windows without the OpenSSH client and its limits. [[lines 1032-1067](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/desktop.md?plain=1#L1032-L1067)] [[Source](https://code.claude.com/docs/en/desktop#use-your-ssh-configuration)]
* Rejoining a running SSH task after quit or restart now works on Windows from v3.1623.0. Updated guidance for long tasks and the `Restarting Claude Code on <host>…` state. [[lines 1269-1352](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/desktop.md?plain=1#L1269-L1352)] [[Source](https://code.claude.com/docs/en/desktop#prepare-a-long-task)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Same updates as `desktop` (SSH `MaxSessions 1`, Windows OpenSSH client, rejoining tasks). [[lines 983-1067](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/desktop-changelog.md?plain=1#L983-L1067)] [[Source](https://code.claude.com/docs/en/desktop-changelog#remote-machine-requirements-for-ssh-sessions)]

#### [desktop-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/desktop-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks)]

* Accounts that show **Routines** instead of **Scheduled** are covered, and a new "Full-page form" section describes the **Local**/**Cloud** menu and the **New local routine** page. [[lines 14-117](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/desktop-scheduled-tasks.md?plain=1#L14-L117)] [[Source](https://code.claude.com/docs/en/desktop-scheduled-tasks#schedule-recurring-tasks-in-claude-code-desktop)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries: `MCP server "<name>" is disabled`, `git is not installed on this Mac`, and two `Sandbox is required` messages. [[lines 316-351](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/errors.md?plain=1#L316-L351)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* The `Waiting for API response` banner behind a gateway now appears after 45 seconds (was 20) from v2.1.309. [[lines 491-501](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/errors.md?plain=1#L491-L501)] [[Source](https://code.claude.com/docs/en/errors#the-waiting-banner-comes-and-goes-behind-a-gateway)]
* Disk-full error guidance consolidated for the quota and inode messages. [[lines 4786-4796](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/errors.md?plain=1#L4786-L4796)] [[Source](https://code.claude.com/docs/en/errors#disk-full-or-disk-quota-used-up)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Availability-check troubleshooting split into one section per message (network connectivity, currently unavailable, disabled by your organization), with the right skip variable for each. [[lines 154-171](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/fast-mode.md?plain=1#L154-L171)] [[Source](https://code.claude.com/docs/en/fast-mode#use-fast-mode-behind-proxies-and-llm-gateways)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Windows without Git Bash: reorganized fixes, and a new "PowerShell started no program" section for a `command` that is only quoted strings. [[lines 960-981](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/hooks.md?plain=1#L960-L981)] [[Source](https://code.claude.com/docs/en/hooks#failed-hooks-on-windows-without-git-bash)]
* New note: pressing `Esc` during a prompt check stops it, but a block issued at the same moment still stands. [[lines 1482-1487](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/hooks.md?plain=1#L1482-L1487)] [[Source](https://code.claude.com/docs/en/hooks#esc-during-a-prompt-check)]
* A plugin's `WorktreeCreate` hook doesn't run with `--worktree` plus `--tmux`. Define it in a settings file instead. [[lines 3140-3144](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/hooks.md?plain=1#L3140-L3144)] [[Source](https://code.claude.com/docs/en/hooks#worktreecreate)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Multiple `PreToolUse` hooks returning `updatedInput` are not merged, and which rewrite wins isn't guaranteed. [[line 953](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/hooks-guide.md?plain=1#L953)] [[Source](https://code.claude.com/docs/en/hooks-guide#limitations)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* The diff panel keeps its last-read state during an unfinished merge, rebase, cherry-pick, or revert. [[lines 658-659](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/interactive-mode.md?plain=1#L658-L659)] [[Source](https://code.claude.com/docs/en/interactive-mode#diff-panel)]

#### [llm-gateway-connect](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/llm-gateway-connect.md) [[Source](https://code.claude.com/docs/en/llm-gateway-connect)]

* New `/fast` row for "currently unavailable" with a gateway-issued `ANTHROPIC_API_KEY`. [[lines 518-520](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/llm-gateway-connect.md?plain=1#L518-L520)] [[Source](https://code.claude.com/docs/en/llm-gateway-connect#troubleshoot-gateway-errors)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Claude Code (v2.1.310+) also retries without `effort` when the upstream rejects the `effort-2025-11-24` beta value with `Unexpected value(s)`. [[lines 237-241](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L237-L241)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#automatic-retry-and-error-forwarding)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Allowlist matching details: Google Cloud Agent Platform IDs with an `@` date need the date in the entry, and `[1m]` suffixes are stripped before matching. [[lines 946-952](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/model-config.md?plain=1#L946-L952)] [[Source](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* For Desktop SSH sessions, set variables under `env` in the remote machine's managed settings file instead of login files. `precompute_reuse` scope clarified. [[lines 469-1402](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/monitoring-usage.md?plain=1#L469)] [[Source](https://code.claude.com/docs/en/monitoring-usage#attribute-telemetry-to-desktop-ssh-sessions)]

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* New "Cloud provider and LLM gateway routing" heading. Fast mode behind a gateway needs `api.anthropic.com` reachable through the proxy. [[lines 239-243](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/network-config.md?plain=1#L239-L243)] [[Source](https://code.claude.com/docs/en/network-config#cloud-provider-and-llm-gateway-routing)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Monitors don't start with `-p`. On Windows, `${CLAUDE_PLUGIN_ROOT}` keeps backslashes in exec-form and PowerShell hooks. [[lines 154-605](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins-reference.md?plain=1#L154)] [[Source](https://code.claude.com/docs/en/plugins-reference#fields)]

#### [plugins/components](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/components.md) [[Source](https://code.claude.com/docs/en/plugins/components)]

* Monitor availability reworked: on Bedrock, AWS, Agent Platform, Foundry, or with telemetry off, monitors need v2.1.310 or later. [[lines 583-585](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/components.md?plain=1#L583-L585)] [[Source](https://code.claude.com/docs/en/plugins/components#monitors)]

#### [plugins/mods/api](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* New section "Calls refused in `claude -p` runs and Agent SDK sessions": refusal reasons (`--max-turns`, `--max-budget-usd`, input ended, interrupted) and fixes. [[lines 340-364](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/api.md?plain=1#L340-L364)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#calls-refused-in-claude-p-runs-and-agent-sdk-sessions)]
* Explains why a `claude -p` run with a mod that submits prompts every turn never exits, and how to bound it. [[lines 366-378](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/api.md?plain=1#L366-L378)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#send-and-receive-messages-between-sessions)]
* `$.settings.read()` accepts `{ source }` and `{ key }` (key requires v2.1.304+). [[lines 414-452](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/api.md?plain=1#L414-L452)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#reach-files-processes-and-the-network)]

#### [plugins/mods/events](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/events.md) [[Source](https://code.claude.com/docs/en/plugins/mods/events)]

* New `settings.read` hook section covering `e.layers`, `e.source`, returning `{ value }` or `{ deny }`, distinguishing Claude Code's own read via `next.origin`, and an example. [[lines 312-373](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/events.md?plain=1#L312-L373)] [[Source](https://code.claude.com/docs/en/plugins/mods/events#change-or-refuse-a-settings-read)]
* A hook that throws or times out is skipped and the action proceeds. Add a `.catch` handler to refuse instead. [[lines 114-216](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/events.md?plain=1#L114)] [[Source](https://code.claude.com/docs/en/plugins/mods/events#guard-or-change-a-tool-call)]

#### [plugins/mods/gallery](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/gallery.md) [[Source](https://code.claude.com/docs/en/plugins/mods/gallery)]

* `Image` can now draw inside tmux 3.3+ (Claude Code v2.1.310+), with a requirements checklist and the tmux options to set. File-path sources fail in tmux like iTerm2. [[lines 352-381](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/gallery.md?plain=1#L352-L381)] [[Source](https://code.claude.com/docs/en/plugins/mods/gallery#image-and-client)]

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* New "Which controls need a `key`": every `Input` and `Select` needs one, and a `Button` falls back to its label. [[lines 507-516](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/interface.md?plain=1#L507-L516)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#which-controls-need-a-key)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* Added the `settings.read` event and its fields. `types` can be omitted from the manifest from v2.1.299. [[lines 20-128](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/reference.md?plain=1#L117-L125)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#files)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* New entries: "This mod's change didn't load", `needs a key` / `is drawn twice` / `key each once`, and `settings.read` problems (key has no effect, value the key can't hold, refused to the engine). [[lines 167-342](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L167-L176)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#this-mods-change-didnt-load-or-the-earlier-version-is-no-longer-running)]

#### [plugins/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/troubleshooting.md) [[Source](https://code.claude.com/docs/en/plugins/troubleshooting)]

* Marketplace clones turn off git prompts and askpass programs (including `GIT_ASKPASS`) and run SSH in batch mode. New test command: `git -c core.askPass= ls-remote <url>`. [[lines 250-255](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L250-L255)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#ssh-authentication-failed-or-https-authentication-failed)]
* Forward-slash plugin root paths apply only to hooks that run through Git Bash. [[lines 978-980](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/plugins/troubleshooting.md?plain=1#L978-L980)] [[Source](https://code.claude.com/docs/en/plugins/troubleshooting#claude_plugin_root-shows-forward-slashes-on-windows)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New troubleshooting entry for "Remote Control disconnected" / "Can't reach". [[lines 400-407](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/remote-control.md?plain=1#L400-L407)] [[Source](https://code.claude.com/docs/en/remote-control#remote-control-disconnected-or-cant-reach)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* New "Full-page form" for creating tasks, a cron time-zone note (UTC unless `CRON_TZ=`), an **Issue** GitHub event category, and run outcomes (**Succeeded**, **Failed**, **Cancelled**). [[lines 65-333](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/routines.md?plain=1#L130-L141)] [[Source](https://code.claude.com/docs/en/routines#create-from-the-web)]
* New troubleshooting table of "The last run" warnings and what to do for each. [[lines 503-517](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/routines.md?plain=1#L503-L517)] [[Source](https://code.claude.com/docs/en/routines#the-last-run-warnings)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New troubleshooting for `Sandbox is required` refusals when `sandbox.failIfUnavailable` is set. Excluded commands and `!` commands keep running, and `dangerouslyDisableSandbox` retries are ignored. [[lines 1008-1022](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/sandboxing.md?plain=1#L1008-L1022)] [[Source](https://code.claude.com/docs/en/sandboxing#commands-are-refused-with-sandbox-is-required)]
* New section on when the sandbox deletes a newer top-level `HEAD`, `objects`, or `refs`, and why an `objects` or `refs` folder can disappear (fixed for folders with contents in v2.1.307). [[lines 538-558](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/sandboxing.md?plain=1#L538-L558)] [[Source](https://code.claude.com/docs/en/sandboxing#protected-paths)]
* Leftover placeholder files can also remain when a session exits while a background sandboxed command runs. [[lines 900-910](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/sandboxing.md?plain=1#L900-L910)] [[Source](https://code.claude.com/docs/en/sandboxing#0-byte-read-only-files-appear-at-claude-settings-paths-and-yes-and-dont-ask-again-doesnt-save)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New `CLAUDE_CODE_REMOTE_SLACK_CHANNEL_ID` variable for Claude Tag sessions. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#wrapper-scripts)]
* New "Fix `Argument list too long` at session start" for joined `--append-system-prompt` arguments over 128 KB on Linux. [[lines 89-108](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L89-L108)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#fix-argument-list-too-long-at-session-start)]
* `spawn-runner` hook: after 10 failed requests in a row the session is blocked. New section on re-opened sessions that stay Queued or show Failed when the hook keys on the session ID. [[lines 328-372](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L328-L372)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#the-spawn-runner-hook)]
* New section on stopping sessions that fail to fetch server-managed settings with `forceRemoteSettingsRefresh`, with Claude Tag and Bedrock caveats. [[lines 794-814](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L794-L814)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#stop-sessions-that-fail-to-fetch-server-managed-settings)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* New section on adding github.com repositories to Claude Tag channel sessions (GitHub App, link the org, grant the repository). [[lines 312-331](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L312-L331)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#add-githubcom-repositories-to-claude-tag-channel-sessions)]
* New sizing guidance: several runners per host, per-session memory limits, and process/thread limits with a step-by-step way to measure one session's peak. [[lines 395-477](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L395-L477)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#size-cpu-and-memory-for-sessions)]
* Pre-warmed checkout: clone depth guidance and a way to confirm the runner uses your clone. [[lines 675-690](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L675-L690)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#reuse-a-pre-warmed-checkout)]
* New "Release idle sessions on a fixed fleet" for queued sessions caused by idle ones. [[lines 713-729](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L713-L729)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#release-idle-sessions-on-a-fixed-fleet)]
* New section on proxies that buffer the session event stream, so Claude never answers the first message, with log lines to confirm the cause. [[lines 916-952](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L916-L952)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#a-session-is-picked-up-but-claude-never-answers-its-first-message)]

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* New "Session startup timeout" section. Runners from v2.1.299 through v2.1.308 could release a session mid-turn. Update to v2.1.309 or later. [[lines 51-66](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L60-L65)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference#runner-cli-flags)]
* Prometheus alert rules aggregate by namespace, and there is a new cost-per-idle-session query joining on `ccr_session_id`. [[lines 259-392](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/self-hosted-environments-reference.md?plain=1#L379-L392)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference#sample-alert-rules)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Sandbox filesystem wildcard rules rewritten as a table of what works on macOS versus Linux/WSL2, plus guidance for directory names with brackets, braces, or parentheses. [[lines 1370-1403](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/settings-reference.md?plain=1#L1370-L1403)] [[Source](https://code.claude.com/docs/en/settings-reference#where-wildcards-work-in-sandbox-paths)]
* `sandbox.failIfUnavailable`: if the sandbox fails after startup, the session continues and sandboxed commands are refused. [[line 1229](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/settings-reference.md?plain=1#L1229)] [[Source](https://code.claude.com/docs/en/settings-reference#sandboxfailifunavailable)]
* `idleCompaction` now also applies to the VS Code chat panel and Desktop Code tab for accounts Anthropic selects, with new notices and a new subsection. [[lines 2414-2476](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/settings-reference.md?plain=1#L2414-L2476)] [[Source](https://code.claude.com/docs/en/settings-reference#idlecompaction)]
* `availableModelsMatch: "exact"` also permits an entry's dated Anthropic ID. [[line 332](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/settings-reference.md?plain=1#L332)] [[Source](https://code.claude.com/docs/en/settings-reference#availablemodelsmatch)]
* `allowManagedHooksOnly` also blocks monitors from plugins that aren't force-enabled (v2.1.310+). `disableAllHooks` in `managedSettings` is described by what stops and what keeps running. [[lines 3537-3564](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/settings-reference.md?plain=1#L3537)] [[Source](https://code.claude.com/docs/en/settings-reference#what-runs-under-allowmanagedhooksonly)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* tmux setup adds `set -g focus-events on` and notes the extra requirements for drawing mod `Image` elements. The tab title omits the status glyph in terminals that report protocol support. [[lines 120-137](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/terminal-config.md?plain=1#L120-L137)] [[Source](https://code.claude.com/docs/en/terminal-config#see-session-status-in-your-terminal)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Monitor tool availability: v2.1.310 or later is needed on third-party providers or with telemetry off, and Windows needs Git Bash. [[lines 382-386](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/tools-reference.md?plain=1#L382-L386)] [[Source](https://code.claude.com/docs/en/tools-reference#monitor-tool)]

#### [ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Pressing Enter at the trust question also exits with code 1. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/ultrareview.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/ultrareview#run-ultrareview-non-interactively)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* Diff review and PR creation now go through the **Changes** card. Right-click **Create PR** to choose **Create draft PR**. [[lines 176-193](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/web-quickstart.md?plain=1#L176-L193)] [[Source](https://code.claude.com/docs/en/web-quickstart#review-and-iterate)]

#### [web-scheduled-tasks](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/web-scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/web-scheduled-tasks)]

* Same updates as `routines`: full-page form, cron time zone note, **Issue** event category, run outcome definitions, and "The last run" warnings table. [[lines 65-517](https://github.com/gpambrozio/ClaudeDocs/blob/e774639fb83880cef79be92e86373673ddbec055/docs-md/claude-code/web-scheduled-tasks.md?plain=1#L130-L141)] [[Source](https://code.claude.com/docs/en/web-scheduled-tasks#create-from-the-web)]

-----

## API changes

### New Documents

No new documents.

### Changed documents

No changed documents.
