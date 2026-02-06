# Adaptive thinking

Copy page

Adaptive thinking is the recommended way to use [extended thinking](build-with-claude/extended-thinking.md) with Claude Opus 4.6. Instead of manually setting a thinking token budget, adaptive thinking lets Claude dynamically decide when and how much to think based on the complexity of each request.

Adaptive thinking reliably drives better performance than extended thinking with a fixed `budget_tokens`, and we recommend moving to adaptive thinking to get the most intelligent responses from Opus 4.6. No beta header is required.

## Supported models

Adaptive thinking is supported on the following models:

- Claude Opus 4.6 (`claude-opus-4-6`)

`thinking.type: "enabled"` and `budget_tokens` are **deprecated** on Opus 4.6 and will be removed in a future model release. Use `thinking.type: "adaptive"` with the [effort parameter](build-with-claude/effort.md) instead.

Older models (Sonnet 4.5, Opus 4.5, etc.) do not support adaptive thinking and require `thinking.type: "enabled"` with `budget_tokens`.

## How adaptive thinking works

In adaptive mode, thinking is optional for the model. Claude evaluates the complexity of each request and decides whether and how much to think. At the default effort level (`high`), Claude will almost always think. At lower effort levels, Claude may skip thinking for simpler problems.

Adaptive thinking also automatically enables [interleaved thinking](build-with-claude/extended-thinking.md). This means Claude can think between tool calls, making it especially effective for agentic workflows.

## How to use adaptive thinking

Set `thinking.type` to `"adaptive"` in your API request:

Shell

```shiki
curl https://api.anthropic.com/v1/messages \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --data \
'{
    "model": "claude-opus-4-6",
    "max_tokens": 16000,
    "thinking": {
        "type": "adaptive"
    },
    "messages": [
        {
            "role": "user",
            "content": "Explain why the sum of two even numbers is always even."
        }
    ]
}'
```

## Adaptive thinking with the effort parameter

You can combine adaptive thinking with the [effort parameter](build-with-claude/effort.md) to guide how much thinking Claude does. The effort level acts as soft guidance for Claude's thinking allocation:

| Effort level | Thinking behavior |
| --- | --- |
| `max` | Claude always thinks with no constraints on thinking depth. Opus 4.6 only — requests using `max` on other models will return an error. |
| `high` (default) | Claude always thinks. Provides deep reasoning on complex tasks. |
| `medium` | Claude uses moderate thinking. May skip thinking for very simple queries. |
| `low` | Claude minimizes thinking. Skips thinking for simple tasks where speed matters most. |

Python

```shiki
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=16000,
    thinking={
        "type": "adaptive"
    },
    output_config={
        "effort": "medium"
    },
    messages=[{
        "role": "user",
        "content": "What is the capital of France?"
    }]
)

print(response.content[0].text)
```

## Streaming with adaptive thinking

Adaptive thinking works seamlessly with [streaming](build-with-claude/streaming.md). Thinking blocks are streamed via `thinking_delta` events just like manual thinking mode:

Python

```shiki
import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    model="claude-opus-4-6",
    max_tokens=16000,
    thinking={"type": "adaptive"},
    messages=[{"role": "user", "content": "What is the greatest common divisor of 1071 and 462?"}],
) as stream:
    for event in stream:
        if event.type == "content_block_start":
            print(f"\nStarting {event.content_block.type} block...")
        elif event.type == "content_block_delta":
            if event.delta.type == "thinking_delta":
                print(event.delta.thinking, end="", flush=True)
            elif event.delta.type == "text_delta":
                print(event.delta.text, end="", flush=True)
```

## Adaptive vs manual vs disabled thinking

| Mode | Config | Availability | When to use |
| --- | --- | --- | --- |
| **Adaptive** | `thinking: {type: "adaptive"}` | Opus 4.6 | Claude decides when and how much to think. Use `effort` to guide. |
| **Manual** | `thinking: {type: "enabled", budget_tokens: N}` | All models. Deprecated on Opus 4.6 — use adaptive mode instead. | When you need precise control over thinking token spend. |
| **Disabled** | Omit `thinking` parameter | All models | When you don't need extended thinking and want the lowest latency. |

Adaptive thinking is currently available on Opus 4.6. Older models only support `type: "enabled"` with `budget_tokens`. On Opus 4.6, `type: "enabled"` with `budget_tokens` is still accepted but deprecated — we recommend using adaptive thinking with the [effort parameter](build-with-claude/effort.md) instead.

## Important considerations

### Validation changes

When using adaptive thinking, previous assistant turns don't need to start with thinking blocks. This is more flexible than manual mode, where the API enforces that thinking-enabled turns begin with a thinking block.

### Prompt caching

Consecutive requests using `adaptive` thinking preserve [prompt cache](build-with-claude/prompt-caching.md) breakpoints. However, switching between `adaptive` and `enabled`/`disabled` thinking modes breaks cache breakpoints for messages. System prompts and tool definitions remain cached regardless of mode changes.

### Tuning thinking behavior

Adaptive thinking's triggering behavior is promptable. If Claude is thinking more or less often than you'd like, you can add guidance to your system prompt:

```inline-block
Extended thinking adds latency and should only be used when it
will meaningfully improve answer quality — typically for problems
that require multi-step reasoning. When in doubt, respond directly.
```

Steering Claude to think less often may reduce quality on tasks that benefit from reasoning. Measure the impact on your specific workloads before deploying prompt-based tuning to production. Consider testing with lower [effort levels](build-with-claude/effort.md) first.

### Cost control

Use `max_tokens` as a hard limit on total output (thinking + response text). The `effort` parameter provides additional soft guidance on how much thinking Claude allocates. Together, these give you effective control over cost.

At `high` and `max` effort levels, Claude may think more extensively and can be more likely to exhaust the `max_tokens` budget. If you observe `stop_reason: "max_tokens"` in responses, consider increasing `max_tokens` to give the model more room, or lowering the effort level.

## Working with thinking blocks

The following concepts apply to all models that support extended thinking, regardless of whether you use adaptive or manual mode.

### Summarized thinking

With extended thinking enabled, the Messages API for Claude 4 models returns a summary of Claude's full thinking process. Summarized thinking provides the full intelligence benefits of extended thinking, while preventing misuse.

Here are some important considerations for summarized thinking:

- You're charged for the full thinking tokens generated by the original request, not the summary tokens.
- The billed output token count will **not match** the count of tokens you see in the response.
- The first few lines of thinking output are more verbose, providing detailed reasoning that's particularly helpful for prompt engineering purposes.
- As Anthropic seeks to improve the extended thinking feature, summarization behavior is subject to change.
- Summarization preserves the key ideas of Claude's thinking process with minimal added latency, enabling a streamable user experience and easy migration from Claude Sonnet 3.7 to Claude 4 and later models.
- Summarization is processed by a different model than the one you target in your requests. The thinking model does not see the summarized output.

Claude Sonnet 3.7 continues to return full thinking output.

In rare cases where you need access to full thinking output for Claude 4 models, [contact our sales team](/cdn-cgi/l/email-protection#6c1f0d00091f2c0d0218041e031c050f420f0301).

### Thinking encryption

Full thinking content is encrypted and returned in the `signature` field. This field is used to verify that thinking blocks were generated by Claude when passed back to the API.

It is only strictly necessary to send back thinking blocks when using [tools with extended thinking](build-with-claude/extended-thinking.md). Otherwise you can omit thinking blocks from previous turns, or let the API strip them for you if you pass them back.

If sending back thinking blocks, we recommend passing everything back as you received it for consistency and to avoid potential issues.

Here are some important considerations on thinking encryption:

- When [streaming responses](build-with-claude/extended-thinking.md), the signature is added via a `signature_delta` inside a `content_block_delta` event just before the `content_block_stop` event.
- `signature` values are significantly longer in Claude 4 models than in previous models.
- The `signature` field is an opaque field and should not be interpreted or parsed - it exists solely for verification purposes.
- `signature` values are compatible across platforms (Claude APIs, [Amazon Bedrock](build-with-claude/claude-on-amazon-bedrock.md), and [Vertex AI](build-with-claude/claude-on-vertex-ai.md)). Values generated on one platform will be compatible with another.

### Thinking redaction

Occasionally Claude's internal reasoning will be flagged by our safety systems. When this occurs, we encrypt some or all of the `thinking` block and return it to you as a `redacted_thinking` block. `redacted_thinking` blocks are decrypted when passed back to the API, allowing Claude to continue its response without losing context.

When building customer-facing applications that use extended thinking:

- Be aware that redacted thinking blocks contain encrypted content that isn't human-readable
- Consider providing a simple explanation like: "Some of Claude's internal reasoning has been automatically encrypted for safety reasons. This doesn't affect the quality of responses."
- If showing thinking blocks to users, you can filter out redacted blocks while preserving normal thinking blocks
- Be transparent that using extended thinking features may occasionally result in some reasoning being encrypted
- Implement appropriate error handling to gracefully manage redacted thinking without breaking your UI

Here's an example showing both normal and redacted thinking blocks:

```shiki
{
  "content": [
    {
      "type": "thinking",
      "thinking": "Let me analyze this step by step...",
      "signature": "WaUjzkypQ2mUEVM36O2TxuC06KN8xyfbJwyem2dw3URve/op91XWHOEBLLqIOMfFG/UvLEczmEsUjavL...."
    },
    {
      "type": "redacted_thinking",
      "data": "EmwKAhgBEgy3va3pzix/LafPsn4aDFIT2Xlxh0L5L8rLVyIwxtE3rAFBa8cr3qpPkNRj2YfWXGmKDxH4mPnZ5sQ7vB9URj2pLmN3kF8/dW5hR7xJ0aP1oLs9yTcMnKVf2wRpEGjH9XZaBt4UvDcPrQ..."
    },
    {
      "type": "text",
      "text": "Based on my analysis..."
    }
  ]
}
```

Seeing redacted thinking blocks in your output is expected behavior. The model can still use this redacted reasoning to inform its responses while maintaining safety guardrails.

If you need to test redacted thinking handling in your application, you can use this special test string as your prompt: `ANTHROPIC_MAGIC_STRING_TRIGGER_REDACTED_THINKING_46C9A13E193C177646C7398A98432ECCCE4C1253D5E2D82641AC0E52CC2876CB`

When passing `thinking` and `redacted_thinking` blocks back to the API in a multi-turn conversation, you must include the complete unmodified block back to the API for the last assistant turn. This is critical for maintaining the model's reasoning flow. We suggest always passing back all thinking blocks to the API. For more details, see the [Preserving thinking blocks](build-with-claude/extended-thinking.md) section.

### Pricing

For complete pricing information including base rates, cache writes, cache hits, and output tokens, see the [pricing page](about-claude/pricing.md).

The thinking process incurs charges for:

- Tokens used during thinking (output tokens)
- Thinking blocks from the last assistant turn included in subsequent requests (input tokens)
- Standard text output tokens

When extended thinking is enabled, a specialized system prompt is automatically included to support this feature.

When using summarized thinking:

- **Input tokens**: Tokens in your original request (excludes thinking tokens from previous turns)
- **Output tokens (billed)**: The original thinking tokens that Claude generated internally
- **Output tokens (visible)**: The summarized thinking tokens you see in the response
- **No charge**: Tokens used to generate the summary

The billed output token count will **not** match the visible token count in the response. You are billed for the full thinking process, not the summary you see.

### Additional topics

The extended thinking page covers several topics in more detail with mode-specific code examples:

- **[Tool use with thinking](build-with-claude/extended-thinking.md)**: The same rules apply for adaptive thinking — preserve thinking blocks between tool calls and be aware of `tool_choice` limitations when thinking is active.
- **[Prompt caching](build-with-claude/extended-thinking.md)**: With adaptive thinking, consecutive requests using the same thinking mode preserve cache breakpoints. Switching between `adaptive` and `enabled`/`disabled` modes breaks cache breakpoints for messages (system prompts and tool definitions remain cached).
- **[Context windows](build-with-claude/extended-thinking.md)**: How thinking tokens interact with `max_tokens` and context window limits.

## Next steps

[Extended thinking

Learn more about extended thinking, including manual mode, tool use, and prompt caching.](build-with-claude/extended-thinking.md)[Effort parameter

Control how thoroughly Claude responds with the effort parameter.](build-with-claude/effort.md)

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
