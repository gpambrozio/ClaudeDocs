# [Claude docs changes for October 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e4d297c91d593da479d5c57c63b25d8edc45d414) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e4d297c91d593da479d5c57c63b25d8edc45d414)]

## Executive Summary
- Claude Code 2.1.302 adds `CLAUDE_CODE_AUTO_MODE_MODEL` to choose the client-side auto mode classifier model, plus an `/config` toggle for idle compaction.
- Hooks docs now spell out when a failed hook blocks an action (`onFailure: "block"`), including a new section on Windows without Git Bash.
- Permissions docs add precedence rules for hooks and mods in plan mode, and clearer MCP rule syntax (`mcp__<server>__*`, plugin-scoped names, special characters).
- Mods reference gains `Box` spacing steps and `Text` typography props (`size`, `weight`, `mono`, `tabular`), with `bold` deprecated in favor of `weight`.
- Desktop docs clarify when a long-running task survives quitting Desktop.

## New Claude Code versions

### [2.1.302](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/versions/2.1.302.md)

#### New features

* Added `CLAUDE_CODE_AUTO_MODE_MODEL` to choose the model the client-side auto mode classifier uses (it doesn't affect server-side auto mode)
* Added an `Idle compaction` row to `/config` to turn idle compaction off or on; notices after an idle compaction now say how to turn it off
* Added a notice to `/design-sync` and `/design-login` that standalone Claude Design closes on December 14, 2026

#### Existing feature improvements

* Prompt suggestions no longer spend usage credits on models your plan covers only with credits
* URLs in backticks are now one clickable link when they wrap, in terminals that support hyperlinks
* `claude plugin details <name>@builtin` now points to `/plugin` when the plugin isn't found

#### Major bug fixes

* Fixed a "Prompt is too long" error when stopping a turn during compaction
* Fixed requests failing with "diagnostics: Extra inputs are not permitted" after switching to Vertex or Bedrock mid-session
* Fixed the Read tool loading image files of any size into memory; image sources over 128 MB are now refused
* Fixed a prompt cache miss when a tool added mid-session was loaded again through ToolSearch or after compaction
* Fixed `claude plugin` and other subcommands exiting before a queued settings or config write finished, which could lose the change
* Fixed MCP servers showing no tools, or all tool calls failing, when the server negotiates protocol version 2026-07-28 but omits `resultType`, `ttlMs` or `cacheScope`
* Fixed `classifier_category` missing from OpenTelemetry `tool_decision` events for most auto mode classifier blocks
* Fixed worktree isolation failing under git 2.56 or later when a stray `.git` file points at a missing directory

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* The `.env` protection example now compares case-insensitively, with a note that it doesn't catch Windows backslash paths or `Bash` writes. [[lines 54-139](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L54-L139)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#how-hooks-work)]
* The `PreToolUse` timeout behavior is described as blocking the tool call, with version notes for earlier behavior. [[line 751](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L751)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#hook-timeout)]

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/agent-sdk/mcp.md) [[Source](https://code.claude.com/docs/en/agent-sdk/mcp)]

* Explains how server names are normalized in tool names (`.` and spaces become `_`), with a table, and how plugin-provided servers are named. [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L171)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#tool-naming-convention)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Plan mode: file edits aren't auto-approved even when a `PreToolUse` hook returns `allow`. [[line 273](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L273)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#plan-mode-plan)]
* New Auto mode section: switching a session in auto mode to an unsupported model drops it to `default` mode (Claude Code v2.1.299+), and you must call `set_permission_mode("auto")` to return. [[lines 281-291](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L281-L291)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#auto-mode-auto)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Rewrote guidance on quitting Desktop during long tasks: Windows never rejoins, third-party-provider tasks started before v2.42304.0 are lost, and other tasks continue only if Desktop can rejoin the process. [[lines 972-1075](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/desktop.md?plain=1#L972-L1075)] [[Source](https://code.claude.com/docs/en/desktop#keep-a-task-running-while-desktop-is-disconnected)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* Same rejoin-after-quit clarifications as the Desktop page. [[lines 972-1075](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/desktop-changelog.md?plain=1#L972-L1075)] [[Source](https://code.claude.com/docs/en/desktop-changelog#keep-a-task-running-while-desktop-is-disconnected)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `onFailure` is reworded, and non-blocking error, JSON parse, start-failure, timeout and HTTP sections now note the exception for hooks whose failure blocks the action. [[lines 443-1004](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/hooks.md?plain=1#L443-L1004)] [[Source](https://code.claude.com/docs/en/hooks#command-hook-fields)]
* New section "Failed hooks on Windows without Git Bash": a shell-form `PreToolUse` or `PermissionRequest` hook that fails there can block the call, with four fixes. [[lines 934-950](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/hooks.md?plain=1#L934-L950)] [[Source](https://code.claude.com/docs/en/hooks#failed-hooks-on-windows-without-git-bash)]
* `UserPromptSubmit` hooks receive a typed skill or command line (e.g. `/deploy staging`) as typed, not the expanded content. [[line 1469](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/hooks.md?plain=1#L1469)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit-input)]
* `permissionDecision: "allow"` wording refined for actions no mode auto-approves. [[line 1922](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/hooks.md?plain=1#L1922)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]
* New "PreModelSwitch timeouts and other exit codes" subsection. [[line 3422](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/hooks.md?plain=1#L3422)] [[Source](https://code.claude.com/docs/en/hooks#premodelswitch-timeouts-and-other-exit-codes)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Same changes as the VS Code page (the two files carry the same content).

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Stream timers: explains what happens when no response headers arrive (first-byte deadline vs. body idle timeout after 5-6 minutes), and that `API_TIMEOUT_MS` can be lowered below 300000 to retry sooner where the first-byte deadline doesn't run. [[lines 168-188](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/network-config.md?plain=1#L168-L188)] [[Source](https://code.claude.com/docs/en/network-config#streaming-idle-watchdogs)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Clarified that an ignored bypass request leaves `bypassPermissions` out of the `Shift+Tab` cycle or starts the session in Manual mode. [[lines 592-594](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/permission-modes.md?plain=1#L592-L594)] [[Source](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)]
* `dev-mods/` in the config directory is now a protected path. [[line 647](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/permission-modes.md?plain=1#L647)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* MCP rule syntax: `mcp__<server>__*` and `mcp__<server>__<tool>`, with guidance for special characters, plugin-provided servers, and names containing `__`. [[lines 526-538](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/permissions.md?plain=1#L526-L538)] [[Source](https://code.claude.com/docs/en/permissions#mcp)]
* New "Precedence among rules, hooks, and mods" heading and a "Hook approvals in plan mode" section: a hook's or mod's `allow` has no effect on non-read-only calls in plan mode. [[lines 580-603](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/permissions.md?plain=1#L580-L603)] [[Source](https://code.claude.com/docs/en/permissions#precedence-among-rules-hooks-and-mods)]

#### [plugins/mods/create](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/create.md) [[Source](https://code.claude.com/docs/en/plugins/mods/create)]

* Approval prompts happen because the mods folder, not `~/.claude`, is a protected path. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/create.md?plain=1#L24)] [[Source](https://code.claude.com/docs/en/plugins/mods/create#ask-claude-for-a-mod)]

#### [plugins/mods/events](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/events.md) [[Source](https://code.claude.com/docs/en/plugins/mods/events)]

* `tool.check` hooks can't approve non-read-only calls in plan mode. [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/events.md?plain=1#L204)] [[Source](https://code.claude.com/docs/en/plugins/mods/events#approve-or-refuse-a-tool-call-before-the-user-is-asked)]

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* `Box` spacing props accept step names, and `Text` accepts typography props such as `weight`. [[lines 426-427](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/interface.md?plain=1#L426-L427)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#build-a-tree-from-elements)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* New `Box` spacing steps table (`xs` to `xl`), requires v2.1.299+. [[lines 300-320](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/reference.md?plain=1#L300-L320)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#elements)]
* New `Text` typography props `size`, `weight`, `mono`, `tabular`, with how the terminal and VS Code extension treat them. `bold` is deprecated in favor of `weight`. [[lines 320-340](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/reference.md?plain=1#L320-L340)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#elements)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* New entry "Another mod's band shows and yours doesn't": mods share one band above the prompt, so keep `await next(e)` in your tree. [[lines 182-194](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L182-L194)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#a-drawing-doesnt-appear-or-respond)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Auto-allow mode: commands in a form that a `Bash` deny rule matches are still blocked; critical-path `rm`/`rmdir` checks apply to commands recognized as targeting such a path. [[lines 174-175](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/sandboxing.md?plain=1#L174-L175)] [[Source](https://code.claude.com/docs/en/sandboxing#auto-allow-mode)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Feature list reformatted; new guidance to run the CLI in the integrated terminal for editors that can't install the extension. [[lines 9-41](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/vs-code.md?plain=1#L9-L41)] [[Source](https://code.claude.com/docs/en/vs-code#use-claude-code-in-vs-code)]
* Diffs with more than 100 changes open without per-change accept/reject buttons. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/e4d297c91d593da479d5c57c63b25d8edc45d414/docs-md/claude-code/vs-code.md?plain=1#L98)] [[Source](https://code.claude.com/docs/en/vs-code#get-started)]

-----

## API changes

No API documentation changes today.
