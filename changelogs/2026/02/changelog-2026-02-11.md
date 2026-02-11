# [Claude docs changes for February 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/127647174fc11171ec36e3183efba9583568e2a9) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/127647174fc11171ec36e3183efba9583568e2a9)]

## Executive Summary
- New server-managed settings feature for centralized Claude Code configuration via Claude.ai admin console
- Added 12+ remote MCP server integrations including Circleback, Day AI, Fireflies, and more
- Enhanced documentation for pause_turn stop reason with detailed handling instructions
- Improved prompt caching guidance for compaction with system prompt optimization techniques

## New Claude Code versions

### [2.1.39](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/versions/2.1.39.md)

#### New features

* Added guard against launching Claude Code inside another Claude Code session

#### Existing feature improvements

* Improved model error messages for Bedrock/Vertex/Foundry users with fallback suggestions
* Improved terminal rendering performance
* Improved /resume session previews showing readable command names instead of raw XML tags

#### Major bug fixes

* Fixed Agent Teams using wrong model identifier for Bedrock, Vertex, and Foundry customers
* Fixed a crash when MCP tools return image content during streaming
* Fixed fatal errors being swallowed instead of displayed
* Fixed process hanging after session close
* Fixed character loss at terminal screen boundary
* Fixed blank lines in verbose transcript view

-----

## Claude Code changes

### New Documents

#### [Server-managed settings](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/server-managed-settings.md) [[Source](https://code.claude.com/docs/en/server-managed-settings)]

New documentation for server-managed settings in public beta. This feature allows administrators to centrally configure Claude Code through a web-based interface on Claude.ai, with clients automatically receiving settings when users authenticate. Requires Claude for Teams or Enterprise plans and version 2.1.30 or later. Includes comparison with endpoint-managed settings, configuration instructions via Admin Console, settings precedence and caching behavior, security approval dialogs for risky settings, platform availability limitations (not available with third-party providers like Bedrock/Vertex/Foundry), audit logging capabilities, and security considerations including threat model documentation.

### Changed documents

#### [Fast mode](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/fast-mode.md) [[Source](https://code.claude.com/docs/en/fast-mode)]

* Updated description to specify fast mode is a high-speed configuration that delivers 2.5x faster Claude Opus 4.6 responses. [[line 5](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/fast-mode.md?plain=1#L5)] [[Source](https://code.claude.com/docs/en/fast-mode)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Updated Port IO server instructions to require user-specific URL retrieval from Port IO documentation instead of direct command. [[lines 601-603](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/mcp.md?plain=1#L601-L603)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

#### [Permissions](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/permissions.md) [[Source](https://code.claude.com/docs/en/permissions)]

* Enhanced managed settings description to reference server-managed settings as alternative for organizations without device management infrastructure. [[line 210](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/permissions.md?plain=1#L210)] [[Source](https://code.claude.com/docs/en/permissions#how-permissions-interact-with-sandboxing)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated managed settings documentation reference to include note about server-managed settings alternative with link to new documentation. [[line 87](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/settings.md?plain=1#L87)] [[Source](https://code.claude.com/docs/en/settings#settings-files)]
* Updated settings precedence hierarchy to clarify that managed settings can come from either managed-settings.json files or server-managed settings from Anthropic's servers for Enterprise customers. [[lines 381-382](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/claude-code/settings.md?plain=1#L381-L382)] [[Source](https://code.claude.com/docs/en/settings#hook-configuration)]

-----

## API changes

### Changed documents

#### [Compaction](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Enhanced prompt caching description with link to prompt caching documentation. [[line 299](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/build-with-claude/compaction.md?plain=1#L299)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]
* Added new section "Maximizing cache hits with system prompts" explaining how to add cache breakpoint at end of system prompt to keep it cached separately from compaction summary, includes Python code example with cache_control configuration. [[lines 318-347](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/build-with-claude/compaction.md?plain=1#L318-L347)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

#### [Handling stop reasons](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

* Significantly expanded pause_turn documentation from brief mention to detailed explanation, clarifying it occurs when server-side sampling reaches iteration limit (default 10), with code example showing how to continue conversation after pause_turn. [[lines 194-219](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L194-L219)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]
* Completely rewrote retry logic section, renaming from generic retry to server tool-specific handle_server_tool_conversation() with detailed docstring explaining server sampling loop behavior, improved code example with proper role alternation handling, and changed max_retries to max_continuations for clarity. [[lines 314-346](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L314-L346)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

#### [Remote MCP servers](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added extensive list of 12+ new remote MCP server integrations including Circleback (meeting search at https://app.circleback.ai/api/mcp), Day AI (CRM records at https://day.ai/api/mcp), ICD-10 Codes (medical code sets at https://mcp.deepsense.ai/icd10_codes/mcp), DevRev (knowledge graph at https://api.devrev.ai/mcp/v1), Fireflies (meeting transcripts at https://api.fireflies.ai/mcp), Granola (AI notepad at https://mcp.granola.ai/mcp), Harmonic (company/people discovery at https://mcp.api.harmonic.ai), LunarCrush (social media data at https://lunarcrush.ai/mcp), Scholar Gateway (scholarly research at https://connector.scholargateway.ai/mcp), Ticket Tailor (event platform at https://mcp.tickettailor.ai/mcp), Vibe Prospecting (company/contact data at https://vibeprospecting.explorium.ai/mcp), and Windsor.ai (marketing data sources). [[lines 23-895](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/agents-and-tools/remote-mcp-servers.md?plain=1#L23-L895)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

#### [Tool use overview](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Enhanced server tools workflow documentation clarifying that Anthropic's servers handle tool execution in a loop. [[lines 102-128](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L102-L128)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]
* Added new section explaining pause_turn stop reason with 10-iteration default limit for server-side sampling loop and instructions for handling pause_turn responses. [[lines 102-128](https://github.com/gpambrozio/ClaudeDocs/blob/127647174fc11171ec36e3183efba9583568e2a9/docs-md/api/agents-and-tools/tool-use/overview.md?plain=1#L102-L128)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]
