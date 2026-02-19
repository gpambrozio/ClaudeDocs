# [Claude docs changes for February 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/8a16334468bc5741d69ab96b83710bf034f17ee0) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/8a16334468bc5741d69ab96b83710bf034f17ee0)]

## Executive Summary
- Claude Code 2.1.47 is a massive release with dozens of improvements: performance boosts (~500ms faster startup), major memory usage reductions for long sessions, a new `last_assistant_message` field in Stop/SubagentStop hooks, a new `chat:newline` keybinding action, and `ctrl+f` to kill background agents (replacing double-ESC)
- Delegate mode has been removed from Claude Code — the `delegate` permission mode is gone from all documentation, and agent team navigation simplified to Shift+Down only (with wrapping)
- OTPM rate limits now evaluated in real-time based on actual tokens generated (not estimated from `max_tokens`), so setting a high `max_tokens` no longer penalizes rate limits
- Compaction is now ZDR-eligible and supports Claude Sonnet 4.6 in addition to Opus 4.6
- Web search/fetch dynamic filtering has graduated from beta — the `code-execution-web-tools-2026-02-09` beta header is no longer required

## New Claude Code versions

### [2.1.46](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/versions/2.1.46.md)

#### New features

* Added support for using claude.ai MCP connectors in Claude Code

#### Major bug fixes

* Fixed orphaned Claude Code processes after terminal disconnect on macOS

---

### [2.1.47](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/versions/2.1.47.md)

#### New features

* Added `last_assistant_message` field to Stop and SubagentStop hook inputs, providing the final assistant response text so hooks can access it without parsing transcript files
* Added `chat:newline` keybinding action for configurable multi-line input
* Added `added_dirs` to the statusline JSON `workspace` section, exposing directories added via `/add-dir` to external scripts
* Use `ctrl+f` to kill all background agents (replaces double-pressing ESC). Background agents now continue running when you press ESC to cancel the main thread, giving more control over agent lifecycle
* `spinnerTipsOverride` setting added: override spinner tips with custom strings, with option to exclude default tips

#### Existing feature improvements

* Improved VS Code plan preview: auto-updates as Claude iterates, enables commenting only when the plan is ready for review, and keeps the preview open when rejecting so Claude can revise
* Improved startup performance by deferring SessionStart hook execution, reducing time-to-interactive by ~500ms
* Improved performance of `@` file mentions — file suggestions now appear faster by pre-warming the index on startup and using session-based caching with background refresh
* Improved memory usage in long-running sessions by releasing API stream buffers, agent context, and skill state after use
* Improved memory usage by trimming agent task message history after tasks complete and eliminating O(n²) message accumulation in agent progress updates
* Simplified teammate navigation to use only Shift+Down (with wrapping back to lead) instead of both Shift+Up and Shift+Down
* Increased initial session count in resume picker from 10 to 50 for faster session discovery
* Moved config backup files from home directory root to `~/.claude/backups/`
* The `/rename` command now updates the terminal tab title by default
* Search patterns in collapsed tool results are now displayed in quotes for clarity

#### Major bug fixes

* Fixed compaction failing when conversation contains many PDF documents
* Fixed plan mode being lost after context compaction, causing the model to switch from planning to implementation mode
* Fixed background agent results returning raw transcript data instead of the agent's final answer
* Fixed custom agent `model` field in `.claude/agents/*.md` being ignored when spawning team teammates
* Fixed bash permission classifier to validate that returned match descriptions correspond to actual input rules, preventing hallucinated descriptions from incorrectly granting permissions
* Fixed custom session titles set via `/rename` being lost after resuming a conversation or context compaction
* Fixed `/resume` silently dropping sessions when the first message exceeds 16KB or uses array-format content
* Fixed hooks (PreToolUse, PostToolUse) silently failing to execute on Windows (now uses Git Bash instead of cmd.exe)
* Fixed Edit tool silently corrupting Unicode curly quotes when making edits
* Fixed `alwaysThinkingEnabled: true` in settings.json not enabling thinking mode on Bedrock and Vertex providers
* Fixed shell commands permanently failing after a command deletes its own working directory
* Fixed custom agents and skills not being discovered when running from a git worktree
* Fixed image pasting not working on WSL2 systems where Windows copies images as BMP format
* Fixed CJK wide characters causing misaligned timestamps and layout elements in the TUI
* Fixed LSP `findReferences` and other location-based operations returning results from gitignored files
* Fixed "Always allow" on multiline bash commands creating invalid permission patterns that corrupt settings
* Fixed inline code spans in markdown being incorrectly parsed as bash commands

-----

## Claude Code changes

### Changed documents

#### [Agent Teams](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Navigation simplified: Use `Shift+Down` to cycle through teammates (with wrapping back to the lead) instead of `Shift+Up/Down`. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/agent-teams.md?plain=1#L81)] [[Source](https://code.claude.com/docs/en/agent-teams#start-your-first-agent-team)]
* Delegate mode section removed — the "Use delegate mode" subsection is gone from the documentation

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* New "Pin model versions" section added (step 4) with specific environment variable instructions and example values for pinning Bedrock model IDs to prevent breakage when Anthropic releases new models. [[line 161](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/amazon-bedrock.md?plain=1#L161)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)]

#### [Common Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Delegate mode mention removed from the Plan Mode `Shift+Tab` cycling description

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* `delegate` mode removed from the permission modes available only in the CLI; comparison table updated accordingly

#### [Google Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* New "Pin model versions" section added (step 5) with specific environment variable instructions for Vertex AI model IDs. [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/google-vertex-ai.md?plain=1#L85)] [[Source](https://code.claude.com/docs/en/google-vertex-ai#4-configure-claude-code)]
* Duplicate warning about Vertex AI regional/global endpoint support consolidated into a single clearer note

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* SubagentStop hooks now receive a `last_assistant_message` field containing the subagent's final response text, eliminating the need to parse transcript files. [[line 1227](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/hooks.md?plain=1#L1227)] [[Source](https://code.claude.com/docs/en/hooks#subagentstop)]
* Stop hooks now receive a `last_assistant_message` field containing Claude's final response text. [[line 1259](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/hooks.md?plain=1#L1259)] [[Source](https://code.claude.com/docs/en/hooks#stop)]

#### [How Claude Code Works](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Delegate mode removed from the list of permission modes in the `Shift+Tab` cycle

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Shift+Tab` description updated — delegate mode no longer listed as part of the permission mode cycle

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Several MCP connectors reordered in the listing
* New MCP connectors added to the featured list

#### [Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* New "Pin model versions" section added (step 4) with guidance on setting Azure deployment names as model environment variables. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/microsoft-foundry.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#3-configure-claude-code)]

#### [Model Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Extended context (1M token window) availability updated: Pro/Max/Teams/Enterprise subscribers can now access it with extra usage enabled (previously stated they had no access at launch). [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/model-config.md?plain=1#L165)] [[Source](https://code.claude.com/docs/en/model-config#extended-context)]
* New "Pin models for third-party deployments" section added explaining how to pin model versions for Bedrock, Vertex AI, and Foundry to prevent user breakage on new model releases. [[line 209](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/model-config.md?plain=1#L209)] [[Source](https://code.claude.com/docs/en/model-config#environment-variables)]

#### [Monitoring Usage](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` environment variable added (default: `delta`, set to `cumulative` for backends that expect cumulative temporality). [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L88)] [[Source](https://code.claude.com/docs/en/monitoring-usage#common-configuration-variables)]
* New standard telemetry attributes: `user.id` (anonymous device identifier) and `user.email` (OAuth-authenticated email). [[line 259](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L259)] [[Source](https://code.claude.com/docs/en/monitoring-usage#standard-attributes)]
* File edit counter metric: `tool` attribute renamed to `tool_name`; new `source` attribute added for decision source. [[line 333](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L333)] [[Source](https://code.claude.com/docs/en/monitoring-usage#code-edit-tool-decision-counter)]
* Active time counter now has a `type` attribute (`"user"` for keyboard interactions, `"cli"` for tool execution and AI responses). [[line 345](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L345)] [[Source](https://code.claude.com/docs/en/monitoring-usage#active-time-counter)]
* New event correlation section: `prompt.id` UUID attribute links all events (user_prompt, api_request, tool_result) triggered by a single user prompt. [[line 352](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L352)] [[Source](https://code.claude.com/docs/en/monitoring-usage#events)]
* Tool result events: `decision`/`source` renamed to `decision_type`/`decision_source`; new `tool_result_size_bytes` and `mcp_server_scope` attributes added; Bash tool parameters updated to include `dangerouslyDisableSandbox` and `git_commit_id`. [[line 389](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L389)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* API request and API error events now include a `speed` attribute (`"fast"` or `"normal"`) indicating whether fast mode was active. [[line 415](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L415)] [[Source](https://code.claude.com/docs/en/monitoring-usage#api-request-event)]
* Tool decision event `source` field now includes `"hook"` as a possible value. [[line 446](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L446)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)]
* Security/privacy section clarified: `tool_parameters` may contain sensitive values (bash commands, file paths) and should be filtered if needed; `user.email` is now always included when authenticated via OAuth. [[line 526](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/monitoring-usage.md?plain=1#L526)] [[Source](https://code.claude.com/docs/en/monitoring-usage#roi-measurement-resources)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `delegate` permission mode removed from the supported modes table

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `spinnerTipsOverride` setting added: allows overriding spinner tips with custom strings; `excludeDefault: true` shows only custom tips, `false` merges with built-in tips. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/settings.md?plain=1#L172)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `delegate` removed from `permissionMode` field options in the YAML frontmatter reference table

#### [Third-party Integrations](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* New "Pin model versions for cloud providers" section added, recommending use of `ANTHROPIC_DEFAULT_OPUS_MODEL`, `ANTHROPIC_DEFAULT_SONNET_MODEL`, and `ANTHROPIC_DEFAULT_HAIKU_MODEL` when deploying through Bedrock, Vertex AI, or Foundry. [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/claude-code/third-party-integrations.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/third-party-integrations#pin-model-versions-for-cloud-providers)]

-----

## API changes

### Changed documents

#### [Computer Use Tool](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Claude Sonnet 4.6 now uses the `computer-use-2025-11-24` beta header (previously only Opus 4.6 and Opus 4.5 used this newer version). [[line 6](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L6)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP servers added: PitchBook Premium, Open Targets, LSEG, Yardi Virtuoso, Common Room, Sprouts Data Intelligence, DirectBooker

#### [Web Fetch Tool](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Dynamic filtering no longer requires the `code-execution-web-tools-2026-02-09` beta header — use `web_fetch_20260209` tool version directly. [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L62)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

#### [Web Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Dynamic filtering no longer requires the `code-execution-web-tools-2026-02-09` beta header — use `web_search_20260209` tool version directly. [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L49)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

#### [Compaction](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Compaction is now eligible for Zero Data Retention (ZDR) arrangements (previously excluded as a beta feature). [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/build-with-claude/compaction.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]
* Claude Sonnet 4.6 added to the list of supported models for compaction. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/build-with-claude/compaction.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

#### [Rate Limits](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* OTPM rate limits are now evaluated in real time based on actual tokens generated — the `max_tokens` parameter no longer factors into OTPM calculations, so there is no rate limit downside to setting a higher `max_tokens` value. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/api/rate-limits.md?plain=1#L92)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [What's New in Claude 4.6](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/about-claude/models/whats-new-claude-4-6.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]

* Web search and web fetch dynamic filtering section updated: no longer labeled as "beta", beta header requirement removed from the description. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/8a16334468bc5741d69ab96b83710bf034f17ee0/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]
