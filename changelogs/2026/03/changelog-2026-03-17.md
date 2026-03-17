# [Claude docs changes for March 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7751665c45eac949ae0fae34b9dd1ae996fcf371) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7751665c45eac949ae0fae34b9dd1ae996fcf371)]

## Executive Summary
- Extended thinking gains a new `display: "omitted"` option that skips streaming thinking tokens for faster time-to-first-text-token, while preserving the signature for multi-turn continuity
- Claude Code 2.1.77 fixes a critical security bug where `PreToolUse` hooks returning `"allow"` could bypass `deny` permission rules, including enterprise managed settings
- Fast mode pricing is now flat at $30/$150 MTok across the full 1M token context window (removing the previous tiered <200K / >200K pricing)
- Session quality surveys now appear for Bedrock, Vertex, and Foundry users by default (previously they were off for third-party providers)
- The `PermissionRequest` hook can now auto-approve specific permission dialogs programmatically, documented with a new example in the hooks guide

## New Claude Code versions

### [2.1.77](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/versions/2.1.77.md)

#### New features

* Added `allowRead` sandbox filesystem setting to re-allow read access within `denyRead` regions
* `/copy` now accepts an optional index: `/copy N` copies the Nth-latest assistant response
* Background bash tasks are now killed if output exceeds 5GB, preventing runaway processes from filling disk
* Sessions are now auto-named from plan content when you accept a plan
* `SendMessage` now auto-resumes stopped agents in the background instead of returning an error
* Renamed `/fork` to `/branch` (`/fork` still works as an alias)

#### Existing feature improvements

* Increased default maximum output token limits for Claude Opus 4.6 to 64k tokens, and the upper bound for Opus 4.6 and Sonnet 4.6 models to 128k tokens
* Faster startup on macOS (~60ms) by reading keychain credentials in parallel with module loading
* Faster `--resume` on fork-heavy and very large sessions — up to 45% faster loading and ~100-150MB less peak memory
* Improved `claude plugin validate` to check skill, agent, and command frontmatter plus `hooks/hooks.json`, catching YAML parse errors and schema violations
* The Agent tool no longer accepts a `resume` parameter — use `SendMessage({to: agentId})` to continue a previously spawned agent
* Show a notice when `apiKeyHelper` takes longer than 10s, preventing it from blocking the main loop
* [VSCode] Improved plan preview tab titles to use the plan's heading instead of "Claude's Plan"

#### Major bug fixes

* Fixed PreToolUse hooks returning `"allow"` bypassing `deny` permission rules, including enterprise managed settings
* Fixed "Always Allow" on compound bash commands (e.g. `cd src && npm test`) saving a single rule for the full string instead of per-subcommand, leading to dead rules and repeated permission prompts
* Fixed `--resume` silently truncating recent conversation history due to a race between memory-extraction writes and the main transcript
* Fixed Write tool silently converting line endings when overwriting CRLF files or creating files in CRLF directories
* Fixed auto-updater starting overlapping binary downloads when the slash-command overlay repeatedly opened and closed, accumulating tens of gigabytes of memory
* Fixed memory growth in long-running sessions from progress messages surviving compaction
* Fixed cost and token usage not being tracked when the API falls back to non-streaming mode
* Fixed `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` not stripping beta tool-schema fields, causing proxy gateways to reject requests
* Fixed Bash tool reporting errors for successful commands when the system temp directory path contains spaces
* Fixed Claude Desktop sessions incorrectly using the terminal CLI's configured API key instead of OAuth
* Fixed `git-subdir` plugins at different subdirectories of the same monorepo commit colliding in the plugin cache
* Fixed a race condition where stale-worktree cleanup could delete an agent worktree just resumed from a previous crash
* Fixed input deadlock when opening `/mcp` or similar dialogs while the agent is running
* Fixed IDE integration not auto-connecting when Claude Code is launched inside tmux or screen
* Fixed iTerm2 session crash when selecting text inside tmux over SSH
* Fixed clipboard copy silently failing in tmux sessions

-----

## Claude Code changes

### Changed documents

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Updated `/reload-plugins` description: now reports counts for each reloaded component and flags any load errors, rather than just reporting what was loaded. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/commands.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/commands)]

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Session quality surveys now appear by default for Bedrock, Vertex, and Foundry users (previously they were off for third-party providers). [[line 71](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/data-usage.md?plain=1#L71)] [[Source](https://code.claude.com/docs/en/data-usage#default-behaviors-by-api-provider)]
* `feedbackSurveyRate` setting can now be used to control survey frequency instead of disabling entirely; surveys are also disabled when `DISABLE_TELEMETRY` or `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` is set. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/data-usage.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/data-usage#session-quality-surveys)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* After installing a plugin, you must now run `/reload-plugins` to activate it (previously commands were described as immediately available). [[line 167](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/discover-plugins.md?plain=1#L167)] [[Source](https://code.claude.com/docs/en/discover-plugins#try-it-add-the-demo-marketplace)]
* `/reload-plugins` now shows counts for reloaded commands, skills, agents, hooks, plugin MCP servers, and plugin LSP servers. [[line 382](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/discover-plugins.md?plain=1#L382)] [[Source](https://code.claude.com/docs/en/discover-plugins#apply-plugin-changes-without-restarting)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDECODE` environment variable: set to `1` in shell environments spawned by Claude Code (Bash tool, tmux sessions), useful to detect when a script is running inside Claude Code. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/env-vars.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/env-vars)]
* New `CLAUDE_CODE_SKIP_FAST_MODE_NETWORK_ERRORS` variable: allows fast mode when the organization status check fails due to a network error (useful for corporate proxies). [[line 62](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/env-vars.md?plain=1#L62)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Fast mode pricing is now flat at $30/$150 MTok across the full 1M token context window — the previous tiered <200K / >200K pricing distinction has been removed. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/fast-mode.md?plain=1#L40)] [[Source](https://code.claude.com/docs/en/fast-mode#understand-the-cost-tradeoff)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* New example: "Auto-approve specific permission prompts" showing how to use the `PermissionRequest` hook to automatically answer permission dialogs (e.g., auto-approving `ExitPlanMode`) without user interaction, including how to set a specific permission mode via `updatedPermissions`. [[lines 326-384](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/hooks-guide.md?plain=1#L326-L384)] [[Source](https://code.claude.com/docs/en/hooks-guide#audit-configuration-changes)]
* Hook file changes are now picked up automatically by the file watcher — no longer require a session restart or `/hooks` review to take effect. [[line 644](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/hooks-guide.md?plain=1#L644)] [[Source](https://code.claude.com/docs/en/hooks-guide#configure-hook-location)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* The `permission_suggestions` output field now uses `addRules` format (with `toolName`, `ruleContent`, `behavior`, `destination`) instead of the old `toolAlwaysAllow` format. [[line 1076](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/hooks.md?plain=1#L1076)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-input)]
* New "Permission update entries" section documenting all entry types for `updatedPermissions` and `permission_suggestions`: `addRules`, `replaceRules`, `removeRules`, `setMode`, `addDirectories`, `removeDirectories`, with their fields and destination options (`session`, `localSettings`, `projectSettings`, `userSettings`). [[lines 1118-1147](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/hooks.md?plain=1#L1118-L1147)] [[Source](https://code.claude.com/docs/en/hooks#permissionrequest-decision-control)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New MCP servers added: Mixpanel (analytics), Krisp (meeting transcripts/notes), and Craft (notes/second brain). [[lines 429, 652, 726](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/mcp.md?plain=1#L429)]
* Plugin MCP server lifecycle clarified: run `/reload-plugins` to connect or disconnect MCP servers when enabling/disabling plugins mid-session. [[line 973](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/mcp.md?plain=1#L973)] [[Source](https://code.claude.com/docs/en/mcp#plugin-provided-mcp-servers)]

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* `/reload-plugins` now reloads plugin MCP servers in addition to commands, skills, agents, hooks, and LSP servers. [[line 352](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/plugins.md?plain=1#L352)] [[Source](https://code.claude.com/docs/en/plugins#test-your-plugins-locally)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `feedbackSurveyRate` description updated: setting to `0` suppresses surveys entirely; noted as useful for Bedrock/Vertex/Foundry where the default sample rate does not apply. [[line 189](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/settings.md?plain=1#L189)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Plugin subagents do not support `hooks`, `mcpServers`, or `permissionMode` frontmatter fields for security reasons — these fields are ignored when loading agents from a plugin. Workaround: copy the agent file into `.claude/agents/` or `~/.claude/agents/`. [[line 201](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/claude-code/sub-agents.md?plain=1#L201)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-the-subagent-scope)]

-----

## API changes

### Changed documents

#### [adaptive-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* New "Controlling thinking display" section: the `display` field on thinking configuration accepts `"summarized"` (default) or `"omitted"` (empty thinking field, signature preserved for multi-turn). Also documents pricing for `display: "omitted"` (billed the same, zero visible tokens). [[lines 184-215](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L184-L215)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]
* Disabled thinking can now also be specified as `{type: "disabled"}` in addition to omitting the parameter. [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L130)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/api/errors.md) [[Source](https://platform.claude.com/docs/en/api/errors)]

* New `402 billing_error` HTTP status code documented: indicates an issue with billing or payment information. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/api/errors.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/api/errors)]

#### [extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* New "Controlling thinking display" section: introduces `display: "omitted"` to skip streaming thinking tokens for lower latency, with full code examples for curl and notes on SDK support. [[lines 106-190](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L106-L190)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Streaming event documentation updated: `content_block_start` for thinking blocks now includes a `signature` field; when `display: "omitted"`, only a `signature_delta` is emitted with no `thinking_delta` events. [[lines 250, 284-305](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L250)]
* Pricing section expanded with `display: "omitted"` breakdown: billed tokens are the same as summarized, but zero thinking tokens appear in the response. [[lines 614-632](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L614-L632)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Best practices updated to recommend `display: "omitted"` for latency-sensitive applications that don't display thinking content. [[line 641](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L641)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [pdf-support](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/pdf-support.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/pdf-support)]

* Clarified that large PDFs can fail even when using the Files API (not just when sending inline), and suggested downsampling embedded images as a mitigation. [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/pdf-support.md?plain=1#L26)] [[Source](https://platform.claude.com/docs/en/build-with-claude/pdf-support)]

#### [rate-limits](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Added "Monthly Spend Limit" column to the tier requirements table, showing the maximum spend per calendar month at each tier ($100/$500/$1,000/$200,000/no limit). [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/api/rate-limits.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* March 16, 2026 entry: launch of `display` field for extended thinking, enabling `display: "omitted"` for faster streaming. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/release-notes/overview.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP servers added: Mixpanel (analytics), Pigment (business data), Krisp (meeting transcripts/notes), Craft (notes/second brain), and Jentic (single connection to all tools). [[lines 572, 768, 948, 1064, 1148](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L572)]

#### [streaming](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/streaming.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

* Added note that when `display: "omitted"` is set, no `thinking_delta` events are sent — only a `signature_delta`. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/streaming.md?plain=1#L113)] [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]
* Updated streaming example: `content_block_start` for thinking blocks now includes `"signature": ""` in the initial content block. [[line 366](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/streaming.md?plain=1#L366)] [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

#### [vision](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* Added note that requests with many large images can fail before reaching the 600-image count limit even when using the Files API; recommends downsampling before uploading. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/7751665c45eac949ae0fae34b9dd1ae996fcf371/docs-md/api/build-with-claude/vision.md?plain=1#L23)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]
