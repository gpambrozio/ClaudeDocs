# Claude Mythos 5.1Invite only



Claude Mythos 5.1 is offered separately, by invitation only, as part of Project Glasswing. It shares Claude Fable 5.1’s specifications and pricing. For access, contact your Anthropic, AWS, or Google Cloud account team.

[See Claude Fable 5.1](models/fable-5-1/overview.md)

## How it compares

| Model | Context | Max output | Price / MTok | Latency | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Claude Fable 5.1](models/fable-5-1/overview.md) | 1M | 128K | $10 / $50 | Slower | Adaptive (always on) | `high` | Jun 2026 |
| Claude Mythos 5.1This model | 1M | 128K | $10 / $50 | Slower | Adaptive (always on) | `high` | Jun 2026 |
| [Claude Opus 5](models/opus-5/overview.md) | 1M | 128K | $5 / $25 | Moderate | Adaptive | `high` | May 2026 |
| [Claude Sonnet 5](models/sonnet-5/overview.md) | 1M | 128K | $2 / $10 | Fast | Adaptive | `high` | Jan 2026 |
| [Claude Haiku 4.5](models/haiku-4-5/overview.md) | 200K | 64K | $1 / $5 | Fastest | Extended | — | Feb 2025 |

## Specifications

### Model IDs

Claude API
:   claude-mythos-5-1

[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)
:   anthropic.claude-mythos-5-1

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)
:   claude-mythos-5-1

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)
:   claude-mythos-5-1

### Pricing

Input
:   $10 / MTok

Output
:   $50 / MTok

[5m cache write](build-with-claude/prompt-caching.md)
:   $12.50 / MTok

[1h cache write](build-with-claude/prompt-caching.md)
:   $20 / MTok

[Cache read](build-with-claude/prompt-caching.md)
:   $0.25 / MTok

[Batch API](build-with-claude/batch-processing.md)
:   50% discount on input and output

Full price list
:   [Pricing](about-claude/pricing.md)

### Capabilities

[Context window](build-with-claude/context-windows.md)
:   1M tokens

Max output
:   128K tokens

[Thinking](build-with-claude/thinking.md)
:   Adaptive (always on)

[Default effort](build-with-claude/effort.md)
:   `high`

Comparative latency
:   Slower

Input → output
:   Text and images → text

Reliable knowledge cutoff
:   Jun 2026

Training data cutoff
:   Jun 2026

### Availability

[Status](about-claude/model-deprecations.md)
:   Active (invite only)

Released
:   September 1, 2026

Retirement
:   Not sooner than September 1, 2027

Platforms
:   Claude API[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)[Google Cloud](build-with-claude/claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)

## Reference



[Migrating from Claude Mythos 5](models/fable-5-1/migration-guide.md)

What changes when you move from Claude Mythos 5.



[System card](https://www.anthropic.com/claude-fable-5-1-mythos-5-1-system-card)

Safety evaluations and deployment decisions for Claude Fable 5.1 and Claude Mythos 5.1.

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
