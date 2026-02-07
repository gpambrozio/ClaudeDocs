# [Claude docs changes for January 26th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/23337a57d14360af62799ffc70f78bb3b3f22e7f) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/23337a57d14360af62799ffc70f78bb3b3f22e7f)]

## Executive Summary
- Asana MCP server connection updated from SSE to streamable-http transport
- New Slack MCP server added for sending messages, creating canvases, and fetching Slack data

## Detailed Changes

## Claude Code changes

### Changed documents

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Asana MCP server connection command updated to use `streamable-http` transport instead of `sse` transport, with new endpoint `/v2/mcp`. [[line 171](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/claude-code/mcp.md?plain=1#L171)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* New Slack MCP server added for sending messages, creating canvases, and fetching Slack data at `https://mcp.slack.com/mcp`. [[lines 393-397](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/claude-code/mcp.md?plain=1#L393-L397)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

-----

## API changes

### Changed documents

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Box MCP server documentation link updated from `box.dev` to `developer.box.com`. [[line 219](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L219)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* New Slack MCP server added for sending messages, creating canvases, and fetching Slack data at `https://mcp.slack.com/mcp`. [[lines 549-555](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L549-L555)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Contact email link updated to direct `mailto:sales@anthropic.com` instead of email protection link for accessing full thinking output. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [files](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Contact link for higher file API rate limits updated (remains an email protection link but with different encoding). [[line 284](https://github.com/gpambrozio/ClaudeDocs/blob/23337a57d14360af62799ffc70f78bb3b3f22e7f/docs-md/api/build-with-claude/files.md?plain=1#L284)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]
