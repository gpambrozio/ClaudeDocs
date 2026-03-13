# [Claude docs changes for March 13th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/b823c19) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/b823c19)]

## Executive Summary
- Code Review gained a new **Manual** trigger mode and documented `@claude review` comment behavior, allowing teams to opt specific PRs into review on demand
- MCP tool search is now **enabled by default** for all sessions (previously activated only at 10% context threshold), with automatic disabling for non-first-party API hosts
- Subagents can now **scope MCP servers** to only that subagent via the `mcpServers` field, keeping server tool descriptions out of the main conversation entirely
- SessionEnd hooks now have a **1.5-second default timeout** configurable via `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS`
- The `commands/` directory format is now **legacy** in the Agent SDK — `skills/` is the recommended format for new plugins

-----

## Claude Code changes

### Changed documents

#### [Agent Teams](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Added minimum version requirement: agent teams require Claude Code v2.1.32 or later. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/agent-teams.md?plain=1#L8)] [[Source](https://code.claude.com/docs/en/agent-teams)]
* Added clarifying sentence distinguishing subagents from agent teams: "Subagents only report results back to the main agent and never talk to each other. In agent teams, teammates share a task list, claim work, and communicate directly with each other." [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/agent-teams.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/agent-teams#compare-with-subagents)]

#### [Best Practices](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Removed the "Safe autonomous mode" section, which documented `--dangerously-skip-permissions`, its risks, and guidance about running it in a sandboxed container. The flag itself is still documented in the CLI reference.

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* The `model` field for the `--agents` flag now accepts full model IDs (e.g., `claude-opus-4-6`) in addition to short aliases and `inherit`. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/cli-reference.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/cli-reference#agents-flag-format)]

#### [Code Review](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/code-review.md) [[Source](https://code.claude.com/docs/en/code-review)]

* Added a new **Manual** review trigger mode: reviews only start when someone comments `@claude review` on a PR; subsequent pushes to that PR are then reviewed automatically. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/code-review.md?plain=1#L79)] [[Source](https://code.claude.com/docs/en/code-review#set-up-code-review)]
* Added a new "Manually trigger reviews" section documenting that `@claude review` must be a top-level PR comment starting with that phrase, commenter needs owner/member/collaborator access, and the PR must be open and non-draft. [[lines 86-92](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/code-review.md?plain=1#L86-L92)] [[Source](https://code.claude.com/docs/en/code-review#manually-trigger-reviews)]
* Code Review usage is now explicitly documented as billed via "extra usage" and does not count against a plan's included usage. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/code-review.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/code-review#pricing)]
* The repository config UI dropdown is now named **Review Behavior**. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/code-review.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/code-review#set-up-code-review)]

#### [Fast Mode](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Added minimum version requirement: Fast mode requires Claude Code v2.1.36 or later. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/fast-mode.md?plain=1#L8)] [[Source](https://code.claude.com/docs/en/fast-mode)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* SessionEnd hooks now have a documented default timeout of 1.5 seconds (applies to both session exit and `/clear`). Users can increase this via the `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` environment variable. Per-hook `timeout` values are capped by this budget. [[line 1806](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/hooks.md?plain=1#L1806)] [[Source](https://code.claude.com/docs/en/hooks#sessionend-input)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `/context` command description expanded: now shows "optimization suggestions for context-heavy tools, memory bloat, and capacity warnings" in addition to the colored grid. [[line 86](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/interactive-mode.md?plain=1#L86)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]
* Removed the note that setting `CLAUDE_CODE_ENABLE_TASKS=false` reverts to the previous TODO list.

#### [Keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Added minimum version requirement: customizable keyboard shortcuts require Claude Code v2.1.18 or later. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/keybindings.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/keybindings)]
* Added `Ctrl+P` as a default keybinding for "move up in list" (`messageSelector:up`) and `Ctrl+N` for "move down in list" (`messageSelector:down`). [[lines 226-227](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/keybindings.md?plain=1#L226-L227)] [[Source](https://code.claude.com/docs/en/keybindings#message-selector-actions)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* MCP tool search is now **enabled by default** for all sessions. Previously it activated automatically at 10% context threshold (`auto` mode). Now: enabled by default, but automatically disabled when `ANTHROPIC_BASE_URL` points to a non-first-party host. Setting `ENABLE_TOOL_SEARCH=true` forces it on even for proxies. [[lines 1785-1791](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/mcp.md?plain=1#L1785-L1791)] [[Source](https://code.claude.com/docs/en/mcp#configure-tool-search)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Added minimum version requirement: auto memory requires Claude Code v2.1.59 or later. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/memory.md?plain=1#L284)] [[Source](https://code.claude.com/docs/en/memory#auto-memory)]
* Added documentation for the new `autoMemoryDirectory` setting: users can configure a custom directory for auto memory storage. This setting is not accepted from project settings to prevent shared repos from redirecting memory writes to sensitive locations. [[lines 307-317](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/memory.md?plain=1#L307-L317)] [[Source](https://code.claude.com/docs/en/memory#storage-location)]

#### [Plugin Marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Relative plugin paths (starting with `./`) must resolve within the marketplace root; using `../` to climb out is explicitly disallowed. [[lines 267-300](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/plugin-marketplaces.md?plain=1#L267-L300)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#plugin-sources)]
* The `url` field no longer requires a `.git` suffix — Azure DevOps and AWS CodeCommit URLs without the suffix now work. [[line 386](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/plugin-marketplaces.md?plain=1#L386)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#git-repositories)]
* Clarified that `strictKnownMarketplaces` restricts what users can add but does not pre-register marketplaces; use it with `extraKnownMarketplaces` to both restrict and pre-register. [[line 892](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/plugin-marketplaces.md?plain=1#L892)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#set-up-release-channels)]

#### [Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* When `--plugin-dir` and a marketplace plugin share the same name, the local `--plugin-dir` copy now takes precedence for that session. Exception: marketplace plugins force-enabled by managed settings cannot be overridden. [[line 354](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/plugins.md?plain=1#L354)] [[Source](https://code.claude.com/docs/en/plugins#test-your-plugins-locally)]

#### [Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added minimum version requirement: Remote Control requires Claude Code v2.1.51 or later. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/remote-control.md?plain=1#L14)] [[Source](https://code.claude.com/docs/en/remote-control)]

#### [Scheduled Tasks](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Added minimum version requirement: scheduled tasks require Claude Code v2.1.72 or later. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/scheduled-tasks.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `cleanupPeriodDays: 0` is now documented to delete all existing transcripts at startup and disable session persistence entirely — no new `.jsonl` files are written, `/resume` shows no conversations, and hooks receive an empty `transcript_path`. [[line 143](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/settings.md?plain=1#L143)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `autoMemoryDirectory` setting documented: custom directory for auto memory storage, accepts `~/`-expanded paths, not accepted from project settings. [[line 142](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/settings.md?plain=1#L142)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` environment variable: sets maximum time in milliseconds for SessionEnd hooks (default: 1500ms). [[line 993](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/settings.md?plain=1#L993)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* `CLAUDE_CODE_ENABLE_TASKS` behavior changed: setting to `true` now enables the task system in non-interactive mode (`-p` flag); tasks are on by default in interactive mode. Previously `false` reverted to the old TODO list. [[line 980](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/settings.md?plain=1#L980)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* `ENABLE_TOOL_SEARCH` documentation updated to reflect new default (enabled unless `ANTHROPIC_BASE_URL` is a non-first-party host), plus `true` to force on for proxies. [[line 1021](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/settings.md?plain=1#L1021)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added a `managed-settings.json` example combining `strictKnownMarketplaces` and `extraKnownMarketplaces` to both restrict and pre-register a marketplace. [[line 892](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/settings.md?plain=1#L892)] [[Source](https://code.claude.com/docs/en/settings#strictknownmarketplaces)]

#### [Sub-Agents](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* The `model` field now accepts full model IDs (e.g., `claude-opus-4-6` or `claude-sonnet-4-6`) in addition to short aliases; explicitly noted to accept the same values as the `--model` flag. [[line 233](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/sub-agents.md?plain=1#L233)] [[Source](https://code.claude.com/docs/en/sub-agents#supported-frontmatter-fields)]
* New section: **Scope MCP servers to a subagent** — the `mcpServers` field in subagent definitions allows scoping MCP servers to a specific subagent. Inline servers connect when the subagent starts and disconnect when it finishes; string references reuse the parent session's connection. Defining a server inline keeps it out of the main conversation's context entirely. [[lines 311-340](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/claude-code/sub-agents.md?plain=1#L311-L340)] [[Source](https://code.claude.com/docs/en/sub-agents#scope-mcp-servers-to-a-subagent)]

-----

## API changes

### Changed documents

#### [Plugins (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agent-sdk/plugins.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/plugins)]

* The `commands/` directory is now documented as a **legacy format**; `skills/` is the recommended format for new plugins. Both formats continue to work for backward compatibility. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agent-sdk/plugins.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/agent-sdk/plugins)]
* Plugin directory structure updated to show `skills/` first and label `commands/` as "Legacy: use skills/ instead." [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agent-sdk/plugins.md?plain=1#L150)] [[Source](https://platform.claude.com/docs/en/agent-sdk/plugins)]
* Troubleshooting section renamed from "Commands not available" to "Skills not appearing"; instructions updated to require skill files in subdirectories under `skills/` (e.g., `skills/my-skill/SKILL.md`). [[lines 205-209](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agent-sdk/plugins.md?plain=1#L205-L209)] [[Source](https://platform.claude.com/docs/en/agent-sdk/plugins)]

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Four new MCP servers added to the directory: **Tavily** (`https://mcp.tavily.com/mcp`), **Calendly** (`https://mcp.calendly.com`), **Metaview** (`https://mcp.metaview.ai/mcp`), and **Brex** (`https://api.brex.com/mcp`). [[lines 1057-1111](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L1057-L1111)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [Retrieve Message Batch (Java)](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/api/java/messages/batches/retrieve.md) [[Source](https://platform.claude.com/docs/en/api/java/messages/batches/retrieve)]

* Added a full JSON response body example (HTTP 200) showing a sample `MessageBatch` object with all fields populated. [[lines 140-165](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/api/java/messages/batches/retrieve.md?plain=1#L140-L165)] [[Source](https://platform.claude.com/docs/en/api/java/messages/batches/retrieve)]

#### [Slash Commands (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agent-sdk/slash-commands.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/slash-commands)]

* Added a note that `.claude/commands/` is the legacy format; the recommended format is now `.claude/skills/<name>/SKILL.md`, which supports both slash-command invocation and autonomous invocation by Claude. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agent-sdk/slash-commands.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/agent-sdk/slash-commands)]
* Personal and project command directory descriptions updated to note "(legacy; prefer `.claude/skills/`)". [[lines 101-102](https://github.com/gpambrozio/ClaudeDocs/blob/b823c19/docs-md/api/agent-sdk/slash-commands.md?plain=1#L101-L102)] [[Source](https://platform.claude.com/docs/en/agent-sdk/slash-commands)]
