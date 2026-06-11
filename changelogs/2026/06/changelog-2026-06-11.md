# [Claude docs changes for June 11th, 2026](https://github.com/gpambrozio/ClaudeDocs/tree/a08d0715d715154d18f7843d1d58304765647859) [[diff](https://github.com/gpambrozio/ClaudeDocs/commit/a08d0715d715154d18f7843d1d58304765647859)]

## Executive Summary
- Sub-agents can now spawn their own sub-agents up to 5 levels deep (Claude Code 2.1.172)
- Vision documentation completely overhauled with accurate patch-based tokenization formula, coordinate handling guide, and reference Python code for computing exact resize dimensions
- Claude Fable 5 and Mythos 5 added to code execution, programmatic tool calling, web search/fetch dynamic filtering, structured outputs, and tool search supported models
- New advisor tool guidance: mid-conversation nudge pattern for Haiku executors and alternative system prompt optimized for coding workloads
- New `frontier_llm` refusal category documented — blocks requests that could assist development of competing AI models

## New Claude Code versions

### [2.1.172](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/versions/2.1.172.md)

#### New features

* Sub-agents can now spawn their own sub-agents (up to 5 levels deep)
* Amazon Bedrock now reads the AWS region from `~/.aws` config files when `AWS_REGION` isn't set, matching AWS SDK precedence; `/status` shows where the region came from
* Added a search bar when browsing a marketplace's plugins in `/plugin`
* Added `model` attribute to the `claude_code.lines_of_code.count` OTEL metric

#### Existing feature improvements

* Improved performance in long conversations by removing redundant message normalization and avoiding full message-history transforms when streaming tool-use state is unchanged
* Reduced idle CPU usage: `/goal` status chip no longer re-renders the terminal at 5 Hz while idle, and fewer UI re-renders while subagents run in parallel
* Improved Claude in Chrome tool loading: browser tools now load in a single batched call instead of one per tool
* `/code-review` now keeps the `ultra` option visible when not signed in to claude.ai, with an explanation that cloud review requires a claude.ai account

#### Major bug fixes

* Fixed sessions using 1M context without usage credits getting permanently stuck — the session now automatically compacts back under the standard context limit
* Fixed background agents potentially reading another directory's project settings (`.mcp.json` approvals, trust) when dispatched onto a pre-warmed worker
* Fixed `availableModels` restrictions not being applied to subagent model overrides, the agent dispatch model picker, and the advisor model
* Fixed `WebFetch(domain:*.example.com)` wildcard domain rules never matching subdomains in allow, deny, and ask position; also fixed file permission rules with mid-pattern wildcards (e.g. `Read(secrets-*/config.json)`) being rejected at startup
* Fixed background-session attach failing with EAUTH for sessions started on an older version after the daemon auto-updated

### [2.1.173](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/versions/2.1.173.md)

#### Major bug fixes

* Fixed Fable 5 model names with a `[1m]` suffix not being normalized — Fable 5 includes 1M context by default, so the suffix is now stripped automatically
* Fixed a spurious "sandbox dependencies missing" startup warning on Windows when sandbox was enabled in settings

-----

## Claude Code changes

### Changed documents

#### [Model Config](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/claude-code/model-config.md) [[Source](https://code.claude.com/docs/en/model-config)]

* Updated internal link for Fable 5 to point to the new combined model introduction page (`introducing-claude-fable-5-and-claude-mythos-5.md`) [[line 38](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/claude-code/model-config.md?plain=1#L38)] [[Source](https://code.claude.com/docs/en/model-config#work-with-fable-5)]

#### [Plugins](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/claude-code/plugins.md) [[Source](https://code.claude.com/docs/en/plugins)]

* Clarified that `claude-plugins-official` is registered on first interactive launch; non-interactive scripts that run before that must add it explicitly with `claude plugin marketplace add anthropics/claude-plugins-official` [[line 357](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/claude-code/plugins.md?plain=1#L357)] [[Source](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace)]
* Updated plugin submission URL for claude.ai to the new path (`/admin-settings/directory/submissions/plugins/new`) [[line 362](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/claude-code/plugins.md?plain=1#L362)] [[Source](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace)]
* Added note that the claude.ai submission form requires a Team or Enterprise organization; individual authors without such an org can use the Console form instead [[line 365](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/claude-code/plugins.md?plain=1#L365)] [[Source](https://code.claude.com/docs/en/plugins#submit-your-plugin-to-the-community-marketplace)]

-----

## API changes

### Changed documents

#### [Adaptive Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/adaptive-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

* Expanded documentation on `thinking.display` defaults — Claude Mythos Preview is now explicitly listed alongside Fable 5, Mythos 5, Opus 4.8, and 4.7 as defaulting to `"omitted"`; Claude Opus 4.6's default of `"summarized"` is now called out separately [[lines 221-230](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L221-L230)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]
* Improved guidance on stripping thinking blocks when switching models — now clearly separated into main rule and two named exceptions [[lines 271-279](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/adaptive-thinking.md?plain=1#L271-L279)] [[Source](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)]

#### [Advisor Tool](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/advisor-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

* Added new "Mid-conversation nudge for under-calling executors" section with code example — a nudge injected before turn 2 raised Haiku task pass rates ~7 points; Sonnet showed no benefit; Opus should not receive the nudge [[lines 247-310](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L247-L310)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]
* Added "Alternative system prompt for Haiku on coding workloads" — a specialized block that raised Haiku pass rates ~7.5 points on coding benchmarks, with a caveat that it costs ~4 points on browse/lookup workloads [[lines 490-537](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L490-L537)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]
* Added "Increasing advisor calls on Opus executors" section with a targeted checkpoint system prompt for under-calling Opus executors [[lines 539-553](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/advisor-tool.md?plain=1#L539-L553)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)]

#### [Code Execution Tool](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

* Added Claude Fable 5 and Claude Mythos 5 to the supported models table, including support for `code_execution_20260120` (REPL persistence and programmatic tool calling) [[lines 21-22](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/code-execution-tool.md?plain=1#L21-L22)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)]

#### [Extended Thinking](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/extended-thinking.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

* Added explicit documentation of the `thinking blocks cannot be modified` 400 error — explains its cause (application code filtering or rebuilding the assistant message) and links to the errors reference for fix steps [[line 392](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/extended-thinking.md?plain=1#L392)] [[Source](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)]

#### [Build with Claude Overview](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/overview.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

* Added "Fallback credit" entry to the features table — describes the beta feature for avoiding double prompt-cache costs on refused requests [[line 47](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/overview.md?plain=1#L47)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]
* Added "Server-side fallback" entry to the features table — describes the beta feature for retrying refused requests inside a single API call [[line 49](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/overview.md?plain=1#L49)] [[Source](https://platform.claude.com/docs/en/build-with-claude/overview)]

#### [Programmatic Tool Calling](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

* Added Claude Fable 5 and Claude Mythos 5 to the supported models table [[lines 21-22](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/programmatic-tool-calling.md?plain=1#L21-L22)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)]

#### [Refusals and Fallback](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/refusals-and-fallback.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

* Added `"frontier_llm"` as a new refusal `category` value — triggered when a request could assist development of competing AI models; benign ML work can also trigger it [[line 69](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L69)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]
* Improved documentation structure for streaming vs. non-streaming fallback behavior, now with separate labeled sections [[lines 214-237](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/refusals-and-fallback.md?plain=1#L214-L237)] [[Source](https://platform.claude.com/docs/en/build-with-claude/refusals-and-fallback)]

#### [Structured Outputs](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/structured-outputs.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

* Added Claude Fable 5 and Claude Mythos 5 to the list of supported models on both the Claude API and Vertex AI [[line 12](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/structured-outputs.md?plain=1#L12)] [[Source](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)]

#### [Tool Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

* Added Claude Fable 5 and Claude Mythos 5 to the model support list [[line 366](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/tool-search-tool.md?plain=1#L366)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)]

#### [Troubleshooting Tool Use](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

* Added new error section for "thinking blocks cannot be modified" 400 error — explains the cause and links to the errors reference [[lines 44-49](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/troubleshooting-tool-use.md?plain=1#L44-L49)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/troubleshooting-tool-use)]

#### [API and Data Retention](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/manage-claude/api-and-data-retention.md) [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

* Added documentation that organizations with a ZDR arrangement can enable 30-day data retention per workspace via Console, allowing Claude Fable 5 and Mythos 5 to be used in that workspace while other workspaces remain zero-retention [[lines 49-51](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/manage-claude/api-and-data-retention.md?plain=1#L49-L51)] [[Source](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)]

#### [Self-Hosted Sandboxes](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/managed-agents/self-hosted-sandboxes.md) [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

* Added Blaxel, E2B, Namespace, and Superserve to the list of platform-specific self-hosted sandbox guides [[line 30](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L30)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]
* Updated `ant` CLI version from `1.11.0` to `1.12.0` in the Dockerfile and install instructions [[line 112](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/managed-agents/self-hosted-sandboxes.md?plain=1#L112)] [[Source](https://platform.claude.com/docs/en/managed-agents/self-hosted-sandboxes)]

#### [Vision](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/vision.md) [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

* Replaced the approximate `width * height / 750` token formula with the accurate patch-based formula: `⌈width / 28⌉ × ⌈height / 28⌉` visual tokens (one token per 28×28 pixel block) [[line 45](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/vision.md?plain=1#L45)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]
* Updated image cost tables with exact token counts (removing approximations) and added a 4K (3840×2160) row showing that 4K and 1920×1080 images can have the same cost when both downscale to the same size [[lines 64-69](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/vision.md?plain=1#L64-L69)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]
* Added a major new section "Working with coordinates and bounding boxes" covering: how Claude's resize-and-pad pipeline works, a reference Python implementation of `resized_size()` and `to_relative_coordinates()`, guidance to always request absolute pixel coordinates, and separate subsections for pre-resizing before upload vs. rescaling coordinates after the fact [[lines 108-230](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/build-with-claude/vision.md?plain=1#L108-L230)] [[Source](https://platform.claude.com/docs/en/build-with-claude/vision)]

#### [Web Fetch Tool](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

* Added Claude Fable 5 and Claude Mythos 5 to the list of models that support dynamic filtering with `web_fetch_20260209` [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/web-fetch-tool.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)]

#### [Web Search Tool](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/web-search-tool.md) [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]

* Added Claude Fable 5 and Claude Mythos 5 to the list of models that support dynamic filtering with `web_search_20260209` [[line 7](https://github.com/gpambrozio/ClaudeDocs/blob/a08d0715d715154d18f7843d1d58304765647859/docs-md/api/agents-and-tools/tool-use/web-search-tool.md?plain=1#L7)] [[Source](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)]
