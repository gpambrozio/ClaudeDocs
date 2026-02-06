# Features overview

Copy page

## Core capabilities

These features enhance Claude's fundamental abilities for processing, analyzing, and generating content across various formats and use cases.

| Feature | Description | Availability |
| --- | --- | --- |
| [1M token context window](build-with-claude/context-windows.md) | An extended context window that allows you to process much larger documents, maintain longer conversations, and work with more extensive codebases. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Adaptive thinking](build-with-claude/adaptive-thinking.md) | Let Claude dynamically decide when and how much to think. The recommended thinking mode for Opus 4.6. Use the effort parameter to control thinking depth. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Agent Skills](agents-and-tools/agent-skills/overview.md) | Extend Claude's capabilities with Skills. Use pre-built Skills (PowerPoint, Excel, Word, PDF) or create custom Skills with instructions and scripts. Skills use progressive disclosure to efficiently manage context. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Batch processing](build-with-claude/batch-processing.md) | Process large volumes of requests asynchronously for cost savings. Send batches with a large number of queries per batch. Batch API calls costs 50% less than standard API calls. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI |
| [Citations](build-with-claude/citations.md) | Ground Claude's responses in source documents. With Citations, Claude can provide detailed references to the exact sentences and passages it uses to generate responses, leading to more verifiable, trustworthy outputs. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Compaction](build-with-claude/compaction.md) | Server-side context summarization for long-running conversations. When context approaches the window limit, the API automatically summarizes earlier parts of the conversation. Supported on Opus 4.6 and Haiku 4.5. | Claude API (Beta) |
| [Context editing](build-with-claude/context-editing.md) | Automatically manage conversation context with configurable strategies. Supports clearing tool results when approaching token limits and managing thinking blocks in extended thinking conversations. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Data residency](build-with-claude/data-residency.md) | Control where model inference runs using geographic controls. Specify `"global"` or `"us"` routing per request via the `inference_geo` parameter. | Claude API |
| [Effort](build-with-claude/effort.md) | Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency. Supported on Opus 4.6 and Opus 4.5. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Extended thinking](build-with-claude/extended-thinking.md) | Enhanced reasoning capabilities for complex tasks, providing transparency into Claude's step-by-step thought process before delivering its final answer. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Files API](build-with-claude/files.md) | Upload and manage files to use with Claude without re-uploading content with each request. Supports PDFs, images, and text files. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [PDF support](build-with-claude/pdf-support.md) | Process and analyze text and visual content from PDF documents. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Prompt caching (5m)](build-with-claude/prompt-caching.md) | Provide Claude with more background knowledge and example outputs to reduce costs and latency. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Prompt caching (1hr)](build-with-claude/prompt-caching.md) | Extended 1-hour cache duration for less frequently accessed but important context, complementing the standard 5-minute cache. | Claude API  Microsoft Foundry |
| [Search results](build-with-claude/search-results.md) | Enable natural citations for RAG applications by providing search results with proper source attribution. Achieve web search-quality citations for custom knowledge bases and tools. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Structured outputs](build-with-claude/structured-outputs.md) | Guarantee schema conformance with two approaches: JSON outputs for structured data responses, and strict tool use for validated tool inputs. | Claude API  Amazon Bedrock  Microsoft Foundry (Beta) |
| [Token counting](api/messages-count-tokens.md) | Token counting enables you to determine the number of tokens in a message before sending it to Claude, helping you make informed decisions about your prompts and usage. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Tool use](agents-and-tools/tool-use/overview.md) | Enable Claude to interact with external tools and APIs to perform a wider variety of tasks. For a list of supported tools, see [the Tools table](#tools). | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |

## Tools

These features enable Claude to interact with external systems, execute code, and perform automated tasks through various tool interfaces.

| Feature | Description | Availability |
| --- | --- | --- |
| [Bash](agents-and-tools/tool-use/bash-tool.md) | Execute bash commands and scripts to interact with the system shell and perform command-line operations. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Code execution](agents-and-tools/tool-use/code-execution-tool.md) | Run Python code in a sandboxed environment for advanced data analysis. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Programmatic tool calling](agents-and-tools/tool-use/programmatic-tool-calling.md) | Enable Claude to call your tools programmatically from within code execution containers, reducing latency and token consumption for multi-tool workflows. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Computer use](agents-and-tools/tool-use/computer-use-tool.md) | Control computer interfaces by taking screenshots and issuing mouse and keyboard commands. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Fine-grained tool streaming](agents-and-tools/tool-use/fine-grained-tool-streaming.md) | Stream tool use parameters without buffering/JSON validation, reducing latency for receiving large parameters. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [MCP connector](agents-and-tools/mcp-connector.md) | Connect to remote [MCP](mcp.md) servers directly from the Messages API without a separate MCP client. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Memory](agents-and-tools/tool-use/memory-tool.md) | Enable Claude to store and retrieve information across conversations. Build knowledge bases over time, maintain project context, and learn from past interactions. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Text editor](agents-and-tools/tool-use/text-editor-tool.md) | Create and edit text files with a built-in text editor interface for file manipulation tasks. | Claude API  Amazon Bedrock  Google Cloud's Vertex AI  Microsoft Foundry |
| [Tool search](agents-and-tools/tool-use/tool-search-tool.md) | Scale to thousands of tools by dynamically discovering and loading tools on-demand using regex-based search, optimizing context usage and improving tool selection accuracy. | Claude API (Beta)  Amazon Bedrock (Beta)  Google Cloud's Vertex AI (Beta)  Microsoft Foundry (Beta) |
| [Web fetch](agents-and-tools/tool-use/web-fetch-tool.md) | Retrieve full content from specified web pages and PDF documents for in-depth analysis. | Claude API (Beta)  Microsoft Foundry (Beta) |
| [Web search](agents-and-tools/tool-use/web-search-tool.md) | Augment Claude's comprehensive knowledge with current, real-world data from across the web. | Claude API  Google Cloud's Vertex AI  Microsoft Foundry |

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
