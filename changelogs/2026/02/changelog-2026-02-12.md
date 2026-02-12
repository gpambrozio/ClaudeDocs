# [Claude docs changes for February 12th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/06c50d316c9878a31300084a15cb8be884a502e5) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/06c50d316c9878a31300084a15cb8be884a502e5)]

## Executive Summary
- Claude Code 2.1.39 released with Agent Teams model identifier fixes for Bedrock, Vertex, and Foundry customers
- Chrome integration now supports Microsoft Edge browser with native messaging configuration
- New Clarify MCP server added for CRM query and record creation
- Server-managed settings version requirement updated for Claude for Teams to 2.1.38

## New Claude Code versions

### [2.1.39](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/versions/2.1.39.md)

#### New features

* Added guard against launching Claude Code inside another Claude Code session
* Added `speed` attribute to OTel events and trace spans for fast mode visibility

#### Existing feature improvements

* Improved model error messages for Bedrock/Vertex/Foundry users with fallback suggestions
* Improved error message for many-image dimension limit errors with /compact suggestion
* Improved terminal rendering performance

#### Major bug fixes

* Fixed Agent Teams using wrong model identifier for Bedrock, Vertex, and Foundry customers
* Fixed a crash when MCP tools return image content during streaming
* Fixed /resume session previews showing raw XML tags instead of readable command names
* Fixed plugin browse showing misleading "Space to Toggle" hint for already-installed plugins
* Fixed hook blocking errors (exit code 2) not showing stderr to the user
* Fixed /resume showing interrupt messages as session titles
* Fixed Opus 4.6 launch announcement showing for Bedrock/Vertex/Foundry users
* Fixed fatal errors being swallowed instead of displayed
* Fixed process hanging after session close
* Fixed character loss at terminal screen boundary
* Fixed blank lines in verbose transcript view

-----

## Claude Code changes

### Changed documents

#### [Chrome](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/claude-code/chrome.md) [[Source](https://code.claude.com/docs/en/chrome)]

* Chrome integration now supports Microsoft Edge in addition to Google Chrome. [[line 6](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/claude-code/chrome.md?plain=1#L6)] [[Source](https://code.claude.com/docs/en/chrome)]
* Added Edge-specific native messaging host configuration paths for macOS, Linux, and Windows. [[lines 222-231](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/claude-code/chrome.md?plain=1#L222-L231)] [[Source](https://code.claude.com/docs/en/chrome#extension-not-detected)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added new MCP server: Clarify (CRM query and record creation tool) with installation command `claude mcp add --transport http clarify https://api.clarify.ai/mcp`. [[lines 31-37](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/claude-code/mcp.md?plain=1#L31-L37)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Server-managed settings](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

* Updated version requirements for server-managed settings: Claude for Teams now requires version 2.1.38 or later (was 2.1.30). [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/claude-code/server-managed-settings.md?plain=1#L13)] [[Source](https://code.claude.com/docs/en/server-managed-settings#requirements)]

-----

## API changes

### Changed documents

#### [Model deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* Updated Console Usage page URL from `/settings/usage` to `/usage`. [[line 36](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/api/about-claude/model-deprecations.md?plain=1#L36)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

#### [Rate limits](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Updated Console Usage page URL from `/settings/usage` to `/usage`. [[lines 89, 192](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/api/api/rate-limits.md?plain=1#L89)]

#### [Fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Changed pricing symbol from `<=` to `≤` for better typography in the description of fast mode pricing for prompts 200K tokens or less. [[line 46](https://github.com/gpambrozio/ClaudeDocs/blob/06c50d316c9878a31300084a15cb8be884a502e5/docs-md/api/build-with-claude/fast-mode.md?plain=1#L46)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]
