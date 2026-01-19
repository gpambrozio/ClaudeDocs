# Prompt engineering overview

Copy page

While these tips apply broadly to all Claude models, you can find prompting tips specific to extended thinking models [here](build-with-claude/prompt-engineering/extended-thinking-tips.md).

## Before prompt engineering

This guide assumes that you have:

1. A clear definition of the success criteria for your use case
2. Some ways to empirically test against those criteria
3. A first draft prompt you want to improve

If not, we highly suggest you spend time establishing that first. Check out [Define your success criteria](test-and-evaluate/define-success.md) and [Create strong empirical evaluations](test-and-evaluate/develop-tests.md) for tips and guidance.

[Prompt generator

Don't have a first draft prompt? Try the prompt generator in the Claude Console!](/dashboard)

---

## When to prompt engineer

This guide focuses on success criteria that are controllable through prompt engineering.
Not every success criteria or failing eval is best solved by prompt engineering. For example, latency and cost can be sometimes more easily improved by selecting a different model.

### Prompting vs. finetuning

---

## How to prompt engineer

The prompt engineering pages in this section have been organized from most broadly effective techniques to more specialized techniques. When troubleshooting performance, we suggest you try these techniques in order, although the actual impact of each technique will depend on your use case.

1. [Prompt generator](build-with-claude/prompt-engineering/prompt-generator.md)
2. [Be clear and direct](build-with-claude/prompt-engineering/be-clear-and-direct.md)
3. [Use examples (multishot)](build-with-claude/prompt-engineering/multishot-prompting.md)
4. [Let Claude think (chain of thought)](build-with-claude/prompt-engineering/chain-of-thought.md)
5. [Use XML tags](build-with-claude/prompt-engineering/use-xml-tags.md)
6. [Give Claude a role (system prompts)](build-with-claude/prompt-engineering/system-prompts.md)
7. [Prefill Claude's response](build-with-claude/prompt-engineering/prefill-claudes-response.md)
8. [Chain complex prompts](build-with-claude/prompt-engineering/chain-prompts.md)
9. [Long context tips](build-with-claude/prompt-engineering/long-context-tips.md)

---

## Prompt engineering tutorial

If you're an interactive learner, you can dive into our interactive tutorials instead!

[GitHub prompting tutorial

An example-filled tutorial that covers the prompt engineering concepts found in our docs.](https://github.com/anthropics/prompt-eng-interactive-tutorial)[Google Sheets prompting tutorial

A lighter weight version of our prompt engineering tutorial via an interactive spreadsheet.](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8)

---

*Copyright © Anthropic. All rights reserved.*
