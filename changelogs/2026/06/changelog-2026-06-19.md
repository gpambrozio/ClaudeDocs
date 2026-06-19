# [Claude docs changes for June 19th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/7cd7a71d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/7cd7a71d)]

## Executive Summary
- **Artifacts** is a new Claude Code feature (Team/Enterprise) that publishes session output as private, interactive web pages on claude.ai — shareable within your organization and live-updating as the session continues
- **Agent teams UI redesigned**: in-process mode now uses an agent panel with arrow-key navigation instead of Shift+Down; idle teammates auto-hide after 30 seconds; the default `teammateMode` changed from `auto` to `in-process`
- **New server tool versions**: `web_search_20260318` and `web_fetch_20260318` add `response_inclusion` control to reduce output tokens in agentic loops; `web_fetch_20260309` adds cache bypass; `code_execution_20260521` discloses the 90-second per-cell time limit
- **CMEK now supports HIPAA**: the previous restriction preventing CMEK from being used with HIPAA-enabled organizations has been removed
- **Automatic prompt caching for server tools**: the API now automatically places 5-minute cache breakpoints on server tool results during agentic loops when prompt caching is enabled

## New Claude Code versions

### [2.1.183](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/versions/2.1.183.md)

#### New features

* Added `attribution.sessionUrl` setting to omit the claude.ai session link from commits and PRs in web and Remote Control sessions
* Added `/config --help` to list all available shorthand keys for `/config key=value`

#### Existing feature improvements

* Improved auto mode safety: destructive git commands (`git reset --hard`, `git checkout -- .`, `git clean -fd`, `git stash drop`) are now blocked when you didn't ask to discard local work; `git commit --amend` is blocked when the commit wasn't made by the agent this session; `terraform destroy`/`pulumi destroy`/`cdk destroy` are blocked unless you asked for the specific stack
* Added a warning when the requested model is deprecated or automatically updated to a newer model, shown on stderr in print mode (`-p`) and now also covering models set in agent frontmatter
* Changed `/config` toggle behavior: Enter and Space both change the selected setting; Esc now saves and closes instead of reverting
* Removed the startup "setup issues" line under the logo — run `/doctor` to see configuration issues or use `--debug`

#### Major bug fixes

* Fixed `thinking.disabled.display: Extra inputs are not permitted` 400 errors on subagent spawns and session-title generation for affected configurations
* Fixed WebSearch returning empty results in subagents
* Fixed the terminal cursor being stranded above the prompt after navigating history in vim mode with the native cursor enabled
* Fixed fullscreen TUI corruption (statusline mid-screen, duplicated spinner rows, merged text) in Windows Terminal under heavy nested-subagent load
* Fixed turns silently completing with no visible output when the model returned only a thinking block; Claude now re-prompts once
* Fixed user-level skills appearing multiple times in slash-command autocomplete when multiple plugins are enabled
* Fixed MCP servers requiring authentication exposing auth-stub tools to the model in headless/SDK mode
* Fixed tmux teammate panes failing to launch when the shell has slow rc-file initialization, and keystrokes typed during agent spawn leaking into the new tmux pane instead of the leader prompt
* Fixed background tasks started by a teammate being killed when the teammate finishes a turn
* Fixed scheduled task and webhook trigger deliveries being treated as keyboard input; they now classify as task notifications and can no longer approve a pending action or set the session title in auto mode
* Fixed focus mode showing "Ran N PostToolUse hooks" timing lines under each response

-----

## Claude Code changes

### New Documents

#### [Artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

New documentation for the Artifacts beta feature (requires Team or Enterprise plan and `/login` authentication). Artifacts are live, interactive web pages that Claude Code publishes from your session to a private URL on claude.ai. The page updates in place as the session continues and can be shared within your organization. The doc covers when to use artifacts, how to create/update/share them, prompting patterns for richer pages, page constraints (single HTML page, no external requests, 16 MiB limit), availability requirements, and how admins can manage artifacts including retention policies, audit logs, and Compliance API endpoints.

### Changed documents

#### [Agent SDK / Subagents](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* Clarified subagent depth limit: the foreground/background distinction is removed. All subagents (both foreground and background) are now capped at depth 5 — the previous rule that foreground subagents could spawn at any depth is no longer accurate. [[line 119](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L119)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#agentdefinition-configuration)]

#### [Agent SDK / TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Updated `peer` origin description for `SDKMessageOrigin`: now explicitly documents that for in-process teammates sending to `main` via `SendMessage`, `from` is the teammate's name and `senderTaskId` is its task ID; for cross-session peers, `from` is the sender address and `senderTaskId` is absent. [[line 1249](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1249)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#sdkmessageorigin)]

#### [Agent Teams](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* In-process mode now uses an **agent panel** below the prompt input: up/down arrows to select a teammate, Enter to open their transcript and message them, Escape to interrupt. The previous Shift+Down cycling is removed. [[line 72](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-teams.md?plain=1#L72)] [[Source](https://code.claude.com/docs/en/agent-teams#start-your-first-agent-team)]
* As of v2.1.181, idle teammates' rows auto-hide after 30 seconds and reappear on their next turn; teammates stay running and addressable while hidden. [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-teams.md?plain=1#L78)] [[Source](https://code.claude.com/docs/en/agent-teams#start-your-first-agent-team)]
* The default `teammateMode` changed from `"auto"` to `"in-process"` as of v2.1.179; upgraded sessions that previously used split panes now stay in one terminal unless the mode is set explicitly. [[line 94](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-teams.md?plain=1#L94)] [[Source](https://code.claude.com/docs/en/agent-teams#choose-a-display-mode)]
* In-process mode now has a stop shortcut: press `x` on a selected teammate to stop it. [[line 140](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/agent-teams.md?plain=1#L140)] [[Source](https://code.claude.com/docs/en/agent-teams#talk-to-teammates-directly)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* As of v2.1.181, the flat output from `aws configure export-credentials --format process` is now accepted (keys at the top level instead of nested under `Credentials`). [[line 132](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/amazon-bedrock.md?plain=1#L132)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#advanced-credential-configuration)]

#### [Claude Code on the Web](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* As of v2.1.179, commits that Claude creates in a web session automatically include a `Claude-Session: <url>` git trailer, and PR bodies include the session URL — no manual construction needed. Instructions for linking session output in other contexts (Slack posts, reports) retained. [[line 101](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L101)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#link-output-back-to-the-session)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* New `--ax-screen-reader` flag: renders screen-reader-friendly output (flat text, no decorative borders or animations). Requires v2.1.181. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/cli-reference.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]
* `--teammate-mode` default changed from `auto` to `in-process` as of v2.1.179. [[line 106](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/cli-reference.md?plain=1#L106)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* `/config` now accepts `key=value` pairs to set a setting directly without opening the UI, e.g. `/config thinking=false`. Also works in non-interactive mode (`-p`) and from Remote Control. Run `/config help` to list available keys. Requires v2.1.181. [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/commands.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_AX_SCREEN_READER` env var: enables screen-reader-friendly output (requires v2.1.181). [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/env-vars.md?plain=1#L130)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CLIENT_PRESENCE_FILE` env var: path to a marker file that suppresses mobile push notifications while you're at the machine (requires v2.1.181). [[line 132](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/env-vars.md?plain=1#L132)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_ARTIFACT_AUTO_OPEN` env var: set to `0` to prevent the browser from opening automatically when a new artifact is published. [[line 153](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/env-vars.md?plain=1#L153)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_DISABLE_ARTIFACT` env var: set to `1` to disable the Artifact tool. [[line 155](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/env-vars.md?plain=1#L155)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* New `CLAUDE_CODE_OTEL_DIAG_STDERR` env var: set to `1` to write OpenTelemetry exporter diagnostic errors to stderr (requires v2.1.179). [[line 214](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/env-vars.md?plain=1#L214)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `OTEL_LOG_TOOL_DETAILS` now also includes the refusal `category` on `api_refusal` events. [[line 324](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/env-vars.md?plain=1#L324)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` description updated: Remote Control sessions no longer listed as a proactive compaction case. [[line 128](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/env-vars.md?plain=1#L128)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [Fullscreen](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* As of v2.1.181, clicking a URL or file path no longer opens it — you must hold `Cmd` on macOS or `Ctrl` on Linux/Windows while clicking. This matches native terminal behavior. [[line 41](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/fullscreen.md?plain=1#L41)] [[Source](https://code.claude.com/docs/en/fullscreen#use-the-mouse)]

#### [Headless / Non-interactive Mode](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Clarified that `/config key=value` works in `-p` mode; `/config` without arguments (interactive dialog) does not. [[line 196](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/headless.md?plain=1#L196)] [[Source](https://code.claude.com/docs/en/headless#create-a-commit)]

#### [MCP Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/mcp-quickstart.md) [[Source](https://code.claude.com/docs/en/mcp-quickstart)]

* New MCP server status: `! Connected · tools fetch failed` — the server connected but couldn't list its tools; run `claude mcp get <name>` for details. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/mcp-quickstart.md?plain=1#L56)] [[Source](https://code.claude.com/docs/en/mcp-quickstart#add-and-verify-a-server)]

#### [Monitoring Usage](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `api_refusal` event now emits many additional attributes: `query_source`, `speed`, `attempt`, `effort`, `server_fallback_hop` (whether the API's server-side fallback already retried on a different model), `has_category`, `has_explanation`, `category` (only with `OTEL_LOG_TOOL_DETAILS=1`), and skill/plugin/MCP attribution fields. [[line 592](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/monitoring-usage.md?plain=1#L592)] [[Source](https://code.claude.com/docs/en/monitoring-usage#api-refusal-event)]

#### [Network Config](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/network-config.md) [[Source](https://code.claude.com/docs/en/network-config)]

* New allowlist entry: `*.claudeusercontent.com` — required in the browser (not the CLI) for viewing artifacts on claude.ai. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/network-config.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/network-config#network-access-requirements)]

#### [Plugin Marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Expanded explanation of how skills load for marketplace-root plugin entries: when `source: "./"`, listing specific subdirectories in `skills` makes that list the complete set for the entry; listing `./skills/` itself keeps the full scan. [[line 471](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/plugin-marketplaces.md?plain=1#L471)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#advanced-plugin-entries)]

#### [Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* RC failure behavior changed: a notification now appears with the failure reason and the indicator disappears from the footer (previously the indicator turned red). Run `/remote-control` again to retry. [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/remote-control.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/remote-control#check-connection-status)]
* New `CLAUDE_CLIENT_PRESENCE_FILE` option: configure a screen-lock listener to skip mobile push notifications while you're at the computer (requires v2.1.181). [[line 166](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/remote-control.md?plain=1#L166)] [[Source](https://code.claude.com/docs/en/remote-control#mobile-push-notifications)]
* `/config key=value` now works from mobile and web Remote Control (from v2.1.181). [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/remote-control.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/remote-control#limitations)]

#### [Sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* New `allowAppleEvents` sandbox setting (macOS only): allows `open`, `osascript`, and browser-based auth flows that otherwise fail with error `-600`. **Removes code-execution isolation** — sandboxed commands can launch other apps unsandboxed. Only honored from user, managed, or CLI settings, not project settings. [[line 302](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/sandboxing.md?plain=1#L302)] [[Source](https://code.claude.com/docs/en/sandboxing#troubleshooting)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* New `axScreenReader` setting: render screen-reader-friendly output (requires v2.1.181). [[line 200](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/settings.md?plain=1#L200)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New `disableArtifact` setting: set to `true` to disable the Artifact tool. [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/settings.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* `teammateMode` default changed from `"auto"` to `"in-process"` as of v2.1.179. [[line 273](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/settings.md?plain=1#L273)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* New sandbox setting `allowAppleEvents` (macOS only): allow sandboxed commands to send Apple Events. [[line 366](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/settings.md?plain=1#L366)] [[Source](https://code.claude.com/docs/en/settings#sandbox-settings)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New section "Evaluate and iterate on a skill": documents how to use the `skill-creator` plugin to run automated evals comparing with-skill vs without-skill, blind A/B version comparisons, description tuning, and visual review via an HTML report viewer. [[line 532](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/skills.md?plain=1#L532)] [[Source](https://code.claude.com/docs/en/skills#evaluate-and-iterate-on-a-skill)]

#### [Sub-Agents](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Simplified depth limit: the foreground/background distinction removed. All subagents are capped at depth 5; the previous rule that foreground subagents could spawn at any depth no longer applies. [[line 739](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/sub-agents.md?plain=1#L739)] [[Source](https://code.claude.com/docs/en/sub-agents#spawn-nested-subagents)]

#### [Tools Reference](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* New `Artifact` tool added to the built-in tools table: publishes an HTML or Markdown file as a private, interactive page on claude.ai. Requires Team/Enterprise plan and `/login` authentication. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/tools-reference.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/tools-reference)]

#### [Ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* If a PR's diff is too large, Claude Code now refuses the review with a scoping hint before any review work runs. [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/ultrareview.md?plain=1#L31)] [[Source](https://code.claude.com/docs/en/ultrareview#run-ultrareview-from-the-cli)]

#### [Workflows](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Added context that the closest-`.claude/workflows/` saving behavior (v2.1.178) is especially useful in monorepos to keep workflows alongside the package they apply to. [[line 162](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/workflows.md?plain=1#L162)] [[Source](https://code.claude.com/docs/en/workflows#save-the-workflow-for-reuse)]

#### [Zero Data Retention](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/zero-data-retention.md) [[Source](https://code.claude.com/docs/en/zero-data-retention)]

* Artifacts added to the list of features not available with ZDR (requires storing published content on Anthropic-operated infrastructure). [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/claude-code/zero-data-retention.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/zero-data-retention#features-disabled-under-zdr)]

-----

## API changes

### New Documents

#### [Create an Admin API key](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/admin-api-keys.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api-keys)]

New guide centralizing Admin API key creation for both organization types. Covers which key type is needed (Claude Console vs Claude Enterprise), step-by-step creation instructions, the scope selection table for Claude Enterprise keys (read/write:spend_limits, read:analytics, read:compliance_activities, read/delete:compliance_user_data, read:compliance_org_data/settings), and how to use the key in API requests.

### Changed documents

#### [Agents and Tools / Tool Use / Code Execution Tool](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* New tool version `code_execution_20260521`: same runtime as `_20260120` but discloses the 90-second per-cell wall-clock time limit in the tool description, so Claude can budget long-running cells. Code exceeding the limit returns a `detection_timeout` result. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L40)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* "Free with web search or web fetch" pricing updated to say `_20260209` or later (not just `_20260209` specifically). [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Agents and Tools / Tool Use / Computer Use Tool](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Screenshot handling guidance updated: the API does NOT silently downscale oversized screenshots — it rejects them with HTTP 400. Updated guidance requires you to resize before sending and set display dimensions to the resized size. [[line 562](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L562)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

#### [Agents and Tools / Tool Use / Parallel Tool Use](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)]

* Major conceptual clarification: execution order of parallel tool calls is your decision. You may run calls concurrently or sequentially depending on your tools' dependencies. Documentation updated to reflect that running sequentially and stopping on first failure is a valid strategy; return `is_error: true` for any call you didn't execute. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/parallel-tool-use.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)]

#### [Agents and Tools / Tool Use / Server Tools](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/server-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]

* References to `_20260209` versions updated to `_20260209` or later throughout, covering ZDR configuration and dynamic filtering notes. [[line 84](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/server-tools.md?plain=1#L84)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]

#### [Agents and Tools / Tool Use / Tool Reference](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/tool-reference.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)]

* New tool versions added to the server tools table: `web_search_20260318`, `web_fetch_20260318`, `web_fetch_20260309`, `code_execution_20260521`. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/tool-reference.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)]
* `code_execution_20260521` and `code_execution_20260120` are interchangeable in `allowed_callers` — a request using either version satisfies tools listing either caller. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/tool-reference.md?plain=1#L69)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-reference)]

#### [Agents and Tools / Tool Use / Tool Use with Prompt Caching](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/tool-use-with-prompt-caching.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)]

* New section "Server tool results are cached automatically": when prompt caching is enabled and Claude uses a server tool, the API automatically places a 5-minute cache breakpoint on the result before the next agentic loop iteration. These writes appear as `cache_creation.ephemeral_5m_input_tokens` in the response. Applies only when the request already has at least one `cache_control` marker. [[line 74](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/tool-use-with-prompt-caching.md?plain=1#L74)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-use-with-prompt-caching)]

#### [Agents and Tools / Tool Use / Web Fetch Tool](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Latest version is now `web_fetch_20260318`, which adds `response_inclusion` control and includes dynamic filtering and cache bypass from previous versions. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]
* New `cache bypass` option (`use_cache: false`) in `web_fetch_20260309`+: bypass the cache to fetch fresh content. Default is `true`. [[line 174](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L174)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]
* New `response_inclusion` parameter in `web_fetch_20260318`+: set to `"excluded"` to omit fetch result blocks consumed by a completed code execution call from the API response, reducing output tokens. [[line 182](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L182)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

#### [Agents and Tools / Tool Use / Web Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Latest version is now `web_search_20260318`, which adds `response_inclusion` control in addition to dynamic filtering. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]
* New `response_inclusion` parameter in `web_search_20260318`+: set to `"excluded"` to omit search result blocks consumed by a completed code execution call from the API response, reducing output tokens. [[line 168](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L168)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

#### [API / Compliance / Activities / List](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/api/compliance/activities/list.md) [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)]

* New Compliance API activity event types added: `abuse_decision_received` (external anti-abuse service decision on sign-in/sign-up), `claude_project_document_updated`, `claude_project_sync_source_created/deleted/updated`, `design_project_created/deleted/updated`, `org_capability_grant_added/removed`, and others. [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/api/compliance/activities/list.md?plain=1#L22)] [[Source](https://platform.claude.com/docs/en/api/compliance/activities/list)]

#### [Build with Claude / Prompt Caching](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Added a note explaining that unexpected `ephemeral_5m_input_tokens` writes in the response may occur when using server tools such as web search — with a link to the tool use + caching guide. [[line 521](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L521)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Manage Claude / Admin API](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

* Added link to the new [Create an Admin API key](manage-claude/admin-api-keys.md) guide in the authentication section. [[line 17](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/admin-api.md?plain=1#L17)] [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

#### [Manage Claude / Analytics API](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

* Major content addition for the Claude Enterprise Analytics API: new sections on data availability and freshness (engagement endpoints available for dates on/after January 1, 2026; cost data refreshes within 4 hours, revisable for 30 days), metric definitions (active user counting, per-product metric blocks, connector name normalization), and working with the API (pagination cursor binding, bracket notation for list params, decimal string currency amounts, rate limits). [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/analytics-api.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

#### [Manage Claude / API and Data Retention](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Computer use tool is now marked as **HIPAA-eligible** (changed from No to Yes). [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L175)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [Manage Claude / CMEK](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Removed the restriction that CMEK is not supported for organizations with HIPAA enabled. CMEK can now be used together with HIPAA. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/cmek.md?plain=1#L37)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

#### [Manage Claude / Spend Limits API](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/spend-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]

* Added direct links to the API reference for each endpoint (list effective limits, retrieve/create/delete a limit, list/retrieve/approve/deny increase requests). [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/7cd7a71d/docs-md/api/manage-claude/spend-limits-api.md?plain=1#L117)] [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]
