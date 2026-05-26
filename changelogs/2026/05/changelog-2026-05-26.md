# [Claude docs changes for May 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/49929ef158f0e907b3c0f84019112ea56b1ea233) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/49929ef158f0e907b3c0f84019112ea56b1ea233)]

## Executive Summary
- Effort level is now part of the prompt cache key — switching it mid-session invalidates the cache and now triggers a confirmation dialog
- New `allowAllClaudeAiMcps` managed setting lets enterprise admins load claude.ai connectors alongside a deployed `managed-mcp.json`
- `/usage` now shows a usage breakdown by skill, subagent, plugin, and MCP server on Pro/Max/Team/Enterprise plans
- Claude Security is now supported on GitHub Enterprise Server in public beta for Enterprise plans
- New documentation clarifies which tools are unavailable to subagents in the Agent SDK (Agent, AskUserQuestion, EnterPlanMode, ScheduleWakeup, WaitForMcpServers)

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Critical clarification about the `env` option: it **replaces** the subprocess environment instead of merging with `process.env`, so callers must pass `{ ...process.env, YOUR_VAR: 'value' }` to preserve inherited variables like `PATH`. [[line 407](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L407)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#options)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Clarified `Ctrl+C` behavior while attached to a session: it keeps its standard interrupt behavior (cancels a running response or `!` shell command). Double `Ctrl+C` on an empty prompt detaches, same as in any session. [[lines 153-154](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/agent-view.md?plain=1#L153-L154)] [[Source](https://code.claude.com/docs/en/agent-view#attach-to-a-session)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Added `statsig/` and `logs/` as additional legacy directories covered by the startup cleanup sweep (alongside the existing `todos/`). These are no longer written by current versions, and the sweep removes their contents and then the empty directories. [[line 201](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/claude-directory.md?plain=1#L201)] [[Source](https://code.claude.com/docs/en/claude-directory#cleaned-up-automatically)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Updated `/usage` description to mention it now includes a breakdown of usage by skill, subagent, plugin, and MCP server on Pro, Max, Team, and Enterprise plans. [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/commands.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Added documentation for the new `/usage` breakdown feature: on Pro/Max/Team/Enterprise plans, shows usage attributed to skills, subagents, plugins, and individual MCP servers as a percentage of total. Press `d` or `w` to switch between last 24 hours and last 7 days. [[lines 28-30](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/costs.md?plain=1#L28-L30)] [[Source](https://code.claude.com/docs/en/costs#using-the-/usage-command)]
* Added note that Pro and Max subscribers can set a monthly spend limit on usage credits with `/usage-credits`, with a prompt to raise/remove the limit if it is reached mid-session. [[line 34](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/costs.md?plain=1#L34)] [[Source](https://code.claude.com/docs/en/costs#managing-costs-for-teams)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Added new environment variable `CLAUDE_CODE_SYNC_SKILLS`: set to `1` to download enabled claude.ai skills into `~/.claude/skills/` before the first query and resync every 10 minutes. Applies only in non-interactive mode (`-p`). Set automatically in Claude Code on the web sessions. [[line 242](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/env-vars.md?plain=1#L242)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added new environment variable `CLAUDE_CODE_SYNC_SKILLS_WAIT_TIMEOUT_MS`: timeout in milliseconds for the first query to wait on the initial skills sync (default: 5000). [[line 243](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/env-vars.md?plain=1#L243)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [features-overview](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/features-overview.md) [[Source](https://code.claude.com/docs/en/features-overview)]

* Updated MCP description to clarify it provides "purpose-built tools for an external system, with connection and authentication handled by the server." [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/features-overview.md?plain=1#L134)] [[Source](https://code.claude.com/docs/en/features-overview#compare-similar-features)]
* Updated MCP reliability note: Claude Code now reconnects to remote servers automatically if they drop. [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/features-overview.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/features-overview#understand-how-features-load)]

#### [github-enterprise-server](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/github-enterprise-server.md) [[Source](https://code.claude.com/docs/en/github-enterprise-server)]

* Added Claude Security to the list of supported GHES features: available in public beta for Enterprise plans at [claude.ai/security](https://claude.ai/security). [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/github-enterprise-server.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/github-enterprise-server#what-works-with-github-enterprise-server)]

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* Added pager-style keyboard shortcuts for the diff detail view: `J`/`K` for line-by-line scrolling, `Space`/`Shift+Space` and `B` for full-page scrolling, `G`/`Shift+G` and `Home`/`End` to jump to top/bottom. [[lines 257-265](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/keybindings.md?plain=1#L257-L265)] [[Source](https://code.claude.com/docs/en/keybindings#diff-actions)]

#### [managed-mcp](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/managed-mcp.md) [[Source](https://code.claude.com/docs/en/managed-mcp)]

* Clarified that deploying `managed-mcp.json` suppresses claude.ai connectors by default, including admin-configured organization connectors, unless the new `allowAllClaudeAiMcps` setting is enabled. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/managed-mcp.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/managed-mcp#exclusive-control-with-managed-mcp-json)]
* Added new section documenting the `allowAllClaudeAiMcps` managed setting: set to `true` to load claude.ai connectors alongside `managed-mcp.json`. Requires v2.1.149 or later. Only effective from admin-controlled policy tiers; user/project settings have no effect. [[lines 105-111](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/managed-mcp.md?plain=1#L105-L111)] [[Source](https://code.claude.com/docs/en/managed-mcp#allow-claude-ai-connectors-alongside-the-managed-set)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added troubleshooting guidance: if the plugin marketplace is not found when installing an MCP server plugin, run `/plugin marketplace add anthropics/claude-plugins-official` first before retrying the install. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/mcp.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/mcp#find-and-build-mcp-servers)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Clarified that the OTel headers helper value can be a path to an executable (including paths with spaces) or a shell command line with arguments. On Windows, the value always runs through the shell. [[line 250](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/monitoring-usage.md?plain=1#L250)] [[Source](https://code.claude.com/docs/en/monitoring-usage#settings-configuration)]
* Added documentation on where helper failures are reported: `/doctor` output, the debug log (with `--debug`), and stderr in non-interactive sessions. [[lines 262-267](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/monitoring-usage.md?plain=1#L262-L267)] [[Source](https://code.claude.com/docs/en/monitoring-usage#script-requirements)]
* Clarified that the `tool_result` OTel event is not emitted for rejected tool calls; `decision_type` on this event is always `"accept"`. [[lines 509-525](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/monitoring-usage.md?plain=1#L509-L525)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-result-event)]
* Clarified `user_reject` vs `config` source distinction: in interactive CLI, deny-rule matches emit `"config"`; in Agent SDK and non-interactive sessions, deny-rule matches emit `"user_reject"`. [[line 629](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/monitoring-usage.md?plain=1#L629)] [[Source](https://code.claude.com/docs/en/monitoring-usage#tool-decision-event)]

#### [output-styles](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Added note that the `/output-style` command was deprecated in v2.1.73 and removed in v2.1.91; use `/config` or edit the `outputStyle` setting directly. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/output-styles.md?plain=1#L25)] [[Source](https://code.claude.com/docs/en/output-styles#change-your-output-style)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified that the `permissions.additionalDirectories` setting in a settings file grants file access only and does not trigger configuration discovery. The `--add-dir` flag and `/add-dir` command are the only paths that load configuration from additional directories. [[line 260](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/permissions.md?plain=1#L260)] [[Source](https://code.claude.com/docs/en/permissions#additional-directories-grant-file-access-not-configuration)]
* Added `allowAllClaudeAiMcps` to the managed-settings-only settings table. [[line 301](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/permissions.md?plain=1#L301)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* Effort level is now documented as part of the cache key: each effort level has its own cache for the same model. Switching mid-session recomputes the entire request. [[lines 28-29](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/prompt-caching.md?plain=1#L28-L29)] [[Source](https://code.claude.com/docs/en/prompt-caching#how-the-cache-is-organized)]
* Claude Code now shows a confirmation dialog before applying an effort level change that would invalidate the cache. A change that resolves to the same level already in effect skips the dialog. [[lines 62-65](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/prompt-caching.md?plain=1#L62-L65)] [[Source](https://code.claude.com/docs/en/prompt-caching#changing-effort-level)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added note that renaming a session from claude.ai or the Claude app also updates the local title shown in `claude --resume`. [[line 109](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/remote-control.md?plain=1#L109)] [[Source](https://code.claude.com/docs/en/remote-control#connect-from-another-device)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `allowAllClaudeAiMcps` to the settings reference: managed-settings-only option to load claude.ai connectors alongside `managed-mcp.json`. [[line 158](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/settings.md?plain=1#L158)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Clarified that `permissions.additionalDirectories` in `settings.json` does not load skills; only the `--add-dir` flag and `/add-dir` command trigger skill loading from additional directories. [[line 129](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/skills.md?plain=1#L129)] [[Source](https://code.claude.com/docs/en/skills#skills-from-additional-directories)]
* Added new section "How a skill gets its command name" explaining that the invocation name comes from the skill's file/directory location, not the frontmatter `name` field (except for plugin-root `SKILL.md` files where `name` sets the command name). [[lines 193-207](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/skills.md?plain=1#L193-L207)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added documentation for tools that are unavailable to subagents even when listed in the `tools` field: `Agent`, `AskUserQuestion`, `EnterPlanMode`, `ExitPlanMode` (unless the subagent's `permissionMode` is `plan`), `ScheduleWakeup`, and `WaitForMcpServers`. [[lines 291-298](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/sub-agents.md?plain=1#L291-L298)] [[Source](https://code.claude.com/docs/en/sub-agents#available-tools)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Clarified that `EnterWorktree` and `ExitWorktree` are not available to subagents that already run in their own working directory (e.g., with `isolation: worktree`). [[lines 22-23](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/claude-code/tools-reference.md?plain=1#L22-L23)] [[Source](https://code.claude.com/docs/en/tools-reference)]

-----

## API changes

### Changed documents

#### [adaptive-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Updated the contact link for requesting full thinking output access for Claude 4 models to use a direct `mailto:sales@anthropic.com` address instead of an obfuscated link. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/49929ef158f0e907b3c0f84019112ea56b1ea233/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L179)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]
