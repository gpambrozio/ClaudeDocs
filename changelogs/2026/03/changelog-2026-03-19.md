# [Claude docs changes for March 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b966a23) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b966a23)]

## Executive Summary
- New `StopFailure` hook event added to fire when turns end due to API errors (rate limits, auth failures, etc.), with full schema and matcher support
- Models API now returns `capabilities`, `max_input_tokens`, and `max_tokens` fields for programmatic feature discovery
- Files API storage limit increased from 100 GB to 500 GB per organization
- New `ANTHROPIC_CUSTOM_MODEL_OPTION` env vars allow adding custom model entries to the `/model` picker for gateway deployments
- Sandbox path prefix semantics clarified: `/path` now means absolute (not settings-relative), `./path` for relative paths

## New Claude Code versions

### [2.1.79](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/versions/2.1.79.md)

#### New features

* Added `--console` flag to `claude auth login` for Anthropic Console (API billing) authentication instead of a Claude subscription
* Added "Show turn duration" toggle to the `/config` menu
* `CLAUDE_CODE_PLUGIN_SEED_DIR` now supports multiple seed directories separated by the platform path delimiter (`:` on Unix, `;` on Windows)
* [VSCode] Added `/remote-control` command to the command menu to bridge a session to claude.ai/code for remote access from a browser or phone
* [VSCode] Session tabs now get AI-generated titles based on your first message

#### Existing feature improvements

* Improved startup memory usage by ~18MB across all scenarios
* Improved non-streaming API fallback with a 2-minute per-attempt timeout, preventing sessions from hanging indefinitely

#### Major bug fixes

* Fixed `claude -p` hanging when spawned as a subprocess without explicit stdin (e.g. Python `subprocess.run`)
* Fixed Ctrl+C not working in `-p` (print) mode
* Fixed `/btw` returning the main agent's output instead of answering the side question when triggered during streaming
* Fixed enterprise users being unable to retry on rate limit (429) errors
* Fixed `SessionEnd` hooks not firing when using interactive `/resume` to switch sessions
* [VSCode] Fixed the thinking pill showing "Thinking" instead of "Thought for Ns" after a response completes

-----

## Claude Code changes

### Changed documents

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `--console` flag to `claude auth login` to sign in with Anthropic Console for API usage billing instead of a Claude subscription. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/cli-reference.md?plain=1#L15)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Three new environment variables added for custom model picker entries: `ANTHROPIC_CUSTOM_MODEL_OPTION` (model ID), `ANTHROPIC_CUSTOM_MODEL_OPTION_NAME` (display name), and `ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION` (description). [[lines 45-47](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/env-vars.md?plain=1#L45-L47)] [[Source](https://code.claude.com/docs/en/env-vars)]
* Updated `CLAUDE_CODE_PLUGIN_SEED_DIR` description to reflect support for multiple directories separated by `:` (Unix) or `;` (Windows). [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/env-vars.md?plain=1#L56)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added new `StopFailure` hook event that fires when a turn ends due to an API error. Output and exit code are ignored. [[line 116](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks-guide.md?plain=1#L116)] [[Source](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)]
* Added matcher support for `StopFailure` (error type), `InstructionsLoaded` (load reason), `Elicitation`, and `ElicitationResult` (MCP server name). [[lines 124-127](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks-guide.md?plain=1#L124-L127)] [[Source](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)]
* Clarified that `Stop` hooks fire on API errors via `StopFailure` instead. [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks-guide.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added new `StopFailure` hook event to the events table. [[line 157](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks.md?plain=1#L157)] [[Source](https://code.claude.com/docs/en/hooks#configuration)]
* Updated matcher table: `StopFailure` supports error type matchers (`rate_limit`, `authentication_failed`, `billing_error`, etc.); `InstructionsLoaded` now supports load reason matchers (`session_start`, `nested_traversal`, etc.); `Elicitation`/`ElicitationResult` support MCP server name matchers. [[lines 166-170](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks.md?plain=1#L166-L170)] [[Source](https://code.claude.com/docs/en/hooks#hook-locations)]
* `InstructionsLoaded` now supports matchers (previously listed as no-matcher). [[line 230](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks.md?plain=1#L230)] [[Source](https://code.claude.com/docs/en/hooks#match-mcp-tools)]
* Full `StopFailure` hook event documented with input schema including `error`, `error_details`, and `last_assistant_message` fields. [[lines 272-304](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/hooks.md?plain=1#L272-L304)] [[Source](https://code.claude.com/docs/en/hooks#match-mcp-tools)]
* Clarified that `permission_mode` is not present in all hook event JSON — only events that actually receive it include it. `SessionStart`, `InstructionsLoaded`, `Notification`, `SubagentStart`, `PreCompact`, `PostCompact`, `SessionEnd`, and `ConfigChange` no longer show `permission_mode` in their example JSON.
* Updated hooks lifecycle diagram to include `StopFailure`.

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Added `/remote-control` to the VS Code command menu description. [[line 376](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/ide-integrations.md?plain=1#L376)] [[Source](https://code.claude.com/docs/en/ide-integrations#the-built-in-ide-mcp-server)]
* New sessions now receive AI-generated titles based on your first message. [[line 385](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/ide-integrations.md?plain=1#L385)] [[Source](https://code.claude.com/docs/en/ide-integrations#fix-common-issues)]
* Added new section documenting the built-in IDE MCP server: transport, authentication (random token written to `~/.claude/ide/`), and the two model-visible tools (`mcp__ide__getDiagnostics` and `mcp__ide__executeCode`). [[lines 393-408](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/ide-integrations.md?plain=1#L393-L408)] [[Source](https://code.claude.com/docs/en/ide-integrations#spark-icon-not-visible)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New MCP server added: ICD-10 Codes (access ICD-10-CM and ICD-10-PCS code sets).

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* New section "Add a custom model option" documenting how to use `ANTHROPIC_CUSTOM_MODEL_OPTION`, `ANTHROPIC_CUSTOM_MODEL_OPTION_NAME`, and `ANTHROPIC_CUSTOM_MODEL_OPTION_DESCRIPTION` to add a non-standard model ID to the `/model` picker for gateway deployments. [[lines 181-199](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/model-config.md?plain=1#L181-L199)] [[Source](https://code.claude.com/docs/en/model-config#extended-context)]

#### [plugin-marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Added documentation for layering multiple `CLAUDE_CODE_PLUGIN_SEED_DIR` directories: separate paths with `:` on Unix or `;` on Windows; first seed containing a given plugin wins. [[line 694](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/plugin-marketplaces.md?plain=1#L694)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#pre-populate-plugins-for-containers)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* Replaced the bullet-list of available hook events with a comprehensive table matching the full hooks reference, including new events like `StopFailure`, `InstructionsLoaded`, `ConfigChange`, `WorktreeCreate/Remove`, `Elicitation`/`ElicitationResult`. [[lines 49-73](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/plugins-reference.md?plain=1#L49-L73)] [[Source](https://code.claude.com/docs/en/plugins-reference#agents)]
* Added `http` as a supported hook type alongside `command`, `prompt`, and `agent`. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/plugins-reference.md?plain=1#L80)] [[Source](https://code.claude.com/docs/en/plugins-reference#hooks)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Clarified that on Team and Enterprise plans Remote Control is off by default until an admin enables the toggle specifically. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/remote-control.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/remote-control#connection-and-security)]
* Session title priority order now documented explicitly (name arg → /rename → last message → first prompt). [[lines 149-156](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/remote-control.md?plain=1#L149-L156)] [[Source](https://code.claude.com/docs/en/remote-control#”remote-control-is-not-yet-enabled-for-your-account”)]
* Added three new troubleshooting sections: "Remote Control is not yet enabled for your account" (env var conflicts), "Remote Control is disabled by your organization's policy" (API key vs OAuth, admin toggle, compliance restrictions), and "Remote credentials fetch failed". [[lines 165-184](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/remote-control.md?plain=1#L165-L184)] [[Source](https://code.claude.com/docs/en/remote-control#”remote-control-is-disabled-by-your-organization’s-policy”)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* Corrected sandbox path prefix table: single `/` now means absolute path (not settings-relative); `./` or no prefix means relative to project root (for project settings) or `~/.claude` (for user settings). The old `//path` prefix still works for backwards compatibility. [[lines 218-226](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/sandboxing.md?plain=1#L218-L226)] [[Source](https://code.claude.com/docs/en/sandboxing#transparent-operation)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated `showTurnDuration` description: clarified it now appears in `/config` as **Show turn duration** (previously said "Edit `~/.claude.json` directly to change"). [[line 239](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/settings.md?plain=1#L239)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]
* Sandbox path prefix table and examples updated to reflect `/path` = absolute, `./path` = relative (matching sandboxing.md fix). [[lines 259-265](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/settings.md?plain=1#L259-L265)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Changed recommended persistent memory scope from `user` to `project` — project scope is shareable via version control. Use `user` for cross-project knowledge. [[line 308](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/sub-agents.md?plain=1#L308)] [[Source](https://code.claude.com/docs/en/sub-agents#restrict-which-subagents-can-be-spawned)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Same changes as ide-integrations.md (this file is identical): `/remote-control` in command menu, AI-generated session titles, and new built-in IDE MCP server section.

-----

## API changes

### Changed documents

#### [about-claude/models/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/about-claude/models/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

* Added note that model capabilities and token limits can be queried programmatically via the Models API, which now returns `max_input_tokens`, `max_tokens`, and a `capabilities` object. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/about-claude/models/overview.md?plain=1#L39)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP server added: Indeed (search for jobs on Indeed).

#### [api/api/messages/create](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

* `metadata.user_id` maximum length increased from 256 to 512 characters.
* Added `thinking.display` parameter to `ThinkingConfigEnabled` and `ThinkingConfigAdaptive` — accepts `"summarized"` (default) or `"omitted"` to redact thinking content while preserving the signature for multi-turn continuity.

#### [api/api/models/list](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/api/models/list.md) [[Source](https://platform.claude.com/docs/en/api/models/list)] (and all SDK variants)

* Models API response now includes `capabilities` object (batch, citations, code_execution, context_management, effort, image_input, and more), `max_input_tokens`, and `max_tokens` for each model. All SDK variants (Python, TypeScript, Go, Java, C#, Ruby, and beta endpoints) updated accordingly.

#### [build-with-claude/compaction](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Fixed code example for `pause_after_compaction`: now correctly preserves the prior exchange plus current user message (3 messages total) instead of only 2. [[lines 1166-1178](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/build-with-claude/compaction.md?plain=1#L1166-L1178)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Files API total storage limit per organization increased from 100 GB to 500 GB. [[line 1204](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/build-with-claude/files.md?plain=1#L1204)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [build-with-claude/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Added note about querying model capabilities programmatically via the Models API. [[line 1234](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/build-with-claude/overview.md?plain=1#L1234)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added March 18, 2026 entry: Models API now returns `max_input_tokens`, `max_tokens`, and a `capabilities` object for each model. [[lines 1248-1250](https://github.com/gpambrozio/ClaudeDocs/blob/b966a23/docs-md/api/release-notes/overview.md?plain=1#L1248-L1250)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
