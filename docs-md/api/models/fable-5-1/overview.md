## Overview

Claude Fable 5.1 extends Claude Fable 5 at the same input and output prices, with cache reads at a quarter of the cost, and brings stronger long-running agentic coding, multistep research, and document, spreadsheet, and slide work. For most workloads, start with Claude Opus 5 (see [Choosing a model](about-claude/models/choosing-a-model.md)). Use Claude Fable 5.1 for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short. Claude Mythos 5.1 offers the same capabilities to [Project Glasswing](https://anthropic.com/glasswing) participants only.

If you already call Claude Fable 5, three changes are breaking: [forced tool use returns an error](models/fable-5-1/whats-new-fable-5-1.md), [earlier models can't read its thinking blocks](models/fable-5-1/whats-new-fable-5-1.md), and [editing earlier turns invalidates thinking blocks](models/fable-5-1/whats-new-fable-5-1.md). Five are additive: [per-message effort](models/fable-5-1/whats-new-fable-5-1.md) (beta), [turn-scoped system messages](models/fable-5-1/whats-new-fable-5-1.md) (beta), [readable progress updates between tool calls](models/fable-5-1/whats-new-fable-5-1.md) (`display: "updates"`, beta), a [lower cache read price](models/fable-5-1/whats-new-fable-5-1.md), and [content provenance](models/fable-5-1/whats-new-fable-5-1.md).

[What's new in Claude Fable 5.1](models/fable-5-1/whats-new-fable-5-1.md)

## Claude Fable 5.1 and Claude Mythos 5.1

[Claude Mythos 5.1](models/mythos-5-1/overview.md) offers the same capabilities by invitation only, as part of [Project Glasswing](https://anthropic.com/glasswing). It shares Claude Fable 5.1's specifications and pricing. For access, contact your Anthropic, AWS, or Google Cloud account team.

## How it compares

| Model | Context | Max output | Price / MTok | Latency | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Fable 5.1This model | 1M | 128K | $10 / $50 | Slower | Adaptive (always on) | `high` | Jun 2026 |
| [Claude Opus 5](models/opus-5/overview.md) | 1M | 128K | $5 / $25 | Moderate | Adaptive | `high` | May 2026 |
| [Claude Sonnet 5](models/sonnet-5/overview.md) | 1M | 128K | $2 / $10 | Fast | Adaptive | `high` | Jan 2026 |
| [Claude Haiku 4.5](models/haiku-4-5/overview.md) | 200K | 64K | $1 / $5 | Fastest | Extended | — | Feb 2025 |

## Specifications

### Model IDs

Claude API
:   claude-fable-5-1

[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)
:   anthropic.claude-fable-5-1

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)
:   claude-fable-5-1

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)
:   claude-fable-5-1

[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)
:   claude-fable-5-1

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
:   Active (latest)

Released
:   September 1, 2026

Retirement
:   Not sooner than September 1, 2027

Platforms
:   Claude API[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)[Google Cloud](build-with-claude/claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)[Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md)

## Resources



[Prompting Claude Fable 5.1](build-with-claude/prompt-engineering/prompting-claude-fable-5-1.md)

Model-specific prompting guidance for long-horizon and agentic work.



[Migrating to Claude Fable 5.1](models/fable-5-1/migration-guide.md)

What changes when you move from Claude Fable 5, Claude Opus 5, or Claude Opus 4.8.



[Preserved thinking](build-with-claude/thinking.md)

When this model's thinking blocks stay usable: across model switches and across changes to the conversation.



[Per-message effort](build-with-claude/effort.md)

Change the effort level partway through a conversation without invalidating the prompt cache.



[Refusals and fallback](build-with-claude/refusals-and-fallback.md)

Handle classifier refusals and retry on another Claude model.



[Adaptive thinking](build-with-claude/thinking.md)

The only thinking mode on Claude Fable 5.1. Steer depth with `effort`.

## Reference



[System prompt](release-notes/system-prompts/claude-fable-5-1.md)

The system prompt Claude Fable 5.1 uses on claude.ai and the Claude apps.

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
