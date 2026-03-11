# [Claude docs changes for March 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849)]

## Executive Summary
- New `/btw` slash command lets you ask quick side questions without adding to conversation history — runs independently even while Claude is working, and answers appear in a dismissible overlay
- Plugin development workflow improved: `/reload-plugins` now hot-reloads plugins without a full restart (LSP config changes still require restart)
- Files API documentation updated with better code examples using `$FILE_ID` variable instead of hardcoded IDs, and clarified storage/retention language

-----

## Claude Code changes

### Changed documents

#### [best-practices](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/best-practices.md) [[Source](https://code.claude.com/docs/en/best-practices)]

* Added recommendation to use `/btw` for quick questions that don't need to stay in context — the answer appears in a dismissible overlay and never enters conversation history. [[line 425](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/best-practices.md?plain=1#L425)] [[Source](https://code.claude.com/docs/en/best-practices#manage-context-aggressively)]

#### [discover-plugins](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/discover-plugins.md) [[Source](https://code.claude.com/docs/en/discover-plugins)]

* When auto-update updates installed plugins, the notification now prompts users to run `/reload-plugins` instead of suggesting a full restart of Claude Code. [[line 444](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/discover-plugins.md?plain=1#L444)] [[Source](https://code.claude.com/docs/en/discover-plugins#configure-auto-updates)]

#### [interactive-mode](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/interactive-mode.md) [[Source](https://code.claude.com/docs/en/interactive-mode)]

* Added `/btw <question>` to the slash command table for asking side questions without adding to conversation history. [[line 81](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/interactive-mode.md?plain=1#L81)] [[Source](https://code.claude.com/docs/en/interactive-mode#built-in-commands)]
* New full section documenting "Side questions with /btw": can run while Claude is working, has no tool access, is single-response only, reuses the parent conversation's prompt cache (low cost), and is dismissed with Space/Enter/Escape. [[lines 318-344](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/interactive-mode.md?plain=1#L318-L344)] [[Source](https://code.claude.com/docs/en/interactive-mode#side-questions-with-/btw)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* MCP server listing reordered and updated with new entries in the marketplace.

#### [plugins](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Plugin development instructions updated to use `/reload-plugins` instead of restarting Claude Code to pick up changes. Changes to LSP server configuration still require a full restart. [[lines 198, 284, 354](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/plugins.md?plain=1#L198)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added guidance to use `/btw` instead of a subagent when you only need a quick answer about something already in your conversation context (no tool access, answer is discarded rather than added to history). [[line 676](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/claude-code/sub-agents.md?plain=1#L676)] [[Source](https://code.claude.com/docs/en/sub-agents#choose-between-subagents-and-main-conversation)]

-----

## API changes

### Changed documents

#### [agent-sdk/python](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* Internal anchor links in the API reference table updated to use kebab-case format (e.g., `#sdkbeta` → `#sdk-beta`, `#canusetool` → `#can-use-tool`) for correctness.

#### [agent-sdk/typescript](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Internal anchor links in the API reference table updated to use kebab-case format (same pattern as Python SDK fixes).

#### [agents-and-tools/remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP servers added to the remote server listing: **Daloopa** (financial fundamental data), **Airtable** (structured data), **Close** (CRM), **Supermetrics** (marketing analytics), **Sanity** (content management), **Stytch** (authentication), **Postman** (API context for agents), **Gusto** (HR/payroll data), **Harmonic** (company research), **Jotform** (forms), **Base44** (app building), **PagerDuty** (incident management), **Brex** (finance automation).
* Various existing entries reordered within the listing.

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Code examples updated to use `$FILE_ID` environment variable instead of a hardcoded example file ID, making examples easier to copy and use. [[lines 67-96](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/api/build-with-claude/files.md?plain=1#L67-L96)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]
* Retrieve, delete, and download file curl examples similarly updated to use `$FILE_ID`. [[lines 193, 206, 219](https://github.com/gpambrozio/ClaudeDocs/blob/d9b9cb9203582fa32c4c71ccf0dc73ab5d824849/docs-md/api/build-with-claude/files.md?plain=1#L193)]
