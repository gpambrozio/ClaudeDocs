##  How it compares to the current lineup

| Model | Context | Max output | Price / MTok | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- |
| [Claude Fable 5](models/fable-5/overview.md) | 1M | 128K | $10 / $50 | Adaptive (always on) | `high` | Jan 2026 |
| [Claude Opus 5](models/opus-5/overview.md) | 1M | 128K | $5 / $25 | Adaptive | `high` | May 2026 |
| [Claude Sonnet 5](models/sonnet-5/overview.md) | 1M | 128K | $2 / $10 | Adaptive | `high` | Jan 2026 |
| Claude Sonnet 4.5This modelLegacy | 200K | 64K | $3 / $15 | Extended | — | Jan 2025 |
| [Claude Haiku 4.5](models/haiku-4-5/overview.md) | 200K | 64K | $1 / $5 | Extended | — | Feb 2025 |

##  Specifications

### Model IDs

Claude API
:   claude-sonnet-4-5-20250929

Claude API alias
:   claude-sonnet-4-5

[Amazon Bedrock (InvokeModel)](build-with-claude/claude-on-amazon-bedrock-legacy.md)
:   anthropic.claude-sonnet-4-5-20250929-v1:0

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)
:   claude-sonnet-4-5@20250929

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)
:   claude-sonnet-4-5

[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)
:   claude-sonnet-4-5

### Pricing

Input
:   $3 / MTok

Output
:   $15 / MTok

[5m cache write](build-with-claude/prompt-caching.md)
:   $3.75 / MTok

[1h cache write](build-with-claude/prompt-caching.md)
:   $6 / MTok

[Cache read](build-with-claude/prompt-caching.md)
:   $0.30 / MTok

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

Input → output
:   Text and images → text

Reliable knowledge cutoff
:   Jan 2025

Training data cutoff
:   Jul 2025

### Availability

[Status](about-claude/model-deprecations.md)
:   Active (legacy)

Released
:   September 29, 2025

Retirement
:   Not sooner than September 29, 2026

Platforms
:   Claude API[Amazon Bedrock (InvokeModel)](build-with-claude/claude-on-amazon-bedrock-legacy.md)[Google Cloud](build-with-claude/claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)

##  Resources

[Migrate to Claude Sonnet 5](about-claude/models/migration-guide.md)

What changes when moving from Claude Sonnet 4.5 and earlier Sonnet models to Claude Sonnet 5.



[Claude Sonnet 5](models/sonnet-5/overview.md)

The current Sonnet model: overview, specs, and resources.

##  Reference



[System prompt](release-notes/system-prompts.md)

The system prompt Claude Sonnet 4.5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-sonnet-4-5-system-card)

Safety evaluations and deployment decisions for Claude Sonnet 4.5.

[Pricing](about-claude/pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude/models/model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude/model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude/claude-on-amazon-bedrock-legacy.md)

Claude Sonnet 4.5 uses the InvokeModel Bedrock integration and Bedrock-style model IDs.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
