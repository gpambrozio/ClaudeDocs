# [Claude docs changes for March 9th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/5fba71ddb388188b2d32c4944fde326dd1af839d) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/5fba71ddb388188b2d32c4944fde326dd1af839d)]

## Executive Summary
- Four new remote MCP servers added to both API and Claude Code docs: Omni Analytics (natural language data querying), Clarity AI (SFDR 2.0 fund simulation), Local Falcon (local search intelligence), and DataGrail (privacy-focused AI orchestration, Claude Code only)
- The remote MCP servers directory continues to grow, reflecting expanded third-party integrations available for Claude

-----

## Claude Code changes

### Changed documents

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* New MCP server added: **Omni Analytics** — query your data using natural language through Omni's semantic model. [[line 523](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/claude-code/mcp.md?plain=1#L523)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* New MCP server added: **DataGrail** — secure, production-ready AI orchestration for privacy (user-specific URL). [[line 731](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/claude-code/mcp.md?plain=1#L731)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* New MCP server added: **Clarity AI** — simulate fund classifications under proposed SFDR 2.0. [[line 739](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/claude-code/mcp.md?plain=1#L739)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]
* New MCP server added: **Local Falcon** — AI visibility and local search intelligence platform. [[line 745](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/claude-code/mcp.md?plain=1#L745)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

-----

## API changes

### Changed documents

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP server added: **Omni Analytics** — query your data using natural language through Omni's semantic model (`https://callbacks.omniapp.co/callback/mcp`). [[line 733](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L733)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* New MCP server added: **Clarity AI** — simulate fund classifications under proposed SFDR 2.0 (`https://clarity-sfdr20-mcp.pro.clarity.ai/mcp`). [[line 1083](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L1083)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
* New MCP server added: **Local Falcon** — AI visibility and local search intelligence platform (`https://mcp.localfalcon.com`). [[line 1091](https://github.com/gpambrozio/ClaudeDocs/blob/5fba71ddb388188b2d32c4944fde326dd1af839d/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L1091)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]
