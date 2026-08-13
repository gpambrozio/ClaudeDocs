# Fast mode (research preview)

Copy page



Fast mode delivers up to 2.5x higher output tokens per second from Claude Opus 5 and Claude Opus 4.8 at premium pricing. Set `speed: "fast"` with the `fast-mode-2026-02-01` beta header on your request to opt in.

##  Supported models

Fast mode is supported on the following models:

- Claude Opus 5 (claude-opus-5)
- Claude Opus 4.8 (claude-opus-4-8)

##  How fast mode works

Fast mode runs the same model with a faster inference configuration. There is no change to intelligence or capabilities.

- Up to 2.5x higher output tokens per second compared to standard speed
- Speed benefits are focused on output tokens per second (OTPS), not time to first token (TTFT)
- Same model weights and behavior (not a different model)
- Compatible with [streaming](build-with-claude/streaming.md), where the OTPS gain is most visible

##  Basic usage

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=4096,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[
        {"role": "user", "content": "Refactor this module to use dependency injection"}
    ],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
```

##  Pricing

Fast mode is priced at a multiplier on standard rates across the full context window, including requests over 200k input tokens. The following table shows fast mode pricing for the supported models:

| Model | Input | Output |
| --- | --- | --- |
| Claude Opus 5 / Claude Opus 4.8 | $10 USD / MTok | $50 USD / MTok |

Fast mode pricing stacks with other pricing modifiers:

- [Prompt caching multipliers](about-claude/pricing.md) apply on top of fast mode pricing
- [Data residency](manage-claude/data-residency.md) multipliers apply on top of fast mode pricing

For complete pricing details, see the [Pricing](about-claude/pricing.md) page.

##  Rate limits

Fast mode has a dedicated rate limit that is separate from standard Opus rate limits. When your fast mode rate limit is exceeded, the API returns a `429` error with a `retry-after` header indicating when capacity will be available.

The response includes headers that indicate your fast mode rate limit status:

| Header | Description |
| --- | --- |
| `anthropic-fast-input-tokens-limit` | Maximum fast mode input tokens per minute |
| `anthropic-fast-input-tokens-remaining` | Remaining fast mode input tokens |
| `anthropic-fast-input-tokens-reset` | Time when the fast mode input token limit resets |
| `anthropic-fast-output-tokens-limit` | Maximum fast mode output tokens per minute |
| `anthropic-fast-output-tokens-remaining` | Remaining fast mode output tokens |
| `anthropic-fast-output-tokens-reset` | Time when the fast mode output token limit resets |

For tier-specific rate limits, see the [Rate limits](api/rate-limits.md) page.

##  Checking which speed was used

The response `usage` object includes a `speed` field that indicates which speed was used, either `"fast"` or `"standard"`. Requesting `speed: "fast"` on a [model that doesn't support fast mode](#supported-models) returns an error, and so does exceeding fast mode's rate limits or capacity (a `429` or `529`). When a request with `speed: "fast"` succeeds, `usage.speed` is `"fast"`. If you are using Claude Opus 4.6 and request fast mode, its behavior is unique. Instead of returning an error like other models that don't support fast mode, it silently switches to standard speed. Though there is no error with Opus 4.6, the `speed` field accurately shows `"standard"`.

cURLCLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    speed="fast",
    betas=["fast-mode-2026-02-01"],
    messages=[{"role": "user", "content": "Hello"}],
)

print(response.usage.speed)  # "fast" or "standard"
```

Output



```shiki
{
  "id": "msg_01XFDUDYJgAACzvnptvVoYEL",
  "type": "message",
  "role": "assistant",
// ...
  "usage": {
    "input_tokens": 8,
    "output_tokens": 12,
    "speed": "fast"
  }
}
```

To track fast mode usage and costs across your organization, see the [Usage and Cost API](manage-claude/usage-cost-api.md).

##  Retries and fallback

###  Automatic retries

When fast mode rate limits are exceeded, the API returns a `429` error with a `retry-after` header. The Anthropic SDKs automatically retry these requests up to 2 times by default (configurable with `max_retries`), waiting for the server-specified delay before each retry. Because fast mode uses continuous token replenishment, the `retry-after` delay is typically short and requests succeed once capacity is available.

###  Falling back to standard speed

If you'd prefer to fall back to standard speed rather than wait for fast mode capacity, catch the rate limit error and retry without `speed: "fast"`. Set `max_retries` to `0` on the initial fast request to skip automatic retries and fail immediately on rate limit errors.

Because setting `max_retries` to `0` also disables retries for other transient errors (overloaded, internal server errors), the following examples reissue the original request with default retries for those cases.

CLIPythonTypeScriptC#GoJavaPHPRuby



```shiki
client = anthropic.Anthropic()

def create_message_with_fast_fallback(max_retries=0, max_attempts=3, **params):
    try:
        return client.with_options(max_retries=max_retries).beta.messages.create(
            **params
        )
    except anthropic.RateLimitError:
        if params.get("speed") == "fast":
            del params["speed"]
            return create_message_with_fast_fallback(max_retries=max_retries, **params)
        raise
    except (
        anthropic.APIStatusError,
        anthropic.APIConnectionError,
    ) as error:
        if isinstance(error, anthropic.APIStatusError) and error.status_code < 500:
            raise
        if max_attempts > 1:
            return create_message_with_fast_fallback(
                max_retries=max_retries, max_attempts=max_attempts - 1, **params
            )
        raise

message = create_message_with_fast_fallback(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    betas=["fast-mode-2026-02-01"],
    speed="fast",
    max_retries=0,
)
```

##  Considerations

- **Prompt caching:** Switching between fast and standard speed invalidates the prompt cache. Requests at different speeds do not share cached prefixes.
- **Supported models:** Fast mode is supported on Claude Opus 5 and Claude Opus 4.8. See [Supported models](#supported-models).
- **TTFT:** Fast mode's benefits are focused on output tokens per second (OTPS), not time to first token (TTFT).
- **Batch API:** Fast mode is not available with the [Batch API](build-with-claude/batch-processing.md).
- **Priority Tier:** Fast mode is not available with a [Priority Tier](api/service-tiers.md) commitment.
- **Claude Platform on AWS:** Fast mode is not currently available on [Claude Platform on AWS](build-with-claude/claude-platform-on-aws.md).

##  Next steps



[Structured outputs](build-with-claude/structured-outputs.md)

Get validated JSON results from agent workflows.

[Pricing](about-claude/pricing.md)

Learn about Anthropic's pricing structure for models and features.



[Effort](build-with-claude/effort.md)

Control how many tokens Claude uses when responding with the effort parameter, trading off between response thoroughness and token efficiency.



[Streaming messages](build-with-claude/streaming.md)

Stream Messages API responses incrementally with server-sent events, including text, tool use, and extended thinking deltas.

Was this page helpful?



---

*Copyright © Anthropic. All rights reserved.*
