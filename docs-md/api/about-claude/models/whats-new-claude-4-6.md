# What's new in Claude 4.6

Copy page

Claude 4.6 represents the next generation of Claude models, bringing significant new capabilities and API improvements. This page summarizes all new features available at launch.

## New models

| Model | API model ID | Description |
| --- | --- | --- |
| Claude Opus 4.6 | `claude-opus-4-6` | Our most intelligent model for building agents and coding |
| Claude Sonnet 4.6 | `claude-sonnet-4-6` | Our best combination of speed and intelligence |

Claude Opus 4.6 supports a 200K context window (with [1M token context window](build-with-claude/context-windows.md) available in beta), 128K max output tokens, extended thinking, and all existing Claude API features.

Claude Sonnet 4.6 supports a 200K context window (with [1M token context window](build-with-claude/context-windows.md) available in beta), 64K max output tokens, extended thinking, and adaptive thinking.

For complete pricing and specs, see the [models overview](about-claude/models/overview.md).

## New features

### Adaptive thinking mode

[Adaptive thinking](build-with-claude/adaptive-thinking.md) (`thinking: {type: "adaptive"}`) is the recommended thinking mode for Opus 4.6 and Sonnet 4.6. Claude dynamically decides when and how much to think. At the default effort level (`high`), Claude will almost always think. At lower effort levels, it may skip thinking for simpler problems.

`thinking: {type: "enabled"}` and `budget_tokens` are **deprecated** on Opus 4.6 and Sonnet 4.6. They remain functional but will be removed in a future model release. Use adaptive thinking and the [effort parameter](build-with-claude/effort.md) to control thinking depth instead. Adaptive thinking also automatically enables interleaved thinking.

```shiki
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[{"role": "user", "content": "Solve this complex problem..."}],
)
```

### Effort parameter GA

The [effort parameter](build-with-claude/effort.md) is now generally available (no beta header required). A new `max` effort level provides the absolute highest capability on Opus 4.6. Combine effort with adaptive thinking for optimal cost-quality tradeoffs.

Sonnet 4.6 introduces the effort parameter to the Sonnet family. Consider setting effort to `medium` for most Sonnet 4.6 use cases to balance speed, cost, and performance.

### Code execution is now free with web tools

[Code execution](agents-and-tools/tool-use/code-execution-tool.md) is now free when used with [web search](agents-and-tools/tool-use/web-search-tool.md) or [web fetch](agents-and-tools/tool-use/web-fetch-tool.md). When either tool is included in your API request, there are no additional charges for code execution beyond standard input and output token costs. Code execution enables dynamic filtering in web search and web fetch tools, improving accuracy while reducing token consumption. See the [code execution pricing](agents-and-tools/tool-use/code-execution-tool.md) for details on standalone usage.

### Improved web search and web fetch with dynamic filtering

[Web search](agents-and-tools/tool-use/web-search-tool.md) and [web fetch](agents-and-tools/tool-use/web-fetch-tool.md) tools now support dynamic filtering with Opus 4.6 and Sonnet 4.6. Claude can write and execute code to filter results before they reach the context window, keeping only relevant information and improving accuracy while reducing token consumption. To enable dynamic filtering, use the `web_search_20260209` or `web_fetch_20260209` tool versions.

### Tools graduating to general availability

The following tools are now generally available:

- [Code execution](agents-and-tools/tool-use/code-execution-tool.md) (free with web tools)
- [Web fetch](agents-and-tools/tool-use/web-fetch-tool.md)
- [Programmatic tool calling](agents-and-tools/tool-use/programmatic-tool-calling.md)
- [Tool search tool](agents-and-tools/tool-use/tool-search-tool.md)
- [Tool use examples](agents-and-tools/tool-use/implement-tool-use.md)
- [Memory tool](agents-and-tools/tool-use/memory-tool.md)

### Compaction API (beta)

[Compaction](build-with-claude/compaction.md) provides automatic, server-side context summarization, enabling effectively infinite conversations. When context approaches the window limit, the API automatically summarizes earlier parts of the conversation.

### Fast mode (research preview)

[Fast mode](build-with-claude/fast-mode.md) (`speed: "fast"`) delivers significantly faster output token generation for Opus models. Fast mode is up to 2.5x as fast at premium pricing ($30/$150 per MTok). This is the same model running with faster inference (no change to intelligence or capabilities).

```shiki
response = client.beta.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "Refactor this module..."}],
)
```

### Fine-grained tool streaming (GA)

[Fine-grained tool streaming](agents-and-tools/tool-use/fine-grained-tool-streaming.md) is now generally available on all models and platforms. No beta header is required.

### 128K output tokens

Opus 4.6 supports up to 128K output tokens, doubling the previous 64K limit. This enables longer thinking budgets and more comprehensive responses. The SDKs require streaming for requests with large `max_tokens` values to avoid HTTP timeouts. If you don't need to process events incrementally, use `.stream()` with `.get_final_message()` to get the complete response. See [Streaming Messages](build-with-claude/streaming.md) for details.

### Data residency controls

[Data residency controls](build-with-claude/data-residency.md) allow you to specify where model inference runs using the `inference_geo` parameter. You can choose `"global"` (default) or `"us"` routing per request. US-only inference is priced at 1.1x on Claude Opus 4.6 and newer models.

## Deprecations

### `type: "enabled"` and `budget_tokens`

`thinking: {type: "enabled", budget_tokens: N}` is **deprecated** on Opus 4.6. It remains functional but will be removed in a future model release. Migrate to `thinking: {type: "adaptive"}` with the [effort parameter](build-with-claude/effort.md).

### `interleaved-thinking-2025-05-14` beta header

The `interleaved-thinking-2025-05-14` beta header is **deprecated** on Opus 4.6. It is safely ignored if included, but is no longer required. [Adaptive thinking](build-with-claude/adaptive-thinking.md) automatically enables [interleaved thinking](build-with-claude/extended-thinking.md). Remove `betas=["interleaved-thinking-2025-05-14"]` from your requests when using Opus 4.6.

**Sonnet 4.6** continues to support the `interleaved-thinking-2025-05-14` beta header for use with manual extended thinking (`thinking: {type: "enabled"}`). You can use either interleaved thinking with the beta header or adaptive thinking on Sonnet 4.6.

### `output_format`

The `output_format` parameter for [structured outputs](build-with-claude/structured-outputs.md) has been moved to `output_config.format`. The old parameter remains functional but is deprecated and will be removed in a future model release.

```shiki
# Before
response = client.messages.create(
    output_format={"type": "json_schema", "schema": {...}},
    # ...
)

# After
response = client.messages.create(
    output_config={"format": {"type": "json_schema", "schema": {...}}},
    # ...
)
```

## Breaking changes

### Prefill removal

Prefilling assistant messages (last-assistant-turn prefills) is **not supported** on Opus 4.6. Requests with prefilled assistant messages return a 400 error.

**Alternatives:**

- [Structured outputs](build-with-claude/structured-outputs.md) for controlling response format
- System prompt instructions for guiding response style
- [`output_config.format`](build-with-claude/structured-outputs.md) for JSON output

### Tool parameter quoting

Opus 4.6 may produce slightly different JSON string escaping in tool call arguments (e.g., different handling of Unicode escapes or forward slash escaping). Standard JSON parsers handle these differences automatically. If you parse tool call `input` as a raw string rather than using `json.loads()` or `JSON.parse()`, verify your parsing logic still works.

## Migration guide

For step-by-step migration instructions, see [Migrating to Claude 4.6](about-claude/models/migration-guide.md).

## Next steps

[Adaptive thinking

Learn how to use adaptive thinking mode.](build-with-claude/adaptive-thinking.md)[Models overview

Compare all Claude models.](about-claude/models/overview.md)[Compaction

Explore server-side context compaction.](build-with-claude/compaction.md)[Fast mode

Faster output token generation for Opus models.](build-with-claude/fast-mode.md)[Migration guide

Step-by-step migration instructions.](about-claude/models/migration-guide.md)

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
