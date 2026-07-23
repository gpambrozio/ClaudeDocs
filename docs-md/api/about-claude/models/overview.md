# Models overview

Copy page



##  Choosing a model

If you're unsure which model to use, start with **Claude Opus 4.8** for complex agentic coding and enterprise work. For workloads that need the highest available capability, use [Claude Fable 5](#claude-fable-5-and-claude-mythos-5).

All current Claude models support text and image input, text output, multilingual capabilities, and vision. Models are available through the Claude API, [Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md), [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md), [Google Cloud](build-with-claude/claude-on-vertex-ai.md), and [Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md).

Once you've picked a model, [learn how to make your first API call](get-started.md).

###  Claude Fable 5 and Claude Mythos 5

Claude Fable 5 (`claude-fable-5`) is Anthropic's most capable widely released model. Claude Mythos 5 (`claude-mythos-5`) shares Claude Fable 5's specs and pricing and joins the invitation-only Claude Mythos Preview (`claude-mythos-preview`) within [Project Glasswing](https://anthropic.com/glasswing). See [Introducing Claude Fable 5 and Claude Mythos 5](about-claude/models/introducing-claude-fable-5-and-claude-mythos-5.md) for launch details and API changes.

Claude Fable 5 is generally available on the Claude API, Amazon Bedrock, Claude Platform on AWS, Google Cloud, and Microsoft Foundry beginning June 9, 2026. Claude Mythos 5 is not generally available: it is offered in limited availability to approved customers in [Project Glasswing](https://anthropic.com/glasswing), beginning the same day. For access, contact your Anthropic, AWS, or Google Cloud account team.

###  Latest models comparison

| Feature | Claude Fable 5 | Claude Opus 4.8 | Claude Sonnet 5 | Claude Haiku 4.5 |
| --- | --- | --- | --- | --- |
| **Description** | Next-generation intelligence for long-running agents | For complex agentic coding and enterprise work | The best combination of speed and intelligence | The fastest model with near-frontier intelligence |
| **Claude API ID** | claude-fable-5 | claude-opus-4-8 | claude-sonnet-5 | claude-haiku-4-5-20251001 |
| **Claude API alias** | claude-fable-5 | claude-opus-4-8 | claude-sonnet-5 | claude-haiku-4-5 |
| **AWS Bedrock ID** | anthropic.claude-fable-53 | anthropic.claude-opus-4-83 | anthropic.claude-sonnet-53 | anthropic.claude-haiku-4-5-20251001-v1:0 |
| **Google Cloud ID** | claude-fable-5 | claude-opus-4-8 | claude-sonnet-5 | claude-haiku-4-5@20251001 |
| **Pricing**1 | $10 / input MTok $50 / output MTok | $5 / input MTok $25 / output MTok | $3 / input MTok $15 / output MTok4 | $1 / input MTok $5 / output MTok |
| **[Extended thinking (`thinking.type: "enabled"`)](build-with-claude/extended-thinking.md)** | No | No | No | Yes |
| **[Adaptive thinking](build-with-claude/thinking-steering-and-cost.md)** | Yes (always on) | Yes | Yes | No |
| **Comparative latency** | Slower | Moderate | Fast | Fastest |
| **Context window** | 1M tokens | 1M tokens | 1M tokens | 200k tokens |
| **Max output** | 128k tokens | 128k tokens | 128k tokens | 64k tokens |
| **Reliable knowledge cutoff** | Jan 20262 | Jan 20262 | Jan 20262 | Feb 2025 |
| **Training data cutoff** | Jan 2026 | Jan 2026 | Jan 2026 | Jul 2025 |

*1 - See [Pricing](about-claude/pricing.md) for complete pricing information including Batch API discounts and prompt caching rates.*

*2 - **Reliable knowledge cutoff** indicates the date through which a model's knowledge is most extensive and reliable. **Training data cutoff** is the broader date range of training data used. For more information, see [Anthropic's Transparency Hub](https://www.anthropic.com/transparency).*

*3 - Claude Fable 5, Claude Opus 4.8, and Claude Sonnet 5 are available on Bedrock through [Claude in Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md) (the Messages-API Bedrock endpoint).*

*4 - Introductory pricing of $2 / $10 per MTok applies to Claude Sonnet 5 through August 31, 2026. See [Pricing](about-claude/pricing.md).*



Claude Mythos 5 and Claude Mythos Preview are offered separately for defensive cybersecurity workflows as part of [Project Glasswing](https://anthropic.com/glasswing). Access is invitation-only and there is no self-serve sign-up.



Every Claude model ID is a pinned snapshot. Models with a date in the ID (for example, `20250929`) are fixed to that specific release. Starting with the Claude 4.6 generation, model IDs use a dateless format that is also a pinned snapshot, not an evergreen pointer. For models before the 4.6 generation, entries in the Claude API alias column are convenience pointers that resolve to a dated model ID. For details on the naming convention and how versioning works, see [Model IDs and versioning](about-claude/models/model-ids-and-versions.md).



Starting with **Claude Sonnet 4.5 and all subsequent models** (including Claude Sonnet 4.6), Bedrock offers two endpoint types: **global endpoints** (dynamic routing for maximum availability) and **regional endpoints** (guaranteed data routing through specific geographic regions). Google Cloud offers three endpoint types: global endpoints, **multi-region endpoints** (dynamic routing within a geographic area), and regional endpoints. For more information, see [Cloud platform pricing](about-claude/pricing.md).



**Claude Platform on AWS** uses the same model IDs as the Claude API (for example, `claude-opus-4-6`), not Bedrock-style IDs. Model lifecycle on Claude Platform on AWS follows Anthropic's first-party [Model deprecations](about-claude/model-deprecations.md), not Bedrock's. See [Available models](build-with-claude/claude-platform-on-aws.md) for the model list.



You can query model capabilities and token limits programmatically with the [Models API](api/models/list.md). The response includes `max_input_tokens`, `max_tokens`, and a `capabilities` object for every available model.



On Claude Opus 4.8, the `effort` parameter defaults to `high` on all surfaces, including the Claude API, Claude Code, and claude.ai. On Claude Sonnet 5, it defaults to `high` on the Claude API and Claude Code. Set `effort` explicitly to use a different level. See [Effort](build-with-claude/effort.md) for guidance on choosing a level.



The Max output values in the table apply to the synchronous Messages API. On the [Message Batches API](build-with-claude/batch-processing.md), Claude Opus 4.8, Opus 4.7, Opus 4.6, Sonnet 5, and Sonnet 4.6 support up to 300k output tokens by using the `output-300k-2026-03-24` beta header.

### Legacy models

##  Prompt and output performance

Current Claude models excel in:

- **Performance:** Top-tier results in reasoning, coding, multilingual tasks, long-context handling, honesty, and image processing. See [Prompting Claude Sonnet 5](build-with-claude/prompt-engineering/prompting-claude-sonnet-5.md) and [Prompting Claude Opus 4.8](build-with-claude/prompt-engineering/prompting-claude-opus-4-8.md) for model-specific prompting guidance.
- **Engaging responses:** Claude models are ideal for applications that require rich, human-like interactions.

  - If you prefer more concise responses, you can adjust your prompts to guide the model toward the desired output length. Refer to the [prompt engineering guides](build-with-claude/prompt-engineering.md) for details.
  - For prompting best practices, see [Prompting best practices](build-with-claude/prompt-engineering/claude-prompting-best-practices.md).
- **Output quality:** When migrating from a previous model generation, you may notice larger improvements in overall performance.

##  Migrating to Claude Opus 4.8

If you're currently using Claude Opus 4.7 or earlier Claude models, see [Migrating to Claude Opus 4.8](about-claude/models/migration-guide.md).

If you're currently using Claude Opus 4.6 or older Claude models, see [Migrating to Claude Opus 4.8 from Claude Opus 4.6](about-claude/models/migration-guide.md).

##  Get started with Claude

If you're ready to start exploring what Claude can do for you, dive in! Whether you're a developer looking to integrate Claude into your applications or a user wanting to experience the power of AI firsthand, the following resources can help.



Looking to chat with Claude? Visit [claude.ai](https://claude.ai)!

[

Intro to Claude

Explore Claude's capabilities and development flow.](intro.md)[

Quickstart

Learn how to make your first API call in minutes.](get-started.md)[

Claude Console

Craft and test powerful prompts directly in your browser.](/)

If you have any questions or need assistance, don't hesitate to reach out to the [support team](https://support.claude.com/) or consult the [Discord community](https://www.anthropic.com/discord).

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
