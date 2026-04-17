# [Claude docs changes for April 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/2792971) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/2792971)]

## Executive Summary
- **Claude Opus 4.7 launched** as the most capable generally available model, with step-change improvements in agentic coding, high-resolution image support (up to 2576px), and a new `xhigh` effort level — requires Claude Code v2.1.111+
- **Task budgets (beta)** introduced for Opus 4.7: a new advisory token budget that lets the model self-regulate token spend across an agentic loop using the `task-budgets-2026-03-13` beta header
- **`/ultrareview` command** added: runs a deep, multi-agent code review in a cloud sandbox with independent verification of findings, available for Pro/Max users with 3 free runs
- **Session recap** automatically generates a one-line summary when you return to a terminal after 3+ minutes away, keeping you oriented in long sessions
- **`ENABLE_PROMPT_CACHING_1H`** now covers Vertex AI and Foundry in addition to Bedrock, and the `--enable-auto-mode` flag was removed in favor of Auto mode being built into the `Shift+Tab` cycle by default

## New Claude Code versions

### [2.1.111](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/versions/2.1.111.md)

#### New features

* Added Claude Opus 4.7 support with new `xhigh` effort level, sitting between `high` and `max`. Available via `/effort`, `--effort`, and the model picker
* Auto mode is now available for Max subscribers when using Opus 4.7
* Added `/ultrareview` for comprehensive cloud-based code review using parallel multi-agent analysis — invoke with no arguments to review your current branch, or `/ultrareview <PR#>` for a specific GitHub PR
* Added `/less-permission-prompts` skill that scans transcripts for common read-only Bash and MCP tool calls and proposes an allowlist for `.claude/settings.json`
* Added "Auto (match terminal)" theme option that matches your terminal's dark/light mode — select from `/theme`
* Windows: PowerShell tool is progressively rolling out; opt in/out with `CLAUDE_CODE_USE_POWERSHELL_TOOL`

#### Existing feature improvements

* Auto mode no longer requires `--enable-auto-mode`; it is now available in the `Shift+Tab` cycle by default
* Read-only Bash commands with glob patterns (e.g. `ls *.ts`) and `cd <project-dir> &&` prefixes no longer trigger a permission prompt
* `/effort` now opens an interactive slider when called without arguments, with arrow-key navigation
* Plan files are now named after your prompt instead of purely random words
* `Ctrl+U` now clears the entire input buffer (previously: delete to start of line); press `Ctrl+Y` to restore
* `Ctrl+L` now forces a full screen redraw in addition to clearing the prompt input
* Transcript view footer now shows `[` (dump to scrollback) and `v` (open in editor) shortcuts
* Improved `/setup-vertex` and `/setup-bedrock` to show actual `settings.json` path when `CLAUDE_CONFIG_DIR` is set, seed model candidates from existing pins on re-run, and offer a "1M context" option
* Headless `--output-format stream-json` now includes `plugin_errors` on the init event when plugins are demoted for unsatisfied dependencies
* Typo suggestion for near-miss subcommands (e.g. `claude udpate` → "Did you mean `claude update`?")

#### Major bug fixes

* Fixed terminal display tearing in iTerm2 + tmux setups when terminal notifications are sent
* Fixed `@` file suggestions re-scanning the entire project on every turn in non-git working directories
* Fixed LSP diagnostics from before an edit appearing after it, causing the model to re-read files it just edited
* Fixed tab-completing `/resume` immediately resuming an arbitrary titled session instead of showing the session picker
* Fixed `/clear` dropping the session name set by `/rename`
* Fixed Claude calling a non-existent `commit` skill for users without a custom `/commit` command
* Fixed 429 rate-limit errors on Bedrock/Vertex/Foundry incorrectly referencing status.claude.com
* Windows: `CLAUDE_ENV_FILE` and SessionStart hook environment files now apply (previously a no-op)
* Windows: permission rules with drive-letter paths are now correctly root-anchored

### [2.1.112](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/versions/2.1.112.md)

#### Major bug fixes

* Fixed "claude-opus-4-7 is temporarily unavailable" error for auto mode

-----

## Claude Code changes

### New Documents

#### [Errors](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

Comprehensive error reference page listing all runtime errors Claude Code displays, with explanations and recovery steps for each. Covers server errors, usage limits, authentication errors, network errors, and request errors including the new `thinking.type.enabled` error when using Opus 4.7 with an outdated SDK.

#### [Plugin Dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/plugin-dependencies.md) [[Source](https://code.claude.com/docs/en/plugin-dependencies)]

New guide for plugin authors on declaring versioned dependencies in `plugin.json`. Covers the `~2.1.0`-style semver constraint syntax, how Claude Code resolves and intersects ranges from multiple plugins, release tagging convention (`{plugin-name}--v{version}`), and how to diagnose `range-conflict`, `dependency-version-unsatisfied`, and `no-matching-tag` errors. Requires Claude Code v2.1.110+.

#### [Plugin Hints](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/plugin-hints.md) [[Source](https://code.claude.com/docs/en/plugin-hints)]

New guide for CLI/SDK maintainers on how to emit a `<claude-code-hint />` tag to stderr to recommend a plugin install to Claude Code users. Claude Code strips the hint from command output (no token impact) and shows a one-time install prompt. Covers format, placement strategies, and requirements for being listed in the official Anthropic marketplace.

#### [Ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

New document for the `/ultrareview` command — a deep code review that runs a fleet of reviewer agents in a remote cloud sandbox to find bugs with independent verification. Pro and Max subscribers get 3 free runs; subsequent reviews are billed as extra usage (~$5–$20 per review). Reviews run in the background in 5–10 minutes and results appear as a notification.

### Changed documents

#### [Agent SDK - Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* Clarified that shell command hooks from settings files load when the corresponding `settingSources`/`setting_sources` entry is enabled, which it is for default `query()` options. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#how-hooks-work)]

#### [Agent SDK - Migration Guide](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/migration-guide.md) [[Source](https://code.claude.com/docs/en/agent-sdk/migration-guide)]

* Updated `settingSources` default behavior: current SDK releases have reverted to loading all settings by default for `query()`, matching the CLI. Pass `settingSources: []` explicitly to get isolated behavior; Python SDK 0.1.59 and earlier treated an empty list the same as omitting the option. [[line 206](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/migration-guide.md?plain=1#L206)] [[Source](https://code.claude.com/docs/en/agent-sdk/migration-guide#settings-sources-no-longer-loaded-by-default)]
* Code examples updated to reference `claude-opus-4-7`.

#### [Agent SDK - Overview](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* Added note that Opus 4.7 requires Agent SDK v0.2.111 or later, with troubleshooting pointer for `thinking.type.enabled` API errors. [[line 6](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/overview.md?plain=1#L6)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]
* Clarified that with default options the SDK loads settings from `.claude/` in the working directory and `~/.claude/`; `setting_sources` controls which sources load.

#### [Agent SDK - Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Updated `setting_sources` documentation: project settings load by default for `query()` options; pass `setting_sources` explicitly with `"project"` if you set it. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)]
* Clarified subagent permission inheritance: `acceptEdits` and `auto` modes also inherit to subagents, not just `bypassPermissions`. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#available-modes)]

#### [Agent SDK - Python](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `effort` parameter now accepts `"xhigh"` as a valid literal for Opus 4.7. [[line 756](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/python.md?plain=1#L756)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)]
* `setting_sources` default updated to reflect that `query()` now loads all settings by default (CLI defaults: all sources). [[line 795](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/python.md?plain=1#L795)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)]
* `max_budget_usd` documentation clarified as a client-side cost estimate comparison. [[line 770](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/python.md?plain=1#L770)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)]

#### [Agent SDK - Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/quickstart.md) [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart)]

* Added troubleshooting section for `thinking.type.enabled` API error on Opus 4.7, directing users to upgrade to Agent SDK v0.2.111. [[line 236](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/quickstart.md?plain=1#L236)] [[Source](https://code.claude.com/docs/en/agent-sdk/quickstart#key-concepts)]

#### [Agent SDK - TypeScript v2 Preview](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/agent-sdk/typescript-v2-preview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript-v2-preview)]

* All code examples updated to reference `claude-opus-4-7`.

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Removed promotional banner from the top of the page.
* Added guidance that `ANTHROPIC_DEFAULT_OPUS_MODEL` defaults to Opus 4.6 on Bedrock; set it to the Opus 4.7 ID to use the latest model. [[line 146](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/amazon-bedrock.md?plain=1#L146)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)]
* Updated `modelOverrides` example to include `claude-opus-4-7`. [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/amazon-bedrock.md?plain=1#L182)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#map-each-model-version-to-an-inference-profile)]
* Opus 4.7 now supports the 1M token context window on Bedrock; setup wizard offers 1M option when pinning models. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/amazon-bedrock.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#iam-configuration)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--effort` now accepts `xhigh` as a valid level. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/cli-reference.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* `--enable-auto-mode` flag removed in v2.1.111; auto mode is in the `Shift+Tab` cycle by default; use `--permission-mode auto` to start in it. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/cli-reference.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* New typo suggestion behavior documented: near-miss subcommands show a "Did you mean?" suggestion. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/cli-reference.md?plain=1#L24)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [Claude Code on the Web](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* New "Environment caching" section: the setup script runs once, then Anthropic snapshots the filesystem and reuses it as the starting point for later sessions — keeping startup fast even for large toolchains. Cache rebuilds when the script or allowed network hosts change, or after ~7 days. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#setup-scripts)]
* Docker improvements: added guidance for `docker compose up` and caching of pulled images in setup scripts. [[line 107](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L107)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#run-tests-start-services-and-add-packages)]
* Setup scripts vs. SessionStart hooks table updated to reflect the new cached environment behavior.

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Extended thinking section updated: Opus 4.7 always uses adaptive reasoning and does not support `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING`. [[line 540](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/common-workflows.md?plain=1#L540)] [[Source](https://code.claude.com/docs/en/common-workflows#configure-thinking-mode)]
* Session picker improvements: `/resume` now has keyboard shortcuts to widen to other worktrees or projects, search, preview, and rename. [[line 568](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/common-workflows.md?plain=1#L568)] [[Source](https://code.claude.com/docs/en/common-workflows#resume-previous-conversations)]
* Rename shortcut in session picker changed from `R` to `Ctrl+R`. [[line 594](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/common-workflows.md?plain=1#L594)] [[Source](https://code.claude.com/docs/en/common-workflows#name-your-sessions)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Download links for macOS (Universal) and Windows (x64/ARM64) added directly to the page.
* Auto mode availability clarified: now requires Sonnet 4.6, Opus 4.6, or Opus 4.7 on Team/Enterprise/API; Opus 4.7 only on Max plans; not available on Pro or third-party providers. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/desktop.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/desktop#choose-a-permission-mode)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_DISABLE_ADAPTIVE_THINKING`: clarified it has no effect on Opus 4.7, which always uses adaptive reasoning. [[line 59](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/env-vars.md?plain=1#L59)] [[Source](https://code.claude.com/docs/en/env-vars)]
* `CLAUDE_CODE_EFFORT_LEVEL`: `xhigh` added as valid value. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/env-vars.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `CLAUDE_CODE_ENABLE_AWAY_SUMMARY`: override session recap availability independent of `/config` toggle. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/env-vars.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `CLAUDE_CODE_ENABLE_BACKGROUND_PLUGIN_REFRESH`: opt in to refreshing plugin state at turn boundaries after a background install in non-interactive mode. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/env-vars.md?plain=1#L81)] [[Source](https://code.claude.com/docs/en/env-vars)]
* `ENABLE_PROMPT_CACHING_1H` replaces `ENABLE_PROMPT_CACHING_1H_BEDROCK` (which is now deprecated): now works for API key, Bedrock, Vertex, and Foundry users. [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/env-vars.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `FORCE_PROMPT_CACHING_5M`: force 5-minute cache TTL even when 1-hour TTL would otherwise apply. [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/env-vars.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/env-vars)]
* `CLAUDE_CODE_USE_POWERSHELL_TOOL` behavior updated: now progressively rolling out on Windows; also available on Linux/macOS with `pwsh` on PATH. [[line 139](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/env-vars.md?plain=1#L139)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Fast Mode](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Added explicit note that fast mode is not available on Opus 4.7 or other models. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/fast-mode.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/fast-mode)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Announcement updated: Claude Opus 4.7 is now available; configure the model parameter to `claude-opus-4-7` to use it. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/github-actions.md?plain=1#L4)] [[Source](https://code.claude.com/docs/en/github-actions)]

#### [Headless](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New documentation for `system/init` event: lists `plugins` and `plugin_errors` fields for checking plugin load status in CI. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/headless.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/headless#stream-responses)]
* New documentation for `system/plugin_install` events emitted when `CLAUDE_CODE_SYNC_PLUGIN_INSTALL` is set. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/headless.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/headless#stream-responses)]
* Read-only command set referenced in `dontAsk` mode description. [[line 149](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/headless.md?plain=1#L149)] [[Source](https://code.claude.com/docs/en/headless#auto-approve-tools)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `PermissionRequest` hook `behavior: "allow"` clarified: deny-and-ask rules are still evaluated; a hook returning `"allow"` does not override a matching deny rule. [[line 1031](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/hooks.md?plain=1#L1031)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-decision-control)]
* `updatedInput` now re-evaluated against deny and ask rules after modification. [[line 1031](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/hooks.md?plain=1#L1031)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-decision-control)]
* `setMode` with `bypassPermissions` documented: only takes effect when bypass mode was already available at session launch. [[line 1064](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/hooks.md?plain=1#L1064)] [[Source](https://code.claude.com/docs/en/hooks#permission-update-entries)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New "Session recap" section: Claude Code automatically generates a one-line recap when returning to a terminal after 3+ minutes; toggle with `/config` or `CLAUDE_CODE_ENABLE_AWAY_SUMMARY`. [[line 279](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/interactive-mode.md?plain=1#L279)] [[Source](https://code.claude.com/docs/en/interactive-mode#task-list)]
* `Ctrl+G` / external editor now supports a "Show last response in external editor" `/config` option that prepends Claude's previous reply as commented context. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/interactive-mode.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* `Ctrl+L` clarified: also forces a full terminal redraw to recover garbled display.
* New transcript viewer shortcuts: `[` dumps conversation to terminal scrollback; `v` opens in `$VISUAL`/`$EDITOR`. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/interactive-mode.md?plain=1#L74)] [[Source](https://code.claude.com/docs/en/interactive-mode#transcript-viewer)]
* `Ctrl+U` updated: now clears the entire input buffer; `Cmd+Backspace` deletes from cursor to line start.

#### [Model Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `opus` alias now resolves to Opus 4.7 on the Anthropic API; on Bedrock/Vertex/Foundry it still resolves to Opus 4.6. Opus 4.7 requires Claude Code v2.1.111+. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/model-config.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]
* Default model for Max and Team Premium plans changed to Opus 4.7; Enterprise pay-as-you-go and Anthropic API will switch to Opus 4.7 default on April 23, 2026. [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/model-config.md?plain=1#L111)] [[Source](https://code.claude.com/docs/en/model-config#special-model-behavior)]
* New effort level table: Opus 4.7 supports `low`, `medium`, `high`, `xhigh`, `max`; Opus 4.6 and Sonnet 4.6 support `low`, `medium`, `high`, `max`. Unsupported levels fall back to the nearest lower supported level. [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/model-config.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/model-config#opusplan-model-setting)]
* Opus 4.7 default effort is `xhigh` for all plans and providers. [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/model-config.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/model-config#opusplan-model-setting)]
* `/model` picker now asks for confirmation when switching mid-conversation. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/model-config.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* New "Read-only commands" section: built-in set of commands (ls, cat, grep, find, etc.) always run without a permission prompt; unquoted glob patterns allowed for fully read-only commands. [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/permissions.md?plain=1#L116)] [[Source](https://code.claude.com/docs/en/permissions#process-wrappers)]
* New symlink permission rules: allow rules check both symlink and target (require both to match); deny rules block when either matches. [[line 159](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/permissions.md?plain=1#L159)] [[Source](https://code.claude.com/docs/en/permissions#read-and-edit)]
* Permission dialog now writes the space-separated form (e.g. `Bash(ls *)`) instead of the `:*` form for "don't ask again". [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/claude-code/permissions.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/permissions#wildcard-patterns)]

-----

## API changes

### New Documents

#### [What's New in Claude Opus 4.7](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/whats-new-claude-4-7.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-7)]

Launch overview for Claude Opus 4.7 — Anthropic's most capable generally available model. Highlights include high-resolution image support (up to 2576px / 3.75MP, 1:1 pixel coordinates for computer use), the new `xhigh` effort level, task budgets (beta), and breaking changes from Opus 4.6: extended thinking budgets removed (replaced by adaptive thinking), `temperature`/`top_p`/`top_k` sampling parameters removed, thinking content omitted by default, and a new tokenizer (up to ~35% more tokens).

#### [Task Budgets](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/build-with-claude/task-budgets.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/task-budgets)]

New guide for the task budgets beta feature on Claude Opus 4.7. A task budget (`output_config.task_budget`) gives Claude an advisory token cap for the full agentic loop (thinking + tool calls + output). The model sees a running countdown and self-regulates to finish gracefully. Distinct from `max_tokens` (a hard per-request cap). Requires the `task-budgets-2026-03-13` beta header; minimum budget is 20k tokens.

#### [CLI Beta - User Profiles API](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/cli/beta/user_profiles.md) [[Source](https://platform.claude.com/docs/en/api/cli/beta/user_profiles)]

New CLI reference for the User Profiles beta API, covering list, create, retrieve, update, and create enrollment URL endpoints.

### Changed documents

#### [Agent Skills - Claude API Skill](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]

* Skill now covers both the Messages API and Claude Managed Agents (beta). Updated language coverage table: Java, Go, PHP, and cURL now also supported for Managed Agents. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md?plain=1#L53)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]
* New `/claude-api migrate` subcommand that automates model ID swaps, breaking parameter changes, and effort calibration across a codebase when migrating to Opus 4.7. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]
* Added Managed Agents onboarding flow (`/claude-api managed-agents-onboard`), deployment constraints documentation, and prompt caching / model migration guidance.

#### [Agent Skills - Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Code examples updated from cURL/Shell to Python format with `claude-opus-4-7`.

#### [MCP Connector](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* Code examples updated from cURL to Python format with `claude-opus-4-7`.

#### [Tool Use - Overview](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Claude Opus 4.7 added to tool use system prompt token count table. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L67)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]
* Default code example tab changed from Shell/cURL to Python.

#### [Tool Use - Bash, Code Execution, Computer Use, Fine-Grained Streaming, Memory, Programmatic Tool Calling, Text Editor, Tool Search, Web Fetch, Web Search](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/agents-and-tools/tool-use/bash-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/bash-tool)]

* Across all tool reference pages: default code example tab changed from Shell/cURL to Python; model references updated to `claude-opus-4-7`; Computer Use beta header updated to include Opus 4.7; Programmatic Tool Calling model support table adds Opus 4.7; Web Search dynamic filtering now supported on Opus 4.7.

#### [Beta API](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* New `user-profiles-2026-03-24` beta header added to the supported headers list. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/beta.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* New `xhigh` field added to `BetaEffortCapability` model object. [[line 292](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/beta.md?plain=1#L292)] [[Source](https://platform.claude.com/docs/en/api/beta)]
* `BetaManagedAgentsModel` enum updated to include `claude-opus-4-7` at the top.

#### [Beta API - Agents Create/Update/List/Retrieve](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/beta/agents/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]

* `claude-opus-4-7` added as a supported `BetaManagedAgentsModel` with description "Frontier intelligence for long-running agents and coding".
* `user-profiles-2026-03-24` beta header added to all managed agents endpoints.

#### [Beta API - Sessions Create](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/beta/sessions/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/sessions/create)]

* `claude-opus-4-7` added as a supported model for sessions.
* `archived_at` example response value corrected from a placeholder date to `null`.

#### [Beta API - User Profiles](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/beta/user_profiles.md) [[Source](https://platform.claude.com/docs/en/api/beta/user_profiles)]

* API path parameter renamed from `{id}` to `{user_profile_id}` across retrieve, update, and create enrollment URL endpoints. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/beta/user_profiles.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/api/beta/user_profiles)]
* Added field descriptions for `id` (prefixed `uprof_`), `metadata` (max 16 pairs), and `trust_grants` object with `status` enum (`active`, `pending`, `rejected`). [[line 32](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/api/beta/user_profiles.md?plain=1#L32)] [[Source](https://platform.claude.com/docs/en/api/beta/user_profiles)]

#### [Model Deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* `claude-opus-4-7` added as an active model, not retiring before April 16, 2027. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/model-deprecations.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]
* Replacement recommendations for several deprecated models updated to Opus 4.7 (claude-opus-4-20250514, claude-3-opus-20240229, claude-2.0, claude-2.1); Sonnet 3.7 and Sonnet 3.5 replacements corrected to `claude-sonnet-4-6`. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/model-deprecations.md?plain=1#L86)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

#### [Migration Guide](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* Entire guide rewritten for Claude Opus 4.7 migration. Documents five breaking changes: extended thinking removed (use adaptive), sampling parameters (`temperature`/`top_p`/`top_k`) removed (400 error), thinking content omitted by default (set `display: "summarized"` to restore), new tokenizer (up to ~35% more tokens), and prefill removal (carried over from 4.6). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/migration-guide.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]
* New guidance on choosing an effort level for Opus 4.7 with description of each level. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/migration-guide.md?plain=1#L80)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

#### [Models - Choosing a Model](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/choosing-a-model.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

* Updated recommendation table to list Opus 4.7 for complex reasoning and agentic coding use cases (long-horizon coding, refactoring, complex systems engineering). [[line 55](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/choosing-a-model.md?plain=1#L55)] [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

#### [Models - Overview](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

* Claude Opus 4.7 added as the recommended model with `claude-opus-4-7` API ID. Extended thinking is not supported (uses adaptive thinking only). Knowledge cutoff updated to Jan 2026; training data cutoff Jan 2026. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/overview.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]
* Microsoft Foundry added to the list of supported platforms alongside API, Bedrock, and Vertex.
* Opus 4.7 and Sonnet 4.6 now support up to 300k output tokens on the Batch API via the `output-300k-2026-03-24` beta header. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/models/overview.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

#### [Pricing](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Claude Opus 4.7 added to all pricing tables ($5/$25 per MTok, same as Opus 4.6; batch: $2.50/$12.50). [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/pricing.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Note added that Opus 4.7 uses a new tokenizer that may use up to 35% more tokens for the same text. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/pricing.md?plain=1#L28)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* 1M token context window long-context pricing section updated to include Opus 4.7. [[line 128](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/pricing.md?plain=1#L128)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Data residency pricing (1.1x multiplier) extended to Opus 4.7. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/2792971/docs-md/api/about-claude/pricing.md?plain=1#L81)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
