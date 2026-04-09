# Completions

Copy page

CLI

# Completions

##### [Create a Text Completion](api/completions/create.md)

$ ant completions create

POST/v1/complete

##### ModelsExpand Collapse

completion: object { id, completion, model, 2 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

completion: string

The resulting completion up to and excluding the stop sequences.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

stop\_reason: string

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

type: "completion"

Object type.

For Text Completions, this is always `"completion"`.

---

*Copyright © Anthropic. All rights reserved.*
