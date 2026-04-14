# [Claude docs changes for April 14th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/c91fda0da7c9bc10a405f666343767ef3d4cf9a8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/c91fda0da7c9bc10a405f666343767ef3d4cf9a8)]

## Executive Summary
- Version 2.1.105 is a major release: PreCompact hooks can now block compaction, a new `asyncRewake` hook type wakes Claude on background failures, and skills get a new `when_to_use` field with a raised 1,536-character description cap
- Bash permission rules gained a detailed "Process wrappers" section documenting which wrappers (`timeout`, `nice`, `nohup`, `xargs`, etc.) are stripped before matching, and deny/ask rules are now evaluated regardless of hook return values
- `subagentStatusLine` is a new setting that lets you render custom rows in the agent panel, and plugins can now ship `monitors` that auto-arm at session start
- New telemetry events added: `plugin_installed` and `skill_activated`, and `OTEL_LOG_TOOL_DETAILS` now also populates trace span attributes
- Two new MCP servers listed: Kindora Funder Discovery and AdisInsight (pharmaceutical intelligence)

## New Claude Code versions

### [2.1.105](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/versions/2.1.105.md)

#### New features

* Added `path` parameter to the `EnterWorktree` tool to switch into an existing worktree of the current repository
* Added PreCompact hook support: hooks can now block compaction by exiting with code 2 or returning `{"decision":"block"}`
* Added background monitor support for plugins via a top-level `monitors` manifest key that auto-arms at session start or on skill invoke
* `/proactive` is now an alias for `/loop`

#### Existing feature improvements

* Improved stalled API stream handling: streams now abort after 5 minutes of no data and retry non-streaming instead of hanging indefinitely
* Improved network error messages: connection errors now show a retry message immediately instead of a silent spinner
* Improved file write display: long single-line writes are now truncated in the UI
* Improved `/doctor` layout with status icons; press `f` to have Claude fix reported issues
* Improved `/config` labels and descriptions for clarity
* Improved skill description handling: raised the listing cap from 250 to 1,536 characters and added a startup warning when descriptions are truncated
* Improved `WebFetch` to strip `<style>` and `<script>` contents from fetched pages
* Improved stale agent worktree cleanup to remove worktrees whose PR was squash-merged
* Improved MCP large-output truncation prompt to give format-specific recipes

#### Major bug fixes

* Fixed images attached to queued messages being dropped
* Fixed screen going blank when the prompt input wraps to a second line in long conversations
* Fixed leading whitespace getting copied when selecting multi-line assistant responses in fullscreen mode
* Fixed garbled bash output when commands print clickable file links
* Fixed alt+enter not inserting a newline in terminals using ESC-prefix alt encoding, and Ctrl+J not inserting a newline (regression in 2.1.100)
* Fixed queued user prompts disappearing from focus mode
* Fixed one-shot scheduled tasks re-firing repeatedly
* Fixed inbound channel notifications being silently dropped after the first message for Team/Enterprise users
* Fixed marketplace plugins with `package.json` and lockfile not having dependencies installed automatically after install/update
* Fixed stdio MCP server emitting malformed output hanging the session instead of failing fast
* Fixed MCP tools missing on the first turn of headless/remote-trigger sessions
* Fixed `/model` picker on AWS Bedrock in non-US regions persisting invalid model IDs
* Fixed 429 rate-limit errors showing a raw JSON dump instead of a clean message
* Fixed crash on resume when session contains malformed text blocks
* Fixed `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` in one project permanently disabling usage metrics for all projects
* Fixed washed-out 16-color palette when using Ghostty, Kitty, Alacritty, WezTerm, foot, rio, or Contour over SSH/mosh
* Fixed Bash tool suggesting `acceptEdits` permission mode when exiting plan mode would downgrade from a higher permission level

### [2.1.107](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/versions/2.1.107.md)

#### Existing feature improvements

* Show thinking hints sooner during long operations

-----

## Claude Code changes

### New Documents

#### [whats-new/2026-w15](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/whats-new/2026-w15.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w15)]

Week 15 (April 6–10, 2026) digest covering releases v2.1.92–v2.1.101. Highlights: **Ultraplan** enters early preview (plan in the cloud from CLI, review in browser, execute remotely or locally); **Monitor tool** streams background events into the conversation for live log tailing and reactions; **`/loop` self-pacing** when interval is omitted; **`/team-onboarding`** generates a teammate ramp-up guide; **`/autofix-pr`** enables PR auto-fix from the terminal.

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `EnterWorktreeInput` now has an optional `path` field to switch into an existing worktree; `name` and `path` are mutually exclusive. [[line ~1597](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1597)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/doctor` description updated: results now show with status icons and pressing `f` sends the report to Claude for fixing.
* `/loop` now lists `/proactive` as an alias.
* New `/team-onboarding` command: generates a team onboarding guide from the last 30 days of Claude Code usage history.

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* `claude --resume` now accepts custom session names (set with `--name` or `/rename`) in addition to session IDs.

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Added a reference to `claude.com/pricing` for subscription plan pricing (Pro, Max, Team, Enterprise).

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Added troubleshooting guidance for when a plugin is not found: run `/plugin marketplace update claude-plugins-official` to refresh, or `/plugin marketplace add anthropics/claude-plugins-official` to add it.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `ANTHROPIC_CUSTOM_MODEL_OPTION_SUPPORTED_CAPABILITIES` env var for specifying capabilities of custom model entries.
* `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` updated: now also loads `CLAUDE.local.md` from additional directories (skipped if `local` is excluded from `--setting-sources`).
* `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` updated: default budget is now auto-raised to the highest per-hook timeout configured in settings files, up to 60 seconds.
* New `CLAUDE_ENABLE_BYTE_WATCHDOG` env var: controls a byte-level streaming watchdog (enabled by default for Anthropic API) that aborts when no bytes arrive for the duration set by `CLAUDE_STREAM_IDLE_TIMEOUT_MS` (minimum 5 minutes).
* `CLAUDE_ENABLE_STREAM_WATCHDOG` now only enables the event-level watchdog (off by default); the byte-level watchdog is the new default mechanism for Anthropic API.
* `CLAUDE_STREAM_IDLE_TIMEOUT_MS` updated with per-watchdog defaults: 5 minutes (minimum) for byte-level, 90 seconds for event-level.
* `OTEL_LOG_TOOL_DETAILS` updated: now also populates tool input in trace span attributes in addition to log events.
* New `VERTEX_REGION_CLAUDE_4_5_OPUS` and `VERTEX_REGION_CLAUDE_4_6_OPUS` region override env vars for Vertex AI.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `asyncRewake` command hook field: runs in the background and wakes Claude immediately when it exits with code 2, delivering the hook's stderr as a system reminder. [[line ~291](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/hooks.md?plain=1#L291)]
* `PreCompact` hooks can now block compaction via exit code 2 or `{"decision":"block"}` JSON; previously they were side-effect only. [[line ~528](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/hooks.md?plain=1#L528)]
* Documented the two different effects of blocking PreCompact: skips proactive compaction vs. surfaces context-limit error for recovery compaction. [[line ~1788](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/hooks.md?plain=1#L1788)]
* `SessionEnd` hooks timeout behavior updated: per-hook `timeout` settings automatically raise the overall budget up to 60 seconds; the env var is now an explicit override rather than an absolute cap. [[line ~1863](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/hooks.md?plain=1#L1863)]
* Clarified that `PreToolUse` hook `permissionDecision` values do not bypass deny/ask rules — those are evaluated regardless. [[line ~930](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/hooks.md?plain=1#L930)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Ctrl+O` description updated: MCP calls now collapse to "Called slack 3 times" style (previously only read and search calls collapsed).

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New `Doctor` keybinding context with a `doctor:fix` action (default key: `F`) to send diagnostics to Claude for fixing.
* `chat:newline` now has a default binding: `Ctrl+J`.

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New MCP server added: **Kindora Funder Discovery** — find funders who support causes like yours.
* New MCP server added: **AdisInsight** — pharmaceutical drug & clinical trial intelligence.
* Updated links for bioRxiv, ChEMBL, Clinical Trials, CMS Coverage, ICD-10 Codes, and NPI Registry servers.
* Asana transport updated from `streamable-http` to `http`.

#### [memory](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD` now also loads `CLAUDE.local.md` from additional directories; previously only `CLAUDE.md`, `.claude/CLAUDE.md`, and `.claude/rules/*.md` were loaded.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `ANTHROPIC_CUSTOM_MODEL_OPTION` now supports the `_NAME`, `_DESCRIPTION`, and `_SUPPORTED_CAPABILITIES` suffixes, matching the pattern already available for the default Opus/Sonnet/Haiku model env vars.

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `claude_code.plugin_installed` telemetry event with attributes including plugin name, version, marketplace source, and install trigger (`cli` or `ui`).
* New `claude_code.skill_activated` telemetry event with attributes including skill name, source, and owning plugin.
* `OTEL_LOG_TOOL_DETAILS` now also includes `tool_input` and derived attributes (e.g., `file_path`) in trace spans, not just log events.

#### [network-config](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* Chrome integration requires `bridge.claudeusercontent.com` to be allowlisted for outbound WebSocket connections.

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified that the `:*` trailing wildcard is only recognized at the end of a pattern; in the middle (e.g., `Bash(git:* push)`) the colon is treated literally.
* A single `*` matches any sequence including spaces, so one wildcard spans multiple arguments.
* New "Compound commands" section: documented recognized command separators (`&&`, `||`, `;`, `|`, `|&`, `&`, newlines) and that each subcommand must match independently.
* New "Process wrappers" section: `timeout`, `time`, `nice`, `nohup`, `stdbuf`, and bare `xargs` are stripped before matching rules. Development environment runners (`devbox`, `mise`, `npx`, `docker exec`, etc.) are NOT stripped — write rules that include the runner.
* Hook decisions clarified: deny/ask permission rules are evaluated regardless of what a `PreToolUse` hook returns — a deny rule blocks even when the hook returned `"allow"`.
* `CLAUDE.local.md` is now also loaded from `--add-dir` directories (requires `CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1` and the `local` setting source).

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Plugin `settings.json` now supports the `subagentStatusLine` key in addition to `agent`.

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New `monitors` manifest key: background Monitor configurations that auto-arm when the plugin is enabled at session start or when a skill in the plugin is invoked.
* Plugin directory structure updated to include `monitors/monitors.json` as a recognized location.
* Plugin `settings.json` now supports `subagentStatusLine` in addition to `agent`.

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `viewMode` setting: sets the default transcript view mode on startup (`"default"`, `"verbose"`, or `"focus"`), overriding the sticky `Ctrl+O` selection.

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Added a comparison table for native Windows vs WSL 2 vs WSL 1, including sandboxing support.
* Expanded Windows setup documentation with clearer guidance on PowerShell vs CMD and how Claude Code uses Git Bash internally.
* Clarified that WSL setups do not require Git for Windows.

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New "Live change detection" section: skill directories are watched for changes; edits take effect within the current session without restarting.
* New `when_to_use` frontmatter field for skills: additional context on when Claude should invoke the skill, appended to `description` in the listing.
* Skill description cap raised from 250 to 1,536 characters, now covering the combined `description` + `when_to_use` text.

#### [statusline](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/statusline.md) [[Source](https://code.claude.com/docs/en/statusline)]

* New `subagentStatusLine` setting: renders custom row bodies in the agent panel for each subagent. The command receives subagent task data via stdin and writes one JSON line per row to override. [[line ~569](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/statusline.md?plain=1#L569)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Clarified that frontmatter hooks in subagent files only fire when the agent is spawned via the `Agent` tool or an `@-mention`, not when it runs as the main session via `--agent` or the `agent` setting.

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* `EnterWorktree` tool description updated: pass a `path` to switch into an existing worktree instead of creating a new one.
* Monitor tool: now also unavailable when `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set.

#### [ultraplan](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/claude-code/ultraplan.md) [[Source](https://code.claude.com/docs/en/ultraplan)]

* Ultraplan now automatically creates a default cloud environment on first launch if one doesn't exist.

-----

## API changes

### Changed documents

#### [agents-and-tools/agent-skills/quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Code example tabs expanded to include Python and TypeScript variants across all examples.

#### [agents-and-tools/mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* Code example tabs expanded to include more language variants.

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP server listed: **Kindora Funder Discovery** — find funders who support causes like yours (`https://kindora-mcp.azurewebsites.net/mcp/`).
* New MCP server listed: **AdisInsight** — pharmaceutical drug & clinical trial intelligence (`https://adisinsight-mcp.springer.com/mcp`).
* Updated link for ICD-10 Codes to point to the official Claude tutorial page.

#### [build-with-claude/adaptive-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Fixed contact sales link for requesting full thinking output for Claude 4 models (now uses a plain `mailto:` link).
* Code example tabs expanded to include more language variants.

#### [managed-agents/agent-setup](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* Code example tabs expanded to include curl, Python, TypeScript, and other language variants.

#### [managed-agents/environments](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/api/managed-agents/environments.md) [[Source](https://platform.claude.com/docs/en/managed-agents/environments)]

* Code example tabs expanded to include more language variants across all examples.

#### [managed-agents/memory](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/api/managed-agents/memory.md) [[Source](https://platform.claude.com/docs/en/managed-agents/memory)]

* Code example tabs expanded to include more language variants across all examples.

#### [managed-agents/sessions](https://github.com/gpambrozio/ClaudeDocs/blob/c91fda0da7c9bc10a405f666343767ef3d4cf9a8/docs-md/api/managed-agents/sessions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

* Code example tabs expanded to include more language variants across all examples.
