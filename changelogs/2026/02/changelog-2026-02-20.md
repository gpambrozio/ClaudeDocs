# [Claude docs changes for February 20th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/f0f09b8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/f0f09b8)]

## Executive Summary

- **Git worktree isolation goes first-class**: A new `--worktree` (`-w`) CLI flag and `isolation: "worktree"` subagent field let Claude spin up isolated git worktrees automatically, replacing the previous manual `git worktree add` workflow.
- **New `ConfigChange` hook**: A new hook event fires whenever a configuration file changes during a session, enabling enterprise security auditing and the ability to block unauthorized settings changes.
- **Automatic prompt caching**: A new top-level `cache_control` field on the Messages API automatically caches the last cacheable block and advances the cache point as conversations grow — no manual breakpoint management required.
- **Model retirements and deprecations**: Claude Sonnet 3.7 and Claude Haiku 3.5 are now retired (requests return errors). Claude Haiku 3 is newly deprecated with retirement scheduled for April 20, 2026.
- **`Ctrl+F` to kill background agents**: A new keyboard shortcut kills all background agents (double-press confirmation within 3 seconds).

---

## New Claude Code versions

### [2.1.49](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/versions/2.1.49.md)

#### New features

* Added `--worktree` (`-w`) flag to start Claude in an isolated git worktree at `<repo>/.claude/worktrees/<name>`. If no name is given, one is auto-generated.
* Subagents support `isolation: "worktree"` to run in a temporary git worktree; the worktree is automatically cleaned up if the subagent makes no changes.
* Added `Ctrl+F` keybinding to kill all background agents (two-press confirmation within 3 seconds required).
* Agent definitions support `background: true` to always run as a background task.
* Plugins can ship a `settings.json` for default configuration (currently only the `agent` key is supported).
* Added `ConfigChange` hook event that fires when configuration files change during a session, enabling enterprise security auditing and optional blocking of settings changes.
* SDK model info now includes `supportsEffort`, `supportedEffortLevels`, and `supportsAdaptiveThinking` fields so consumers can discover model capabilities.
* Simple mode (`CLAUDE_CODE_SIMPLE`) now includes the file edit tool in addition to the Bash tool.
* Permission suggestions are now populated when safety checks trigger an ask response, enabling SDK consumers to display permission options.

#### Existing feature improvements

* Improved performance in non-interactive mode (`-p`) by skipping unnecessary API calls during startup.
* Improved startup performance by caching MCP authentication failures for HTTP and SSE MCP servers, avoiding repeated connection attempts.
* Improved startup performance by batching MCP tool token counting into a single API call and reducing HTTP calls for analytics token counting.
* Improved permission prompts for path safety and working directory blocks to show the reason for the restriction instead of a bare prompt.

#### Major bug fixes

* Fixed file-not-found errors to suggest corrected paths when the model drops the repo folder prefix.
* Fixed `Ctrl+C` and `ESC` being silently ignored when background agents are running and the main thread is idle. Pressing twice within 3 seconds now kills all background agents.
* Fixed prompt suggestion cache regression that reduced cache hit rates.
* Fixed `plugin enable` and `plugin disable` to auto-detect the correct scope when `--scope` is not specified, instead of always defaulting to user scope.
* Fixed verbose mode not updating thinking block display when toggled via `/config`.
* Fixed unbounded WASM memory growth during long sessions by periodically resetting the tree-sitter parser and resetting Yoga WASM linear memory.
* Fixed `disableAllHooks` setting to respect the managed settings hierarchy — non-managed settings can no longer disable managed hooks set by policy.
* Fixed `--resume` session picker showing raw XML tags for sessions that start with commands like `/clear`.

---

## Claude Code changes

### Changed documents

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--worktree` / `-w` flag documented in the CLI flags table, which starts Claude in an isolated git worktree. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/cli-reference.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* The "Run parallel Claude Code sessions with Git worktrees" section was completely rewritten around the new `--worktree` flag, replacing the old multi-step manual `git worktree add` workflow. It now includes a "Worktree cleanup" subsection describing automatic cleanup behavior and a "Manage worktrees manually" subsection for advanced use cases. [[lines 969-1130](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/common-workflows.md?plain=1#L969)] [[Source](https://code.claude.com/docs/en/common-workflows#use-the-session-picker)]
* Added a new section "Get notified when Claude needs your attention" covering how to configure desktop notifications using the `Notification` hook event, with per-OS command examples (macOS via `osascript`, Linux via `notify-send`, Windows via PowerShell). [[lines 1037-1130](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/common-workflows.md?plain=1#L1037)] [[Source](https://code.claude.com/docs/en/common-workflows#manage-worktrees-manually)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Updated the "Session isolation" row in the CLI vs Desktop comparison table to reference the `--worktree` flag with a link to the CLI reference. [[line 239](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/desktop.md?plain=1#L239)] [[Source](https://code.claude.com/docs/en/desktop#feature-comparison)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added a new "Audit configuration changes" example showing how to use the `ConfigChange` hook to log settings changes to an audit log, with a ready-to-use JSON config block. [[lines 316-351](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks-guide.md?plain=1#L316)] [[Source](https://code.claude.com/docs/en/hooks-guide#re-inject-context-after-compaction)]
* `ConfigChange` added to the hook events table with description "When a configuration file changes during a session." [[line 368](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks-guide.md?plain=1#L368)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `ConfigChange` added to the hook events summary table. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks.md?plain=1#L29)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* `ConfigChange` added to the matcher table, with supported values: `user_settings`, `project_settings`, `local_settings`, `policy_settings`, `skills`. [[line 185](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks.md?plain=1#L185)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]
* `ConfigChange` added to the blocking decision table — it can block configuration changes from taking effect (except `policy_settings`). [[line 496](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks.md?plain=1#L496)] [[Source](https://code.claude.com/docs/en/hooks#exit-code-2-behavior-per-event)]
* Full `ConfigChange` event reference added, including input schema, matcher values, decision control, and a note that `policy_settings` changes cannot be blocked. [[lines 1420-1510](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks.md?plain=1#L1420)] [[Source](https://code.claude.com/docs/en/hooks#taskcompleted-decision-control)]
* Added a note that `disableAllHooks` respects the managed settings hierarchy: user/project/local settings cannot disable managed hooks set by policy. [[line 413](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/hooks.md?plain=1#L413)] [[Source](https://code.claude.com/docs/en/hooks#disable-or-remove-hooks)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Updated the "Use git worktrees for parallel tasks" section to use the `--worktree` flag (`claude -w feature-auth`) instead of the old manual `git worktree add` workflow. [[lines 317-335](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/ide-integrations.md?plain=1#L317)] [[Source](https://code.claude.com/docs/en/ide-integrations#create-commits-and-pull-requests)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added `Ctrl+F` keyboard shortcut to the shortcuts table: kills all background agents with a two-press confirmation within 3 seconds. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/interactive-mode.md?plain=1#L16)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Added `settings.json` to the plugin directory structure example and to the plugin components table. Only `agent` settings are currently supported. [[lines 468-492](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/plugins-reference.md?plain=1#L468)] [[Source](https://code.claude.com/docs/en/plugins-reference#standard-plugin-layout)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Added `settings.json` to the plugin capabilities table with a description of its role. [[line 235](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/plugins.md?plain=1#L235)] [[Source](https://code.claude.com/docs/en/plugins#plugin-structure-overview)]
* Added a new "Ship default settings with your plugin" section documenting the `settings.json` file, including an example that activates a named agent as the main thread. [[lines 312-337](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/plugins.md?plain=1#L312)] [[Source](https://code.claude.com/docs/en/plugins#add-lsp-servers-to-your-plugin)]

#### [security](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Added `ConfigChange` hooks to the enterprise security best practices list as a way to audit or block settings changes during sessions. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/security.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/security#team-security)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Added a note that `ConfigChange` hooks can be used to detect runtime configuration changes and block unauthorized changes before they take effect. [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/server-managed-settings.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/server-managed-settings#security-considerations)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `CLAUDE_CODE_SIMPLE` environment variable to the environment variables table, documenting that it enables a minimal mode with only Bash, file read, and file edit tools (disabling MCP tools, attachments, hooks, and CLAUDE.md). [[line 920](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/settings.md?plain=1#L920)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added `background` field to the subagent YAML frontmatter table: set to `true` to always run as a background task. [[line 239](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/sub-agents.md?plain=1#L239)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* Added `isolation` field to the subagent YAML frontmatter table: set to `worktree` to run the subagent in a temporary git worktree. [[line 240](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/sub-agents.md?plain=1#L240)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Updated the "Use git worktrees for parallel tasks" section to use the `--worktree` flag (`claude -w feature-auth`) instead of the old manual workflow. [[lines 317-335](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/claude-code/vs-code.md?plain=1#L317)] [[Source](https://code.claude.com/docs/en/vs-code#create-commits-and-pull-requests)]

---

## API changes

### Changed documents

#### [about-claude/model-deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* Claude Sonnet 3.7 (`claude-3-7-sonnet-20250219`) and Claude Haiku 3.5 (`claude-3-5-haiku-20241022`) status updated from "Deprecated" to "Retired" as of February 19, 2026. [[lines 71-72](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/about-claude/model-deprecations.md?plain=1#L71)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]
* Claude Haiku 3 (`claude-3-haiku-20240307`) status changed to "Deprecated" with a retirement date of April 20, 2026. [[line 73](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/about-claude/model-deprecations.md?plain=1#L73)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]
* New deprecation history entry added for the 2026-02-19 Claude Haiku 3 deprecation announcement, with recommended replacement `claude-haiku-4-5-20251001`. [[lines 80-89](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/about-claude/model-deprecations.md?plain=1#L80)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

#### [about-claude/models/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* Added a migration code snippet for upgrading from Claude Haiku 3 to Haiku 4.5, alongside the existing Haiku 3.5 migration. [[lines 393-395](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/about-claude/models/migration-guide.md?plain=1#L393)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

#### [api/api/messages](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages.md) [[Source](https://platform.claude.com/docs/en/api/messages)]

* New `code_execution_20260120` tool type added, supporting REPL state persistence with daemon mode and gVisor checkpoint. [[line 300+](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages.md?plain=1#L1)]
* `allowed_callers` arrays across all tool types now include the new `"code_execution_20260120"` enum value.
* `CodeExecution20260120` inline type renamed to the named type `ServerToolCaller20260120` in caller union types.
* `speed` field removed from the `Usage` response object (the `"standard"/"fast"` inference speed mode field has been retired).

#### [api/api/messages/batches](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/messages/batches)]

* Same `ServerToolCaller20260120` rename, `allowed_callers` expansion, and `speed` field removal as in the Messages API reference.

#### [api/api/messages/batches/create](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/batches/create)]

* New top-level `cache_control` request parameter added for automatic prompt caching, with `type` ("ephemeral") and optional `ttl` ("5m" or "1h"). [[line 100+](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages/batches/create.md?plain=1#L1)]
* `speed` request parameter removed.
* Same `ServerToolCaller20260120` rename and `allowed_callers` expansion.

#### [api/api/messages/batches/results](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/messages/batches/results)]

* Same `ServerToolCaller20260120` rename, `speed` field removal, and `allowed_callers` expansion as in the Batches API reference.

#### [api/api/messages/count_tokens](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/messages/count_tokens)]

* New top-level `cache_control` request parameter added for automatic prompt caching.
* `speed` request parameter removed.
* Same `ServerToolCaller20260120` rename and `allowed_callers` expansion.

#### [api/api/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

* New top-level `cache_control` request parameter added for automatic prompt caching. [[line 100+](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/api/messages/create.md?plain=1#L1)]
* `speed` request parameter removed from request body and `Usage` response object.
* Same `ServerToolCaller20260120` rename and `allowed_callers` expansion.

#### [build-with-claude/claude-on-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

* Claude Haiku 3 (`anthropic.claude-3-haiku-20240307-v1:0`) marked with the deprecation warning symbol (⚠️) in the model table.

#### [build-with-claude/claude-on-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Claude Haiku 3 (`claude-3-haiku@20240307`) marked with the deprecation warning symbol (⚠️) in the model table.

#### [build-with-claude/overview](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Added "Automatic prompt caching" as a new entry in the context management table, available on the Claude API and Azure AI Foundry (preview). [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/build-with-claude/overview.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* Several features previously listed without "(Beta)" for Microsoft Foundry are now marked as "(Beta)" (Adaptive thinking, Citations, Effort, Extended thinking, PDF support, Search results, Code execution, Memory, Web fetch, Web search, Bash, Text editor, Fine-grained tool streaming, Programmatic tool calling, Tool search, Token counting, Prompt caching 5m and 1hr).

#### [build-with-claude/prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Major restructure to introduce automatic caching as the primary recommended approach. The introduction now explains two caching modes: automatic (top-level `cache_control`) and explicit (block-level `cache_control`). [[lines 1-35](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* New "Automatic caching" section added with a table showing how the cache breakpoint advances with each turn in a multi-turn conversation, plus TTL support, edge cases, and how to combine automatic and explicit caching. [[lines 110-200](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L110)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* The existing explicit cache breakpoints content reorganized under a new "Explicit cache breakpoints" heading, with the "Understanding cache breakpoint costs" section moved here.
* Best practices updated to recommend starting with automatic caching for multi-turn conversations.
* Automatic caching noted as available on the Claude API and Azure AI Foundry (preview), with Bedrock and Vertex AI support coming later.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* New February 19, 2026 release notes entry added covering: launch of automatic caching, retirement of Claude Sonnet 3.7 and Claude Haiku 3.5, and deprecation of Claude Haiku 3 with an April 19, 2026 retirement date. [[lines 1-15](https://github.com/gpambrozio/ClaudeDocs/blob/f0f09b8/docs-md/api/release-notes/overview.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
