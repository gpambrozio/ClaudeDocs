# Completions

Copy page

Java

# Completions

##### [Create a Text Completion](api/completions/create.md)

[Completion](api/completions.md) completions().create(CompletionCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/complete

##### ModelsExpand Collapse

class Completion:

String id

Unique object identifier.

The format and length of IDs may change over time.

String completion

The resulting completion up to and excluding the stop sequences.

Model model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

CLAUDE\_OPUS\_4\_6("claude-opus-4-6")

Most intelligent model for building agents and coding

CLAUDE\_SONNET\_4\_6("claude-sonnet-4-6")

Best combination of speed and intelligence

CLAUDE\_HAIKU\_4\_5("claude-haiku-4-5")

Fastest model with near-frontier intelligence

CLAUDE\_HAIKU\_4\_5\_20251001("claude-haiku-4-5-20251001")

Fastest model with near-frontier intelligence

CLAUDE\_OPUS\_4\_5("claude-opus-4-5")

Premium model combining maximum intelligence with practical performance

CLAUDE\_OPUS\_4\_5\_20251101("claude-opus-4-5-20251101")

Premium model combining maximum intelligence with practical performance

CLAUDE\_SONNET\_4\_5("claude-sonnet-4-5")

High-performance model for agents and coding

CLAUDE\_SONNET\_4\_5\_20250929("claude-sonnet-4-5-20250929")

High-performance model for agents and coding

CLAUDE\_OPUS\_4\_1("claude-opus-4-1")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_1\_20250805("claude-opus-4-1-20250805")

Exceptional model for specialized complex tasks

CLAUDE\_OPUS\_4\_0("claude-opus-4-0")

Powerful model for complex tasks

CLAUDE\_OPUS\_4\_20250514("claude-opus-4-20250514")

Powerful model for complex tasks

CLAUDE\_SONNET\_4\_0("claude-sonnet-4-0")

High-performance model with extended thinking

CLAUDE\_SONNET\_4\_20250514("claude-sonnet-4-20250514")

High-performance model with extended thinking

CLAUDE\_3\_HAIKU\_20240307("claude-3-haiku-20240307")

Fast and cost-effective model

Optional<String> stopReason

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

JsonValue; type "completion"constant"completion"constant

Object type.

For Text Completions, this is always `"completion"`.

---

*Copyright © Anthropic. All rights reserved.*
