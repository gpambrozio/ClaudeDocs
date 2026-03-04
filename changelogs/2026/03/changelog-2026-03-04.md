# [Claude docs changes for March 4th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/c86701492cb0826413e711afaa79ed7eb7822a09) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/c86701492cb0826413e711afaa79ed7eb7822a09)]

## Executive Summary
- Claude Code 2.1.68 expands effort level support to Sonnet 4.6 (previously Opus 4.6 only), re-introduces the `ultrathink` keyword for high-effort mode, and removes Opus 4/4.1 from the first-party API
- The Agent SDK permissions documentation was significantly expanded with a new `dontAsk` mode (TypeScript only), clearer distinction between allow/deny rule evaluation, and guidance on how `bypassPermissions` interacts with `allowed_tools`
- Dozens of API documentation pages had their primary code examples switched from Python to Shell (curl), making them more accessible to users of any language
- Multiple new MCP server integrations were added to both the Claude Code and API documentation (Gusto, LSEG, Mem, Pylon, Daloopa, Similarweb, Bigdata.com, and more)

## New Claude Code versions

### [2.1.68](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/versions/2.1.68.md)

#### Existing feature improvements

* Opus 4.6 now defaults to medium effort for Max and Team subscribers; medium effort is the sweet spot between speed and thoroughness and can be changed with `/model`
* Effort level support expanded to Sonnet 4.6 (in addition to Opus 4.6)
* Re-introduced the `ultrathink` keyword to enable high effort for the next turn

#### Major bug fixes

* Removed Opus 4 and Opus 4.1 from Claude Code on the first-party API; users with these models pinned are automatically moved to Opus 4.6

-----

## Claude Code changes

### Changed documents

#### [common-workflows](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/claude-code/common-workflows.md) [[Source](https://code.claude.com/docs/en/common-workflows)]

* Updated effort level description to note that both Opus 4.6 and Sonnet 4.6 support effort control (previously only Opus 4.6 was mentioned) [[line 845](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/claude-code/common-workflows.md?plain=1#L845)] [[Source](https://code.claude.com/docs/en/common-workflows#configure-thinking-mode)]

#### [mcp](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Added new MCP server: **Smartsheet** — Analyze and manage Smartsheet data with Claude
* Added new MCP server: **Windsor.ai** — Connect 325+ marketing, analytics and CRM data sources
* Added new MCP server: **Mem** — The AI notebook for everything on your mind
* Various MCP server entries were reordered

#### [model-config](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Effort level support now documented for both Opus 4.6 and Sonnet 4.6; removed note saying effort was only supported on Opus 4.6 [[line 145](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/claude-code/model-config.md?plain=1#L145)] [[Source](https://code.claude.com/docs/en/model-config#adjust-effort-level)]

#### [settings](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* `CLAUDE_CODE_EFFORT_LEVEL` environment variable description updated to reflect support for both Opus 4.6 and Sonnet 4.6 [[line 945](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/claude-code/settings.md?plain=1#L945)] [[Source](https://code.claude.com/docs/en/settings#environment-variables)]

-----

## API changes

### Changed documents

#### [content-moderation](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/about-claude/use-case-guides/content-moderation.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation)]

* Removed redundant client initialization boilerplate from multiple code examples, cleaning up the guide

#### [legal-summarization](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/about-claude/use-case-guides/legal-summarization.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/legal-summarization)]

* Removed redundant client initialization boilerplate from code examples

#### [migration-guide](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* All Python migration code examples replaced with Shell (curl) equivalents, covering low-effort, medium-effort with extended thinking, and adaptive thinking scenarios [[lines 232-362](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/about-claude/models/migration-guide.md?plain=1#L232-L362)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

#### [ticket-routing](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/about-claude/use-case-guides/ticket-routing.md) [[Source](https://platform.claude.com/docs/en/about-claude/use-case-guides/ticket-routing)]

* Removed redundant client initialization boilerplate from code examples

#### [overview (agent-sdk)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/overview.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/overview)]

* Minor cleanup

#### [permissions](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/permissions.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]

* Significantly restructured permission evaluation flow: deny rules are now evaluated separately before allow rules, and the ordering is now: hooks → deny rules → permission mode → allow rules → `canUseTool` [[lines 17-44](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/permissions.md?plain=1#L17-L44)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]
* New section added explaining `allowed_tools` and `disallowed_tools` behavior with a table and practical examples [[lines 46-72](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/permissions.md?plain=1#L46-L72)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]
* New `dontAsk` permission mode documented (TypeScript only): converts permission prompts into denials for fixed, explicit tool surfaces [[lines 80-84](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/permissions.md?plain=1#L80-L84)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]
* Clarification that `allowed_tools` does NOT constrain `bypassPermissions` — all tools are still approved unless explicitly in `disallowed_tools` [[lines 66-68](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/permissions.md?plain=1#L66-L68)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]
* New dedicated subsection for `dontAsk` mode with guidance on Python equivalent workarounds [[lines 131-140](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/permissions.md?plain=1#L131-L140)] [[Source](https://platform.claude.com/docs/en/agent-sdk/permissions)]

#### [python (agent-sdk)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/python.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/python)]

* Minor cleanup

#### [quickstart (agent-sdk)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/quickstart.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/quickstart)]

* Minor cleanup

#### [skills (agent-sdk)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/skills.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/skills)]

* Minor cleanup

#### [typescript (agent-sdk)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agent-sdk/typescript.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/typescript)]

* Minor cleanup

#### [quickstart (agent-skills)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Minor cleanup

#### [mcp-connector](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* Minor cleanup

#### [remote-mcp-servers](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Added new MCP server: **Gusto** — Query and analyze your Gusto data (`https://mcp.api.gusto.com/anthropic`)
* Added new MCP server: **LSEG** — Access best in class data & analytics across a broad spectrum of asset classes (`https://api.analytics.lseg.com/lfa/mcp/server-cl`)
* Added new MCP server: **Bigdata.com** — Access real-time financial data (`https://mcp.bigdata.com/`)
* Added new MCP server: **Daloopa** — Financial fundamental data and KPIs with hyperlinks (`https://mcp.daloopa.com/server/mcp`)
* Added new MCP server: **Pylon** — Search and manage Pylon support issues (`https://mcp.usepylon.com/`)
* Added new MCP server: **Similarweb** — Real time web, mobile app, and market data (`https://mcp.similarweb.com`)
* Added new MCP server: **WordPress.com** — Secure AI access to manage your WordPress.com sites (`https://public-api.wordpress.com/wpcom/v2/mcp/v1`)
* Added new MCP server: **Yardi Virtuoso** — Real-time Yardi data & insights (`https://mcp.virtuoso.ai/mcp`)
* Various existing server entries were reordered

#### [code-execution-tool](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Container reuse example replaced with Shell (curl) equivalent, showing how to extract container ID with `jq` and pass it to a second request [[lines 506-553](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L506-L553)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [computer-use-tool](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

* Getting started example replaced with Shell (curl) equivalent [[lines 70-110](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/computer-use-tool.md?plain=1#L70-L110)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)]

#### [implement-tool-use](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/implement-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use)]

* Minor cleanup

#### [overview (tool-use)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/overview.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)]

* Minor cleanup

#### [programmatic-tool-calling](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* Minor cleanup

#### [tool-search-tool](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

* Fixed `cache_control` structure in multi-turn conversation example: moved `cache_control` inside the content block array (correct API structure) [[lines 403-414](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L403-L414)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]
* Fixed `usage.get()` call to use proper SDK attribute access: `response2.usage.cache_read_input_tokens or 0`

#### [web-fetch-tool](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Fixed `cache_control` structure in multi-turn example: moved inside content block array (matching correct API structure) [[lines 379-390](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L379-L390)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]
* Fixed `usage.get()` call to use proper SDK attribute access

#### [web-search-tool](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Fixed `cache_control` structure in multi-turn example: moved inside content block array (correct API structure) [[lines 324-336](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L324-L336)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]
* Fixed `usage.get()` call to use proper SDK attribute access

#### [client-sdks](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/client-sdks.md) [[Source](https://platform.claude.com/docs/en/api/client-sdks)]

* Language tab ordering updated: C# now appears before Java, Ruby moved after PHP

#### [openai-sdk](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/openai-sdk.md) [[Source](https://platform.claude.com/docs/en/api/openai-sdk)]

* API key now read from environment variable `os.environ.get("ANTHROPIC_API_KEY")` instead of a literal placeholder string [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/openai-sdk.md?plain=1#L30)] [[Source](https://platform.claude.com/docs/en/api/openai-sdk)]
* Extended thinking example now includes a concrete `messages` parameter instead of `...` [[line 76](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/openai-sdk.md?plain=1#L76)] [[Source](https://platform.claude.com/docs/en/api/openai-sdk)]

#### [python (sdk)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/sdks/python.md) [[Source](https://platform.claude.com/docs/en/api/sdks/python)]

* Removed redundant `client` initialization boilerplate from multiple code snippets throughout the guide
* Added a proper example instantiation before the `if response.my_field is None` null-distinction example [[line 537](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/sdks/python.md?plain=1#L537)] [[Source](https://platform.claude.com/docs/en/api/sdks/python)]

#### [typescript (sdk)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/sdks/typescript.md) [[Source](https://platform.claude.com/docs/en/api/sdks/typescript)]

* Removed redundant `import Anthropic` and client initialization boilerplate from many code snippets
* Fixed Message Batches examples to use `client` instead of `anthropic` variable name for consistency [[lines 272-302](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/sdks/typescript.md?plain=1#L272-L302)] [[Source](https://platform.claude.com/docs/en/api/sdks/typescript)]
* `fetchAllMessageBatches` function now uses typed parameter `params: Record<string, unknown>` instead of untyped `params` [[line 491](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/api/sdks/typescript.md?plain=1#L491)] [[Source](https://platform.claude.com/docs/en/api/sdks/typescript)]

#### [adaptive-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Adaptive thinking + effort level example replaced with Shell (curl) equivalent [[lines 63-92](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L63-L92)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [batch-processing](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Polling loop example replaced with Shell (curl/bash) equivalent using a `until` loop [[lines 169-197](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/batch-processing.md?plain=1#L169-L197)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]
* List batches example replaced with Shell (curl) equivalent with manual pagination loop using `jq` [[lines 205-244](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/batch-processing.md?plain=1#L205-L244)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]
* Cancel batch example replaced with Shell (curl) equivalent [[lines 303-316](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/batch-processing.md?plain=1#L303-L316)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

#### [citations](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/citations.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/citations)]

* Minor cleanup

#### [claude-in-microsoft-foundry](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]

* API key authentication example replaced with Shell (curl) equivalent [[lines 98-118](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L98-L118)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]
* Entra ID (Azure AD) authentication example replaced with Shell equivalent using `az account get-access-token` [[lines 126-150](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/claude-in-microsoft-foundry.md?plain=1#L126-L150)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry)]
* Language tab ordering updated: C# now appears before Java

#### [claude-on-amazon-bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/claude-on-amazon-bedrock.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock)]

* Language tab ordering updated: C# now appears before Java

#### [claude-on-vertex-ai](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/claude-on-vertex-ai.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]

* Basic text generation example replaced with Shell (curl) equivalent using `gcloud auth print-access-token` [[lines 69-94](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/claude-on-vertex-ai.md?plain=1#L69-L94)] [[Source](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)]
* Language tab ordering updated: Go now appears before Java

#### [compaction](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Added a complete example request showing how to trigger manual compaction using `context_management` with `compact_20260112` edit type [[lines 234-243](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/compaction.md?plain=1#L234-L243)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

#### [context-editing](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/context-editing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-editing)]

* Minor cleanup

#### [effort](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Basic usage example replaced with Shell (curl) equivalent [[lines 46-68](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/effort.md?plain=1#L46-L68)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

#### [extended-thinking](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Minor cleanup

#### [fast-mode](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Minor cleanup

#### [files](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Minor cleanup

#### [handling-stop-reasons](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/handling-stop-reasons.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

* Added full client initialization and message creation context to the `end_turn` stop reason code example [[lines 39-47](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L39-L47)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]
* Added full setup code (client, tool definition, execute_tool function) to the `tool_use` stop reason example [[lines 180-205](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L180-L205)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]
* Added complete client and request setup to the error handling and streaming examples [[lines 387-400](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/handling-stop-reasons.md?plain=1#L387-L400)] [[Source](https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons)]

#### [multilingual-support](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/multilingual-support.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/multilingual-support)]

* Minor cleanup

#### [prompting-tools](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/prompt-engineering/prompting-tools.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-tools)]

* Minor cleanup

#### [search-results](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/search-results.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

* Direct search results example replaced with Shell (curl) equivalent, showing the full JSON structure for `search_result` content blocks [[lines 187-244](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/search-results.md?plain=1#L187-L244)] [[Source](https://platform.claude.com/docs/en/build-with-claude/search-results)]

#### [skills-guide](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* All major code examples converted from Python to Shell (curl): basic skill usage, file download, multi-turn `pause_turn` handling, combining multiple skills, skill upload, listing/retrieving/deleting skills, versioning, and prompt caching examples [[throughout](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/skills-guide.md?plain=1#L62)]
* Error handling section retains Python as it uses the SDK's exception model (no shell equivalent)

#### [streaming](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/streaming.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/streaming)]

* Minor cleanup

#### [structured-outputs](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Language tab ordering updated: C# now appears before Java, Ruby moved after PHP

#### [token-counting](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/token-counting.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]

* Basic token counting example replaced with Shell (curl) equivalent [[lines 26-46](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/token-counting.md?plain=1#L26-L46)] [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]
* Token counting with tools example replaced with Shell (curl) equivalent [[lines 53-90](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/build-with-claude/token-counting.md?plain=1#L53-L90)] [[Source](https://platform.claude.com/docs/en/build-with-claude/token-counting)]

#### [overview (resources)](https://github.com/gpambrozio/ClaudeDocs/blob/c86701492cb0826413e711afaa79ed7eb7822a09/docs-md/api/resources/overview.md) [[Source](https://platform.claude.com/docs/en/resources/overview)]

* Minor cleanup
