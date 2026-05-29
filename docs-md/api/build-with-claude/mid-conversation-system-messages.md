# Mid-conversation system messages

Copy page

This feature is eligible for [Zero Data Retention (ZDR)](build-with-claude/api-and-data-retention.md). When your organization has a ZDR arrangement, data sent through this feature is not stored after the API response is returned.

System instructions normally live in the top-level `system` field, ahead of every message in the conversation. That position is great for [prompt caching](build-with-claude/prompt-caching.md): the system prompt is part of the stable prefix, so subsequent turns hit the cache. It is a poor position for instructions you only discover you need partway through a session, because editing the top-level `system` field changes the very beginning of the prompt and invalidates the cache for everything that follows.

Mid-conversation system messages close that gap. You append a `{"role": "system"}` message at the point in the conversation where the new instruction becomes relevant, instead of editing the top-level `system` field. The cached prefix stays the same, so the next request still reads it from cache, and the new instruction is still applied as a system instruction rather than as ordinary user text.

Mid-conversation system messages are available on the Claude API and [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md). They are not available on [Amazon Bedrock](build-with-claude/claude-in-amazon-bedrock.md), [Vertex AI](build-with-claude/claude-on-vertex-ai.md), or [Microsoft Foundry](build-with-claude/claude-in-microsoft-foundry.md).

This feature is available on Claude Opus 4.8 only. No beta header is required.

## Why position matters for caching

[Prompt caching](build-with-claude/prompt-caching.md) hashes the request prefix in order: `tools`, then `system`, then `messages`. A cache hit requires the prefix to match a recent request exactly, byte for byte, up to the cache breakpoint.

That ordering means the top-level `system` field sits near the very start of the hashed prefix. Any change to it, even appending a sentence, produces a different hash, and the request misses the cache for the system prompt and every cached message after it.

Mid-conversation system messages let you add the instruction at the **end** of the message history instead. Everything before the new instruction is unchanged, so the existing cache entry still matches, and only the new message is processed as fresh input.

A few situations where this matters:

- **Mid-session policy or persona changes.** A long agentic session needs a new constraint ("from now on, write all SQL as parameterized queries") after dozens of cached turns. Adding it to the top-level `system` field would re-process the entire history.
- **Per-turn context that must be authoritative.** You want to inject a freshness note, a session deadline, or a tool-availability change with system-level weight, and it changes too often to live in the cached prefix.
- **Tool results that should reshape behavior.** A tool surfaces a fact the model must treat as an instruction ("the customer is on the enterprise plan; do not suggest the consumer upgrade flow") for the rest of the session.
- **Mode switches that grant standing permissions.** A session-level mode can use a mid-conversation system message to grant standing consent to an expensive capability, such as automatically launching multi-agent workflows, with a short refresher every several turns and an exit notice when the mode is turned off. For a worked example, see [Build an orchestration mode](build-with-claude/mid-conversation-effort-example.md).

In all of these cases, putting the instruction in a regular `user` message works, but the model treats user content as data to interpret, not as an instruction with system-level priority. A mid-conversation system message preserves the instruction's authority without paying the cache-miss cost.

## How it works

Add a message with `"role": "system"` to the `messages` array. Use a plain string or content blocks for `content`, the same as a `user` or `assistant` turn. The instruction applies from that point in the conversation onward. When instructions conflict, later system messages take precedence over earlier ones, and mid-conversation system messages take precedence over the top-level `system` field for the turns that follow them.

You can still set the top-level `system` field for instructions that should apply to the entire conversation. Reserve mid-conversation system messages for instructions that only become relevant later, or that you want to add without invalidating the cached prefix.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    # Automatic prompt caching: each request caches the conversation so far,
    # and the next request reads the unchanged prefix from cache.
    cache_control={"type": "ephemeral"},
    system="You are a code review assistant. Be concise.",
    messages=[
        {
            "role": "user",
            "content": "Review process() in utils.py for performance issues.",
        },
        {
            "role": "assistant",
            "content": "The list comprehension is fine for small inputs. For large inputs, consider a generator to avoid materializing the full list.",
        },
        {
            "role": "user",
            "content": "Now review the calling code that invokes process().",
        },
        # The reviewer realizes mid-session that all suggestions must
        # also pass the team's strict typing policy. Appending the
        # instruction here keeps earlier turns byte-identical, so the
        # prefix cached by the previous request is still read from cache.
        {
            "role": "system",
            "content": "From now on, every suggestion must include explicit type annotations.",
        },
    ],
)

print(response.content[0].text)
```

This example enables [automatic caching](build-with-claude/prompt-caching.md) with the top-level `cache_control` field. Prompt caching is opt-in: if a request has no `cache_control` field (automatic or an [explicit breakpoint](build-with-claude/prompt-caching.md)), nothing is cached and every request pays the regular input token price for the full conversation. With caching enabled, appending the system message leaves the already-cached turns unchanged, so the request that carries the new instruction still reads them from cache instead of processing them again. Caching also requires the conversation to meet the [minimum cacheable prompt length](build-with-claude/prompt-caching.md); an example as short as this one falls below it, so `cache_creation_input_tokens` and `cache_read_input_tokens` stay at 0 until the conversation grows.

A mid-conversation system message must immediately follow a `user` message (or an `assistant` message that ends in a server tool use), and must either be the last entry in `messages` or be followed by an `assistant` turn. In practice, append it at the end of the array, after the latest `user` turn.

## Combining with prompt caching

Mid-conversation system messages and [prompt caching](build-with-claude/prompt-caching.md) are designed to be used together:

- **Enable caching explicitly.** Caching only happens when the request includes `cache_control`, either the top-level [automatic caching](build-with-claude/prompt-caching.md) field or an [explicit breakpoint](build-with-claude/prompt-caching.md) on a content block. A mid-conversation system message does not create a cache entry on its own, and without caching enabled there are no savings to preserve.
- **Cache the stable prefix as usual.** Place `cache_control` on the last block that stays the same across requests, whether that is the end of the top-level `system` field, the end of your tool definitions, or a stable point in the message history.
- **Append the system message after the breakpoint.** Because it comes after the cached prefix, it does not change the prefix hash and the cache still hits.
- **A mid-conversation system message is itself cacheable.** Once it is in the conversation, it becomes part of the stable history. On the next turn you can move your cache breakpoint past it (or rely on [automatic caching](build-with-claude/prompt-caching.md) to do so) and the system message is read from cache like any other turn.

Avoid editing or removing a mid-conversation system message that has already been sent. Like any other change to earlier messages, that invalidates the cache from that point forward. If the instruction needs to evolve, append a new system message rather than rewriting the old one. Consecutive system messages are not allowed; merge instructions into one message or wait for the next user turn before appending.

## Limitations

- **Not for the first message.** A `system` message cannot be the first entry in `messages`. Use the top-level `system` field for instructions that apply from the very start.
- **Placement is constrained.** A `system` message must immediately follow a `user` turn (or an `assistant` turn ending in server tool use) and must precede an `assistant` turn or end the array. Placing it elsewhere returns a 400 error.
- **Not a security boundary.** Mid-conversation system messages give an instruction system-level priority. They do not make untrusted content trustworthy. Continue to follow the guidance in [mitigate jailbreaks and prompt injections](test-and-evaluate/strengthen-guardrails/mitigate-jailbreaks.md) when building instructions from third-party data, regardless of which role carries them.

## Related

[Prompt caching

How caching works, where to place breakpoints, and how to read cache usage fields.](build-with-claude/prompt-caching.md)[Cache diagnostics

Find out exactly where two requests diverged when a cache hit you expected does not happen.](build-with-claude/cache-diagnostics.md)[Using the Messages API

Message structure, multi-turn conversations, and the `system` field.](build-with-claude/working-with-messages.md)[Prompting best practices

Writing effective prompts and system instructions.](build-with-claude/prompt-engineering/claude-prompting-best-practices.md)

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
