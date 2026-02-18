# [Claude docs changes for February 18th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/756487e) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/756487e)]

## Executive Summary
- Claude Sonnet 4.6 launches as the new flagship balanced model, replacing Sonnet 4.5 as the default across Claude Code and the API. It supports adaptive thinking, 1M token context window (beta), and free code execution when paired with web tools.
- Code execution, web fetch, web search, memory tool, programmatic tool calling, and tool search tool all graduate to general availability — no beta headers required.
- Web search and web fetch now support **dynamic filtering** (beta): Claude can write and execute code to filter results before they reach the context window, improving accuracy and reducing token costs.
- Claude Code 2.1.45 adds `spinnerTipsOverride` customization, `SDKRateLimitInfo` types, and fixes Agent Teams failures on Bedrock/Vertex/Foundry.
- The legal and compliance docs now include an explicit **Usage Policy** section clarifying that OAuth tokens from Free/Pro/Max plans cannot be used in third-party products or the Agent SDK.

## New Claude Code versions

### [2.1.45](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/versions/2.1.45.md)

#### New features

* Added support for Claude Sonnet 4.6 as the new default model
* Added support for reading `enabledPlugins` and `extraKnownMarketplaces` from `--add-dir` directories
* Added `spinnerTipsOverride` setting to customize spinner tips — configure `tips` with an array of custom tip strings, and optionally set `excludeDefault: true` to show only your custom tips instead of the built-in ones
* Added `SDKRateLimitInfo` and `SDKRateLimitEvent` types to the SDK, enabling consumers to receive rate limit status updates including utilization, reset times, and overage information

#### Existing feature improvements

* Improved startup performance by removing eager loading of session history for stats caching
* Improved memory usage for shell commands that produce large output — RSS no longer grows unboundedly with command output size
* Improved collapsed read/search groups to show the current file or search pattern being processed beneath the summary line while active
* [VSCode] Improved permission destination choice (project/user/session) to persist across sessions

#### Major bug fixes

* Fixed Agent Teams teammates failing on Bedrock, Vertex, and Foundry by propagating API provider environment variables to tmux-spawned processes
* Fixed sandbox "operation not permitted" errors when writing temporary files on macOS by using the correct per-user temp directory
* Fixed Task tool (backgrounded agents) crashing with a `ReferenceError` on completion
* Fixed autocomplete suggestions not being accepted on Enter when images are pasted in the input
* Fixed skills invoked by subagents incorrectly appearing in main session context after compaction
* Fixed excessive `.claude.json.backup` files accumulating on every startup
* Fixed plugin-provided commands, agents, and hooks not being available immediately after installation without requiring a restart

-----

## Claude Code changes

### Changed documents

#### [Amazon Bedrock](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/amazon-bedrock.md) [[Source](https://code.claude.com/docs/en/amazon-bedrock)]

* Updated default primary model to `claude-sonnet-4-6` (was `claude-sonnet-4-5-20250929`), reflected in the models table and example environment variable exports. [[line 165](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/amazon-bedrock.md?plain=1#L165)] [[Source](https://code.claude.com/docs/en/amazon-bedrock#4-model-configuration)]

#### [CLI Reference](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/cli-reference.md) [[Source](https://code.claude.com/docs/en/cli-reference)]

* Updated the `--model` flag example to reference `claude-sonnet-4-6`. [[line 48](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/cli-reference.md?plain=1#L48)] [[Source](https://code.claude.com/docs/en/cli-reference#cli-flags)]

#### [Costs](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/costs.md) [[Source](https://code.claude.com/docs/en/costs)]

* Updated average cost reference from Sonnet 4.5 to Sonnet 4.6. [[line 3](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/costs.md?plain=1#L3)] [[Source](https://code.claude.com/docs/en/costs)]

#### [GitHub Actions](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/github-actions.md) [[Source](https://code.claude.com/docs/en/github-actions)]

* Updated all model references to `claude-sonnet-4-6` in workflow examples (direct API and Bedrock). [[lines 104, 123, 530, 658](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/github-actions.md?plain=1#L104)]

#### [GitLab CI/CD](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/gitlab-ci-cd.md) [[Source](https://code.claude.com/docs/en/gitlab-ci-cd)]

* Updated Bedrock model ID example to `us.anthropic.claude-sonnet-4-6` (simplified format without version suffix). [[line 342](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/gitlab-ci-cd.md?plain=1#L342)] [[Source](https://code.claude.com/docs/en/gitlab-ci-cd#aws-bedrock-job-example-oidc)]

#### [Google Vertex AI](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/google-vertex-ai.md) [[Source](https://code.claude.com/docs/en/google-vertex-ai)]

* Updated default primary model to `claude-sonnet-4-6` and noted that Sonnet 4.6 supports the 1M token context window on Vertex AI. [[lines 95, 127](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/google-vertex-ai.md?plain=1#L95)]

#### [Hooks](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/hooks.md) [[Source](https://code.claude.com/docs/en/hooks)]

* Updated `SessionStart` hook example payload to show `claude-sonnet-4-6` as the model. [[line 642](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/hooks.md?plain=1#L642)] [[Source](https://code.claude.com/docs/en/hooks#sessionstart-input)]

#### [Legal and Compliance](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/legal-and-compliance.md) [[Source](https://code.claude.com/docs/en/legal-and-compliance)]

* Added a new **Usage Policy** section covering acceptable use and authentication/credential restrictions. OAuth tokens from Free, Pro, or Max accounts are exclusively for Claude Code and Claude.ai and cannot be used in third-party tools or the Agent SDK. Developers building on Claude must use API key authentication. [[lines 20-35](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/legal-and-compliance.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/legal-and-compliance#usage-policy)]

#### [MCP](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/mcp.md) [[Source](https://code.claude.com/docs/en/mcp)]

* Updated the featured MCP server list substantially — replaced niche/vertical integrations (Circleback, Clarify, Day AI, bioRxiv, ChEMBL, DevRev, etc.) with major platforms: Notion, Slack, Figma, Canva, Atlassian, Linear, Gamma, Sentry, Vercel, n8n, Hugging Face, Zapier, Stripe, Intercom, monday.com, ClickUp, Asana, Supabase, Amplitude, Box, PubMed, Miro, Cloudflare, Context7, Clay, Webflow, NetSuite, Ramp, and PayPal.

#### [Microsoft Foundry](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/microsoft-foundry.md) [[Source](https://code.claude.com/docs/en/microsoft-foundry)]

* Updated default Sonnet model environment variable to `claude-sonnet-4-6`. [[line 79](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/microsoft-foundry.md?plain=1#L79)] [[Source](https://code.claude.com/docs/en/microsoft-foundry#3-configure-claude-code)]

#### [Model Config](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Updated `sonnet` alias description to reflect that it now points to Sonnet 4.6. [[line 20](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/model-config.md?plain=1#L20)] [[Source](https://code.claude.com/docs/en/model-config#model-aliases)]
* Clarified default model behavior: Max and Team Premium now default to Opus 4.6; Pro and Team Standard now default to Sonnet 4.6. [[lines 131-132](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/model-config.md?plain=1#L131)] [[Source](https://code.claude.com/docs/en/model-config#default-model-setting)]

#### [Monitoring Usage](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/monitoring-usage.md) [[Source](https://code.claude.com/docs/en/monitoring-usage)]

* Updated all model identifier examples from `claude-sonnet-4-5-20250929` to `claude-sonnet-4-6` in telemetry attributes and event log schema. [[lines 313, 322, 389, 407](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/monitoring-usage.md?plain=1#L313)]

#### [Settings](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/settings.md) [[Source](https://code.claude.com/docs/en/settings)]

* Updated `model` setting example to `claude-sonnet-4-6`. [[line 150](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/settings.md?plain=1#L150)] [[Source](https://code.claude.com/docs/en/settings#available-settings)]
* Updated auto-generated commit attribution footer to reference `Claude Sonnet 4.6`. [[line 283](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/claude-code/settings.md?plain=1#L283)] [[Source](https://code.claude.com/docs/en/settings#attribution-settings)]

-----

## API changes

### Changed documents

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Adaptive thinking is now supported on **Claude Sonnet 4.6** in addition to Opus 4.6. [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]
* Clarified that extended thinking with `budget_tokens` is deprecated on both Opus 4.6 and Sonnet 4.6 but remains functional. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]
* Clarified interleaved thinking availability by mode: automatic with adaptive thinking on both models; supported via beta header with manual mode on Sonnet 4.6; not available with manual mode on Opus 4.6. [[lines 124-131](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L124)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Batch Processing](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/batch-processing.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

* Added Claude Sonnet 4.6 to the Batch API pricing table at $1.50/$7.50 per MTok (input/output). [[line 78](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/batch-processing.md?plain=1#L78)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]
* Clarified that the Batch API is **not** covered by Zero Data Retention (ZDR) arrangements. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/batch-processing.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/batch-processing)]

#### [Choosing a Model](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/choosing-a-model.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

* Updated the model recommendation table: Sonnet 4.6 replaces Sonnet 4.5 with the description "Frontier intelligence at scale—built for coding, agents, and enterprise workflows." [[line 58](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/choosing-a-model.md?plain=1#L58)] [[Source](https://platform.claude.com/docs/en/about-claude/models/choosing-a-model)]

#### [Code Execution Tool](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* **Code execution is now generally available** — beta header (`code-execution-2025-08-25`) is no longer required. All example requests updated accordingly. [[line 2](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L2)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* **Code execution is now free when used with web search or web fetch** (`web_search_20260209` or `web_fetch_20260209`). [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L8)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* Added Claude Sonnet 4.6 to the supported models table. [[line 21](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L21)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* Added platform availability section: available on Claude API and Microsoft Azure AI Foundry; not currently available on Amazon Bedrock or Google Vertex AI. [[lines 35-42](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L35)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* Clarified that code execution is **not** ZDR-eligible; data is retained per standard policy. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]
* Added code execution usage tracking example showing `server_tool_use.code_execution_requests` in the response. [[lines 568-578](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L568)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Compaction](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/compaction.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

* Clarified that the Compaction feature (beta) is **not** covered by ZDR arrangements. [[line 13](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/compaction.md?plain=1#L13)] [[Source](https://platform.claude.com/docs/en/build-with-claude/compaction)]

#### [Context Windows](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/context-windows.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

* Claude Sonnet 4.6 added to the 1M token context window support list (beta for tier 4+ orgs). [[line 90](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/context-windows.md?plain=1#L90)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]
* Sonnet 4.6 now features **context awareness** (tracks remaining token budget during long conversations), joining Sonnet 4.5 and Haiku 4.5. [[line 122](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/context-windows.md?plain=1#L122)] [[Source](https://platform.claude.com/docs/en/build-with-claude/context-windows)]

#### [Effort](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/effort.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

* The effort parameter is now supported on **Claude Sonnet 4.6** in addition to Opus 4.6 and Opus 4.5. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/effort.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]
* Added recommended effort levels for Sonnet 4.6: `medium` (recommended default), `low` for latency-sensitive workloads, `high` for maximum intelligence. [[lines 39-46](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/effort.md?plain=1#L39)] [[Source](https://platform.claude.com/docs/en/build-with-claude/effort)]

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Added Claude Sonnet 4.6 to the supported models list — supports both manual extended thinking with interleaved mode and adaptive thinking. [[line 15](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Updated interleaved thinking documentation: Opus 4.6 automatically enables it with adaptive thinking (beta header deprecated); Sonnet 4.6 supports it via beta header with manual mode or automatically with adaptive thinking. [[lines 277-285](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L277)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]
* Updated comparison table to include Sonnet 4.6 column. [[line 505](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L505)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Files](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/files.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

* Clarified that the Files API (beta) is **not** covered by ZDR arrangements. [[line 9](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/files.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/build-with-claude/files)]

#### [Intro](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/intro.md) [[Source](https://platform.claude.com/docs/en/intro)]

* Updated the featured model list: replaced Claude Sonnet 4.5 with **Claude Sonnet 4.6** as the featured balanced model. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/intro.md?plain=1#L8)] [[Source](https://platform.claude.com/docs/en/intro)]

#### [MCP Connector](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/mcp-connector.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]

* Clarified MCP connector is **not** ZDR-eligible (beta feature). [[line 11](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/mcp-connector.md?plain=1#L11)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)]
* Updated code examples to use `claude-sonnet-4-6`. [[lines 428, 444, 460](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/mcp-connector.md?plain=1#L428)]

#### [Memory Tool](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/memory-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]

* **Memory tool is now generally available** — beta header (`context-management-2025-06-27`) is no longer required. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L8)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]
* Added Claude Sonnet 4.6 to the supported models list. [[line 104](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L104)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]
* Clarified that memory tool is ZDR-eligible. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/memory-tool.md?plain=1#L10)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)]

#### [Migration Guide](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/migration-guide.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

* Added a comprehensive new section: **Migrating to Claude Sonnet 4.6**, covering breaking changes (assistant prefilling removed, JSON escaping differences, tool version updates), recommended changes (remove fine-grained tool streaming beta header, migrate `output_format`), and detailed migration paths for extended thinking, adaptive thinking, and effort levels. [[lines 158-330](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/migration-guide.md?plain=1#L158)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]
* Clarified that the `interleaved-thinking-2025-05-14` beta header deprecation applies to Opus 4.6 only; Sonnet 4.6 continues to support it. [[line 43](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/migration-guide.md?plain=1#L43)] [[Source](https://platform.claude.com/docs/en/about-claude/models/migration-guide)]

#### [Model Deprecations](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/model-deprecations.md) [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

* Added `claude-sonnet-4-6` with Active status and a deprecation date not sooner than February 17, 2027. [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/model-deprecations.md?plain=1#L69)] [[Source](https://platform.claude.com/docs/en/about-claude/model-deprecations)]

#### [Models Overview](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/overview.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

* **Claude Sonnet 4.6** replaces Sonnet 4.5 in the latest models comparison table. API ID is `claude-sonnet-4-6`. Adaptive thinking is now supported. Reliable knowledge cutoff is Aug 2025; training data cutoff is Jan 2026. [[lines 15-29](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/overview.md?plain=1#L15)] [[Source](https://platform.claude.com/docs/en/about-claude/models/overview)]

#### [Overview (Build with Claude)](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Code execution, memory, web fetch — updated to show GA status (no longer "Beta"). [[lines 30-32](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/overview.md?plain=1#L30)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* Programmatic tool calling and tool search — updated to show GA status. [[lines 52-53](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/overview.md?plain=1#L52)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* Updated code execution description: now "free when used with web search or web fetch." [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/overview.md?plain=1#L30)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [Pricing](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/pricing.md) [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

* Added **Claude Sonnet 4.6** pricing: $3/$15 per MTok (input/output), same as Sonnet 4.5. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/pricing.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Added Sonnet 4.6 to Batch API pricing table at $1.50/$7.50 per MTok. [[line 98](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/pricing.md?plain=1#L98)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Added Sonnet 4.6 to long context pricing (supported with 1M token context window beta). [[line 111](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/pricing.md?plain=1#L111)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Added Sonnet 4.6 to tool use system prompt token counts table. [[line 179](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/pricing.md?plain=1#L179)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]
* Expanded code execution pricing section to clarify free usage with web tools and added usage tracking example showing `server_tool_use.code_execution_requests`. [[lines 210-230](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/pricing.md?plain=1#L210)] [[Source](https://platform.claude.com/docs/en/about-claude/pricing)]

#### [Programmatic Tool Calling](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* **Programmatic tool calling is now generally available** — beta header (`advanced-tool-use-2025-11-20`) is no longer required. All example requests updated accordingly. [[line 2](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L2)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]
* Added Claude Sonnet 4.6 to the supported models table. [[line 18](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L18)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]
* Clarified programmatic tool calling is **not** ZDR-eligible. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L8)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

#### [Prompt Caching](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/prompt-caching.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

* Added Claude Sonnet 4.6 to the supported models list and pricing table. [[lines 92, 121](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L92)]
* Added a note that prompt caching may be suitable for ZDR customers (it stores KV cache representations and hashes, not raw prompt text). [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/prompt-caching.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)]

#### [Rate Limits](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/api/rate-limits.md) [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

* Updated Sonnet 4.x rate limit footnote to include Sonnet 4.6 in the combined traffic pool. [[line 132](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/api/rate-limits.md?plain=1#L132)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]
* Added Sonnet 4.6 to the long context rate limits section. [[line 172](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/api/rate-limits.md?plain=1#L172)] [[Source](https://platform.claude.com/docs/en/api/rate-limits)]

#### [Release Notes Overview](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/release-notes/overview.md) [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

* Added February 17, 2026 release notes: Sonnet 4.6 launch, code execution now free with web tools, web search and programmatic tool calling going GA, and additional tools graduating to GA. [[lines 9-15](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/release-notes/overview.md?plain=1#L9)] [[Source](https://platform.claude.com/docs/en/release-notes/overview)]

#### [Remote MCP Servers](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/remote-mcp-servers.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/remote-mcp-servers)]

* Updated the remote MCP server examples list to feature major platforms: Notion, Slack, Figma, Canva, Linear, HubSpot, Gamma, Sentry, Vercel, n8n, Hugging Face, Granola, Zapier, Stripe, Intercom, monday.com, ClickUp, Asana, Supabase, Amplitude, Box, Miro, Cloudflare, Context7, Webflow, Netlify, and more.

#### [Skills Guide](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/skills-guide.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

* Clarified that the Skills feature (beta) is **not** ZDR-eligible. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/skills-guide.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/skills-guide)]

#### [Tool Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

* **Tool search tool is now generally available** — beta headers removed from examples. [[line 14](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L14)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]
* Clarified ZDR status: server-side tool search is **not** ZDR-eligible; custom client-side implementations are. [[line 16](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L16)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

#### [Web Fetch Tool](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* **Web fetch tool is now generally available** — beta header (`web-fetch-2025-09-10`) is no longer required. All example requests updated. [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]
* Added Claude Sonnet 4.6 to the supported models list. [[line 29](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L29)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]
* Added new `web_fetch_20260209` tool version supporting **dynamic filtering** (beta): use with `code-execution-web-tools-2026-02-09` beta header to let Claude filter fetched content using code execution before it reaches the context window. [[lines 49-92](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L49)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]
* Clarified web fetch is ZDR-eligible. [[line 10](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L10)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

#### [Web Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* **Web search tool is now generally available** (no beta header required). [[line 4](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L4)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]
* Added Claude Sonnet 4.6 to the supported models list. [[line 19](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L19)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]
* Added new `web_search_20260209` tool version supporting **dynamic filtering** (beta): Claude can write and execute code to post-process search results before they reach context, improving accuracy and reducing token costs. Requires `code-execution-web-tools-2026-02-09` beta header. [[lines 34-75](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L34)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]
* Clarified web search is ZDR-eligible. [[line 8](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L8)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

#### [What's New in Claude 4.6](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/whats-new-claude-4-6.md) [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]

* Added **Claude Sonnet 4.6** (`claude-sonnet-4-6`) to the models table — supports 200K context (with 1M token beta), 64K max output, extended thinking, and adaptive thinking. [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]
* Documented adaptive thinking support for Sonnet 4.6 including effort parameter recommendations. [[lines 31-48](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L31)] [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]
* Added new section: **Code execution is now free with web tools** when `web_search_20260209` or `web_fetch_20260209` is included in requests. [[lines 42-45](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L42)] [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]
* Added new section: **Improved web search and web fetch with dynamic filtering** (beta) — available for Opus 4.6 and Sonnet 4.6 via `code-execution-web-tools-2026-02-09` beta header. [[lines 48-52](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L48)] [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]
* Added new section: **Tools graduating to general availability**: code execution, web fetch, programmatic tool calling, tool search, tool use examples, and memory tool. [[lines 54-63](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L54)] [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]
* Clarified that `interleaved-thinking-2025-05-14` beta header is deprecated on Opus 4.6 but continues to be supported on Sonnet 4.6. [[lines 101-103](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/about-claude/models/whats-new-claude-4-6.md?plain=1#L101)] [[Source](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-6)]

#### [Zero Data Retention](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/zero-data-retention.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]

* Added web search, web fetch, memory tool, and client-side tool search to the ZDR-eligible features table. [[lines 38-41](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/zero-data-retention.md?plain=1#L38)] [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]
* Added code execution, programmatic tool calling, and server-side tool search to the not-ZDR-eligible table with retention policy details. [[lines 50-52](https://github.com/gpambrozio/ClaudeDocs/blob/756487e/docs-md/api/build-with-claude/zero-data-retention.md?plain=1#L50)] [[Source](https://platform.claude.com/docs/en/build-with-claude/zero-data-retention)]
