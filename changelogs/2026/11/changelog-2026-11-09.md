# [Claude docs changes for November 9th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/8d17e90f02f9386e506041167cd070fd6395c03b) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/8d17e90f02f9386e506041167cd070fd6395c03b)]

## Executive Summary
- **Claude Fable 5.2 and Claude Mythos 5.2 launched** (`claude-fable-5-2`, `claude-mythos-5-2`). They have a 1M context window and cost $8/$40 per MTok. Mythos 5.2 is the same model, limited to verified organizations. Each model has new overview, what's new, migration guide and prompting pages.
- **Breaking API changes for the new models:** thinking blocks are account-bound, the prefix check applies to every account, forced `tool_choice` returns a 400, and computer use moves to `computer_toolset_20260801`. A Fable 5.2 executor accepts only Fable 5.2 or Mythos 5.2 as its advisor.
- **Claude Code 2.1.321** makes Fable 5.2 the default `fable` model. It also adds fast mode for Fable 5.2 ($16/$80 per MTok), a `--settings` option for `claude remote-control`, and many security and permission fixes.
- **Claude apps gateway** gains a `login_notice`, pooled-budget ordering, JSON logs and clearer spend-limit messages.
- **New `permissions.denyInsteadOfPrompting` setting** keeps unattended sessions running by denying calls that would otherwise wait on a permission prompt.

## New Claude Code versions

### [2.1.321](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/versions/2.1.321.md)

#### New features

* Added Claude Fable 5.2 (`claude-fable-5-2`), now the default Fable model, with 1M context and $8/$40 per Mtok pricing
* Added `--settings <file>` to `claude remote-control`, which applies a settings file to every session it starts

#### Existing feature improvements

* Fast mode falls back to standard speed on the same model first when fast serving is rate-limited or failing, and its labels now name your current model
* The `/model` picker lists "More models" as an unnumbered row below the others
* Saved Fable 5.1 model picks move to the `fable` alias, on Pro and Max at once and on Team and Enterprise once the organization allows it
* Mods Claude writes turn on without asking in auto and bypass modes. Mods' own tool calls (`$.tool.call`, `$.mcp.call`) raise no permission prompts, and deny rules still apply
* Headless sessions reload mods in `.claude/skills` when files change (`CLAUDE_CODE_PLUGIN_DIR_WATCH=0` turns this off)
* `cp` and `mv` spelled by a path, such as `/bin/cp`, get the same path checks as plain `cp` and `mv`
* Managed `extraKnownMarketplaces` are stricter: a declared name can't be added from another source
* Claude apps gateway: `policy_mode: layered` now adds up managed MCP servers over every matching policy, spend-limit messages show reset times in local time, and Bedrock, Vertex and Foundry upstreams ignore `ANTHROPIC_*_BASE_URL` (use `base_url`)
* Faster `claude install` and faster startup on Windows
* Background command notifications show only the start and end of commands over 1,000 characters, which saves context

#### Major bug fixes

* MCP OAuth requests no longer send secrets such as refresh tokens to another host when a server redirects them
* Fixed a read-only Bash command running outside the sandbox without a prompt
* Fixed Bash permission checks judging a file write from the wrong folder
* Deny rules and protected-file prompts now apply to the file that a `cp` or `mv` into a directory writes
* Fixed `NotebookEdit` and Edit mistakes on network paths (UNC shares, WSL folders, `/net` mounts)
* Fixed `/config` showing the wrong default permission mode when sessions start in auto mode
* Fixed the TLS handshake error that ended turns partway through a reply
* Fixed sign-in, token refresh and logout hanging when the network never answers the TLS handshake
* Fixed a PreToolUse hook's `ask` being lost or overridden by another hook
* Fixed Bash commands sometimes running in the wrong folder when several were sent at once
* Fixed `claude -p` on Linux exiting 0 silently when NFS storage lost transcript lines

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* Fable 5.2 was added to the advisor pairing table. It requires Claude Code v2.1.321 or later. [[lines 97-101](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/advisor.md?plain=1#L97-L101)] [[Source](https://code.claude.com/docs/en/advisor#choose-an-advisor-model)]

#### [agent-sdk/custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* Added `structuredContent` on tool results, which returns raw JSON fields that Claude can read exactly, and explained how it interacts with image and text content blocks.
* Explained that a bare name in `disallowedTools` removes the tool from Claude's context, while a scoped rule leaves it in context and only denies matching calls.

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Clarified that a hook returning `allow` does not skip deny and ask rules.
* Documented how `allowedTools` and `disallowedTools` feed the permission evaluation flow, including `*` and `mcp__*` globs in deny rules.
* In `dontAsk` mode the `canUseTool` step is skipped and the tool is denied.

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Documented Monitor's `timeout_ms`. It defaults to 300000 and is capped at 30 minutes, and Claude gets one notice at the deadline.
* Noted that Monitor commands follow Bash permission rules.

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* Noted that the Monitor `ws` source requires v2.1.195 or later.

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* Added the `login_notice` key, a notice of up to 500 characters shown at sign-in. It requires v2.1.319.
* Added `pooled_conflict_rule` (`default_order` or `priority_list`) and `pooled_priority_order` to control which pooled group budget is charged first.

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* Added `CLAUDE_GATEWAY_LOG_FORMAT=json` for JSON operational logs with `severity`, `time` and `message`.

#### [claude-apps-gateway-spend-limits](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/claude-apps-gateway-spend-limits.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-spend-limits)]

* The spend-limit message now shows the reset date and any operator note, and the response carries a `retry-after` header.
* Developers can see their estimated spend under `/usage` when no cap applies.

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Added HTML file previews in SSH and WSL sessions, with notices that explain empty charts and an Export option. [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/desktop.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/desktop#preview-html-files-in-ssh-and-wsl-sessions)]
* Added the `disableBrowserExternalNavigation` managed setting, which turns off scripts in those previews and blocks external browsing in the Browser pane.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added `CLAUDE_CODE_PROXY_RESOLVES_HOSTS` and `VERTEX_REGION_CLAUDE_FABLE_5_2`.

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added sections for gateway spend-limit and pooled-budget errors, "Couldn't send feedback", and the feedback-disabled message.
* Added a section on the "Two Claude Code config files exist" warning, with steps to move the unwanted file.
* Added the mistyped model name warning and the `/rewind` file-backup message.

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Fast mode now supports Fable 5.2, at $16/$80 per MTok and up to 2.5x faster.
* Described how fast mode behaves when you switch models: on Fable 5.2 it persists only if you turned it on while using that model.
* Noted usage-tier dependence and the "not in your organization's allowed models" refusal.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* The `fable` alias now resolves to Fable 5.2, except in Claude apps gateway sessions where it stays Fable 5. `best` now maps to the same model as `opus`.
* Documented the one-time move of a saved `claude-fable-5-1` setting to `fable`.
* Fable 5.2 defaults to `medium` effort. Fable models are now covered by automatic fallback (biology to Opus 5, cybersecurity to Opus 4.8).
* Explained that `availableModels` version prefixes also match later IDs, and added a "Fix a mistyped model name" section.
* Added guidance on the 1M context window for gateways with lower limits.

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified how Bash rules match `git -C`/`-c` variants, and that `which` with flags such as `-i` prompts.

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* Added `$.ui.place`, which places a row in the terminal transcript (v2.1.314 or later), with an example and edge cases.
* Added `$.theme.set` and `$.theme.clear` for backdrops in the Desktop and mobile apps. They replace `$.ui.backdrop`, which v2.1.319 removed.

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* Added the `$.theme` API, the `Placed` and `Backdrop` render sites, and limits for placed rows (500) and name characters.

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added a troubleshooting cause: Remote Control is unavailable when the organization has Zero Data Retention.

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* Added the `CLAUDE_RUNNER_CHECKOUT_PATH` variable and rules for checkout folder names.

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Added `permissions.denyInsteadOfPrompting` (v2.1.319 or later). It is set in user or managed scope and denies calls that would wait on a prompt, so unattended sessions keep running. [[lines 1163-1222](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/settings-reference.md?plain=1#L1163-L1222)] [[Source](https://code.claude.com/docs/en/settings-reference#permissionsdenyinsteadofprompting)]
* `fastMode` now covers Fable 5.2, which also requires running `/fast` on that model. [[line 448](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/claude-code/settings-reference.md?plain=1#L448)] [[Source](https://code.claude.com/docs/en/settings-reference#fastmode)]
* Added `disableBrowserExternalNavigation` to the managed settings.

-----

## API changes

### New Documents

#### [build-with-claude/prompt-engineering/prompting-claude-fable-5-2](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/build-with-claude/prompt-engineering/prompting-claude-fable-5-2.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2)]

Prompting guide for Fable 5.2 and Mythos 5.2. It covers calibrating effort, getting the model to finish the whole task, approvals, code ownership, progress updates, subagent use, caution that builds up, reviewing instructions written for earlier models, readable final reports, and safeguard refusals.

#### [models/fable-5-2/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/models/fable-5-2/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-2/migration-guide)]

Migration guide to Fable 5.2 and Mythos 5.2 from Fable 5.1, Mythos 5.1 and other models. It covers the preserved-thinking prefix check, the computer use toolset change, forced tool use, advisor changes and feature support.

#### [models/fable-5-2/overview](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/models/fable-5-2/overview.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-2/overview)]

Overview of Claude Fable 5.2 (released November 9, 2026). The model has 1M context and 128K output, costs $8/$40 per MTok, and has `high` default effort. The page lists model IDs on every platform, pricing, capabilities and a comparison with other models.

#### [models/fable-5-2/whats-new-fable-5-2](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/models/fable-5-2/whats-new-fable-5-2.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-2/whats-new-fable-5-2)]

Lists what's new in Fable 5.2 and Mythos 5.2:
* Breaking changes: thinking blocks are invalidated when earlier turns are edited, only Fable 5.2 and Mythos 5.2 read their own thinking blocks, computer use moves to `computer_toolset_20260801`, and the advisor must be Fable 5.2 or Mythos 5.2.
* Adaptive thinking is always on, and forced `tool_choice` is unsupported.
* Supports all five effort levels, compaction on demand (beta) and mid-conversation tool changes (beta).
* Behavior differences, refusals and fallback, pricing and availability.

#### [models/mythos-5-2/overview](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/models/mythos-5-2/overview.md) [[Source](https://platform.claude.com/docs/en/models/mythos-5-2/overview)]

Overview of Claude Mythos 5.2 (`claude-mythos-5-2`). It is the same model as Fable 5.2, available only to organizations verified through Anthropic's verification programs, with identical specifications and pricing.

#### [release-notes/system-prompts/claude-fable-5-2](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/release-notes/system-prompts/claude-fable-5-2.md) [[Source](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-2)]

Published system prompt for Claude Fable 5.2.

### Changed documents

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Added Fable 5.2 and Mythos 5.2 pricing: $8/$40, 0.025x cache reads, and $4/$20 on the Batch API. [[lines 19-20](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/about-claude/pricing.md?plain=1#L19-L20)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#model-pricing)]
* Added fast mode for Fable 5.2 and Mythos 5.2 at $16/$80, including availability on Google Cloud and Foundry. [[lines 167-181](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/about-claude/pricing.md?plain=1#L167-L181)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing#fast-mode-pricing)]

#### [agents-and-tools/tool-use/advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Fable 5.2 and Mythos 5.2 were added as executors and advisors. Fable 5.2 and Mythos 5.2 executors accept only those two as advisors.
* Switching advisor models or toggling `caching` mid-conversation edits `tools`, which returns a 400 where the prefix check is enforced.

#### [api/rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Fable 5.2 has its own row in the rate limit tables (4,000 RPM, 500K ITPM, 100K OTPM).

#### [build-with-claude/fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Added fast mode for Fable 5.2 and Mythos 5.2 on the Claude API (`speed: "fast"`).

#### [build-with-claude/effort](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Updated effort guidance and defaults for Fable 5.2.

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* Documented the prefix check (enforced for every account on Fable 5.2 and Mythos 5.2) and account-bound thinking blocks.

#### [build-with-claude/prompt-engineering/claude-prompting-best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/build-with-claude/prompt-engineering/claude-prompting-best-practices.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)]

* Added Fable 5.2 guidance and links to the new prompting guide.

#### [agents-and-tools/tool-use/computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Added the `computer_toolset_20260801` toolset for Fable 5.2 and Mythos 5.2. The earlier `computer_20251124` tool returns a 400 there, except on Amazon Bedrock.

#### [build-with-claude/refusals-and-fallback](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* Updated fallback behavior and refusal billing to include Fable 5.2 and Mythos 5.2.

#### [models/overview](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/models/overview.md) [[Source](https://platform.claude.com/docs/en/models/overview)]

* Fable 5.2 and Mythos 5.2 are now the latest models, and the model comparison tables were updated.

#### [models/fable-5-1/overview](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/models/fable-5-1/overview.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/overview)]

* Reworked to point to Fable 5.2 as the successor. Fable 5.1 now returns the prefix-check error by default on accounts created on or after August 31, 2026.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added the November 9, 2026 entry covering the Fable 5.2 and Mythos 5.2 launch, their breaking changes, 30-day data retention requirement, and fast mode. [[lines 15-25](https://github.com/gpambrozio/ClaudeDocs/blob/8d17e90f02f9386e506041167cd070fd6395c03b/docs-md/api/release-notes/overview.md?plain=1#L15-L25)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#november-9-2026)]

#### Other platform and model pages

Cloud platform pages (Bedrock, Foundry, Google Cloud, Claude Platform on AWS), the data retention and residency pages, and the context windows, thinking, compaction, task budgets and token counting pages were updated to add Fable 5.2 and Mythos 5.2 availability and requirements. Many managed-agents and tool-use pages gained a small line each, mostly pointers to the new models.
