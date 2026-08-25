##  How it compares to the current lineup

| Model | Context | Max output | Price / MTok | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- |
| [Claude Fable 5](models/fable-5/overview.md) | 1M | 128K | $10 / $50 | Adaptive (always on) | `high` | Jan 2026 |
| [Claude Opus 5](models/opus-5/overview.md) | 1M | 128K | $5 / $25 | Adaptive | `high` | May 2026 |
| Claude Opus 4.6This modelLegacy | 1M | 128K | $5 / $25 | Adaptive (extended deprecated) | `high` | May 2025 |
| [Claude Sonnet 5](models/sonnet-5/overview.md) | 1M | 128K | $2 / $10 | Adaptive | `high` | Jan 2026 |
| [Claude Haiku 4.5](models/haiku-4-5/overview.md) | 200K | 64K | $1 / $5 | Extended | — | Feb 2025 |

##  Specifications

### Model IDs

Claude API
:   claude-opus-4-6

[Amazon Bedrock (InvokeModel)](build-with-claude/claude-on-amazon-bedrock-legacy.md)
:   anthropic.claude-opus-4-6-v1

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)
:   claude-opus-4-6

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)
:   claude-opus-4-6

[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)
:   claude-opus-4-6

### Pricing

Input
:   $5 / MTok

Output
:   $25 / MTok

[5m cache write](build-with-claude/prompt-caching.md)
:   $6.25 / MTok

[1h cache write](build-with-claude/prompt-caching.md)
:   $10 / MTok

[Cache read](build-with-claude/prompt-caching.md)
:   $0.50 / MTok

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
:   Adaptive (extended deprecated)

[Default effort](build-with-claude/effort.md)
:   `high`

Input → output
:   Text and images → text

Reliable knowledge cutoff
:   May 2025

Training data cutoff
:   Aug 2025

### Availability

[Status](about-claude/model-deprecations.md)
:   Active (legacy)

Released
:   February 5, 2026

Retirement
:   Not sooner than February 5, 2027

Platforms
:   Claude API[Amazon Bedrock (InvokeModel)](build-with-claude/claude-on-amazon-bedrock-legacy.md)[Google Cloud](build-with-claude/claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)

##  Resources

[Migrate to Claude Opus 5](about-claude/models/migration-guide.md)

What changes when moving from Claude Opus 4.6 and earlier Opus models to Claude Opus 5.



[Claude Opus 5](models/opus-5/overview.md)

The current Opus model: overview, specs, and resources.

##  Reference



[System prompt](release-notes/system-prompts.md)

The system prompt Claude Opus 4.6 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-opus-4-6-system-card)

Safety evaluations and deployment decisions for Claude Opus 4.6.

[Pricing](about-claude/pricing.md)

Full price list, including batch discounts and prompt caching rates.

[Model IDs and versioning](about-claude/models/model-ids-and-versions.md)

How model IDs, aliases, and pinned snapshots work.



[Model deprecations](about-claude/model-deprecations.md)

Lifecycle status and retirement commitments for every Claude model.



[Amazon Bedrock (Opus 4.6 and earlier)](build-with-claude/claude-on-amazon-bedrock-legacy.md)

Claude Opus 4.6 uses the InvokeModel Bedrock integration and Bedrock-style model IDs.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
