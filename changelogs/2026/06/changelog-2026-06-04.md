# [Claude docs changes for June 4th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/d89b5fb0) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/d89b5fb0)]

## Executive Summary
- Claude Code 2.1.162 brings the `/fork` command out of beta (now enabled by default), creating a distinct split between `/fork` (background subagent) and `/branch` (switch into conversation copy)
- Massive expansion of remote MCP server integrations (70+ new servers including Google Workspace, Spotify, Shopify, Uber, and many others)
- The orchestration mode example received a major overhaul: content-addressed journaling for resumable fan-outs, a verification wave that adversarially checks every subagent result, and a guide to building production harnesses
- Image size limits are now documented for the Vision API: 10 MB on the Claude API, 5 MB on Bedrock/Vertex
- Fourteen bugs fixed in `claude agents`, covering wide-terminal truncation, session attachment stalls, lost replies, and Ctrl+V paste

## New Claude Code versions

### [2.1.162](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/versions/2.1.162.md)

#### New features

* `claude agents --json` now includes `waitingFor` showing what a waiting session is blocked on (e.g., permission prompt)
* `--tools`: explicitly listing Grep/Glob now provides the dedicated search tools on native builds with embedded search (previously these names were silently ignored)
* `/effort` now confirms when your chosen level will persist as the default for new sessions
* Clicking a slash command in the autocomplete menu now fills it into your prompt instead of running it immediately; press Enter to run
* Remote Control now shows as a persistent footer pill (with a link to the session) instead of a startup message
* Renamed Windsurf to Devin Desktop in the `/ide` menu, `/terminal-setup`, and `/scroll-speed`, following the editor's rebrand

#### Existing feature improvements

* Quieter startup: notices group by severity, and session info and announcements share a single line per launch
* Startup warnings rewritten to be shorter and clearer, each with a concrete fix
* Launch-prompt warnings (deep link/pre-filled prompt) now stay pinned below the input until you act instead of scrolling away
* Failed turns now show a compact warning line instead of a multi-line red error block
* Improved background service startup and `claude update` verification to wait out endpoint-security scanning of new binaries instead of failing after 5 seconds
* Background dispatch spawn failures now report the error class name when no errno is available
* Removed the "Claude in Chrome enabled" and "marketplace installed" startup messages; model auto-updates and the team-onboarding tip now show as quiet notices under the logo

#### Major bug fixes

* Fixed a silent startup hang when the config directory is read-only or unwritable — Claude Code now starts with in-memory config and surfaces startup errors instead of showing a blank screen
* Fixed WebFetch permission rules not being applied to built-in preapproved domains; explicit `WebFetch(domain:...)` deny/ask/allow rules now take precedence over the preapproved-host auto-allow
* Fixed Windows permission rules never matching when spelled with backslashes (`~\`, `\\server\share`) or case-variant paths, and Read deny rules not hiding files from Glob/Grep results
* Fixed an interrupt (Esc) sent at the very start of a turn being silently dropped in stream-json/SDK sessions, leaving the turn running with no "Interrupted" feedback
* Fixed API 400 `no low surrogate in string` errors for classifier side-queries and MCP server descriptions containing emoji near a truncation boundary
* Fixed MCP per-server `timeout` config values below 1000 ms being floored to a 1-second watchdog that aborted every tool call; sub-1000 ms values are now ignored (falling back to `MCP_TOOL_TIMEOUT` or default)
* Fixed the LSP tool's `workspaceSymbol` operation returning no results; it now accepts a `query` parameter and passes it to the language server
* Fixed `claude agents` cutting live status text (tool args, replies, prompts, exec output) at 60–120 columns on wide terminals; the status detail now uses the full terminal width
* Fixed `claude agents` truncating long session names at 40 columns; the name column now grows with terminal width
* Fixed `claude agents` attach occasionally bouncing straight back to the session list on the first try after a background-service restart
* Fixed `claude agents` Ctrl+V image paste doing nothing in the dispatch input and the session reply box; pasting with no image now shows a hint
* Fixed backgrounding a session with ← silently losing the conversation when the background service cannot start; the session stays in the list as a failed row you can wake with Enter
* Fixed replies from the agents view that fail to send being lost; they are now queued for delivery on the next session start
* Fixed cross-session messaging (`SendMessage`) silently breaking when `CLAUDE_CODE_TMPDIR` or `$TMPDIR` points at a deep directory
* Fixed opening a running background session from `claude agents` stalling for 5 seconds before attaching

-----

## Claude Code changes

### Changed documents

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* The `agent` key in `applyFlagSettings()` now takes effect on the next turn (not a no-op mid-session); switching `agent` mid-session also applies that agent's model override, hooks, and system prompt. [[line 524](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L524)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#applyflagsettings)]
* When a client sends `initialize` to an already-running session, the control-response wrapper now carries an optional `pending_permission_requests` array for in-flight permission prompts that arrived before the client connected. [[line 583](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L583)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkcontrolinitializeresponse)]
* New `SDKCommandsChangedMessage` type (`system/commands_changed` subtype) documented — emitted when the set of available commands changes mid-session.
* New `'overloaded'` error value added to `SDKAssistantMessageError` (HTTP 529 server capacity, distinct from `'rate_limit'` which is HTTP 429). [[line 972](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L972)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkassistantmessage)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* From v2.1.161, when a session runs two or more parallel work items (subagents, background shell commands, monitors), a `done/total` count appears before the summary text in each row. [[line 123](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/agent-view.md?plain=1#L123)] [[Source](https://code.claude.com/docs/en/agent-view#row-summaries)]
* The peek panel now shows the longest-running parallel work item and its duration, so you can see what the session is waiting on without attaching. [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/agent-view.md?plain=1#L144)] [[Source](https://code.claude.com/docs/en/agent-view#peek-and-reply)]

#### [amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Added note that the WebSearch tool is not available on Bedrock, with a link to the tools reference for details. [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/amazon-bedrock.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#3-configure-claude-code)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/branch` and `/fork` are now distinct commands: `/branch` creates a copy of the conversation you switch into; `/fork` spawns a background subagent that inherits conversation context while you keep going. Before v2.1.161, `/fork` was an alias for `/branch`. [[lines 36-60](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/commands.md?plain=1#L36-L60)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [context-window](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/context-window.md) [[Source](https://code.claude.com/docs/en/context-window)]

* New "When your context fills up" section added, covering `/compact` with focus, clearing between tasks, delegating large reads to subagents, and the 1M token context window available on Opus 4.6+ and Sonnet 4.6. [[lines 87-96](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/context-window.md?plain=1#L87-L96)] [[Source](https://code.claude.com/docs/en/context-window#when-your-context-fills-up)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_ENABLE_AUTO_MODE` now requires Claude Code v2.1.158 or later (version requirement added). [[line 166](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/env-vars.md?plain=1#L166)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_CODE_FORK_SUBAGENT` behavior clarified: it makes forks the model's default spawn behavior; the `/fork` command now works independently without this variable. [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/env-vars.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES` environment variable (v2.1.161): controls whether `OTEL_RESOURCE_ATTRIBUTES` keys are attached as metric datapoint labels (default: true). [[line 313](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/env-vars.md?plain=1#L313)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Fast mode cache invalidation clarified: the cost applies only once per conversation; toggling fast mode off and back on does not repeat the cost; automatic fallback to standard speed after rate limits also preserves the cache.

#### [fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Expanded clipboard behavior documentation: per-platform clipboard tools documented (macOS: `pbcopy`, Linux: `wl-copy`/`xclip`/`xsel`, Windows/WSL: PowerShell `Set-Clipboard`) and modifier keys for native text selection per terminal.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* New `'overloaded'` error type added to `StopFailure` hook event matcher values (and in `hooks-guide.md`). [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/hooks.md?plain=1#L197)] [[Source](https://code.claude.com/docs/en/hooks#matcher-patterns)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* From v2.1.161, unused connectors (never signed in to) are collapsed behind a "Show unused connectors" row in the claude.ai section of the MCP panel, preventing long organization-provisioned lists from filling the panel. [[line 733](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/mcp.md?plain=1#L733)] [[Source](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-claude-ai)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* New `OTEL_METRICS_INCLUDE_RESOURCE_ATTRIBUTES` variable documented; `OTEL_RESOURCE_ATTRIBUTES` custom keys are now attached to metric datapoints directly (not just the OTLP resource block), enabling grouping/filtering in metrics backends, with a high-cardinality warning.

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* The `.claude` protected directory exception is now narrowed to only `.claude/worktrees`; previously `.claude/commands`, `.claude/agents`, and `.claude/skills` were also listed as exceptions. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/permission-modes.md?plain=1#L284)] [[Source](https://code.claude.com/docs/en/permission-modes#protected-paths)]

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/prompt-caching.md) [[Source](https://code.claude.com/docs/en/prompt-caching)]

* New "Turning on fast mode" section explains cache invalidation mechanics: enabling fast mode invalidates the cache once per conversation; subsequent toggles and rate-limit fallbacks preserve the cache. Requires v2.1.86 or later for persistent header behavior. [[lines 62-65](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/prompt-caching.md?plain=1#L62-L65)] [[Source](https://code.claude.com/docs/en/prompt-caching#turning-on-fast-mode)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `forceLoginMethod` clarified: third-party provider sessions (Bedrock, Vertex, Foundry) are NOT blocked by this setting; only `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, and `apiKeyHelper` sessions are blocked. [[line 197](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/settings.md?plain=1#L197)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `workflowKeywordTriggerEnabled` versioned: added in v2.1.157; the trigger keyword was `workflow` before v2.1.160. [[line 244](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/settings.md?plain=1#L244)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* The `git` marketplace source type now documented to work with any git hosting service, including self-hosted GitLab and Bitbucket. [[line 654](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/settings.md?plain=1#L654)] [[Source](https://code.claude.com/docs/en/settings#extraknownmarketplaces)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* `/fork` command is now enabled by default from v2.1.161; `CLAUDE_CODE_FORK_SUBAGENT` only controls whether forks are the model's default spawn behavior (not whether `/fork` is available).

#### [troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/troubleshooting.md) [[Source](https://code.claude.com/docs/en/troubleshooting)]

* New entry for garbled or corrupted text in VS Code, Cursor, or Devin Desktop integrated terminals: fix is to disable GPU acceleration via `/terminal-setup` or by setting `terminal.integrated.gpuAcceleration` to `"off"`. [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/claude-code/troubleshooting.md?plain=1#L52)] [[Source](https://code.claude.com/docs/en/troubleshooting#garbled-or-corrupted-text-in-an-editor’s-integrated-terminal)]

-----

## API changes

### Changed documents

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Over 70 new remote MCP server integrations added, including Google Workspace (Calendar, Drive, Gmail), Spotify, Shopify, Uber/Uber Eats, Expedia, Booking.com, Datadog, Sourcegraph, Wolfram, SurveyMonkey, Todoist, Ramp, and many more. [[line 263](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L263)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* New integrations in the first-listed section: Fathom, Klarity, Lawve AI, Otter.ai, Peec AI, Read AI, and Scite. [[lines 263-391](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L263-L391)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [api/csharp/beta/sessions/events](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/api/csharp/beta/sessions/events.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/sessions/events)]

* Comprehensive C# SDK reference added for all session event types, including `BetaManagedAgentsUserMessageEvent`, `BetaManagedAgentsAgentCustomToolUseEvent`, `BetaManagedAgentsAgentThinkingEvent`, `BetaManagedAgentsAgentMcpToolUseEvent`, `BetaManagedAgentsSessionErrorEvent`, and others.
* New `types` filter parameter documented for filtering session events by type (e.g., `user.message`, `agent.tool_use`).

#### [build-with-claude/mid-conversation-effort-example](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/build-with-claude/mid-conversation-effort-example.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example)]

* New `MAX_CONCURRENT` / `MAX_TOTAL_SUBTASKS` split: the two parameters now separate how many subagents run at once from how many the model may queue per Workflow call. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/build-with-claude/mid-conversation-effort-example.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example)]
* New "Journal results so reruns resume" section: content-addressed journaling with SHA-256 keys makes fan-outs idempotent — interrupted runs recompute only unfinished subtasks on restart. [[line 266](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/build-with-claude/mid-conversation-effort-example.md?plain=1#L266)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example)]
* New adversarial verification wave: after the first fan-out wave completes, a second wave re-derives each result and defaults to "refuted" when uncertain, returning both the original result and its verdict to the orchestrator. [[line 311](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/build-with-claude/mid-conversation-effort-example.md?plain=1#L311)] [[Source](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-effort-example)]
* New "Toward a production harness" section outlines what a real-world harness would add: sandboxed orchestration scripts, durable journaling, and per-session budget enforcement.

#### [build-with-claude/vision](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* New per-image size limits documented: 10 MB (base64) on the Claude API and claude.ai, 5 MB on Amazon Bedrock and Vertex AI. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/build-with-claude/vision.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Claude Platform on AWS authentication clarified: workers can now authenticate with either AWS IAM (SigV4) or an API key generated in the AWS Console (not just SigV4). [[line 52](https://github.com/gpambrozio/ClaudeDocs/blob/d89b5fb0/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L52)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]
