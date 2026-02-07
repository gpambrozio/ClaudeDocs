# [Claude docs changes for January 30th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/ca2a4e3) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/ca2a4e3)]

## Executive Summary
- New version 2.1.25: Fixed beta header validation for Bedrock/Vertex gateway users
- Structured outputs graduated from beta to GA with `output_format` renamed to `output_config.format` across all SDKs
- Analytics documentation rewritten for Teams/Enterprise dashboards with GitHub contribution metrics

## Detailed Changes

## New Claude Code versions

### [2.1.25](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/versions/2.1.25.md)

#### Major bug fixes

* Fixed beta header validation error for gateway users on Bedrock and Vertex, ensuring `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS=1` avoids the error

-----

## Claude Code changes

### Changed documents

#### [Analytics](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/analytics.md) [[Source](https://code.claude.com/docs/en/analytics)]

* Complete rewrite of analytics documentation with new structure for Teams/Enterprise and API customers. [[lines 1-10](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/analytics.md?plain=1#L1-L10)] [[Source](https://code.claude.com/docs/en/analytics)]
* Added documentation for Teams and Enterprise dashboard including usage metrics, contribution metrics with GitHub integration, leaderboard, and data export capabilities. [[lines 12-17](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/analytics.md?plain=1#L12-L17)] [[Source](https://code.claude.com/docs/en/analytics#access-analytics-for-teams-and-enterprise)]
* Added detailed setup instructions for enabling contribution metrics through GitHub app integration. [[lines 19-51](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/analytics.md?plain=1#L19-L51)] [[Source](https://code.claude.com/docs/en/analytics#access-analytics-for-teams-and-enterprise)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added Granola MCP server for AI notepad for meetings. [[lines 79-83](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/mcp.md?plain=1#L79-L83)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Updated Atlassian transport from SSE to HTTP. [[line 183](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/mcp.md?plain=1#L183)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added Smartsheet MCP server for analyzing and managing Smartsheet data. [[lines 417-421](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/mcp.md?plain=1#L417-L421)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* Added Supabase MCP server for managing databases, authentication, and storage. [[lines 439-443](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/mcp.md?plain=1#L439-L443)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Added `spinnerVerbs` configuration option to customize action verbs shown in spinner and turn duration messages. [[line 163](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/settings.md?plain=1#L163)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]

#### [Setup](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/setup.md) [[Source](https://code.claude.com/docs/en/setup)]

* Updated Windows operating system requirements to specify Windows 10 1809+ / Windows Server 2019+. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/claude-code/setup.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/setup#system-requirements)]

-----

## API changes

### New Documents

#### [Agent SDK - Stream responses in real-time](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/agent-sdk/streaming-output.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/streaming-output)]

New comprehensive documentation for streaming responses in the Agent SDK. Covers enabling streaming output with `include_partial_messages` / `includePartialMessages`, understanding StreamEvent message types, streaming text responses, streaming tool calls, building streaming UIs, and known limitations with extended thinking and structured outputs. Includes detailed examples for handling content_block_delta events, tracking tool execution progress, and creating cohesive streaming interfaces.

### Changed documents

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added Granola remote MCP server. [[lines 63-68](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L63-L68)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added Smartsheet remote MCP server. [[lines 573-578](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L573-L578)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* Added Supabase remote MCP server. [[lines 603-608](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L603-L608)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [Beta](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta.md) [[Source](https://platform.claude.com/docs/en/api/beta)]

* Removed structured outputs beta header requirement and updated parameter name from `output_format` to `output_config.format`. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta.md)]

#### [Beta - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages)]

* Updated structured outputs parameter from `output_format` to `output_config.format` in examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages.md)]

#### [Beta - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches)]

* Updated structured outputs parameter references from `output_format` to `output_config.format`. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/batches.md)]

#### [Beta - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches/create)]

* Updated structured outputs parameter from `output_format` to `output_config.format` throughout API reference. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/batches/create.md)]

#### [Beta - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/batches/results)]

* Updated structured outputs parameter references in API response documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/batches/results.md)]

#### [Beta - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/count_tokens)]

* Updated structured outputs parameter from `output_format` to `output_config.format`. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/count_tokens.md)]

#### [Beta - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

* Added `output_config` parameter with nested `format` object for structured outputs configuration. [[lines 1816-1832](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/create.md?plain=1#L1816-L1832)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Added `strict` parameter to Tool objects for schema validation guarantee. [[lines 2244-2246](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/create.md?plain=1#L2244-L2246)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]
* Added `request_too_large` error code to WebSearchToolRequestError. [[line 1655](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/beta/messages/create.md?plain=1#L1655)] [[Source](https://platform.claude.com/docs/en/api/beta/messages/create)]

#### [Completions - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/completions/create.md) [[Source](https://platform.claude.com/docs/en/api/completions/create)]

* Updated structured outputs parameter references from `output_format` to `output_config.format`. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/completions/create.md)]

#### [Go - Beta](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta.md) [[Source](https://platform.claude.com/docs/en/api/go/beta)]

* Updated Go SDK examples to use new `output_config.format` parameter instead of `output_format`. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta.md)]

#### [Go - Beta - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/go/beta/messages)]

* Updated Go SDK structured outputs examples with new parameter structure. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages.md)]

#### [Go - Beta - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/go/beta/messages/batches)]

* Updated Go SDK batch API examples with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/batches.md)]

#### [Go - Beta - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/go/beta/messages/batches/create)]

* Updated structured outputs parameter in Go SDK batch create examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/batches/create.md)]

#### [Go - Beta - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/go/beta/messages/batches/results)]

* Updated Go SDK batch results documentation with new parameter structure. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/batches/results.md)]

#### [Go - Beta - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/go/beta/messages/count_tokens)]

* Updated Go SDK token counting examples with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/count_tokens.md)]

#### [Go - Beta - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/go/beta/messages/create)]

* Updated Go SDK message creation examples with `output_config.format` parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/beta/messages/create.md)]

#### [Go - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages.md) [[Source](https://platform.claude.com/docs/en/api/go/messages)]

* Updated Go SDK messages documentation with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages.md)]

#### [Go - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/go/messages/batches)]

* Updated Go SDK batch messages with new parameter structure. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/batches.md)]

#### [Go - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/go/messages/batches/create)]

* Updated Go SDK batch create examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/batches/create.md)]

#### [Go - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/go/messages/batches/results)]

* Updated Go SDK batch results documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/batches/results.md)]

#### [Go - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/go/messages/count_tokens)]

* Updated Go SDK token counting examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/count_tokens.md)]

#### [Go - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/go/messages/create)]

* Updated Go SDK message creation with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/go/messages/create.md)]

#### [Java - Beta](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta.md) [[Source](https://platform.claude.com/docs/en/api/java/beta)]

* Updated Java SDK examples with new `output_config.format` parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta.md)]

#### [Java - Beta - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/java/beta/messages)]

* Updated Java SDK messages examples with new parameter structure. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages.md)]

#### [Java - Beta - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/java/beta/messages/batches)]

* Updated Java SDK batch examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/batches.md)]

#### [Java - Beta - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/java/beta/messages/batches/create)]

* Updated Java SDK batch create documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/batches/create.md)]

#### [Java - Beta - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/java/beta/messages/batches/results)]

* Updated Java SDK batch results examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/batches/results.md)]

#### [Java - Beta - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/java/beta/messages/count_tokens)]

* Updated Java SDK token counting documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/count_tokens.md)]

#### [Java - Beta - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/java/beta/messages/create)]

* Updated Java SDK message creation examples with new parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/beta/messages/create.md)]

#### [Java - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages.md) [[Source](https://platform.claude.com/docs/en/api/java/messages)]

* Updated Java SDK messages documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages.md)]

#### [Java - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/java/messages/batches)]

* Updated Java SDK batch messages. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/batches.md)]

#### [Java - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/java/messages/batches/create)]

* Updated Java SDK batch create examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/batches/create.md)]

#### [Java - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/java/messages/batches/results)]

* Updated Java SDK batch results documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/batches/results.md)]

#### [Java - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/java/messages/count_tokens)]

* Updated Java SDK token counting examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/count_tokens.md)]

#### [Java - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/java/messages/create)]

* Updated Java SDK message creation with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/java/messages/create.md)]

#### [Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages.md) [[Source](https://platform.claude.com/docs/en/api/messages)]

* Updated Messages API examples with new `output_config.format` parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages.md)]

#### [Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/messages/batches)]

* Updated batch API examples with new parameter structure. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/batches.md)]

#### [Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/batches/create)]

* Updated batch create documentation with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/batches/create.md)]

#### [Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/messages/batches/results)]

* Updated batch results examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/batches/results.md)]

#### [Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/messages/count_tokens)]

* Updated token counting documentation with new parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/count_tokens.md)]

#### [Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/messages/create)]

* Added `output_config` parameter with nested `format` object for structured outputs configuration. [[lines 1816-1832](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/create.md?plain=1#L1816-L1832)] [[Source](https://platform.claude.com/docs/en/api/messages/create)]
* Added `strict` parameter to Tool objects for guaranteed schema validation on tool names and inputs. [[lines 2244-2246](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/create.md?plain=1#L2244-L2246)] [[Source](https://platform.claude.com/docs/en/api/messages/create)]
* Added `request_too_large` error code to WebSearchToolRequestError enum. [[line 1655](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/messages/create.md?plain=1#L1655)] [[Source](https://platform.claude.com/docs/en/api/messages/create)]

#### [Python - Beta](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta.md) [[Source](https://platform.claude.com/docs/en/api/python/beta)]

* Updated Python SDK examples to use `output_config.format` and removed beta header requirements. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta.md)]

#### [Python - Beta - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/python/beta/messages)]

* Updated Python SDK messages examples with new parameter structure. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages.md)]

#### [Python - Beta - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/python/beta/messages/batches)]

* Updated Python SDK batch examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/batches.md)]

#### [Python - Beta - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/python/beta/messages/batches/create)]

* Updated Python SDK batch create documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/batches/create.md)]

#### [Python - Beta - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/python/beta/messages/batches/results)]

* Updated Python SDK batch results examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/batches/results.md)]

#### [Python - Beta - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/python/beta/messages/count_tokens)]

* Updated Python SDK token counting documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/count_tokens.md)]

#### [Python - Beta - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/python/beta/messages/create)]

* Updated Python SDK message creation examples with new parameter and moved from `client.beta.messages` to `client.messages`. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/beta/messages/create.md)]

#### [Python - Completions](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/completions.md) [[Source](https://platform.claude.com/docs/en/api/python/completions)]

* Updated Python SDK completions examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/completions.md)]

#### [Python - Completions - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/completions/create.md) [[Source](https://platform.claude.com/docs/en/api/python/completions/create)]

* Updated Python SDK completions create documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/completions/create.md)]

#### [Python - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages.md) [[Source](https://platform.claude.com/docs/en/api/python/messages)]

* Updated Python SDK messages documentation with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages.md)]

#### [Python - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/python/messages/batches)]

* Updated Python SDK batch messages. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/batches.md)]

#### [Python - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/python/messages/batches/create)]

* Updated Python SDK batch create examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/batches/create.md)]

#### [Python - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/python/messages/batches/results)]

* Updated Python SDK batch results documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/batches/results.md)]

#### [Python - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/python/messages/count_tokens)]

* Updated Python SDK token counting examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/count_tokens.md)]

#### [Python - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/python/messages/create)]

* Updated Python SDK message creation with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/python/messages/create.md)]

#### [Ruby - Beta](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta.md) [[Source](https://platform.claude.com/docs/en/api/ruby/beta)]

* Updated Ruby SDK examples with new `output_config.format` parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta.md)]

#### [Ruby - Beta - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/ruby/beta/messages)]

* Updated Ruby SDK messages examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages.md)]

#### [Ruby - Beta - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/ruby/beta/messages/batches)]

* Updated Ruby SDK batch examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/batches.md)]

#### [Ruby - Beta - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/ruby/beta/messages/batches/create)]

* Updated Ruby SDK batch create documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/batches/create.md)]

#### [Ruby - Beta - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/ruby/beta/messages/batches/results)]

* Updated Ruby SDK batch results examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/batches/results.md)]

#### [Ruby - Beta - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/ruby/beta/messages/count_tokens)]

* Updated Ruby SDK token counting documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/count_tokens.md)]

#### [Ruby - Beta - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/ruby/beta/messages/create)]

* Updated Ruby SDK message creation examples with new parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/beta/messages/create.md)]

#### [Ruby - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages.md) [[Source](https://platform.claude.com/docs/en/api/ruby/messages)]

* Updated Ruby SDK messages documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages.md)]

#### [Ruby - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/ruby/messages/batches)]

* Updated Ruby SDK batch messages. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/batches.md)]

#### [Ruby - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/ruby/messages/batches/create)]

* Updated Ruby SDK batch create examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/batches/create.md)]

#### [Ruby - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/ruby/messages/batches/results)]

* Updated Ruby SDK batch results documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/batches/results.md)]

#### [Ruby - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/ruby/messages/count_tokens)]

* Updated Ruby SDK token counting examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/count_tokens.md)]

#### [Ruby - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/ruby/messages/create)]

* Updated Ruby SDK message creation with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/ruby/messages/create.md)]

#### [TypeScript - Beta](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta)]

* Updated TypeScript SDK examples with new `output_config.format` parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta.md)]

#### [TypeScript - Beta - Files - Download](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/files/download.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta/files/download)]

* Updated TypeScript SDK files documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/files/download.md)]

#### [TypeScript - Beta - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta/messages)]

* Updated TypeScript SDK messages examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages.md)]

#### [TypeScript - Beta - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta/messages/batches)]

* Updated TypeScript SDK batch examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/batches.md)]

#### [TypeScript - Beta - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta/messages/batches/create)]

* Updated TypeScript SDK batch create documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/batches/create.md)]

#### [TypeScript - Beta - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta/messages/batches/results)]

* Updated TypeScript SDK batch results examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/batches/results.md)]

#### [TypeScript - Beta - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta/messages/count_tokens)]

* Updated TypeScript SDK token counting documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/count_tokens.md)]

#### [TypeScript - Beta - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/typescript/beta/messages/create)]

* Updated TypeScript SDK message creation examples with new parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/beta/messages/create.md)]

#### [TypeScript - Messages](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages.md) [[Source](https://platform.claude.com/docs/en/api/typescript/messages)]

* Updated TypeScript SDK messages documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages.md)]

#### [TypeScript - Messages - Batches](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/batches.md) [[Source](https://platform.claude.com/docs/en/api/typescript/messages/batches)]

* Updated TypeScript SDK batch messages. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/batches.md)]

#### [TypeScript - Messages - Batches - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/batches/create.md) [[Source](https://platform.claude.com/docs/en/api/typescript/messages/batches/create)]

* Updated TypeScript SDK batch create examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/batches/create.md)]

#### [TypeScript - Messages - Batches - Results](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/batches/results.md) [[Source](https://platform.claude.com/docs/en/api/typescript/messages/batches/results)]

* Updated TypeScript SDK batch results documentation. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/batches/results.md)]

#### [TypeScript - Messages - Count tokens](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/count_tokens.md) [[Source](https://platform.claude.com/docs/en/api/typescript/messages/count_tokens)]

* Updated TypeScript SDK token counting examples. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/count_tokens.md)]

#### [TypeScript - Messages - Create](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/create.md) [[Source](https://platform.claude.com/docs/en/api/typescript/messages/create)]

* Updated TypeScript SDK message creation with new structured outputs parameter. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/api/typescript/messages/create.md)]

#### [Citations](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/citations.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

* Updated incompatibility note to reference new `output_config.format` parameter instead of `output_format`. [[line 125](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/citations.md?plain=1#L125)] [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

#### [Extended thinking](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Updated sales team contact link from obfuscated email to direct mailto link. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Updated contact link for higher rate limits from obfuscated email to direct mailto link. [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Overview](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Updated structured outputs availability to include Amazon Bedrock (Beta) and changed from "Claude API (Beta)" to "Claude API" to reflect GA status. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/overview.md?plain=1#L23)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* Removed Opus 4.1 from supported models list for structured outputs. [[line 23](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/overview.md?plain=1#L23)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [Structured outputs](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Changed from beta to GA status - removed beta header requirement and updated parameter from `output_format` to `output_config.format`. [[lines 1-13](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L1-L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* Added migration note explaining that old beta header and parameter will continue working during transition period. [[lines 14-15](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L14-L15)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* Updated all examples throughout the document to use new parameter structure. [[throughout file](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/structured-outputs.md)]
* Updated Python SDK examples to use `client.messages` instead of `client.beta.messages`. [[lines 129-162](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L129-L162)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]
* Removed Opus 4.1 from supported models. [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

#### [Release notes - Overview](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added January 29, 2026 release note announcing structured outputs GA with expanded schema support, improved grammar compilation latency, and simplified integration. [[lines 9-11](https://github.com/gpambrozio/ClaudeDocs/blob/ca2a4e3/docs-md/api/release-notes/overview.md?plain=1#L9-L11)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]
