##  Overview

Claude Sonnet 5 is the next generation of Anthropic's Sonnet model family. It is a drop-in upgrade for Claude Sonnet 4.6 with three behavior changes: [adaptive thinking](build-with-claude/thinking.md) is on by default, manual extended thinking now returns a 400 error (it was deprecated on Claude Sonnet 4.6), and setting sampling parameters (`temperature`, `top_p`, `top_k`) to non-default values returns a 400 error. This page summarizes everything new at launch, including a new tokenizer.

[What's new in Claude Sonnet 5](models/sonnet-5/whats-new-sonnet-5.md)

##  How it compares

| Model | Context | Max output | Price / MTok | Latency | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Claude Fable 5](models/fable-5/overview.md) | 1M | 128K | $10 / $50 | Slower | Adaptive (always on) | `high` | Jan 2026 |
| [Claude Opus 5](models/opus-5/overview.md) | 1M | 128K | $5 / $25 | Moderate | Adaptive | `high` | May 2026 |
| Claude Sonnet 5This model | 1M | 128K | $2 / $10 | Fast | Adaptive | `high` | Jan 2026 |
| [Claude Haiku 4.5](models/haiku-4-5/overview.md) | 200K | 64K | $1 / $5 | Fastest | Extended | — | Feb 2025 |

##  Specifications

### Model IDs

Claude API
:   claude-sonnet-5

[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)
:   anthropic.claude-sonnet-5

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)
:   claude-sonnet-5

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)
:   claude-sonnet-5

[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)
:   claude-sonnet-5

### Pricing

Input
:   $2 / MTok

Output
:   $10 / MTok

[5m cache write](build-with-claude/prompt-caching.md)
:   $2.50 / MTok

[1h cache write](build-with-claude/prompt-caching.md)
:   $4 / MTok

[Cache read](build-with-claude/prompt-caching.md)
:   $0.20 / MTok

[Batch API](build-with-claude/batch-processing.md)
:   50% discount on input and output

Full price list
:   [Pricing](about-claude/pricing.md)

### Capabilities

[Context window](build-with-claude/context-windows.md)
:   1M tokens

Max output
:   128K tokens

[Max output (Batch API, beta)](build-with-claude/batch-processing.md)
:   300K tokens

[Thinking](build-with-claude/thinking.md)
:   Adaptive

[Default effort](build-with-claude/effort.md)
:   `high`

Comparative latency
:   Fast

Input → output
:   Text and images → text

Reliable knowledge cutoff
:   Jan 2026

Training data cutoff
:   Jan 2026

### Availability

[Status](about-claude/model-deprecations.md)
:   Active (latest)

Released
:   June 30, 2026

Retirement
:   Not sooner than June 30, 2027

Platforms
:   Claude API[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)[Google Cloud](build-with-claude/claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)

##  Good to know

- On the [Message Batches API](build-with-claude/batch-processing.md), Claude Sonnet 5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- Setting `temperature`, `top_p`, or `top_k` to non-default values returns a 400 error. See [What's new in Claude Sonnet 5](models/sonnet-5/whats-new-sonnet-5.md).
- Query limits and capabilities programmatically with the [Models API](api/models/list.md).

##  Resources



[Prompting Claude Sonnet 5](build-with-claude/prompt-engineering/prompting-claude-sonnet-5.md)

Model-specific prompting guidance.



[Adaptive thinking](build-with-claude/thinking.md)

On by default on Claude Sonnet 5. Steer depth with `effort`.



[Effort](build-with-claude/effort.md)

Effort defaults to `high` on the Claude API and Claude Code. Choose a level per workload.



[Context windows](build-with-claude/context-windows.md)

1M tokens by default. How the window is counted and managed.

##  Reference



[System card](https://www.anthropic.com/claude-sonnet-5-system-card)

Safety evaluations and deployment decisions for Claude Sonnet 5.

[Pricing](about-claude/pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude/models/model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude/model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
