# Extended thinking

Copy page





For how zero data retention (ZDR) applies to this feature, see [API and data retention](manage-claude/api-and-data-retention.md).



Extended thinking (`thinking.type: "enabled"` with `budget_tokens`) is deprecated on Claude Opus 4.6 and Claude Sonnet 4.6 (it still works there). Claude Opus 4.7, Claude Opus 4.8, Claude Sonnet 5, Claude Fable 5, and Claude Mythos 5 do not support it and reject requests that use it, returning a 400 error. On earlier models, including Claude Sonnet 4.5, Claude Opus 4.5, and Claude Haiku 4.5, extended thinking is the only thinking mode. Claude Mythos Preview supports both modes. Where both modes are available, use [adaptive thinking](build-with-claude/thinking-steering-and-cost.md) instead.

See [Migrating to adaptive thinking](#migrating-to-adaptive-thinking) to move to adaptive thinking. If your model supports only extended thinking, this page describes the supported configuration; no change is needed until you move to a newer model.



If a request fails with a 400 error whose message starts with `"thinking.type.enabled" is not supported`, your model uses adaptive thinking instead. See [Troubleshooting thinking](build-with-claude/thinking-troubleshooting.md), or jump to [Migrating to adaptive thinking](#migrating-to-adaptive-thinking).

Extended thinking in manual mode gives you direct control over how much Claude thinks. You set a thinking token budget on each request with `thinking: {type: "enabled", budget_tokens: N}`, and Claude thinks against that budget before it starts its final answer. Manual mode remains useful when your workload requires predictable latency or precise control over thinking costs. This page covers how to set and tune the budget, how manual mode interacts with interleaved thinking and prompt caching, and how to migrate to adaptive thinking.

For how thinking itself works, including thinking blocks and the response shape, the `display` parameter, streaming, thinking with tool use, and encryption, see the [thinking overview](build-with-claude/thinking.md).

##  Supported models

Extended thinking availability per model, including the models where extended thinking is the only mode, is listed in the [per-model configuration table](build-with-claude/thinking-troubleshooting.md).

##  How to use extended thinking

Here is an example of using extended thinking in the Messages API:

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[
        {
            "role": "user",
            "content": "Are there an infinite number of prime numbers such that n mod 4 == 3?",
        }
    ],
)

# The response contains summarized thinking blocks and text blocks
for block in response.content:
    match block.type:
        case "thinking":
            print(f"\nThinking summary: {block.thinking}")
        case "text":
            print(f"\nResponse: {block.text}")
```

To turn on manual extended thinking, add a `thinking` object with `type` set to `enabled` and a `budget_tokens` value.

The `budget_tokens` parameter sets a target for how many tokens Claude can use for its internal reasoning process. Larger budgets can improve response quality by enabling more thorough analysis for complex problems.

##  Budget rules and tuning

`budget_tokens` must satisfy these constraints:

- **Minimum of 1,024 tokens.** The API rejects smaller values.
- **Less than `max_tokens`.** Thinking tokens count toward the `max_tokens` limit for the turn, so the budget must leave room for the final response. The one exception is [interleaved thinking](#interleaved-thinking), where `budget_tokens` can exceed `max_tokens` because the budget spans all thinking blocks within one assistant turn.
- **No cache pre-warming.** Because `budget_tokens` must be less than `max_tokens`, extended thinking cannot be combined with `max_tokens: 0` ([cache pre-warming](build-with-claude/prompt-caching.md)).

The budget is a target rather than a strict cap. Actual token usage varies with the task, and Claude may stop reasoning well before the budget is exhausted; `max_tokens` remains the hard ceiling on total output.

On Claude Opus 4.5, the only extended-thinking-only model that supports [effort](build-with-claude/effort.md), effort shapes the overall response while `budget_tokens` sets thinking depth; set both.

To tune the budget:

- Match the starting point to the task. For simple tasks, start near the 1,024-token minimum and increase incrementally to find the optimal range for your use case. For complex tasks, start with a larger budget of 16,000 tokens or more and adjust to your latency and quality needs. Higher budgets enable more comprehensive reasoning, with diminishing returns that depend on the task, and at the cost of increased latency. For critical tasks, test different settings to find the right balance.
- For thinking budgets above 32k, use [batch processing](build-with-claude/batch-processing.md) to avoid networking issues. Pushing the model to think beyond 32k tokens produces long-running requests that can hit system timeouts and open-connection limits.

To track what a budget actually costs you, monitor the `usage.output_tokens_details.thinking_tokens` field in the response, which reports how many of the billed output tokens were internal reasoning. When streaming, this breakdown appears only on the final `message_delta` event.

When you are ready to move off manual budgets, see [Migrating to adaptive thinking](#migrating-to-adaptive-thinking).

##  Interleaved thinking in manual mode

Interleaved thinking lets Claude think between tool calls within a single assistant turn, reasoning about each tool result before deciding what to do next. For the concept, the turn structure, and how it behaves on adaptive-thinking models, see [interleaved thinking](build-with-claude/thinking.md) in the thinking overview. This section covers how to enable it when you use manual `type: "enabled"` thinking.

On Claude Opus 4.5, Claude Sonnet 4.5, and earlier Claude 4 models (Claude Opus 4.1 (deprecated), Claude Opus 4, and Claude Sonnet 4), add the `interleaved-thinking-2025-05-14` [beta header](api/beta-headers.md) to your API request.

The 4.6 generation splits in manual mode:

- **Claude Sonnet 4.6**: the beta header with manual `type: "enabled"` is still functional but deprecated. Prefer [adaptive thinking](build-with-claude/thinking-steering-and-cost.md), which interleaves automatically with no header.
- **Claude Opus 4.6**: manual mode has no interleaved thinking at all. Only its adaptive mode interleaves, so switch to `thinking: {type: "adaptive"}` if you need reasoning between tool calls on this model.

Claude Haiku 4.5 does not support interleaved thinking. On the Claude API, the beta header is accepted but ignored.

Two more considerations for interleaved thinking in manual mode:

- `budget_tokens` can exceed `max_tokens` here; the [budget rules](#budget-rules-and-tuning) explain this exception.
- Interleaved thinking is only supported for [tools used through the Messages API](agents-and-tools/tool-use/overview.md).

How platforms treat the beta header differs. The Claude API and [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md) accept `interleaved-thinking-2025-05-14` on any model and ignore it where unsupported. Acceptance is not the same as effect: on models that reject `type: "enabled"` (4.7 and later) or lack manual-mode interleaving (Claude Opus 4.6), the header has no manual-mode effect; adaptive thinking interleaves automatically there.

Partner-operated platforms ([Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md) and [Google Cloud](build-with-claude/claude-on-vertex-ai.md)) reject the request unless the model is one of the following:

- Claude Opus 4.8, Claude Opus 4.7, Claude Sonnet 5
- Claude Opus 4.6, Claude Sonnet 4.6, Claude Opus 4.5, Claude Sonnet 4.5, Claude Opus 4.1 (deprecated)
- Claude Opus 4 ([retired, except on Google Cloud](about-claude/model-deprecations.md)) and Claude Sonnet 4 ([retired, except on Bedrock and Google Cloud](about-claude/model-deprecations.md))

##  Turn structure in manual mode

The general turn-structure rules, including the single-turn tool-use loop, mid-turn conflict handling, and toggling thinking between turns, are on [Thinking with tool use](build-with-claude/thinking.md).

Manual mode adds one requirement: the final assistant turn of a thinking-enabled request must begin with a thinking block ([adaptive thinking](build-with-claude/thinking-steering-and-cost.md) drops that requirement). Changing the thinking configuration between turns also invalidates prompt caching; see the following section.

##  Prompt caching in manual mode

Manual mode adds one rule on top of the mode-neutral caching behavior described in [thinking and prompt caching](build-with-claude/thinking.md): changing `budget_tokens` between requests invalidates cache breakpoints, just as switching thinking modes does, because the budget value is rendered into the prompt. Message-level breakpoints always miss after a budget change; whether tool and system-prompt breakpoints miss too depends on where the model renders the configuration.

In practice, pick a budget and hold it stable for the life of a cached conversation. Running a multi-turn conversation with message-level caching on Claude Sonnet 4.6 and changing the budget on the third request from 4,000 to 8,000 tokens shows the invalidation directly:

Output



```block
First request - establishing cache
First response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 17, output_tokens: 700 }

Second request - same thinking parameters (cache hit expected)
Second response usage: { cache_creation_input_tokens: 0, cache_read_input_tokens: 1370, input_tokens: 303, output_tokens: 874 }

Third request - different thinking budget (cache miss expected)
Third response usage: { cache_creation_input_tokens: 1370, cache_read_input_tokens: 0, input_tokens: 747, output_tokens: 619 }
```

The third request re-creates the cache (`cache_creation_input_tokens=1370`, `cache_read_input_tokens=0`) because the budget changed between requests. For a runnable version of the same experiment in adaptive mode, where the effort level plays the cache role that `budget_tokens` plays here, see [Prompt caching](build-with-claude/thinking-steering-and-cost.md) on the steering page.

##  Shared mechanics

Most thinking behavior is mode neutral and documented once on the [Thinking](build-with-claude/thinking.md) page. Everything there applies in manual mode too:

- [Controlling thinking display](build-with-claude/thinking.md)
- [Streaming thinking](build-with-claude/thinking.md)
- [Thinking with tool use](build-with-claude/thinking.md), including [preserving thinking blocks](build-with-claude/thinking.md)
- [Thinking and prompt caching](build-with-claude/thinking.md)
- [Thinking and the context window](build-with-claude/thinking.md)
- [Thinking encryption](build-with-claude/thinking.md)
- [Pricing](build-with-claude/thinking-steering-and-cost.md) (on the [Steering thinking](build-with-claude/thinking-steering-and-cost.md) page)

##  Migrating to adaptive thinking

If your model supports only extended thinking (Claude Sonnet 4.5, Claude Opus 4.5, Claude Haiku 4.5, and earlier Claude 4 models), no action is needed now: adaptive thinking is not available there, and `type: "adaptive"` [returns a 400 error](build-with-claude/thinking-troubleshooting.md). Keep `budget_tokens` until you move to a model that supports adaptive thinking, then apply the mapping that follows.

You need to migrate off `type: "enabled"` if:

- You use Claude Opus 4.6 or Claude Sonnet 4.6, where `budget_tokens` is deprecated and will be removed in a future model release.
- You are moving to Claude Opus 4.7, Claude Opus 4.8, Claude Sonnet 5, Claude Fable 5, or Claude Mythos 5, where `type: "enabled"` returns a 400 error.

The mapping is small: remove `budget_tokens`, set `thinking: {type: "adaptive"}`, and control reasoning depth with `output_config: {effort: ...}` instead of a token budget.

```shiki
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 16000,
  "thinking": {
    "type": "enabled",
    "budget_tokens": 10000
  }
}
```



becomes:

```shiki
{
  "model": "claude-sonnet-4-6",
  "max_tokens": 16000,
  "thinking": {
    "type": "adaptive"
  },
  "output_config": {
    "effort": "high"
  }
}
```



`effort: "high"` matches the API default; it appears here only to show where the depth control now lives, and omitting it produces identical behavior.

Expect a behavioral difference, not just a syntax change. With a fixed budget, Claude thinks on every request. With adaptive thinking, Claude decides whether and how much to think on each request, and at lower [effort](build-with-claude/effort.md) settings it may skip thinking entirely on easy inputs. You can also remove the `interleaved-thinking-2025-05-14` beta header after migrating: adaptive thinking interleaves automatically, and the Claude API ignores the header on these models. Thinking block preservation changes too: Claude Opus 4.5 and models numbered 4.6 and higher keep prior turns' thinking blocks in context and bill them as input, where Claude Sonnet 4.5, Claude Haiku 4.5, and earlier models stripped them; see [thinking block preservation by model](build-with-claude/thinking.md).

Switching modes is a thinking-configuration change, so the first request after the switch invalidates cache breakpoints, as described in [Prompt caching in manual mode](#extended-thinking-with-prompt-caching).

For full guidance, see [adaptive thinking](build-with-claude/thinking-steering-and-cost.md), [effort](build-with-claude/effort.md), and the [model migration guide](about-claude/models/migration-guide.md).

##  Next steps

[Thinking

Learn how thinking works: blocks, display, streaming, and tool use.](build-with-claude/thinking.md)[Steering thinking

Let Claude decide when and how much to think on each request.](build-with-claude/thinking-steering-and-cost.md)[

Thinking in tool and multi-turn workflows

Preserve thinking blocks and manage thinking across tool calls and turns.](build-with-claude/thinking-tool-workflows.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
