# [Claude docs changes for October 27th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/98e885a80b5a5c1f72b580f3e271f3e6c190650c) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/98e885a80b5a5c1f72b580f3e271f3e6c190650c)]

## Executive Summary
- Claude Code 2.1.311 adds `ultrathink` as a real xhigh-effort trigger, a long list of stability fixes (startup freezes, MCP and subagent issues, compaction) and new self-hosted runner flags for holding idle sessions.
- The Agent SDK gets per-tool approval policies for custom tools (`always_ask` / `always_deny`) and the ability to add plugins to a running session with `reloadPlugins({ addPlugins })`. The permissions docs were rewritten to match.
- Permission docs now cover the "Dangerous rm operation not ruled out" prompt, with time limits and denials for critical-path removals in `auto` and `bypassPermissions` modes, plus a new `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT` variable.
- Managed Agents self-hosted sandboxes now support macOS hosts, with a step-by-step guide for preparing `/mnt/memory`.
- The Best practices guide was substantially rewritten and reorganized, and the Claude Security plugin gained scan effort levels.

## New Claude Code versions

### [2.1.311](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/versions/2.1.311.md)

#### New features

* Added `--hold-idle-file` and `--max-hold-min` to `self-hosted-runner` to keep an idle session while the host reports processes it left running
* `ultrathink` typed in the interactive terminal now runs its turn at xhigh effort on Opus 5.5, Sonnet 5.5, Haiku 5.5 and Fable 5.1 through Anthropic's API, and the rainbow highlight only appears where it can take effect
* [VSCode] Syntax coloring for code blocks in Claude's replies, and a "Running UserPromptSubmit hooks" spinner and screen reader announcement
* [Claude Tag] New Skills view in Claude Tag analytics showing how often each attached skill runs in Slack channels

#### Existing feature improvements

* Faster startup for Pro and Max accounts and for launches whose only arguments are options
* Compaction now usually asks again for the summary when the model's reply lacks one
* Shell commands that hit their timeout now show the output so far and say the command is still running in the background
* `/teleport` warns when a compacted cloud session loads from its last compaction
* Clearer messages when a background session's process exits, on "Connection dropped" API errors and on refused sign-in codes
* Artifact tool better distinguishes artifact pages from documents; multi-view artifacts route on the link's `#name`
* Model names and IDs drop the `[1m]` suffix where it has no effect (the suffix is still accepted)
* Claude Code on Bedrock, Mantle, Vertex and Foundry loads model settings from a signed file on downloads.claude.ai (disable with `CLAUDE_CODE_MODEL_CATALOG=off`)
* `DISABLE_COMPACT` in settings files and in a mod's `$.env.set` can now only turn compaction off
* `--output-format json` / `stream-json` escape DEL, C1 control and Unicode format characters as `\uXXXX`
* Ctrl+D in agent view now matches the prompt: on empty input, press twice to exit
* [VSCode] Sessions start with `DISABLE_TELEMETRY` set while VS Code's telemetry setting is off
* [Claude Tag] Routines with nothing to report can end without posting a message
* [Code Review] Transient session start failures are retried once automatically

#### Major bug fixes

* Fixed long freezes at startup and after file reads/edits when CLAUDE.md contains a very long list item
* Fixed interrupts not taking effect while an MCP server hadn't answered a resource read or a skill was downloading
* Fixed standard-context sessions stopping with "Usage credits required for 1M context"; Claude Code now compacts and continues
* Fixed Write and Edit stalling up to 5 seconds and reporting 0 lines changed on very large edits
* Fixed subagents being unable to use MCP tools from servers that connect after the subagent starts
* Fixed stale MEMORY.md and CLAUDE.md content after automatic compaction
* Fixed `claude -p` and SDK sessions saving transcript messages out of order
* Fixed `SubagentStop` hooks firing repeatedly for running subagents instead of once at the end
* Fixed a subagent's worktree being removed while its background subagent was still using it
* Fixed Claude Code retrying requests the API marked not to retry, which could hold a turn indefinitely
* Fixed agent teams sessions showing an empty task list after `--resume` / `--continue`
* Fixed Cowork cloud sessions losing connectors and tools after a restart when a plugin or setting named an `agent`
* Fixed pasted text mentioning an image path attaching the image and dropping the path
* Fixed `DISABLE_COMPACT` being ignored by agent teammates and the rewind menu
* Fixed `/mcp` authentication status being wrong for remote servers

-----

## Claude Code changes

### New Documents

None.

### Changed documents

#### [agent-sdk/agent-loop](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/agent-loop.md) [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop)]

* The `dontAsk` and `bypassPermissions` mode descriptions now note calls that still reach `canUseTool` or are denied, such as network-path reads. [[lines 232-234](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/agent-loop.md?plain=1#L232-L234)] [[Source](https://code.claude.com/docs/en/agent-sdk/agent-loop#permission-mode)]

#### [agent-sdk/custom-tools](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/custom-tools.md) [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools)]

* New "Require approval for specific tools" section: set a tool's `permission_policy` to `always_ask` or `always_deny` (TypeScript SDK) on the config returned by `createSdkMcpServer()`. [[lines 377-403](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L377-L403)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#require-approval-for-specific-tools)]
* Set `destructiveHint: true` on `always_ask` tools so the auto mode classifier doesn't approve them. [[line 322](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/custom-tools.md?plain=1#L322)] [[Source](https://code.claude.com/docs/en/agent-sdk/custom-tools#add-tool-annotations)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Documents calls that no allow rule approves: `AskUserQuestion`, org-`ask` connector tools, `always_ask` custom tools, network-path reads and critical-path removals. [[lines 97-110](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L97-L110)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)]
* Clarified how deny rules, `always_deny` policies, `bypassPermissions` and `plan` mode interact with `canUseTool`. [[lines 23-50](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L23-L50)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)]
* Documented the `CLAUDE_SDK_CAN_USE_TOOL_SHADOWED` warning. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L69)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#how-permissions-are-evaluated)]
* `dontAsk` mode lists the calls denied even when an allow rule matches; `touch` with options or prefixes is no longer auto-approved in `acceptEdits`. [[lines 269-287](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L269-L287)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#accept-edits-mode-acceptedits)]

#### [agent-sdk/plugins](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/plugins.md) [[Source](https://code.claude.com/docs/en/agent-sdk/plugins)]

* New "Add plugins to a running session" section using `reloadPlugins({ addPlugins })`. [[lines 67-82](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/plugins.md?plain=1#L67-L82)] [[Source](https://code.claude.com/docs/en/agent-sdk/plugins#add-plugins-to-a-running-session)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* `reloadPlugins()` gains an `addPlugins` option, with a troubleshooting section for when folders don't load. [[lines 1135-1167](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1135-L1167)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#load-more-plugin-folders-with-addplugins)]
* `McpSdkServerConfigWithInstance` gains a `tools` list of the new `McpServerToolPolicy` type (`permission_policy`: `always_allow` / `always_ask` / `always_deny`), changeable mid-session through `setMcpServers()`. Requires SDK v0.3.301+ and Claude Code v2.1.301+. [[lines 1463-1562](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L1463-L1562)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#mcpsdkserverconfigwithinstance)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Peek panel shows how long a session has waited on you, and a safe-mode indicator for `claude --bg --safe-mode`. [[lines 205-209](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-view.md?plain=1#L205-L209)] [[Source](https://code.claude.com/docs/en/agent-view#peek-and-reply)]
* Explains which in-flight work carries over when you background a session (shell commands, subagents, `/loop` tasks), which continues only when Claude relaunches it (dynamic workflows) and which stops (monitors). [[lines 470-495](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/agent-view.md?plain=1#L470-L495)] [[Source](https://code.claude.com/docs/en/agent-view#what-carries-over-when-you-background)]

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Largely rewritten and reorganized. New sections cover deterministic vs. non-deterministic instructions, what Claude can't see, writing specific prompts, a short CLAUDE.md, scoped rules, team skills, review against a spec, Stop-hook checks, enforcing rules with hooks/permissions/sandbox, changing defaults, subagent costs, running without you (scripts, schedules, parallel sessions). [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/best-practices.md?plain=1#L1)] [[Source](https://code.claude.com/docs/en/best-practices#best-practices-for-claude-code)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* Clarified that `serve_to_desktop` is a legacy key with no effect when Desktop uses `bootstrapUrl`, and how to silence the boot warning. [[line 926](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L926)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#choose-cli-or-code)]
* New "Test a policy before deployment" section using a throwaway Postgres database. [[line 1007](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-apps-gateway-config.md?plain=1#L1007)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config#test-a-policy-before-deployment)]

#### [claude-apps-gateway-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-apps-gateway-deploy.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy)]

* Troubleshooting entry for `auth.denied` / `invalid_token` on `/v1/logs` and `/v1/metrics` when `otelHeadersHelper` is set in managed settings. [[line 392](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-apps-gateway-deploy.md?plain=1#L392)] [[Source](https://code.claude.com/docs/en/claude-apps-gateway-deploy#troubleshooting)]

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* New "Plugin suggestions in the conversation" section: Claude can suggest plugins with an Add button; deny `SearchPlugins` and `SuggestPluginInstall` to turn it off. [[lines 287-308](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L287-L308)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#plugin-suggestions-in-the-conversation)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* Transcripts can also hold the system prompt, tool definitions, request parameters and loaded instruction files; subagent transcripts are listed. [[lines 102-117](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-directory.md?plain=1#L102-L117)] [[Source](https://code.claude.com/docs/en/claude-directory#application-data)]

#### [claude-security](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-security.md) [[Source](https://code.claude.com/docs/en/claude-security)]

* New "Choose a scan effort" section (`low`, `medium` default, `high`). [[lines 100-111](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-security.md?plain=1#L100-L111)] [[Source](https://code.claude.com/docs/en/claude-security#choose-a-scan-effort)]
* Scans can target only a set of changes (branch, PR or commit diff); a revision stamp file records scan details; new "Update the plugin" section. [[lines 5-7](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/claude-security.md?plain=1#L5-L7)] [[Source](https://code.claude.com/docs/en/claude-security#scan-your-codebase-for-vulnerabilities)]

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Worktree can be enabled with third-party providers and set as default for saved local or SSH environments. [[lines 400-403](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/desktop.md?plain=1#L400-L403)] [[Source](https://code.claude.com/docs/en/desktop#run-a-session-in-its-own-worktree)]
* Switch sessions with Ctrl+Tab / Ctrl+Shift+Tab; diff comments are added via the "+" beside a line number. [[lines 165-283](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/desktop.md?plain=1#L165-L283)] [[Source](https://code.claude.com/docs/en/desktop#review-changes-with-diff-view)]

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New `CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF` and `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT`. [[lines 235-241](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/env-vars.md?plain=1#L235-L241)] [[Source](https://code.claude.com/docs/en/env-vars#variables)]

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* New section for MCP servers on Java MCP SDK 0.17.0 or older rejecting the elicitation capability; fix with `"bareElicitationCapability": true` or upgrading the SDK. [[lines 3473-3503](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/errors.md?plain=1#L3473-L3503)] [[Source](https://code.claude.com/docs/en/errors#mcp-server-rejected-the-elicitation-capability)]
* `claude rm <id> --discard-unpushed` documented for sessions whose worktree has unpushed commits. [[line 5114](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/errors.md?plain=1#L5114)] [[Source](https://code.claude.com/docs/en/errors#worktree-has-commits-that-are-not-pushed-anywhere)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Hooks can't loosen calls to Agent SDK tools marked `always_ask`. [[line 628](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/hooks-guide.md?plain=1#L628)] [[Source](https://code.claude.com/docs/en/hooks-guide#structured-json-output)]

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* New `attachSelection` (v2.1.300+) and `attachOpenFile` (v2.1.271+) settings to keep selected text and the open file out of messages; also apply in the integrated terminal. [[lines 225-250](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/ide-integrations.md?plain=1#L225-L250)] [[Source](https://code.claude.com/docs/en/ide-integrations#automatic-context-from-your-selection-and-open-file)]
* Section reorganization; new sections for reading specific PDF pages and including `@terminal:name` output. [[lines 202-210](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/ide-integrations.md?plain=1#L202-L210)] [[Source](https://code.claude.com/docs/en/ide-integrations#read-specific-pages-of-a-pdf)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New "Elicitation modes Claude Code declares" section for MCP server authors. [[line 1623](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/mcp.md?plain=1#L1623)] [[Source](https://code.claude.com/docs/en/mcp#elicitation-modes-claude-code-declares)]

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* `ultrathink` can raise a turn to `xhigh` effort in the terminal (v2.1.311+), with troubleshooting for when the rainbow doesn't appear. [[lines 673-679](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/model-config.md?plain=1#L673-L679)] [[Source](https://code.claude.com/docs/en/model-config#use-ultrathink-for-one-off-deep-reasoning)]
* New sections on checking the effort level you set and when a new level takes effect (queueing a message while Claude works); `/effort auto` clears the saved level. [[lines 685-709](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/model-config.md?plain=1#L685-L709)] [[Source](https://code.claude.com/docs/en/model-config#set-the-effort-level)]

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* New "The `Dangerous rm operation not ruled out` prompt" section; no allow rule or hook approves it. [[lines 846-861](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/permission-modes.md?plain=1#L846-L861)] [[Source](https://code.claude.com/docs/en/permission-modes#the-dangerous-rm-operation-not-ruled-out-prompt)]
* Time limits and denials for critical-path removals in `auto` and `bypassPermissions` modes (v2.1.281+), per surface, with `CLAUDE_CODE_DISABLE_DANGEROUS_RM_TIMEOUT` to change it. [[lines 918-955](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/permission-modes.md?plain=1#L918-L955)] [[Source](https://code.claude.com/docs/en/permission-modes#critical-path-removals-in-each-permission-mode)]
* `acceptEdits`: `touch` with options, globs or prefixes still prompts. Files passed via `--settings`, `--mcp-config` or `--agents` are protected. [[lines 264-271](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/permission-modes.md?plain=1#L264-L271)] [[Source](https://code.claude.com/docs/en/permission-modes#auto-approve-file-edits-with-acceptedits-mode)]
* Auto mode is available in cloud sessions in Anthropic-hosted environments. [[line 369](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/permission-modes.md?plain=1#L369)] [[Source](https://code.claude.com/docs/en/permission-modes#server-side-classifier-review)]

#### [plugins/mods/gallery](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/gallery.md) [[Source](https://code.claude.com/docs/en/plugins/mods/gallery)]

* `Input` accepts a `rows` prop for multi-line fields (Enter submits, backslash+Enter or Shift+Enter adds a line). [[lines 245-290](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/gallery.md?plain=1#L245-L290)] [[Source](https://code.claude.com/docs/en/plugins/mods/gallery#input)]

#### [plugins/mods/reference](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/reference.md) [[Source](https://code.claude.com/docs/en/plugins/mods/reference)]

* New limits table rows: string lengths, nesting depth 32, 20,000 elements, 262,144 `Raster` cells, 2 MiB of images. [[lines 371-377](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/reference.md?plain=1#L371-L377)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#limits)]
* Step names and `size`/`weight`/`mono`/`tabular` require v2.1.299+. [[lines 332-355](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/reference.md?plain=1#L332-L355)] [[Source](https://code.claude.com/docs/en/plugins/mods/reference#box-spacing-steps)]

#### [plugins/mods/troubleshoot](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/troubleshoot.md) [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot)]

* Expanded guidance for invalid `ui.render` trees, with example messages and a new "A `ui.render` line says `refused`" section. [[lines 225-247](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/troubleshoot.md?plain=1#L225-L247)] [[Source](https://code.claude.com/docs/en/plugins/mods/troubleshoot#another-mods-band-shows-and-yours-doesnt)]

#### [plugins/mods/interface](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/interface.md) [[Source](https://code.claude.com/docs/en/plugins/mods/interface)]

* Invalid-tree failure example and `Input` `rows` / scrolling key behavior. [[lines 420-545](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/interface.md?plain=1#L420-L545)] [[Source](https://code.claude.com/docs/en/plugins/mods/interface#build-a-tree-from-elements)]

#### [plugins/mods/test](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/test.md) [[Source](https://code.claude.com/docs/en/plugins/mods/test)]

* Test handle `input()` supports multi-line text for `rows` fields and `kind: 'change'`. [[line 311](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/mods/test.md?plain=1#L311)] [[Source](https://code.claude.com/docs/en/plugins/mods/test#test-a-drawing)]

#### [plugins/org](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/org.md) [[Source](https://code.claude.com/docs/en/plugins/org)]

* `disableSideloadFlags` now also covers the Agent SDK `plugins` option, `CLAUDE_CODE_PLUGIN_DIRS`, `--mcp-config` and more; cloud plugin suggestions note. [[lines 181-362](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/org.md?plain=1#L181-L362)] [[Source](https://code.claude.com/docs/en/plugins/org#control-matrix)]

#### [plugins/relevance](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/relevance.md) [[Source](https://code.claude.com/docs/en/plugins/relevance)]

* Terminal suggestions from a marketplace appear only after an admin allowlists it in managed settings. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/plugins/relevance.md?plain=1#L7)] [[Source](https://code.claude.com/docs/en/plugins/relevance#recommend-plugins-for-your-org)]

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* New "Keep an idle session while its processes run" guide for `--hold-idle-file` and `--max-hold-min`. [[lines 731-775](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L731-L775)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#keep-an-idle-session-while-its-processes-run)]
* Guidance on idle sessions holding runner slots and using `--release-idle-session-min`; package-registry mirror added to network host requirements. [[lines 67-725](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/self-hosted-environments-deploy.md?plain=1#L67)] [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy#network-requirements)]

#### [self-hosted-environments-reference](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/self-hosted-environments-reference.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-reference)]

* Runner CLI flag reference updated for the new hold-idle flags.

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Mirrors the ide-integrations changes: selection/open-file context controls, PDF page reading, `@terminal` references.

#### [workflows](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Notes on resuming a workflow after leaving or backgrounding the session.

-----

## API changes

### New Documents

None.

### Changed documents

#### [api/completions](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/api/completions.md) [[Source](https://platform.claude.com/docs/en/api/completions)]

* Text Completions prompt-format examples now show `\n\nHuman:` and `\n\nAssistant:` inline instead of broken line-wrapped text (same fix across all SDK language variants). [[lines 252-278](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/api/completions.md?plain=1#L252-L278)] [[Source](https://platform.claude.com/docs/en/api/completions#body-parameters)]

#### [build-with-claude/preserved-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/build-with-claude/preserved-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking)]

* The API can drop a thinking block produced by another account no longer in good standing; the request still succeeds. Applies to Fable, Mythos, Opus 5, Opus 5.5, Sonnet 5.5 and Haiku 5.5. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L76)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#thinking-blocks-stay-with-the-account-that-produced-them)]
* Removed the Claude API skill automation prompt; the check is now described as a manual procedure. [[line 439](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/build-with-claude/preserved-thinking.md?plain=1#L439)] [[Source](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking#check-whether-your-code-edits-the-prefix)]

#### [manage-claude/access-transparency](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/access-transparency.md) [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency)]

* Turning the Compliance API off stops access to Access Transparency events, not their recording. [[line 75](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/access-transparency.md?plain=1#L75)] [[Source](https://platform.claude.com/docs/en/manage-claude/access-transparency#receiving-access-transparency-events)]

#### [manage-claude/api-and-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Claude in Microsoft Foundry is now HIPAA-eligible with a BAA plus the HIPAA configuration enabled on the Azure subscription; only Claude Platform on AWS remains unavailable. [[lines 57-64](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L57-L64)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention#what-hipaa-readiness-covers)]

#### [manage-claude/claude-tag-api](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/claude-tag-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/claude-tag-api)]

* Bundle target examples updated to a typed `target` object (`slack_channel` / `slack_workspace`) across CLI and SDKs; C# and Java examples fixed. [[lines 1920-2160](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/claude-tag-api.md?plain=1#L1920-L2160)] [[Source](https://platform.claude.com/docs/en/manage-claude/claude-tag-api#attach-a-bundle)]

#### [manage-claude/compliance-faq](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/compliance-faq.md) [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-faq)]

* Clarified Compliance API on/off behavior in Claude Console: events captured earlier are kept, recording resumes when turned back on, and the change is logged as `org_compliance_api_settings_updated`. [[lines 19-27](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/compliance-faq.md?plain=1#L19-L27)] [[Source](https://platform.claude.com/docs/en/manage-claude/compliance-faq#access-and-scopes)]

#### [manage-claude/opentelemetry](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/opentelemetry.md) [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry)]

* Added an overview video on tracing agents with OpenTelemetry. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/manage-claude/opentelemetry.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry#opentelemetry)]

#### [managed-agents/self-hosted-sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Workers now run on Linux or macOS hosts (macOS uses system Bash 3.2); quickstart gets separate Linux and macOS steps with `~/workspace` as the working directory on macOS. [[lines 38-216](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L38-L216)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes#prerequisites)]

#### [managed-agents/self-hosted-sandboxes-memory](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/managed-agents/self-hosted-sandboxes-memory.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory)]

* New "Prepare a macOS host" section: create `/System/Volumes/Data/mnt/memory`, add a `synthetic.conf` entry, run `apfs.util -t`, and verify. Notes macOS volumes are case-insensitive by default. [[lines 44-96](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/managed-agents/self-hosted-sandboxes-memory.md?plain=1#L44-L96)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-memory#prepare-a-macos-host)]

#### [managed-agents/self-hosted-sandboxes-operations](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/managed-agents/self-hosted-sandboxes-operations.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations)]

* Memory-mount troubleshooting now points macOS users to the macOS host preparation steps. [[line 333](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/managed-agents/self-hosted-sandboxes-operations.md?plain=1#L333)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-operations#memory-stores-fail-to-mount)]

#### [managed-agents/self-hosted-sandboxes-reference](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/managed-agents/self-hosted-sandboxes-reference.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference)]

* Worker host requirement is now Linux or macOS; on macOS, set the working directory somewhere writable since `/workspace` can't be created. [[lines 47-56](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/managed-agents/self-hosted-sandboxes-reference.md?plain=1#L47-L56)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes-reference#host-requirements)]

#### [models/*/migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/models/fable-5-1/migration-guide.md) [[Source](https://platform.claude.com/docs/en/models/fable-5-1/migration-guide)]

* The Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5 migration guides no longer promote the bundled Claude API skill for automating migration.

#### [release-notes/overview](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* The Claude Tag API beta announcement is now dated October 23, 2026. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/98e885a80b5a5c1f72b580f3e271f3e6c190650c/docs-md/api/release-notes/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/release-notes/overview#october-23-2026)]
