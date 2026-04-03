# [Claude docs changes for April 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/8beb9b4845315420de6af0c2d222028830915df5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/8beb9b4845315420de6af0c2d222028830915df5)]

## Executive Summary
- **Distributed tracing support (beta)**: Claude Code can now export distributed traces via OpenTelemetry, with new env vars and backend recommendations for tools like Jaeger, Grafana Tempo, and Datadog
- **CLAUDE.local.md**: New personal, gitignored project-specific instructions file that loads alongside `CLAUDE.md`, allowing per-worktree private notes without affecting version control
- **Computer use on Windows**: Desktop app computer use is now available on Windows in addition to macOS
- **Python SDK parity**: Per-step token breakdowns and the `dontAsk` permission mode are now available in the Python SDK (previously TypeScript-only)
- **Plugin bin/ directory + marketplace CLI**: Plugins can now ship executables under `bin/`, and marketplaces can be managed via `claude plugin marketplace` CLI subcommands

## New Claude Code versions

### [2.1.91](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/versions/2.1.91.md)

#### New features

* Added MCP tool result persistence override via `_meta["anthropic/maxResultSizeChars"]` annotation (up to 500,000 characters), allowing larger results like DB schemas to pass through without truncation
* Added `disableSkillShellExecution` setting to disable inline shell execution in skills, custom slash commands, and plugin commands
* Added support for multi-line prompts in `claude-cli://open?q=` deep links (URL-encoded newlines `%0A` no longer rejected)
* Plugins can now ship executables under `bin/` and invoke them as bare commands from the Bash tool

#### Existing feature improvements

* `/feedback` now explains why it's unavailable instead of disappearing from the slash menu
* Improved `/claude-api` skill guidance for agent design patterns including tool surface decisions, context management, and caching strategy
* Improved performance: faster `stripAnsi` on Bun by routing through `Bun.stripANSI`
* Edit tool now uses shorter `old_string` anchors, reducing output tokens

#### Major bug fixes

* Fixed transcript chain breaks on `--resume` that could lose conversation history when async transcript writes fail silently
* Fixed `cmd+delete` not deleting to start of line on iTerm2, kitty, WezTerm, Ghostty, and Windows Terminal
* Fixed plan mode in remote sessions losing track of the plan file after a container restart, which caused permission prompts on plan edits and an empty plan-approval modal
* Fixed JSON schema validation for `permissions.defaultMode: "auto"` in settings.json

-----

## Claude Code changes

### Changed documents

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Added reference link to "Bedrock token burndown and quotas" documentation [[line 258](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/amazon-bedrock.md?plain=1#L258)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#additional-resources)]

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added `CLAUDE.local.md` as a new file location — a personal, project-specific notes file that should be gitignored [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/best-practices.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/best-practices#explore-first-then-plan-then-code)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Added new `/powerup` command: "Discover Claude Code features through quick interactive lessons with animated demos" [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/commands.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/commands)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Clarified `/resume` picker behavior: only shows interactive sessions; sessions from `claude -p` or SDK invocations don't appear but can still be resumed via `claude --resume <session-id>` [[~line 117](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/common-workflows.md?plain=1#L117)]
* Documented that subagent worktrees orphaned by a crash or interrupted parallel run are automatically removed at startup once older than `cleanupPeriodDays`, provided they have no modifications or unpushed commits; worktrees created with `--worktree` are never removed by this sweep [[~line 125](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/common-workflows.md?plain=1#L125)]

#### [computer-use](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/computer-use.md) [[Source](https://code.claude.com/docs/en/computer-use)]

* Clarified that Desktop app computer use is available on macOS and Windows (not just macOS) [[~line 147](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/computer-use.md?plain=1#L147)]
* Added platform comparison row to the Desktop vs CLI table: Desktop supports macOS and Windows; CLI supports macOS only [[~line 160](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/computer-use.md?plain=1#L160)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Computer use availability extended to Windows throughout the document [[~lines 207-283](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/desktop.md?plain=1#L207-L283)]
* On Windows, the computer use toggle takes effect immediately; macOS still requires granting Accessibility and Screen Recording permissions [[~line 240](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/desktop.md?plain=1#L240)]
* `CLAUDE.md` and `CLAUDE.local.md` are both used by Desktop and CLI [[~line 274](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/desktop.md?plain=1#L274)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added new env var `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE`: when set to `1`, keeps the existing marketplace cache when a `git pull` fails instead of wiping and re-cloning — useful in offline/airgapped environments [[line 104](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/env-vars.md?plain=1#L104)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Corrected teleport command syntax: `/teleport` updated to `claude --teleport` [[~line 14](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/index.md?plain=1#L14)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added `Alt+T` to the list of shortcuts that require Option-as-Meta configuration in macOS terminals [[~line 401](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/interactive-mode.md?plain=1#L401)]
* Updated VS Code configuration instruction: now correctly directs users to set `"terminal.integrated.macOptionIsMeta": true` in VS Code settings [[~line 406](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/interactive-mode.md?plain=1#L406)]
* Changed `Ctrl+L` description from "Clear terminal screen" to "Redraw the screen" (conversation history is preserved) [[~line 415](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/interactive-mode.md?plain=1#L415)]
* Extended thinking toggle no longer requires `/terminal-setup`; configure Option as Meta in your terminal instead [[~line 424](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/interactive-mode.md?plain=1#L424)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Added new global action `app:redraw` bound to `Ctrl+L` [[~line 454](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/keybindings.md?plain=1#L454)]
* Added second default binding for `chat:undo`: now `Ctrl+\_` and `Ctrl+Shift+-` [[~line 463](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/keybindings.md?plain=1#L463)]
* Added new confirmation context action `confirm:toggle` bound to `Space` [[~line 471](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/keybindings.md?plain=1#L471)]
* Updated `transcript:exit` default bindings to include `q` (previously only `Ctrl+C` and `Escape`) [[~line 480](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/keybindings.md?plain=1#L480)]
* Added new settings context action `settings:close` bound to `Enter` (saves and closes; `Escape` discards and closes) [[~line 488](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/keybindings.md?plain=1#L488)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added new MCP server entries: **Exa** (Web Search + Code Docs Search), **Fiscal.ai** (Public Equity Fundamental Data), **Lucid** (Ideate, diagram, and align teams), **Enterpret Wisdom**, **GoCardless**, **IFTTT** [[~lines 500-562](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/mcp.md?plain=1#L500-L562)]
* Added new section "Override result size per tool": MCP server authors can set `_meta["anthropic/maxResultSizeChars"]` in a tool's `tools/list` response to allow individual tools to return results larger than the default limit (up to 500,000 characters) [[line 1605](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/mcp.md?plain=1#L1605)] [[Source](https://code.claude.com/docs/en/mcp#override-result-size-per-tool)]

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added `CLAUDE.local.md` as a new "Local instructions" scope in the CLAUDE.md files table [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/memory.md?plain=1#L43)] [[Source](https://code.claude.com/docs/en/memory#choose-where-to-put-claude-md-files)]
* Documented full behavior of `CLAUDE.local.md`: loaded alongside `CLAUDE.md`, appended after it so personal notes take precedence when instructions conflict; not loaded from additional directories; works across worktrees via home directory imports [[lines 80-123](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/memory.md?plain=1#L80-L123)] [[Source](https://code.claude.com/docs/en/memory#import-additional-files)]
* Updated `/memory` command description: now lists `CLAUDE.local.md` files as well [[line 316](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/memory.md?plain=1#L316)] [[Source](https://code.claude.com/docs/en/memory#view-and-edit-with-/memory)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Updated intro to mention distributed traces via the traces protocol (beta) [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/monitoring-usage.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/monitoring-usage)]
* Added new env var `OTEL_LOG_TOOL_CONTENT`: enables logging of tool input/output content in span events (requires tracing, truncated at 60 KB) [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/monitoring-usage.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)]
* Added new "Traces (beta)" subsection: enabled via `CLAUDE_CODE_ENABLE_TELEMETRY=1` and `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`, includes trace-specific env vars (`OTEL_TRACES_EXPORTER`, `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL`, `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT`) [[lines 94-104](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/monitoring-usage.md?plain=1#L94-L104)] [[Source](https://code.claude.com/docs/en/monitoring-usage#traces-beta)]
* Added "For traces" backend section recommending Jaeger, Zipkin, Grafana Tempo, Honeycomb, Datadog [[line 492](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/monitoring-usage.md?plain=1#L492)] [[Source](https://code.claude.com/docs/en/monitoring-usage#for-traces)]
* Added security note that `OTEL_LOG_TOOL_CONTENT=1` can expose raw file contents and Bash output in trace spans [[~line 500](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/monitoring-usage.md?plain=1#L500)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Corrected teleport command syntax: `/teleport` updated to `claude --teleport` [[~line 14](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/overview.md?plain=1#L14)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Clarified that `acceptEdits` auto-approves file edits "except in protected directories" [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/permission-modes.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]
* Added new paragraph: writes to `.git`, `.vscode`, `.idea`, `.husky`, and `.claude` are never auto-approved in any mode (with exceptions for `.claude/commands`, `.claude/agents`, `.claude/skills`) [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/permission-modes.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/permission-modes#available-modes)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Added `.husky` to the list of directories protected even in `bypassPermissions` mode [[~line 847](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/permissions.md?plain=1#L847)]
* Added note: when sandboxing is enabled with `autoAllowBashIfSandboxed: true` (the default), sandboxed Bash commands run without prompting even if permissions include `ask: Bash(*)` [[~line 855](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/permissions.md?plain=1#L855)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Added guidance to use `CLAUDE_CODE_PLUGIN_CACHE_DIR` to install plugins directly to a seed path during container image builds, avoiding a separate copy step [[lines 570-577](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugin-marketplaces.md?plain=1#L570-L577)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#pre-populate-plugins-for-containers)]
* Added note that `remove` and `update` commands are blocked against seed-managed marketplaces [[line 584](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugin-marketplaces.md?plain=1#L584)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#pre-populate-plugins-for-containers)]
* Added new section "Manage marketplaces from the CLI" with full documentation of `claude plugin marketplace add`, `list`, `remove`, and `update` subcommands [[lines 780-873](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugin-marketplaces.md?plain=1#L780-L873)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#manage-marketplaces-from-the-cli)]
* Added troubleshooting entry for "Marketplace updates fail in offline environments" explaining the `CLAUDE_CODE_PLUGIN_KEEP_MARKETPLACE_ON_FAILURE=1` workaround [[line 946](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugin-marketplaces.md?plain=1#L946)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#marketplace-updates-fail-in-offline-environments)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Added `bin/` directory to the plugin components table: executables placed here are added to the Bash tool's PATH while the plugin is enabled [[line 180](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugins.md?plain=1#L180)] [[Source](https://code.claude.com/docs/en/plugins#plugin-structure-overview)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Added `bin/` directory as a plugin component with full documentation: executables placed here are added to the Bash tool's PATH while the plugin is enabled [[~line 1061](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/plugins-reference.md?plain=1#L1061)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Removed `claude commit` from the quick-reference commands table [[~line 1120](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/quickstart.md?plain=1#L1120)]
* Corrected exit instruction: `exit` or `Ctrl+D` (not `Ctrl+C`) [[~line 1124](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/quickstart.md?plain=1#L1124)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Clarified sandbox auto-allow mode: explicit `ask` rules now only apply to commands that fall back to the regular permission flow (not to sandboxed commands) [[~line 1137](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/sandboxing.md?plain=1#L1137)]
* Fixed `excludedCommands` example: entry for docker should be `"docker *"` (with glob) rather than just `"docker"` [[~line 1146](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/sandboxing.md?plain=1#L1146)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `CLAUDE.local.md` as the local scope for the CLAUDE.md row in the scopes table [[~line 1168](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/settings.md?plain=1#L1168)]
* Updated `cleanupPeriodDays` description: also controls automatic removal of orphaned subagent worktrees [[~line 1177](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/settings.md?plain=1#L1177)]
* Updated `disableDeepLinkRegistration` description: the `q` parameter in deep links now supports multi-line prompts via URL-encoded newlines (`%0A`) [[~line 1184](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/settings.md?plain=1#L1184)]
* Updated `excludedCommands` example: corrected from `["docker"]` to `["docker *"]` (glob syntax required) [[~line 1201](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/settings.md?plain=1#L1201)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Updated `allowed-tools` frontmatter syntax: now uses space-separated string (`Read Grep`) instead of comma-separated (`Read, Grep`); accepts a space-separated string or a YAML list [[~lines 1264-1274](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/skills.md?plain=1#L1264-L1274)]

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* Added new status line field `workspace.added_dirs`: additional directories added via `/add-dir` or `--add-dir` [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/statusline.md?plain=1#L140)] [[Source](https://code.claude.com/docs/en/statusline#available-data)]
* Added new status line field `session_name`: custom session name set with `--name` or `/rename` (absent if not set) [[line 154](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/statusline.md?plain=1#L154)] [[Source](https://code.claude.com/docs/en/statusline#available-data)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Updated `acceptEdits` mode description: "Auto-accept file edits except in protected directories" [[~line 1368](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/sub-agents.md?plain=1#L1368)]
* Added `.husky` to the list of protected directories in the `bypassPermissions` warning [[~line 1375](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/sub-agents.md?plain=1#L1375)]

#### [terminal-guide](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/terminal-guide.md) [[Source](https://code.claude.com/docs/en/terminal-guide)]

* Corrected exit instruction: `Ctrl+D` (not `Ctrl+C`) to exit Claude Code [[~line 1397](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/claude-code/terminal-guide.md?plain=1#L1397)]

-----

## API changes

### Changed documents

#### [agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/agent-loop.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/agent-loop)]

* Clarified that in TypeScript, the compact boundary is a separate `SDKCompactBoundaryMessage` type rather than a subtype of `SDKSystemMessage` [[~line 10](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/agent-loop.md?plain=1#L10)]
* Added `"auto"` (TypeScript only) permission mode to the modes table: uses a model classifier to approve or deny each tool call [[~line 20](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/agent-loop.md?plain=1#L20)]

#### [api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/build-with-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]

* Renamed "HIPAA compliance" to "HIPAA readiness" throughout the document — language now describes the offering as "HIPAA-ready" rather than "HIPAA-compliant"; the section now clarifies that HIPAA-ready API access no longer requires ZDR [[lines 10-64](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/build-with-claude/api-and-data-retention.md?plain=1#L10-L64)] [[Source](https://platform.claude.com/docs/en/build-with-claude/api-and-data-retention)]

#### [cost-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/cost-tracking.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/cost-tracking)]

* Updated documentation: Python SDK now exposes per-step token breakdowns on each assistant message via `message.usage` and `message.message_id` (previously documented as TypeScript-only) [[~lines 43-56](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/cost-tracking.md?plain=1#L43-L56)]
* Renamed section from "Track detailed usage in TypeScript" to "Track per-step and per-model usage" [[~line 74](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/cost-tracking.md?plain=1#L74)]

#### [file-checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/file-checkpointing.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/file-checkpointing)]

* Added `-p` flag to the CLI rewind command: `claude -p --resume <session-id> --rewind-files <checkpoint-uuid>` [[~line 99](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/file-checkpointing.md?plain=1#L99)]

#### [hosting](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/hosting.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/hosting)]

* Clarified that the Claude Code CLI is bundled in both SDK packages — no separate install needed [[~line 113](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/hosting.md?plain=1#L113)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/mcp.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp)]

* Corrected `.mcp.json` loading behavior: the SDK does not load filesystem settings automatically; `settingSources: ["project"]` must be set explicitly [[~line 126](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/mcp.md?plain=1#L126)]

#### [modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/modifying-system-prompts.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Corrected TypeScript `systemPrompt` syntax: `{ type: "preset", preset: "claude_code" }` (was missing the `type` field) [[~line 148](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/modifying-system-prompts.md?plain=1#L148)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/permissions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]

* `dontAsk` permission mode is now available in both Python and TypeScript (previously TypeScript-only) [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/permissions.md?plain=1#L79)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]
* Added new `auto` mode (TypeScript only) to the modes table: uses a model classifier to approve or deny each tool call [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/permissions.md?plain=1#L83)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/plugins.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/plugins)]

* Fixed code example: `message.message.content` instead of `message.content` to correctly access assistant message content [[~line 212](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/plugins.md?plain=1#L212)]

#### [python](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* Added `"dontAsk"` to the `PermissionMode` type definition [[line 983](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/python.md?plain=1#L983)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* Added `message_id: str | None` field to `AssistantMessage` dataclass: API message ID shared by all messages from one turn [[line 1344](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/python.md?plain=1#L1344)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]
* Added `model_usage: dict[str, Any] | None` field to `ResultMessage` dataclass with full documentation of the inner dict keys (`inputTokens`, `outputTokens`, `cacheReadInputTokens`, `cacheCreationInputTokens`, `webSearchRequests`, `costUSD`, `contextWindow`, `maxOutputTokens`) [[line 1401](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/python.md?plain=1#L1401)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/quickstart.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/quickstart)]

* Removed TypeScript-only restriction from `dontAsk` mode; added `auto` (TypeScript only) permission mode to the table [[~line 290](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/quickstart.md?plain=1#L290)]

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added new remote MCP server entries: **Exa**, **Fiscal.ai**, **Lucid**, **Intuit Credit Karma**, **Enterpret Wisdom**, **GoCardless**, **IFTTT** [[~lines 389-486](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L389-L486)]

#### [streaming-output](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/streaming-output.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/streaming-output)]

* Clarified compact boundary message type names per SDK: `SDKCompactBoundaryMessage` in TypeScript vs `SystemMessage` with subtype `"compact_boundary"` in Python [[~line 317](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/streaming-output.md?plain=1#L317)]

#### [structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/structured-outputs)]

* Updated result message checks: added `message.subtype === "success"` guard to all `message.type === "result"` checks to prevent processing error results as structured data [[~lines 330-349](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/structured-outputs.md?plain=1#L330-L349)]

#### [typescript](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Added `"auto"` to the `PermissionMode` type union: "Use a model classifier to approve or deny each tool call" [[line 541](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/typescript.md?plain=1#L541)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

#### [typescript-v2-preview](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/typescript-v2-preview.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript-v2-preview)]

* Added `msg.subtype === "success"` guard to result message check [[~line 363](https://github.com/gpambrozio/ClaudeDocs/blob/8beb9b4845315420de6af0c2d222028830915df5/docs-md/api/agent-sdk/typescript-v2-preview.md?plain=1#L363)]
