# [Claude docs changes for November 2nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/93c351256c450e023d87791e53ebaf1b48760054) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/93c351256c450e023d87791e53ebaf1b48760054)]

## Executive Summary
- New **message threads** beta for the Messages API: the server keeps the conversation, so each turn sends only new messages, giving smaller requests and a lower time to first token in long agent loops.
- New `permissions.blockWritesOutsideWorkingDirectories` setting makes `Write`, `Edit` and `NotebookEdit` refuse paths outside the working directories in every permission mode. It also removes the worktree tools and protects settings files.
- Fast mode for Opus 4.8 is deprecated and will be removed on November 30, 2026. Switch to Opus 5.5 (Claude Code v2.1.280 or later) or run `/fast off`.
- The Claude Apps gateway gained per-team upstream routing with `groups`, Bedrock guardrail input tagging, and `guardrail.trace` logging.
- Per-message effort (beta) is now documented across several models, so you can change effort mid-conversation without invalidating the prompt cache. Java SDK 3.4.0, `ant` CLI 2.5.0 and the other SDKs were bumped.

## New Claude Code versions

No new Claude Code versions in this update.

-----

## Claude Code changes

### Changed documents

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* The `/permissions` **Recently denied** tab is now **Recently blocked**, and retrying is documented as a step-by-step flow: check the command, press `r` to approve, close the dialog. [[lines 354-390](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/auto-mode-config.md?plain=1#L354-L390)] [[Source](https://code.claude.com/docs/en/auto-mode-config#review-denials)]
* Approving doesn't add a permission rule, so a retried action can be blocked again. You can also approve for later with `Enter` then `Esc`, take back an approval, or discard with `Ctrl+C` twice. Rows that read "This row can't be approved here" can't be approved. [[lines 356-385](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/auto-mode-config.md?plain=1#L356-L385)] [[Source](https://code.claude.com/docs/en/auto-mode-config#review-denials)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New "Send each team to its own upstream" section: give upstreams a `groups` list so only developers in those IdP groups reach them. An upstream without `groups` is open to everyone, so list it last. [[lines 775-850](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L775-L850)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#send-each-team-to-its-own-upstream)]
* Failover rules clarified: a request moves past an upstream only if it failed, doesn't serve the model, or its `groups` list excludes the developer. Model-scoped and built-in model routing were also described. [[lines 708-770](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L708-L770)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#multiple-upstreams)]
* New Bedrock guardrail `input_tagging` option (`last_message`, `user_messages`, `all_messages`, `all_messages_and_system`). Without it, Bedrock filters that need tagged input don't run. Limits are listed, such as tool results and images not being covered. [[lines 368-440](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L368-L440)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#apply-an-amazon-bedrock-guardrail)]
* New `guardrail_trace: true` upstream option logs a `guardrail.trace` event showing which filter fired, without the matched text. [[lines 410-450](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L410-L450)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#what-input-tags-dont-cover)]
* Notes for `assume_role` upstreams: without `groups`, every admitted developer can use the upstream. [[line 494](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L494)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#bedrock-in-another-aws-account)]

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* Added the `guardrail.trace` log stream. [[line 168](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L168)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#logs)]
* Warning for rollbacks: removing only the `groups` key from an upstream leaves it open to every developer. [[lines 311-314](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L311-L314)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#upgrades)]
* Troubleshooting entry for `400 you aren't in a group that can use this gateway`. Upstream `groups` now count among the groups to keep when trimming the groups claim. [[lines 426-459](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L426-L459)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#troubleshooting)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* New table of Claude Code settings that behave differently in the Desktop Code tab, for example `defaultShell`, `fileSuggestion`, `modelPicker` and `prUrlTemplate`. [[lines 1947-1968](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/desktop.md?plain=1#L1947-L1968)] [[Source](https://code.claude.com/docs/en/desktop#claude-code-settings-that-behave-differently-in-the-code-tab)]
* In SSH sessions Claude has no Browser pane tools, so it can't open your app or auto-verify changes. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/desktop.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/desktop#preview-your-app)]
* Diagnostics now also ask for `remote-server.log.old`, which is lost the next time the helper restarts. [[lines 2302-2307](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/desktop.md?plain=1#L2302-L2307)] [[Source](https://code.claude.com/docs/en/desktop#get-desktops-logs-for-an-ssh-problem)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New error "Claude Code didn't send your claude.ai login": an administrator's `apiKeyHelper` isn't in effect, and Claude Code refuses prompts. [[lines 1077-1089](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/errors.md?plain=1#L1077-L1089)] [[Source](https://code.claude.com/docs/en/errors#claude-code-didnt-send-your-claudeai-login)]
* New entries for write refusals caused by `permissions.blockWritesOutsideWorkingDirectories`, covering paths outside working directories and Claude Code settings files, with remedies such as `/add-dir`. [[lines 4579-4618](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/errors.md?plain=1#L4579-L4618)] [[Source](https://code.claude.com/docs/en/errors#setting-blocks-writes-outside-the-working-directories)]
* Auto mode "no usable answer" row clarified, including when the server gave no verdict. [[line 675](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/errors.md?plain=1#L675)] [[Source](https://code.claude.com/docs/en/errors#auto-mode-cannot-determine-the-safety-of-an-action)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Fast mode for Opus 4.8 was deprecated on October 30, 2026, and will be removed on November 30, 2026. Switch to Opus 5.5 with `/model` (needs v2.1.280 or later) to keep fast mode, or run `/fast off`. [[lines 13-19](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/fast-mode.md?plain=1#L13-L19)] [[Source](https://code.claude.com/docs/en/fast-mode#speed-up-responses-with-fast-mode)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Writes outside the working directories are never auto-approved while `blockWritesOutsideWorkingDirectories` is on. Settings-file writes are refused in every mode. [[lines 40, 738-739](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/permission-modes.md?plain=1#L40)]
* `remote-settings.json` and its sync and consent files are now protected files. [[line 778](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/permission-modes.md?plain=1#L778)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]
* Renamed "Recently denied" to "Recently blocked". [[lines 553-555](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/permission-modes.md?plain=1#L553-L555)] [[Source](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* New section "Block file-tool reads and writes outside the working directories" covering `blockReadsOutsideWorkingDirectories` and the new `blockWritesOutsideWorkingDirectories`. [[lines 669-677](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/permissions.md?plain=1#L669-L677)] [[Source](https://code.claude.com/docs/en/permissions#block-file-tool-reads-and-writes-outside-the-working-directories)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* New section explaining when a machine's `apiKeyHelper` isn't in effect while server-managed settings are the selected source, and how to clear the resulting refusal (v2.1.314 or later). [[lines 156-164](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/server-managed-settings.md?plain=1#L156-L164)] [[Source](https://code.claude.com/docs/en/server-managed-settings#when-a-machines-apikeyhelper-isnt-in-effect)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `permissions.blockWritesOutsideWorkingDirectories` is a restrictive key honored from any scope, even when managed settings set `false` (v2.1.314 or later). [[line 306](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/settings.md?plain=1#L306)] [[Source](https://code.claude.com/docs/en/settings#exceptions-to-managed-settings-precedence)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `permissions.blockWritesOutsideWorkingDirectories` entry: scope, type, default, a test procedure, and what stays writable (plan files, scratchpad and similar). It also removes the worktree tools. The write block is on by default while managed `permissions` can't be read. [[lines 1092-1133](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/settings-reference.md?plain=1#L1092-L1133)] [[Source](https://code.claude.com/docs/en/settings-reference#permissionsblockwritesoutsideworkingdirectories)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Git is listed as an optional requirement: `claude plugin eval` needs git 2.31 or later, and uploading a local repository to a cloud session has its own git requirement. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/setup.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/setup#additional-dependencies)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New "EnterWorktree tool behavior" section: which `path` values are accepted (including nested repositories), when approval is prompted for paths outside `.claude/worktrees/`, restrictions from inside a worktree, and the tool's removal when writes are blocked. [[lines 298-306](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/tools-reference.md?plain=1#L298-L306)] [[Source](https://code.claude.com/docs/en/tools-reference#enterworktree-tool-behavior)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* New troubleshooting section "Claude has no `EnterWorktree` tool" with workarounds: `claude --worktree`, `claude --bg --worktree`, `worktree.bgIsolation: "none"`, and `git worktree add`. [[lines 51-64](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/worktrees.md?plain=1#L51-L64)] [[Source](https://code.claude.com/docs/en/worktrees#claude-has-no-enterworktree-tool)]
* Background sessions' edits to the main checkout are blocked. To change those files, edit them yourself or start an interactive session there. [[line 104](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/claude-code/worktrees.md?plain=1#L104)] [[Source](https://code.claude.com/docs/en/worktrees#how-claude-code-enforces-isolation)]

-----

## API changes

### New Documents

#### [message-threads](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/message-threads.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/message-threads)]

New beta feature (header `message-threads-2026-08-12`) for the Messages API. You send the full conversation once with your system prompt and tools. Later turns send only the new messages and the previous response `id`, and the API rebuilds the conversation server-side. This gives smaller requests and a lower, steadier time to first token in long agent loops. A thread expires 5 minutes after its last request and is deleted within 1 hour. The page covers SDK helpers, using the `thread` field directly, prompt caching, streaming, recovering from threads that can't be continued, compaction, errors, unsupported features, pricing and rate limits, and availability. The feature is not ZDR or HIPAA eligible, and it is available on the Claude API, Claude Platform on AWS, Claude Models on Google Cloud (Anthropic managed) and Microsoft Foundry.

### Changed documents

#### [api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Message threads added to the feature eligibility table: not ZDR or HIPAA eligible, with contents held encrypted in memory and deleted within 1 hour. [[lines 197-206](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L197-L206)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#messages-api-features)]

#### [effort](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Effort is now listed as stable on Claude Models on Google Cloud (Anthropic managed). The availability table now reads "All supported platforms". [[lines 31, 710-712](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/effort.md?plain=1#L31)]
* Per-message effort (beta) is documented with its supported models and platforms. Claude Haiku 5.5 can change effort mid-conversation while preserving the prompt cache. [[lines 286-397](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/effort.md?plain=1#L286-L397)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels)]

#### [anthropic-managed](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed)]

* Adaptive thinking and effort are added to the supported-features list. [[lines 518-519](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/claude-models-on-google-cloud/anthropic-managed.md?plain=1#L518-L519)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed#feature-support)]

#### [extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Clarified how each platform handles the interleaved-thinking beta header. [[line 316](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L316)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking#interleaved-thinking-in-manual-mode)]

#### [mid-conversation-system-messages](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* A `role: "system"` message can carry `output_config.effort` to change effort mid-conversation (beta). [[line 1656](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L1656)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#how-it-works)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Message threads added to the capability table. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/overview.md?plain=1#L92)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview#messages-api-features)]

#### [preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* Changing top-level `output_config.effort` doesn't invalidate thinking but does restart the prompt cache. [[line 1240](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L1240)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#change-effort-with-a-per-message-output_config)]

#### [prompting-claude-haiku-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5)]

* Changing top-level effort between requests invalidates the prompt cache, so use per-message effort changes instead where available. [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5.md?plain=1#L41)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-haiku-5-5#use-effort-to-control-thinking)]

#### [thinking-steering-and-cost](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/thinking-steering-and-cost.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)]

* On Claude Haiku 5.5 the discouraging phrase doesn't reliably reduce thinking. Use per-message effort instead. [[line 97](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/thinking-steering-and-cost.md?plain=1#L97)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost#per-message-steering)]

#### [vision](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* The FAQ on image storage now points to API and data retention, and notes that Files API uploads can be deleted. [[line 1368](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/vision.md?plain=1#L1368)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision#faq)]

#### [whats-new-fable-5-1](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)]

* Fable 5.1 supports per-message effort changes (beta) without invalidating the prompt cache. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md?plain=1#L93)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#change-effort-mid-conversation-beta)]

#### [working-with-messages](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/working-with-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)]

* Notes that message threads (beta) let the API keep the conversation, so later requests send only new messages. [[lines 188-189](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/build-with-claude/working-with-messages.md?plain=1#L188-L189)] [[Source](https://platform.claude.com/docs/en/build-with-claude/working-with-messages#multiple-conversational-turns)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/cli-sdks-libraries/overview.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)]

* SDK and CLI versions updated: ant CLI 2.5.0, Python 2.4.0, TypeScript 1.4.0, C# 13.4.0, Go 2.5.0, Java 3.4.0, PHP 1.4.0, Ruby 2.4.0. Java 3.4.0 and CLI 2.5.0 are also reflected in the quickstarts and the cloud-platform pages. [[lines 59-66](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/cli-sdks-libraries/overview.md?plain=1#L59-L66)] [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview#latest-versions)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* November 2, 2026 release note announcing message threads in beta. [[lines 15-18](https://github.com/gpambrozio/ClaudeDocs/blob/93c351256c450e023d87791e53ebaf1b48760054/docs-md/api/release-notes/overview.md?plain=1#L15-L18)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-2-2026)]
