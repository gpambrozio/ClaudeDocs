# [Claude docs changes for June 13th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e)]

## Executive Summary
- Subagents can now spawn their own subagents (as of v2.1.172), enabling multi-level agent delegation with depth limits for background agents
- New Analytics APIs guide clarifies which of the two analytics APIs (Claude Code vs. Claude Enterprise) fits your organization and how to provision keys
- AWS region configuration for Bedrock is now optional if your AWS profile already sets a region, with a full resolution order including AWS config files
- The `availableModels` allowlist now covers subagents and the advisor tool (not just the main session), and matching now supports version prefixes and full model IDs
- New `CLAUDE_CODE_CHILD_SESSION` environment variable lets scripts reliably detect when they're running inside a Claude Code tool call or hook

## New Claude Code versions

### [2.1.176](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/versions/2.1.176.md)

#### New features

* Session titles are now generated in the language of your conversation; set the `language` setting to pin a specific language
* Added `footerLinksRegexes` setting for regex-matched link badges in the footer row, configurable via user or managed settings

#### Existing feature improvements

* Improved Bedrock credential caching: credentials from `awsCredentialExport` are now cached until their actual `Expiration` timestamp instead of a fixed 1 hour
* Background sessions now show clearer guidance when a window left open across an auto-update can't submit a reply, and `claude daemon status` explains version-skew behavior

#### Major bug fixes

* Fixed `availableModels` enforcement: alias model picks can no longer be redirected to a blocked model via `ANTHROPIC_DEFAULT_*_MODEL` environment variables, and `/fast` now refuses to toggle when it would switch to a blocked model
* Fixed auto mode failing on Fable 5 for organizations without Opus 4.8 enabled — the classifier now falls back to the best available Opus model
* Fixed hook `if` conditions for Read/Edit/Write tool paths: patterns like `Edit(src/**)`, `Read(~/.ssh/**)`, and `Read(.env)` now match correctly
* Fixed Linux sandbox failing to start when `.claude/settings.json` is a symlink with an absolute target
* Fixed `/copy` and mouse-selection copy not reaching the system clipboard inside tmux over SSH, and tmux paste buffer not loading on versions older than 3.2
* Fixed Remote Control connecting from web/mobile silently switching the session's model
* Fixed Remote Control disconnect notifications showing a bare numeric code instead of a human-readable reason, and connection failures adding a duplicate line to the transcript
* Fixed Remote Control sessions not disconnecting when you sign in to a different account
* Fixed `/cd` and worktree moves leaving the session reporting the previous directory's git branch
* Fixed `claude agents`: pressing back in one window no longer detaches other windows attached to the same session
* Fixed backgrounded sessions showing "Working" forever when `/bg` mid-turn had nothing left to continue
* Fixed background agent search by PR URL: PRs opened during scheduled wakeups or while a job was blocked now appear in `claude agents` search
* Fixed `claude --bg -cn <name>` not seeding the session name
* Fixed cloud sessions failing with "Could not resolve authentication method" when idle for too long before being claimed

-----

## Claude Code changes

### Changed documents

#### [Agent Loop](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* Updated `xhigh` effort level recommendation from "Opus 4.8 and Opus 4.7" to "Fable 5 and Opus 4.7+" [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L136)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#effort-level)]
* Expanded `error_max_structured_output_retries` description to cover model fallback retracting completed output as a second failure mode [[line 237](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L237)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#handle-the-result)]

#### [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/structured-outputs.md) [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs)]

* Added explanation that model fallbacks can retract completed structured output mid-stream, causing the same error as validation failures; advise checking `errors` text to distinguish the two causes [[line 216](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/structured-outputs.md?plain=1#L216)] [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs#example-todo-tracking-agent)]

#### [Subagents (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* As of v2.1.172, subagents can spawn their own subagents; foreground subagents can spawn at any depth, background subagents are limited to five levels deep; updated note and added pointer to full depth rules [[line 117](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L117)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#agentdefinition-configuration)]

#### [TypeScript SDK Reference](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* Added `skipMcpDiscovery` optional field to `SdkPluginConfig`; when `true`, the SDK loads plugin skills/hooks/agents/commands but skips reading its MCP server configuration [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L64)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#startup)]
* Added `auto-continuation` origin kind to `SDKMessageOrigin` for synthetic turns injected when a session continues without fresh user input [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#returns-2)]
* Added `resolvedModel` optional field on `AgentOutput` `completed` and `async_launched` variants, naming the model the subagent actually ran on; requires v2.1.174 [[line 2101](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L2101)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#tooloutputschemas)]

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* `AWS_REGION` is now optional as of v2.1.172; Claude Code resolves the region from `AWS_REGION`, `AWS_DEFAULT_REGION`, the active AWS profile, then `us-east-1` as a fallback; older versions still require `AWS_REGION` explicitly [[line 148](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/amazon-bedrock.md?plain=1#L148)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#3-configure-claude-code)]
* Added note that AWS GovCloud regions should use the `us-gov.` prefix in model IDs [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/amazon-bedrock.md?plain=1#L165)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#4-pin-model-versions)]

#### [Costs](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Added note that the VS Code extension shows the same usage breakdown as `/usage` via the Account & usage dialog with Day/Week toggle; requires v2.1.174 [[line 22](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/costs.md?plain=1#L22)] [[Source](https://code.claude.com/docs/en/costs#using-the-/usage-command)]

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Updated `CLAUDECODE` description: IDE extensions also set this in their integrated terminals; added guidance to use `CLAUDE_CODE_CHILD_SESSION` instead when you need to distinguish nested sessions [[line 211](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/env-vars.md?plain=1#L211)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Added new `CLAUDE_CODE_CHILD_SESSION` variable (v2.1.172): set to `1` in Bash/PowerShell tool calls, hook commands, and status line commands — not set in stdio MCP servers or IDE terminals, making it a reliable way to detect a direct tool subprocess [[line 225](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/env-vars.md?plain=1#L225)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Updated `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` with detailed explanation of when it takes effect (cloud sessions, Remote Control, Sonnet/Opus 4.6 models, and when `CLAUDE_CODE_AUTO_COMPACT_WINDOW` is set) [[line 217](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/env-vars.md?plain=1#L217)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Updated `CLAUDE_CODE_FORCE_SESSION_PERSISTENCE` — reinstated to override `CLAUDE_CODE_CHILD_SESSION` misclassification; clarified behavior across version ranges [[line 234](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/env-vars.md?plain=1#L234)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]
* Updated `CLAUDE_CODE_SCROLL_SPEED` to accept fractional values below 1 (e.g., `0.5`) to slow accelerated trackpad scrolling [[line 243](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/env-vars.md?plain=1#L243)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [Errors](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Added "Could not resolve authentication method" to the error navigation table and added a new section explaining it — affects background, cloud, and SDK sessions; upgrade to v2.1.174 to fix the idle worker variant [[line 255](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/errors.md?plain=1#L255)] [[Source](https://code.claude.com/docs/en/errors#not-logged-in)]
* Added note for the 1M context entitlement error: Claude Code now auto-compacts when context exceeds 200K and keeps the session at that limit; v2.1.171 and earlier required `/clear` to recover [[line 263](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/errors.md?plain=1#L263)] [[Source](https://code.claude.com/docs/en/errors#could-not-resolve-authentication-method)]

#### [Fullscreen Rendering](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/fullscreen.md) [[Source](https://code.claude.com/docs/en/fullscreen)]

* Updated scroll speed documentation: `CLAUDE_CODE_SCROLL_SPEED` now accepts fractional values below 1 to slow trackpad acceleration [[line 308](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/fullscreen.md?plain=1#L308)] [[Source](https://code.claude.com/docs/en/fullscreen#research-preview)]
* Added note about `wheelScrollAccelerationEnabled` setting (v2.1.174): set to `false` for a constant scroll rate per wheel notch [[line 310](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/fullscreen.md?plain=1#L310)] [[Source](https://code.claude.com/docs/en/fullscreen#research-preview)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Clarified that `model` field in `SessionStart` hooks is not guaranteed to be present (e.g., after `/clear` or conversation recovery) — check for the field before reading it [[line 322](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/hooks.md?plain=1#L322)] [[Source](https://code.claude.com/docs/en/hooks#command-hook-fields)]
* Added `resolvedModel` field to `PostToolUse` Agent tool response (v2.1.174): names the actual model the subagent ran on, present on both `completed` and `async_launched` status variants [[line 340](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/hooks.md?plain=1#L340)] [[Source](https://code.claude.com/docs/en/hooks#command-hook-fields)]

#### [JetBrains](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/jetbrains.md) [[Source](https://code.claude.com/docs/en/jetbrains)]

* Rewrote installation instructions to clearly explain that the plugin does not bundle the CLI — both the CLI and the plugin must be installed separately; added note about setting the `claude` path if not on PATH [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/jetbrains.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/jetbrains#features)]

#### [Model Configuration](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Expanded `availableModels` enforcement: the allowlist now applies to the main session, subagent models, the advisor model, and fallback chains [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/model-config.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/model-config#restrict-model-selection)]
* Updated `opusplan` context window behavior: it now receives the same 1M context upgrade as `opus` on subscription tiers that auto-upgrade; the `opusplan[1m]` suffix works to force 1M for both plan and execute phases [[line 166](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/model-config.md?plain=1#L166)] [[Source](https://code.claude.com/docs/en/model-config#opusplan-model-setting)]
* Updated `availableModels` matching: now matches on alias, version prefix (e.g., `claude-opus-4-8`), or full model ID; `[1m]` suffix is stripped before matching [[line 469](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/model-config.md?plain=1#L469)] [[Source](https://code.claude.com/docs/en/model-config#prompt-caching-configuration)]

#### [Monitoring Usage](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Added `model` attribute to the `claude_code.lines_of_code.count` metric (v2.1.172), enabling per-model breakdown of code additions/removals [[line 482](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/monitoring-usage.md?plain=1#L482)] [[Source](https://code.claude.com/docs/en/monitoring-usage#active-time-counter)]
* Added `host_owned_mcp` field to `plugin_loaded` event (v2.1.172): `true` when the SDK host manages the plugin's MCP connections [[line 490](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/monitoring-usage.md?plain=1#L490)] [[Source](https://code.claude.com/docs/en/monitoring-usage#event-correlation-attributes)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified glob pattern behavior: `*` matches within a single path segment and can appear at any position, while `**` matches across directories [[line 534](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/permissions.md?plain=1#L534)] [[Source](https://code.claude.com/docs/en/permissions#see-also)]
* Added comprehensive WebFetch domain matching rules: `*` as a leading `*.` matches subdomains at any depth; `WebFetch(domain:*)` matches every domain; exact rules take precedence over wildcards [[line 543](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/permissions.md?plain=1#L543)] [[Source](https://code.claude.com/docs/en/permissions#see-also)]

#### [Plugin Hints](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/plugin-hints.md) [[Source](https://code.claude.com/docs/en/plugin-hints)]

* Added `CLAUDE_CODE_CHILD_SESSION` (v2.1.172) as an alternative to `CLAUDECODE` for gating plugin hint emission; explains trade-offs: `CLAUDECODE` has broader reach, `CLAUDE_CODE_CHILD_SESSION` is less likely to appear in human terminals [[line 562](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/plugin-hints.md?plain=1#L562)] [[Source](https://code.claude.com/docs/en/plugin-hints#see-also)]

#### [Remote Control](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* As of v2.1.172, the Remote Control footer indicator reads `/rc active` (shortened) and is hidden when the terminal is too narrow; earlier versions always showed `Remote Control active` [[line 61](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/remote-control.md?plain=1#L61)] [[Source](https://code.claude.com/docs/en/remote-control#start-a-remote-control-session)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated `availableModels` description to mention subagents and the advisor tool (not just the main session) [[line 621](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/settings.md?plain=1#L621)] [[Source](https://code.claude.com/docs/en/settings#enabledplugins)]
* Added `wheelScrollAccelerationEnabled` setting (v2.1.174): controls whether scroll speed accelerates during fast scrolling; default `true` [[line 629](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/settings.md?plain=1#L629)] [[Source](https://code.claude.com/docs/en/settings#enabledplugins)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added new "Spawn nested subagents" section (v2.1.172): subagents can now spawn their own subagents; foreground subagents can spawn at any depth, background subagents are capped at depth 5; subagent panel shows the full tree with descendant counts [[line 678](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/sub-agents.md?plain=1#L678)] [[Source](https://code.claude.com/docs/en/sub-agents#isolate-high-volume-operations)]
* Removed `Agent` from the list of tools unavailable to subagents — subagents can now use the Agent tool to spawn children [[line 285](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/sub-agents.md?plain=1#L285)] [[Source](https://code.claude.com/docs/en/sub-agents#available-tools)]
* Updated `/agents` Running tab description: now lists both live and recently finished subagents [[line 145](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/sub-agents.md?plain=1#L145)] [[Source](https://code.claude.com/docs/en/sub-agents#configure-subagents)]

#### [VS Code](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Added new "Check account and usage" section: `/usage` opens an Account & usage dialog with plan, usage bars, and attribution tables for skills/subagents/plugins/MCP servers; includes Day/Week toggle; requires v2.1.174 [[line 118](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/claude-code/vs-code.md?plain=1#L118)] [[Source](https://code.claude.com/docs/en/vs-code#resume-cloud-sessions-from-claude-ai)]

-----

## API changes

### New Documents

#### [Analytics APIs](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/analytics-api)]

New guide explaining the two analytics APIs: the **Claude Code Analytics API** (uses an Admin API key, reports Claude Code productivity metrics for Claude Platform organizations) and the **Claude Enterprise Analytics API** (uses an Analytics API key created in claude.ai, reports organization-wide engagement, adoption, and cost data for Claude Enterprise organizations). Includes a comparison table, step-by-step instructions for provisioning each key type, and a summary of what each API covers.

### Changed documents

#### [C# Beta: File Upload](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/api/csharp/beta/files/upload.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/files/upload)]

* Page was previously a "Console temporarily unavailable" placeholder; now contains full C# SDK reference for the `Beta.Files.Upload` method including parameters, return type, and example code

#### [C# Beta: Delete a Memory](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/api/csharp/beta/memory_stores/memories/delete.md) [[Source](https://platform.claude.com/docs/en/api/csharp/beta/memory_stores/memories/delete)]

* Page was previously a "Console temporarily unavailable" placeholder; now contains full C# SDK reference for `Beta.MemoryStores.Memories.Delete` including parameters, return type, and example code

#### [Claude Code Analytics API](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/claude-code-analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)]

* Added callout noting that Claude Enterprise organizations should use the Claude Enterprise Analytics API (with an Analytics API key) for claude.ai users; links to the new Analytics APIs guide [[line 26](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/claude-code-analytics-api.md?plain=1#L26)] [[Source](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)]

#### [Compliance API Access](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/compliance-api-access.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

* Updated Analytics API key row in the key types table to link to the new Analytics APIs guide instead of the external support article [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/compliance-api-access.md?plain=1#L18)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-api-access)]

#### [Self-Hosted Sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Added GKE Agent Sandbox to the list of platform-specific guides for managed agent sandboxes [[line 31](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L31)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

#### [Usage and Cost API](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

* Added "Which API do you need?" section with a table distinguishing Claude Console (Admin API key) vs. Claude Enterprise (Analytics API key) for usage and cost reporting; links to the new Analytics APIs guide [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/usage-cost-api.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

#### [WIF Providers: Azure](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/wif-providers/azure.md) [[Source](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure)]

* Clarified that `aud` claim behavior differs between Azure Entra v1 and v2 tokens: v2 tokens carry the application client ID (GUID), while v1 tokens carry the resource identifier passed when fetching the token [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/9462f8cc5a5e20e84b5c3b1e740e6ff05000ef1e/docs-md/api/manage-claude/wif-providers/azure.md?plain=1#L56)] [[Source](https://platform.claude.com/docs/en/manage-claude/wif-providers/azure)]
