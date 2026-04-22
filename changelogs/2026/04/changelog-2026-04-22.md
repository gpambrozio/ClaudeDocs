# [Claude docs changes for April 22nd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/76254a0) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/76254a0)]

## Executive Summary
- **New `UserPromptExpansion` hook event** lets hooks intercept and block slash commands before they expand into prompts — filling a gap that `PreToolUse` couldn't cover for direct `/skillname` invocations.
- **SDK session storage** is now supported via a `SessionStore` adapter interface, enabling session resume across machines, serverless functions, and multi-host deployments with S3, Redis, or Postgres backends.
- **Massive OpenTelemetry expansion** in monitoring docs: full span attribute reference, seven new log events (permission mode changes, auth, MCP connections, hook execution, compaction, etc.), and a new `file:<dir>` mode for `OTEL_LOG_RAW_API_BODIES` that writes untruncated bodies to disk.
- **Voyage 4 embedding models** added to the embeddings guide, including `voyage-4`, `voyage-4-large`, `voyage-4-lite`, `voyage-4-nano`, and `voyage-multimodal-3.5` with video support.
- **New "Debug your configuration" guide** consolidates all configuration diagnostic commands and a symptom-first lookup table into one dedicated page.

## New Claude Code versions

### [2.1.117](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/versions/2.1.117.md)

#### New features

* Forked subagents can now be enabled on external builds by setting `CLAUDE_CODE_FORK_SUBAGENT=1`
* Agent frontmatter `mcpServers` are now loaded for main-thread agent sessions via `--agent`
* OpenTelemetry: `user_prompt` events now include `command_name` and `command_source` for slash commands; `cost.usage`, `token.usage`, `api_request`, and `api_error` now include an `effort` attribute when the model supports effort levels
* `OTEL_LOG_RAW_API_BODIES` now supports `file:<dir>` mode for writing untruncated API bodies to disk instead of inline in events
* Native builds on macOS and Linux: `Glob` and `Grep` tools replaced by embedded `bfs` and `ugrep` available through Bash — faster searches without a separate tool round-trip

#### Existing feature improvements

* `/model` selections now persist across restarts even when the project pins a different model; startup header shows when the active model comes from a project or managed-settings pin
* `/resume` command now offers to summarize stale, large sessions before re-reading them
* Faster startup when both local and claude.ai MCP servers are configured (concurrent connect now default)
* `plugin install` on an already-installed plugin now installs any missing dependencies instead of stopping at "already installed"
* Plugin dependency errors now show "not installed" with an install hint; `claude plugin marketplace add` now auto-resolves missing dependencies from configured marketplaces
* Managed-settings `blockedMarketplaces` and `strictKnownMarketplaces` are now enforced on plugin install, update, refresh, and autoupdate
* `cleanupPeriodDays` retention sweep now also covers `~/.claude/tasks/`, `~/.claude/shell-snapshots/`, and `~/.claude/backups/`
* Advisor Tool (experimental): dialog now carries an "experimental" label, learn-more link, and startup notification when enabled
* Windows: cached `where.exe` executable lookups per process for faster subprocess launches
* Default effort for Pro/Max subscribers on Opus 4.6 and Sonnet 4.6 is now `high` (was `medium`)

#### Major bug fixes

* Fixed Plain-CLI OAuth sessions dying with "Please run /login" when the access token expires mid-session — token is now refreshed reactively on 401
* Fixed `WebFetch` hanging on very large HTML pages by truncating input before HTML-to-markdown conversion
* Fixed a crash when a proxy returns HTTP 204 No Content
* Fixed `/login` having no effect when launched with `CLAUDE_CODE_OAUTH_TOKEN` env var and that token expires
* Fixed `NO_PROXY` not being respected for remote API requests when running under Bun
* Fixed SDK `reload_plugins` reconnecting all user MCP servers serially
* Fixed Bedrock application-inference-profile requests failing with 400 when backed by Opus 4.7 with thinking disabled
* Fixed subagents running a different model than the main agent incorrectly flagging file reads with a malware warning
* Fixed idle re-render loop when background tasks are present, reducing memory growth on Linux
* [VSCode] Fixed "Manage Plugins" panel breaking when multiple large marketplaces are configured
* Fixed Opus 4.7 sessions showing inflated `/context` percentages and autocompacting too early (was computing against 200K instead of 1M context window)

-----

## Claude Code changes

### New Documents

#### [debug-your-config](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/debug-your-config.md) [[Source](https://code.claude.com/docs/en/debug-your-config)]

New diagnostic guide for configuration issues. Covers using `/context`, `/memory`, `/skills`, `/agents`, `/hooks`, `/mcp`, `/permissions`, `/doctor`, and `/status` to inspect what loaded; how to check resolved settings scope precedence; debugging MCP servers and hooks; and a symptom-first lookup table for common configuration surprises (wrong hook matchers, standalone hook files, settings.json vs ~/.claude.json, etc.).

#### [agent-sdk/session-storage](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/session-storage.md) [[Source](https://code.claude.com/docs/en/agent-sdk/session-storage)]

New guide on persisting SDK sessions to external storage so any host can resume them. Covers the `SessionStore` interface (`append`, `load`, and optional `listSessions`, `delete`, `listSubkeys` methods), quick start with `InMemorySessionStore`, writing custom adapters, reference implementations for S3/Redis/Postgres, dual-write architecture notes, and a conformance test suite for validating adapters.

### Changed documents

#### [agent-sdk/observability](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/observability.md) [[Source](https://code.claude.com/docs/en/agent-sdk/observability)]

* `claude_code.hook` span now requires detailed beta tracing (`ENABLE_BETA_TRACING_DETAILED=1` and `BETA_TRACING_ENDPOINT`) in addition to the standard variables. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/observability.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces)]
* New section describing span hierarchy: subagent spans nest under the parent's `claude_code.tool` span when spawned via the Task tool. [[lines 103-104](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/observability.md?plain=1#L103-L104)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces)]
* New section on linking traces to your application via W3C trace context propagation (`TRACEPARENT`/`TRACESTATE`). [[lines 107-111](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/observability.md?plain=1#L107-L111)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#read-agent-traces)]
* `OTEL_LOG_RAW_API_BODIES` added to the sensitive-data opt-in table with description of inline (`=1`) and file (`file:<dir>`) modes. [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/observability.md?plain=1#L144)] [[Source](https://code.claude.com/docs/en/agent-sdk/observability#control-sensitive-data-in-exports)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `effort` field in `ClaudeAgentOptions` drops `xhigh` as a valid value; new `session_store` field added accepting a `SessionStore` adapter. [[lines 758-759](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/python.md?plain=1#L758-L759)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#claudeagentoptions)]
* `AgentDefinition` gains `disallowedTools`, `initialPrompt`, `maxTurns`, `background`, `effort`, and `permissionMode` fields; `model` now accepts a full model ID in addition to aliases. [[lines 969-980](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/python.md?plain=1#L969-L980)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#agentdefinition)]
* New note clarifying that `AgentDefinition` uses camelCase field names (matching the wire format), not Python snake_case. [[lines 993-994](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/python.md?plain=1#L993-L994)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#agentdefinition)]

#### [agent-sdk/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/sessions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/sessions)]

* Added note pointing to `SessionStore` adapter for resuming sessions across machines or serverless environments. [[line 188](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/sessions.md?plain=1#L188)] [[Source](https://code.claude.com/docs/en/agent-sdk/sessions#resume-by-id)]

#### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* `AgentDefinition` reference table gains `disallowedTools`, `maxTurns`, `background`, `effort`, `permissionMode`; `model` now accepts full model IDs; `memory` field no longer Python-only. [[lines 107-120](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L107-L120)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#agentdefinition-configuration)]
* Added note that Python SDK `AgentDefinition` uses camelCase field names. [[line 121](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L121)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#filesystem-based-definition-alternative)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `sessionStore` option added to the `Options` reference. [[line 350](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L350)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]
* `AgentDefinition` gains `initialPrompt`, `background`, `memory`, `effort`, `permissionMode`; `model` now accepts full model IDs. [[lines 454-468](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L454-L468)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#agentdefinition)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Troubleshoot section and "Check what loaded" section replaced with a single pointer to the new `debug-your-config.md` page. [[line 170](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/claude-directory.md?plain=1#L170)] [[Source](https://code.claude.com/docs/en/claude-directory#troubleshoot-configuration)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* New `WebFetch domain safety check` section explaining that the WebFetch tool sends each hostname to `api.anthropic.com` for blocklist checking before fetching; results cached for 5 minutes; runs regardless of provider; can be disabled with `skipWebFetchPreflight: true`. [[lines 79-82](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/data-usage.md?plain=1#L79-L82)] [[Source](https://code.claude.com/docs/en/data-usage#default-behaviors-by-api-provider)]
* New row added to the provider defaults table for the WebFetch domain safety check. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/data-usage.md?plain=1#L79)] [[Source](https://code.claude.com/docs/en/data-usage#default-behaviors-by-api-provider)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_SIMPLE_SYSTEM_PROMPT` env var: uses the minimal system prompt from `CLAUDE_CODE_SIMPLE` without disabling full tool set, hooks, MCP, or CLAUDE.md discovery. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/env-vars.md?plain=1#L125)] [[Source](https://code.claude.com/docs/en/env-vars)]
* `OTEL_LOG_RAW_API_BODIES` description updated to document the new `file:<dir>` mode. [[line 188](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/env-vars.md?plain=1#L188)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `UserPromptExpansion` hook event: fires when a slash command expands into a prompt before reaching Claude; matches on `command_name`; supports `decision: "block"` and `additionalContext`; covers the path that `PreToolUse` does not (direct `/skillname` invocations bypass `PreToolUse`). [[lines 818-868](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/hooks.md?plain=1#L818-L868)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit-decision-control)]
* Lifecycle diagram updated to include `UserPromptExpansion` and `PostToolUseFailure`. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/hooks.md?plain=1#L11)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* `CwdChanged` and `FileChanged` hook docs: removed the restriction that only `type: "command"` hooks are supported. [[lines 1679, 1714](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/hooks.md?plain=1#L1679)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* `UserPromptExpansion` added to the events reference table and matcher examples. [[line 409](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/hooks-guide.md?plain=1#L409)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Task list display changed: shows up to 5 tasks at a time (was 10). [[line 281](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/interactive-mode.md?plain=1#L281)] [[Source](https://code.claude.com/docs/en/interactive-mode#task-list)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Claude.ai connectors settings URL updated from `claude.ai/settings/connectors` to `claude.ai/customize/connectors`. [[line 1584](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/mcp.md?plain=1#L1584)] [[Source](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claude-ai)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New span hierarchy section with diagram showing `claude_code.interaction` → `llm_request` / `tool` → `tool.blocked_on_user` / `tool.execution` nesting. [[lines 120-130](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md?plain=1#L120-L130)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-hierarchy)]
* Full span attribute tables added for all span types: `claude_code.interaction`, `claude_code.llm_request`, `claude_code.tool`, `claude_code.tool.blocked_on_user`, `claude_code.tool.execution`, and `claude_code.hook`. [[lines 134-214](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md?plain=1#L134-L214)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]
* Seven new log events documented: `permission_mode_changed`, `auth`, `mcp_server_connection`, `internal_error`, `api_retries_exhausted`, `hook_execution_start`, `hook_execution_complete`, and `compaction`. [[lines 578-644](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md?plain=1#L578-L644)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)]
* `OTEL_LOG_RAW_API_BODIES` updated throughout: now supports `file:<dir>` mode that writes untruncated bodies to disk and emits a `body_ref` path pointer in events instead of inline `body`. [[lines 75-76](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md?plain=1#L75-L76)] [[Source](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)]
* `start_type` attribute added to session counter (`"fresh"`, `"resume"`, `"continue"`). [[line 373](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md?plain=1#L373)] [[Source](https://code.claude.com/docs/en/monitoring-usage#session-counter)]
* `query_source` and `speed` attributes added to `api_request` and `token` counters; `query_source` added to `api_request` and `api_error` events. [[lines 403-404](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md?plain=1#L403-L404)] [[Source](https://code.claude.com/docs/en/monitoring-usage#cost-counter)]
* `error` on `tool_result` event split into `error_type` (always emitted) and `error` (gated by `OTEL_LOG_TOOL_DETAILS=1`). [[lines 476-477](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md?plain=1#L476-L477)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* Plugin-installed and skill-activated events: third-party marketplace `plugin.name`, `plugin.version`, `marketplace.name`, and `skill.name` are now redacted unless `OTEL_LOG_TOOL_DETAILS=1`. [[lines 649-676](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/monitoring-usage.md?plain=1#L649-L676)] [[Source](https://code.claude.com/docs/en/monitoring-usage#plugin-installed-event)]

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* `downloads.claude.ai` is now the primary download host; `storage.googleapis.com` documented as legacy used by older clients. [[lines 97-99](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/network-config.md?plain=1#L97-L99)] [[Source](https://code.claude.com/docs/en/network-config#network-access-requirements)]
* Added note that WebFetch calls `api.anthropic.com` for its domain safety check even on Bedrock/Vertex/Foundry deployments. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/network-config.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/network-config#network-access-requirements)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarification that `rm`/`rmdir` targeting `/`, the home directory, or other critical system paths still trigger a permission prompt even in auto-allow sandboxed mode. [[line 251](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/permissions.md?plain=1#L251)] [[Source](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)]
* Auto mode classifier section updated: recommends CLAUDE.md for project-level behavioral rules; `autoMode` settings block is for cross-project infrastructure rules. [[lines 286-288](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/permissions.md?plain=1#L286-L288)] [[Source](https://code.claude.com/docs/en/permissions#configure-the-auto-mode-classifier)]

#### [plugin-dependencies](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/plugin-dependencies.md) [[Source](https://code.claude.com/docs/en/plugin-dependencies)]

* Auto-reinstall behavior documented: if a dependency goes missing, `/reload-plugins` and background auto-update reinstall it automatically (if the marketplace is configured). [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/plugin-dependencies.md?plain=1#L7)] [[Source](https://code.claude.com/docs/en/plugin-dependencies)]
* New section on cross-marketplace dependencies: explains `allowCrossMarketplaceDependenciesOn` field in `marketplace.json` that must be set to allow auto-install of dependencies from another marketplace. [[lines 39-62](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/plugin-dependencies.md?plain=1#L39-L62)] [[Source](https://code.claude.com/docs/en/plugin-dependencies#declare-a-dependency-with-a-version-constraint)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* New `allowCrossMarketplaceDependenciesOn` array field documented in the optional marketplace.json fields table. [[line 180](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/plugin-marketplaces.md?plain=1#L180)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#optional-fields)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `UserPromptExpansion` hook event added to the plugin hooks event table. [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/plugins-reference.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]
* `userConfig` schema expanded: fields now require `type` and `title`, and gain optional `required`, `default`, `multiple`, `min`/`max` properties; the reference table is fully documented. [[lines 396-407](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/plugins-reference.md?plain=1#L396-L407)] [[Source](https://code.claude.com/docs/en/plugins-reference#user-configuration)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Auto-allow mode description clarified: `rm`/`rmdir` targeting critical paths still trigger a permission prompt even when sandboxed. [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/sandboxing.md?plain=1#L83)] [[Source](https://code.claude.com/docs/en/sandboxing#enable-sandboxing)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `skipWebFetchPreflight` setting documented (skips the hostname safety check before WebFetch fetches a URL). [[line 198](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/settings.md?plain=1#L198)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* macOS MDM: plist format clarified — top-level keys mirror `managed-settings.json` with nested settings as dictionaries and arrays as plist arrays. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/settings.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* `/status` now shows `Enterprise managed settings (HKCU)` for Windows user-level registry policies. [[line 454](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/settings.md?plain=1#L454)] [[Source](https://code.claude.com/docs/en/settings#verify-active-settings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New `arguments` frontmatter field for named positional arguments; named substitution via `$name` placeholders documented. [[lines 176-177](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/skills.md?plain=1#L176-L177)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]
* `model` frontmatter field clarified: override applies only for the current turn and is not saved to settings. [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/skills.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]
* `disable-model-invocation: true` now also prevents the skill from being preloaded into subagents. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/skills.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Skills with `disable-model-invocation: true` cannot be preloaded into subagents; missing or disabled skills are skipped with a debug log warning. [[line 361](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/sub-agents.md?plain=1#L361)] [[Source](https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents)]
* Frontmatter hooks now also fire when the agent runs as the main session via `--agent`, not only as a subagent. [[line 475](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/sub-agents.md?plain=1#L475)] [[Source](https://code.claude.com/docs/en/sub-agents#hooks-in-subagent-frontmatter)]
* `Stop` hooks in frontmatter are only converted to `SubagentStop` when the agent is invoked as a subagent (not in main-session mode). [[line 505](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/sub-agents.md?plain=1#L505)] [[Source](https://code.claude.com/docs/en/sub-agents#hooks-in-subagent-frontmatter)]

#### [terminal-config](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/terminal-config.md) [[Source](https://code.claude.com/docs/en/terminal-config)]

* `/terminal-setup` now also sets `terminal.integrated.mouseWheelScrollSensitivity` in VS Code, Cursor, and Windsurf for smoother fullscreen scrolling; existing bindings are left in place rather than overwritten. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/terminal-config.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/terminal-config#enter-multiline-prompts)]

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* Download host updated from `storage.googleapis.com` to `downloads.claude.ai` throughout installation troubleshooting steps. [[lines 34-35](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/claude-code/troubleshooting.md?plain=1#L34-L35)] [[Source](https://code.claude.com/docs/en/troubleshooting#check-network-connectivity)]

-----

## API changes

### Changed documents

#### [build-with-claude/embeddings](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/api/build-with-claude/embeddings.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/embeddings)]

* New Voyage 4 embedding model generation documented: `voyage-4-large`, `voyage-4`, `voyage-4-lite` (optimized for latency/cost), and `voyage-4-nano` (open-weight Apache 2.0 on Hugging Face), all with 32K context and flexible embedding dimensions. [[lines 20-30](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/api/build-with-claude/embeddings.md?plain=1#L20-L30)] [[Source](https://platform.claude.com/docs/en/build-with-claude/embeddings)]
* New `voyage-multimodal-3.5` documented with video support (first production-grade video embedding model) and flexible embedding dimensions; previous `voyage-multimodal-3` retained as previous generation. [[lines 47-48](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/api/build-with-claude/embeddings.md?plain=1#L47-L48)] [[Source](https://platform.claude.com/docs/en/build-with-claude/embeddings)]
* Code examples updated to use `voyage-4` as the recommended model. [[lines 84-184](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/api/build-with-claude/embeddings.md?plain=1#L84-L184)] [[Source](https://platform.claude.com/docs/en/build-with-claude/embeddings)]

#### [managed-agents/events-and-streaming](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/api/managed-agents/events-and-streaming.md) [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]

* New "Resuming an idle session" section: explains that session containers are checkpointed when idle (filesystem, packages, and files preserved); checkpoints retained for 30 days after last activity; resume by sending a `user.message` event as usual. [[lines 177-205](https://github.com/gpambrozio/ClaudeDocs/blob/76254a0/docs-md/api/managed-agents/events-and-streaming.md?plain=1#L177-L205)] [[Source](https://platform.claude.com/docs/en/managed-agents/events-and-streaming)]
