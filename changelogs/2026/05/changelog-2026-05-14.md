# [Claude docs changes for May 14th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/e15add8) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/e15add8)]

## Executive Summary
- **Agent SDK billing change (June 15, 2026)**: `claude -p` and Agent SDK usage on subscription plans will draw from a new separate monthly credit, distinct from interactive usage limits — announced across multiple docs
- **`claude agents` gains session defaults and config flags**: new `--permission-mode`, `--model`, and `--effort` flags set defaults for all dispatched sessions; new section documents how to pass settings, plugins, and MCP servers to the agent view
- **Output styles page overhauled**: restructured with a numbered creation workflow, clearer guidance on when to use `keep-coding-instructions`, and a new comparison table against CLAUDE.md, `--append-system-prompt`, agents, and skills
- **Model lifecycle updates**: Claude Sonnet 3.7 marked as fully retired on Bedrock (April 28) and Vertex AI (May 11); explicit retirement dates added for Opus 4, Sonnet 4, and Haiku 3.5 across platforms; removed from tool/pricing tables throughout
- **Context window overflow behavior clarified**: Claude 4.5+ now accepts requests exceeding the context window and stops with `stop_reason: "model_context_window_exceeded"` instead of a validation error

## New Claude Code versions

### [2.1.141](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/versions/2.1.141.md)

#### New features

* Added `terminalSequence` field to hook JSON output so hooks can emit desktop notifications, window titles, and terminal bells without needing a controlling terminal
* Added `CLAUDE_CODE_PLUGIN_PREFER_HTTPS` environment variable to clone GitHub plugin sources over HTTPS instead of SSH, for environments without a GitHub SSH key
* Added `ANTHROPIC_WORKSPACE_ID` environment variable for workload identity federation — scopes the minted token to a specific workspace when the federation rule covers more than one
* Added `claude agents --cwd <path>` to scope the session list to a specific directory
* `/feedback` can now include recent sessions (last 24 hours or 7 days) for issues that span more than the current session
* Rewind menu: added "Summarize up to here" to compress earlier context while keeping recent turns intact
* Auto mode permission dialog now explains when a `permissions.ask` rule caused the prompt
* Restored the "view diff in your IDE" option on file-edit permission prompts when an IDE is connected

#### Existing feature improvements

* Background agents launched via `/bg` or `←←` now preserve the current permission mode instead of reverting to default
* `claude agents`: agents that finish work but leave a background shell running now move to Completed instead of staying as Working
* Spinner warms to amber after 10 seconds of thinking to signal Claude is still working
* Improved plugin menu navigation: `→`/Tab switch tabs, `↑` moves to the tab strip, and tab headers and search box are clickable in fullscreen mode
* Background side-queries on Bedrock/Vertex/Foundry/gateway now fall back to the main-loop model when no `ANTHROPIC_SMALL_FAST_MODEL` is set, instead of sending an unavailable Haiku model ID
* `claude agents` launching no longer fails when the pre-warmed background worker is unhealthy — now falls back to a fresh launch
* Empty idle background sessions left over from `←` are automatically retired by the daemon after 5 minutes

#### Major bug fixes

* Fixed `/model` in one session silently changing the autocompact threshold in other concurrent sessions
* Fixed hooks receiving a non-existent `transcript_path` after `EnterWorktree` switches the working directory
* Fixed markdown tables with cell wrapping falling back to the vertical key-value layout instead of rendering as a bordered grid (regression in 2.1.136)
* Fixed Ctrl+C not interrupting a running turn while in vim INSERT/VISUAL mode
* Fixed alternative `chat:submit` keybindings (e.g. `meta+enter`, `ctrl+enter`) not working when `enter` is rebound to `chat:newline`
* Fixed prompt suggestions being silently disabled when an output style was configured
* Fixed `/tui` silently dropping running background shells and subagents — now refuses and asks to wait for them to finish
* Fixed Bedrock `awsCredentialExport` being skipped when ambient AWS credentials resolve, fixing auth for cross-account access
* Fixed Remote Control MCP connectors all failing with 401 when the worker session token rotated mid-session
* Fixed SDK "Claude Code native binary not found" on Linux when both glibc and musl platform packages are installed
* Fixed MCP HTTP/SSE servers returning 403 on connect showing as "failed" instead of "needs auth"
* Fixed plugin details pane showing 0 MCP servers for plugins that declare them via `.mcp.json`
* Fixed Web Search status showing "Did 0 searches" when searches returned errors

-----

## Claude Code changes

### Changed documents

#### [Admin Setup](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/admin-setup.md) [[Source](https://code.claude.com/docs/en/admin-setup)]

* Added a note that several Claude Code features (web, Routines, Code Review, Remote Control, Chrome extension) require a Claude.ai account and are not available through Console API keys or cloud-provider credentials alone — relevant for teams deploying via Bedrock, Vertex, or Foundry [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/admin-setup.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/admin-setup)]

#### [Agent SDK - Modifying System Prompts](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-sdk/modifying-system-prompts.md) [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts)]

* Clarified that a custom output style replaces `claude_code` preset's software engineering instructions by default; set `keep-coding-instructions: true` in the frontmatter to keep them and layer your instructions on top [[lines 30-34](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L30-L34)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#decide-on-a-starting-point)]
* Updated the code-review example to include `keep-coding-instructions: true` in the frontmatter [[line 42](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L42)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#decide-on-a-starting-point)]
* Updated comparison table: output styles column now reads "Replace or extend default" to reflect the new `keep-coding-instructions` option [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-sdk/modifying-system-prompts.md?plain=1#L51)] [[Source](https://code.claude.com/docs/en/agent-sdk/modifying-system-prompts#claude-md-files-for-project-level-instructions)]

#### [Agent SDK - Overview](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-sdk/overview.md) [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

* Added notice: starting June 15, 2026, Agent SDK and `claude -p` usage on subscription plans will draw from a new monthly Agent SDK credit, separate from interactive usage limits [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-sdk/overview.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/agent-sdk/overview)]

#### [Agent View](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-view.md) [[Source](https://code.claude.com/docs/en/agent-view)]

* "Permission mode and settings" section renamed to "Permission mode, model, and effort" and expanded: `claude agents` now accepts `--permission-mode`, `--model`, and `--effort` flags that set defaults for every session dispatched from that agent view instance; active defaults appear in the footer [[lines 108-121](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-view.md?plain=1#L108-L121)] [[Source](https://code.claude.com/docs/en/agent-view#read-session-state)]
* New "Settings, plugins, and MCP servers" section documents how to pass `--settings`, `--add-dir`, `--plugin-dir`, `--mcp-config`, and `--strict-mcp-config` to `claude agents` — these apply to agent view itself and to every session dispatched from it [[lines 123-141](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-view.md?plain=1#L123-L141)] [[Source](https://code.claude.com/docs/en/agent-view#pull-request-status)]
* Clarified that backgrounding a session also does not transfer running monitors (in addition to subagents and background commands) [[line 91](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/agent-view.md?plain=1#L91)] [[Source](https://code.claude.com/docs/en/agent-view#monitor-sessions-with-agent-view)]

#### [Authentication](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/authentication.md) [[Source](https://code.claude.com/docs/en/authentication)]

* Added notice about the Agent SDK credit starting June 15, 2026 in the "Generate a long-lived token" section [[line 152](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/authentication.md?plain=1#L152)] [[Source](https://code.claude.com/docs/en/authentication#authentication-precedence)]

#### [Claude Platform on AWS](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/claude-platform-on-aws.md) [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

* Added enterprise deployment callout at the top of the page with links to pricing and sales contact [[lines 9-11](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/claude-platform-on-aws.md?plain=1#L9-L11)] [[Source](https://code.claude.com/docs/en/claude-platform-on-aws)]

#### [Commands](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/commands.md) [[Source](https://code.claude.com/docs/en/commands)]

* Removed the "through May 5, 2026" expiration date from the `/ultrareview` free runs description — the 3 free runs are now described as a standing one-time allotment with no expiry date [[line 181](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/commands.md?plain=1#L181)] [[Source](https://code.claude.com/docs/en/commands#see-also)]

#### [Fast Mode](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Fast mode pricing updated from `$30/150 MTok` to a 4-tier rate `30/30/30/150 MTok` for both Opus 4.6 and Opus 4.7 [[line 194](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/fast-mode.md?plain=1#L194)] [[Source](https://code.claude.com/docs/en/fast-mode#see-also)]

#### [Headless](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/headless.md) [[Source](https://code.claude.com/docs/en/headless)]

* Added notice about the Agent SDK credit starting June 15, 2026 at the top of the page [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/headless.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/headless)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Clarified that `disableAllHooks: true` only disables user-configured hooks — hooks configured in managed settings continue to run unless `disableAllHooks` is also set there [[line 226](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/hooks-guide.md?plain=1#L226)] [[Source](https://code.claude.com/docs/en/hooks-guide#block-edits-to-protected-files)]

#### [Legal and Compliance](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/legal-and-compliance.md) [[Source](https://code.claude.com/docs/en/legal-and-compliance)]

* Added notice about the Agent SDK credit starting June 15, 2026 at the top of the page [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/legal-and-compliance.md?plain=1#L9)] [[Source](https://code.claude.com/docs/en/legal-and-compliance)]

#### [Memory](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/memory.md) [[Source](https://code.claude.com/docs/en/memory)]

* Updated the CLAUDE.md locations table to show explicit load order from broadest to most specific scope; corrected the row ordering so "User instructions" appears before "Project instructions", matching actual load order [[lines 252-260](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/memory.md?plain=1#L252-L260)] [[Source](https://code.claude.com/docs/en/memory#deploy-organization-wide-claude-md)]

#### [Output Styles](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/output-styles.md) [[Source](https://code.claude.com/docs/en/output-styles)]

* Page substantially rewritten and restructured: custom output style creation is now presented as a 3-step numbered guide (create file → add frontmatter/instructions → switch to style) [[lines 346-393](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/output-styles.md?plain=1#L346-L393)] [[Source](https://code.claude.com/docs/en/output-styles#related-resources)]
* Clarified that custom styles exclude Claude Code's built-in software engineering instructions unless `keep-coding-instructions: true` is set in the frontmatter [[line 273](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/output-styles.md?plain=1#L273)] [[Source](https://code.claude.com/docs/en/output-styles#related-resources)]
* Comparisons section replaced with a concise table comparing output styles, CLAUDE.md, `--append-system-prompt`, agents, and skills [[lines 447-454](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/output-styles.md?plain=1#L447-L454)] [[Source](https://code.claude.com/docs/en/output-styles#related-resources)]
* Added "Related resources" section with links to settings, permission modes, plugins, and debug config [[lines 456-461](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/output-styles.md?plain=1#L456-L461)] [[Source](https://code.claude.com/docs/en/output-styles#related-resources)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Clarified deny rule precedence: a user-level deny blocks a project-level allow (and vice versa) because deny rules from any scope are evaluated before allow rules [[line 473](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/permissions.md?plain=1#L473)] [[Source](https://code.claude.com/docs/en/permissions#see-also)]

#### [Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Clarified that both force-enabled and force-disabled plugins in managed settings cannot be overridden by `--plugin-dir` (previously only force-enabled was mentioned) [[line 486](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/plugins.md?plain=1#L486)] [[Source](https://code.claude.com/docs/en/plugins#for-plugin-developers)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Clarified how scopes interact: scalar settings from higher-priority scopes override lower ones; array settings (like permission rules) concatenate and deduplicate across scopes rather than replace [[lines 499-527](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/settings.md?plain=1#L499-L527)] [[Source](https://code.claude.com/docs/en/settings#settings-precedence)]
* Updated examples to distinguish scalar vs. array setting behavior and avoid using permission rules as the example for simple override [[lines 508-517](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/settings.md?plain=1#L508-L517)] [[Source](https://code.claude.com/docs/en/settings#settings-precedence)]

#### [Ultrareview](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/ultrareview.md) [[Source](https://code.claude.com/docs/en/ultrareview)]

* Removed the "expire on May 5, 2026" language from the free runs description — the 3 free runs are now described as a permanent one-time allotment that does not refresh or expire [[lines 540-545](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/claude-code/ultrareview.md?plain=1#L540-L545)] [[Source](https://code.claude.com/docs/en/ultrareview#related-resources)]

-----

## API changes

### Changed documents

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Removed references to Claude Sonnet 3.7 migration; updated summarization description to remove the "easy migration from Claude Sonnet 3.7" framing [[lines 168-175](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L168-L175)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Batch Processing](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Removed older models (Claude Sonnet 3.7, Haiku 3.5, Opus 3, Haiku 3) from the Batches API pricing table; added deprecation/retirement labels to Claude Opus 4, Sonnet 4, and Haiku 3.5 [[lines 187-198](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/batch-processing.md?plain=1#L187-L198)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

#### [Claude on Amazon Bedrock (Legacy)](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

* Added a note explaining that lifecycle terms and dates in the Bedrock table are set independently by AWS and may differ from the Anthropic-operated schedule [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md?plain=1#L210)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]
* Updated model table: Claude Sonnet 3.7 now marked as "Retired April 28, 2026" with all regions removed; Claude Opus 4 retiring May 31 2026; Claude Sonnet 4 retiring October 14 2026; Claude Haiku 3.5 retiring June 19 2026 [[lines 219-227](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/claude-on-amazon-bedrock-legacy.md?plain=1#L219-L227)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy)]

#### [Claude on Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Added a note explaining that lifecycle terms and dates in the Vertex AI table are set independently by Google Cloud [[line 239](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L239)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]
* Updated model table: Claude Sonnet 3.7 marked as "Retired May 11, 2026"; Claude Opus 4 and Sonnet 4 retiring September 14 2026; Claude Haiku 3.5 retiring July 5 2026 [[lines 247-257](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L247-L257)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

#### [Code Execution Tool](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Removed Claude Sonnet 3.7 and Claude Haiku 3.5 from the supported models table for the code execution tool [[lines 9-10](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L9-L10)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Computer Use Tool](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Updated beta header documentation: removed references to Sonnet 3.7 from the beta version table and added Claude Haiku 4.5 and Opus 4 ([deprecated]) to the `computer-use-2025-01-24` list [[lines 27-28](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L27-L28)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]
* Simplified the sampling loop code example: removed `thinking_budget` parameter, the `text_editor_type` variable, and the optional thinking block — uses `text_editor_20250728` unconditionally [[lines 47-89](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L47-L89)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]
* Enhanced actions description changed from "Available in Claude 4 models and Claude Sonnet 3.7" to "Available on all models that support computer use" [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]
* Removed Claude Sonnet 3.7 row from the tool token pricing table [[line 120](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L120)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

#### [Context Windows](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Section renamed "Context window overflow behavior" and content updated: on Claude 4.5 models and newer, requests that exceed the context window are accepted and generation stops with `stop_reason: "model_context_window_exceeded"`; older models still return a validation error but can opt in with the `model-context-window-exceeded-2025-08-26` beta header [[line 282](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/context-windows.md?plain=1#L282)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

#### [Dreams](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/managed-agents/dreams.md) [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]

* Sessions parameter is now required (1 to 100) rather than optional (0 to 100) when creating a dream [[lines 484-493](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/managed-agents/dreams.md?plain=1#L484-L493)] [[Source](https://platform.claude.com/docs/en/managed-agents/dreams)]

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Removed Claude Sonnet 3.7 from the thinking model comparison table; Opus 4.7 now shows thinking output as "Omitted by default" (matching Opus 4.6), and the table is condensed from 7 columns to 6 [[lines 365-374](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L365-L374)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Updated context window behavior: on Claude 4.5+ models, `max_tokens` exceeding the context window now stops with `model_context_window_exceeded` instead of a validation error; older behavior documented alongside [[line 335](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L335)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Removed note about Claude Sonnet 3.7 returning full (non-summarized) thinking output [[lines 321-322](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L321-L322)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Simplified the supported models description: images are now described as supported on "all current Claude models" rather than "all Claude 3+ models"; PDF and code execution tool support now deferred to their respective linked pages [[line 387](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/files.md?plain=1#L387)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Tool Use - Overview](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Updated the tool token counts table: removed Claude Sonnet 3.7, Haiku 3.5, Opus 3, Sonnet 3, and Haiku 3; added deprecation/retirement labels to Claude Opus 4, Sonnet 4, and Haiku 3.5 [[lines 132-144](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L132-L144)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

#### [Prompt Caching](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Updated pricing table: removed Claude Sonnet 3.7, Haiku 3.5, Opus 3, and Haiku 3; added deprecation/retirement labels to Claude Opus 4, Sonnet 4, and Haiku 3.5 [[lines 408-419](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L408-L419)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]
* Updated minimum cacheable prompt lengths: Claude Sonnet 4.6 minimum lowered from 2,048 to 1,024 tokens (grouped with Sonnet 4.5, Opus 4.1, Opus 4, Sonnet 4); cache minimums section now notes platform differences and adds a separate callout for Bedrock's own prompt caching documentation [[lines 428-447](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L428-L447)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Search Results](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/search-results.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

* Removed Claude Sonnet 3.7 from the supported models list; updated Claude Haiku 3.5 status to "retired, except on Bedrock and Vertex AI" [[lines 468-471](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/build-with-claude/search-results.md?plain=1#L468-L471)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

#### [Text Editor Tool](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/text-editor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)]

* Removed the `text_editor_20250124` (Claude Sonnet 3.7) row from the additional input token pricing table [[line 156](https://github.com/gpambrozio/ClaudeDocs/blob/e15add8/docs-md/api/agents-and-tools/tool-use/text-editor-tool.md?plain=1#L156)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/text-editor-tool)]
