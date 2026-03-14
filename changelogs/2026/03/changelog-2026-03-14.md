# [Claude docs changes for March 14th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/dd19df9953f5991733717511ec95951f202ce0f3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/dd19df9953f5991733717511ec95951f202ce0f3)]

## Executive Summary
- **1M context window is now GA for Opus 4.6 and Sonnet 4.6** at standard pricing — no beta header, no premium pricing for long requests. Sonnet 4.5 and Sonnet 4 still require the beta header and premium pricing.
- **MCP elicitation support** added to Claude Code 2.1.76 — MCP servers can now request structured user input mid-task via interactive dialogs (form fields or browser URLs), with new `Elicitation` and `ElicitationResult` hooks to programmatically intercept responses.
- **Three new reference pages** extracted from the monolithic settings.md: `commands.md` (built-in slash commands), `env-vars.md` (environment variables), and `tools-reference.md` (Claude's tools).
- **New CLI flags and commands**: `/effort` slash command, `--effort` flag, `-n`/`--name` session naming flag, `--remote-control`/`--rc` flag for interactive + remote sessions, and new `PostCompact` hook.
- **Opus 4.6 1M context included for Max/Team/Enterprise** subscribers at no extra cost (previously required extra usage).

## New Claude Code versions

### [2.1.75](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/versions/2.1.75.md)

#### New features

* Added 1M context window for Opus 4.6 by default for Max, Team, and Enterprise plans (previously required extra usage)
* Added `/color` command to set a prompt-bar color for the current session
* Added session name display on the prompt bar when using `/rename`
* Added last-modified timestamps to memory files so Claude can reason about freshness
* Added hook source display (settings/plugin/skill) in permission prompts when a hook requires confirmation

#### Existing feature improvements

* Improved startup performance on macOS non-MDM machines by skipping unnecessary subprocess spawns
* Suppressed async hook completion messages by default (visible with `--verbose` or transcript mode)

#### Major bug fixes

* Fixed voice mode not activating correctly on fresh installs without toggling `/voice` twice
* Fixed Claude Code header not updating displayed model name after switching models
* Fixed session crash when an attachment message computation returns undefined values
* Fixed Bash tool mangling `!` in piped commands (e.g., `jq 'select(.x != .y)'`)
* Fixed managed-disabled plugins showing up in the `/plugin` Installed tab
* Fixed token estimation over-counting for thinking and `tool_use` blocks (prevented premature context compaction)
* Fixed `/resume` losing session names after resuming a forked or continued session

**Breaking change:** Removed deprecated Windows managed settings fallback at `C:\ProgramData\ClaudeCode\managed-settings.json` — use `C:\Program Files\ClaudeCode\managed-settings.json`

### [2.1.76](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/versions/2.1.76.md)

#### New features

* Added MCP elicitation support — MCP servers can now request structured input mid-task via an interactive dialog (form fields or browser URL)
* Added new `Elicitation` and `ElicitationResult` hooks to intercept and override responses before they're sent back to MCP servers
* Added `-n` / `--name <name>` CLI flag to set a display name for the session at startup
* Added `worktree.sparsePaths` setting for `claude --worktree` to check out only specified directories via git sparse-checkout
* Added `PostCompact` hook that fires after compaction completes
* Added `/effort` slash command to set model effort level (low/medium/high persist across sessions; `max` is session-only on Opus 4.6)
* Added session quality survey — enterprise admins can configure the sample rate via `feedbackSurveyRate` setting

#### Existing feature improvements

* Improved `--worktree` startup performance by reading git refs directly and skipping redundant `git fetch`
* Improved background agent behavior — killing a background agent now preserves its partial results
* Improved model fallback notifications — now always visible with human-friendly model names
* Improved stale worktree cleanup — worktrees left behind after interrupted parallel runs are automatically cleaned up
* Improved Remote Control session titles — now derived from your first prompt
* Updated `--plugin-dir` to only accept one path per flag; use repeated `--plugin-dir` for multiple directories

#### Major bug fixes

* Fixed deferred tools (loaded via `ToolSearch`) losing their input schemas after conversation compaction
* Fixed slash commands showing "Unknown skill"
* Fixed plan mode asking for re-approval after plan was already accepted
* Fixed auto-compaction retrying indefinitely after consecutive failures (circuit breaker now stops after 3 attempts)
* Fixed clipboard copying in tmux over SSH
* Fixed several Remote Control issues: sessions silently dying, rapid messages queued one-at-a-time, stale work items causing redelivery after JWT refresh
* Fixed bridge sessions failing to recover after extended WebSocket disconnects
* [VSCode] Fixed gitignore patterns containing commas silently excluding entire filetypes from `@`-mention file picker

-----

## Claude Code changes

### New Documents

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

New standalone reference for all built-in Claude Code slash commands (previously embedded in interactive-mode.md). Includes the new `/color` and `/effort` commands, with full argument descriptions.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

New standalone reference for all Claude Code environment variables (previously embedded in settings.md). Now also documents `CLAUDE_CODE_AUTO_COMPACT_WINDOW` for decoupling the compaction threshold from context window size.

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

New standalone reference for all tools available to Claude (previously embedded in settings.md). Includes the tool names used in permission rules, subagent tool lists, and hook matchers, plus Bash tool behavior details.

### Changed documents

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Added `--effort` flag to set effort level (low/medium/high/max) for the current session without persisting to settings. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/cli-reference.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* Added `--name` / `-n` flag to set a session display name at startup; named sessions are resumable by name. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/cli-reference.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* Added `--remote-control` / `--rc` flag to start an interactive session with Remote Control enabled simultaneously. [[line 63](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/cli-reference.md?plain=1#L63)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* Updated `--plugin-dir` to only accept one path per flag (use repeated flags for multiple directories). [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/cli-reference.md?plain=1#L61)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* Simplified system prompt flags table (replaced verbose descriptions with concise examples). [[lines 81-88](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/cli-reference.md?plain=1#L81-L88)] [[Source](https://code.claude.com/docs/en/cli-reference#system-prompt-flags)]

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Adaptive reasoning now documented as available on both Opus 4.6 and Sonnet 4.6 (previously Opus 4.6 only). [[line 831](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/common-workflows.md?plain=1#L831)] [[Source](https://code.claude.com/docs/en/common-workflows#use-extended-thinking-thinking-mode)]
* Session naming updated: `-n` flag documented for naming at startup, `/rename` noted as mid-session alternative. [[lines 877-888](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/common-workflows.md?plain=1#L877-L888)] [[Source](https://code.claude.com/docs/en/common-workflows#name-your-sessions)]
* Notification hook setup workflow updated to show JSON settings configuration directly instead of using the (now read-only) `/hooks` menu. [[lines 1069-1176](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/common-workflows.md?plain=1#L1069-L1176)] [[Source](https://code.claude.com/docs/en/common-workflows#get-notified-when-claude-needs-your-attention)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Added `PostCompact` hook event that fires after compaction completes; receives `trigger` and `compact_summary` fields. [[lines 34-36](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks.md?plain=1#L34-L36)] [[Source](https://code.claude.com/docs/en/hooks#hook-lifecycle)]
* Added `Elicitation` hook to intercept MCP server input requests; supports `accept`/`decline`/`cancel` action with form field values. [[lines 1861-1944](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks.md?plain=1#L1861-L1944)] [[Source](https://code.claude.com/docs/en/hooks#sessionend-input)]
* Added `ElicitationResult` hook to observe or modify user responses to MCP elicitations before they're sent back. [[lines 1946-2010](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks.md?plain=1#L1946-L2010)] [[Source](https://code.claude.com/docs/en/hooks#elicitation-output)]
* `/hooks` menu is now a read-only browser (no longer supports adding/deleting hooks interactively); hook source is shown on each entry. [[lines 448-470](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks.md?plain=1#L448-L470)] [[Source](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents)]
* When a hook returns `"ask"`, the permission prompt now shows a label identifying the hook's source ([User], [Project], [Plugin], [Local]). [[line 1026](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks.md?plain=1#L1026)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-decision-control)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* First hook setup walkthrough updated: hooks are now configured by editing settings JSON directly; `/hooks` is a read-only browser for verification. [[lines 8-60](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks-guide.md?plain=1#L8-L60)] [[Source](https://code.claude.com/docs/en/hooks-guide)]
* Added `PostCompact`, `Elicitation`, and `ElicitationResult` to the hook events reference table. [[lines 346-348](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/hooks-guide.md?plain=1#L346-L348)] [[Source](https://code.claude.com/docs/en/hooks-guide#how-hooks-work)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Built-in commands table removed; replaced with pointer to the new [commands reference](commands.md). [[lines 70-73](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/interactive-mode.md?plain=1#L70-L73)] [[Source](https://code.claude.com/docs/en/interactive-mode#quick-commands)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added new section documenting MCP elicitation support — form mode and URL mode dialogs, and how to use the `Elicitation` hook to respond programmatically. [[lines 1705-1719](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/mcp.md?plain=1#L1705-L1719)] [[Source](https://code.claude.com/docs/en/mcp#mcp-output-limits-and-warnings)]
* Zapier MCP server updated from user-specific URL to a standard command URL (`https://mcp.zapier.com/api/v1/connect`). [[line 654](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/mcp.md?plain=1#L654)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added Fever Event Discovery MCP server. [[lines 756-762](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/mcp.md?plain=1#L756-L762)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Added `opus[1m]` model alias for 1M context window on Opus 4.6. [[line 24](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/model-config.md?plain=1#L24)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]
* Added `max` effort level (Opus 4.6 only, session-scoped, deeper reasoning than `high`). [[line 147](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/model-config.md?plain=1#L147)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]
* Added `/effort` command and `--effort` flag to the effort level configuration options. [[lines 150-153](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/model-config.md?plain=1#L150-L153)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]
* 1M context window availability now documented by plan: Opus 4.6 included for Max/Team/Enterprise; Sonnet 4.6 requires extra usage on subscriptions; both available to API/pay-as-you-go. [[lines 155-168](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/model-config.md?plain=1#L155-L168)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]
* 1M context window pricing changed: no longer described as premium — now standard pricing for Opus 4.6 and Sonnet 4.6. [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/model-config.md?plain=1#L169)] [[Source](https://code.claude.com/docs/en/model-config#extended-context)]
* Added `[1m]` suffix support for `ANTHROPIC_DEFAULT_OPUS_MODEL` environment variable. [[lines 237-244](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/model-config.md?plain=1#L237-L244)] [[Source](https://code.claude.com/docs/en/model-config#pin-models-for-third-party-deployments)]

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Added `--spawn` flag for server mode to control how concurrent sessions are created (`same-dir` or `worktree`). [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/remote-control.md?plain=1#L50)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]
* Added `--capacity` flag to limit concurrent sessions in server mode (default 32). [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/remote-control.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]
* Documented new `--remote-control`/`--rc` flag for starting an interactive session that is simultaneously available for remote control. [[lines 64-85](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/remote-control.md?plain=1#L64-L85)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `effortLevel` setting to persist effort level across sessions (`"low"`, `"medium"`, `"high"`). [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/settings.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added `feedbackSurveyRate` setting for enterprise admins to control session quality survey frequency. [[line 192](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/settings.md?plain=1#L192)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added new `worktree` settings section: `worktree.symlinkDirectories` and `worktree.sparsePaths` for large monorepo optimization. [[lines 195-202](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/settings.md?plain=1#L195-L202)] [[Source](https://code.claude.com/docs/en/settings#worktree-settings)]
* Added migration note: legacy Windows managed settings path `C:\ProgramData\ClaudeCode\managed-settings.json` no longer supported as of v2.1.75. [[lines 89-91](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/settings.md?plain=1#L89-L91)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Environment variables section replaced with a pointer to the new [env-vars reference](env-vars.md). [[line 950](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/settings.md?plain=1#L950)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Tools table removed; replaced with pointer to the new [tools reference](tools-reference.md). [[line 953](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/settings.md?plain=1#L953)] [[Source](https://code.claude.com/docs/en/settings#tools-available-to-claude)]

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* Bundled skills section reformatted as a table with concise descriptions. [[lines 14-21](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/claude-code/skills.md?plain=1#L14-L21)] [[Source](https://code.claude.com/docs/en/skills#bundled-skills)]

-----

## API changes

### Changed documents

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* Clarified that `context-1m-2025-08-07` beta flag applies to Sonnet 4.5 and Sonnet 4 only; Opus 4.6 and Sonnet 4.6 have 1M context natively and the flag has no effect on them. [[lines 997-1001](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/agent-sdk/python.md?plain=1#L997-L1001)] [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Updated `SdkBeta` type: `context-1m-2025-08-07` now listed as compatible with Sonnet 4.5 and Sonnet 4 only; clarified that Opus 4.6 and Sonnet 4.6 have 1M context natively. [[lines 2030-2038](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/agent-sdk/typescript.md?plain=1#L2030-L2038)] [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Zapier MCP server with standard command URL (previously required a user-specific URL). [[lines 948-954](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L948-L954)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added Fever Event Discovery MCP server. [[lines 1130-1136](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L1130-L1136)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [api/rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Added new section on increasing spend limits, with step-by-step instructions for both customer-set limits and tier-enforced limits. [[lines 45-77](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/api/rate-limits.md?plain=1#L45-L77)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]
* Removed dedicated long-context rate limits section — separate 1M rate limits no longer apply to Opus 4.6/Sonnet 4.6; standard account limits now apply across all context lengths. [[lines 127-130](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/api/rate-limits.md?plain=1#L127-L130)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [api/service-tiers](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/api/service-tiers.md) [[Source](https://platform.claude.com/docs/en/api/service-tiers)]

* Priority Tier burndown rates clarified: long-context premium (2x input, 1.5x output) now only applies to Sonnet 4.5 and Sonnet 4, not to Opus 4.6 or Sonnet 4.6. [[lines 35-47](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/api/service-tiers.md?plain=1#L35-L47)] [[Source](https://platform.claude.com/docs/en/api/service-tiers)]

#### [about-claude/models/overview](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/about-claude/models/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

* Context window for Opus 4.6 and Sonnet 4.6 updated to show 1M tokens (no longer listed as beta); Haiku remains 200k. [[lines 27-28](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/about-claude/models/overview.md?plain=1#L27-L28)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

#### [about-claude/models/whats-new-claude-4-6](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/about-claude/models/whats-new-claude-4-6.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]

* Updated to reflect 1M token context window as standard (not beta) for both Opus 4.6 and Sonnet 4.6. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]

#### [about-claude/pricing](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Long context pricing restructured: Opus 4.6 and Sonnet 4.6 now billed at standard rates regardless of token count (no premium for >200k tokens). Premium long-context pricing retained only for Sonnet 4.5 and Sonnet 4. [[lines 127-162](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/about-claude/pricing.md?plain=1#L127-L162)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [build-with-claude/claude-in-microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* Added context window section: Opus 4.6 and Sonnet 4.6 have 1M context natively on Foundry; Sonnet 4.5 still requires the beta header. [[lines 215-220](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L215-L220)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

#### [build-with-claude/claude-on-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Added context window section noting 1M support for Opus 4.6 and Sonnet 4.6 natively on Vertex AI; beta header still needed for Sonnet 4.5 and Sonnet 4. [[lines 116-123](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L116-L123)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]
* Added note that Vertex AI limits request payloads to 30 MB. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L124)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [build-with-claude/context-windows](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* 1M context window is now GA for Opus 4.6 and Sonnet 4.6 — no beta header required; beta header still required for Sonnet 4.5 and Sonnet 4. [[lines 92-95](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/context-windows.md?plain=1#L92-L95)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]
* Media limit raised from 100 to 600 images or PDF pages per request. [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/context-windows.md?plain=1#L96)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]
* Server-side compaction now available in beta for both Opus 4.6 and Sonnet 4.6 (previously Opus 4.6 only). [[line 134](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/build-with-claude/context-windows.md?plain=1#L134)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added March 13, 2026 release notes: 1M context GA for Opus 4.6 and Sonnet 4.6 at standard pricing, removal of dedicated 1M rate limits, media limit raised to 600. [[lines 9-13](https://github.com/gpambrozio/ClaudeDocs/blob/dd19df9953f5991733717511ec95951f202ce0f3/docs-md/api/release-notes/overview.md?plain=1#L9-L13)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
