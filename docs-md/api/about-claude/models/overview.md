# Models overview

Copy page

## Choosing a model

If you're unsure which model to use, we recommend starting with **Claude Opus 4.6** for the most complex tasks. It is our latest generation model with exceptional performance in coding and reasoning.

All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available via the Anthropic API, AWS Bedrock, and Google Vertex AI.

Once you've picked a model, [learn how to make your first API call](get-started.md).

### Latest models comparison

| Feature | Claude Opus 4.6 | Claude Sonnet 4.5 | Claude Haiku 4.5 |
| --- | --- | --- | --- |
| **Description** | Our most intelligent model for building agents and coding | Our best combination of speed and intelligence | Our fastest model with near-frontier intelligence |
| **Claude API ID** | claude-opus-4-6 | claude-sonnet-4-5-20250929 | claude-haiku-4-5-20251001 |
| **Claude API alias** | claude-opus-4-6 | claude-sonnet-4-5 | claude-haiku-4-5 |
| **AWS Bedrock ID** | anthropic.claude-opus-4-6-v1 | anthropic.claude-sonnet-4-5-20250929-v1:0 | anthropic.claude-haiku-4-5-20251001-v1:0 |
| **GCP Vertex AI ID** | claude-opus-4-6 | claude-sonnet-4-5@20250929 | claude-haiku-4-5@20251001 |
| **Pricing**1 | $5 / input MTok $25 / output MTok | $3 / input MTok $15 / output MTok | $1 / input MTok $5 / output MTok |
| **[Extended thinking](build-with-claude/extended-thinking.md)** | Yes | Yes | Yes |
| **[Adaptive thinking](build-with-claude/adaptive-thinking.md)** | Yes | No | No |
| **[Priority Tier](api/service-tiers.md)** | Yes | Yes | Yes |
| **Comparative latency** | Moderate | Fast | Fastest |
| **Context window** | 200K tokens /   1M tokens (beta)3 | 200K tokens /   1M tokens (beta)3 | 200K tokens |
| **Max output** | 128K tokens | 64K tokens | 64K tokens |
| **Reliable knowledge cutoff** | May 20252 | Jan 20252 | Feb 2025 |
| **Training data cutoff** | Aug 2025 | Jul 2025 | Jul 2025 |

*1 - See our [pricing page](about-claude/pricing.md) for complete pricing information including batch API discounts, prompt caching rates, extended thinking costs, and vision processing fees.*

*2 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used. For more information, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).*

*3 - Claude Opus 4.6 and Sonnet 4.5 support a [1M token context window](build-with-claude/context-windows.md) when using the `context-1m-2025-08-07` beta header. [Long context pricing](about-claude/pricing.md) applies to requests exceeding 200K tokens.*

Models with the same snapshot date (e.g., 20240620) are identical across all platforms and do not change. The snapshot date in the model name ensures consistency and allows developers to rely on stable performance across different environments.

Starting with **Claude Sonnet 4.5 and all subsequent models**, AWS Bedrock and Google Vertex AI offer two endpoint types: **global endpoints** (dynamic routing for maximum availability) and **regional endpoints** (guaranteed data routing through specific geographic regions). For more information, see the [third-party platform pricing section](about-claude/pricing.md).

### Legacy models

## Prompt and output performance

Claude 4 models excel in:

- **Performance**: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the [Claude 4 blog post](http://www.anthropic.com/news/claude-4) for more information.
- **Engaging responses**: Claude models are ideal for applications that require rich, human-like interactions.

  - If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to our [prompt engineering guides](build-with-claude/prompt-engineering.md) for details.
  - For prompting best practices, see our [prompting best practices guide](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).
- **Output quality**: When migrating from previous model generations to Claude 4, you may notice larger improvements in overall performance.

## Migrating to Claude 4.6

If you're currently using older Claude models, we recommend migrating to Claude Opus 4.6 to take advantage of improved intelligence and enhanced capabilities. For detailed migration instructions, see [Migrating to Claude 4.6](about-claude/models/migration-guide.md).

## Get started with Claude

If you're ready to start exploring what Claude can do for you, let's dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, we've got you covered.

Looking to chat with Claude? Visit [claude.ai](http://www.claude.ai)!

[Intro to Claude

Explore Claude's capabilities and development flow.](intro.md)[Quickstart

Learn how to make your first API call in minutes.](get-started.md)[Claude Console

Craft and test powerful prompts directly in your browser.](/)

If you have any questions or need assistance, don't hesitate to reach out to our [support team](https://support.claude.com/) or consult the [Discord community](https://www.anthropic.com/discord).

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
