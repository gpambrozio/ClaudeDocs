# [Claude docs changes for March 3rd, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/2ff1e5f) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/2ff1e5f)]

## Executive Summary
- Agent SDK stop-reasons doc overhauled: `stop_reason` on `ResultMessage` is now TypeScript-only; Python users need a stream-event workaround
- File checkpointing simplified: the `CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING` environment variable is no longer required
- Data residency expanded: US-only inference now costs 1.1x standard rate for Opus 4.6+, with new workspace-level geo controls
- Fast mode constraints clarified: Opus 4.6 only, not available with Batch API or Priority Tier, and switching speeds invalidates prompt cache
- New MCP servers added: Customer.io, MailerLite, Clerk, Gusto, and Airtable

-----

## Claude Code changes

### Changed documents

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Three new MCP servers added: **Customer.io** (explore customer data), **MailerLite** (email marketing assistant), and **Clerk** (authentication, organizations, and billing). [[MCP servers list](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/claude-code/mcp.md?plain=1#L498)]
* **PostHog** changed from requiring a user-specific URL to providing a direct public endpoint (`https://mcp.posthog.com/mcp`). [[line 501](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/claude-code/mcp.md?plain=1#L501)] [[Source](https://code.claude.com/docs/en/mcp#popular-mcp-servers)]

-----

## API changes

### Changed documents

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Minor wording fix: "Claude will almost always think" corrected to "Claude almost always thinks" for accuracy.

#### [Agent Skills - Best Practices](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agents-and-tools/agent-skills/best-practices.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)]

* Widespread punctuation normalization throughout the document (bold labels now use `:` consistently). No substantive content changes.

#### [Agent Skills - Quickstart](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agents-and-tools/agent-skills/quickstart.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/quickstart)]

* Section header renamed from "What are Agent Skills?" to "Agent Skills overview". Minor wording normalization throughout.

#### [Batch Processing](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Results format description clarified: results are in `.jsonl` format (rewording from future to present tense).

#### [Data Residency](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/data-residency.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]

* Added pricing details: US-only inference (`inference_geo: "us"`) is priced at **1.1x the standard rate** for Opus 4.6 and newer models across all token pricing categories. [[line 82](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/data-residency.md?plain=1#L82)] [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]
* Added distinction between **inference geo** (per-request, `inference_geo` parameter) and **workspace geo** (data at rest and endpoint processing, configured in Console). [[lines 7-9](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/data-residency.md?plain=1#L7-L9)] [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]
* Documented two new workspace settings: `allowed_inference_geos` (restricts which geos a workspace can use) and `default_inference_geo` (fallback when `inference_geo` is omitted). [[lines 63-64](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/data-residency.md?plain=1#L63-L64)] [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]
* Added note about Priority Tier: the 1.1x US inference multiplier also affects committed TPM burndown. [[line 88](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/data-residency.md?plain=1#L88)] [[Source](https://platform.claude.com/docs/en/build-with-claude/data-residency)]

#### [Effort](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* Added new guidance on effort level use cases: **low effort** is recommended for high-volume or latency-sensitive workloads and chat/non-coding tasks; **high effort** for tasks requiring maximum intelligence from Sonnet 4.6. [[lines near effort table](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/effort.md?plain=1#L1)]
* Section header renamed from "When should I adjust the effort parameter?" to "When to adjust the effort parameter".

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Minor wording fix: clarified that using `max` effort on unsupported models "return an error" (present tense).

#### [Fast Mode](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/fast-mode.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]

* Added new **Limitations** section with multiple constraints: [[lines 164-168](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/fast-mode.md?plain=1#L164-L168)] [[Source](https://platform.claude.com/docs/en/build-with-claude/fast-mode)]
  * Fast mode is currently supported on **Opus 4.6 only**; sending `speed: "fast"` with another model returns an error
  * Switching between fast and standard speed **invalidates the prompt cache**; requests at different speeds do not share cached prefixes
  * Fast mode benefits focus on **output tokens per second (OTPS)**, not time to first token (TTFT)
  * Fast mode is **not available** with the Batch API
  * Fast mode is **not available** with Priority Tier

#### [File Checkpointing](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/file-checkpointing.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/file-checkpointing)]

* **Removed requirement** for the `CLAUDE_CODE_ENABLE_SDK_FILE_CHECKPOINTING` environment variable. File checkpointing now only requires setting `enable_file_checkpointing=True` (Python) or `enableFileCheckpointing: true` (TypeScript) in the SDK options. All code examples and the step-by-step guide updated accordingly. [[line 57](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/file-checkpointing.md?plain=1#L57)] [[Source](https://platform.claude.com/docs/en/agent-sdk/file-checkpointing)]
* Troubleshooting section updated: the "CheckpointNotFound" error cause now correctly references the missing `enable_file_checkpointing` flag rather than the old environment variable. [[line 436](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/file-checkpointing.md?plain=1#L436)] [[Source](https://platform.claude.com/docs/en/agent-sdk/file-checkpointing)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Added a note that users can contact Anthropic for higher file storage limits.

#### [Handle Stop Reasons](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/stop-reasons.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/stop-reasons)]

* **Major rewrite**: Clarified that `stop_reason` on `ResultMessage` is currently **TypeScript-only**. The Python SDK's `ResultMessage` does not include this field yet. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/stop-reasons.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/agent-sdk/stop-reasons)]
* All primary code examples converted to TypeScript; a new **"Read stop\_reason in Python"** section added with a workaround using `include_partial_messages=True` and scanning `StreamEvent` messages for `message_delta` events. [[line 105](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/stop-reasons.md?plain=1#L105)] [[Source](https://platform.claude.com/docs/en/agent-sdk/stop-reasons)]
* Added a new **"Detect refusals"** section with a TypeScript example for checking `stop_reason === "refusal"`. [[line near 70](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/stop-reasons.md?plain=1#L70)]

#### [Implement Tool Use](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agents-and-tools/tool-use/implement-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use)]

* Added descriptive alt text to the `tool_choice` options diagram image. [[line 483](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agents-and-tools/tool-use/implement-tool-use.md?plain=1#L483)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use)]

#### [Migration Guide (Agent SDK)](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/migration-guide.md) [[Source](https://platform.claude.com/docs/en/agent-sdk/migration-guide)]

* Corrected "Before" package version for `@anthropic-ai/claude-code` from `^1.0.0` to `^0.0.42`. [[line 56](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/migration-guide.md?plain=1#L56)] [[Source](https://platform.claude.com/docs/en/agent-sdk/migration-guide)]
* Updated `@anthropic-ai/claude-agent-sdk` target version from `^0.1.0` to `^0.2.0`. [[line 66](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/migration-guide.md?plain=1#L66)] [[Source](https://platform.claude.com/docs/en/agent-sdk/migration-guide)]
* Fixed Python "Before" migration example to correctly show `from claude_code_sdk import` (was incorrectly showing `from claude_agent_sdk import`). [[line 130](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agent-sdk/migration-guide.md?plain=1#L130)] [[Source](https://platform.claude.com/docs/en/agent-sdk/migration-guide)]

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* New MCP servers added: **Airtable** (bring structured data to Claude), **Gusto** (query and analyze Gusto data), **Customer.io** (explore customer data), **MailerLite** (email marketing assistant), and **Clerk** (authentication, organizations, and billing).

#### [SDK - C#](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/api/sdks/csharp.md) [[Source](https://platform.claude.com/docs/en/api/sdks/csharp)]

* Added integration notes for Bedrock (`Anthropic.Bedrock`) and Foundry (`Anthropic.Foundry`) client variants.

#### [SDK - Go](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/api/sdks/go.md) [[Source](https://platform.claude.com/docs/en/api/sdks/go)]

* Added integration notes for Bedrock (`github.com/anthropics/anthropic-sdk-go/bedrock`) and Vertex AI (`github.com/anthropics/anthropic-sdk-go/vertex`) packages.

#### [SDK - Java](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/api/sdks/java.md) [[Source](https://platform.claude.com/docs/en/api/sdks/java)]

* Added integration notes for Bedrock (`com.anthropic:anthropic-java-bedrock`), Vertex AI (`com.anthropic:anthropic-java-vertex`), and Foundry (`com.anthropic:anthropic-java-foundry`) packages.

#### [SDK - Ruby](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/api/sdks/ruby.md) [[Source](https://platform.claude.com/docs/en/api/sdks/ruby)]

* Added integration notes for Bedrock (`Anthropic::BedrockClient`) and Vertex AI (`Anthropic::VertexClient`) clients.

#### [SDK - TypeScript](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/api/sdks/typescript.md) [[Source](https://platform.claude.com/docs/en/api/sdks/typescript)]

* Added integration notes for Bedrock (`@anthropic-ai/bedrock-sdk`), Vertex AI (`@anthropic-ai/vertex-sdk`), and Foundry (`@anthropic-ai/foundry-sdk`) packages.

#### [Skills Guide](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* Added explicit limits: **maximum 8 Skills per request** and **maximum 8MB total upload size** per Skill. [[lines 586-587](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/skills-guide.md?plain=1#L586-L587)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]
* Documented that changing the Skills list in a container breaks the prompt cache.

#### [Zero Data Retention](https://github.com/gpambrozio/ClaudeDocs/blob/2ff1e5f/docs-md/api/build-with-claude/zero-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]

* Added **1M Token Context Window** to the ZDR-eligible features table. The extended context window via `anthropic-beta: context-1m-2025-08-07` is now confirmed ZDR-eligible.
