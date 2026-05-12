# [Claude docs changes for May 12th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3)]

## Executive Summary
- **Agent view (Research Preview)** lands in v2.1.139: `claude agents` opens a single screen to dispatch, monitor, and interact with background sessions running in parallel, with full documentation added
- **`/goal` command**: set a completion condition and Claude keeps working across turns until it's met, powered by a session-scoped Stop hook using a small fast model as evaluator
- **Claude Platform on AWS**: comprehensive new documentation covers using Claude Code and the API via AWS authentication, IAM access control, and AWS Marketplace billing
- **Hook exec form (`args` field)**: commands can now spawn directly without a shell, eliminating quoting issues for path placeholders
- **Auto mode `hard_deny` rules**: new unconditional block tier that user intent and `allow` exceptions cannot override, for security boundaries that must never be crossed

## New Claude Code versions

### [2.1.139](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/versions/2.1.139.md)

#### New features

* Added agent view (Research Preview): `claude agents` opens a single list of every Claude Code session — running, blocked, or done — with dispatch, peek/reply, and attach from one screen
* Added `/goal` command: set a completion condition and Claude keeps working across turns until it's met, with a live overlay showing elapsed time, turns, and tokens
* Added `/scroll-speed` command to tune mouse wheel scroll speed with a live preview ruler
* Added `claude plugin details <name>` to show a plugin's component inventory and projected per-session token cost
* Added transcript view navigation: `?` for keyboard shortcuts, `{`/`}` to jump between user prompts, `v` to toggle shortcut panel
* Added hook `args: string[]` field (exec form) that spawns the command directly without a shell, eliminating quoting issues for path placeholders
* Added hook `continueOnBlock` option for `PostToolUse` — set to `true` to feed the hook's rejection reason back to Claude and continue the turn
* MCP stdio servers now receive `CLAUDE_PROJECT_DIR` in their environment; plugin configs can reference `${CLAUDE_PROJECT_DIR}` in commands
* API requests from subagents now carry `x-claude-code-agent-id` / `x-claude-code-parent-agent-id` headers, and OTEL spans include `agent_id` / `parent_agent_id` attributes

#### Existing feature improvements

* Compaction prompt now asks the model to preserve sensitive user instructions
* `/mcp` Reconnect picks up `.mcp.json` edits without a restart and shows HTTP status and URL when reconnecting fails
* `/context all` per-skill token estimates now account for the model's tokenizer and show rounded values
* `claude plugin install` now auto-refreshes the marketplace and retries before reporting a plugin as not found
* Remote MCP server reconnect retry on transient failures is now enabled for all users
* Remote Control, `/schedule`, claude.ai MCP connectors, and notification preferences are disabled when an API key is set even if a Claude.ai login also exists
* [VSCode] Press Cmd/Ctrl+Shift+T to reopen the most recently closed session tab

#### Major bug fixes

* Fixed a deadlock where expired credentials and `forceRemoteSettingsRefresh` blocked `claude auth login`/`logout`/`status` with no recovery path
* Fixed `autoAllowBashIfSandboxed` not auto-approving commands with shell expansions like `$VAR` and `$(cmd)`
* Fixed unbounded memory growth when an HTTP/SSE MCP server streams non-protocol data — response bodies now capped at 16 MB per SSE frame
* Fixed `Skill(name *)` permission rules — the wildcard form now works as a prefix match
* Fixed settings hot-reload not detecting edits to symlinked `~/.claude/settings.json`
* Fixed `/model` picker "Default" row not reflecting `ANTHROPIC_DEFAULT_OPUS_MODEL`/`ANTHROPIC_DEFAULT_SONNET_MODEL` overrides
* Fixed spurious "stream idle timeout" 5 minutes after a response completed
* Fixed Bash-mode up-arrow history repeating the first entry and clobbering the in-progress draft
* Fixed pasting or dropping multiple images only inserting the last one

-----

## Claude Code changes

### New Documents

#### [Agent view](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

New "Manage multiple agents with agent view" page covering the Research Preview feature introduced in v2.1.139. Documents how to open agent view with `claude agents`, monitor sessions by state (working, needs input, idle, completed, failed, stopped), peek and reply from the panel without attaching, dispatch new background sessions, manage sessions from the shell (`claude attach`, `claude logs`, `claude stop`, `claude respawn`, `claude rm`), and how the supervisor process hosts background sessions. Includes how file edits are isolated into automatic git worktrees and the `disableAgentView` admin setting.

#### [Agents](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agents.md) [[Source](https://code.claude.com/docs/en/agents)]

New "Run agents in parallel" comparison page that contrasts subagents, agent view, agent teams, worktrees, and `/batch`, explaining when to use each and how to check on running work from each approach.

#### [Claude Code on Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

New guide for pointing Claude Code at a Claude Platform on AWS workspace. Covers both authentication methods (SigV4 with standard AWS credential chain or workspace API key via `ANTHROPIC_AWS_API_KEY`), the required env vars (`CLAUDE_CODE_USE_ANTHROPIC_AWS`, `ANTHROPIC_AWS_WORKSPACE_ID`, `AWS_REGION`), model pinning, Agent SDK usage, routing through a corporate proxy, and troubleshooting common errors.

#### [Goal](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/goal.md) [[Source](https://code.claude.com/docs/en/goal)]

New `/goal` command documentation. The command sets a completion condition; after each turn a small fast model evaluates whether the condition holds and either keeps Claude working or marks the goal achieved. Covers setting a goal, writing effective conditions, checking status, clearing early, resuming with an active goal, running non-interactively with `-p`, and how evaluation works under the hood (session-scoped prompt-based Stop hook).

#### [What's New — Week 18 (April 27 – May 1, 2026)](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/whats-new/2026-w18.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w18)]

Week 18 digest covering v2.1.120–v2.1.126: sign in without a browser callback (OAuth code paste), `claude project purge`, resume by PR URL, Windows without Git Bash, `claude ultrareview` subcommand for CI, `PostToolUse` `hookSpecificOutput.updatedToolOutput`, `/skills` filter search, gateway model discovery, and more.

#### [What's New — Week 19 (May 4–8, 2026)](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/whats-new/2026-w19.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w19)]

Week 19 digest covering v2.1.128–v2.1.136: plugins from `.zip` archives and URLs (`--plugin-dir` / `--plugin-url`), history search across all projects (restored `Ctrl+R` default), `worktree.baseRef` setting, `hard_deny` auto mode rules, hooks receiving effort level, `CLAUDE_CODE_DISABLE_ALTERNATE_SCREEN`, `parentSettingsBehavior` admin key, and OAuth reliability fixes.

### Changed Documents

#### [Agent SDK — Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* New notification hook event types added: `elicitation_response` and `elicitation_complete` alongside the existing types. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]
* Clarified that `permissionDecision: 'allow'` or `'ask'` (not just `'allow'`) is required when using `updatedInput`. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

#### [Agent SDK — Overview](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* Claude Platform on AWS added as a supported provider, with `CLAUDE_CODE_USE_ANTHROPIC_AWS` and `ANTHROPIC_AWS_WORKSPACE_ID` env vars documented alongside Bedrock, Vertex, and Foundry. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agent-sdk/overview.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

#### [Agent SDK — Subagents](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* Clarified that `skills` in `AgentDefinition` controls which skills are *preloaded* (full content injected), not which skills are accessible; unlisted skills remain invocable through the Skill tool. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

#### [Auto Mode Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* New `autoMode.hard_deny` rules tier added — blocks unconditionally regardless of user intent or `allow` exceptions, for security boundaries that must never be crossed. [[line 92](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/auto-mode-config.md?plain=1#L92)] [[Source](https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules)]
* Classifier precedence updated to four tiers: `hard_deny` → `soft_deny` → `allow` → explicit user intent. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/auto-mode-config.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/auto-mode-config#override-the-block-and-allow-rules)]
* `claude auto-mode defaults` now also prints built-in `hard_deny` rules. [[line 135](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/auto-mode-config.md?plain=1#L135)] [[Source](https://code.claude.com/docs/en/auto-mode-config#inspect-the-defaults-and-your-effective-config)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New background session management commands: `claude attach <id>`, `claude logs <id>`, `claude respawn <id>`, `claude rm <id>`, `claude stop <id>`. [[lines 28-38](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/cli-reference.md?plain=1#L28-L38)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]
* `claude agents` now opens agent view; when output is piped, it lists configured subagents instead. [[line 27](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/cli-reference.md?plain=1#L27)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-commands)]
* New `--bg` flag starts a session as a background agent and returns immediately. [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/cli-reference.md?plain=1#L58)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* `--worktree` / `-w` now accepts `#<number>` or a GitHub PR URL to fetch and branch the worktree from that PR. [[line 112](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/cli-reference.md?plain=1#L112)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New workflow section added explaining which commands to use at each stage (first session, during a task, parallel work, before shipping, between sessions, troubleshooting). [[lines 14-25](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/commands.md?plain=1#L14-L25)] [[Source](https://code.claude.com/docs/en/commands#commands-across-a-typical-workflow)]
* New `/background [prompt]` command to detach the session as a background agent. [[line 35](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/commands.md?plain=1#L35)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* New `/goal [condition|clear]` command. [[line 60](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/commands.md?plain=1#L60)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* New `/radio` command to open Claude FM lo-fi radio. [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/commands.md?plain=1#L84)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* New `/scroll-speed` command (fullscreen only). [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/commands.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* New `/stop` command to stop the current background session. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/commands.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* `/clear` now accepts an optional name argument to label the previous conversation in the `/resume` picker. [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/commands.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New Claude Platform on AWS variables: `ANTHROPIC_AWS_API_KEY`, `ANTHROPIC_AWS_BASE_URL`, `ANTHROPIC_AWS_WORKSPACE_ID`, `CLAUDE_CODE_USE_ANTHROPIC_AWS`, `CLAUDE_CODE_SKIP_ANTHROPIC_AWS_AUTH`. [[lines 15-17, 152, 167](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/env-vars.md?plain=1#L15-L17)]
* New `CLAUDE_CODE_DISABLE_AGENT_VIEW` to disable background agents and agent view. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/env-vars.md?plain=1#L75)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `CLAUDE_EFFORT` env var automatically set in Bash and hook subprocesses with the active effort level. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/env-vars.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `CLAUDE_CODE_MAX_TURNS` env var to cap agentic turns globally. [[line 122](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/env-vars.md?plain=1#L122)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `DO_NOT_TRACK=1` for telemetry opt-out following the cross-tool convention. [[line 202](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/env-vars.md?plain=1#L202)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `MCP_CONNECT_TIMEOUT_MS` to control how long a query waits for the MCP connection batch. [[line 218](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/env-vars.md?plain=1#L218)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* `/scroll-speed` command documented: opens an interactive dialog with a ruler to tune mouse wheel scroll speed; writes the value to `~/.claude/settings.json`. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/fullscreen.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/fullscreen)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New section on combining results from multiple hooks: clarifies that all matching hooks run to completion before results are merged, `deny` does not short-circuit sibling hooks, and includes a two-hook example. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks-guide.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/hooks-guide)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `args` field in command hooks enables exec form: spawns the executable directly without a shell, so path placeholders need no quoting and special characters pass through verbatim. [[lines 307-341](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks.md?plain=1#L307-L341)] [[Source](https://code.claude.com/docs/en/hooks#command-hook-fields)]
* New `ExitPlanMode` hook input documentation: `plan`, `planFilePath`, and `allowedPrompts` fields described, plus how to read `tool_response.plan` in `PostToolUse`. [[lines 1142-1182](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks.md?plain=1#L1142-L1182)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-input)]
* New `continueOnBlock` option on `PostToolUse` prompt-based hooks: feeds the rejection reason back to Claude and continues the turn instead of stopping. [[line 2358](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks.md?plain=1#L2358)] [[Source](https://code.claude.com/docs/en/hooks#prompt-hook-configuration)]
* `SubagentStop` hooks clarified: do not support `additionalContext`; returning `decision: "block"` delivers the reason as the subagent's next instruction. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/hooks)]
* Note added that `/goal` is a built-in shortcut for a session-scoped prompt-based Stop hook. [[line 1747](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks.md?plain=1#L1747)] [[Source](https://code.claude.com/docs/en/hooks#stop)]
* `agent_type` for custom subagents is now the `name` field from frontmatter, not the filename. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/hooks.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/hooks)]

#### [Interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* New transcript viewer keyboard shortcuts: `?` to toggle help panel, `{`/`}` to jump between user prompts (both require fullscreen rendering). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/interactive-mode.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/interactive-mode)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* New `claudeMd` managed setting documented: embeds CLAUDE.md instructions directly in `managed-settings.json` instead of deploying a separate file; honored only in managed and policy settings. [[lines 255-263](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/memory.md?plain=1#L255-L263)] [[Source](https://code.claude.com/docs/en/memory#deploy-organization-wide-claude-md)]
* Note that CLAUDE.md scope is "per repository, shared across worktrees" (was "per working tree"). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/memory.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/memory)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified that Read/Edit deny rules now also apply to recognized Bash file commands (`cat`, `head`, `tail`, `sed`) — not just the built-in file tools. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/permissions.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/permissions)]
* New table showing which paths a deny rule matches and does not match depending on its anchor. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/permissions.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/permissions)]
* Note added that permission rules are enforced by Claude Code, not the model; CLAUDE.md shapes intent but doesn't enforce boundaries. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/permissions.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/permissions)]

#### [Plugins Reference](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* `${CLAUDE_PROJECT_DIR}` added as a third path variable (alongside `${CLAUDE_PLUGIN_ROOT}` and `${CLAUDE_PLUGIN_DATA}`), exported to hook processes and MCP/LSP servers. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/plugins-reference.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/plugins-reference)]
* `skills` manifest field now *adds* to (not replaces) the default `skills/` directory — the default is always scanned. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/plugins-reference.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/plugins-reference)]
* New `claude plugin details <name>` command documented with output format and token-cost breakdown. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/plugins-reference.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/plugins-reference)]
* Symlink behavior inside marketplaces clarified: within-plugin symlinks are preserved, cross-plugin symlinks are dereferenced, outside-marketplace symlinks are skipped. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/plugins-reference.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/plugins-reference)]

#### [Scheduled Tasks](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Cross-reference to `/goal` added: use `/goal` to keep a session working until a condition is met rather than running on an interval. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/scheduled-tasks.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `disableAgentView` setting (managed) to turn off background agents, agent view, and the supervisor. [[line 178](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L178)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `claudeMd` setting (managed only) to embed CLAUDE.md instructions directly in managed settings. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L172)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `claudeMdExcludes` setting to skip specific CLAUDE.md files by glob or path. [[line 173](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L173)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `policyHelper` setting (managed, requires v2.1.136+): points at an executable that computes managed settings dynamically at startup from device posture, identity, or a remote service. [[line 212](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L212)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `parentSettingsBehavior` setting (managed, requires v2.1.133+): controls whether SDK/IDE-supplied managed settings apply alongside an admin-deployed managed tier (`"first-wins"` or `"merge"`). [[line 208](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L208)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `autoMode` setting now documents `hard_deny` as a fourth array alongside `environment`, `allow`, and `soft_deny`. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `worktree.baseRef` setting (`"fresh"` | `"head"`) controls whether new worktrees branch from the remote default or local `HEAD`. [[line 257](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L257)] [[Source](https://code.claude.com/docs/en/settings#worktree-settings)]
* New `gcpAuthRefresh` setting for a custom script to refresh GCP Application Default Credentials. [[line 196](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L196)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `syntaxHighlightingDisabled` setting to disable syntax highlighting in diffs, code blocks, and file previews. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/settings)]
* New `bwrapPath` and `socatPath` managed-only settings (Linux/WSL2) to specify non-standard paths for sandbox binaries. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/settings.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/settings)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `skills` field clarified: it preloads full skill content into context at startup; unlisted skills remain invocable through the Skill tool during execution. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/sub-agents.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/sub-agents)]
* Background subagent permission behavior clarified: they auto-deny anything that would otherwise prompt (not "pre-approved before launch"). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/sub-agents.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/sub-agents)]
* `name` frontmatter field noted as the value hooks receive as `agent_type` (filename does not have to match). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/sub-agents.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/sub-agents)]

#### [What's New — Week 16](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/whats-new/2026-w16.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w16)]

* `/ultrareview` moved from a featured item to the "Other wins" section; mobile push notifications promoted to a featured item. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/claude-code/whats-new/2026-w16.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/whats-new/2026-w16)]

-----

## API changes

### New Documents

#### [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/claude-platform-on-aws.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws)]

Comprehensive new guide for Claude Platform on AWS: Anthropic's API with AWS authentication (SigV4 and API key), IAM access control, and AWS Marketplace billing. Covers the architecture differences from Amazon Bedrock, data retention and residency, model support including Agent Skills, Managed Agents, structured outputs, Files API, prompt caching (including 1-hour TTL), how workspace-level cache isolation applies, comparison tables with Bedrock for key features, supported SDK languages, and data governance.

### Changed Documents

#### [Agent Skills — Overview](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/agents-and-tools/agent-skills/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

* Pre-built Agent Skills and custom Skills are now documented as available on Claude Platform on AWS and Microsoft Foundry in addition to the Claude API and claude.ai. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/agents-and-tools/agent-skills/overview.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]
* Custom Skills are now described as "workspace-wide" (not org-wide); all workspace members can access them. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/agents-and-tools/agent-skills/overview.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)]

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Clarified that on the Claude API and Claude Platform on AWS, `interleaved-thinking-2025-05-14` is accepted without error on any model (ignored where not supported), while on partner-operated platforms (Bedrock, Vertex AI) it causes a failure if passed to unsupported models. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* On Claude Opus 4.7 and Opus 4.6, the `interleaved-thinking` beta header is now described as "deprecated and safely ignored" (not just deprecated). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Fast Mode](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Fast mode explicitly documented as not available on Claude Platform on AWS. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/fast-mode.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Files API availability updated: now also available on Claude Platform on AWS and Microsoft Foundry; still not available on Amazon Bedrock or Vertex AI. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/files.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Managed Agents — Overview](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/overview.md) [[Source](https://platform.claude.com/docs/en/managed-agents/overview)]

* Claude Managed Agents is also available on Claude Platform on AWS, with a reference to its guide for feature differences. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/overview.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/managed-agents/overview)]

#### [Managed Agents — Permission Policies](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/permission-policies.md) [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]

* Fixed `stop_reason.event_ids` path (was `stop_reason.requires_action.event_ids`). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/permission-policies.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]
* MCP toolset `permission_policy` now correctly documented under `default_config.permission_policy`. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/permission-policies.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]

#### [Managed Agents — Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/sessions.md) [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

* Two-step lifecycle now called out explicitly: first create the session (provisions the container), then send a user event to start work. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/sessions.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/managed-agents/sessions)]

#### [Managed Agents — Skills](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/skills.md) [[Source](https://platform.claude.com/docs/en/managed-agents/skills)]

* Skills are now described as "workspace-authored" (not "organization-authored"); workspace-level scope replaces org-level scope. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/managed-agents/skills.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/managed-agents/skills)]

#### [Prompt Caching](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Automatic caching availability updated: now includes Claude Platform on AWS (in addition to the Claude API and Microsoft Foundry beta); Bedrock and Vertex AI remain unsupported for automatic caching. [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L182)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Workspace-level cache isolation described as current (not future): as of February 5, 2026, applies to the Claude API, Claude Platform on AWS, and Microsoft Foundry (beta). [[line 387](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L387)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* 1-hour cache duration availability clarified: Claude API, Claude Platform on AWS, Vertex AI, and Microsoft Foundry (beta); Bedrock does not support it. [[line 435](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L435)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Skills Guide](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* Skill bundle format described explicitly: directory with a `SKILL.md` at the top level with `name` and `description` YAML frontmatter; Python SDK provides `files_from_dir`, and zip archives are now also accepted. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/skills-guide.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]
* Skill `name` reserved words clarified to exclude `"anthropic"` and `"claude"`. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/skills-guide.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

#### [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Structured outputs documented as generally available on Claude Platform on AWS. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/1ab2f9c6252ff0f0e534bd38595a25f3164b45d3/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
