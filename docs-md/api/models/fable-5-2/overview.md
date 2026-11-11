# Overview

---
title: Claude Fable 5.2
url: https://platform.claude.com/docs/en/models/fable-5-2/overview
description: "An overview of Claude Fable 5.2: what it's for, model IDs on every platform, context window, output limits, pricing, availability, and resources for building with it."
---

**Latest.** Released November 9, 2026.

For demanding reasoning and long-horizon agentic work

Model ID: `claude-fable-5-2`

Context window: 1M tokens · Max output: 128K tokens · Input pricing: $8 / MTok · Output pricing: $40 / MTok

[Announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2) · [What’s new](whats-new-fable-5-2.md) · [Migration guide](migration-guide.md)

## Overview

Claude Fable 5.2 is built for demanding reasoning and long-horizon agentic work. Typical uses include agent sessions that run for hours, multistep deep research, and analysis carried through to a finished document, spreadsheet, or deck.

## Claude Fable 5.2 and Claude Mythos 5.2

[Claude Mythos 5.2](../mythos-5-2/overview.md) offers the same capabilities only to organizations verified through Anthropic’s verification programs, such as the [Cyber Verification Program](https://support.claude.com/en/articles/14604842). It shares Claude Fable 5.2’s specifications and pricing. To request access, apply to the program that covers your use case, or contact your account team.

## How it compares

| Model                                                                               | Context | Max output | Price / MTok       | Latency  | Thinking             | Default effort | Knowledge cutoff |
| :---------------------------------------------------------------------------------- | :------ | :--------- | :----------------- | :------- | :------------------- | :------------- | :--------------- |
| **Claude Fable 5.2** (this model)                                                   | 1M      | 128K       | $8 / $40           | Moderate | Adaptive (always on) | `high`         | Jun 2026         |
| [Claude Opus 5.5](../opus-5-5/overview.md)     | 1M      | 128K       | $4 / $20           | Moderate | Adaptive (always on) | `medium`       | Jun 2026         |
| [Claude Sonnet 5.5](../sonnet-5-5/overview.md) | 1M      | 128K       | $2 / $10           | Fast     | Adaptive             | `high`         | Jun 2026         |
| [Claude Haiku 5.5](../haiku-5-5/overview.md)   | 1M      | 128K       | From $0.10 / $0.50 | Fastest  | Adaptive             | `medium`       | Jun 2026         |

* **Context:** 1M tokens is roughly 555k words or 2.5M Unicode characters on the current tokenizer (introduced with Claude Opus 4.7); models before it fit about 750k words in 1M tokens. 200k tokens is roughly 150k words.
* **Max output:** Synchronous Messages API limit. On the Message Batches API, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Haiku 5.5, Claude Opus 4.8, Claude Opus 4.7, Claude Opus 4.6, and Claude Sonnet 4.6 support up to 300k output tokens with the output-300k-2026-03-24 beta header.
* **Price / MTok:** Input / output, base price per million tokens. Batch API requests are 50% off; prompt caching reads cost 10% of the base input price (2.5% on Claude Fable 5.2, Claude Mythos 5.2, Claude Fable 5.1, and Claude Mythos 5.1, 5% on Claude Opus 5.5 and Claude Sonnet 5.5). See Pricing for the full list.
* **Latency:** Comparative latency, relative to the current lineup, as published in the models overview. Actual latency depends on prompt length, output length, and thinking effort.
* **Thinking:** Adaptive thinking lets the model decide how much to think, steered by effort. Extended thinking is the manual budget\_tokens mode on earlier models.
* **Default effort:** The effort parameter’s default on the Claude API. Models without a value don’t support the parameter.
* **Knowledge cutoff:** Reliable knowledge cutoff: the date through which the model’s knowledge is most extensive and reliable.

## Specifications

### Model IDs

| Platform                                                                                                                                                   | Model ID                            |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------------------------- |
| Claude API                                                                                                                                                 | `claude-fable-5-2`                  |
| [Amazon Bedrock (bedrock-runtime)](../../build-with-claude/claude-on-amazon-bedrock-legacy.md)                                  | `global.anthropic.claude-fable-5-2` |
| [Claude Models on Google Cloud (Google managed)](../../build-with-claude/claude-models-on-google-cloud/google-managed.md)       | `claude-fable-5-2`                  |
| [Microsoft Foundry](../../build-with-claude/claude-in-microsoft-foundry.md)                                                     | `claude-fable-5-2`                  |
| [Claude Platform on AWS](../../build-with-claude/claude-platform-on-aws.md)                                                     | `claude-fable-5-2`                  |
| [Claude Models on Google Cloud (Anthropic managed)](../../build-with-claude/claude-models-on-google-cloud/anthropic-managed.md) | `claude-fable-5-2`                  |

### Pricing

| Feature                                                                                | Value                            |
| :------------------------------------------------------------------------------------- | :------------------------------- |
| Input                                                                                  | $8 / MTok                        |
| Output                                                                                 | $40 / MTok                       |
| [5m cache write](../../build-with-claude/prompt-caching.md) | $10 / MTok                       |
| [1h cache write](../../build-with-claude/prompt-caching.md) | $16 / MTok                       |
| [Cache read](../../build-with-claude/prompt-caching.md)     | $0.20 / MTok                     |
| [Batch API](../../build-with-claude/batch-processing.md)    | 50% discount on input and output |

[Full price list](../../about-claude/pricing.md)

### Capabilities

| Feature                                                                                 | Value                  |
| :-------------------------------------------------------------------------------------- | :--------------------- |
| [Context window](../../build-with-claude/context-windows.md) | 1M tokens              |
| Max output                                                                              | 128K tokens            |
| [Thinking](../../build-with-claude/thinking.md)              | Adaptive (always on)   |
| [Default effort](../../build-with-claude/effort.md)          | `high`                 |
| Comparative latency                                                                     | Moderate               |
| Input → output                                                                          | Text and images → text |
| Reliable knowledge cutoff                                                               | Jun 2026               |
| Training data cutoff                                                                    | Jun 2026               |

### Availability

| Feature                                                                       | Value                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| :---------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Status](../../about-claude/model-deprecations.md) | Active (latest)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Released                                                                      | November 9, 2026                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Retirement                                                                    | Not sooner than November 9, 2027                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Platforms                                                                     | Claude API, [Amazon Bedrock (bedrock-runtime)](../../build-with-claude/claude-on-amazon-bedrock-legacy.md), [Claude Models on Google Cloud (Google managed)](../../build-with-claude/claude-models-on-google-cloud/google-managed.md), [Microsoft Foundry](../../build-with-claude/claude-in-microsoft-foundry.md), [Claude Platform on AWS](../../build-with-claude/claude-platform-on-aws.md), [Claude Models on Google Cloud (Anthropic managed)](../../build-with-claude/claude-models-on-google-cloud/anthropic-managed.md) |

## Good to know

* Adaptive thinking is always on and can’t be turned off. Control thinking depth with the [effort parameter](../../build-with-claude/effort.md).
* Forced tool use (`tool_choice` types `any` and `tool`) returns a 400 error. See [Thinking and tool choice](whats-new-fable-5-2.md#thinking-and-tool-choice).
* Omit `temperature`, `top_p`, and `top_k`. See [Sampling parameters](../../build-with-claude/thinking.md#sampling-parameters) for the values that return a 400 error.
* Claude Fable 5.2 requires 30-day data retention and isn’t available under zero data retention unless expressly authorized by Anthropic. See [Model-specific data retention requirements](../../manage-claude/api-and-data-retention.md#model-specific-data-retention-requirements).
* Query limits and capabilities programmatically with the [Models API](../../api/models/list.md).

## Resources

**Prompting Claude Fable 5.2**

Behavioral differences and prompting patterns specific to Claude Fable 5.2.

**Claude Fable 5.2 migration guide**

What changes when you move from Claude Fable 5.1 or from a Claude Opus model.

**Preserved thinking**

Editing earlier turns invalidates thinking blocks, for every account.

**Adaptive thinking**

How adaptive thinking works. It’s the only thinking mode on Claude Fable 5.2.

**Effort**

The control for thinking depth, latency, and cost. Choose a level for each workload.

**Refusals and fallback**

Handle classifier refusals and retry on another Claude model.

**Fast mode**

Faster output from Claude Fable 5.2 in Messages API requests, at premium pricing.

## Reference

**System prompt**

The system prompt Claude Fable 5.2 uses on claude.ai and the Claude apps.

**System card**

Safety evaluations and deployment decisions for Claude Fable 5.2 and Claude Mythos 5.2.

**Pricing**

Full price list, including batch discounts and prompt caching rates.

**Model IDs and versioning**

How model IDs, aliases, and pinned snapshots work.

**Model deprecations**

Lifecycle status and retirement commitments for every Claude model.

---

*Copyright © Anthropic. All rights reserved.*
