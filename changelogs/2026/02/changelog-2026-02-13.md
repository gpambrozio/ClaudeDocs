# [Claude docs changes for February 13th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/281ec02) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/281ec02)]

## Executive Summary
- Claude Code 2.1.41 adds new authentication CLI commands (`claude auth login/status/logout`) and Windows ARM64 support
- Features overview page reorganized into clearer categories: Model capabilities, Tools, Tool infrastructure, Context management, and Files & assets
- Attio CRM integration added as new remote MCP server for both Claude Code and API
- Important streaming behavior change for Claude Opus 4.6 requiring explicit continuation prompts after interruptions

## New Claude Code versions

### [2.1.41](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/versions/2.1.41.md)

#### New features

* Added `claude auth login`, `claude auth status`, and `claude auth logout` CLI subcommands for authentication management
* Added Windows ARM64 (win32-arm64) native binary support

#### Existing feature improvements

* Improved `/rename` to auto-generate session name from conversation context when called without arguments
* Improved narrow terminal layout for prompt footer

#### Major bug fixes

* Fixed AWS auth refresh hanging indefinitely by adding a 3-minute timeout
* Fixed file resolution failing for @-mentions with anchor fragments (e.g., `@README.md#installation`)
* Fixed FileReadTool blocking the process on FIFOs, `/dev/stdin`, and large files
* Fixed background task notifications not being delivered in streaming Agent SDK mode
* Fixed cursor jumping to end on each keystroke in classifier rule input
* Fixed markdown link display text being dropped for raw URL
* Fixed auto-compact failure error notifications being shown to users
* Fixed permission wait time being included in subagent elapsed time display
* Fixed proactive ticks firing while in plan mode
* Fixed clear stale permission rules when settings change on disk
* Fixed hook blocking errors showing stderr content in UI

-----

## Claude Code changes

### New Documents

#### [Attio MCP Server](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

Added Attio CRM as a new remote MCP server that allows searching, managing, and updating Attio CRM from Claude Code. [[line 761](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/claude-code/mcp.md?plain=1#L761)]

-----

## API changes

### New Documents

#### [Attio Remote MCP Server](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

Added Attio as a new remote MCP server for managing CRM data from Claude. [[line 169](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L169)]

### Changed documents

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Reorganized features page with new categorization: "Model capabilities" replaces "Core capabilities", with new sections for "Tools" (split into Server-side and Client-side), "Tool infrastructure", "Context management", and "Files & assets" for better organization. [[lines 456-542](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/overview.md?plain=1#L456-L542)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [Streaming](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/streaming.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

* Important behavioral change: For Claude Opus 4.6, error recovery from interrupted streams now requires adding a user message that explicitly instructs the model to continue (e.g., "Your previous response was interrupted and ended with [previous_response]. Continue from where you left off."). This differs from Claude 4.5 and earlier models. [[lines 605-612](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/streaming.md?plain=1#L605-L612)] [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Updated email contact link for accessing full thinking output. [[line 353](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L353)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Context Windows](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Changed code block formatting from `inline-block` to `shiki` for consistency. [[lines 386-396](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/context-windows.md?plain=1#L386-L396)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

#### [Customer Support Chat](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/about-claude/use-case-guides/customer-support-chat.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]

* Changed code block formatting from `inline-block` to `shiki` for consistency. [[line 67](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/about-claude/use-case-guides/customer-support-chat.md?plain=1#L67)] [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/customer-support-chat)]

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated email contact link for accessing full thinking output. [[line 421](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L421)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact email link for rate limit increases. [[line 443](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/build-with-claude/files.md?plain=1#L443)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Service Tiers](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/api/service-tiers.md) [[Source](https://platform.claude.com/docs/en/api/service-tiers)]

* Changed wording from "We offer" to "Anthropic offers" for company name consistency. [[line 291](https://github.com/gpambrozio/ClaudeDocs/blob/281ec02/docs-md/api/api/service-tiers.md?plain=1#L291)] [[Source](https://platform.claude.com/docs/en/api/service-tiers)]
