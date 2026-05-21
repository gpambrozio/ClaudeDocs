# [Claude docs changes for May 21st, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/1d19986fb9178359dd36f68e9f2d3694764d4e77) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/1d19986fb9178359dd36f68e9f2d3694764d4e77)]

## Executive Summary
- **Claude Code 2.1.146** renames `/simplify` to `/code-review` (with optional effort level) and fixes 13 bugs including Windows PowerShell failures, MCP pagination dropping items, and `CLAUDE_CODE_SUBAGENT_MODEL` not forwarding to child processes
- **New `strictPluginOnlyCustomization` managed setting** lets enterprise admins lock all customization (skills, agents, hooks, MCP servers) to plugin or managed sources only, blocking user/project-level overrides
- **1-hour prompt caching now available on Amazon Bedrock** — the feature availability table and caching docs are updated to reflect this expansion
- **Hooks clarification**: exit 0 in a `PreToolUse` hook no longer implies approval — the normal permission flow still applies; only exit 2 or JSON output with `decision: "deny"` affects the outcome
- **New Prompt Library doc** for Claude Code provides curated prompts organized by workflow category (understand, plan, build, test, refactor, etc.)

## New Claude Code versions

### [2.1.146](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/versions/2.1.146.md)

#### New features

* Renamed `/simplify` to `/code-review` with an optional effort level (e.g. `/code-review high`)

#### Existing feature improvements

* Auto mode no longer suppresses `AskUserQuestion` when the user or a skill explicitly relies on it
* Improved auto-updater reliability: native version checks and downloads now retry transient network failures instead of failing immediately
* Improved diff rendering performance for large file edits

#### Major bug fixes

* Fixed Windows PowerShell tool failing with "command line is invalid" when `pwsh` is installed via winget or the Microsoft Store (regression in v2.1.124)
* Fixed MCP `resources/list`, `resources/templates/list`, and `prompts/list` dropping items past page 1 on paginating servers
* Fixed full-screen strobing in attached background sessions on Windows Terminal while Claude is streaming
* Fixed `/background` refusing sessions whose only typed input was a skill or custom slash command
* Fixed backgrounded sessions re-prompting for tool permissions you already granted with "don't ask again"
* Fixed `forceLoginOrgUUID` and `forceLoginMethod` managed-settings policies not being enforced against third-party-provider and API-key sessions
* Fixed `CLAUDE_CODE_SUBAGENT_MODEL` not being forwarded to child processes in multi-agent sessions
* Fixed uncaught exception at the end of streaming sessions when running via the Agent SDK
* Fixed auto-updater status line not showing your current version when an update fails
* Fixed on Windows, removing a background-job worktree no longer follows NTFS junctions into the main repo
* Fixed `/theme` color editor and "New custom theme" dialogs not responding to Esc
* Fixed GNOME Terminal right-click and middle-click paste not inserting text

-----

## Claude Code changes

### New Documents

#### [Prompt library](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/prompt-library.md) [[Source](https://code.claude.com/docs/en/prompt-library)]

New file introducing a curated library of prompts organized by workflow category (Start here, Understand, Plan, Prototype, Build, Test, Refactor, Review, Debug, Git, Release, and more). Includes 52 prompts drawn from Anthropic guides and real team workflows, plus an explanation of the prompting patterns that make them work (outcome-first descriptions, self-verification steps, reference anchoring, measurable targets).

### Changed documents

#### [Admin setup](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Added `strictPluginOnlyCustomization` to the managed policies table — blocks skills, agents, hooks, and MCP servers from user and project sources so they can only come from plugins or managed settings. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/admin-setup.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/admin-setup#decide-what-to-enforce)]

#### [Checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/checkpointing.md) [[Source](https://code.claude.com/docs/en/checkpointing)]

* Clarified double `Esc` behavior: only opens the rewind menu when the prompt input is empty. If the input contains text, double `Esc` clears it instead and saves the draft to history so `Up` recalls it. [[lines 25-29](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/checkpointing.md?plain=1#L25-L29)] [[Source](https://code.claude.com/docs/en/checkpointing#rewind-and-summarize)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Clarified `/desktop` availability: requires macOS or Windows **and** a Claude subscription (not just OS). [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/commands.md?plain=1#L46)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]
* Updated `/loop` description to note that the autonomous maintenance prompt is not available everywhere. [[line 68](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/commands.md?plain=1#L68)] [[Source](https://code.claude.com/docs/en/commands#all-commands)]

#### [Desktop](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/desktop.md) [[Source](https://code.claude.com/docs/en/desktop)]

* Clarified interrupt vs. redirect behavior: clicking the stop button interrupts immediately, while typing a correction and pressing Enter sends it without stopping the running action. [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/desktop.md?plain=1#L47)] [[Source](https://code.claude.com/docs/en/desktop#work-with-code)]
* Added explicit note that `/desktop` requires a Claude subscription and is not available with API key authentication or on Bedrock, Vertex, or Foundry. [[line 579](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/desktop.md?plain=1#L579)] [[Source](https://code.claude.com/docs/en/desktop#coming-from-the-cli)]

#### [Desktop quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/desktop-quickstart.md) [[Source](https://code.claude.com/docs/en/desktop-quickstart)]

* Clarified interrupt behavior: stop button interrupts immediately; typing a correction sends it without stopping the running action. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/desktop-quickstart.md?plain=1#L95)] [[Source](https://code.claude.com/docs/en/desktop-quickstart#now-what)]

#### [Hooks guide](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Clarified that exit 0 in a `PreToolUse` hook reports no objection but does not approve the tool call — the normal permission flow still applies. [[line 529](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks-guide.md?plain=1#L529)] [[Source](https://code.claude.com/docs/en/hooks-guide#hook-output)]
* Reworded structured JSON output intro: "exit codes only let you block or stay silent" (previously said "allow or block"). [[line 540](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks-guide.md?plain=1#L540)] [[Source](https://code.claude.com/docs/en/hooks-guide#structured-json-output)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Clarified that exit 0 means "no decision" — it does not approve a `PreToolUse` tool call, and the normal permission flow continues. Multiple locations updated. [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L90)] [[Source](https://code.claude.com/docs/en/hooks#how-a-hook-resolves)]
* `suppressOutput` clarified: hides hook stdout from the transcript (not just the debug log). [[line 661](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L661)] [[Source](https://code.claude.com/docs/en/hooks#json-output)]
* Added `SessionStart, Setup, SubagentStart` row to the hook event decision table — these events only support context injection via `hookSpecificOutput.additionalContext`; SessionStart also accepts `initialUserMessage` and `watchPaths`. [[line 744](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L744)] [[Source](https://code.claude.com/docs/en/hooks#decision-control)]
* New `initialUserMessage` SessionStart output field: sets the first user message in non-interactive (`-p`) mode. [[line 831](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L831)] [[Source](https://code.claude.com/docs/en/hooks#sessionstart-decision-control)]
* New `watchPaths` SessionStart output field: array of absolute paths to watch for `FileChanged` events during the session. [[line 832](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L832)] [[Source](https://code.claude.com/docs/en/hooks#sessionstart-decision-control)]
* New `suppressOriginalPrompt` field for `UserPromptSubmit` block decisions: when `true`, omits the original prompt text from the block message shown to the user. [[line 1004](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L1004)] [[Source](https://code.claude.com/docs/en/hooks#userpromptsubmit-decision-control)]
* `setMode` permission mode now includes `auto` as a valid value. [[line 1340](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L1340)] [[Source](https://code.claude.com/docs/en/hooks#permission-update-entries)]
* `session_crons` in Stop hook input now lists `ScheduleWakeup` as a source alongside `CronCreate` and `/loop`. [[line 1821](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L1821)] [[Source](https://code.claude.com/docs/en/hooks#stop-input)]
* `PermissionDenied` and `TeammateIdle` events upgraded to support all five hook types (command, http, mcp_tool, prompt, and agent); previously only supported the first three. [[lines 2382-2406](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L2382-L2406)] [[Source](https://code.claude.com/docs/en/hooks#prompt-based-hooks)]
* Added blocking behavior for `TeammateIdle`: supports `continueOnBlock: true` to feed the reason back to the teammate instead of stopping it. `PermissionDenied` blocking clarified: `ok: false` has no effect; only `hookSpecificOutput.retry` matters, and only from command hooks. [[lines 2476-2481](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/hooks.md?plain=1#L2476-L2481)] [[Source](https://code.claude.com/docs/en/hooks#response-schema)]

#### [How Claude Code works](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Clarified interrupt vs. steer distinction: `Esc` cancels the running tool call immediately; typing a correction and pressing `Enter` sends it without stopping the running tool. [[lines 173-177](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/how-claude-code-works.md?plain=1#L173-L177)] [[Source](https://code.claude.com/docs/en/how-claude-code-works#interrupt-and-steer)]

#### [Interactive mode](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* `Ctrl+C` behavior clarified: interrupts a running operation; if nothing is running, first press clears the prompt input and a second press exits Claude Code. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/interactive-mode.md?plain=1#L23)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]
* `Esc` + `Esc` behavior clarified: clears input draft (saving to history) when input contains text; opens the rewind menu only when input is empty. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/interactive-mode.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/interactive-mode#general-controls)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Added `strictPluginOnlyCustomization` to the managed-only settings table. [[line 311](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/permissions.md?plain=1#L311)] [[Source](https://code.claude.com/docs/en/permissions#managed-only-settings)]

#### [Plugin marketplaces](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/plugin-marketplaces.md) [[Source](https://code.claude.com/docs/en/plugin-marketplaces)]

* Clarified `claude plugin validate` scoping: when pointed at a marketplace directory it validates `marketplace.json` only; plugin-level validation (skills, agents, hooks) requires pointing the command at the plugin directory itself. [[lines 919-933](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/plugin-marketplaces.md?plain=1#L919-L933)] [[Source](https://code.claude.com/docs/en/plugin-marketplaces#marketplace-not-loading)]

#### [Scheduled tasks](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/scheduled-tasks.md) [[Source](https://code.claude.com/docs/en/scheduled-tasks)]

* Clarified that the built-in maintenance prompt is not available to everyone and is not supported on Bedrock, Vertex AI, or Microsoft Foundry. Where unavailable, `/loop` with no prompt prints the usage message instead. [[line 85](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/scheduled-tasks.md?plain=1#L85)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#run-the-built-in-maintenance-prompt)]
* Added note that `loop.md` follows the same availability restriction as the built-in maintenance prompt. [[line 110](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/scheduled-tasks.md?plain=1#L110)] [[Source](https://code.claude.com/docs/en/scheduled-tasks#customize-the-default-prompt-with-loop-md)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `strictPluginOnlyCustomization` to the settings reference table (managed settings only). [[line 237](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/settings.md?plain=1#L237)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added full documentation section for `strictPluginOnlyCustomization`: value can be `true` (lock all four surfaces) or an array naming specific surfaces (`skills`, `agents`, `hooks`, `mcp`). Requires v2.1.82 or later. [[lines 916-942](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/settings.md?plain=1#L916-L942)] [[Source](https://code.claude.com/docs/en/settings#strictpluginonlycustomization)]

#### [Tools reference](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/tools-reference.md) [[Source](https://code.claude.com/docs/en/tools-reference)]

* Added `ScheduleWakeup` tool: reschedules the next iteration of a self-paced `/loop`; Claude calls it automatically at the end of each iteration. Not available on Bedrock, Vertex AI, or Foundry. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/claude-code/tools-reference.md?plain=1#L36)] [[Source](https://code.claude.com/docs/en/tools-reference)]

-----

## API changes

### Changed documents

#### [API and data retention](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Added Claude Managed Agents and MCP tunnels to the ZDR/HIPAA eligibility table — both are not ZDR eligible and not HIPAA BAA eligible. [[lines 163-164](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L163-L164)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [Claude in Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

* Expanded "Feature support" section with detailed supported and not-supported lists, including links to individual feature docs. Supported highlights now include Bash, Computer use, Memory, and Text editor tools. Not-supported items now explicitly list URL input sources, server-side tools, agent infrastructure, and additional API endpoints. [[lines 176-204](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/claude-in-amazon-bedrock.md?plain=1#L176-L204)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock)]

#### [Claude on Amazon Bedrock (legacy)](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

* Added detailed supported and not-supported feature lists matching the current Bedrock page format. [[lines 184-204](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md?plain=1#L184-L204)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

#### [Claude on Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Added new "Data retention" section: data handling for Vertex AI is governed by Google Cloud; link to Vertex AI zero data retention docs. [[lines 109-111](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L109-L111)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]
* Added detailed supported and not-supported feature lists, including web search tool in the supported section. [[lines 125-145](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L125-L145)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [Features overview](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Batch processing availability updated: Bedrock and Vertex AI removed from the supported platforms list. [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/overview.md?plain=1#L42)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* Fine-grained tool streaming on Microsoft Foundry changed from Beta to GA. [[line 80](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/overview.md?plain=1#L80)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* 1-hour prompt caching now lists Bedrock as GA (previously Bedrock was absent). [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/overview.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [Fine-grained tool streaming](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/agents-and-tools/tool-use/fine-grained-tool-streaming.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)]

* Added C#, Go, Java, PHP, and Ruby to the SDK language tabs in code examples. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/agents-and-tools/tool-use/fine-grained-tool-streaming.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)]
* Simplified the accumulation section: notes that SDK accumulator helpers handle delta concatenation automatically; the manual pattern is only needed when reacting to partial input before the block closes. [[lines 52-57](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/agents-and-tools/tool-use/fine-grained-tool-streaming.md?plain=1#L52-L57)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)]

#### [MCP tunnels overview](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/agents-and-tools/mcp-tunnels/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)]

* Added reference to the data retention page for ZDR and HIPAA BAA eligibility. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/agents-and-tools/mcp-tunnels/overview.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-tunnels/overview)]

#### [Managed agents overview](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/overview.md) [[Source](https://platform.claude.com/docs/en/managed-agents/overview)]

* Updated research preview features list: outcomes and multiagent removed; MCP tunnels and dreaming added. [[line 93](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/overview.md?plain=1#L93)] [[Source](https://platform.claude.com/docs/en/managed-agents/overview)]
* Added explicit note that Claude Managed Agents is not ZDR or HIPAA BAA eligible due to its stateful nature, with guidance on how to delete session data. [[line 95](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/overview.md?plain=1#L95)] [[Source](https://platform.claude.com/docs/en/managed-agents/overview)]

#### [Multi-agent](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/multi-agent.md) [[Source](https://platform.claude.com/docs/en/managed-agents/multi-agent)]

* Added new "Connect agents to MCP servers" section: explains that MCP servers are agent-scoped while vault credentials are session-scoped, with a code example showing how to declare servers per agent and supply credentials via `vault_ids`. [[lines 71-114](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/multi-agent.md?plain=1#L71-L114)] [[Source](https://platform.claude.com/docs/en/managed-agents/multi-agent)]
* Clarified that all agents in a multiagent session share the same vault credentials (session-scoped). [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/multi-agent.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/managed-agents/multi-agent)]

#### [PDF support](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/pdf-support.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/pdf-support)]

* Added note that on Amazon Bedrock and Vertex AI, only base64-encoded PDF sources are currently available (URL and Files API sources are not). [[line 83](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/pdf-support.md?plain=1#L83)] [[Source](https://platform.claude.com/docs/en/build-with-claude/pdf-support)]

#### [Prompt caching](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* 1-hour cache duration is now available on Amazon Bedrock (both current and legacy integrations). [[line 438](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L438)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Self-hosted sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Added reference to the data retention page for ZDR and HIPAA BAA eligibility. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

#### [Vaults](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/vaults.md) [[Source](https://platform.claude.com/docs/en/managed-agents/vaults)]

* Added note that in multiagent sessions, vault credentials apply to every thread and authenticate any agent whose definition declares the matching MCP server. [[line 113](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/managed-agents/vaults.md?plain=1#L113)] [[Source](https://platform.claude.com/docs/en/managed-agents/vaults)]

#### [Vision](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* Added note that on Amazon Bedrock and Vertex AI, only base64-encoded image sources are currently available (URL and Files API sources are not). [[line 115](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/build-with-claude/vision.md?plain=1#L115)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

#### [Workspaces](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/manage-claude/workspaces.md) [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]

* Added new "Claude Code workspace" section: documents the auto-created workspace that appears when the first org member signs into Claude Code, its per-user API key behavior, separate rate limiting, per-user spend limits, and what happens when it is archived. [[lines 18-29](https://github.com/gpambrozio/ClaudeDocs/blob/1d19986fb9178359dd36f68e9f2d3694764d4e77/docs-md/api/manage-claude/workspaces.md?plain=1#L18-L29)] [[Source](https://platform.claude.com/docs/en/manage-claude/workspaces)]
