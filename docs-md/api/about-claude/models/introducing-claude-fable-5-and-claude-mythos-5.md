# Introducing Claude Fable 5 and Claude Mythos 5

Copy page





Access to Claude Fable 5 and Claude Mythos 5 has been restored. See [our statement](https://www.anthropic.com/news/redeploying-fable-5) for more information.

Claude Fable 5 is Anthropic's most capable widely released model, built for the most demanding reasoning and long-horizon agentic work. Claude Mythos 5 shares the same capabilities and is available only in limited release through [Project Glasswing](https://anthropic.com/glasswing).

The headline change for integrations: Claude Fable 5 includes safety classifiers that can decline requests. Claude Mythos 5 does not include these classifiers. If your integration calls Claude Fable 5, plan for three changes: new response handling for refusals, fallback options for retrying on another Claude model, and new billing rules. [Refusals, fallback, and billing on Claude Fable 5](#refusals-fallback-and-billing-on-claude-fable-5) summarizes all three.

##  Models

| Model | API model ID | Description |
| --- | --- | --- |
| Claude Fable 5 | `claude-fable-5` | Anthropic's most capable widely released model, for the most demanding reasoning and long-horizon agentic work |
| Claude Mythos 5 | `claude-mythos-5` | Shares Claude Fable 5's capabilities without the safety classifiers. Available through Project Glasswing. Successor to Claude Mythos Preview. |

Claude Fable 5 and Claude Mythos 5 share the same specs and pricing:

- **Context window and output:** a [1M token context window](build-with-claude/context-windows.md) by default, and up to 128k output tokens per request.
- **Pricing:** $10 USD per million input tokens and $50 USD per million output tokens.

For specs across all current models, see the [models overview](about-claude/models/overview.md).

##  Refusals, fallback, and billing on Claude Fable 5

Claude Fable 5 includes safety classifiers that can decline certain requests. Claude Mythos 5 does not include these classifiers, so this section applies to Claude Fable 5 only. The following sections summarize what refusals mean for your integration; each links to the full guide.

###  Refusals

When Claude Fable 5 declines a request, the Messages API returns `stop_reason: "refusal"` as a successful HTTP 200 response, not an error. The response also reports which classifier declined the request. See [Refusals and fallback](build-with-claude/refusals-and-fallback.md) for response shapes and handling guidance.

###  Fallback

A request that Claude Fable 5 refuses can usually be served by another Claude model. There are three ways to retry:

- **Server-side:** Pass the `fallbacks` parameter to have the API retry for you (in beta on the Claude API and Claude Platform on AWS). See [Server-side fallback](build-with-claude/refusals-and-fallback.md).
- **Client-side:** Use the [SDK middleware](cli-sdks-libraries/middleware.md) to retry from the client on any platform. See [Client-side fallback](build-with-claude/refusals-and-fallback.md).
- **Manual:** Build the retry yourself, on any platform and in any language. See [Fallback credit](build-with-claude/fallback-credit.md).

###  Billing

You are not billed for a request that is refused before any output is generated. When you retry on another model, [fallback credit](build-with-claude/fallback-credit.md) refunds the prompt-cache cost of switching, so you avoid paying that cost twice.

##  Availability

Claude Fable 5 and Claude Mythos 5 both become available on June 9, 2026:

- **Claude Fable 5** is generally available on the Claude API, [Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md), [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md), [Google Cloud](build-with-claude/claude-on-vertex-ai.md), and [Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md).
- **Claude Mythos 5** is not generally available: it is offered in limited availability to approved customers in [Project Glasswing](https://anthropic.com/glasswing). For access, contact your Anthropic, AWS, or Google Cloud account team. Customers without access to Claude Mythos 5 can use Claude Fable 5, which is generally available and offers the same capabilities.

Claude Fable 5 and Claude Mythos 5 carry 30-day data retention and are not available under zero data retention: both are designated [Covered Models](https://support.claude.com/en/articles/15425695). See [Model-specific data retention requirements](manage-claude/api-and-data-retention.md).

##  Working with Claude Fable 5 and Claude Mythos 5

###  Prompting

Claude Fable 5 responds to the same prompting techniques as other Claude models, with a few differences in how to structure long-context prompts and reasoning instructions. See [Prompting Claude Fable 5](build-with-claude/prompt-engineering/prompting-claude-fable-5.md).

##  Messages API on Claude Fable 5 and Claude Mythos 5



The behaviors in this section are specific to Claude Fable 5 and Claude Mythos 5. The Messages API is unchanged for Opus, Sonnet, and Haiku models.

###  Adaptive thinking is always on

[Adaptive thinking](build-with-claude/adaptive-thinking.md) is the only thinking mode on Claude Fable 5 and Claude Mythos 5. It applies whenever the `thinking` parameter is unset. `thinking: {"type": "disabled"}` is not supported. Use the [effort parameter](build-with-claude/effort.md) to control thinking depth.

###  Raw thinking content is never returned

The raw chain of thought is never returned on Claude Fable 5 and Claude Mythos 5. The `thinking.display` setting controls what thinking blocks contain instead:

- `"summarized"` returns thinking blocks with a readable summary of the reasoning.
- `"omitted"` (the default) returns thinking blocks with an empty `thinking` field.

Pass thinking blocks back unchanged in multi-turn conversations on the same model. See [thinking output on Claude Fable 5 and Claude Mythos 5](build-with-claude/adaptive-thinking.md) for cross-model handling.

##  Supported features

At launch, Claude Fable 5 and Claude Mythos 5 support:

- [Effort](build-with-claude/effort.md)
- [Task budgets](build-with-claude/task-budgets.md) (beta: set the `task-budgets-2026-03-13` header)
- The [memory tool](agents-and-tools/tool-use/memory-tool.md)
- [Code execution](agents-and-tools/tool-use/code-execution-tool.md)
- [Programmatic tool calling](agents-and-tools/tool-use/programmatic-tool-calling.md)
- Tool result clearing through [context editing](build-with-claude/context-editing.md) (beta: set the `context-management-2025-06-27` header)
- [Compaction](build-with-claude/compaction.md)
- [Vision](build-with-claude/vision.md)

##  Migrating from earlier models

Step-by-step instructions live in the migration guide:

- From Claude Mythos Preview: see [Migrating from Claude Mythos Preview to Claude Mythos 5](about-claude/models/migration-guide.md).
- From Claude Opus 4.8: see [Migrating from Claude Opus 4.8 to Claude Fable 5](about-claude/models/migration-guide.md).

##  Next steps

[

Migration guide

Step-by-step upgrade instructions from Claude Opus 4.8 and Claude Mythos Preview.](about-claude/models/migration-guide.md)[

Models overview

Specs and comparison for all current Claude models.](about-claude/models/overview.md)[Adaptive thinking

The only thinking mode on Claude Fable 5 and Claude Mythos 5.](build-with-claude/adaptive-thinking.md)[Refusals and fallback

How Claude Fable 5 declines requests, and how to retry on another model.](build-with-claude/refusals-and-fallback.md)[Fallback credit

Avoid paying the prompt-cache cost twice on a retry.](build-with-claude/fallback-credit.md)[Fallback and billing cookbook



A worked end-to-end example of refusal handling, fallback, and billing.](https://platform.claude.com/cookbook/fable-5-fallback-billing-guide)[Effort

Control thinking depth and cost on Claude Fable 5 and Claude Mythos 5.](build-with-claude/effort.md)[Prompting Claude Fable 5

Fable-specific prompting techniques.](build-with-claude/prompt-engineering/prompting-claude-fable-5.md)

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
