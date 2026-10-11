# [Claude docs changes for October 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a6a246813817f8866d5c3425809b06923d2e8776) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a6a246813817f8866d5c3425809b06923d2e8776)]

## Executive Summary
- New **network path** permission check: reads from UNC paths (Windows) and `/net` automounts (macOS/Linux) now always prompt, ignoring allow rules, hooks and auto mode (v2.1.292+).
- Edit and NotebookEdit now refuse files that aren't valid UTF-8 instead of silently corrupting them with `U+FFFD` (v2.1.296+). There is a new error section and a new "Non-UTF-8 files" section.
- Hooks docs gained a precise description of how stdout is parsed as JSON, and `CLAUDE_ENV_FILE` variables now reach PowerShell commands under strict conditions (v2.1.296+).
- Agent view and background sessions got a lot of detail on backgrounding behavior, `claude respawn`, `claude daemon stop --keep-workers`, and bypass-permission acceptance rules.
- Desktop SSH sessions can now choose where worktrees go (`worktree.location` setting, **Worktree folder** field), and the Agent SDK documents a new `forkSession()` function.

## New Claude Code versions

No new version files in this update.

-----

## Claude Code changes

### New Documents

No new documents.

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Documented the new `forkSession()` function, which copies a session transcript into a new session, optionally up to a given message (`upToMessageId`). [[lines 397-424](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L397-L424)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#forksession)]
* `allowedTools` auto-approval doesn't cover reads from network paths. [[line 494](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L494)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* New `∙` status icon for exited processes; replying or attaching restarts them from the saved conversation. [[line 137](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-view.md?plain=1#L137)] [[Source](https://code.claude.com/docs/en/agent-view#read-session-state)]
* Clarified detaching and `Ctrl+C` behavior while attached, and that detaching never stops a background session. [[lines 243-245](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-view.md?plain=1#L243-L245)] [[Source](https://code.claude.com/docs/en/agent-view#attach-to-a-session)]
* Detailed what happens when pressing `←` while a tool runs, a prompt is pending, or the turn is stopped, and that foreground shell commands are stopped on backgrounding. [[lines 265-275](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-view.md?plain=1#L265-L275)] [[Source](https://code.claude.com/docs/en/agent-view#switch-sessions-without-leaving-the-terminal)]
* In-flight background work (shell commands, subagents, workflows, scheduled tasks) carries over on backgrounding; monitors can't and are stopped. `/add-dir` directories also carry over. [[lines 455-473](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-view.md?plain=1#L455-L473)] [[Source](https://code.claude.com/docs/en/agent-view#what-carries-over-when-you-background)]
* Background sessions in `bypassPermissions` mode require a recorded acceptance of the disclaimer. [[lines 707-711](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-view.md?plain=1#L707-L711)] [[Source](https://code.claude.com/docs/en/agent-view#dispatch-defaults)]
* New `claude respawn <id>` command, `claude daemon stop --any --keep-workers`, and name-based `claude attach`/`claude logs`. [[lines 756-765](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-view.md?plain=1#L756-L765)] [[Source](https://code.claude.com/docs/en/agent-view#manage-sessions-from-the-shell)]
* Supervisor stop/restart behavior: sessions wait about a minute for a new supervisor to reconnect; `claude daemon status` warns on version mismatch. [[lines 815-836](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/agent-view.md?plain=1#L815-L836)] [[Source](https://code.claude.com/docs/en/agent-view#the-supervisor-process)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* New section explaining the token count shown beside the spinner (output-only, per turn, resets on compaction). [[lines 75-85](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/costs.md?plain=1#L75-L85)] [[Source](https://code.claude.com/docs/en/costs#read-the-token-count-beside-the-spinner)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Worktree location can be customized for local sessions, with a Branch prefix setting and auto-archive after PR merge. [[lines 331-340](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/desktop.md?plain=1#L331-L340)] [[Source](https://code.claude.com/docs/en/desktop#work-in-parallel-with-sessions)]
* New **Worktree folder** for SSH connections and a precedence order for choosing where SSH worktrees go (Desktop v1.44121.0+). [[lines 699-719](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/desktop.md?plain=1#L699-L719)] [[Source](https://code.claude.com/docs/en/desktop#ssh-sessions)]
* Administrators can distribute SSH connections through `sshConfigs` in managed settings. [[line 768](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/desktop.md?plain=1#L768)] [[Source](https://code.claude.com/docs/en/desktop#pre-configure-ssh-connections-for-your-team)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error entry: "File is not valid UTF-8" (Edit/NotebookEdit refusal) with remedies. [[lines 4375-4393](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/errors.md?plain=1#L4375-L4393)] [[Source](https://code.claude.com/docs/en/errors#refusing-to-send-a-cross-session-message)]
* New entry for the `Not run · auto mode's check had no usable answer` row. [[lines 32](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/errors.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* New entry for the reserved marketplace name error. [[line 259](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/errors.md?plain=1#L259)] [[Source](https://code.claude.com/docs/en/errors#find-your-error)]
* `/net` automount paths are refused as working directories; reads under them go through the network path check. [[line 5117](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/errors.md?plain=1#L5117)] [[Source](https://code.claude.com/docs/en/errors#working-directory-is-a-network-path)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Precise rules for when hook stdout is parsed as JSON versus plain text or a parse failure; multi-line JSON requires v2.1.295+ for async hooks. [[lines 786-791](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/hooks.md?plain=1#L786-L791)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-0)]
* `agent_id` now also identifies in-process teammates. [[lines 717-721](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/hooks.md?plain=1#L717-L721)] [[Source](https://code.claude.com/docs/en/hooks#common-input-fields)]
* `additionalContext` containing `<system-reminder>` tags has the `<` escaped. [[line 1052](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/hooks.md?plain=1#L1052)] [[Source](https://code.claude.com/docs/en/hooks#add-context-for-claude)]
* New section on persisting `CLAUDE_ENV_FILE` variables to PowerShell commands (v2.1.296+) and which events have access to it. [[lines 1295-1308](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/hooks.md?plain=1#L1295-L1308)] [[Source](https://code.claude.com/docs/en/hooks#persist-environment-variables)]
* `permissionDecision: "allow"` doesn't skip prompts for network path reads, `AskUserQuestion`, or `ExitPlanMode`. [[line 1869](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/hooks.md?plain=1#L1869)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]
* Resuming a deferred session in plan mode needs `--permission-prompt-tool` (v2.1.246+). [[line 1970](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/hooks.md?plain=1#L1970)] [[Source](https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later)]
* Debug log now records a duration line per command hook (v2.1.296+) for finding slow hooks. [[line 4089](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/hooks.md?plain=1#L4089)] [[Source](https://code.claude.com/docs/en/hooks#debug-hooks)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New section on attributing telemetry to Desktop SSH sessions using `OTEL_RESOURCE_ATTRIBUTES` on each remote machine. [[lines 435-464](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/monitoring-usage.md?plain=1#L435-L464)] [[Source](https://code.claude.com/docs/en/monitoring-usage#attribute-telemetry-to-desktop-ssh-sessions)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* `dontAsk` mode described in the modes table. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permission-modes.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]
* Auto mode: network path reads always prompt; protected-path writes go to the classifier even with an allow rule; `rm` of critical paths is denied despite allow rules or hooks. [[lines 495-556](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permission-modes.md?plain=1#L495-L556)] [[Source](https://code.claude.com/docs/en/permission-modes#how-auto-mode-evaluates-actions)]
* Bypass mode acceptance rules for non-interactive and background sessions. [[lines 598-601](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permission-modes.md?plain=1#L598-L601)] [[Source](https://code.claude.com/docs/en/permission-modes#skip-all-checks-with-bypasspermissions-mode)]
* Symlinked settings files' targets count as protected paths. [[line 666](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permission-modes.md?plain=1#L666)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]
* Expanded Windows critical paths (8.3 short names, `\\?\C:\`, volume GUID paths; v2.1.292+). [[lines 682-702](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permission-modes.md?plain=1#L682-L702)] [[Source](https://code.claude.com/docs/en/permission-modes#which-paths-are-critical)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* New "Network paths" section: UNC and `/net` reads always prompt and are denied in `dontAsk` mode (v2.1.292+), with workarounds via drive mapping or local mounts. [[lines 459-475](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permissions.md?plain=1#L459-L475)] [[Source](https://code.claude.com/docs/en/permissions#network-paths)]
* New section on exec wrappers (`watch`, `setsid`, `flock`...) and `find` actions that prefix rules can't auto-approve. [[lines 231-242](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permissions.md?plain=1#L231-L242)] [[Source](https://code.claude.com/docs/en/permissions#compound-commands)]
* `ps` with arguments that could print environment variables now prompts. [[line 273](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permissions.md?plain=1#L273)] [[Source](https://code.claude.com/docs/en/permissions#read-only-commands)]
* Some prompts offer only a one-time approval when a saved rule couldn't be fully shown. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permissions.md?plain=1#L31)] [[Source](https://code.claude.com/docs/en/permissions#permission-system)]
* Expanded `dontAsk` description and `WebFetch(domain:*.example.com)` subdomain tip. [[lines 78-480](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permissions.md?plain=1#L78-L480)] [[Source](https://code.claude.com/docs/en/permissions#permission-modes)]
* A mod's `tool.check` approval doesn't skip prompts for tools requiring user interaction. [[line 578](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permissions.md?plain=1#L578)] [[Source](https://code.claude.com/docs/en/permissions#extend-permissions-with-hooks)]
* `/cd <path>` moves the session to a new primary working directory. [[line 600](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/permissions.md?plain=1#L600)] [[Source](https://code.claude.com/docs/en/permissions#move-the-session-to-another-directory)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `worktree.location` setting for Desktop SSH session worktrees. [[lines 5184-5203](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/settings-reference.md?plain=1#L5184-L5203)] [[Source](https://code.claude.com/docs/en/settings-reference#worktreelocation)]
* `copyFullResponse` documented as the "Always copy full response" `/copy` picker option. [[lines 588-6216](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/settings-reference.md?plain=1#L6211-L6216)] [[Source](https://code.claude.com/docs/en/settings-reference#settings-index)]
* `forceLoginOrgUUID` with an invalid value blocks sign-in with an explanatory message. [[line 5615](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/settings-reference.md?plain=1#L5615)] [[Source](https://code.claude.com/docs/en/settings-reference#forceloginorguuid)]
* `sshConfigs` managed setting documented for Desktop; Artifacts disable key description added. [[lines 5297-5415](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/settings-reference.md?plain=1#L5415)] [[Source](https://code.claude.com/docs/en/settings-reference#disabledesktoplocalsessions)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New "Non-UTF-8 files" section: Edit and NotebookEdit refuse them; Write can replace them as UTF-8. [[lines 258-265](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/tools-reference.md?plain=1#L258-L265)] [[Source](https://code.claude.com/docs/en/tools-reference#non-utf-8-files)]
* Edit: `Read` deny rules block edits, and Bash views such as `cat`/`grep`/`rg` can satisfy the read-before-edit requirement. [[lines 246-256](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/tools-reference.md?plain=1#L246-L256)] [[Source](https://code.claude.com/docs/en/tools-reference#edit-tool-behavior)]
* New "Large files" section: 25,000-token and 256 KB read limits, `PARTIAL view` notices. [[lines 508-516](https://github.com/gpambrozo/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/tools-reference.md?plain=1#L508-L516)] [[Source](https://code.claude.com/docs/en/tools-reference#large-files)]
* PowerShell follows the same working-directory reset behavior as Bash and receives `CLAUDE_ENV_FILE` variables (v2.1.296+). [[lines 469-471](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/tools-reference.md?plain=1#L469-L471)] [[Source](https://code.claude.com/docs/en/tools-reference#shell-selection-in-settings-hooks-and-skills)]

#### [plugins/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/plugins/troubleshooting.md) [[Source](https://code.claude.com/docs/en/plugins/troubleshooting)]

* Added a troubleshooting section for reserved marketplace names.

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/a6a246813817f8866d5c3425809b06923d2e8776/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* Added content on seeing session status in the terminal (referenced from agent view).

-----

## API changes

No API documentation changes in this update.
