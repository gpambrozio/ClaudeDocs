# [Claude docs changes for June 6th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b6e5ad2688dd5a79427a8287e32907c880622297) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b6e5ad2688dd5a79427a8287e32907c880622297)]

## Executive Summary
- New `fallbackModel` setting in v2.1.166 lets you configure up to three fallback models tried in order when the primary model is overloaded or unavailable
- New `requiredMinimumVersion`/`requiredMaximumVersion` managed settings allow organizations to block Claude Code from starting if the running version is outside an approved range — stronger than the existing `minimumVersion` floor
- Stop and SubagentStop hooks now support `additionalContext` for non-error feedback that continues the conversation without triggering a hook error notification
- Claude Opus 4.1 is now marked as deprecated across API documentation; Claude Opus 4 is marked as retired on Amazon Bedrock
- A new `api_refusal` telemetry event lets operators track API refusal frequency separately from errors

## New Claude Code versions

### [2.1.166](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/versions/2.1.166.md)

#### New features

* Added `fallbackModel` setting to configure up to three fallback models tried in order when the primary model is overloaded or unavailable; `--fallback-model` now also applies to interactive sessions
* Added glob pattern support in deny rule tool-name position (`"*"` denies all tools); allow rules reject non-MCP globs, and unknown tool names in deny rules warn at startup
* Hardened cross-session messaging: messages relayed via `SendMessage` from other Claude sessions no longer carry user authority — receivers refuse relayed permission requests, and auto mode blocks them
* `MAX_THINKING_TOKENS=0`, `--thinking disabled`, and the per-model thinking toggle now disable thinking on models that think by default via the Claude API (3P providers unchanged)
* `claude agents`: typing a URL into the list now filters to the session whose first prompt contained it

#### Existing feature improvements

* Claude Code now retries a turn once on the fallback model when the API rejects an unexpected non-retryable error; auth, rate-limit, request-size, and transport errors still surface immediately
* `claude update` now announces the target version before downloading instead of going silent

#### Major bug fixes

* Fixed a recurring "image could not be processed" error and extra token usage when an unprocessable image was sent in a session
* Fixed remote sessions becoming permanently stuck when a brief backend disruption occurred during worker registration at startup
* Fixed flickering in JetBrains IDE terminals (IntelliJ, PyCharm, WebStorm, etc.) on 2026.1+ by enabling synchronized output
* Fixed Shift+non-ASCII characters (e.g. Shift+ä → Ä) being dropped in terminals using the Kitty keyboard protocol (WezTerm, Ghostty, kitty)
* Fixed PowerShell command validation occasionally hanging far past its time budget on Windows when a killed process's children held its output pipes
* Fixed orphaned `claude --bg-pty-host` processes spinning at 100% CPU after the daemon dies while connected on macOS
* Fixed managed settings with an invalid entry silently disabling enforcement of their remaining valid policies
* Fixed managed-settings `allowedMcpServers`/`deniedMcpServers` predicates not matching when they use `${VAR}` references
* Fixed background agent sessions that entered a git worktree crash-looping with "No conversation found" when reopened from `claude agents`
* Fixed duplicated thinking text in the Ctrl+O transcript view while streaming

### [2.1.167](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/versions/2.1.167.md)

#### Major bug fixes

* Bug fixes and reliability improvements

-----

## Claude Code changes

### Changed documents

#### [Admin setup](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* New `requiredMinimumVersion`/`requiredMaximumVersion` managed settings added to the capabilities table — blocks Claude Code from starting when outside the approved version range, which is stronger than `minimumVersion` (which only prevents downgrades). [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/admin-setup.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Clarified that model aliases resolve to Claude Code's built-in default for Bedrock (which can lag the newest release), not simply "the latest version". [[line 188](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/amazon-bedrock.md?plain=1#L188)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)]

#### [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Added a new enterprise/sales call-to-action section at the top of the page. [[lines 4-6](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L4-L6)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]
* Clarified that the `opus` alias resolves to Opus 4.7 by default on Claude Platform on AWS.

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/plugin` now documented with subcommand support (`list`, `install`, `enable`, `disable`). [[line 234](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/commands.md?plain=1#L234)] [[Source](https://code.claude.com/docs/en/commands#see-also)]
* `/reload-plugins` now supports `--force` flag; without it, the command warns and holds when the reload would invalidate the prompt cache. [[line 242](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/commands.md?plain=1#L242)] [[Source](https://code.claude.com/docs/en/commands#see-also)]

#### [Discover plugins](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* New `/plugin list` command documented for listing installed plugins without opening the menu; supports `--enabled` and `--disabled` filters. [[lines 268-273](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/discover-plugins.md?plain=1#L268-L273)] [[Source](https://code.claude.com/docs/en/discover-plugins#manage-installed-plugins)]

#### [Environment variables](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_FORK_SUBAGENT` now accepts `0` to explicitly disable fork subagents, overriding any server-side staged rollout. [[line 286](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/env-vars.md?plain=1#L286)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_SYNC_SKILLS_INSTALL_TIMEOUT_MS` env var added — bounds the mid-session skills resync triggered when the host requests a skill reload. [[line 303](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/env-vars.md?plain=1#L303)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_TMPDIR` clarified: the short fallback `$TMPDIR` for long paths only applies to sandboxed Bash; unsandboxed Bash inherits your shell's `$TMPDIR` unchanged. [[line 309](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/env-vars.md?plain=1#L309)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [Headless mode](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* New "Background tasks at exit" section: background Bash tasks started during a `claude -p` run are terminated ~5 seconds after Claude returns its final result and stdin closes. [[lines 48-51](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/headless.md?plain=1#L48-L51)] [[Source](https://code.claude.com/docs/en/headless#start-faster-with-bare-mode)]

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Expanded `if` field documentation with a detailed matching table showing exactly when hooks fire for `$()`, backtick substitutions, and compound commands. [[lines 20-30](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/hooks-guide.md?plain=1#L20-L30)] [[Source](https://code.claude.com/docs/en/hooks-guide#set-up-your-first-hook)]
* Clarified that the `if` filter fails open (hook runs) when the Bash command cannot be parsed, and that the permission system should be used for hard allow/deny rather than hooks.

#### [Hooks reference](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Expanded Bash `if` matching table with behavior for leading `VAR=value` assignments, `$()`, and backtick patterns. [[lines 52-60](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/hooks.md?plain=1#L52-L60)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]
* Stop and SubagentStop hooks now support `hookSpecificOutput.additionalContext` as a non-error way to give Claude feedback that keeps the conversation going without showing a hook error notification. [[lines 103-120](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/hooks.md?plain=1#L103-L120)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]
* `prompt` hook field now supports backslash-escaping `$` to include literal dollar signs in prompts. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/hooks.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New `c` key in the `/btw` overlay copies the answer to clipboard as raw Markdown (avoids hard-wrapped terminal rendering from mouse selection). [[line 133](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/interactive-mode.md?plain=1#L133)] [[Source](https://code.claude.com/docs/en/interactive-mode#navigation-normal-mode)]

#### [Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Clarified that model aliases resolve to Claude Code's built-in default for Foundry and that Foundry has no startup model check — requests fail if the default model is unavailable. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/microsoft-foundry.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#additional-resources)]

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `claude_code.api_refusal` telemetry event for tracking `stop_reason: "refusal"` responses, which arrive on a successful stream rather than as HTTP errors. [[lines 183-195](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/monitoring-usage.md?plain=1#L183-L195)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]
* MCP server connection events now include `is_plugin`, `plugin_id_hash`, and `plugin.name` attributes, letting operators identify plugin-provided MCP servers in logs without exposing third-party plugin names. [[lines 201-203](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/monitoring-usage.md?plain=1#L201-L203)] [[Source](https://code.claude.com/docs/en/monitoring-usage#span-attributes)]

#### [Plugins reference](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Documented that `/plugin list` is available within interactive sessions, with `--enabled`/`--disabled` filters and `ls` as a shorthand. [[line 232](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/plugins-reference.md?plain=1#L232)] [[Source](https://code.claude.com/docs/en/plugins-reference#lsp-servers)]

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Documented that as of v2.1.163, `/reload-plugins` warns and holds instead of applying a reload that would trigger a full cache re-read; pass `--force` to proceed anyway. [[line 246](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/prompt-caching.md?plain=1#L246)] [[Source](https://code.claude.com/docs/en/prompt-caching#related-resources)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `requiredMinimumVersion` and `requiredMaximumVersion` managed settings documented — Claude Code exits at startup if the running version is outside the approved range. [[lines 280-281](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/settings.md?plain=1#L280-L281)] [[Source](https://code.claude.com/docs/en/settings#permission-settings)]
* Git commit attribution format updated: the `🤖 Generated with Claude Code` line has been removed; only the `Co-Authored-By` trailer remains. [[lines 289-293](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/settings.md?plain=1#L289-L293)] [[Source](https://code.claude.com/docs/en/settings#permission-rule-syntax)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Documented the distinction between `minimumVersion` (constrains updates only) and the new `requiredMinimumVersion`/`requiredMaximumVersion` (blocks startup entirely). [[line 307](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/setup.md?plain=1#L307)] [[Source](https://code.claude.com/docs/en/setup#install-with-linux-package-managers)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Documented backslash escaping for `$` in skill content — `\$1.00` renders as `$1.00` without triggering argument substitution. [[line 319](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/skills.md?plain=1#L319)] [[Source](https://code.claude.com/docs/en/skills#pre-approve-tools-for-a-skill)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `CLAUDE_CODE_FORK_SUBAGENT=0` now explicitly disables fork mode everywhere, including any server-side staged rollout. [[line 341](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/sub-agents.md?plain=1#L341)] [[Source](https://code.claude.com/docs/en/sub-agents#scope-mcp-servers-to-a-subagent)]
* Fork mode may now be enabled by default in interactive sessions as part of a staged rollout. [[line 341](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/sub-agents.md?plain=1#L341)] [[Source](https://code.claude.com/docs/en/sub-agents#scope-mcp-servers-to-a-subagent)]

#### [Subagents in the SDK](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* New `initialPrompt` parameter added to `AgentDefinition` — auto-submitted as the first user turn when the agent runs as the main thread agent. [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#creating-subagents)]
* Resuming subagents section rewritten: the `agentId` is now found in the Agent tool result text block; built-in `Explore` and `Plan` agents are one-shot and omit the trailer. [[lines 70-83](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L70-L83)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#programmatic-definition-recommended)]
* Resume example replaced: now shows Python (custom `endpoint-finder` agent) instead of TypeScript. [[lines 85-176](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L85-L176)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#programmatic-definition-recommended)]

-----

## API changes

### Changed documents

#### [Adaptive thinking](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* No significant content changes (email link obfuscation updated).

#### [Batch processing](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Claude Opus 4.1 marked as deprecated in the pricing table. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/batch-processing.md?plain=1#L91)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

#### [Claude in Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* Added a lifecycle terms note linking to the model deprecations page. [[line 248](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L248)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]
* Claude Opus 4.1 marked as Deprecated with retirement date of August 5, 2026. [[line 258](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L258)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

#### [Claude on Amazon Bedrock (legacy)](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

* Lifecycle dates note updated: specific Bedrock retirement dates removed; now directs users to Amazon Bedrock's model lifecycle page for current dates. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md?plain=1#L78)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]
* Claude Opus 4.1 marked as Deprecated; Claude Opus 4 changed to Retired (was Deprecated with May 31, 2026 date) with all regional availability removed. [[lines 85-93](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md?plain=1#L85-L93)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

#### [Claude on Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Vertex AI documentation links updated to new URL (`docs.cloud.google.com`). [[lines 12, 54, 274](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L12)]
* Lifecycle dates note updated: specific Vertex AI retirement dates removed; now directs users to Google Cloud's documentation for current dates. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]
* Claude Opus 4.1 marked as Deprecated. [[line 73](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L73)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [Code execution tool](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Claude Opus 4.1 marked as deprecated in the model availability table. [[line 28](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L28)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Computer use tool](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Claude Opus 4.1 marked as deprecated in the beta header compatibility table. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L10)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

#### [Context editing](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* Claude Opus 4.1 marked as deprecated in the thinking block preservation table. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/context-editing.md?plain=1#L42)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Anthropic sales contact link changed from obfuscated email to `mailto:sales@anthropic.com`. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L101)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Claude Opus 4.1 marked as deprecated in multiple sections covering interleaved thinking and thinking block preservation. [[lines 391, 601](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L391)]

#### [Handle streaming refusals](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md) [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

* Claude Opus 4.1 marked as deprecated. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/handle-streaming-refusals)]

#### [Handling stop reasons](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

* Claude Opus 4.1 marked as deprecated in refusal stop reason guidance. [[line 297](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L297)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

#### [Multilingual support](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/multilingual-support.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)]

* Column header corrected from "Claude Opus 4.11" to "Claude Opus 4.1 (deprecated)1" in the benchmark table. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/multilingual-support.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)]

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Claude Opus 4.1 marked as deprecated in pricing and minimum cacheable prompt length tables. [[lines 77, 252](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L77)]

#### [Search results](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/search-results.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

* Claude Opus 4.1 marked as deprecated in the model availability list. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/build-with-claude/search-results.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

#### [Tool use overview](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Claude Opus 4.1 marked as deprecated in the tool use token overhead table. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/b6e5ad2688dd5a79427a8287e32907c880622297/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L86)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]
