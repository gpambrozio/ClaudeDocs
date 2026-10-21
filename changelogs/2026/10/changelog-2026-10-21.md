# [Claude docs changes for Oct, 21st 2026](https://github.com/gpambrozio/ClaudeDocs/tree/46a55a592c1668e7c04ed04061d3dafd053429b5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/46a55a592c1668e7c04ed04061d3dafd053429b5)]

## Executive Summary
- New API docs for **user profiles** (attribute requests to end customers so a safety enforcement action hits one profile, not your whole organization), a **Verification Portal** enrollment link, and beta **organization webhooks** for enforcement events
- Claude Code 2.1.305 adds `sandbox.allowNestedUserNamespaces`, a smarter `/usage` with one-key fixes (`f`), and a retry that keeps requests working when a gateway rejects tool search
- Agent view gains `/model`, `/effort` and `/fast` for dispatched sessions, a `← agents` footer hint, `/resume` to bring back past sessions, and guidance for keeping sessions alive after the supervisor stops
- New Code Review features: `@file` includes in `REVIEW.md`, `@claude review always|stop` comment commands, and a severity line you can parse in CI
- Large new troubleshooting coverage in the errors reference, plus Agent SDK docs for MCP startup waits, `StructuredOutput` tool calls and context usage

## New Claude Code versions

### [2.1.305](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/versions/2.1.305.md)

#### New features

* Added `sandbox.allowNestedUserNamespaces` so sandboxed commands on Linux can create user namespaces (Chromium, rootless podman); this lets them get around the sandbox's file protections
* Added `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS` so unattended retry mode notices a usage limit that was lifted before its reset
* Added a "Running start-up hooks" spinner status in VS Code while SessionStart or Setup hooks run
* Claude Tag admin Add place search now includes public Slack channels Claude hasn't joined

#### Existing feature improvements

* `/usage`: each warning is now a one-line fix naming its source, and `f` applies the fixes; the same fixes appear in VS Code and `/doctor`
* MCP consent dialogs make it less likely that an Enter meant for the prompt is taken as Accept
* A mod's `Image` now draws in iTerm2 3.5+ with fullscreen rendering; a mod's docked pane stays within 45% of terminal width
* Remote Control spawn-mode messages are clearer about saved modes
* Deleting a self-hosted environment now explains what blocks the delete and what it affects
* `allowedMcpServers` no longer filters `managed-mcp.json` stdio servers that use `${VAR}` only in `env` (use `deniedMcpServers` to keep one off)
* Plugins mounted by path by Claude Desktop no longer keep their `allowed-tools` when `allowManagedPermissionRulesOnly` is set
* `/artifacts` delete confirmation now uses 1/Enter to keep, 2 to delete, Esc to cancel
* Code Review re-reviews no longer open with LGTM while earlier blocking findings remain open

#### Major bug fixes

* Fixed every request failing on Vertex, Bedrock and other providers when an endpoint or gateway rejects tool search (a 2.1.304 regression): Claude Code now retries without it
* Fixed `/effort` and `/autocompact` settings not applying when the model name differed from a `modelOverrides` value by case or a `[1m]` tag
* Fixed new worktrees in a bare repository starting from local HEAD instead of the default branch
* Fixed Bash on a full disk failing with a raw `ENOSPC` path; the error now says the disk is full and that nothing ran
* Fixed an MCP server passed by a cloud session or SDK `setMcpServers` being replaced by a same-named server from user settings
* Fixed Workflow resume re-running completed `pipeline()` and `parallel()` agents
* Fixed self-hosted runner regressions: start scripts failing with `Resource temporarily unavailable`, repository access failing with `GIT_CONFIG` credential helpers, and spawn-runner hooks falsely reported as timed out
* Fixed Code Review sometimes not reviewing the newest commit when several pushes landed during a review

### [2.1.306](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/versions/2.1.306.md)

#### Major bug fixes

* Fixed `claude -p` inside cloud sessions reporting "Not logged in" when started without the session's environment variables
* Fixed an API error being replaced by "prompt is too long", and an unneeded compaction, in sessions with many MCP tools

-----

## Claude Code changes

Note: many files were also reformatted today (notes and tips wrapped in `> [!NOTE]` callouts, numbered steps rendered as bold lines, diagrams as images). Those formatting-only changes are not listed.

### New Documents

None.

### Changed documents

#### [admin-setup](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Managed settings table now lists plist/registry policy and file-based managed locations per platform. [[lines 46-47](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/admin-setup.md?plain=1#L46-L47)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-how-settings-reach-devices)]

#### [advisor](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/advisor.md) [[Source](https://code.claude.com/docs/en/advisor)]

* An advisor model that ranks below the main model still starts the session, background or not. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/advisor.md?plain=1#L82)] [[Source](https://code.claude.com/docs/en/advisor#use-the-advisor-flag)]

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/mcp.md) [[Source](https://code.claude.com/docs/en/agent-sdk/mcp)]

* Detailed rules for how long the first turn waits for MCP servers (stdio/HTTP/SSE servers, tool search, gateways, named servers, `permissionPromptToolName`, in-process SDK servers). [[lines 139-180](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L139-L180)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timing)]
* New `CLAUDE_CODE_MCP_STARTUP_WAIT_MS` setting to choose the first-turn wait, and `MCP_CONNECTION_NONBLOCKING=0` / `alwaysLoad: true` to make startup itself wait. [[lines 147-179](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/mcp.md?plain=1#L147-L179)] [[Source](https://code.claude.com/docs/en/agent-sdk/mcp#connection-timing)]

#### [agent-sdk/hooks](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/hooks.md) [[Source](https://code.claude.com/docs/en/agent-sdk/hooks)]

* New `plugin_notification` notification type, raised when a mod calls `$.ui.notify`. [[line 631](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/hooks.md?plain=1#L631)] [[Source](https://code.claude.com/docs/en/agent-sdk/hooks#forward-notifications-to-slack)]

#### [agent-sdk/examples](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/examples.md) [[Source](https://code.claude.com/docs/en/agent-sdk/examples)]

* New "Fork a complete project" section pointing to the Claude for commerce reference implementation for shopping and merchant agents. [[lines 19-22](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/examples.md?plain=1#L19-L22)] [[Source](https://code.claude.com/docs/en/agent-sdk/examples#fork-a-complete-project)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/permissions.md) [[Source](https://code.claude.com/docs/en/agent-sdk/permissions)]

* Allow rules accept tool-name globs only after a literal `mcp__<server>__` prefix with a glob-free server segment. [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/permissions.md?plain=1#L77)] [[Source](https://code.claude.com/docs/en/agent-sdk/permissions#allow-and-deny-rules)]

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/python.md) [[Source](https://code.claude.com/docs/en/agent-sdk/python)]

* New `ClaudeSDKClient.get_context_usage()` method returning the context window breakdown that `/context` shows. [[line 525](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/python.md?plain=1#L525)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#methods)]
* Clarified `is_error` semantics on success results and how to tell failures apart via `stop_reason`, `terminal_reason`, then `subtype`. [[lines 1682-1687](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/python.md?plain=1#L1682-L1687)] [[Source](https://code.claude.com/docs/en/agent-sdk/python#resultmessage)]

#### [agent-sdk/streaming-output](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/streaming-output.md) [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-output)]

* Structured output with partial messages streams as unvalidated `input_json_delta` chunks. [[line 311](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/streaming-output.md?plain=1#L311)] [[Source](https://code.claude.com/docs/en/agent-sdk/streaming-output#known-limitations)]

#### [agent-sdk/structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/structured-outputs.md) [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs)]

* New section explaining the `StructuredOutput` tool call that appears in the message stream, its `tool_result`, retries on schema mismatch, and why apps should hide it. [[lines 359-369](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/structured-outputs.md?plain=1#L359-L369)] [[Source](https://code.claude.com/docs/en/agent-sdk/structured-outputs#recognize-the-structuredoutput-tool-call)]

#### [agent-sdk/subagents](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/subagents.md) [[Source](https://code.claude.com/docs/en/agent-sdk/subagents)]

* `skills` preloads at most the first 32 distinct names; subagent messages carry `parent_tool_use_id` and (TypeScript) agent identifiers. [[line 144](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/subagents.md?plain=1#L144)] [[Source](https://code.claude.com/docs/en/agent-sdk/subagents#agentdefinition-configuration)]

#### [agent-sdk/tool-search](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/tool-search.md) [[Source](https://code.claude.com/docs/en/agent-sdk/tool-search)]

* Documents `ENABLE_TOOL_SEARCH` values (unset, `true`, `auto` with a 10% context threshold) and their fallbacks. [[lines 35-45](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/tool-search.md?plain=1#L35-L45)] [[Source](https://code.claude.com/docs/en/agent-sdk/tool-search#configure-tool-search)]

#### [agent-sdk/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/troubleshooting.md) [[Source](https://code.claude.com/docs/en/agent-sdk/troubleshooting)]

* A `success` result can have no `structured_output`; treat it as a failure, with causes (declined request, unsatisfiable schema). [[lines 139-144](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/troubleshooting.md?plain=1#L139-L144)] [[Source](https://code.claude.com/docs/en/agent-sdk/troubleshooting#structured_output-is-none-but-the-result-says-success)]

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/typescript.md) [[Source](https://code.claude.com/docs/en/agent-sdk/typescript)]

* New `getContextUsage()` query method and `SDKControlGetContextUsageResponse` type. [[line 659](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-sdk/typescript.md?plain=1#L659)] [[Source](https://code.claude.com/docs/en/agent-sdk/typescript#methods)]
* New "What `readFile()` can read" section, `peer` message origin details, and a note that `StructuredOutput` has no exported input type.

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* Pressing `←` on an empty prompt opens agent view; the footer shows `← for agents`, waiting counts, and finished counts. [[lines 57-64](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-view.md?plain=1#L57-L64)] [[Source](https://code.claude.com/docs/en/agent-view#quick-start)]
* What happens to prompts and `!` commands entered as a session moves to the background. [[lines 287-296](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-view.md?plain=1#L287-L296)] [[Source](https://code.claude.com/docs/en/agent-view#prompts-sent-as-the-session-moves-to-the-background)]
* Bare `/resume` in agent view brings back past sessions as background sessions. [[lines 314-325](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-view.md?plain=1#L314-L325)] [[Source](https://code.claude.com/docs/en/agent-view#bring-back-a-past-session)]
* `/model`, `/effort` and `/fast` in the dispatch input set defaults for sessions you dispatch next. [[lines 647-665](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-view.md?plain=1#L647-L665)] [[Source](https://code.claude.com/docs/en/agent-view#set-the-model-effort-and-fast-mode)]
* Prompts containing `--bg` are delivered as typed; ambiguous positions exit with an error. [[lines 535-546](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-view.md?plain=1#L535-L546)] [[Source](https://code.claude.com/docs/en/agent-view#prompts-that-contain-bg)]
* New "Keep sessions running after the supervisor stops" section (one-minute window; run `claude agents`) and stop-failure message table. [[lines 847-858](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-view.md?plain=1#L847-L858)] [[Source](https://code.claude.com/docs/en/agent-view#keep-sessions-running-after-the-supervisor-stops)]
* New `No LLM gateway` troubleshooting entry and new version history rows (v2.1.295 to v2.1.299). [[lines 990-999](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/agent-view.md?plain=1#L990-L999)] [[Source](https://code.claude.com/docs/en/agent-view#a-background-session-shows-no-llm-gateway)]

#### [artifacts](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/artifacts.md) [[Source](https://code.claude.com/docs/en/artifacts)]

* New `d` key in `/artifacts` permanently deletes an artifact you own. [[line 97](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/artifacts.md?plain=1#L97)] [[Source](https://code.claude.com/docs/en/artifacts#find-an-artifact-again)]
* Compliance API endpoints for listing, fetching versions of, and deleting artifacts. [[lines 424-428](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/artifacts.md?plain=1#L424-L428)] [[Source](https://code.claude.com/docs/en/artifacts#list-and-delete-artifacts-with-the-compliance-api)]

#### [auto-mode-config](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/auto-mode-config.md) [[Source](https://code.claude.com/docs/en/auto-mode-config)]

* `/auto-mode-setup` now has its own sections: what it reads, how to turn it off, and an "Unknown command" troubleshooting list; new "Edit rules from `/permissions`" section. [[lines 158-210](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/auto-mode-config.md?plain=1#L158-L210)] [[Source](https://code.claude.com/docs/en/auto-mode-config#generate-environment-entries-with-auto-mode-setup)]

#### [checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* Rewound messages can return if you exit before your next prompt, and how to remove them. [[lines 43-46](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/checkpointing.md?plain=1#L43-L46)] [[Source](https://code.claude.com/docs/en/checkpointing#rewound-messages-can-return-if-you-exit-before-your-next-prompt)]

#### [chrome](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* New "No browsers are connected" troubleshooting row. [[line 328](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/chrome.md?plain=1#L328)] [[Source](https://code.claude.com/docs/en/chrome#common-error-messages)]

#### [claude-apps-gateway-config](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-apps-gateway-config.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway-config)]

* Policy merge rules for deny-lists and hook arrays; `deniedModels` and `availableModelsMatch` are now enforced by the gateway and CLI and filter the bootstrap model list.

#### [claude-apps-gateway](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-apps-gateway.md) [[Source](https://code.claude.com/docs/en/claude-apps-gateway)]

* New "What's enforced on developers" heading and architecture diagram.

#### [claude-code-on-the-web](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-code-on-the-web.md) [[Source](https://code.claude.com/docs/en/claude-code-on-the-web)]

* `claude --cloud` clones the GitHub remote at your branch, not your local checkout; new "Branch is not on GitHub" troubleshooting; `/config` and subagent notes. [[lines 96](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-code-on-the-web.md?plain=1#L96)] [[Source](https://code.claude.com/docs/en/claude-code-on-the-web#start-a-cloud-session-from-your-terminal)]

#### [claude-directory](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-directory.md) [[Source](https://code.claude.com/docs/en/claude-directory)]

* The interactive explorer content was removed from the page, leaving the file reference table and a "State files to keep" section. [[lines 4-49](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-directory.md?plain=1#L4-L49)] [[Source](https://code.claude.com/docs/en/claude-directory#explore-the-claude-directory)]

#### [claude-projects](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-projects.md) [[Source](https://code.claude.com/docs/en/claude-projects)]

* New table of what cloud threads pick up from repositories: `CLAUDE.md` and rules load; skills, agents, `.mcp.json`, plugins, permission rules, hooks and `env` from `.claude/settings.json` do not. [[lines 330-340](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-projects.md?plain=1#L330-L340)] [[Source](https://code.claude.com/docs/en/claude-projects#what-threads-pick-up-from-your-repositories)]
* Repositories can be added to a project or added by a thread on demand; approvals cover only that thread.

#### [claude-platform-on-aws](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Page shortened; the first ~170 lines of introductory content were removed. [[lines 4-11](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L4-L11)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws#claude-code-on-claude-platform-on-aws)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated `--name`/`-n` and `--permission-prompt-tool` flag descriptions. [[lines 105-110](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/cli-reference.md?plain=1#L105-L110)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [cloud-environments](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/cloud-environments.md) [[Source](https://code.claude.com/docs/en/cloud-environments)]

* New "Add network secrets" section: adding a secret (including on Team plans without an admin role), which requests get it, and which never do.
* Hooks and setup scripts behave differently in project cloud threads.

#### [code-review-customize](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/code-review-customize.md) [[Source](https://code.claude.com/docs/en/code-review-customize)]

* New "Include other files in REVIEW.md": `@review-security.md`-style lines pull root-level files in (max eight files, 150,000 bytes combined, 64 links), with protected-branch rules and a checklist when an include isn't applied.

#### [code-review-pull-requests](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/code-review-pull-requests.md) [[Source](https://code.claude.com/docs/en/code-review-pull-requests)]

* Parse the `bughunter-severity` HTML comment from the check run Details with `gh` and jq to gate merges in CI.
* New comment commands table: `@claude review`, `@claude review always`, `@claude review stop` (also `off`/`pause`), and conditions for them to take effect.

#### [code-review-troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/code-review-troubleshooting.md) [[Source](https://code.claude.com/docs/en/code-review-troubleshooting)]

* New check-run messages about `REVIEW.md` being skipped because of links or modified files.

#### [commands](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Added `/auto-mode-setup`, `/claude-api` subcommands, `/design consent` and `/design revoke`, `/design-login` and the `/design-sync` skill.

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* `/usage` on paid plans shows a plan-usage breakdown with recommendations; pressing `f` applies those it can (`/effort` changes run directly, others become a prompt), with a table of row shapes.

#### [cross-session-messaging](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/cross-session-messaging.md) [[Source](https://code.claude.com/docs/en/cross-session-messaging)]

* Replies from other machines and cloud sessions, `dialogExpiry`, and the session inbox socket.

#### [data-usage](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/data-usage.md) [[Source](https://code.claude.com/docs/en/data-usage)]

* Telemetry table now lists defaults and opt-out variables per provider, including error reports, `/feedback`, surveys and the WebFetch domain check.

#### [desktop](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Describes the Code tab, auto mode availability, the session details panel with a Context card, `/context`, and Dispatch/Cowork links. (The same text was added to `desktop-changelog`.)

#### [desktop-linux](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/desktop-linux.md) [[Source](https://code.claude.com/docs/en/desktop-linux)]

* Cowork on Linux requirements (KVM, QEMU, UEFI firmware, virtiofsd), sign-in, and a root/`--no-sandbox` error.

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* New sections on plugins from your claude.ai account, adding a marketplace from claude.ai, and JetBrains/non-interactive/SDK behavior.

#### [env-vars](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* New: `CLAUDE_CODE_DISABLE_BG_EXIT_HANDOFF`, `CLAUDE_CODE_FORCE_TERMINAL_IMAGES`, `CLAUDE_CODE_MCP_STARTUP_WAIT_MS`, `CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS`; updated `API_TIMEOUT_MS` (0 turns off request timeout), `ENABLE_TOOL_SEARCH`, `ENABLE_PROMPT_CACHING_1H`, `CLAUDE_CODE_MAX_RETRIES`.

#### [errors](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/errors.md) [[Source](https://code.claude.com/docs/en/errors)]

* Many new entries: local sign-in listener failures, release verification and auto-update failures, 128 MB image read limit, disk full (ENOSPC/EDQUOT), artifact publish refusals, `No LLM gateway`, shutdown-approval refusals, `/feedback` disabled by policy, plugin path/manifest escape errors, and `--bg` flag ambiguity.
* New gateway guidance for `400` errors naming `context_management` or `defer_loading` (update to v2.1.304+/v2.1.305 or forward the `anthropic-beta` header), plus configuration warnings for `CLAUDE_CODE_AUTO_COMPACT_WINDOW` and permission rules that never match.

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

* Footnotes for cloud-session seat requirements, ZDR enablement, cross-session messaging requirements; new "Partial support" entry for Desktop on 3P.

#### [headless](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* A run without valid structured output has no `structured_output` field.

#### [hooks](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* `permissionDecision: "defer"` (non-interactive `-p`): ends the turn with the tool pending and resumes later; no timeout, falls back if tool unavailable, only works with a single tool call per turn.
* New `plugin_notification` notification type. (Same changes in `hooks-guide`.)

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Press `Up` to recover a draft cleared with `Ctrl+C` (ten most recent drafts kept).

#### [keybindings](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/keybindings.md) [[Source](https://code.claude.com/docs/en/keybindings)]

* New `settings:fixUsage` action (F); warning about a space next to `+` in key strings.

#### [llm-gateway-protocol](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/llm-gateway-protocol.md) [[Source](https://code.claude.com/docs/en/llm-gateway-protocol)]

* Beta body fields and their beta headers must travel together; new automatic retries (thinking type, mid-conversation system messages, `cache_control`, `context_management`) and retry without tool search on v2.1.305+.

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Tool search is on by default with `ENABLE_TOOL_SEARCH` table; `WaitForMcpServers` used without tool search; `claude mcp get` redacts plugin stdio/WebSocket values; gateway tool-search retry.

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Enterprise admins can cap effort level per model per role; capped levels are hidden from `/effort`.

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Documents the `tool.output` span event and a caveat for lowering `OTEL_LOGRECORD_ATTRIBUTE_COUNT_LIMIT`.

#### [permission-modes](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/permission-modes.md) [[Source](https://code.claude.com/docs/en/permission-modes)]

* Background sessions require bypass-permissions acceptance recorded in user or managed settings; new "Bypass permissions was requested at launch and ignored" notice.

#### [permissions](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* MCP allow-rule glob rules, a startup warning for deny/ask rules matching no tool, `find` with write/exec actions, and `Read` deny rules covering `@`-mentions, pasted images, changed files and IDE context.

#### [plugins/mods/api](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/plugins/mods/api.md) [[Source](https://code.claude.com/docs/en/plugins/mods/api)]

* New `$.ui.notify(text)` for terminal notifications, with `{ isSent, channel }` / `{ isSent: false, reason }` results.

#### [plugins/mods/events](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/plugins/mods/events.md) [[Source](https://code.claude.com/docs/en/plugins/mods/events)]

* New `tool.check` guidance for approving or refusing tool calls and the `e.isReadOnly` field (v2.1.304+).

#### [plugins/mods/gallery](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/plugins/mods/gallery.md) [[Source](https://code.claude.com/docs/en/plugins/mods/gallery)]

* `Image` terminal support (kitty, Ghostty, iTerm2 3.5+ in fullscreen) and fallbacks.

#### [plugins/troubleshooting](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/plugins/troubleshooting.md) [[Source](https://code.claude.com/docs/en/plugins/troubleshooting)]

* Steps to fix `Version: unknown` for git-sourced plugins.

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Saved spawn mode behavior (`w` key, `--spawn`), cross-session messages over the connection, and auto-connect with `DISABLE_TELEMETRY`/`DO_NOT_TRACK`.

#### [sandboxing](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/sandboxing.md) [[Source](https://code.claude.com/docs/en/sandboxing)]

* IPv6 allow/deny spelling, symlinked denied paths on macOS, and a user-settings fallback when no project folder is writable.

#### [self-hosted-environments-configuration](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/self-hosted-environments-configuration.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-configuration)]

* New `CLAUDE_RUNNER_ACCOUNT_ID`; redirect output of background processes started by `spawn-runner` hooks; settings/MCP/skills loading differences inside projects.

#### [self-hosted-environments-deploy](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/self-hosted-environments-deploy.md) [[Source](https://code.claude.com/docs/en/self-hosted-environments-deploy)]

* Git proxy behavior and new troubleshooting for `Resource temporarily unavailable` and `This runner couldn't read`.

#### [settings-reference](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/settings-reference.md) [[Source](https://code.claude.com/docs/en/settings-reference)]

* Idle compaction setting and `/config` row; locking the `hooks` surface (which hooks stop and which keep running); notification channel note.

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Clarified precedence and which settings files cloud sessions and project threads read.

#### [skills](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* New `managed-agents-secure` subcommand; project/nested skills are not loaded in project cloud threads; forked skills in dynamic workflows wait for results. (Mirrored in `slash-commands`.)

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Fallback-model warning line in subagent reports; resumed subagents can be messaged by name again (v2.1.299+).

#### [tools-reference](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Read refuses images larger than 128 MB. [[line 503](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/tools-reference.md?plain=1#L503)] [[Source](https://code.claude.com/docs/en/tools-reference#read-tool-behavior)]
* Web search limit applies per turn in `-p` and the Agent SDK. [[line 666](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/tools-reference.md?plain=1#L666)] [[Source](https://code.claude.com/docs/en/tools-reference#session-search-limit)]

#### [troubleshoot-install](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/troubleshoot-install.md) [[Source](https://code.claude.com/docs/en/troubleshoot-install)]

* New "Release verification failed" and "Auto-update failed" sections.

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Fix for missing conversations with `claudeProcessWrapper` (extension 2.1.304+), `/tasks` agent map hint, and screen reader status announcements. (Same in `ide-integrations`.)

#### [workflows](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/workflows.md) [[Source](https://code.claude.com/docs/en/workflows)]

* Resume replay semantics: failed agents and every agent started after them run again.

#### [worktrees](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/claude-code/worktrees.md) [[Source](https://code.claude.com/docs/en/worktrees)]

* Cleanup behavior when another branch is checked out in the worktree.

-----

## API changes

### New Documents

#### [api/organization/workspaces/rate_limits/update](https://github.com/gpambrozio/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/api/organization/workspaces/rate_limits/update.md) [[Source](https://platform.claude.com/docs/en/api/organization/workspaces/rate_limits/update)]

Set Workspace Rate Limits: `POST /v1/organizations/workspaces/{workspace_id}/rate_limits/{rate_limit_id}` sets or clears rate-limit overrides for one group (integer sets, `null` clears; the lower of workspace and organization limit applies). A beta variant was added under `api/beta/organization/workspaces/rate_limits/update`.

#### [manage-claude/organization-webhooks](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/organization-webhooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/organization-webhooks)]

Beta (`webhooks-2026-10-07`) Admin API for registering webhook endpoints (up to 32 per organization) that receive `user_profile.enforcement_action_opened` and `user_profile.enforcement_action_resolved`. Covers Standard Webhooks signing, retries, automatic disabling, secret rotation and error codes. Event delivery isn't live yet. Reference pages for list, create, retrieve, update, delete and regenerate signing secret were added under `api/api/beta/organization/webhooks/`.

#### [manage-claude/user-profiles](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/user-profiles.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-profiles)]

Explains registering each end customer with `POST /v1/user_profiles` and sending the `uprof_` ID in the `anthropic-user-profile-id` header so safety enforcement applies to one end customer instead of the organization. Profiles aren't billable. New endpoint reference pages (create, list, retrieve, update, delete) were added under `api/api/user_profiles/` and beta equivalents.

#### [manage-claude/user-profiles-verification-portal](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/user-profiles-verification-portal.md) [[Source](https://platform.claude.com/docs/en/manage-claude/user-profiles-verification-portal)]

How to create an enrollment link with `POST /v1/user_profiles/{id}/action_urls` so end customers can link their profile to their own organization in the Verification Portal, with examples in every SDK. Includes `api/api/user_profiles/action_urls` reference pages.

### Changed documents

#### [about-claude/models/optimizing-for-cost-and-intelligence](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/about-claude/models/optimizing-for-cost-and-intelligence.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence)]

* At `xhigh` and `max`, Claude Sonnet 5.5 can start its own rounds of review after finishing a task, using more time and tokens.

#### [agents-and-tools/agent-skills/claude-api-skill](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/agents-and-tools/agent-skills/claude-api-skill.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/claude-api-skill)]

* New `managed-agents-secure` check that compares an agent's settings with the Managed Agents security guide using the `ant` CLI.

#### [agents-and-tools/mcp-connector](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* MCP server `url` must start with `https://`.

#### [agents-and-tools/tool-use/web-search-tool](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Organization-level web search settings in the Console apply to Messages API requests and Managed Agents sessions, alongside request-level domain restrictions (also noted in `server-tools`).

#### [cli-sdks-libraries/overview](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/cli-sdks-libraries/overview.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/overview)]

* New table of latest versions: ant CLI 1.44.0, Python 1.17.0, TypeScript 0.137.0, C# 12.60.0, Go 1.84.0, Java 2.75.0, PHP 0.61.0, Ruby 1.82.0, also available as JSON at `/docs/sdk-versions.json`. Java dependency snippets across cloud-provider pages now use 2.75.0.

#### [cli-sdks-libraries/cli/authentication](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/cli-sdks-libraries/cli/authentication.md) [[Source](https://platform.claude.com/docs/en/cli-sdks-libraries/cli/authentication)]

* `ANTHROPIC_API_KEY` or `ANTHROPIC_AUTH_TOKEN` takes precedence over every profile. (`get-started` also documents `--no-browser` for remote hosts.)

#### [manage-claude/claude-code-analytics-api](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/claude-code-analytics-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/claude-code-analytics-api)]

* Records cover only usage authenticated against your Console organization; subscription-plan usage isn't included, with alternatives (Enterprise Analytics API, claude.ai dashboard, OpenTelemetry).

#### [manage-claude/cmek](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* Lists features unavailable or not covered under CMEK (artifacts including Claude Design/Slides/Docs, some beta and research preview features, OpenTelemetry destination headers). The provider-specific CMEK pages warn that enabling CMEK is permanent; the AWS KMS page adds workspace-limiting key policy examples and compartment ID guidance, and the Claude Platform on AWS page adds `aws:SourceArn` conditions.

#### [manage-claude/inference-hooks](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/inference-hooks.md) [[Source](https://platform.claude.com/docs/en/manage-claude/inference-hooks)]

* Inference hooks are available only to Claude Enterprise organizations and require `organization:manage`; system prompts and tool definitions are never included in governed requests. (Same notes in the configuration and endpoint pages; `compliance-api` links to them.)

#### [manage-claude/opentelemetry/api](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/opentelemetry/api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/opentelemetry/api)]

* Destinations can be added through the Admin API; documents gzip compression, retries, 5-second timeouts, auto-disable behavior and a failure-reason table. SDK page adds tracer setup for C#, Ruby and Java.

#### [manage-claude/rate-limits-api](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/rate-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/rate-limits-api)]

* Workspace limits can now be set via the Set Workspace Rate Limits endpoint; organization limits cannot. Unmatched model strings return 404.

#### [manage-claude/admin-api](https://github.com/gpambrozo/ClaudeDocs/blob/46a55a592c1668e7c04ed04061d3dafd053429b5/docs-md/api/manage-claude/admin-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/admin-api)]

* Links to organization webhooks. (`api-and-data-retention` lists the new `/v1/user_profiles` endpoints.)
