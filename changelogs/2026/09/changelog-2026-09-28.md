# [Claude docs changes for Sept, 28th 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5)]

## Executive Summary
- Claude Sonnet 5.5 (`claude-sonnet-5-5`) launches: 1M context, $2/$10 per MTok, with a new overview, what's-new page, migration guide and prompting guide, and Claude Code 2.1.284 adopts it as the default Sonnet model
- Sonnet 5.5 brings breaking API changes: `thinking: disabled` is replaced by `between_tools`, forced tool use is rejected, thinking blocks are bound to the account and conversation prefix, and computer use requires `computer_toolset_20260801`
- Claude Code now starts in auto mode by default when no permission mode is configured, and Ultracode becomes its own toggle in `/effort`
- Agent SDK docs explain the system reminders Claude Code adds outside the system prompt and how to turn them off
- Claude apps gateway gains dollar-based spend limits, Google Cloud OTLP telemetry export and certificate client authentication

## New Claude Code versions

### [2.1.284](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/versions/2.1.284.md)

#### New features

* Added Claude Sonnet 5.5 (`claude-sonnet-5-5`) as the default Sonnet model on the Anthropic API (1M context, $2/$10 per Mtok)
* Added a "Yes, but ask again next time" answer to auto mode's prompt for reads outside the working directories
* Added dollar amounts for the Claude apps gateway spend limit in `/usage` and the status line (`rate_limits.spend_limit` gains `used_usd`, `limit_usd`, `period`)
* Added `effortSlider:decreaseEffort`, `increaseEffort` and `toggleUltracode` keybinding actions
* Added `/rate-limit-options` to `/help` for claude.ai subscribers, and `/mcp reconnect all` to retry every failed or unauthenticated MCP server
* Added Claude apps gateway startup warnings for empty or inconsistent `availableModels`, `auth: { google: {} }` for `telemetry.forward_to` destinations, and `private_key_jwt` certificate client authentication with the identity provider
* [VSCode] Added optional message timestamps, plugin load errors in Manage plugins, and an Ultracode on/off switch under the Effort slider
* [Claude Tag] Added model family choices such as "Opus (latest)" and org-wide limit spend in the analytics projection chart

#### Existing feature improvements

* Interactive terminal and VS Code sessions now start in auto mode when no permission mode is configured (`permissions.defaultMode` still overrides it)
* Ultracode is its own toggle in `/effort` (Tab, or `/effort ultracode [on|off]`), no longer forces xhigh effort, and works at any effort level
* Retries after a dropped mid-response connection share one budget with other retries, so failing requests give up sooner
* Safety-flag notices for Sonnet models explain the cause and offer edit and retry; on pinned Opus models the API picks the fallback model
* Auto-memory loading neutralizes invisible characters and look-alike markup tags in `MEMORY.md` and recalled notes
* Improved startup time and memory use by building only the used parts of the settings schema
* `claude plugin marketplace add` says when it replaces a marketplace of the same name; `/recap` declines when relayed from chat threads, routines or webhooks
* Improved `/claude-api` `hillclimb`, aligned columns in `/tasks`, `/copy` and `/hooks`, and better Monitor event rows

#### Major bug fixes

* Fixed damaged response streams showing raw errors ("JSON Parse error", "undefined") instead of being retried, and overloaded errors after a thinking block ending the turn instead of being retried
* Fixed "Prompt is too long" errors persisting after compaction; Claude Code now compacts again keeping less recent conversation
* Fixed `allowed-tools` in marketplace, claude.ai and npm plugins pre-approving tools under managed `allowManagedPermissionRulesOnly`
* Fixed rules symlinked into `.claude/rules` from outside the project skipping the external-imports approval prompt
* Fixed `{"decision":"block"}` from Elicitation and ElicitationResult hooks being ignored
* Fixed MCP tool calls in resumed sessions failing with "No such tool available" while the server was still connecting
* Fixed `claude mcp add` reporting success when managed settings restrict MCP servers to plugins
* Fixed Agent SDK sessions crashing on images with malformed `source`
* Fixed Bash tool failing on Windows with many plugins, and sandboxed Bash failing to start on Linux with write-denied working directories
* Fixed the Claude apps gateway returning 431 for sign-ins with many identity provider groups
* Fixed repeated plan-usage endpoint calls after rate-limiting or login rejection

-----

## Claude Code changes

### Changed documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* Advisor pairing table updated for Sonnet 5.5 (accepts Fable, Opus 4.7+, Sonnet 5+) and for the new Opus 5.5 and Fable 5.1 constraints. [[lines 84-93](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/advisor.md?plain=1#L84-L93)] [[Source](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)]

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* New section "Context Claude Code adds outside the system prompt": lists the system reminders (CLAUDE.md, output style, attribution, hook output, skills, subagents, task nudges, file-changed notes). [[lines 367-468](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L367-L468)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#context-claude-code-adds-outside-the-system-prompt)]
* Table and TypeScript/Python example for turning off built-in context (`includeGitInstructions`, `attribution`, `CLAUDE_CODE_DISABLE_CLAUDE_MDS`, `CLAUDE_CODE_DISABLE_ATTACHMENTS`), and how to log raw requests to see what Claude received.

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Substantial updates to the TypeScript SDK reference (about 150 lines changed).

#### [claude-md](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/claude-md.md) [[Source](https://code.claude.com/docs/en/claude-md)]

* `/doctor prompt-audit [path]` audits CLAUDE.md, rules, skills, commands and subagents for outdated or conflicting instructions. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/claude-md.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/claude-md#write-effective-instructions)]
* Troubleshooting tip: instructions may compete with built-in commit/PR guidance; disable it with `includeGitInstructions`. [[line 547](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/claude-md.md?plain=1#L547)] [[Source](https://code.claude.com/docs/en/claude-md#claude-isnt-following-my-claudemd)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Command table updated: `/rate-limit-options`, `/mcp reconnect all`, `/doctor [prompt-audit [path]]`, `/claude-api` prompt-audit and other modes. [[lines 44-160](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/commands.md?plain=1#L44-L160)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `VERTEX_REGION_CLAUDE_5_5_SONNET`; updated descriptions of `CLAUDE_CODE_DISABLE_THINKING`, `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING` and `MAX_THINKING_TOKENS`. [[line 492](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/env-vars.md?plain=1#L492)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New sections for marketplace names that impersonate official Anthropic marketplaces, plugin uninstall refusals, and unresolvable path refusals. [[lines 3441-3462](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/errors.md?plain=1#L3441-L3462)] [[Source](https://code.claude.com/docs/en/errors#marketplace-is-registered-from-an-untrusted-source)]
* Startup refusal when `forceLoginMethod`/`forceLoginOrgUUID` conflicts with a configured credential, and how to remove it. [[line 1275](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/errors.md?plain=1#L1275)] [[Source](https://code.claude.com/docs/en/errors#claude-login-not-accepted)]
* Minimum Claude Code version for Sonnet 5.5 thinking support, and safeguard-flag notices for Opus 5.5/Sonnet 5.5. [[line 2359](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/errors.md?plain=1#L2359)] [[Source](https://code.claude.com/docs/en/errors#thinkingtypeenabled-is-not-supported-for-this-model)]

#### [glossary](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/glossary.md) [[Source](https://code.claude.com/docs/en/glossary)]

* About 23 lines of new glossary entries.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Sonnet 5.5 added as the default Sonnet alias, with updated effort, thinking and extended-context guidance.

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Documentation of auto mode as the default start mode and the new "ask again next time" read answer.

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* Gateway docs (config, deploy, AWS, GCP, spend limits) updated for Google OTLP telemetry auth, `private_key_jwt` identity provider auth, dollar spend limits and startup warnings.

#### [plugins/loading](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/claude-code/plugins/loading.md) [[Source](https://code.claude.com/docs/en/plugins/loading)]

* Plugin docs (loading, CLI reference, manifest, marketplace reference, troubleshooting) updated for reserved marketplace names, `allowed-tools` pre-approval rules and install/uninstall behavior.

-----

## API changes

### New Documents

#### [build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-sonnet-5-5)]

Prompting guide for Claude Sonnet 5.5, covering how to steer the model and what to change when migrating prompts from Sonnet 5.

#### [models/sonnet-5-5/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/models/sonnet-5-5/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide)]

Long migration guide from earlier models to Sonnet 5.5, with code samples for the breaking changes (thinking, forced tool use, computer use, advisor).

#### [models/sonnet-5-5/overview](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/models/sonnet-5-5/overview.md) [[Source](https://platform.claude.com/docs/en/models/sonnet-5-5/overview)]

Overview of Claude Sonnet 5.5, "the best combination of speed and intelligence": model ID, capabilities, pricing and platform availability.

#### [models/sonnet-5-5/whats-new-sonnet-5-5](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/models/sonnet-5-5/whats-new-sonnet-5-5.md) [[Source](https://platform.claude.com/docs/en/models/sonnet-5-5/whats-new-sonnet-5-5)]

Five breaking changes versus Sonnet 5: `between_tools` replaces disabled thinking, forced tool use errors, thinking blocks bound to model and conversation, `computer_20251124` not accepted, and advisor pairing restrictions. Also notes that text between tool calls now comes back in `thinking` blocks, and covers behavior differences, pricing and availability.

### Changed documents

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Sonnet 5.5 added: $2 input, $2.50/$4 cache writes, $0.20 cache reads, $10 output per MTok. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/about-claude/pricing.md?plain=1#L31)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#model-pricing)]
* Batch pricing ($1/$5) and 286-token tool-use system prompt overhead. [[line 200](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/about-claude/pricing.md?plain=1#L200)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#batch-processing)]

#### [api/errors](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* New 400 errors for Sonnet 5.5: `thinking.type.disabled`, `between_tools` at `xhigh`/`max` effort, mid-conversation effort changes with `between_tools`, and `between_tools` on other models. [[lines 484-511](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/api/errors.md?plain=1#L484-L511)] [[Source](https://platform.claude.com/docs/en/api/errors#thinking-cannot-be-disabled)]
* Forced tool use rejected on Opus 5.5, Sonnet 5.5, Fable 5.1 and Mythos 5.1; computer use only as `computer_toolset_20260801` on Opus 5.5 and Sonnet 5.5. [[lines 516-532](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/api/errors.md?plain=1#L516-L532)] [[Source](https://platform.claude.com/docs/en/api/errors#forced-tool-use-not-supported)]
* Thinking-block prefix check now covers Sonnet 5.5. [[line 536](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/api/errors.md?plain=1#L536)] [[Source](https://platform.claude.com/docs/en/api/errors#thinking-block-no-longer-matches-the-conversation)]

#### [build-with-claude/compaction](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Comparison table reworked around on-demand compaction, with links to keep-recent-turns, background compaction and thinking-blocks pages. [[lines 17-26](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/compaction.md?plain=1#L17-L26)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction#choose-how-to-compact)]

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Sonnet 5.5 supports all five effort levels (default `high`, recalibrated); new "Recommended effort levels for Claude Sonnet 5.5" section. [[lines 306-313](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/effort.md?plain=1#L306-L313)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#recommended-effort-levels-for-claude-sonnet-55)]
* Per-message effort changes now supported on Sonnet 5.5 (beta header `mid-conversation-output-config-2026-07-01`). [[line 361](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/effort.md?plain=1#L361)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort#change-effort-mid-conversation)]

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* New section: Sonnet 5.5 thinking blocks stay with the account that produced them; other accounts' blocks are dropped (`organization_binding_mismatch`). [[lines 68-73](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L68-L73)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#thinking-blocks-stay-with-the-account-that-produced-them)]
* Sonnet 5.5 reads thinking blocks from Sonnet 5, Opus 4.8, Haiku 4.5 and earlier, but not Opus 5/5.5, Fable or Mythos. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#switching-models-mid-conversation)]
* Prefix check enforced for new accounts on Sonnet 5.5; `block_binding` works only with adaptive thinking on Sonnet 5.5. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L130)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#set-the-mismatch-behavior-and-read-input_transformations)]

#### [build-with-claude/thinking](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking)]

* New per-model table showing what each `thinking` value does (adaptive, enabled, `between_tools`, disabled), including the new `between_tools` mode. [[lines 47-70](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/thinking.md?plain=1#L47-L70)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking#configuring-thinking)]
* Rewritten introduction explaining up-front thinking, with a diagram. [[lines 13-23](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/thinking.md?plain=1#L13-L23)] [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking#thinking)]

#### [build-with-claude/thinking-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/thinking-troubleshooting.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/thinking-troubleshooting)]

* New troubleshooting entries for the `between_tools` and effort errors.

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Compatibility and result-format guidance updated for Sonnet 5.5 and the newer Opus/Fable advisors.

#### [agents-and-tools/tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Sonnet 5.5 requires `computer_toolset_20260801`; migration from `computer_20251124`.

#### [build-with-claude/prompt-engineering/claude-prompting-best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]

* Updated to cover Sonnet 5.5 and link to its prompting guide.

#### [models/overview](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/models/overview.md) [[Source](https://platform.claude.com/docs/en/models/overview)]

* Sonnet 5.5 added as the newest Sonnet; model pages for other models (Opus, Fable, Mythos, Sonnet, Haiku) and `choosing-a-model` updated accordingly.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Release notes entry for Claude Sonnet 5.5 and related API changes.

#### [build-with-claude/refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/ddbeb4d48034ed6353d3e56fdc7c249b2f8529c5/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* Refusal and fallback guidance updated for Sonnet 5.5.
