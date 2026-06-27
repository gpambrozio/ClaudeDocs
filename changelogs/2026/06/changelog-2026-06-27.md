# [Claude docs changes for June 27th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5a8d759adfd68e218433c30a478bdf4787813747) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5a8d759adfd68e218433c30a478bdf4787813747)]

## Executive Summary
- **MCP CLI authentication**: New `claude mcp login <name>` and `claude mcp logout <name>` commands authenticate MCP servers from the shell without opening an interactive session (v2.1.186)
- **Shell mode responses**: Commands run with the `!` prefix now get a Claude response automatically once output lands in the transcript — no second prompt needed (v2.1.186)
- **Tool-use API overhaul**: The tool-use overview and server-tools docs were significantly restructured; key new guidance covers handling mixed client+server tool calls in the same turn and the `allowed_callers` field for server tools
- **Artifacts (Week 25)**: Claude Code can now publish live, interactive pages from your session to a private claude.ai URL, in beta on Team and Enterprise plans
- **Settings defaults reformatted**: The settings reference now shows `**Default**: X` prominently at the start of each description for easier scanning

-----

## New Claude Code versions

### [2.1.195](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/versions/2.1.195.md)

#### New features

* Added `CLAUDE_CODE_DISABLE_MOUSE_CLICKS` environment variable to disable mouse click/drag/hover in fullscreen mode while keeping wheel scroll

#### Existing feature improvements

* Improved voice mode on Linux to distinguish "no microphone" from "SoX not installed" when SoX is present but no audio capture device exists
* Improved `claude agents` completed list to fill available vertical space; on short terminals the header compacts so live sessions stay visible
* Improved Remote session startup with a provisioning checklist while the container starts

#### Major bug fixes

* Fixed hook matchers with hyphenated identifiers (e.g. `code-reviewer`, `mcp__brave-search`) accidentally substring-matching — they now exact-match. Use `mcp__brave-search__.*` to match all tools from a hyphenated MCP server
* Fixed voice dictation on macOS capturing silence in long-running sessions after the default input device changes
* Fixed voice dictation auto-submit never firing for languages written without spaces (Japanese, Chinese, Thai)
* Fixed external plugins enabled only by project `.claude/settings.json` not requiring explicit install consent on every loader path
* Fixed `/plugin` Enable/Disable not working when a plugin's `plugin.json` `name` differs from its marketplace entry name
* Fixed background jobs disappearing from `claude agents` or losing data when written by a newer Claude Code version
* Fixed reopening a crashed background task showing a blank screen for up to 5 seconds instead of its restart
* Fixed background agent daemons running unreachable when the control socket fails to start, blocking restarts

-----

## Claude Code changes

### New Documents

#### [What's New — Week 25 (June 15–19, 2026)](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/whats-new/2026-w25.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w25)]

Weekly digest for v2.1.178–v2.1.183. Highlights: **Artifacts** (publish live interactive pages from a session to a private claude.ai URL, beta on Team/Enterprise); **match by input parameter** (`Tool(param:value)` syntax for deny/ask rules, e.g. `Agent(model:opus)`); **`/config key=value`** to set any setting from the prompt or `-p` mode. Also covers: auto mode blocking destructive git commands, `attribution.sessionUrl` setting, `CLAUDE_CLIENT_PRESENCE_FILE` for suppressing mobile notifications, and streaming paragraphs line by line.

#### [What's New — Week 26 (June 22–26, 2026)](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/whats-new/2026-w26.md) [[Source](https://code.claude.com/docs/en/whats-new/2026-w26)]

Weekly digest for v2.1.185–v2.1.193. Highlights: **`claude mcp login/logout`** for CLI-based MCP server authentication; **shell mode responds to command output** (`! npm test` gets an explanation without a second prompt). Also covers: `/rewind` resuming conversations from before `/clear`, `sandbox.credentials` setting, org-level model restrictions in the model picker, `autoMode.classifyAllShell` setting, `claude_code.assistant_response` OpenTelemetry event, background subagent permission prompts surfacing in the main session, and 37% less streaming CPU usage.

### Changed documents

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Hook deduplication and environment variable information (`$CLAUDE_CODE_REMOTE`) moved to a more prominent position under the general hook handler section rather than buried under prompt/agent hooks. [[line 282](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/hooks.md?plain=1#L282)] [[Source](https://code.claude.com/docs/en/hooks#hook-handler-fields)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Shell mode section updated: clarified that `!` prefix commands don't require Claude to interpret or approve the command, and that Tab autocomplete works for file paths in Bash mode.
* Prompt suggestions: clarified that suggestions are skipped after the first turn and in plan mode; print mode off by default.

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Minor wording improvements throughout; no functional changes.

#### [Model configuration](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Updated `ANTHROPIC_CUSTOM_MODEL_OPTION` example from `claude-opus-4-7` to `claude-opus-4-8`. [[line 383](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/model-config.md?plain=1#L383)] [[Source](https://code.claude.com/docs/en/model-config#add-a-custom-model-option)]
* Organization model restrictions section reorganized: the Console toggle recommendation now leads the paragraph for clarity.

#### [Monitoring usage](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Improved `OTEL_RESOURCE_ATTRIBUTES` documentation: reorganized into clearer sections with better examples, clarified that wrapping values in quotes doesn't escape spaces, and noted that percent-encoding works for any character. [[lines 294-318](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/monitoring-usage.md?plain=1#L294-L318)] [[Source](https://code.claude.com/docs/en/monitoring-usage#multi-team-organization-support)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Sandboxing interaction section expanded: the behavior of `autoAllowBashIfSandboxed: true` now listed as three separate bullet points (content-scoped ask rules still prompt, deny rules still apply, root/home removals still prompt). [[lines 223-229](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/permissions.md?plain=1#L223-L229)] [[Source](https://code.claude.com/docs/en/permissions#read-and-edit)]
* Settings precedence section clarified: explicitly states that a user-level deny blocks a project-level allow (not just the reverse).

#### [Sessions](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/sessions.md) [[Source](https://code.claude.com/docs/en/sessions)]

* New **"Access conversations from scripts"** section documents four interfaces for scripting access to session data: structured output from `claude -p`, follow-up prompts via `--resume`, hooks receiving `transcript_path`, and the Agent SDK. Includes a runnable `jq` example. [[lines 95-117](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/sessions.md?plain=1#L95-L117)] [[Source](https://code.claude.com/docs/en/sessions#export-and-locate-session-data)]
* **"Where transcripts are stored"** section reorganized into a table covering location, retention, and write suppression options. Added a warning that the internal JSONL format can change between versions and scripts should use `/export` or the script interfaces instead.

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Default values for many settings reformatted to appear as `**Default**: X` at the beginning of the description rather than inline at the end, making them easier to scan. Affected settings include `agentPushNotifEnabled`, `autoCompactEnabled`, `autoMemoryEnabled`, `autoScrollEnabled`, `autoUpdatesChannel`, `cleanupPeriodDays`, `defaultShell`, `disableWorkflows`, `editorMode`, `fileCheckpointingEnabled`, `inputNeededNotifEnabled`, `maxSkillDescriptionChars`, `parentSettingsBehavior`, `plansDirectory`, `preferredNotifChannel`, `respectGitignore`, `respondToBashCommands`, `showClearContextOnPlanAccept`, `showThinkingSummaries`, `showTurnDuration`, `skillListingBudgetFraction`, `spinnerTipsEnabled`, `teammateMode`, `terminalProgressBarEnabled`, `theme`, `useAutoModeDuringPlan`, `verbose`, `wheelScrollAccelerationEnabled`, `workflowKeywordTriggerEnabled`, and global config keys. [[lines 178-296](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/settings.md?plain=1#L178-L296)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Minor wording improvements throughout; no functional changes.

#### [What's New](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/whats-new.md) [[Source](https://code.claude.com/docs/en/whats-new)]

* Added Week 25 (June 15–19) and Week 26 (June 22–26) summary entries. [[lines 5-24](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/claude-code/whats-new.md?plain=1#L5-L24)] [[Source](https://code.claude.com/docs/en/whats-new#week-26)]

-----

## API changes

### Changed documents

#### [Build a tool-using agent](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/build-a-tool-using-agent.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent)]

* Example email addresses changed to `[email protected]`/`[email protected]` format (minor cosmetic change).

#### [Handle tool calls](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]

* Added critical new rule: when an assistant turn calls both a server tool and a client tool, the user reply must contain **only** `tool_result` blocks — text after the results ends the turn early and causes a 400 error naming the unresolved server tool. [[line 40](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md?plain=1#L40)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]
* Added callout explaining mixed client+server responses: the server tool result arrives in a later response after you return the client `tool_result` blocks. [[lines 90-94](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/handle-tool-calls.md?plain=1#L90-L94)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/handle-tool-calls)]

#### [How tool use works](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/how-tool-use-works.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)]

* Added explanation of when the server-side loop hands control back: if Claude calls a server tool and a client tool in the same parallel group, the response returns `stop_reason: "tool_use"` with a `server_tool_use` block that has no result yet; the API runs the server tool after you return the client tool results. [[lines 58-60](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/how-tool-use-works.md?plain=1#L58-L60)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)]
* All tool type references now link to their individual documentation pages.

#### [Overview (tool use)](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Major restructure: added a "When Claude uses tools" section explaining steering behavior (system prompt instructions, `tool_choice`). [[lines 41-53](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L41-L53)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]
* New "Choose a tool" section with subsections for your own tools, Anthropic-schema client tools, and server tools — each linking to the relevant docs. [[lines 57-95](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L57-L95)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]
* Opening example updated to clarify it uses the Web search server tool specifically.
* Clarified that server tools can appear without their result block when called alongside client tools in the same turn.

#### [Server tools](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/server-tools.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]

* Added `allowed_callers` explanation: controls whether a tool is invoked directly by Claude (`"direct"`), from inside a code execution container, or both. The `_20260209` versions of web tools default to `code_execution` caller only, and models that don't support programmatic tool calling require `allowed_callers: ["direct"]`. [[lines 103-108](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/server-tools.md?plain=1#L103-L108)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]
* Domain filtering section now includes a code example showing `allowed_domains` on the tool object. [[lines 115-122](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/server-tools.md?plain=1#L115-L122)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]
* Added distinction between web search and web fetch for subpath matching: web search matches subpaths, but web fetch matches on domain only. [[line 131](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/server-tools.md?plain=1#L131)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools)]
* `pause_turn` section expanded: added "Repeat as needed" guidance to check `stop_reason` on each response and continue until a non-pause stop reason is received.
* Added cURL/CLI to the language selector for the `pause_turn` example.
* Noted that a paused turn can end with an unfinished `server_tool_use` block, and the API returns a validation error if that tool is missing from the continuation request.

#### [Troubleshooting tool use](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

* Added new error row: `was found without a corresponding <name>_tool_result block` — caused by a `server_tool_use` block with no result (usually when Claude called it alongside a client tool) and the next user message ended the turn early or didn't include the server tool. Fix: send only `tool_result` blocks for client tools and keep the same `tools` array. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/5a8d759adfd68e218433c30a478bdf4787813747/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

#### API reference files (admin and beta)

A large number of API reference files (`docs-md/api/api/admin/**`, `docs-md/api/api/beta/**`) had their inline "ModelsExpand Collapse" schema documentation sections removed. These files covered the Admin API (analytics, federation, invites, MCP tunnels, service accounts, spend limits, users, workspaces) and the Beta API (agents, deployments, environments, files, memory stores, messages, models, sessions). Internal cross-reference links were also updated from pointing to the top-level `api/beta.md` to the correct individual sub-pages. These are structural cleanup changes with no functional impact on API behavior.
