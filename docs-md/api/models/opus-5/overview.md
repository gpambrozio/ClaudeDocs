##  Overview

Claude Opus 5 is a step-change improvement over Claude Opus 4.8, with the largest gains in deep reasoning, agentic and long-horizon tasks, and test-time compute scaling. This page summarizes everything new in Claude Opus 5, including mid-conversation tool changes and two breaking changes for code running on Claude Opus 4.8: thinking is on by default, and thinking can be disabled only at effort `high` or below.

[What's new in Claude Opus 5](models/opus-5/whats-new-opus-5.md)

##  How it compares

| Model | Context | Max output | Price / MTok | Latency | Thinking | Default effort | Knowledge cutoff |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Claude Fable 5](models/fable-5/overview.md) | 1M | 128K | $10 / $50 | Slower | Adaptive (always on) | `high` | Jan 2026 |
| Claude Opus 5This model | 1M | 128K | $5 / $25 | Moderate | Adaptive | `high` | May 2026 |
| [Claude Sonnet 5](models/sonnet-5/overview.md) | 1M | 128K | $2 / $10 | Fast | Adaptive | `high` | Jan 2026 |
| [Claude Haiku 4.5](models/haiku-4-5/overview.md) | 200K | 64K | $1 / $5 | Fastest | Extended | — | Feb 2025 |

##  Specifications

### Model IDs

Claude API
:   claude-opus-5

[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)
:   anthropic.claude-opus-5

[Google Cloud](build-with-claude/claude-on-vertex-ai.md)
:   claude-opus-5

[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)
:   claude-opus-5

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
:   Adaptive

[Default effort](build-with-claude/effort.md)
:   `high`

Comparative latency
:   Moderate

Input → output
:   Text and images → text

Reliable knowledge cutoff
:   May 2026

Training data cutoff
:   May 2026

### Availability

[Status](about-claude/model-deprecations.md)
:   Active (latest)

Released
:   July 24, 2026

Retirement
:   Not sooner than July 24, 2027

Platforms
:   Claude API[Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md)[Google Cloud](build-with-claude/claude-on-vertex-ai.md)[Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md)

##  Good to know

- On the [Message Batches API](build-with-claude/batch-processing.md), Claude Opus 5 supports up to 300k output tokens with the `output-300k-2026-03-24` beta header.
- The minimum cacheable prompt length is 512 tokens. See [Prompt caching](build-with-claude/prompt-caching.md).
- Query limits and capabilities programmatically with the [Models API](api/models/list.md).

##  Resources



[Prompting Claude Opus 5](build-with-claude/prompt-engineering/prompting-claude-opus-5.md)

Model-specific prompting guidance.



[Effort](build-with-claude/effort.md)

Effort defaults to `high` on Claude Opus 5 and matters more than on earlier models. Choose a level per workload.



[Adaptive thinking](build-with-claude/thinking.md)

On by default. Disabling thinking requires effort `high` or below.



[Fast mode](build-with-claude/fast-mode.md)

Lower-latency Claude Opus 5 on the Claude API (research preview), priced separately.

##  Reference



[System prompt](release-notes/system-prompts.md)

The system prompt Claude Opus 5 uses on claude.ai and the Claude apps.



[System card](https://www.anthropic.com/claude-opus-5-system-card)

Safety evaluations and deployment decisions for Claude Opus 5.

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
