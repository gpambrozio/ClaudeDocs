##  How it compares

| Model | Context | Max output | Price / MTok | Latency | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Claude Fable 5](models/fable-5/overview.md) | 1M | 128K | $10 / $50 | Slower | Adaptive (always on) | `high` | Jan 2026 |
| [Claude Opus 5](models/opus-5/overview.md) | 1M | 128K | $5 / $25 | Moderate | Adaptive | `high` | May 2026 |
| [Claude Sonnet 5](models/sonnet-5/overview.md) | 1M | 128K | $2 / $10 | Fast | Adaptive | `high` | Jan 2026 |
| Claude Haiku 4.5This model | 200K | 64K | $1 / $5 | Fastest | Extended | — | Feb 2025 |

##  Specifications

### Model IDs

Claude API
:   claude-haiku-4-5-20251001

Claude API alias
:   claude-haiku-4-5

[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)
:   anthropic.claude-haiku-4-5

[Amazon Bedrock (InvokeModel)](build-with-claude/claude-on-amazon-bedrock-legacy.md)
:   anthropic.claude-haiku-4-5-20251001-v1:0

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)
:   claude-haiku-4-5@20251001

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)
:   claude-haiku-4-5

[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)
:   claude-haiku-4-5

### Pricing

Input
:   $1 / MTok

Output
:   $5 / MTok

[5m cache write](build-with-claude/prompt-caching.md)
:   $1.25 / MTok

[1h cache write](build-with-claude/prompt-caching.md)
:   $2 / MTok

[Cache read](build-with-claude/prompt-caching.md)
:   $0.10 / MTok

[Batch API](build-with-claude/batch-processing.md)
:   50% discount on input and output

Full price list
:   [Pricing](about-claude/pricing.md)

### Capabilities

[Context window](build-with-claude/context-windows.md)
:   200K tokens

Max output
:   64K tokens

[Thinking](build-with-claude/thinking.md)
:   Extended

[Default effort](build-with-claude/effort.md)
:   Not supported

Comparative latency
:   Fastest

Input → output
:   Text and images → text

Reliable knowledge cutoff
:   Feb 2025

Training data cutoff
:   Jul 2025

### Availability

[Status](about-claude/model-deprecations.md)
:   Active (latest)

Released
:   October 15, 2025

Retirement
:   Not sooner than October 15, 2026

Platforms
:   Claude API[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)[Amazon Bedrock (InvokeModel)](build-with-claude/claude-on-amazon-bedrock-legacy.md)[Google Cloud](build-with-claude/claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)

##  Good to know

- `claude-haiku-4-5` is a convenience alias that resolves to the pinned snapshot `claude-haiku-4-5-20251001`. See [Model IDs and versioning](about-claude/models/model-ids-and-versions.md).
- Claude Haiku 4.5 uses manual extended thinking (`thinking.type: "enabled"`), not adaptive thinking.
- Query limits and capabilities programmatically with the [Models API](api/models/list.md).

##  Resources



[Extended thinking](build-with-claude/extended-thinking.md)

Claude Haiku 4.5 supports manual extended thinking with `budget_tokens`.



[Choosing a model](about-claude/models/choosing-a-model.md)

When to start efficiency-first with Haiku and when to reach for a larger model.



[Reduce latency](test-and-evaluate/strengthen-guardrails/reduce-latency.md)

Techniques that pair well with the fastest model in the lineup.

##  Reference



[System prompt](release-notes/system-prompts.md)

The system prompt Claude Haiku 4.5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-haiku-4-5-system-card)

Safety evaluations and deployment decisions for Claude Haiku 4.5.

[Pricing](about-claude/pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude/models/model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude/model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude/claude-on-amazon-bedrock-legacy.md)

Claude Haiku 4.5 is also available through the InvokeModel Bedrock integration and Bedrock-style model IDs.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
