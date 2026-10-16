# [Claude docs changes for October 16th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/cf5513dbc8c51a3107352b884ae982f99f208ee0) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/cf5513dbc8c51a3107352b884ae982f99f208ee0)]

## Executive Summary
- Claude Code 2.1.301 adds `%` bracket matching to vim mode, multi-line `Input` fields for mods, and richer OpenTelemetry `tool_decision` events. It also fixes many bugs, including a retry on the previous Fable model when the newest one is unavailable to your organization.
- The VS Code extension now typesets LaTeX math in responses. Mods can now draw in the VS Code chat panel, and the panel no longer re-crashes when it reopens a conversation that failed to load.
- The Code Review documentation was split from one page into six: overview, setup, pull requests, local review, customization, costs and troubleshooting.
- Fast mode for Claude Opus 5.5 is out of research preview. It no longer needs the beta header or an access request, and it is available on Microsoft Foundry for Azure-hosted deployments.
- New API docs cover CMEK on Claude Platform on AWS, choosing a Managed Agents environment, Compliance API Code artifacts endpoints, and system prompts for three more models.

## New Claude Code versions

### [2.1.301](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/versions/2.1.301.md)

#### New features

* Added `CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS`, so unattended retry mode ends a request at a usage limit that resets too far away instead of waiting
* Added the `%` motion to vim mode (jump to the matching bracket, alone or with d/c/y)
* Added `rows` to a mod's `Input`, a multi-line text field
* Added `classifier_verdict`, `permission_mode` and `classifier_category` to OpenTelemetry `tool_decision` events, so auto mode classifier decisions can be told apart from permission rules
* Added OpenTelemetry tracing guidance to the `claude-api` skill
* [VSCode] Added LaTeX math rendering in Claude's responses
* [VSCode] Added a "Get more usage" link to the usage-limit banner for Pro and Max plans

#### Existing feature improvements

* Switching to a model with a smaller context window now summarizes a too-long conversation with the previous model first
* Faster rendering while a long-running subagent works
* Artifacts: pages now paint the band above a sticky header in the mobile apps
* Mods: in VS Code and the desktop and mobile apps, a tree above the question dialog can hold Markdown and up to 48 rows
* A mod hook's `.catch` handler now runs only when the hook throws or times out
* A mod's `$.env.set` now resolves with `{}` or `{ deny }`

#### Major bug fixes

* Fixed quitting removing a `WorktreeCreate` hook worktree without asking when it may hold unpushed commits
* Fixed the `fable` and `best` aliases erroring when the newest Fable model isn't available to your organization (Claude Code now retries once on the previous Fable model)
* Fixed a misleading "Please run /login" error when a full disk blocks the login refresh
* Fixed Grep and Glob reporting no matches when the search program failed
* Fixed conversations being compacted repeatedly behind an LLM gateway whose responses name a different model
* Fixed the Read tool reading binary files such as .xlsm, .parquet, .epub and .heic as text
* Fixed sign-in refresh timeouts and unexpected sign-outs after short commands exited mid-refresh
* Fixed skills and commands with very many or very long argument names stalling or using large amounts of memory
* Fixed vim mode staying in INSERT after Escape, and Esc discarding a typed AskUserQuestion answer
* Fixed artifact updates being refused where a PreToolUse hook covers Edit or Write
* [VSCode] Fixed a conversation that crashes or freezes the panel being reopened on every reload

-----

## Claude Code changes

### New Documents

#### [code-review-costs](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/code-review-costs.md) [[Source](https://code.claude.com/docs/en/code-review-costs)]

Split out of the Code Review page. It covers what Code Review costs, how to view usage and spend on its dashboard, and how to control spend.

#### [code-review-customize](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/code-review-customize.md) [[Source](https://code.claude.com/docs/en/code-review-customize)]

Split out of the Code Review page. It covers how to customize what Code Review checks and reports.

#### [code-review-local](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/code-review-local.md) [[Source](https://code.claude.com/docs/en/code-review-local)]

Covers reviewing a diff, PR, branch or path locally with `/code-review`: effort levels, `--fix`, `--comment`, and `--max-findings`.

#### [code-review-pull-requests](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/code-review-pull-requests.md) [[Source](https://code.claude.com/docs/en/code-review-pull-requests)]

Describes how Code Review behaves on GitHub pull requests: when reviews run, what the inline comments look like, and how to interact with them.

#### [code-review-setup](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/code-review-setup.md) [[Source](https://code.claude.com/docs/en/code-review-setup)]

Setup guide for enabling Code Review on GitHub repositories for Team and Enterprise organizations.

#### [code-review-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/code-review-troubleshooting.md) [[Source](https://code.claude.com/docs/en/code-review-troubleshooting)]

Troubleshooting guide for Code Review problems.

### Changed documents

#### [analytics](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Noted that Code Review has its own dashboard, linking to the usage view. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/analytics.md?plain=1#L12)] [[Source](https://code.claude.com/docs/en/analytics#track-team-usage-with-analytics)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* Turning off feature-flag fetching no longer changes artifact publish or read approval. Only plan mode now triggers the approval prompt before reading another user's artifact. [[line 128](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/artifacts.md?plain=1#L128)] [[Source](https://code.claude.com/docs/en/artifacts#read-an-artifact-shared-with-you)]

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)]

* Added a debugging pointer for the `Instruction file not loaded` notice. [[line 567](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/claude-md.md?plain=1#L567)] [[Source](https://code.claude.com/docs/en/claude-md#claude-isnt-following-my-claudemd)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* The SessionStart dependency install script now hashes `package.json`, `package-lock.json` and itself, and skips `npm install` when none changed. Added how to verify it and when to add more files to the hash. [[lines 486-515](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/cloud-environments.md?plain=1#L486-L515)] [[Source](https://code.claude.com/docs/en/cloud-environments#install-dependencies-with-a-sessionstart-hook)]

#### [code-review](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Rewritten as a shorter overview with an updated description. The detailed content moved to the new setup, pull-requests, local, customize, costs and troubleshooting pages. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/code-review.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/code-review#code-review)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Updated the `/code-review` and `/review` entries to link to the new local review page. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/commands.md?plain=1#L65)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* With feature-flag fetching off, you can't see what a mod draws in the VS Code chat panel. [[line 578](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/env-vars.md?plain=1#L578)] [[Source](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New entries: Remote Control could not renew the connection, response exceeded the output token maximum, `--bg` ambiguity, `--sandbox`/`--no-sandbox` unsupported by `claude remote-control`, and no shell command run due to control characters. [[lines 1158-1172](https://github.com/gpambrozo/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/errors.md?plain=1#L1158-L1172)] [[Source](https://code.claude.com/docs/en/errors#remote-control-requires-the-anthropic-api)]
* New configuration warnings: Instruction file not loaded, reserved MCP server name, managed-settings hooks not loaded, and sandbox allow entries ignored under a managed lock. [[line 5320](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/errors.md?plain=1#L5320)] [[Source](https://code.claude.com/docs/en/errors#configuration-warnings)]
* Image errors now explain the "could not be processed and was removed" message and the pre-v2.1.299 causes of repeats. [[lines 2229-2238](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/errors.md?plain=1#L2229-L2238)] [[Source](https://code.claude.com/docs/en/errors#image-was-too-large)]
* Cybersecurity safeguard flag message updated, with earlier wordings listed by version. [[lines 2815-2834](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/errors.md?plain=1#L2815-L2834)] [[Source](https://code.claude.com/docs/en/errors#safety-measures-flagged-a-cybersecurity-topic)]
* Context-limit errors near 200K tokens can come from an unrecognized model ID. [[line 2173](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/errors.md?plain=1#L2173)] [[Source](https://code.claude.com/docs/en/errors#prompt-is-too-long)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Added LaTeX math rendering: supported syntaxes, copy behavior, and a troubleshooting section for formulas shown as raw LaTeX. Requires v2.1.301. [[lines 201-211](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/ide-integrations.md?plain=1#L201-L211)] [[Source](https://code.claude.com/docs/en/ide-integrations#latex-math-in-responses)]
* Added the "A conversation was not reopened" notice and its recovery options, plus troubleshooting for a panel that stops responding on reload. [[lines 301-313](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/ide-integrations.md?plain=1#L301-L313)] [[Source](https://code.claude.com/docs/en/ide-integrations#a-conversation-was-not-reopened)]
* Added a section on plugins containing mods that draw in the panel, with labels naming the plugin. [[lines 431-447](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/ide-integrations.md?plain=1#L431-L447)] [[Source](https://code.claude.com/docs/en/ide-integrations#plugins-that-draw-in-the-panel)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Documented the vim `%` motion and `d%`/`c%`/`y%` (v2.1.301). [[line 191](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/interactive-mode.md?plain=1#L191)] [[Source](https://code.claude.com/docs/en/interactive-mode#navigation-normal-mode)]

#### [mcp-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/mcp-quickstart.md) [[Source](https://code.claude.com/docs/en/mcp-quickstart)]

* Before v2.1.299, some HTTP server connections timed out at startup regardless of `MCP_TIMEOUT`. [[line 338](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/mcp-quickstart.md?plain=1#L338)] [[Source](https://code.claude.com/docs/en/mcp-quickstart#troubleshooting)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added a debugging pointer for the `Instruction file not loaded` notice. [[line 567](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/memory.md?plain=1#L567)] [[Source](https://code.claude.com/docs/en/memory#claude-isnt-following-my-claudemd)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New section on the "model isn't recognized, context assumed 200k" warning. It explains how to correct the window with `claude update`, `modelOverrides`, `modelPicker`, a `[1m]` suffix, or `CLAUDE_CODE_MAX_CONTEXT_TOKENS`. [[lines 800-819](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/model-config.md?plain=1#L800-L819)] [[Source](https://code.claude.com/docs/en/model-config#correct-the-window-for-a-gateway-or-custom-model-id)]

#### [plugins/mods/admin](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/admin.md) [[Source](https://code.claude.com/docs/en/plugins/mods/admin)]

* Clarified that settings hooks keep working alongside mods. Added that disabling WebFetch does not stop a mod's `http.fetch`, and that `$.process.run` programs are not covered by these controls. [[lines 69-80](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/admin.md?plain=1#L69-L80)] [[Source](https://code.claude.com/docs/en/plugins/mods/admin#know-which-controls-still-apply)]

#### [plugins/mods/api](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* In VS Code, status lines and toasts show above the prompt box and log lines in the conversation. [[line 207](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/api.md?plain=1#L207)] [[Source](https://code.claude.com/docs/en/plugins/mods/api#show-something-without-starting-a-turn)]

#### [plugins/mods/gallery](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/gallery.md) [[Source](https://code.claude.com/docs/en/plugins/mods/gallery)]

* `Code` shows plain text in VS Code, `Svg` draws in Desktop and VS Code, and `focus: true` requests keyboard focus for a pane. [[lines 160-356](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/gallery.md?plain=1#L160-L356)] [[Source](https://code.claude.com/docs/en/plugins/mods/gallery#show-code-and-changes)]

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* New "Draw in the VS Code extension" section. It covers pane docking by panel width, stacked toasts and status lines, plugin labels, no button hotkeys, focus rules, and text limits. [[lines 335-350](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/interface.md?plain=1#L335-L350)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#draw-in-the-vs-code-extension)]
* Element and render-site tables now list VS Code support, and the hotkey table gained a VS Code column. [[lines 430-560](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/interface.md?plain=1#L430-L560)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#build-a-tree-from-elements)]

#### [plugins/mods/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/overview.md) [[Source](https://code.claude.com/docs/en/plugins/mods/overview)]

* Mods now work in the VS Code extension too (extension 2.1.299+ with feature flags fetched). [[lines 19-186](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/overview.md?plain=1#L19-L186)] [[Source](https://code.claude.com/docs/en/plugins/mods/overview#what-a-mod-can-do)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* Render sites table now shows which of Terminal, Desktop and VS Code render each site, with the VS Code requirements. [[lines 220-234](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/reference.md?plain=1#L220-L234)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#render-sites)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* Updated troubleshooting for mods in the VS Code extension.

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* `--sandbox` and `--no-sandbox` were removed in v2.1.300 and now make the server exit with an error. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/remote-control.md?plain=1#L65)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Added a note on control characters in injected `!` commands that stop the whole skill from running. [[line 761](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/skills.md?plain=1#L761)] [[Source](https://code.claude.com/docs/en/skills#control-characters-in-injected-commands)]
* Clarified that after a background forked skill, `/rewind` restores only files Claude had already edited in the conversation. [[line 792](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/skills.md?plain=1#L792)] [[Source](https://code.claude.com/docs/en/skills#run-skills-in-a-subagent)]

#### [slash-commands](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/slash-commands.md) [[Source](https://code.claude.com/docs/en/slash-commands)]

* Same changes as the skills page: control characters in injected commands and `/rewind` behavior after background forked skills. [[lines 761-792](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/slash-commands.md?plain=1#L761-L792)] [[Source](https://code.claude.com/docs/en/slash-commands#control-characters-in-injected-commands)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Same additions as the IDE integrations page: LaTeX math rendering, the "conversation was not reopened" notice, plugins that draw in the panel, and related troubleshooting. [[lines 201-445](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/claude-code/vs-code.md?plain=1#L201-L445)] [[Source](https://code.claude.com/docs/en/vs-code#latex-math-in-responses)]

-----

## API changes

### New Documents

#### [api/compliance/apps/code](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/api/compliance/apps/code.md) [[Source](https://platform.claude.com/docs/en/api/compliance/apps/code)]

New Compliance API reference for Code apps, with the artifacts endpoints (list, delete, download, retrieve version) under `api/compliance/apps/code/artifacts`.

#### [cmek-claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/manage-claude/cmek-claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek-claude-platform-on-aws)]

Guide to using an AWS KMS key as a customer-managed encryption key on Claude Platform on AWS.

#### [choosing-an-environment](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/managed-agents/choosing-an-environment.md) [[Source](https://platform.claude.com/docs/en/managed-agents/choosing-an-environment)]

Helps you decide between an Anthropic-managed cloud environment and a self-hosted sandbox for Managed Agents, and what changes if you switch.

#### [system-prompts/claude-haiku-4-5](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/release-notes/system-prompts/claude-haiku-4-5.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-haiku-4-5)]

Published system prompt for Claude Haiku 4.5. Similar new pages exist for [Claude Sonnet 4.6](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/release-notes/system-prompts/claude-sonnet-4-6.md) and [Claude Sonnet 5.5](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/release-notes/system-prompts/claude-sonnet-5-5.md).

### Changed documents

#### [build-with-claude/fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Fast mode for Claude Opus 5.5 no longer needs the `fast-mode-2026-02-01` beta header or an access request. Opus 5 and Opus 4.8 remain in research preview. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/build-with-claude/fast-mode.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode#ant-retries-4295xx-automatically-and-has-no-per-request-max_retries)]
* New supported models and platforms table, including Microsoft Foundry for Azure-hosted deployments (not Anthropic-hosted). [[lines 17-27](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/build-with-claude/fast-mode.md?plain=1#L17-L27)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode#supported-models-and-platforms)]
* Code samples now use the non-beta `messages.create` API. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/build-with-claude/fast-mode.md?plain=1#L72)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode#basic-usage)]

#### [manage-claude/spend-limits-api](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/manage-claude/spend-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]

* Added SDK and CLI (`ant`) examples across languages for the spend limit endpoints.

#### [manage-claude/user-management](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/manage-claude/user-management.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-management)]

* Added SDK and CLI examples across languages.

#### [managed-agents/vaults](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/managed-agents/vaults.md) [[Source](https://platform.claude.com/docs/en/managed-agents/vaults)]

* Self-hosted sandboxes can get placeholder-to-secret substitution by running your own egress proxy. [[line 135](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/managed-agents/vaults.md?plain=1#L135)] [[Source](https://platform.claude.com/docs/en/managed-agents/vaults#add-a-credential)]

#### [managed-agents/self-hosted-sandboxes-custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/managed-agents/self-hosted-sandboxes-custom-tools.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-custom-tools)]

* Substantially expanded content on custom tools with self-hosted sandboxes.

#### [models/fable-5-1/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/models/fable-5-1/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)]

* Code samples updated to typed model constants (C#, Go, Java), and migration guides for Opus 5.5, Sonnet 5.5 and Haiku 5.5 gained Claude Code migration help.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* October 15 entries: the Compliance API now returns user preferences (Instructions for Claude and Cowork Global instructions) in beta, fast mode for Opus 5.5 is out of research preview, and Opus 5.5 fast mode is available on Microsoft Foundry. [[lines 15-20](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/release-notes/overview.md?plain=1#L15-L20)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-15-2026)]

#### [test-and-evaluate/develop-tests](https://github.com/gpambrozio/ClaudeDocs/blob/cf5513dbc8c51a3107352b884ae982f99f208ee0/docs-md/api/test-and-evaluate/develop-tests.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)]

* Expanded with additional code examples across SDK languages.
