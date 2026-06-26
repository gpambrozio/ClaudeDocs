# [Claude docs changes for June 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/24ffc754ee595eb884407350070e73627186ac5e) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/24ffc754ee595eb884407350070e73627186ac5e)]

## Executive Summary
- Claude Code 2.1.193 adds Trusted Devices (beta) for Remote Control sessions on Team/Enterprise, requiring biometric device enrollment; also adds `autoMode.classifyAllShell` to route all shell commands through the auto-mode classifier
- The API introduces a new `CodeExecutionTool20260521` tool type with REPL state persistence and a new `frontier_llm` refusal category, plus a `session.updated` webhook event
- Vision documentation gains a new dedicated [Coordinates and bounding boxes](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/vision-coordinates.md) reference page extracted from the main vision doc
- Google Cloud Vertex AI is now referred to as "Google Cloud Agent Platform" throughout the API docs
- The Spend Limits API documentation gains three new example workflow guides combining spend limits and analytics APIs

## New Claude Code versions

### [2.1.193](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/versions/2.1.193.md)

#### New features

* Added `autoMode.classifyAllShell` setting to route all Bash/PowerShell commands through the auto-mode classifier instead of only arbitrary-code-execution patterns
* Added auto-mode denial reasons to the transcript, the denial toast, and `/permissions` recent denials
* Added `claude_code.assistant_response` OpenTelemetry log event containing the model's response text (redacted by default; enable with `OTEL_LOG_ASSISTANT_RESPONSES=1`)
* Added live file path autocomplete in bash mode (`!`)
* Added a startup notice when MCP servers need authentication, pointing at `/mcp`
* Added automatic memory-pressure reaping for idle background shell commands (disable with `CLAUDE_CODE_DISABLE_BG_SHELL_PRESSURE_REAP=1`)

#### Existing feature improvements

* Improved background agents: the launch result no longer instructs Claude to "end your response" — it keeps working on other tasks while the agent runs
* Improved MCP `headersHelper` auth: the helper now re-runs and reconnects automatically when a tool call returns 401/403
* Improved plugin auto-rename: marketplace `renames` maps are now followed automatically, updating your settings to the new name
* Improved `/add-dir` message when the directory is already a working directory

#### Major bug fixes

* Fixed `/model` and other client-data-gated UI showing stale/empty state immediately after `/login`
* Fixed backgrounding (←←) spuriously cancelling with "N background tasks would be abandoned" when all running tasks carry over to the new session
* Fixed pinned background agents being re-prompted to "Continue from where you left off" after every auto-update
* Fixed backgrounding the main turn spawning a phantom "general-purpose (resumed)" subagent that re-ran the main conversation
* Fixed agent panel hiding sibling agents when viewing a subagent

-----

## Claude Code changes

### New Documents

#### [feature-availability](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/feature-availability.md) [[Source](https://code.claude.com/docs/en/feature-availability)]

New comprehensive reference showing which Claude Code features are available per provider (Claude subscription, Anthropic Console, Amazon Bedrock, Claude Platform on AWS, Google Vertex AI, Microsoft Foundry) and per subscription plan. Includes per-provider "what's missing" summary tabs and a model availability section.

### Changed documents

#### [agent-teams](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/agent-teams.md) [[Source](https://code.claude.com/docs/en/agent-teams)]

* Teammates now inherit the lead's effort level; in split-pane mode this applies from v2.1.186 — earlier versions did not pass the lead's effort to split-pane teammates. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/agent-teams.md?plain=1#L125)] [[Source](https://code.claude.com/docs/en/agent-teams#specify-teammates-and-models)]

#### [agent-view](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* `--bg` flag now has a documented long-form alias `--background`. [[line 258](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/agent-view.md?plain=1#L258)] [[Source](https://code.claude.com/docs/en/agent-view#from-your-shell)]

#### [cli-reference](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* `--bg` flag entry updated to document `--background` as an equivalent alias. [[line 143](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/cli-reference.md?plain=1#L143)] [[Source](https://code.claude.com/docs/en/cli-reference#see-also)]

#### [debug-your-config](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/debug-your-config.md) [[Source](https://code.claude.com/docs/en/debug-your-config)]

* Hook matcher separator: Claude Code v2.1.191 or later accepts `,` as a separator in addition to `|` (e.g., `"Edit,Write"` is now valid); earlier versions treat a comma as a literal regex character causing silent non-matches. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/debug-your-config.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/debug-your-config#check-hooks)]
* New troubleshooting table row added for the comma-separator version incompatibility. [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/debug-your-config.md?plain=1#L76)] [[Source](https://code.claude.com/docs/en/debug-your-config#check-common-causes)]

#### [hooks-guide](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Auto-format hook example updated to note that on v2.1.191+ the matcher `Edit,Write` is equivalent to `Edit|Write`. [[line 306](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/hooks-guide.md?plain=1#L306)] [[Source](https://code.claude.com/docs/en/hooks-guide#audit-configuration-changes)]

#### [index](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/index.md) [[Source](https://code.claude.com/docs/en/index)]

* Added Windows install troubleshooting hint: if the install command fails with `syntax error near unexpected token '<'`, a `403`, or another curl error, users are directed to `troubleshoot-install.md`. [[line 39](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/index.md?plain=1#L39)] [[Source](https://code.claude.com/docs/en/index#get-started)]

#### [mcp-quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/mcp-quickstart.md) [[Source](https://code.claude.com/docs/en/mcp-quickstart)]

* As of v2.1.191, an HTTP MCP server returning `404 Not Found` now shows a specific error `MCP endpoint not found at <url>. Check the URL in your MCP config.`; earlier versions show a generic `Error POSTing to endpoint` message. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/mcp-quickstart.md?plain=1#L284)] [[Source](https://code.claude.com/docs/en/mcp-quickstart#troubleshooting)]

#### [monitoring-usage](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* `start_type` attribute for `claude_code.session.start` now includes a new value `"agents_view"` identifying the `claude agents` dashboard process (a local UI, not a conversational session), with guidance to filter on this value. [[line 411](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/monitoring-usage.md?plain=1#L411)] [[Source](https://code.claude.com/docs/en/monitoring-usage#session-counter)]
* New guidance for per-model commit attribution: filter the token or cost metric to rows where `query_source` is `"main"` to avoid attributing session commits to auxiliary or subagent models. [[line 962](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/monitoring-usage.md?plain=1#L962)] [[Source](https://code.claude.com/docs/en/monitoring-usage#alerting-and-segmentation)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/overview.md) [[Source](https://code.claude.com/docs/en/overview)]

* Added same Windows install troubleshooting hint for `syntax error near unexpected token '<'` errors.

#### [quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/quickstart.md) [[Source](https://code.claude.com/docs/en/quickstart)]

* Added same Windows install troubleshooting hint for `syntax error near unexpected token '<'` errors.

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* New "Trusted Devices" section (beta, Team and Enterprise plans): requires an enrolled device plus a sign-in within the last 18 hours to view or steer Remote Control sessions. Uses biometric step-up (Face ID, Touch ID, Windows Hello, passkey). Includes setup instructions for admins, member enrollment flow, device management via account settings, and error message guidance for unenrolled devices and expired sessions. [[lines 122-185](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/remote-control.md?plain=1#L122-L185)] [[Source](https://code.claude.com/docs/en/remote-control#trusted-devices)]

#### [routines](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/routines.md) [[Source](https://code.claude.com/docs/en/routines)]

* `/schedule` troubleshooting now also covers the `"No commands match"` message in addition to `"Unknown command"`, with clarification of what both messages look like in the UI.

#### [setup](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Added same Windows install troubleshooting hint for `syntax error near unexpected token '<'` errors.

#### [terminal-guide](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/terminal-guide.md) [[Source](https://code.claude.com/docs/en/terminal-guide)]

* Windows "Start Claude Code" step updated to run `claude` directly rather than closing and reopening PowerShell.
* macOS/Linux `command not found: claude` fix updated: installer now prints the exact fix under `Setup notes` at install end; added check to verify `~/.local/bin/claude` exists if still not found.
* Windows `'claude is not recognized'` fix updated: removes "restart your computer" advice and instead gives users PATH fix commands to run directly in PowerShell.

#### [third-party-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/claude-code/third-party-integrations.md) [[Source](https://code.claude.com/docs/en/third-party-integrations)]

* Added a reference link to `feature-availability.md` for a feature-by-feature breakdown of what's available on each deployment option.

-----

## API changes

### New Documents

#### [vision-coordinates](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/vision-coordinates.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision-coordinates)]

New dedicated reference page on working with pixel coordinates and bounding boxes returned by Claude. Covers how Claude resizes and pads images before processing, a Python reference implementation for computing exact resized dimensions, how to pre-resize images before upload so coordinates map directly, and how to rescale coordinates when pre-resizing isn't possible.

### Changed documents

#### [advisor-tool](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Priority Tier behavior clarified: a Priority Tier commitment on the executor model does not extend to the advisor; advisor calls run at Priority Tier only if the organization holds a separate commitment on the advisor model. [[line 630](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L630)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [build-a-tool-using-agent](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/agents-and-tools/tool-use/build-a-tool-using-agent.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)]

* Code examples for all five Rings now include C#, Go, Java, PHP, and Ruby SDK tabs in addition to cURL, CLI, Python, and TypeScript. SDK-specific helpers documented: `BetaRunnableTool` in C# and PHP, typed tool classes in Java and Ruby, and `toolrunner.NewBetaToolFromJSONSchema` in Go.

#### [mcp-connector (managed-agents)](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/managed-agents/mcp-connector)]

* Clarified that each declared MCP server needs a matching `mcp_toolset` entry in the `tools` array, with `mcp_server_name` matching the server's `name`. [[lines 24-25](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/mcp-connector.md?plain=1#L24-L25)] [[Source](https://platform.claude.com/docs/en/managed-agents/mcp-connector)]
* `session.error` event now linked to the events-and-streaming guide. [[line 122](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/mcp-connector.md?plain=1#L122)] [[Source](https://platform.claude.com/docs/en/managed-agents/mcp-connector)]

#### [agent-setup](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/agent-setup.md) [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

* `model` field now explicitly accepts either a string or an object (e.g., `{"id": "claude-opus-4-8"}`). [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/agent-setup.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
* CLI example updated to capture the agent ID and version into shell variables using `jq`. [[lines 45-51](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/agent-setup.md?plain=1#L45-L51)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
* Update semantics clarified: `version` field is required and must match the current version; a mismatch returns 409; updates to archived agents are rejected. [[line 96](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/agent-setup.md?plain=1#L96)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
* Metadata deletion: to delete a specific key, set its value to `null` (previously said empty string). [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/agent-setup.md?plain=1#L111)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
* Archiving is stated as irreversible ("cannot be undone"). [[line 136](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/agent-setup.md?plain=1#L136)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]
* `list versions` results noted as paginated, with SDKs fetching every page automatically. [[line 124](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/agent-setup.md?plain=1#L124)] [[Source](https://platform.claude.com/docs/en/managed-agents/agent-setup)]

#### [permission-policies](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/permission-policies.md) [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]

* Default policies clarified per toolset kind: agent toolset defaults to `always_allow`, MCP toolsets default to `always_ask`. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/permission-policies.md?plain=1#L20)] [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]
* Note added: permission policy settings apply to sessions created after an update; running sessions keep the configuration they were created with. [[line 25](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/permission-policies.md?plain=1#L25)] [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]
* Confirmation flow clarified: denied tools don't run and the agent receives a tool result stating the call was rejected including any `deny_message`; multiple confirmations can be sent in a single `events` request; session waits indefinitely for a response. [[lines 116-119](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/permission-policies.md?plain=1#L116-L119)] [[Source](https://platform.claude.com/docs/en/managed-agents/permission-policies)]

#### [tools](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/tools.md) [[Source](https://platform.claude.com/docs/en/managed-agents/tools)]

* `read` and `write` tool descriptions changed from "local filesystem" to "sandbox filesystem". [[lines 22-23](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/tools.md?plain=1#L22-L23)] [[Source](https://platform.claude.com/docs/en/managed-agents/tools)]
* `default_config` object behavior explained: sets the baseline for every tool; per-tool `configs` entries override it. [[line 70](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/managed-agents/tools.md?plain=1#L70)] [[Source](https://platform.claude.com/docs/en/managed-agents/tools)]

#### [claude-on-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Page title and all content updated from "Vertex AI" to "Google Cloud Agent Platform" — model IDs, section headers, payload limits, and instructions now reference "Agent Platform" throughout. [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [cmek](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/manage-claude/cmek.md) [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

* New prerequisite: Zero Data Retention (ZDR) must be turned off for your organization before using CMEK. [[line 33](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/manage-claude/cmek.md?plain=1#L33)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]
* Cowork in Claude Desktop added to the list of what CMEK covers; removed from the list of features NOT covered under Claude Enterprise. [[line 64](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/manage-claude/cmek.md?plain=1#L64)] [[Source](https://platform.claude.com/docs/en/manage-claude/cmek)]

#### [overview (build-with-claude)](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* "Vertex AI" replaced with "Google Cloud" in the platform labels legend and feature availability tables.

#### [prompt-caching](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Pre-warm request example now shows tabs for all nine SDKs (cURL, CLI, Python, TypeScript, C#, Go, Java, PHP, Ruby) instead of Python only. [[line 526](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L526)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [spend-limits-api](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/manage-claude/spend-limits-api.md) [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]

* New "Example workflows" section with three detailed workflow guides combining the Spend Limits API and Analytics APIs: (1) automating the increase-request review flow, (2) identifying members close to their spend limit, and (3) finding members with rapidly changing usage — each with curl examples. [[line 287](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/manage-claude/spend-limits-api.md?plain=1#L287)] [[Source](https://platform.claude.com/docs/en/manage-claude/spend-limits-api)]

#### [vision](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* New "Image limits and costs" section with a consolidated table comparing standard-tier vs. high-resolution-tier token costs across image sizes. [[line 192](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/vision.md?plain=1#L192)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]
* Coordinate and bounding box guidance extracted to a new dedicated page; the section now redirects to [Coordinates and bounding boxes](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/vision-coordinates.md). [[line 261](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/build-with-claude/vision.md?plain=1#L261)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

#### [API reference (all SDKs) — messages/create, messages/count_tokens, batches](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

* New `CodeExecutionTool20260521` tool type added (`"code_execution_20260521"`) with REPL state persistence, including fields `name`, `type`, `allowed_callers`, `cache_control`, `defer_loading`, `strict`. [[line 4036](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/api/messages/create.md?plain=1#L4036)] [[Source](https://platform.claude.com/docs/en/api/messages/create)]
* Several older model IDs removed from the supported model enum: `claude-opus-4-0`, `claude-opus-4-20250514`, `claude-sonnet-4-0`, `claude-sonnet-4-20250514`, `claude-3-haiku-20240307`.

#### [API reference (beta) — messages/create, beta.md](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* New `frontier_llm` refusal category added to `RefusalBlock.category` and `BetaRefusalBlock.category` enums (previously only `"cyber"`, `"bio"`, `"reasoning_extraction"`).
* New `trigger` field on `BetaFallbackBlock`: `{ from, to, trigger, type }` where `trigger` is a new `BetaFallbackRefusalTrigger { category, type }` object documenting what caused the model handoff. [[line 4396](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/api/beta.md?plain=1#L4396)] [[Source](https://platform.claude.com/docs/en/api/beta)]

#### [API reference (beta) — agents/create, agents/update (all SDKs)](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/api/beta/agents/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/agents/create)]

* `mcp_servers` constraint clarified: every declared server must be referenced by an `mcp_toolset` in `tools`; unreferenced servers are rejected.

#### [API reference (beta) — webhooks (all SDKs)](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/api/beta/webhooks.md) [[Source](https://platform.claude.com/docs/en/api/beta/webhooks)]

* New `session.updated` webhook event type added (`BetaWebhookSessionUpdatedEventData` with fields `id`, `organization_id`, `type: "session.updated"`, `workspace_id`). [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/24ffc754ee595eb884407350070e73627186ac5e/docs-md/api/api/beta/webhooks.md?plain=1#L30)] [[Source](https://platform.claude.com/docs/en/api/beta/webhooks)]
