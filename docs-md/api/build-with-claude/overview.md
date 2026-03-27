# Features overview

Copy page

Claude's API surface is organized into five areas:

- **Model capabilities:** Control how Claude reasons and formats responses.
- **Tools:** Let Claude take actions on the web or in your environment.
- **Tool infrastructure:** Handles discovery and orchestration at scale.
- **Context management:** Keeps long-running sessions efficient.
- **Files and assets:** Manage the documents and data you provide to Claude.

If you're new, start with [model capabilities](#model-capabilities) and [tools](#tools). Return to the other sections when you're ready to optimize cost, latency, or scale.

## Feature availability

Features on the Claude Platform are assigned one of the following availability classifications per platform (shown in the Availability column of each table below). Not all features pass through every stage. A feature may enter at any classification and may skip stages.

| Classification | Description |
| --- | --- |
| **Beta**\* | Preview features used for gathering feedback and iterating on a less mature use case. Availability may be limited, including through sign-up requirements or waitlists, and may not be publicly announced.    Features may change significantly or be discontinued based on feedback. Not guaranteed for ongoing production use. Breaking changes are possible with notice, and some platform-specific limitations may apply. Beta features have a [beta header](api/beta-headers.md). |
| **Generally available (GA)** | Feature is stable, fully supported, and recommended for production use. Should not have a beta header or other indicator that the feature is in a preview state. Covered by standard API [versioning](api/versioning.md) guarantees. |
| **Deprecated** | Feature is still functional but no longer recommended. A migration path and removal timeline are provided. |
| **Retired** | Feature is no longer available. |

*\* May carry a qualifier indicating narrower availability or added constraints (for example, "beta: research preview"). See the feature's page for details.*

## Model capabilities

Ways to steer Claude and Claude's direct outputs, including response format, reasoning depth, and input modalities.

You can discover which capabilities a model supports programmatically. The [Models API](api/models/list.md) returns `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.

| Feature | Description | Zero Data Retention (ZDR) | Availability |
| --- | --- | --- | --- |
| [Context windows](build-with-claude/context-windows.md) | Up to 1M tokens for processing large documents, extensive codebases, and long conversations. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Adaptive thinking](build-with-claude/adaptive-thinking.md) | Let Claude dynamically decide when and how much to think. The recommended thinking mode for Opus 4.6. Use the effort parameter to control thinking depth. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Batch processing](build-with-claude/batch-processing.md) | Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls cost 50% less than standard API calls. | Not ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA) |
| [Citations](build-with-claude/citations.md) | Ground Claude's responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Data residency](build-with-claude/data-residency.md) | Control where model inference runs using geographic controls. Specify `"global"` or `"us"` routing per request via the `inference_geo` parameter. | ZDR eligible | Claude API (GA) |
| [Effort](build-with-claude/effort.md) | Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. Supported on Opus 4.6 and Opus 4.5. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Extended thinking](build-with-claude/extended-thinking.md) | Enhanced reasoning capabilities for complex tasks, providing transparency into Claude's step-by-step thought process before delivering its final answer. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [PDF support](build-with-claude/pdf-support.md) | Process and analyze text and visual content from PDF documents. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Search results](build-with-claude/search-results.md) | Enable natural citations for RAG applications by providing search results with proper source attribution. Achieve web search-quality citations for custom knowledge bases and tools. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Structured outputs](build-with-claude/structured-outputs.md) | Guarantee schema conformance with two approaches: JSON outputs for structured data responses, and strict tool use for validated tool inputs. | [ZDR eligible (qualified)](build-with-claude/structured-outputs.md)\* | Claude API (GA)  Amazon Bedrock (GA)  Microsoft Foundry (Beta) |

## Tools

Built-in tools that Claude invokes via `tool_use`. Server-side tools are run by the platform; client-side tools are implemented and executed by you.

### Server-side tools

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Code execution](agents-and-tools/tool-use/code-execution-tool.md) | Run code in a sandboxed environment for advanced data analysis, calculations, and file processing. Free when used with web search or web fetch. | Not ZDR eligible | Claude API (GA)  Microsoft Foundry (Beta) |
| [Web fetch](agents-and-tools/tool-use/web-fetch-tool.md) | Retrieve full content from specified web pages and PDF documents for in-depth analysis. | ZDR eligible\* | Claude API (GA)  Microsoft Foundry (Beta) |
| [Web search](agents-and-tools/tool-use/web-search-tool.md) | Augment Claude's comprehensive knowledge with current, real-world data from across the web. | ZDR eligible\* | Claude API (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |

### Client-side tools

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Bash](agents-and-tools/tool-use/bash-tool.md) | Execute bash commands and scripts to interact with the system shell and perform command-line operations. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Computer use](agents-and-tools/tool-use/computer-use-tool.md) | Control computer interfaces by taking screenshots and issuing mouse and keyboard commands. | ZDR eligible | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Memory](agents-and-tools/tool-use/memory-tool.md) | Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Text editor](agents-and-tools/tool-use/text-editor-tool.md) | Create and edit text files with a built-in text editor interface for file manipulation tasks. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |

## Tool infrastructure

Infrastructure that supports discovering, orchestrating, and scaling tool use.

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Agent Skills](agents-and-tools/agent-skills/overview.md) | Extend Claude's capabilities with Skills. Use pre-built Skills (PowerPoint, Excel, Word, PDF) or create custom Skills with instructions and scripts. Skills use progressive disclosure to efficiently manage context. | Not ZDR eligible | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Fine-grained tool streaming](agents-and-tools/tool-use/fine-grained-tool-streaming.md) | Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [MCP connector](agents-and-tools/mcp-connector.md) | Connect to remote [MCP](mcp.md) servers directly from the Messages API without a separate MCP client. | Not ZDR eligible | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Programmatic tool calling](agents-and-tools/tool-use/programmatic-tool-calling.md) | Enable Claude to call your tools programmatically from within code execution containers, reducing latency and token consumption for multi-tool workflows. | Not ZDR eligible | Claude API (GA)  Microsoft Foundry (Beta) |
| [Tool search](agents-and-tools/tool-use/tool-search-tool.md) | Scale to thousands of tools by dynamically discovering and loading tools on-demand using regex-based search, optimizing context usage and improving tool selection accuracy. | [ZDR eligible (qualified)](agents-and-tools/tool-use/tool-search-tool.md)\* | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |

## Context management

Infrastructure for controlling and optimizing Claude's context window.

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Compaction](build-with-claude/compaction.md) | Server-side context summarization for long-running conversations. When context approaches the window limit, the API automatically summarizes earlier parts of the conversation. Supported on Opus 4.6 and Sonnet 4.6. | ZDR eligible | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Context editing](build-with-claude/context-editing.md) | Automatically manage conversation context with configurable strategies. Supports clearing tool results when approaching token limits and managing thinking blocks in extended thinking conversations. | ZDR eligible | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Automatic prompt caching](build-with-claude/prompt-caching.md) | Simplify prompt caching to a single API parameter. The system automatically caches the last cacheable block in your request, moving the cache point forward as conversations grow. | ZDR eligible | Claude API (GA)  Microsoft Foundry (Beta) |
| [Prompt caching (5m)](build-with-claude/prompt-caching.md) | Provide Claude with more background knowledge and example outputs to reduce costs and latency. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Prompt caching (1hr)](build-with-claude/prompt-caching.md) | Extended 1-hour cache duration for less frequently accessed but important context, complementing the standard 5-minute cache. | ZDR eligible | Claude API (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |
| [Token counting](api/messages-count-tokens.md) | Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. | ZDR eligible | Claude API (GA)  Amazon Bedrock (GA)  Google Cloud's Vertex AI (GA)  Microsoft Foundry (Beta) |

## Files and assets

Manage files and assets for use with Claude.

| Feature | Description | ZDR | Availability |
| --- | --- | --- | --- |
| [Files API](build-with-claude/files.md) | Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files. | Not ZDR eligible | Claude API (Beta)  Microsoft Foundry (Beta) |

\* **Structured outputs:** Your prompts and Claude's outputs are not stored. Only JSON schemas are cached, for up to 24 hours since last use. **Tool search:** Only tool catalog data (names, descriptions, argument metadata) is stored server-side; custom client-side implementations are fully ZDR-eligible. **Web search and web fetch:** ZDR-eligible except when [dynamic filtering](agents-and-tools/tool-use/web-search-tool.md) is enabled. See [ZDR details](build-with-claude/api-and-data-retention.md).

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
