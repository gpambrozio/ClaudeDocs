# Completions

Copy page

Go

# Completions

##### [Create a Text Completion](api/completions/create.md)

client.Completions.New(ctx, params) (\*[Completion](api/completions.md), error)

post/v1/complete

##### ModelsExpand Collapse

type Completion struct{…}

ID string

Unique object identifier.

The format and length of IDs may change over time.

Completion string

The resulting completion up to and excluding the stop sequences.

Model Model

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type Model string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const ModelClaudeOpus4\_6 Model = "claude-opus-4-6"

Most intelligent model for building agents and coding

const ModelClaudeOpus4\_5\_20251101 Model = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const ModelClaudeOpus4\_5 Model = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const ModelClaude3\_7SonnetLatest Model = "claude-3-7-sonnet-latest"

High-performance model with early extended thinking

const ModelClaude3\_7Sonnet20250219 Model = "claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

const ModelClaude3\_5HaikuLatest Model = "claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

const ModelClaude3\_5Haiku20241022 Model = "claude-3-5-haiku-20241022"

Our fastest model

const ModelClaudeHaiku4\_5 Model = "claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeHaiku4\_5\_20251001 Model = "claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

const ModelClaudeSonnet4\_20250514 Model = "claude-sonnet-4-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4\_0 Model = "claude-sonnet-4-0"

High-performance model with extended thinking

const ModelClaude4Sonnet20250514 Model = "claude-4-sonnet-20250514"

High-performance model with extended thinking

const ModelClaudeSonnet4\_5 Model = "claude-sonnet-4-5"

Our best model for real-world agents and coding

const ModelClaudeSonnet4\_5\_20250929 Model = "claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

const ModelClaudeOpus4\_0 Model = "claude-opus-4-0"

Our most capable model

const ModelClaudeOpus4\_20250514 Model = "claude-opus-4-20250514"

Our most capable model

const ModelClaude4Opus20250514 Model = "claude-4-opus-20250514"

Our most capable model

const ModelClaudeOpus4\_1\_20250805 Model = "claude-opus-4-1-20250805"

Our most capable model

const ModelClaude3OpusLatest Model = "claude-3-opus-latest"

Excels at writing and complex tasks

const ModelClaude\_3\_Opus\_20240229 Model = "claude-3-opus-20240229"

Excels at writing and complex tasks

const ModelClaude\_3\_Haiku\_20240307 Model = "claude-3-haiku-20240307"

Our previous most fast and cost-effective

string

StopReason string

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum

Type Completion

Object type.

For Text Completions, this is always `"completion"`.

Accepts one of the following:

const CompletionCompletion Completion = "completion"

---

*Copyright © Anthropic. All rights reserved.*
