##  Compare models

If you're unsure which model to use, start with [Claude Opus 5](models/opus-5/overview.md) for complex agentic coding and enterprise work; for the highest available capability, use [Claude Fable 5](models/fable-5/overview.md). All current models support text and image input, text output, multilingual capabilities, vision, and tool use; each model’s page lists the platforms it is available on.

| Feature | [Claude Fable 5](models/fable-5/overview.md)Next-generation intelligence for long-running agents | [Claude Opus 5](models/opus-5/overview.md)For complex agentic coding and enterprise work | [Claude Sonnet 5](models/sonnet-5/overview.md)The best combination of speed and intelligence | [Claude Haiku 4.5](models/haiku-4-5/overview.md)The fastest model with near-frontier intelligence |
| --- | --- | --- | --- | --- |
| Comparative latency | Slower | Moderate | Fast | Fastest |
| [Pricing](about-claude/pricing.md) | $10 / input MTok$50 / output MTok | $5 / input MTok$25 / output MTok | $2 / input MTok$10 / output MTok | $1 / input MTok$5 / output MTok |
| Claude API ID | claude-fable-5 | claude-opus-5 | claude-sonnet-5 | claude-haiku-4-5-20251001 |
| Capabilities |  | | | |
| [Thinking](build-with-claude/thinking.md) | Adaptive (always on) | Adaptive | Adaptive | Extended |
| [Default effort](build-with-claude/effort.md) | `high` | `high` | `high` | Not supported |
| [Context window](build-with-claude/context-windows.md) | 1M tokens | 1M tokens | 1M tokens | 200K tokens |
| Max output | 128K tokens | 128K tokens | 128K tokens | 64K tokens |
| Reliable knowledge cutoff | Jan 2026 | May 2026 | Jan 2026 | Feb 2025 |
| Show all detailsShow fewer details | | | | |

Once you've picked a model, [learn how to make your first API call](get-started.md). For how model IDs, aliases, and snapshots work, see [Model IDs and versioning](about-claude/models/model-ids-and-versions.md); for the reliable-knowledge and training-data cutoffs behind each model, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).

##  Using the Models API

You can query model capabilities and token limits programmatically with the [Models API](api/models/list.md). The response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.

##  Prompt and output performance

Current Claude models excel in:

- **Performance:** Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See [Prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md) for general and model-specific prompting guidance.
- **Engaging responses:** Claude models are ideal for applications that require rich, human-like interactions. If you prefer more concise responses, adjust your prompts to guide the model toward the desired output length. Refer to the [prompt engineering guides](build-with-claude/prompt-engineering.md) for details.
- **Output quality:** When migrating from a previous model generation, you may notice larger improvements in overall performance. If you're on Claude Opus 4.8 or earlier, see [Migrating to Claude Opus 5](about-claude/models/migration-guide.md).

##  Get started with Claude

If you're ready to start exploring what Claude can do for you, dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.



[Intro to Claude](intro.md)

Explore Claude's capabilities and development flow.



[Quickstart](get-started.md)

Learn how to make your first API call in minutes.

[Choosing a model](about-claude/models/choosing-a-model.md)

Establish criteria and pick the right model for your use case.

[Pricing](about-claude/pricing.md)

Complete pricing, including batch discounts and prompt caching rates.



[Model deprecations](about-claude/model-deprecations.md)

Lifecycle status and retirement commitments for every model.



[Claude Console](/)

Craft and test prompts directly in your browser.

Looking to chat with Claude? Visit [claude.ai](https://claude.ai). If you have questions, reach out to the [support team](https://support.claude.com/) or the [Discord community](https://www.anthropic.com/discord).

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
