# [Claude docs changes for March 6th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/59b0770b0075627aadd37fbfdd656f8b447d174a) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/59b0770b0075627aadd37fbfdd656f8b447d174a)]

## Executive Summary
- Remote Control is now available on all plans (Pro, Max, Team, Enterprise), no longer limited to Max/Pro research preview
- VS Code gained three major features: an Activity Bar sessions panel, full markdown plan document view with inline comment support, and a native MCP server management dialog via `/mcp`
- ZDR eligibility clarified for web search/fetch tools: the dynamic filtering versions (`web_search_20260209` / `web_fetch_20260209`) are not ZDR-eligible by default, but can be restricted to direct-only invocation to qualify
- Compaction now available on Amazon Bedrock, Google Cloud Vertex AI, and Microsoft Foundry (previously Claude API only)

## New Claude Code versions

### [2.1.70](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd656f8b447d174a/versions/2.1.70.md)

#### New features

* [VSCode] Added Spark icon in VS Code Activity Bar that lists all Claude Code sessions, with sessions opening as full editor tabs
* [VSCode] Added full markdown document view for plans, with support for adding inline comments to provide feedback before Claude begins
* [VSCode] Added native MCP server management dialog — use `/mcp` in the chat panel to enable/disable servers, reconnect, and manage OAuth authentication without switching to the terminal

#### Existing feature improvements

* Improved compaction to preserve images in the summarizer request, allowing prompt cache reuse for faster and cheaper compaction
* Improved `/rename` to work while Claude is processing, instead of being silently queued
* Reduced prompt input re-renders during turns by ~74%
* Reduced Remote Control `/poll` rate to once per 10 minutes while connected (was 1–2s), cutting server load ~300×

#### Major bug fixes

* Fixed API 400 errors when using `ANTHROPIC_BASE_URL` with a third-party gateway — tool search now correctly detects proxy endpoints and disables `tool_reference` blocks
* Fixed `API Error: 400 This model does not support the effort parameter` when using custom Bedrock inference profiles or other non-standard model identifiers
* Fixed empty model responses immediately after `ToolSearch`
* Fixed prompt-cache bust when an MCP server with `instructions` connects after the first turn
* Fixed clipboard corrupting non-ASCII text (CJK, emoji) on Windows/WSL by using PowerShell `Set-Clipboard`
* Fixed voice mode failing on Windows native binary with "native audio module could not be loaded"
* Fixed push-to-talk not activating on session start when `voiceEnabled: true` was set in settings

-----

## Claude Code changes

### Changed documents

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd656f8b447d174a/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Prompt examples in code blocks no longer include a leading `>` prefix, matching actual CLI usage

#### [how-claude-code-works](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd656f8b447d174a/docs-md/claude-code/how-claude-code-works.md) [[Source](https://code.claude.com/docs/en/how-claude-code-works)]

* Prompt examples in code blocks no longer include a leading `>` prefix, matching actual CLI usage

#### [ide-integrations](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/ide-integrations.md) [[Source](https://code.claude.com/docs/en/ide-integrations)]

* Added Activity Bar entry point: the Spark icon is now always visible in the left sidebar to list all sessions; clicking opens a session as a full editor tab. [[line 37](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd6f8b447d174a/docs-md/claude-code/ide-integrations.md?plain=1#L37)] [[Source](https://code.claude.com/docs/en/ide-integrations#get-started)]
* Plan mode in VS Code now automatically opens the plan as a full markdown document where you can add inline comments before Claude begins. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/ide-integrations.md?plain=1#L66)] [[Source](https://code.claude.com/docs/en/ide-integrations#use-the-prompt-box)]
* MCP server config capability in VS Code updated to "Partial": add servers via CLI, manage existing servers with `/mcp` in the chat panel. [[line 249](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/ide-integrations.md?plain=1#L249)] [[Source](https://code.claude.com/docs/en/ide-integrations#vs-code-extension-vs-claude-code-cli)]
* Documented new `/mcp` management dialog in VS Code for enabling/disabling servers, reconnecting, and OAuth without switching to the terminal. [[line 297](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/ide-integrations.md?plain=1#L297)] [[Source](https://code.claude.com/docs/en/ide-integrations#connect-to-external-tools-with-mcp)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Updated Klaviyo MCP URL to include `?include-mcp-app=true`
* Smartsheet entry updated to require a user-specific URL instead of a fixed endpoint
* Added PostHog MCP server (query, analyze, and manage PostHog insights)
* Various reordering of MCP server entries in the directory

#### [remote-control](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/remote-control.md) [[Source](https://code.claude.com/docs/en/remote-control)]

* Remote Control is now available on **all plans** (Pro, Max, Team, Enterprise) — previously restricted to Max plan as a research preview. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/remote-control.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/remote-control)]
* Team and Enterprise admins must first enable Claude Code in admin settings before users can access Remote Control. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/remote-control.md?plain=1#L18)] [[Source](https://code.claude.com/docs/en/remote-control#requirements)]

#### [vs-code](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/claude-code/vs-code.md) [[Source](https://code.claude.com/docs/en/vs-code)]

* Added Activity Bar sessions list entry (Spark icon always visible in the left sidebar)
* Plan mode now automatically opens as a full markdown document with inline comment support
* MCP server config updated to "Partial" — add via CLI, manage with `/mcp` in the chat panel
* Documented `/mcp` management dialog for managing servers and OAuth from within VS Code

-----

## API changes

### Changed documents

#### [handling-stop-reasons](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

* Code example comments updated to clarify that `max_tokens=64000` is a practical non-streaming ceiling — Opus 4.6 supports 128K output tokens with streaming enabled. [[line 275](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L275)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

#### [overview](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Memory tool moved from the "Server-side tools" table to the "Computer use" (client-side) tools table, reflecting that it operates client-side. [[line 50](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/overview.md?plain=1#L50)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* Compaction now listed as available on Amazon Bedrock (Beta), Google Cloud Vertex AI (Beta), and Microsoft Foundry (Beta) in addition to the Claude API. [[line 51](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/overview.md?plain=1#L51)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Smartsheet entry updated to require a user-specific URL instead of a fixed endpoint
* Added Gusto MCP server (query and analyze Gusto payroll/HR data)
* Added Yardi Virtuoso MCP server (real-time Yardi data and insights)
* Various reordering of entries in the MCP server directory

#### [structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Corrected Java SDK method name from `outputFormat(Class<T>)` to `outputConfig(Class<T>)`. [[line 122](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L122)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

#### [web-fetch-tool](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Clarified ZDR eligibility: the basic tool version (`web_fetch_20250910`) is ZDR-eligible, but the dynamic filtering version (`web_fetch_20260209`) is **not** ZDR-eligible by default because it relies on code execution internally. [[lines 10-16](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L10-L16)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]
* Added instructions to disable dynamic filtering (`"allowed_callers": ["direct"]`) to use `web_fetch_20260209` with ZDR.

#### [web-search-tool](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Clarified ZDR eligibility: the basic tool version (`web_search_20250305`) is ZDR-eligible, but the dynamic filtering version (`web_search_20260209`) is **not** ZDR-eligible by default. [[lines 7-16](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L7-L16)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]
* Added instructions to disable dynamic filtering (`"allowed_callers": ["direct"]`) to use `web_search_20260209` with ZDR.

#### [zero-data-retention](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/zero-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]

* Web Search and Web Fetch ZDR eligibility entries updated with version-specific details, noting that dynamic filtering versions are not ZDR-eligible by default. [[lines 99-101](https://github.com/gpambrozio/ClaudeDocs/blob/59b0770b0075627aadd37fbfdd652f8b447d174a/docs-md/api/build-with-claude/zero-data-retention.md?plain=1#L99-L101)] [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]
* Section renamed from "Fully ZDR-eligible" to "ZDR-eligible" and language throughout changed from "covered by ZDR arrangements" to "ZDR-eligible" for consistency.
