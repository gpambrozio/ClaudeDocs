# [Claude docs changes for September 4th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/663b84bc5824b3da59620c346738a7c1360300f7) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/663b84bc5824b3da59620c346738a7c1360300f7)]

## Executive Summary
- A large swathe of the API guides regained content that had been missing from their Markdown source — code examples, language tabs and FAQ sections across `develop-tests` (+505 lines), `prompt-caching` (+404), `increase-consistency` (+332), `text-editor-tool`, `bash-tool`, `computer-use-tool`, `handle-tool-calls`, `structured-outputs` and more
- New `--permission-prompts none` flag for unattended runs: denies anything that would prompt, removes `AskUserQuestion` from the session entirely, cancels unanswered MCP elicitations, and tells Claude not to retry
- Auto mode now asks once before the first file read outside the working directories, and answering "block from now on" writes `permissions.blockReadsOutsideWorkingDirectories: true` to your user settings — which then refuses such reads in **every** mode, `bypassPermissions` included
- A managed settings document that can't be parsed as a JSON object now makes Claude Code **refuse to start** — deliberately failing closed, even when another admin source carries a valid policy
- On Fable 5.1 with an API key or Claude subscription, changing effort mid-session no longer invalidates the prompt cache (2.1.260), and two new weekly "What's new" pages land for weeks 33 and 34

## New Claude Code versions

### [2.1.260](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/versions/2.1.260.md)

#### New features

* Added a diff panel that opens beside the conversation in fullscreen mode and shows uncommitted changes as Claude edits; toggle it with `/diff`
* Added a likely cause for prompt-cache misses to `/cost` and the status line's `prompt_cache` field
* Added `/reload-plugins` to headless sessions, so it appears in the Desktop and SDK command lists
* Added a text form of `/advisor` for the desktop app, Remote Control and other headless sessions
* Added `oidc.scope_on_refresh` to the Claude apps gateway for IdPs that return an id_token on refresh only when asked for `openid` again

#### Existing feature improvements

* Improved `/effort` on Claude Fable 5.1 so changing effort mid-session no longer invalidates the prompt cache
* Improved auto-compact for 1M-context models: Opus and Fable sessions compact shortly before the 1M limit, and recovery compaction on very large contexts no longer times out at 10 minutes
* Improved deleting a background session whose worktree has unpushed commits: the message names the branch and commit count, and deleting again discards the worktree
* Improved `/ultrareview` to wait up to 45 minutes for long-running cloud reviews, up from 30
* Improved idle CPU usage of non-interactive sessions
* Changed `ctrl+l` / `cmd+k` in fullscreen to clear the transcript view like a terminal `clear`
* Changed a managed CLAUDE.md (`claudeMd`) to no longer trigger the security approval dialog
* Changed commands typed at the `!` bash-mode prompt to run outside the sandbox even under strict sandbox mode
* Changed permission rules with text after the closing parenthesis to be reported as invalid rather than silently ignored
* Removed the one-hour time limit on background commands started by subagents

#### Major bug fixes

* Fixed `Edit`/`Write`/`Read` permission rules whose path contains parentheses being dropped as invalid or ignored by the Bash sandbox, **which left "read-only" folders writable**
* Fixed one file permission rule with an uncompilable pattern making every file edit fail with `Invalid regular expression`
* Fixed Bash permission checks auto-approving zsh commands hiding a command substitution in a `REPORTTIME`, `REPORTMEMORY` or `DIRSTACKSIZE` assignment
* Fixed prompt caching on Claude Fable 5.1 not covering the context attached after tool results, so it was re-sent uncached on every tool-call turn
* Fixed the `/model` picker not showing Fable 5.1 for organizations that can use it
* Fixed `model: fable` agents ignoring the `[1m]` tag on an `ANTHROPIC_DEFAULT_FABLE_MODEL` pin and silently running at 200K
* Fixed `permissions.blockReadsOutsideWorkingDirectories` on macOS hiding the user's git config from sandboxed git
* Fixed Bedrock model discovery and AWS SSO/STS calls failing with "unable to get local issuer certificate" when the corporate root CA is only in the OS certificate store
* Fixed `/rewind` reporting success when checkpoint backup files were missing and nothing was restored
* Fixed managed `skillOverrides` keyed on a bundled skill's alias not applying, and `Skill(name)` deny rules not covering a nested skill
* Reverted the 2.1.259 change applying `Read()` deny rules to Bash arguments, which denied `npm run build` under a `Read(./**/build/**)` rule in every mode

-----

## Claude Code changes

### New Documents

#### [whats-new/2026-w33](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/whats-new/2026-w33.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w33)]

Week 33 (August 10–14, v2.1.225 → v2.1.233): auto-continue when usage limits reset, fork mode on by default (`CLAUDE_CODE_FORK_SUBAGENT=0` to turn it off), and GitLab merge requests and marketplaces — bare `gitlab.com` marketplace clones including nested subgroups, `—worktree` from a merge request URL, `!N` labels in `claude agents`, and redaction of `glpat-`/`glrt-` token families.

#### [whats-new/2026-w34](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/whats-new/2026-w34.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w34)]

Week 34 (August 17–21, v2.1.234 → v2.1.239): the `/design` skill bringing Claude Design's artboard workflow into the CLI (research preview), the **Concise** built-in output style, and Remote Control leaving research preview with machines appearing as device cards at the top of the Code tab in the Claude app. Plus a long "Other wins" list including the `spellcheck` setting, the `MR !N` GitLab badge, opening `/permissions` while Claude is working, `ANTHROPIC_DEFAULT_MODEL`, `notify_when_idle` on `SendMessage`, `keybindingFlavor: "readline"`, and cross-session messaging on native Windows.

### Changed documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* Toggling `/advisor` mid-session does **not** invalidate the main model's prompt cache, unlike switching models; the advisor's guidance is cached as part of the transcript on later turns. [[line 127](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/advisor.md?plain=1#L127)] [[Source](https://code.claude.com/docs/en/advisor#impact-on-prompt-caching)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* New `terminal_reason` field on results, with `"aborted_streaming"` and `"aborted_tools"` marking a turn aborted before completing — commonly by `interrupt()` or a permission callback denying with `interrupt=True`. [[line 1540](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/agent-sdk/python.md?plain=1#L1540)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)]

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* A running gateway serves its own protocol reference at `GET /protocol`, covering SSO sign-in, inference, managed settings delivery, model discovery and telemetry — a separate document from the general compatibility guide. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/claude-apps-gateway.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway#other-gateway-implementations)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--permission-prompts` flag (`host` by default, or `none`), requiring v2.1.259. [[line 102](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/cli-reference.md?plain=1#L102)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* New **API credentials** feature, on Pro and Max plans only: store a key once on the environment and the agent proxy attaches it to requests for hosts you list, so sessions never see it. Environment variables, by contrast, are readable by anyone who uses the environment. Team and Enterprise plans don't have this yet, so the section doesn't appear there. [[lines 63-68](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/cloud-environments.md?plain=1#L63-L68)] [[Source](https://code.claude.com/docs/en/cloud-environments#set-environment-variables)]
* Shared organization environments documented as editable by an Owner from the environment selector and read-only to other members, with an explicit warning against secrets in their variables. [[lines 143-144](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/cloud-environments.md?plain=1#L143-L144)] [[Source](https://code.claude.com/docs/en/cloud-environments#organization-shared-environments)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "Managed settings document could not be parsed" section. Claude Code **exits with code 1 at startup** when a deployed managed document is present but unparseable, naming the source — a file path, a macOS managed preferences profile, or the HKLM registry value. It refuses even when another admin source delivers a valid policy, and the page states the reasoning plainly: settings it can't parse can't be enforced, so starting anyway would run sessions without the organization's controls. An empty `managed-settings.json` counts as `{}` and doesn't block launch. [[lines 2931-2952](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/errors.md?plain=1#L2931-L2952)] [[Source](https://code.claude.com/docs/en/errors#managed-settings-document-could-not-be-parsed)]
* Cut-off responses now have four cases where Claude Code handles the failure without showing the incomplete-response notice, including prompting a subagent to continue — before v2.1.257 a subagent showed the notice on the first cut-off. [[lines 367-372](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/errors.md?plain=1#L367-L372)] [[Source](https://code.claude.com/docs/en/errors#the-response-above-may-be-incomplete)]

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New "Turn off permission prompts in unattended runs" section. `--permission-prompts none` matters most when the run *has* a permission host — an SDK `canUseTool` callback or a `--permission-prompt-tool` — because without it the run waits on that host. With the flag, Claude Code removes tools needing a human answer such as `AskUserQuestion` so Claude can't call them, cancels any MCP elicitation no `Elicitation` hook answers, and tells Claude not to retry. Permission rules, `PermissionRequest` hooks and the permission mode still decide every call first. [[lines 243-256](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/headless.md?plain=1#L243-L256)] [[Source](https://code.claude.com/docs/en/headless#turn-off-permission-prompts-in-unattended-runs)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Retitled "Claude Code gateway compatibility guide" and positioned as the operator reference across the gateway pages: what Claude Code sends, the headers and fields to forward, and what breaks when they're stripped. [[lines 1-4](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L1-L4)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#claude-code-gateway-compatibility-guide)]

#### [llm-gateway-rollout](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/llm-gateway-rollout.md) [[Source](https://code.claude.com/docs/en/llm-gateway-rollout)]

* Rate-limit sizing guidance: account for the client retrying transient failures, `429`s included, up to 10 times with backoff while honoring `Retry-After`. [[line 234](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/llm-gateway-rollout.md?plain=1#L234)] [[Source](https://code.claude.com/docs/en/llm-gateway-rollout#maintain-the-gateway)]

#### [managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/managed-settings.md) [[Source](https://code.claude.com/docs/en/managed-settings)]

* A precise account of the validation ladder: individual repairable entries are skipped with a warning, then any top-level key still failing is dropped, and every remaining valid key is enforced. A `policyHelper`'s `managedSettings` is held to a stricter standard — any surviving schema violation fails the whole run and refuses startup. [[lines 241-242](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/managed-settings.md?plain=1#L241-L242)] [[Source](https://code.claude.com/docs/en/managed-settings#find-entries-claude-code-dropped)]
* Exactly what makes each source unparseable, and the three states that don't cause a refusal: an absent source, an empty file (`{}`), and a malformed value in the user-writable HKCU key, which is reported as a notice instead. [[lines 243-253](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/managed-settings.md?plain=1#L243-L253)] [[Source](https://code.claude.com/docs/en/managed-settings#find-entries-claude-code-dropped)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New troubleshooting section "A new session starts on a different model than you picked", with four causes — a one-session choice (`s`, `--model`, `/model` in `-p`), something higher-priority setting the model, a `~/.claude/settings.json` Claude Code couldn't write to, and resuming a session that keeps its own model. [[lines 163-170](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/model-config.md?plain=1#L163-L170)] [[Source](https://code.claude.com/docs/en/model-config#a-new-session-starts-on-a-different-model-than-you-picked)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* New "The first read outside the working directories" section. In auto mode, the first Read, Grep or Glob on an outside path asks you once. **"Block from now on" writes `permissions.blockReadsOutsideWorkingDirectories: true` into your user settings**, which makes the file tools refuse such reads in every later session and every permission mode — reversible only by `/add-dir` or removing the setting. The prompt never appears in `-p` runs or background sessions. [[lines 326-334](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/permission-modes.md?plain=1#L326-L334)] [[Source](https://code.claude.com/docs/en/permission-modes#first-read-outside-the-working-directories)]
* Reads fenced by that setting are added to the actions no mode auto-approves — they prompt even in auto mode and `bypassPermissions`. [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/permission-modes.md?plain=1#L32)] [[Source](https://code.claude.com/docs/en/permission-modes#actions-no-mode-auto-approves)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* The built-in read-only Bash command set is now explicitly fenced by `blockReadsOutsideWorkingDirectories`. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/permissions.md?plain=1#L209)] [[Source](https://code.claude.com/docs/en/permissions#read-only-commands)]
* Plan mode no longer substitutes sandboxed commands; built-in read-only commands still run unprompted, and a bare `Bash` ask rule makes every command prompt, sandboxed read-only ones included. Before v2.1.212 the substitution applied in plan mode too. [[line 496](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/permissions.md?plain=1#L496)] [[Source](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* New "Changing effort level" guidance. On most models a mid-session effort change recomputes the entire request, so Claude Code asks you to confirm while the cache is warm. **On Fable 5.1 with an API key or Claude subscription the cache survives and no confirmation appears** — but not on Bedrock, Agent Platform or a Claude apps gateway, nor under `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` or a HIPAA configuration. Before v2.1.260 it invalidated the cache there too. [[lines 73-75](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/prompt-caching.md?plain=1#L73-L75)] [[Source](https://code.claude.com/docs/en/prompt-caching#changing-effort-level)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* To be prompted on every unsandboxed retry even in auto mode, add an ask rule for `Bash(dangerouslyDisableSandbox:true)`. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/sandboxing.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/sandboxing#the-unsandboxed-retry-escape-hatch)]
* Recommends `blockReadsOutsideWorkingDirectories` over hand-written path rules for denying sandboxed commands access to home directories and mounted volumes. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/sandboxing.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/sandboxing#configure-sandboxing)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* A managed CLAUDE.md via `claudeMd` no longer requires approval, on the reasoning that it's instruction text rather than a command Claude Code runs — permissions still gate the tools Claude uses while following it. Before v2.1.260 it required approval. [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/server-managed-settings.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/server-managed-settings#security-approval-dialogs)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `permissions.blockReadsOutsideWorkingDirectories` entry: refuses outside reads through Read, Grep, Glob and LSP in every permission mode including `bypassPermissions`, and makes a recognized file-reading Bash command such as `cat` prompt even in auto mode. Requires v2.1.257. [[lines 957-960](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/settings-reference.md?plain=1#L957-L960)] [[Source](https://code.claude.com/docs/en/settings-reference#permissions-blockreadsoutsideworkingdirectories)]
* The settings count rose to 223. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/settings-reference.md?plain=1#L19)] [[Source](https://code.claude.com/docs/en/settings-reference#all-settings)]

#### [security](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* The working-directory boundary now covers reads: in Manual mode Claude Code asks before reading outside it with Read, Grep and Glob. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/security.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/security#built-in-protections)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `PermissionRequest` hooks documented as receiving a `permission_suggestions` array, which a hook can echo back as its own `updatedPermissions` output — with the caveat that the array isn't an exact list of the options a user sees. [[lines 1677-1756](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/hooks.md?plain=1#L1677-L1756)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-input)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* The retention sweep pauses with `result: "skipped"` and a `skip_reason` when the retention period can't be determined safely; a managed `cleanupPeriodDays` pins it and lets the sweep run even when a lower-priority settings file is broken. [[line 1043](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/monitoring-usage.md?plain=1#L1043)] [[Source](https://code.claude.com/docs/en/monitoring-usage#retention-sweep-event)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* API credentials added to the list of things that stay outside the sandbox, attached to matching requests after they leave the session — Pro and Max only. [[line 266](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L266)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#security-and-isolation)]

-----

## API changes

### Changed documents

The dominant change on the API side is a restoration: a dozen guide pages regained substantial content that had been absent from their Markdown source — worked code examples with their `Python`/`TypeScript`/`C#`/`Go`/`Java`/`PHP`/`Ruby` language tabs, request and response bodies, and FAQ sections.

#### [test-and-evaluate/develop-tests](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/test-and-evaluate/develop-tests.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests)]

* The page grew from 124 to 629 lines, gaining its full grading-method walkthrough: exact match, cosine similarity with SBERT, ROUGE-L, LLM-based Likert scale, binary classification for PHI detection, and ordinal scales for context utilization — each with what it measures, example test-case counts, and runnable code. [[lines 123-441](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/test-and-evaluate/develop-tests.md?plain=1#L123-L441)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#task-fidelity-sentiment-analysis-exact-match-evaluation)]
* Also regained the criteria questions that open the page: task fidelity, consistency, relevance, tone and style, privacy preservation, context utilization, latency and cost. [[lines 61-89](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/test-and-evaluate/develop-tests.md?plain=1#L61-L89)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/develop-tests#task-fidelity)]

#### [build-with-claude/prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Regained its worked examples and FAQ, including the four-breakpoint example and the advice that **a single breakpoint at the end of your static content is usually sufficient** — place it on the last block that stays identical across requests. [[lines 877-932](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L877-L932)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#putting-it-all-together-multiple-cache-breakpoints)]
* An easily-missed point is now spelled out: `input_tokens` does **not** represent all input tokens, only the portion after your last cache breakpoint, so with a 200k document cached it will look much smaller than your real input. [[lines 946-967](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L946-L967)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#how-do-i-calculate-total-input-tokens-from-the-usage-fields)]
* The 5-minute TTL is measured from the **start** of the request that writes or reads the entry, not the end of its response, so generation time eats into the reuse window — a reason to reach for the 1-hour TTL when responses are long. [[lines 977-979](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L977-L979)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#when-does-the-cache-lifetime-start)]
* Cache breakpoints themselves are free; only cached and read content is billed, so the number of breakpoints doesn't affect pricing. [[lines 936-942](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L936-L942)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#do-cache-breakpoints-add-extra-cost)]
* Tool-definition caching documented: place `cache_control` on the last tool in `tools`, and everything up to and including it caches as one prefix. [[lines 677-712](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L677-L712)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#caching-tool-definitions)]

#### [agents-and-tools/tool-use/bash-tool](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/agents-and-tools/tool-use/bash-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]

* Regained its request and result examples, including the `restart` invocation and the timeout error shape. [[lines 100-333](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/agents-and-tools/tool-use/bash-tool.md?plain=1#L100-L333)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool#example-usage)]

#### [agents-and-tools/tool-use/text-editor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/agents-and-tools/tool-use/text-editor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)]

* 179 net-new lines of command examples and error handling, taking the page from 515 to 738 lines.

#### [agents-and-tools/tool-use/handle-tool-calls](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]

* 139 net-new lines restoring the worked tool-result loop across every SDK language.

#### [agents-and-tools/tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* 102 net-new lines of action examples and screenshots handling.

#### [build-with-claude/structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Regained the empty-response troubleshooting (common causes and prevention) and the explicit list of supported and unsupported regex features. [[lines 81-450](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L81-L450)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#quick-start)]

#### [strengthen-guardrails/increase-consistency](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/test-and-evaluate/strengthen-guardrails/increase-consistency.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/increase-consistency)]

* 332 lines restored, the largest gain outside `develop-tests`.

#### [cli-sdks-libraries/cli/scripting](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/cli-sdks-libraries/cli/scripting.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/scripting)]

* Moved in the other direction, shrinking from 236 to 159 lines: the YAML-resource version-control walkthrough — defining a `summarizer.agent.yaml` and creating it with `ant beta:agents create` — was removed from this page.

#### [cli-sdks-libraries/sdks/go](https://github.com/gpambrozio/ClaudeDocs/blob/663b84bc5824b3da59620c346738a7c1360300f7/docs-md/api/cli-sdks-libraries/sdks/go.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/sdks/go)]

* 173 net-new lines of Go SDK examples.
