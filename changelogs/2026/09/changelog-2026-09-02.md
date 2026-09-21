# [Claude docs changes for September 2nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/96e439024f9a4be47b492c3943f3834a50040738) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/96e439024f9a4be47b492c3943f3834a50040738)]

## Executive Summary
- **Claude Fable 5.1 and Claude Mythos 5.1 launch**, with ten new API pages. Same input/output price as Fable 5 ($10/$50 per MTok) but cache reads drop to a quarter ($0.25/MTok), 1M context, 128K max output, and `high` default effort
- **Three breaking changes for existing Fable 5 callers**: forced tool use (`tool_choice` `any`/`tool`) now returns a 400; earlier models can't read Fable 5.1's thinking blocks; and editing anything before a thinking block invalidates it — enforced for accounts created on or after August 31, 2026
- Three new beta capabilities that all exist to keep a conversation append-only: **per-message effort** (change effort mid-conversation without losing the prompt cache), **turn-scoped system messages** (`clear_at: "next_user_message"`), and **`thinking.display: "updates"`** to receive progress updates as text while reasoning stays hidden
- Fable 5.1 text now carries Anthropic's statistical watermark on every platform, and images and video retrieved through the Files API carry signed C2PA Content Credentials
- Claude Code 2.1.257 makes `fable` resolve to Fable 5.1, adds a Containment Escape auto-mode rule for cloud metadata-credential fetches and egress evasion, and adds `timeFormat`/`timeZone` settings

## New Claude Code versions

### [2.1.257](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/versions/2.1.257.md)

#### New features

* Added Claude Fable 5.1 (`claude-fable-5-1`) as the default Fable model
* Added "Time format" (`timeFormat`) and `timeZone` settings: 12-hour, 24-hour, 24-hour UTC, or a strftime pattern
* Added a Containment Escape rule to auto mode, so cloud metadata-credential fetches, egress evasion and cross-tenant reach are no longer auto-approved unless the environment marks them expected
* Added `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` to apply one model to every subagent, ignoring per-spawn and agent-definition overrides
* Added a one-time auto-mode prompt before the first file read outside the working directories, with `permissions.blockReadsOutsideWorkingDirectories` to block such reads
* Added `s` in `/effort` to change effort for the current session only, matching `/model`
* Added a `/doctor` warning for stale sandbox mask files left by a killed session

#### Existing feature improvements

* Improved rendering performance: less re-render work per turn in long conversations, and streaming no longer slows as the reply grows
* Improved `/fork` to keep the original conversation's prompt cache in the new background session
* Improved `/code-review --comment` to post findings on GitLab merge requests via `glab mr note`
* Improved MCP connection and OAuth logs so credentials in a server's URL or headers are redacted
* Changed `--effort` to lift a new model's default-effort hold for that session only rather than permanently
* Changed `defaultMode: "bypassPermissions"` in project or local settings to be ignored, like `"auto"`
* Changed `fable` and `best` in Claude apps gateway sessions to keep resolving to Fable 5 for now, since gateways not yet configured for Fable 5.1 reject it
* Changed Cowork and cloud sessions so reading an artifact that isn't yours always asks first, even in auto mode
* Changed `/btw` history browsing from `←`/`→` to `Shift+←`/`Shift+→`
* Removed the Ctrl+E command explanation on Bash and PowerShell permission prompts

#### Major bug fixes

* Fixed plugins being able to read files outside their own directory through a symlinked component path
* Fixed a `permissions.ask` rule being skipped in auto mode when the matching command ran inside a compound command or subshell
* Fixed Bash `Read()`/`Edit()` deny rules not applying to `< file` redirects and reader commands like `tac` and `egrep`
* Fixed Bash permission checks auto-approving certain `[[ ]]` conditionals that zsh parses differently from bash
* Fixed dismissing the Remote Control consent prompt counting as consent
* Fixed subagents stopping when a response was cut off mid-stream; they now continue automatically
* Fixed `--disallowedTools` and session deny rules being dropped after the first settings reload under `allowManagedPermissionRulesOnly`
* Fixed sandbox network hosts written with a trailing dot not being blocked by a `deniedDomains` entry
* Fixed unbounded memory growth when non-JSONL data is piped into `claude -p --input-format stream-json`
* Fixed `claude mcp add/remove` hanging when `.mcp.json` is a FIFO or device-file symlink
* Fixed prompt-cache misses on every turn in long screenshot-heavy sessions
* Fixed worktree-isolated sessions refusing Bash loops and heredocs that never touch git
* Fixed background commands that detach from their shell surviving a task stop or Claude Code exit

### [2.1.258](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/versions/2.1.258.md)

#### Major bug fixes

* Fixed Claude Code failing to launch on macOS 12 (Monterey), a regression introduced in 2.1.255
* Fixed remote and scheduled sessions failing with "user messages must have non-empty content" after a re-sent permission approval could not be applied

-----

## Claude Code changes

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* New "Permission lockdown" row in the enforcement table, pairing `allowManagedPermissionRulesOnly` with `permissions.disableBypassPermissionsMode`. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/admin-setup.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)]

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* New "Fable advisor and usage credits" section: on plans where Fable bills to usage credits, selecting Fable in `/advisor` does nothing until you accept the one-time consent by running `/model fable`. Until then a Fable advisor bills nothing, because the selection isn't applied. [[lines 87-89](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/advisor.md?plain=1#L87-L89)] [[Source](https://code.claude.com/docs/en/advisor#fable-advisor-and-usage-credits)]
* The advisor compatibility table gained Fable 5.1: a Fable 5.1 main model rejects a Fable 5 advisor, and no Fable main model accepts an Opus or Sonnet advisor. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/advisor.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)]
* Advisor token costs spelled out: advisor calls bill at the advisor model's rates on top of the main model, and a Fable advisor bills to usage credits on plans where Fable does. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/advisor.md?plain=1#L121)] [[Source](https://code.claude.com/docs/en/advisor#cost)]

#### [agent-sdk/custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* Documents a TypeScript/Python divergence: TypeScript saves audio blocks to disk and gives Claude the file path, while Python drops them with a warning. Resource links likewise reach TypeScript callers as `resourceLinks` but are flattened to text in Python before the CLI sees them. [[lines 435-436](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L435-L436)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#return-images-and-resources)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* New `resourceLinks` key on `UserMessage.tool_use_result` for MCP tools returning `resource_link` blocks, with limits of 50 links or 64 KiB of serialized JSON, omitted on subagent results and never produced by in-process tools. [[lines 1444-1445](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/python.md?plain=1#L1444-L1445)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#usermessage)]
* The stall and stream watchdogs documented together: `CLAUDE_ASYNC_AGENT_STALL_TIMEOUT_MS` now defaults to `CLAUDE_STREAM_IDLE_TIMEOUT_MS` plus five minutes while the stream watchdog is on. Keep-alive `ping` frames from a gateway should be read as liveness — before v2.1.257 they stopped five minutes after the last real event. [[lines 837-840](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/python.md?plain=1#L837-L840)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#handle-slow-or-stalled-api-responses)]
* New `thinkingTokens` field, already counted inside `outputTokens`, absent until a turn runs on a version that records it and not declared on the TypedDict — read it with `.get()`. [[line 1563](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/python.md?plain=1#L1563)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `SDKMcpResourceLink` type with its full field table, delivered as `resourceLinks` on user messages and `resource_links` on background task notifications. Claude Code drops a block whose `uri` or `name` isn't a string. Requires Agent SDK v0.3.257. [[lines 4424-4450](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4424-L4450)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmcpresourcelink)]
* New `updateSettings(source, settings)` method, limited to `localSettings` and an allowlist currently holding only `outputStyle`; it rejects on remote transports and where `settingSources` excludes `local`. [[line 544](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L544)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#methods)]
* `getContextUsage()` gained a `detail` option: the default `'full'` issues token-counting API requests per category, while `'summary'` answers from the last response's usage and local estimates with no requests and approximate numbers. [[lines 664-665](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L664-L665)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolgetcontextusageresponse)]
* `output_tokens_details.thinking_tokens` documented at length: read it for observability, not billing; it re-tokenizes the raw reasoning so it can differ from the model's exact count; it's a placeholder on streamed messages; and the whole object is `null` on synthesized messages such as API errors. [[lines 4402-4407](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4402-L4407)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#usage)]
* `tool_progress` heartbeats every 30 seconds with `heartbeat: true` while a main-conversation tool runs, plus `subagent_type` and `subagent_retry` on Agent tool frames. `attempt` can exceed `max_retries`, so don't derive indicator clearing from the counters. [[lines 4692-4697](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4692-L4697)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdktoolprogressmessage)]
* A server that failed to connect now appears in both `added` and `errors` on `setMcpServers()`; before v2.1.257 it was reported only under `errors`. [[line 4531](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L4531)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#mcpsetserversresult)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* New "LLM gateway" section on what a background session inherits. A gateway `ANTHROPIC_BASE_URL` exported only in your shell reaches a background session **only** when the supervisor was itself started from a shell exporting the same gateway, and only in three specific cases — so the advice is to put gateway variables in a settings file's `env` block instead. A forwarded gateway applies to the running process only and is never written to disk. [[lines 473-483](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-view.md?plain=1#L473-L483)] [[Source](https://code.claude.com/docs/en/agent-view#llm-gateway)]
* Background sessions read settings from the directory they run in and inherit the dispatching shell's `PATH`, cloud provider selection and `CLAUDE_CODE_EXTRA_BODY`. [[lines 470-471](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/agent-view.md?plain=1#L470-L471)] [[Source](https://code.claude.com/docs/en/agent-view#settings-and-provider)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--advisor <model>` and the `fable` alias for `--model` documented. [[lines 52-95](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/cli-reference.md?plain=1#L52-L95)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [context-window](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

* Fable 5.1 added to the models supporting a 1M context window. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/context-window.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/context-window#when-your-context-fills-up)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Notes that disabling thinking isn't available on Fable models at all, so effort levels are the only lever there. [[line 282](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/costs.md?plain=1#L282)] [[Source](https://code.claude.com/docs/en/costs#adjust-extended-thinking)]

#### [desktop-ios-simulator](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/desktop-ios-simulator.md) [[Source](https://code.claude.com/docs/en/desktop-ios-simulator)]

* The iOS Simulator pane is unavailable in Enterprise organizations with a HIPAA configuration enabled. [[lines 3-110](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/desktop-ios-simulator.md?plain=1#L3-L110)] [[Source](https://code.claude.com/docs/en/desktop-ios-simulator#test-ios-apps-in-the-simulator)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Auto mode now requires Opus 4.6+, Sonnet 4.6+ or a Fable model, and `MAX_THINKING_TOKENS=0` has no effect on Fable models. [[lines 76-561](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/desktop.md?plain=1#L76-L561)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `ANTHROPIC_DEFAULT_FABLE_MODEL`, `CLAUDE_CODE_SUBAGENT_MODEL_FORCE`, `CLAUDE_CODE_DISABLE_CFC_PROMPT` and `VERTEX_REGION_CLAUDE_FABLE_5_1`. [[lines 130-464](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/env-vars.md?plain=1#L130-L464)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `MAX_THINKING_TOKENS` and `CLAUDE_CODE_DISABLE_THINKING` both gained the Fable carve-out — thinking can't be turned off there — and `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` is documented as having no effect on Fable, Sonnet 5, or Opus 4.7+. [[lines 206-419](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/env-vars.md?plain=1#L206-L419)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* A trap worth noting: `FALLBACK_FOR_ALL_PRIMARY_MODELS` set to `0` or `false` **still enables** the behavior, unlike most on/off variables — you have to unset it. [[line 410](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/env-vars.md?plain=1#L410)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New "Claude Code does not support this model" section for the server-side per-model minimum version check, which a full `claude-` ID passes locally but the server can still reject. [[lines 1543-1554](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/errors.md?plain=1#L1543-L1554)] [[Source](https://code.claude.com/docs/en/errors#claude-code-does-not-support-this-model)]
* New unanswered-consent messages for the Fable usage-credits prompt in a session with nobody at the terminal — nothing is sent, and the message names the session's Fable model. [[lines 508-515](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/errors.md?plain=1#L508-L515)] [[Source](https://code.claude.com/docs/en/errors#the-prompt-to-confirm-went-unanswered)]

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Auto mode on third-party providers narrowed to Sonnet 5, Opus 4.7+ and the Fable models, across every provider section. [[lines 80-126](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/feature-availability.md?plain=1#L80-L126)] [[Source](https://code.claude.com/docs/en/feature-availability#admin-and-analytics)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* A hook's `setMode` with `bypassPermissions` is now a no-op unless the session launched with bypass mode already available, and it's never persisted as `defaultMode` regardless of `destination`. [[line 1744](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/hooks.md?plain=1#L1744)] [[Source](https://code.claude.com/docs/en/hooks#permission-update-entries)]

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Discovered model IDs are now skipped when they're spellings of the same Fable version as an existing row, and explicit IDs fold into built-in alias rows when both resolve to the same model. [[line 174](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/llm-gateway-protocol.md?plain=1#L174)] [[Source](https://code.claude.com/docs/en/llm-gateway-protocol#picker-entries-and-caching)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Rewritten "Work with Fable" section. `fable` now resolves to Fable 5.1 (it was Fable 5 before v2.1.255), and Fable 5 must be selected by model ID. A saved `claude-fable-5` value in **user** settings is silently rewritten to the `fable` alias on first run of v2.1.255+, with `(auto-updated)` shown once — project, local and managed settings are left alone. [[lines 48-65](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/model-config.md?plain=1#L48-L65)] [[Source](https://code.claude.com/docs/en/model-config#work-with-fable)]
* New "Fable and usage credits" subsection. Interactive sessions show a consent prompt before a Fable request bills usage credits; Enterprise plans with organization billing don't see it. **In `-p` mode and through the Agent SDK the prompt never appears and the request bills without asking.** [[lines 69-85](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/model-config.md?plain=1#L69-L85)] [[Source](https://code.claude.com/docs/en/model-config#fable-and-usage-credits)]
* Automatic model fallback documented per category: on Fable 5.1 and Fable 5, biology-flagged requests re-run on Opus 5 and cybersecurity-flagged requests on Opus 4.8. Offensive-security and biology workloads trigger this often, sometimes on the first request — and once a biology flag moves a session to Opus 5, later biology flags simply refuse, because Opus 5 has no biology fallback. [[lines 378-416](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/model-config.md?plain=1#L378-L416)] [[Source](https://code.claude.com/docs/en/model-config#automatic-model-fallback)]
* `availableModels` prefix matching explained with a Fable example: `claude-fable-5` permits both Fable 5 and 5.1, while `claude-fable-5-1` permits 5.1 only. [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/model-config.md?plain=1#L165)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]
* The default-effort hold applies to Fable 5, Opus 4.8 and Opus 4.7; Opus 5 and Fable 5.1 have no such hold. [[line 434](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/model-config.md?plain=1#L434)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]
* States flatly that thinking cannot be turned off on Fable 5.1 or Fable 5 — the session toggle, `alwaysThinkingEnabled` and `MAX_THINKING_TOKENS=0` all have no effect. [[line 507](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/model-config.md?plain=1#L507)] [[Source](https://code.claude.com/docs/en/model-config#extended-thinking)]

#### [output-styles](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Output styles are now selectable from the VS Code command menu, saved to `.claude/settings.local.json`. Requires v2.1.257. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/output-styles.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/output-styles#change-your-output-style)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* `permissions.defaultMode` in project or local settings now ignores both `"auto"` and `"bypassPermissions"`; an ignored `"auto"` also makes Claude Code fall back to the built-in default rather than a user-settings `defaultMode`. Before v2.1.257, `bypassPermissions` took effect from any file. [[lines 53-54](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/permission-modes.md?plain=1#L53-L54)] [[Source](https://code.claude.com/docs/en/permission-modes#which-mode-a-session-starts-in)]
* The auto-mode classifier's model resolution is now fully specified, including the Opus fallback when the session runs on a Fable model, and that the session's first auto-mode request validates the Sonnet 5 default and settles the choice for the session. [[line 372](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/permission-modes.md?plain=1#L372)] [[Source](https://code.claude.com/docs/en/permission-modes#when-auto-mode-falls-back)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* The Fable usage-credits consent prompt follows the forwarded-dialog deadline but is **not** forwarded — it appears only in the terminal where the session runs, and an unanswered prompt ends the turn without sending. [[line 291](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/remote-control.md?plain=1#L291)] [[Source](https://code.claude.com/docs/en/remote-control#limitations)]

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* New `timeFormat` and `timeZone` settings. `timeFormat` takes `auto`, `12-hour`, `24-hour`, `24-hour-utc`, or a strftime pattern — any value containing `%` is treated as a pattern and anything else outside the presets counts as `auto`. `/config` offers only the presets. Requires v2.1.257. [[lines 2942-2963](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/settings-reference.md?plain=1#L2942-L2963)] [[Source](https://code.claude.com/docs/en/settings-reference#timeformat)]
* New `allowManagedPermissionRulesOnly` entry enumerating everything it ignores: `allow`/`ask`/`deny` rules in user, project, local and `--settings` files, `--allowedTools`, the always-allow choices in prompts, and new rule saving. `--disallowedTools` and session deny/ask rules survive a mid-session reload — before v2.1.257 they were dropped. [[lines 716-722](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/settings-reference.md?plain=1#L716-L722)] [[Source](https://code.claude.com/docs/en/settings-reference#allowmanagedpermissionrulesonly)]
* `permissionExplainerEnabled` marked removed in v2.1.257. [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/claude-code/settings-reference.md?plain=1#L116)] [[Source](https://code.claude.com/docs/en/settings-reference#all-settings)]

-----

## API changes

### New Documents

#### [models/fable-5-1/overview](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/models/fable-5-1/overview.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/overview)]

The model page for Claude Fable 5.1: 1M context, 128K max output, $10/$50 per MTok with a **$0.25/MTok cache read** (a quarter of Fable 5's), `high` default effort, adaptive thinking always on, and a June 2026 knowledge cutoff. The guidance is explicit that most workloads should start with Claude Opus 5, and reach for Fable 5.1 for demanding reasoning and long-horizon agentic work, or when Opus 5 at higher effort still falls short.

#### [models/mythos-5-1/overview](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/models/mythos-5-1/overview.md) [[Source](https://platform.claude.com/docs/en/models/mythos-5-1/overview)]

Claude Mythos 5.1, invite-only under Project Glasswing, sharing Fable 5.1's specifications and pricing. Notably, Mythos 5.1 does **not** run the thinking-prefix check that Fable 5.1 enforces.

#### [models/fable-5-1/whats-new-fable-5-1](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)]

The migration-critical page, splitting the changes into three breaking and five additive:

* **Forced tool use is not supported.** `tool_choice: {"type": "any"}` or `{"type": "tool", ...}` returns a 400, on the token-counting endpoint too. The reasoning given: thinking is always on, and a forced tool call would skip it, pushing the model to write its working-out into the tool arguments and lowering argument quality. Use `strict: true` or structured outputs for schema-valid JSON, and state in the prompt when the tool applies.
* **Thinking blocks are bound to their producing model**, preserved in one direction only: Fable 5.1 reads earlier models' blocks, and no earlier model reads its. Moving a conversation *up* keeps its reasoning; moving *down* loses it for turns that run there.
* **Editing earlier turns invalidates thinking blocks.** Four patterns that break it are listed — editing/reordering/removing an earlier turn, injecting per-request text you later remove, rebuilding `system` or `tools` between requests, and an image or document URL that serves different bytes. Five that don't are listed too, including removing a *leading* run of thinking blocks oldest-first and moving `cache_control` markers. Removing a block from anywhere other than the start invalidates everything after it.
* **Per-message effort (beta)**, **turn-scoped system messages (beta)**, **`display: "updates"` (beta)**, the **lower cache read price**, and **content provenance**.
* A "Changed from Claude Fable 5" section covering seven behavior shifts that show up with no code change, each with a prompting fix: more variable parallel tool calling, fewer progress updates, answering from memory more often at `low` effort, denser prose, less formatting in chat, unmarked quotations in summaries, and whole-file rewrites for small edits.

#### [models/fable-5-1/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/models/fable-5-1/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)]

The step-by-step migration, including the three-step check for whether your integration edits conversation history.

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

A dedicated page on keeping the conversation prefix intact: who is affected, how to tell, what counts as an edit, and eight concrete fixes — append assistant turns exactly as returned, add instructions with a mid-conversation system message rather than editing `system`, send per-turn reminders as turn-scoped system messages, change tools with `tool_addition`/`tool_removal`, trim on the server where possible, handle custom client-side compaction, reference files by ID rather than a URL whose content changes, and choose what happens on a mismatch. Ends with a checklist.

#### [build-with-claude/prompt-engineering/prompting-claude-fable-5-1](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-fable-5-1.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-1)]

Model-specific prompting guidance in seventeen sections, each keyed to one of the behavior differences: batching independent tool calls in agent loops, asking for user-facing progress updates, keeping history append-only, writing density, formatting in chat, quoting retrieved sources, finishing the whole task, telling the model what to preserve in compaction summaries, search triggering at low effort, reducing safeguard false positives, preferring targeted edits over whole-file rewrites, leaving room for long outputs at xhigh and max effort, letting the lead agent keep working while subagents run, and giving vision work tools to crop and zoom.

#### [system-prompts/claude-fable-5-1](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/system-prompts/claude-fable-5-1.md) [[Source](https://platform.claude.com/docs/en/system-prompts/claude-fable-5-1)]

The published system prompt for Claude Fable 5.1.

#### [api/beta/organization/compliance_settings](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/api/beta/organization/compliance_settings.md) [[Source](https://platform.claude.com/docs/en/api/beta/organization/compliance_settings)]

A new beta endpoint pair — `GET` and `POST /v1/organizations/compliance_settings` — for reading and setting whether the Compliance API is enabled for an organization. The state accepts the string shorthand `"enabled"`/`"disabled"` but always returns the canonical object form, and automated provisioning never disables compliance settings.

### Changed documents

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* New "Change effort mid-conversation" section with two mechanisms. **Per-message effort (beta)** adds a `role: "system"` message with empty `content` and the new `output_config.effort`; the level takes effect from the next `user` turn and everything before it is unchanged, so the cached prefix still matches. Models without it, including Fable 5, return `output_config.effort requires a model that supports per-turn effort`. [[lines 160-206](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/effort.md?plain=1#L160-L206)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation)]
* A second reason to prefer the per-message form on Fable 5.1: a top-level change not only restarts the cache but **steers the model less reliably**, because its earlier replies were written at the previous level and it tends to stay consistent with them. [[line 206](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/effort.md?plain=1#L206)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#per-message-effort-beta)]
* An effort-only system message carries no text, so the mid-conversation placement rules don't apply — it can go anywhere in `messages`, including first. [[line 204](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/effort.md?plain=1#L204)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#per-message-effort-beta)]
* Per-model effort recommendations for Fable 5.1: start with `high`, step up to `xhigh`/`max` for the most capability-sensitive work, and set a large `max_tokens` at `high` and above since it's a hard limit on thinking plus response text. [[line 65](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/effort.md?plain=1#L65)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels-for-claude-fable-51)]
* A caution on `max`: on most workloads it adds significant cost for relatively small gains, and on structured-output tasks it can lead to overthinking. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/effort.md?plain=1#L109)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels-for-claude-opus-47)]

#### [build-with-claude/mid-conversation-system-messages](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/mid-conversation-system-messages.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages)]

* New "Turn-scoped system messages" section. `clear_at: "next_user_message"` gives a message system-prompt authority for the current turn, after which it stops rendering but **stays in the array** — which is exactly what keeps the conversation unchanged and later thinking blocks valid. A cleared message costs no input tokens. Beta header: `mid-conversation-system-clear-at-2026-08-21`. [[lines 176-195](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L176-L195)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#turn-scoped-system-messages)]
* New guidance against editing or removing an already-sent mid-conversation system message: append a new one instead, since consecutive system messages are treated as a single section. [[line 338](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L338)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#combining-with-prompt-caching)]
* Mid-conversation **tool changes** documented as the tools counterpart: declare the full set in `tools` up front and use `tool_addition`/`tool_removal` blocks, because the `tools` array sits even earlier in the hashed prefix than `system`. Beta header: `mid-conversation-tool-changes-2026-07-01`. [[lines 13-70](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/mid-conversation-system-messages.md?plain=1#L13-L70)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#mid-conversation-tool-changes)]

#### [build-with-claude/thinking](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

* Restructured around `display`: on Opus 5, Sonnet 5, Fable 5.1, Mythos 5.1, Fable 5, Mythos 5 and Mythos Preview thinking is already on and `display` defaults to `"omitted"`, so the text is hidden until you opt in with `"summarized"`. Blocks are billed and passed back the same either way. [[lines 39-47](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/thinking.md?plain=1#L39-L47)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking#how-thinking-works)]

#### [build-with-claude/prompt-engineering/claude-prompting-best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]

* Reorganized into three parts with a model-specific guidance index pointing at each model's own prompting page. [[lines 7-15](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L7-L15)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#prompting-best-practices)]
* Two opposed verbosity notes now sit side by side: Opus 5 runs longer than prior models and doesn't shorten reliably with effort, while Fable 5.1 writes *fewer* user-facing updates during agentic work — so remove instructions telling it to keep that text brief. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L179)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#communication-style-and-verbosity)]
* Anti-formatting blocks written for earlier models can suppress structure Fable 5.1's content needs, since it already formats less. [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L225)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#control-the-format-of-responses)]
* Recommends sending the parallel-calls instruction as a turn-scoped system message after each round of tool results on Fable 5.1. [[line 374](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md?plain=1#L374)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices#optimize-parallel-tool-calling)]

#### [models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/96e439024f9a4be47b492c3943f3834a50040738/docs-md/api/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/models/optimizing-for-cost-and-intelligence)]

* Reworked to place Fable 5.1 and Mythos 5.1 in the cost/intelligence ladder.
