# Intro

---
title: Intro to Claude
url: https://platform.claude.com/docs/en/intro
description: Claude is a highly performant, trustworthy, and intelligent AI platform built by Anthropic. Claude excels at tasks involving language, reasoning, analysis, coding, and more.
---

Looking to chat with Claude? Visit [claude.ai](https://claude.ai).

Anthropic offers two ways to build with Claude, each suited to different use cases:

|                | Messages API                                | Claude Managed Agents                                                     |
| -------------- | ------------------------------------------- | ------------------------------------------------------------------------- |
| **What it is** | Direct model prompting access               | Pre-built, configurable agent harness that runs in managed infrastructure |
| **Best for**   | Custom agent loops and fine-grained control | Long-running tasks and asynchronous work                                  |

To learn more about each, see [Using the Messages API](build-with-claude/working-with-messages.md) and the [Claude Managed Agents overview](managed-agents/overview.md).

## Explore the latest generation of Claude models

If you're unsure which model to use, start with [Claude Opus 5](models/opus-5/overview.md) for most workloads. Use [Claude Fable 5.1](models/fable-5-1/overview.md) for demanding reasoning and long-horizon agentic work, or when your evals on Claude Opus 5 at higher effort still fall short. All current models support text and image input, text output, multilingual capabilities, vision, and tool use. Each model's page lists the platforms it's available on.

* [Claude Fable 5.1](models/fable-5-1/overview.md) (`claude-fable-5-1`) — New — *For demanding reasoning and long-horizon agentic work* — Most capable · Research · Multi-day tasks
* [Claude Opus 5](models/opus-5/overview.md) (`claude-opus-5`) — *For complex agentic coding and enterprise work* — Complex projects · Agents · Coding
* [Claude Sonnet 5](models/sonnet-5/overview.md) (`claude-sonnet-5`) — *The best combination of speed and intelligence* — Everyday tasks · Writing · Cost-efficient
* [Claude Haiku 4.5](models/haiku-4-5/overview.md) (`claude-haiku-4-5`) — *The fastest model with near-frontier intelligence* — Fastest · Lowest cost · High volume

[Compare models](models/overview.md)

***

## Recommended path for new developers

Follow these steps to go from zero to a working Claude integration.

**Make your first API call**

Set up your environment, install an SDK, and send your first message to Claude.

[Go to the quickstart](get-started.md)

**Secure your credentials**

Set an expiration when you create your API key. Keep the key out of source control, client-side code, and prompts. Check whether your workload can use Workload Identity Federation instead of a static key.

[Read the authentication guide](manage-claude/authentication.md)

**Understand the Messages API**

Learn the core request and response structure, including multi-turn conversations, system prompts, and stop reasons.

[Read the Messages API guide](build-with-claude/working-with-messages.md)

**Choose the right model**

Compare Claude models by capability and cost to pick the best fit for your use case.

[See the models overview](models/overview.md)

**Explore features and tools**

Discover what Claude can do: extended thinking, web search, file handling, structured outputs, and more.

[Browse the features overview](build-with-claude/overview.md)

***

## Develop with Claude

Anthropic provides developer tools to help you build and scale applications with Claude.

**Developer Console**

Explore and understand the API in your browser with playground.

**API Reference**

Explore the full Claude API and client SDK documentation.

**Claude Cookbook**

Learn with interactive Jupyter notebooks covering PDFs, embeddings, and more.

***

## Key capabilities

Claude can assist with many tasks that involve text, code, and images.

**Text and code generation**

Summarize text, answer questions, extract data, translate text, and explain and generate code.

**Vision**

Process and analyze visual input and generate text and code from images.

***

## Support

**Help Center**

Find answers to frequently asked account and billing questions.

**Service Status**

Check the status of Anthropic services.

---

*Copyright © Anthropic. All rights reserved.*
