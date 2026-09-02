## Fable vs. Mythos

[Claude Mythos 5](models/mythos-5/overview.md) is offered separately, by invitation only, for defensive cybersecurity workflows as part of [Project Glasswing](https://anthropic.com/glasswing). It shares Claude Fable 5's specifications and pricing; Claude Fable 5 includes safety classifiers that can decline requests, and Claude Mythos 5 does not. For access, contact your Anthropic, AWS, or Google Cloud account team.

## How it compares to the current lineup

| Model | Context | Max output | Price / MTok | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- |
| [Claude Fable 5.1](models/fable-5-1/overview.md) | 1M | 128K | $10 / $50 | Adaptive (always on) | `high` | Jun 2026 |
| Claude Fable 5This modelLegacy | 1M | 128K | $10 / $50 | Adaptive (always on) | `high` | Jan 2026 |
| [Claude Opus 5](models/opus-5/overview.md) | 1M | 128K | $5 / $25 | Adaptive | `high` | May 2026 |
| [Claude Sonnet 5](models/sonnet-5/overview.md) | 1M | 128K | $2 / $10 | Adaptive | `high` | Jan 2026 |
| [Claude Haiku 4.5](models/haiku-4-5/overview.md) | 200K | 64K | $1 / $5 | Extended | — | Feb 2025 |

## Specifications

### Model IDs

Claude API
:   claude-fable-5

[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)
:   anthropic.claude-fable-5

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)
:   claude-fable-5

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)
:   claude-fable-5

[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)
:   claude-fable-5

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
:   $1 / MTok

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

Input → output
:   Text and images → text

Reliable knowledge cutoff
:   Jan 2026

Training data cutoff
:   Jan 2026

### Availability

[Status](about-claude/model-deprecations.md)
:   Active (legacy)

Released
:   June 9, 2026

Retirement
:   Not sooner than June 9, 2027

Platforms
:   Claude API[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)[Google Cloud](build-with-claude/claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)

## Resources

[Migrate to Claude Fable 5.1](models/fable-5-1/migration-guide.md)

What changes when moving from Claude Fable 5 to Claude Fable 5.1.



[Claude Fable 5.1](models/fable-5-1/overview.md)

The current Fable model: overview, specs, and resources.



[Introducing Claude Fable 5 and Claude Mythos 5](models/fable-5/introducing-claude-fable-5-and-claude-mythos-5.md)

Capabilities, API changes, and availability for Claude Fable 5.



[Prompting Claude Fable 5](build-with-claude/prompt-engineering/prompting-claude-fable-5.md)

Model-specific prompting guidance for long-horizon and agentic work.



[Refusals and fallback](build-with-claude/refusals-and-fallback.md)

Handle classifier refusals and retry on another Claude model with the `fallbacks` parameter.

## Reference



[System prompt](release-notes/system-prompts.md)

The system prompt Claude Fable 5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-fable-5-mythos-5-system-card)

Safety evaluations and deployment decisions for Claude Fable 5 and Claude Mythos 5.

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
