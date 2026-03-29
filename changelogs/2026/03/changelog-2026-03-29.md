# [Claude docs changes for March 29th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/eadec125863a7e2960680aec9148011155b8ba94) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/eadec125863a7e2960680aec9148011155b8ba94)]

## Executive Summary
- LLM gateway docs now document the `X-Claude-Code-Session-Id` request header, which proxies can use to aggregate all API requests from a single session
- `CLAUDE_CODE_SIMPLE` / `--bare` mode now allows MCP tools from `--mcp-config` to remain available
- Skill description budget halved (2%→1% of context window, 16k→8k char fallback) with per-entry 250-char cap; skill names are always included regardless of budget

## New Claude Code versions

### [2.1.87](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/versions/2.1.87.md)

#### Major bug fixes

* Fixed messages in Cowork Dispatch not getting delivered

-----

## Claude Code changes

### Changed documents

#### [Environment Variables](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/env-vars.md) [[Source](https://code.claude.com/docs/en/env-vars)]

* `CLAUDE_CODE_SIMPLE` clarified that MCP tools from `--mcp-config` are still available even in simple/bare mode. [[line 77](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/env-vars.md?plain=1#L77)] [[Source](https://code.claude.com/docs/en/env-vars)]
* `SLASH_COMMAND_TOOL_CHAR_BUDGET` default budget updated from 2%/16,000 chars to 1%/8,000 chars. [[line 118](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/env-vars.md?plain=1#L118)] [[Source](https://code.claude.com/docs/en/env-vars)]

#### [Hooks Guide](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/hooks-guide.md) [[Source](https://code.claude.com/docs/en/hooks-guide)]

* Added troubleshooting section explaining how to enable macOS notifications via `osascript` when notifications from Script Editor are silently failing — requires manually granting permission in System Settings > Notifications. [[lines 92-100](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/hooks-guide.md?plain=1#L92-L100)] [[Source](https://code.claude.com/docs/en/hooks-guide#get-notified-when-claude-needs-input)]

#### [LLM Gateway](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/llm-gateway.md) [[Source](https://code.claude.com/docs/en/llm-gateway)]

* Added documentation for the `X-Claude-Code-Session-Id` request header, which is sent on every API request and can be used by proxies to aggregate requests from a single session without parsing the request body. [[lines 28-33](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/llm-gateway.md?plain=1#L28-L33)] [[Source](https://code.claude.com/docs/en/llm-gateway#gateway-requirements)]

#### [Skills](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/skills.md) [[Source](https://code.claude.com/docs/en/skills)]

* `description` field documentation now notes that descriptions longer than 250 characters are truncated in the skill listing to reduce context usage, and recommends front-loading the key use case. [[line 175](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/skills.md?plain=1#L175)] [[Source](https://code.claude.com/docs/en/skills#frontmatter-reference)]
* Troubleshooting section renamed from "Claude doesn't see all my skills" to "Skill descriptions are cut short" with updated guidance: all skill names are always included, descriptions are shortened to fit the 1%/8,000 char budget, and each entry is capped at 250 chars. [[lines 649-653](https://github.com/gpambrozio/ClaudeDocs/blob/eadec125863a7e2960680aec9148011155b8ba94/docs-md/claude-code/skills.md?plain=1#L649-L653)] [[Source](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short)]

-----

## API changes

### Changed documents

No significant changes.
