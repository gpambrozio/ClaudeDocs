# What's new in Claude Sonnet 5

Copy page



Claude Sonnet 5 is the next generation of Anthropic's Sonnet model family. It is a drop-in upgrade for Claude Sonnet 4.6 with three behavior changes: [adaptive thinking](build-with-claude/adaptive-thinking.md) is on by default, manual extended thinking now returns a 400 error (it was deprecated on Claude Sonnet 4.6), and setting sampling parameters (`temperature`, `top_p`, `top_k`) to non-default values returns a 400 error. This page summarizes everything new at launch, including a new tokenizer.

##  New model

| Model | API model ID | Description |
| --- | --- | --- |
| Claude Sonnet 5 | `claude-sonnet-5` | The best combination of speed and intelligence |

Claude Sonnet 5 supports the [1M token context window](build-with-claude/context-windows.md) by default (1M tokens is both the default and the maximum; there is no smaller context variant), 128k max output tokens, [adaptive thinking](build-with-claude/adaptive-thinking.md), and the same set of tools and platform features as Claude Sonnet 4.6, except [Priority Tier](api/service-tiers.md), which is not available on Claude Sonnet 5.

For complete pricing and specs, see the [models overview](about-claude/models/overview.md).

##  Behavior changes

###  Adaptive thinking on by default

On Claude Sonnet 4.6, requests without a `thinking` field run without thinking. On Claude Sonnet 5, the same requests run with [adaptive thinking](build-with-claude/adaptive-thinking.md). To turn thinking off, pass `thinking: {type: "disabled"}`. Because `max_tokens` is a hard limit on total output (thinking plus response text), revisit it for workloads that ran without thinking on Claude Sonnet 4.6.

###  Sampling parameters not accepted

Setting `temperature`, `top_p`, or `top_k` to a non-default value returns a 400 error. Remove these parameters when migrating; the default value (or omitting the parameter) is accepted. Use system-prompt instructions to guide model behavior. This is new for Sonnet-class models; the same constraint was previously introduced on Claude Opus 4.7.

###  Manual extended thinking removed

Manual extended thinking (`thinking: {type: "enabled", budget_tokens: N}`) was deprecated on Claude Sonnet 4.6; on Claude Sonnet 5 it is removed and returns a 400 error, the same as on Claude Opus 4.8 and Claude Opus 4.7. Use adaptive thinking with the [effort parameter](build-with-claude/effort.md) instead.

Python



```shiki
# Not supported on Claude Sonnet 5 (returns 400)
thinking = {"type": "enabled", "budget_tokens": 32000}

# Use this instead
thinking = {"type": "adaptive"}
```

##  New tokenizer

Claude Sonnet 5 uses a new tokenizer. The same input text produces approximately 30% more tokens than on Claude Sonnet 4.6. The exact increase depends on the content. This is not an API change: requests, responses, and streaming events keep the same shape, and no code changes are required.

The change affects anything you measure or budget in tokens:

- **Token counts:** `usage` fields and [token counting](build-with-claude/token-counting.md) results for the same text are higher than on Claude Sonnet 4.6. Don't reuse counts measured against earlier models; recount against Claude Sonnet 5.
- **Context window capacity in text terms:** the context window is 1M tokens, but each token covers less text on average, so the same window holds less text than on Claude Sonnet 4.6.
- **`max_tokens` budgets:** an output limit tuned for Claude Sonnet 4.6 may truncate equivalent output on Claude Sonnet 5. Revisit limits sized close to your expected output length.
- **Per-request cost:** per-token pricing is unchanged (see [Pricing](#pricing)), but because the same text produces more tokens, the cost of an equivalent request can differ from Claude Sonnet 4.6.

##  API constraints inherited from Claude Sonnet 4.6



This constraint is unchanged from Claude Sonnet 4.6. Aside from the three [behavior changes](#behavior-changes) (see [Migration guide](#migration-guide)), code that already runs on Claude Sonnet 4.6 needs no other changes.

###  Assistant message prefilling not supported

Prefilling the assistant message returns a `400` error, unchanged from Claude Sonnet 4.6. Use [structured outputs](build-with-claude/structured-outputs.md), system prompt instructions, or `output_config.format` instead.

##  Capability improvements

Claude Sonnet 5 is a capability upgrade over Claude Sonnet 4.6 at the same price. It is also an option for workloads that need more capability than Claude Sonnet 4.6 provides without moving to an Opus-class model.

The largest gains over Claude Sonnet 4.6 are in coding and agentic tasks. For benchmark results, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).

##  Cybersecurity safeguards

Claude Sonnet 5 is the first Sonnet-tier model with real-time cybersecurity safeguards. Requests that involve prohibited or high-risk cybersecurity topics may be refused. Refusals return as a successful HTTP 200 response with `stop_reason: "refusal"`, not an error. See [Safeguards, warnings, and appeals](https://support.claude.com/en/articles/8241253-safeguards-warnings-and-appeals) for background.

##  Pricing

Claude Sonnet 5 is priced at $3 per million input tokens and $15 per million output tokens, unchanged from Claude Sonnet 4.6. Because the [new tokenizer](#new-tokenizer) produces approximately 30% more tokens for the same text, the cost of an equivalent request can differ from Claude Sonnet 4.6 even though per-token pricing is unchanged. The exact increase depends on the content and workload shape.

Introductory pricing of $2/$10 per million input/output tokens is in effect through August 31, 2026, after which the standard pricing of $3/$15 per million input/output tokens will take effect.

See [Pricing](about-claude/pricing.md) for complete pricing, including batch processing and prompt caching rates.

##  Availability

At launch, Claude Sonnet 5 is available on:

- **Claude API:** available to all customers.
- **AWS:** available through [Claude in Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md) and [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md). On Amazon Bedrock, Claude Sonnet 5 is also reachable through the `InvokeModel` API, served by the same infrastructure as Claude in Amazon Bedrock. The legacy [Claude on Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude/claude-on-amazon-bedrock-legacy.md) integration does not include Claude Sonnet 5.
- **Google Cloud:** available through [Claude on Google Cloud](build-with-claude/claude-on-vertex-ai.md).
- **Microsoft Foundry:** available through [Claude in Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md).

Claude Sonnet 5 supports [zero data retention](manage-claude/api-and-data-retention.md) for organizations with ZDR agreements.

##  Migration guide

Claude Sonnet 5 is a drop-in replacement for Claude Sonnet 4.6. Update your model ID:

```shiki
model = "claude-sonnet-4-6"  # Before
model = "claude-sonnet-5"  # After
```



Then review the following:

1. **Token budgets and counts:** the [new tokenizer](#new-tokenizer) produces approximately 30% more tokens for the same text. The exact increase depends on the content and workload shape. Recount prompts with [token counting](build-with-claude/token-counting.md), and revisit `max_tokens` limits sized close to your expected output length.
2. **Extended thinking:** if you still set `budget_tokens`, migrate to [adaptive thinking](build-with-claude/adaptive-thinking.md). Manual extended thinking (`thinking: {type: "enabled"}`) is not supported and returns a 400 error.
3. **Sampling parameters:** requests that set sampling parameters (`temperature`, `top_p`, `top_k`) to a non-default value return a 400 error; remove them when migrating. Tool definitions and response shapes are unchanged, and assistant message prefilling was already unsupported on Claude Sonnet 4.6.

See the [Claude Sonnet 5 section of the migration guide](about-claude/models/migration-guide.md) for details.

##  Next steps

[

Models overview

Complete specs and pricing for all current Claude models.](about-claude/models/overview.md)[Token counting

Measure your prompts under the new tokenizer before you migrate.](build-with-claude/token-counting.md)[Adaptive thinking

The recommended thinking-on mode on Claude Sonnet 5.](build-with-claude/adaptive-thinking.md)[Context windows

How the 1M token context window works.](build-with-claude/context-windows.md)[Pricing

Complete pricing, including batch processing and prompt caching rates.](about-claude/pricing.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
