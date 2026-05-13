# [Claude docs changes for May 13th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/339a50f) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/339a50f)]

## Executive Summary
- Fast mode now supports Claude Opus 4.7 (in addition to Opus 4.6), with Opus 4.7 becoming the default fast mode model on May 14, 2026
- New Task tools (`TaskCreate`, `TaskGet`, `TaskUpdate`, `TaskList`) introduced as the future replacement for `TodoWrite`, available via `CLAUDE_CODE_ENABLE_TASKS=1`
- The MCP documentation was overhauled: the large list of third-party servers was removed and replaced with a pointer to the Anthropic Directory
- Agent view received significant improvements: PR status dots, model override per session, new keyboard shortcuts, and expanded troubleshooting
- Agent SDK clarified that settings/hooks load only from `<cwd>/.claude/` while CLAUDE.md/rules/skills load hierarchically up to the repo root

## New Claude Code versions

### [2.1.140](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/versions/2.1.140.md)

#### Existing feature improvements

* Improved Agent tool `subagent_type` matching to accept case- and separator-insensitive values (e.g. `"Code Reviewer"` resolves to `code-reviewer`)
* Updated agent color palette
* Plugins now warn when a default component folder is silently ignored because `plugin.json` sets the matching key — shown in `/doctor`, `claude plugin list`, and `/plugin`

#### Major bug fixes

* Fixed `/goal` silently hanging when `disableAllHooks` or `allowManagedHooksOnly` is set — now shows a clear message
* Fixed a regression in settings hot-reload where symlinked settings files caused misattributed change events and spurious `ConfigChange` hooks
* Fixed `claude --bg` failing with "connection dropped mid-request" when the background service was about to idle-exit
* Fixed background service startup failing on machines with enterprise endpoint security
* Fixed remote managed settings not retrying on 401 — now retries once with a force-refreshed token
* Fixed managed `extraKnownMarketplaces` auto-update policy not being persisted to `known_marketplaces.json`
* Fixed `/loop` scheduling redundant wakeups to poll for background tasks that already notify on completion
* Fixed a recurring event-loop stall on Windows when a missing executable triggered synchronous `where.exe` re-spawns
* Fixed `Read` tool calls failing validation when `offset` is passed as a whitespace-padded or `+`-prefixed string
* Fixed native terminal cursor not staying at the input caret when the terminal loses focus

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/claude-code-features](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/claude-code-features.md) [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features)]

* Clarified that `settings.json` and hooks load only from `<cwd>/.claude/` with no parent-directory fallback, while CLAUDE.md/rules load from `<cwd>` and every parent directory, and skills load up to the repository root. [[line 44](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/claude-code-features.md?plain=1#L44)] [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features#control-filesystem-settings-with-settingsources)]
* `CLAUDE.local.md` is no longer labeled as "gitignored"; `settings.local.json` loads only from `<cwd>/.claude/`. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/claude-code-features.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/agent-sdk/claude-code-features#control-filesystem-settings-with-settingsources)]

#### [agent-sdk/modifying-system-prompts](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* New decision table added for choosing between the `claude_code` preset, preset with `append`, custom prompt, or no system prompt, with explicit criteria for each use case.
* `excludeDynamicSections` now specifies it removes "git-repo flag" rather than "git status" from dynamic content.
* Clarified that CLAUDE.md is injected as a user message (not system prompt), so it does not affect system prompt caching.
* New note: Python SDK does not support the `outputStyle` option programmatically.
* Output style activation updated: TypeScript SDK now supports `options.outputStyle` parameter; Python SDK does not.

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* `TodoWrite` marked as deprecated; new Task tools (`TaskCreate`, `TaskUpdate`, `TaskGet`, `TaskList`) documented as replacements, opt-in via `CLAUDE_CODE_ENABLE_TASKS=1`. [[~line 870](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/python.md?plain=1#L870)]
* Full type definitions and behavior documented for all four Task tools, including that `TaskCreate` returns the assigned task ID in its output (not in the input).

#### [agent-sdk/skills](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/skills.md) [[Source](https://code.claude.com/docs/en/agent-sdk/skills)]

* Skills now load from `.claude/skills/` in `<cwd>` and every parent directory up to the repository root (not just `<cwd>/.claude/skills/`). [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/skills.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/agent-sdk/skills#how-skills-work-with-the-sdk)]

#### [agent-sdk/todo-tracking](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/todo-tracking.md) [[Source](https://code.claude.com/docs/en/agent-sdk/todo-tracking)]

* New notice: `TodoWrite` is the current default; Task tools are opt-in via `CLAUDE_CODE_ENABLE_TASKS=1` and will become the default in a future release.
* New "Migrate to Task tools" section with comparison table and code examples for adapting monitoring code to `TaskCreate`/`TaskUpdate` tool-use blocks. [[~line 113](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/todo-tracking.md?plain=1#L113)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `options.outputStyle` parameter added to `query()` Options: activates a named output style for the session. [[~line 390](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L390)]
* `options.managedSettings` updated: dropped by default when admin-deployed managed tier is present; can be merged under that tier via `parentSettingsBehavior: "merge"`, but can only tighten, not loosen, managed policy. [[~line 324](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L324)]
* `TodoWrite` deprecated with pointer to Task tools; complete TypeScript type definitions for all four Task tools added (not yet exported from the SDK).

#### [agent-sdk/user-input](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/user-input.md) [[Source](https://code.claude.com/docs/en/agent-sdk/user-input)]

* New permission callback response: **"Approve and remember"** — returns a `PermissionUpdate` in `updatedPermissions` to persist the rule, skipping the prompt in future sessions. [[~line 156](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-sdk/user-input.md?plain=1#L156)]
* Third callback argument now includes a `suggestions` array of ready-made `PermissionUpdate` entries; `destination: "localSettings"` writes to `.claude/settings.local.json`.
* Python example requires `claude-agent-sdk` 0.1.80 or later.

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Teammates no longer inherit the lead's `/model` selection by default. New **Default teammate model** setting in `/config` controls this; pick **Default (leader's model)** to have teammates follow the lead's model. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-teams.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/agent-teams#specify-teammates-and-models)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Pull request status dot column added to session rows: color-coded yellow (waiting/failed), green (checks passed), purple (merged), grey (draft/closed); shows count for sessions with multiple PRs.
* `Ctrl+R` documented for renaming sessions in the organize-the-list section.
* New section "Set the model" explains how to override the model for an individual background session via `--model`, `/model`, or subagent frontmatter.
* Deleting a session now explicitly cleans up its worktree including uncommitted changes (transcript remains on disk).
* New troubleshooting entries: `claude agents` listing subagents (fix: `claude update`), "Cannot open agents because background tasks are running" (use `/tasks` then `/bg`), and "Prompt rejected as too short" (minimum 4 characters).
* Worktree auto-cleanup condition now requires no uncommitted changes, no untracked files, and no unpushed commits; named sessions prompt instead of auto-removing.

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--exclude-dynamic-system-prompt-sections` description updated: "git-repo flag" replaces "git status" in the list of removed sections. [[~line 67](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/cli-reference.md?plain=1#L67)]
* Guidance expanded for `--append-system-prompt` vs. `--system-prompt`: append for extra rules on a coding assistant; replace for different surface/identity/permission models. [[~line 123](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/cli-reference.md?plain=1#L123)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* Clarified GitHub authentication model: a cloud session can access any repo the connected GitHub account can see; GitHub App installation is only required for Auto-fix PR webhooks. [[~line 30](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L30)]
* New: to stop Auto-fix monitoring on a PR, clear the **Auto-fix** toggle in the CI status bar or tell Claude to stop.

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/exit` behavior updated: in an attached background session it now detaches and keeps the session running rather than exiting. [[~line 50](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/commands.md?plain=1#L50)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* `DO_NOT_TRACK` added as a third variable (alongside `DISABLE_TELEMETRY` and `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`) that disables the feedback survey. [[~line 31](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/data-usage.md?plain=1#L31)]
* New opt-back-in: `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL=1` routes survey ratings to an organization's own OpenTelemetry collector instead of Anthropic.

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* Administrators can set `"autoUpdate": true` on `extraKnownMarketplaces` entries in managed settings to enable auto-update for an organization marketplace without requiring each user to toggle it. [[~line 343](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/discover-plugins.md?plain=1#L343)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New variable `CLAUDE_CODE_ENABLE_OPUS_4_7_FAST_MODE`: opts in to run fast mode on Opus 4.7; Opus 4.7 becomes the default on May 14, 2026.
* New variable `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE`: forces fast mode to stay on Opus 4.6, takes precedence over `CLAUDE_CODE_ENABLE_OPUS_4_7_FAST_MODE`.
* New variable `CLAUDE_CODE_RESUME_PROMPT`: overrides the continuation message injected when resuming a mid-turn session; default is `Continue from where you left off.`
* New variable `CLAUDE_CODE_ENABLE_FEEDBACK_SURVEY_FOR_OTEL`: routes session quality survey ratings to an OpenTelemetry collector when Anthropic-bound traffic is blocked.
* `DISABLE_TELEMETRY` now also disables feature flags, potentially making some rolling-out features unavailable.

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Fast mode now supports both Opus 4.6 and Opus 4.7; **on May 14, 2026, Opus 4.7 becomes the default fast mode model** (requires v2.1.139+).
* New section "Use fast mode on Opus 4.7" with opt-in instructions via `CLAUDE_CODE_ENABLE_OPUS_4_7_FAST_MODE=1`.
* To pin fast mode to Opus 4.6: set `CLAUDE_CODE_OPUS_4_6_FAST_MODE_OVERRIDE=1`. Both Opus versions share the same rate limit pool.
* Rate limit fallback now falls back to standard speed on the same Opus version.

#### [goal](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/goal.md) [[Source](https://code.claude.com/docs/en/goal)]

* `/goal` is now unavailable when `disableAllHooks` is set at any settings level (previously only checked managed policy). [[~line 116](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/goal.md?plain=1#L116)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* The entire "Popular MCP servers" section listing ~80+ third-party servers with install commands has been removed.
* Replaced with a short "Find and build MCP servers" section pointing to the [Anthropic Directory](https://claude.ai/directory); any remote server there can be added with `claude mcp add`. [[~line 20](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/mcp.md?plain=1#L20)]
* New: the official `mcp-server-dev` plugin is referenced for scaffolding your own MCP server.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Clarified that Sonnet with 1M context is not part of the automatic plan upgrade — it requires extra usage on every subscription plan including Max. [[~line 216](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/model-config.md?plain=1#L216)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New OTEL event `claude_code.feedback_survey` documented: logged when a session quality survey appears or is answered, with attributes for `event_type`, `appearance_id`, `survey_type`, `response`, and `enabled_via_override`. [[~line 837](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/monitoring-usage.md?plain=1#L837)]

#### [output-styles](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Added clarification distinguishing output styles (replace system prompt engineering sections, use for different identity), CLAUDE.md (injected as user message, keeps coding identity), and `--append-system-prompt` (appends without removing). [[~line 111](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/output-styles.md?plain=1#L111)]

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* `echo`, `pwd`, and `which` added to the built-in read-only command set. [[~line 127](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/permissions.md?plain=1#L127)]
* Clarified that hooks and `settings.json` keys from `--add-dir` directories only load from `<cwd>/.claude/` with no parent-directory fallback. [[~line 264](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/permissions.md?plain=1#L264)]
* Embedding hosts can supply additional managed policy via SDK `managedSettings` with `parentSettingsBehavior: "merge"`; embedder values can tighten but not loosen policy. [[~line 324](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/permissions.md?plain=1#L324)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* `--plugin-dir` flag now also accepts a `.zip` archive of the plugin directory; requires Claude Code v2.1.128 or later. [[~line 292](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/plugins.md?plain=1#L292)]

#### [plugins-reference](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/plugins-reference.md) [[Source](https://code.claude.com/docs/en/plugins-reference)]

* New warning in v2.1.140: when a plugin has both a default component folder and the matching manifest key, the ignored folder is flagged in `/doctor`, `claude plugin list`, and `/plugin`. [[~line 486](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/plugins-reference.md?plain=1#L486)]
* `--yes` flag for `plugin uninstall` and `plugin prune` now triggers when stdin **or** stdout is not a TTY (previously only stdin). [[~line 735](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/plugins-reference.md?plain=1#L735)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* Clarified that locally-added MCP servers (`claude mcp add`) are not connectors; to use them in routines, add them as a connector at claude.ai/customize/connectors or declare them in a committed `.mcp.json`. [[~line 292](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/routines.md?plain=1#L292)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New fix for Ubuntu 24.04+ AppArmor blocking bubblewrap: instructions to create an AppArmor profile for `bwrap` and reload AppArmor. [[~line 81](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/sandboxing.md?plain=1#L81)]

#### [security](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/security.md) [[Source](https://code.claude.com/docs/en/security)]

* Updated: Anthropic now reviews connectors against listing criteria before adding them to the Anthropic Directory, but does not security-audit or manage individual MCP servers. [[~line 80](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/security.md?plain=1#L80)]

#### [server-managed-settings](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* New as of v2.1.139: `claude auth` subcommands are exempt from the `forceRemoteSettingsRefresh` fail-closed check, allowing re-authentication when expired credentials cause the settings fetch to fail. [[~line 161](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/server-managed-settings.md?plain=1#L161)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New setting `teammateDefaultModel`: controls the default model for agent team teammates; set to a model alias or `null` to inherit the lead's model. [[~line 247](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/settings.md?plain=1#L247)]
* `worktree.sparsePaths` description updated: "Only the listed directories plus root-level files are written to disk" (removed "cone mode" wording). [[~line 257](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/settings.md?plain=1#L257)]
* `extraKnownMarketplaces` entries now accept an optional `autoUpdate` Boolean to enable auto-update for that marketplace. [[~line 641](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/settings.md?plain=1#L641)]
* Settings precedence updated: embedding hosts can supply policy via `managedSettings` with `parentSettingsBehavior: "merge"`; embedder values can tighten but not loosen admin policy. [[~line 491](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/settings.md?plain=1#L491)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Project skills now load from `.claude/skills/` in the starting directory and in every parent directory up to the repository root (previously only the starting directory). [[~line 91](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/skills.md?plain=1#L91)]

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* `TodoWrite` marked as deprecated in favor of `TaskCreate`, `TaskGet`, `TaskList`, `TaskUpdate`; interactive sessions already use Task tools by default; `claude -p` and Agent SDK still use `TodoWrite` by default — set `CLAUDE_CODE_ENABLE_TASKS=1` to switch. [[~line 44](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/tools-reference.md?plain=1#L44)]

#### [web-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/web-quickstart.md) [[Source](https://code.claude.com/docs/en/web-quickstart)]

* Troubleshooting updated: GitHub App installation is not required for repository access; only the connected GitHub account needs access. App installation is only needed for Auto-fix. [[~line 186](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/web-quickstart.md?plain=1#L186)]

#### [worktrees](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* Worktree cleanup condition on exit now requires no uncommitted changes, no untracked files, and no new commits; named sessions prompt instead of auto-removing. [[~line 79](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/claude-code/worktrees.md?plain=1#L79)]
* Removing a worktree now also discards untracked files.

-----

## API changes

### Changed documents

#### [build-with-claude/fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Fast mode now supports Claude Opus 4.7 in addition to Opus 4.6; code examples updated to use `claude-opus-4-7`. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/api/build-with-claude/fast-mode.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]
* Supported models consideration updated: fast mode is no longer Opus 4.6 only. [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/api/build-with-claude/fast-mode.md?plain=1#L165)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

#### [managed-agents/agent-setup](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* Fast mode example updated to use `claude-opus-4-7`; notes that both Opus 4.6 and Opus 4.7 support fast mode. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/339a50f/docs-md/api/managed-agents/agent-setup.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
