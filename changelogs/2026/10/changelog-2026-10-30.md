# [Claude docs changes for October 30th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/4457c5b8ca41301c5c7350604da55c2a1988eae3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/4457c5b8ca41301c5c7350604da55c2a1988eae3)]

## Executive Summary
- New beta **Usage and Cost Analytics API** (`/v1/organizations/analytics/usage` and `/cost`) covers Console and Enterprise organizations. The older Usage and Cost API and the Enterprise `usage_report`/`cost_report` endpoints are now legacy.
- Claude Code **2.1.314** adds `permissions.blockWritesOutsideWorkingDirectories`, per-group routing and Bedrock guardrail tracing for the Claude apps gateway, and idle compaction in VS Code and Desktop. It also includes many fixes.
- The API **Beta** reference gained a large set of new endpoint pages: Agents, Deployments, Dreams, Environments, Memory Stores, Federation, MCP Tunnels and Plugins.
- Fable 5.1 **preserved thinking** docs were rewritten: append-only history rules, which edits invalidate thinking blocks, and the `prefix_mismatch_behavior` options (`error` or `drop_block`).
- Claude Code docs add the `/restart` command, a clarified effort-level resolution order, and details on how PreToolUse `ask` hooks behave in auto mode.

## New Claude Code versions

### [2.1.314](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/versions/2.1.314.md)

#### New features

* Added `permissions.blockWritesOutsideWorkingDirectories`: Write, Edit and NotebookEdit refuse paths outside the working directories in every permission mode
* Added an optional `groups` list to Claude apps gateway upstreams, so only developers in the listed IdP groups are sent to that upstream
* Added `guardrail_trace` to Claude apps gateway Bedrock upstreams, to log which Amazon Bedrock guardrail filter fired
* Added idle compaction to VS Code and Claude Desktop's Code tab: a 200K+ token conversation left idle is summarized, and the summary is used on the next message if the prompt cache has expired
* Cloud sessions: scheduled tasks run in Anthropic's cloud now load the plugins enabled on your claude.ai account, and the Scheduled tasks page has an "Include completed" button
* Claude Tag: added a dismissible link to the Claude Tag API docs in admin settings

#### Existing feature improvements

* Idle compaction now also runs for subscribers with telemetry off, and on Bedrock, Vertex, Foundry and LLM gateways once the one-hour prompt cache is on
* Flagged requests now retry on another model instead of ending in a refusal when settings leave only an older Opus model, or none
* Auto mode blocked-call messages now name the command and point to `/permissions`, whose review tab is now called "Recently blocked"
* Hook `if` conditions such as `Monitor(tail *)` now match the Monitor tool's shell commands the way `Bash(tail *)` matches Bash
* File tools now ask before editing the local copy of server-managed settings
* `/ultrareview` checks workspace trust before running git
* Session auto-titles now work for sessions that start with a skill or prompt-based command
* Ctrl+R prompt history search matches text inside collapsed `[Pasted text]` pills
* Lower memory use in long headless and SDK turns with many subagents, faster `--resume` on damaged transcripts, and faster `/context` with very many MCP tools
* `FORCE_HYPERLINK=false` now turns hyperlinks off instead of on
* Skills and plugins `.trash` folders are now capped at about 1024 entries

#### Major bug fixes

* Fixed sessions failing repeatedly with "Invalid effort level" when an admin caps a model's effort; Claude Code now lowers the effort and retries
* Fixed `claude -p` exiting 0 with no output when startup failed
* Fixed Bedrock sessions with many images failing every turn and `/compact` failing with "400 Input is too long."
* Fixed Microsoft Foundry sessions failing when the resource has no deployment for the default model; falls back to an older model
* Fixed requests failing when a gateway or provider rejects a beta header or `tool_reference` blocks; the request is retried without them
* Fixed TLS `UNABLE_TO_GET_ISSUER_CERT` errors with cross-signed renewed root certificates
* Fixed `forceRemoteSettingsRefresh` not applying once the stored copy had expired
* Fixed "Continue automatically at usage limit" continuing more than three times without a prompt
* Fixed a PreCompact hook with very large output breaking compaction; output is now cut at 10,000 characters
* Fixed sandbox protections not applying to a worktree entered by `claude -p --resume` or `--continue`
* Fixed `--setting-sources` exclusions still supplying some settings
* Fixed dotted model IDs such as `claude-opus-4.8` behind a gateway being treated as an older model
* Fixed Bash-matching hooks not running on shell commands started by the Monitor tool

-----

## Claude Code changes

### Changed documents

#### [chrome](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* New section explaining the "Claude in Chrome extension detected" startup dialog. Answering Yes turns on **Enabled by default**, and No or Esc turns it off. [[lines 106-114](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/chrome.md?plain=1#L106-L114)] [[Source](https://code.claude.com/docs/en/chrome#answer-the-startup-dialog)]

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* New `/restart` command (alias `/update`) restarts Claude Code and resumes the session to apply an installed update. It needs a Pro or Max plan and a native install on macOS or Linux. [[line 129](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/commands.md?plain=1#L129)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [deep-links](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/deep-links.md) [[Source](https://code.claude.com/docs/en/deep-links)]

* The `claude-cli://` handler is now registered when you send anything to an interactive session, or when you start agent view in a trusted folder. [[lines 147-152](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/deep-links.md?plain=1#L147-L152)] [[Source](https://code.claude.com/docs/en/deep-links#registration-and-supported-platforms)]

#### [desktop-changelog](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/desktop-changelog.md) [[Source](https://code.claude.com/docs/en/desktop-changelog)]

* New "Restrict sign-in to your organization" section covers the Claude Desktop `forceLoginOrgUUID` policy key (v1.2581.0+). [[lines 1929-1946](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/desktop-changelog.md?plain=1#L1929-L1946)] [[Source](https://code.claude.com/docs/en/desktop-changelog#restrict-sign-in-to-your-organization)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* Disabling update fetching also stops `/restart` on Pro and Max plans. [[line 574](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/env-vars.md?plain=1#L574)] [[Source](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)]

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* The `effort.level` hook input field now reflects the effort setting, including skill, subagent and `ultrathink` levels. [[line 734](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/hooks.md?plain=1#L734)] [[Source](https://code.claude.com/docs/en/hooks#common-input-fields)]
* WebSearch tool input documents the new `mode` field (`standard` or `extended`), which needs v2.1.282+. [[line 1897](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/hooks.md?plain=1#L1897)] [[Source](https://code.claude.com/docs/en/hooks#websearch)]
* New "PreToolUse `ask` decisions in auto mode" section. Calls that Claude Code's own checks also flag can be denied by the classifier. `SubagentHandback` calls show no prompt, and a hook can return `deny` to stop them. [[lines 1986-1994](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/hooks.md?plain=1#L1986-L1994)] [[Source](https://code.claude.com/docs/en/hooks#pretooluse-ask-decisions-in-auto-mode)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* The effort resolution order is now five steps: the env var, then an in-session pick, then `--effort`, then settings, then the model default. [[lines 606-610](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/model-config.md?plain=1#L606-L610)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]
* Clarified that a new effort level picked in `/model` starts with the next message at the latest. [[line 688](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/model-config.md?plain=1#L688)] [[Source](https://code.claude.com/docs/en/model-config#set-the-effort-level)]
* Clarified how long a skill's or subagent's frontmatter `effort` applies. [[line 695](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/model-config.md?plain=1#L695)] [[Source](https://code.claude.com/docs/en/model-config#set-the-effort-level)]

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* `denyWrite` entries containing glob characters are now also enforced when a folder before the first glob character is a symlink. [[line 564](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/claude-code/sandboxing.md?plain=1#L564)] [[Source](https://code.claude.com/docs/en/sandboxing#denied-paths-that-pass-through-a-symlink)]

-----

## API changes

### New Documents

#### [usage-cost-analytics-api](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/manage-claude/usage-cost-analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-analytics-api)]

Describes the beta Usage and Cost Analytics API, which needs the `anthropic-beta: analytics-usage-cost-2026-08-24` header. `GET /v1/organizations/analytics/usage` returns token and request counts, and `GET /v1/organizations/analytics/cost` returns USD cost. Results can be filtered and grouped by model, workspace, API key, service tier or the user or service account behind a request, in daily, hourly or per-minute buckets. It covers authentication for Console (Admin API key or OAuth `org:admin`) and Enterprise organizations, SDK and `ant` CLI examples, and a migration guide from the legacy Usage and Cost API.

### Changed documents

#### [api/beta](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* The Beta API reference expanded substantially. It adds pages for Agents, Deployments and deployment runs, Dreams, Environments and work, Files, Memory Stores, Organization Federation (issuers and rules), MCP Tunnels, Plugins and plugin marketplaces, plus the analytics usage and cost endpoints.

#### [manage-claude/usage-cost-api](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/manage-claude/usage-cost-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/usage-cost-api)]

* The page is now marked as a legacy API that remains supported, with a pointer to the new Usage and Cost Analytics API.

#### [manage-claude/workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* The Default Workspace now has a `wrkspc_` ID that matches `workspace_id` in the new analytics API rows. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/manage-claude/workspaces.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces#how-workspaces-work)]
* The workspace usage tracking example was rewritten for the new analytics API, with CLI, Python, TypeScript, C# and Go samples. [[lines 1004-1160](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/manage-claude/workspaces.md?plain=1#L1004-L1160)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces#usage-and-cost-tracking)]

#### [models/fable-5-1/whats-new-fable-5-1](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)]

* The preserved thinking section was rewritten. A thinking block stays valid only while everything before it is unchanged, on Fable 5.1 and Mythos 5.1. The page lists which edits invalidate later blocks and which keep them valid. `prefix_mismatch_behavior` (`error` or `drop_block`, beta header `thinking-binding-controls-2026-08-01`) is also explained. [[lines 64-90](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/models/fable-5-1/whats-new-fable-5-1.md?plain=1#L64-L90)] [[Source](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1#editing-earlier-turns-invalidates-thinking-blocks)]

#### [models/fable-5-1/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/models/fable-5-1/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)]

* The history-editing check was reworked into a three-step integration check for append-only conversation history.

#### [about-claude/models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* New DeepResearch Bench II measurements and charts: caching cuts Fable 5.1 cost per task from $40.58 to $5.64, and effort sweeps for Fable 5.1 run from `low` to `high`. [[lines 66-68](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L66-L68)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#why-caching-comes-first)]
* The model upgrade table was rebuilt with SWE-bench Pro, Terminal-Bench 3 and Managed Agents results. [[lines 401-415](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md?plain=1#L401-L415)] [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence#upgrade-the-model)]
* Added guidance on pricing a task from the five `usage` token counts, and on how breaking the prompt prefix inflates cost. Rewriting an earlier tool result on Claude 5.1+ invalidates later thinking blocks.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* October 29: launch of the Usage and Cost Analytics API beta, and the legacy status of the older usage and cost APIs. October 28: the maximum Messages and Token Counting request size on the first-party API was raised from 32 MB to 128 MB. [[lines 15-23](https://github.com/gpambrozio/ClaudeDocs/blob/4457c5b8ca41301c5c7350604da55c2a1988eae3/docs-md/api/release-notes/overview.md?plain=1#L15-L23)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-29-2026)]
