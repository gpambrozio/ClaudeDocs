# [Claude docs changes for January 17th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/d5088b6) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/d5088b6)]

## Executive Summary
- Three new versions released (2.1.10-2.1.12): New `Setup` hook event, improved file suggestions, and MCP connection fixes
- Agent SDK MCP documentation completely rewritten with new quickstart, authentication, and troubleshooting sections
- `dontAsk` permission mode replaced with `plan` mode for safer autonomous operation

## New Claude Code versions

### [2.1.10](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/versions/2.1.10.md)

#### New features

* Added new `Setup` hook event that can be triggered via `--init`, `--init-only`, or `--maintenance` CLI flags for repository setup and maintenance operations
* Added keyboard shortcut 'c' to copy OAuth URL when browser doesn't open automatically during login

#### Existing feature improvements

* Improved startup to capture keystrokes typed before the REPL is fully ready
* Improved file suggestions to show as removable attachments instead of inserting text when accepted
* [VSCode] Added install count display to plugin listings
* [VSCode] Added trust warning when installing plugins

#### Major bug fixes

* Fixed a crash when running bash commands containing heredocs with JavaScript template literals like `${index + 1}`

### [2.1.11](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/versions/2.1.11.md)

#### Major bug fixes

* Fixed excessive MCP connection requests for HTTP/SSE transports

### [2.1.12](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/versions/2.1.12.md)

#### Major bug fixes

* Fixed message rendering bug

-----

## Claude Code changes

### Changed documents

#### [costs](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Added information about the new `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` environment variable for triggering compaction earlier than the default 95% threshold. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/costs.md?plain=1#L57)] [[Source](https://code.claude.com/docs/en/costs#reduce-token-usage)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added new `spinnerTipsEnabled` setting to show/hide tips in the spinner while Claude is working. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added new `terminalProgressBarEnabled` setting to enable/disable the terminal progress bar in Windows Terminal and iTerm2. [[line 164](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L164)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Added new `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` environment variable to control when auto-compaction triggers. [[line 768](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L768)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added new `CLAUDE_CODE_EXIT_AFTER_STOP_DELAY` environment variable for automated workflows using SDK mode. [[line 776](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L776)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added new `CLAUDE_CODE_PROXY_RESOLVES_HOSTS` environment variable for proxy DNS resolution. [[line 777](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L777)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Updated `CLAUDE_CODE_MAX_OUTPUT_TOKENS` description with default (32,000) and maximum (64,000) values, plus note about context window impact. [[line 784](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L784)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added new `FORCE_AUTOUPDATE_PLUGINS` environment variable to force plugin auto-updates. [[line 807](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L807)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Added new `IS_DEMO` environment variable to enable demo mode for streaming/recording. [[line 810](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L810)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]
* Renamed `BashOutput` tool to `TaskOutput` for retrieving output from background tasks (bash shell or subagent). [[line 832](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L832)] [[Source](https://code.claude.com/docs/en/settings#tools-available-to-claude)]
* Added new `MCPSearch` tool for searching and loading MCP tools when tool search is enabled. [[line 838](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/settings.md?plain=1#L838)] [[Source](https://code.claude.com/docs/en/settings#tools-available-to-claude)]

#### [sub-agents](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/sub-agents.md) [[Source](https://code.claude.com/docs/en/sub-agents)]

* Added information about `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` environment variable for controlling subagent auto-compaction threshold. [[line 550](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/claude-code/sub-agents.md?plain=1#L550)] [[Source](https://code.claude.com/docs/en/sub-agents#auto-compaction)]

-----

## API changes

### Changed documents

#### [agent-sdk/mcp](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/mcp.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp)]

* Complete rewrite of the MCP documentation with improved structure and new sections. [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp)]
* Renamed document from "MCP in the SDK" to "Connect to external tools with MCP". [[line 1](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/mcp.md?plain=1#L1)] [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp)]
* Added new Quickstart section with working example using Claude Code documentation MCP server. [[lines 9-36](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/mcp.md?plain=1#L9-L36)] [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp#quickstart)]
* Added "Allow MCP tools" section explaining tool naming conventions and permissions. [[lines 84-135](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/mcp.md?plain=1#L84-L135)] [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp#allow-mcp-tools)]
* Added "MCP tool search" section for dynamic tool loading with `ENABLE_TOOL_SEARCH` configuration. [[lines 209-245](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/mcp.md?plain=1#L209-L245)] [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp#mcp-tool-search)]
* Added "Authentication" section covering environment variables, HTTP headers, and OAuth2. [[lines 247-333](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/mcp.md?plain=1#L247-L333)] [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp#authentication)]
* Added working examples for listing GitHub issues and querying databases. [[lines 335-419](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/mcp.md?plain=1#L335-L419)] [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp#examples)]
* Added "Troubleshooting" section for common MCP issues. [[lines 456-496](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/mcp.md?plain=1#L456-L496)] [[Source](https://platform.claude.com/docs/en/agent-sdk/mcp#troubleshooting)]

#### [agent-sdk/permissions](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/permissions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]

* Removed `dontAsk` permission mode from available modes. [[line 53](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/permissions.md?plain=1#L53)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions#available-modes)]
* Added `plan` permission mode that prevents tool execution (Claude plans without making changes). [[lines 55, 111-115](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/permissions.md?plain=1#L55)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions#available-modes)]

#### [agent-sdk/user-input](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/user-input.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/user-input)]

* Added note that clarifying questions are especially common in `plan` mode, making it ideal for interactive workflows. [[line 196](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/agent-sdk/user-input.md?plain=1#L196)] [[Source](https://platform.claude.com/docs/en/agent-sdk/user-input#handle-clarifying-questions)]

#### [api/go/beta/files/upload](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/api/go/beta/files/upload.md) [[Source](https://platform.claude.com/docs/en/api/go/beta/files/upload)]

* Added Go code example for file upload with the Anthropic SDK. [[lines 27-55](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/api/go/beta/files/upload.md?plain=1#L27-L55)] [[Source](https://platform.claude.com/docs/en/api/go/beta/files/upload)]

#### [build-with-claude/files](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact email link for higher rate limits. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/d5088b6/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files#rate-limits)]
