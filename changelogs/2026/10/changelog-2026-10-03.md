# [Claude docs changes for October 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513)]

## Executive Summary
- Claude Code 2.1.288 adds `/code-review --max-findings`, recovery of a prompt cleared with Ctrl+C, agents-view search (Ctrl+F), and many resume, auto mode, plugin and permission fixes (including a dangerous `rm` inside `bash -c` running without a prompt).
- Self-hosted environments can now send model requests to Amazon Bedrock or Google Cloud's Agent Platform, with a new setup guide and a list of what differs from Anthropic API sessions.
- The Claude apps gateway supports certificate client authentication (`private_key_jwt`) for identity providers such as Microsoft Entra, and documents a `431` troubleshooting case for users in many IdP groups.
- `UserPromptSubmit` hooks are now documented as also firing on turns Claude Code starts itself (scheduled tasks, background subagent reports, cross-session messages).
- Plugin publishing docs were reorganized into a step-by-step directory submission flow, and mods gained new pane keyboard contexts and sharing guidance.

## New Claude Code versions

### [2.1.288](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/versions/2.1.288.md)

#### New features

* Added `--max-findings <n>|all` to `/code-review` to report more or fewer findings than the usual limit; the choice is reused until `--max-findings default`
* Added recovery of a prompt cleared with Ctrl+C: pressing Up on the empty prompt brings back the draft, including pasted text and images
* Added Ctrl+F to find a session by name and Alt+↑/↓ to jump between groups in the agents view; both, and rename, can be rebound in keybindings.json
* Added `$.ui.selection()` for mods, returning the text last selected in fullscreen mode
* Added a built-in `gh api` for cloud sessions whose image has no GitHub CLI
* Added a re-authenticate prompt when an MCP server asks for more OAuth scope during a tool call
* Added `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS` to turn structured outputs off for gateways that reject them
* Added a screen reader announcement of the new permission mode when you approve a plan

#### Existing feature improvements

* Auto mode: an overly long conversation is now compacted for the safety classifier instead of prompting for, or failing, every tool call
* `/autocompact` now saves the auto-compact window per model
* The background command time limit now applies only to unattended sessions (`-p`, Agent SDK, CI, cloud)
* `claude project purge` is now `claude purge` (old name still works)
* MCP URL prompts from servers that can't report completion now wait for "I'm done, continue"
* Agents view: Enter on a name filter or Ctrl+F search opens the best-matching session
* Improved Remote Control recovery from an expired server credential
* Improved screen reader mode announcements and `/permissions` number selection
* Improved Bash permission prompts with shorter reasons when part of a command can't be checked

#### Major bug fixes

* Fixed a dangerous `rm` inside `bash -c`/`sh -c` running without a prompt in bypassPermissions mode or under a shell allow rule
* Fixed PreToolUse and PermissionRequest hooks being skipped when matching failed; the call is now blocked
* Fixed a `BASHPID` arithmetic assignment being allowed silently by the Bash permission check
* Fixed mid-response API timeouts failing the turn in non-interactive sessions and subagents
* Fixed long conversations failing with "Prompt is too long" instead of auto-compacting
* Fixed several `--resume` problems: dropped post-compaction context, unsaved last responses, truncated transcripts, and lost thinking from 2.1.286 or earlier sessions
* Fixed path-scoped `.claude/rules` and nested CLAUDE.md files not loading on Write or Edit
* Fixed MCP tool calls sometimes running twice for oversized or unparseable results
* Fixed `/login` reporting success when credentials could not be saved
* Fixed LSP tool calls hanging indefinitely; requests now time out after 60s
* Fixed plugin issues: LSP `${user_config.*}` placeholders not substituted, `git-subdir` installs on older git, GitHub-source installs without an SSH key, and `--plugin-dir` plugins missing "Configure options"
* Fixed `idle_prompt` notification hooks firing while background agents are still running
* Fixed agent-team plugin agents running with default prompt, tools and effort

-----

## Claude Code changes

### Changed documents

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Worktree isolation applies to sessions dispatched from agent view or started with `claude --bg`; a session moved to the background with `←` or `/background` keeps editing where it was. [[lines 525-551](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/agent-view.md?plain=1#L525-L551)] [[Source](https://code.claude.com/docs/en/agent-view#how-file-edits-are-isolated)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* New "Certificate client authentication" section: `token_endpoint_auth_method: private_key_jwt` with a `client_assertion` block (private key and certificate) in place of a client secret, e.g. for Microsoft Entra. Includes `openssl` key creation, IdP upload and gateway.yaml steps; requires v2.1.284+. [[lines 68-143](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L68-L143)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#oidc)]

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* New troubleshooting entry for `431` errors after sign-in when a developer belongs to many IdP groups (256 KiB header limit, `limits.max_request_header_bytes`). [[lines 350-380](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L350-L380)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#troubleshooting)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* `claude project purge` renamed to `claude purge`, with a note about the old name. [[lines 1400-1451](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/claude-directory.md?plain=1#L1400-L1451)] [[Source](https://code.claude.com/docs/en/claude-directory#clear-local-data)]

#### [code-review](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Documented the `--max-findings <n>|all|default` flag (also added to `commands`). [[line 299](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/code-review.md?plain=1#L299)] [[Source](https://code.claude.com/docs/en/code-review#review-a-diff-locally)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_STRUCTURED_OUTPUTS`. [[line 258](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/env-vars.md?plain=1#L258)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_NONSTREAMING_TIMEOUT_RETRIES` limiting re-sends of timed-out non-streaming requests. [[line 318](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/env-vars.md?plain=1#L318)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `MCP_PROTOCOL_NEGOTIATION` now also covers stdio servers. [[line 462](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/env-vars.md?plain=1#L462)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New section for `API Error: Output blocked by content filtering policy`: not retried; rephrase or `/rewind`. [[lines 2697-2711](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/errors.md?plain=1#L2697-L2711)] [[Source](https://code.claude.com/docs/en/errors#output-blocked-by-content-filtering-policy)]
* Notes that the stable release channel may not reach the version a new model requires; switch to the latest channel. [[lines 2399](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/errors.md?plain=1#L2399)] [[Source](https://code.claude.com/docs/en/errors#claude-code-does-not-support-this-model)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `UserPromptSubmit` also fires for scheduled tasks and `/loop` iterations, background subagent reports, and messages from other sessions. [[lines 1287-1292](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/hooks.md?plain=1#L1287-L1292)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit)]
* `idle_prompt` is not sent while a background agent is still running. [[line 2230](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/hooks.md?plain=1#L2230)] [[Source](https://code.claude.com/docs/en/hooks#notification)]
* Clarified how `permissionDecisionReason` is shown for `ask` and for denials in `-p` runs. [[line 1764](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/hooks.md?plain=1#L1764)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New `Pane` and `PaneField` contexts for mod panes. [[lines 63-64](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/keybindings.md?plain=1#L63-L64)] [[Source](https://code.claude.com/docs/en/keybindings#contexts)]
* Reorganized the `ctrl+x` chord list by context, adding the pane chords (arrows, `ctrl+x x`) and how to unbind them. [[lines 527-570](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/keybindings.md?plain=1#L527-L570)] [[Source](https://code.claude.com/docs/en/keybindings#unbind-default-shortcuts)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Channel servers that negotiate MCP revision 2026-07-28 can't deliver channel messages; stdio servers are probed with `MCP_PROTOCOL_NEGOTIATION=auto`, which Anthropic is turning on by default. [[line 391](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/mcp.md?plain=1#L391)] [[Source](https://code.claude.com/docs/en/mcp#push-messages-with-channels)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `availableModels` entries get their own `/model` row depending on provider. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/model-config.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]
* `/autocompact` saves the window per model, in `modelSettings`; the global `autoCompactWindow` still applies to every model. [[lines 755-758](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/model-config.md?plain=1#L755-L758)] [[Source](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New LSP server `requestTimeout` field (default 60000 ms); same in `plugins/manifest-reference`. [[line 332](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins-reference.md?plain=1#L332)] [[Source](https://code.claude.com/docs/en/plugins-reference#lspservers)]

#### [plugins/mods/create](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins/mods/create.md) [[Source](https://code.claude.com/docs/en/plugins/mods/create)]

* Sharing guidance by audience: zip, own marketplace, organization-managed install, or public submission. [[lines 346-352](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins/mods/create.md?plain=1#L346-L352)] [[Source](https://code.claude.com/docs/en/plugins/mods/create#share-your-mod)]

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* Pane keys: Page Up/Down, Home, End scroll; Ctrl+X arrows resize; Ctrl+X X closes. [[lines 498-500](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins/mods/interface.md?plain=1#L498-L500)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#what-each-key-does)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* `tool.describe` can set `isDeferred: true` to put a tool behind tool search. [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins/mods/reference.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#tools)]

#### [plugins/publish](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins/publish.md) [[Source](https://code.claude.com/docs/en/plugins/publish)]

* Directory submission rewritten as steps: confirm eligibility, validate locally with `claude plugin validate --strict`, check what loads where, submit in the developer portal. [[lines 122-148](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/plugins/publish.md?plain=1#L122-L148)] [[Source](https://code.claude.com/docs/en/plugins/publish#ship-updates-to-users)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Removed the v2.1.199 version requirement for masking environment variables (also in `settings-reference`). [[line 406](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/sandboxing.md?plain=1#L406)] [[Source](https://code.claude.com/docs/en/sandboxing#mask-credentials)]

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New "Send model requests to Bedrock or Agent Platform" section: preparing the cloud account and egress, narrowly scoped credentials and their security implications, setting `CLAUDE_CODE_USE_BEDROCK`/`CLAUDE_CODE_USE_VERTEX`, verifying the variables, and what differs from Anthropic API sessions (no server-managed settings, files, model selection, web search/fast mode). [[lines 266-348](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/self-hosted-environments-configuration.md?plain=1#L266-L348)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration#send-model-requests-to-bedrock-or-agent-platform)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* `modelSettings` now accepts a per-model `autoCompactWindow` (100000-1000000 or `"auto"`) alongside `effortLevel` and `maxEffortLevel`. [[lines 1190-1194](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/settings-reference.md?plain=1#L1190-L1194)] [[Source](https://code.claude.com/docs/en/settings-reference#modelsettings)]
* Per-model window takes precedence over the global `autoCompactWindow`. [[line 2736](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/settings-reference.md?plain=1#L2736)] [[Source](https://code.claude.com/docs/en/settings-reference#autocompactwindow)]
* Background session isolation setting now describes sessions moved to the background. [[line 5156](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/settings-reference.md?plain=1#L5156)] [[Source](https://code.claude.com/docs/en/settings-reference#worktreebgisolation)]

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* A newly launched model can require a version newer than the stable channel; apt, dnf and apk installs choose a channel by repository. [[lines 224-231](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/setup.md?plain=1#L224-L231)] [[Source](https://code.claude.com/docs/en/setup#configure-release-channel)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New precedence rule: in a local terminal session a skill replaces a built-in command of the same name, but not its aliases. [[line 183](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/skills.md?plain=1#L183)] [[Source](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name)]
* Clarified how the `effort` frontmatter default is resolved when omitted. [[line 380](https://github.com/gpambrozio/ClaudeDocs/blob/1b7e0d5f8ab3bf25a7786cce272f35ba770f0513/docs-md/claude-code/skills.md?plain=1#L380)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

-----

## API changes

No API documentation changes today.
