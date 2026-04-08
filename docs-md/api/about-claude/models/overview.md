# Models overview

Copy page

## Choosing a model

If you're unsure which model to use, consider starting with **Claude Opus 4.6** for the most complex tasks. It is the most intelligent broadly available model with exceptional performance in coding and reasoning.

All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available via the Claude API, AWS Bedrock, and Google Vertex AI.

Once you've picked a model, [learn how to make your first API call](get-started.md).

### Latest models comparison

| Feature | Claude Opus 4.6 | Claude Sonnet 4.6 | Claude Haiku 4.5 |
| --- | --- | --- | --- |
| **Description** | The most intelligent broadly available model for agents and coding | The best combination of speed and intelligence | The fastest model with near-frontier intelligence |
| **Claude API ID** | claude-opus-4-6 | claude-sonnet-4-6 | claude-haiku-4-5-20251001 |
| **Claude API alias** | claude-opus-4-6 | claude-sonnet-4-6 | claude-haiku-4-5 |
| **AWS Bedrock ID** | anthropic.claude-opus-4-6-v1 | anthropic.claude-sonnet-4-6 | anthropic.claude-haiku-4-5-20251001-v1:0 |
| **GCP Vertex AI ID** | claude-opus-4-6 | claude-sonnet-4-6 | claude-haiku-4-5@20251001 |
| **Pricing**1 | $5 / input MTok $25 / output MTok | $3 / input MTok $15 / output MTok | $1 / input MTok $5 / output MTok |
| **[Extended thinking](build-with-claude/extended-thinking.md)** | Yes | Yes | Yes |
| **[Adaptive thinking](build-with-claude/adaptive-thinking.md)** | Yes | Yes | No |
| **[Priority Tier](api/service-tiers.md)** | Yes | Yes | Yes |
| **Comparative latency** | Moderate | Fast | Fastest |
| **Context window** | 1M tokens | 1M tokens | 200k tokens |
| **Max output** | 128k tokens | 64k tokens | 64k tokens |
| **Reliable knowledge cutoff** | May 20252 | Aug 20252 | Feb 2025 |
| **Training data cutoff** | Aug 2025 | Jan 2026 | Jul 2025 |

*1 - See the [pricing page](about-claude/pricing.md) for complete pricing information including batch API discounts, prompt caching rates, extended thinking costs, and vision processing fees.*

*2 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used. For more information, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).*

[Claude Mythos Preview](https://anthropic.com/glasswing) is offered separately as a research preview model for defensive cybersecurity workflows as part of [Project Glasswing](https://anthropic.com/glasswing). Access is invitation-only and there is no self-serve sign-up.

Models with the same snapshot date (e.g., 20240620) are identical across all platforms and do not change. The snapshot date in the model name ensures consistency and allows developers to rely on stable performance across different environments.

Starting with **Claude Sonnet 4.5 and all subsequent models** (including Claude Sonnet 4.6), AWS Bedrock offers two endpoint types: **global endpoints** (dynamic routing for maximum availability) and **regional endpoints** (guaranteed data routing through specific geographic regions). Google Vertex AI offers three endpoint types: global endpoints, **multi-region endpoints** (dynamic routing within a geographic area), and regional endpoints. For more information, see the [third-party platform pricing section](about-claude/pricing.md).

You can query model capabilities and token limits programmatically with the [Models API](api/models/list.md). The response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.

The Max output values above apply to the synchronous Messages API. On the [Message Batches API](build-with-claude/batch-processing.md), Opus 4.6 and Sonnet 4.6 support up to 300k output tokens by using the `output-300k-2026-03-24` beta header.

### Legacy models

## Prompt and output performance

Claude 4 models excel in:

- **Performance**: Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See the [Claude 4 blog post](http://www.anthropic.com/news/claude-4) for more information.
- **Engaging responses**: Claude models are ideal for applications that require rich, human-like interactions.

  - If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to the [prompt engineering guides](build-with-claude/prompt-engineering.md) for details.
  - For prompting best practices, see the [prompting best practices guide](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).
- **Output quality**: When migrating from previous model generations to Claude 4, you may notice larger improvements in overall performance.

## Migrating to Claude 4.6

If you're currently using older Claude models, consider migrating to Claude Opus 4.6 to take advantage of improved intelligence and enhanced capabilities. For detailed migration instructions, see [Migrating to Claude 4.6](about-claude/models/migration-guide.md).

## Get started with Claude

If you're ready to start exploring what Claude can do for you, dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.

Looking to chat with Claude? Visit [claude.ai](http://www.claude.ai)!

[Intro to Claude

Explore Claude's capabilities and development flow.](intro.md)[Quickstart

Learn how to make your first API call in minutes.](get-started.md)[Claude Console

Craft and test powerful prompts directly in your browser.](/)

If you have any questions or need assistance, don't hesitate to reach out to the [support team](https://support.claude.com/) or consult the [Discord community](https://www.anthropic.com/discord).

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
