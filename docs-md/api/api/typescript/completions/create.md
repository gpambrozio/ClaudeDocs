# Create a Text Completion

Copy page



TypeScript

# Create a Text Completion

client.completions.create(CompletionCreateParamsparams, RequestOptionsoptions?): [Completion](api/completions.md) { id, completion, model, 2 more }  | Stream<[Completion](api/completions.md) { id, completion, model, 2 more } >

POST/v1/complete

[Legacy] Create a Text Completion.

The Text Completions API is a legacy API. We recommend using the [Messages API](api/messages.md) going forward.

Future models and features will not be compatible with Text Completions. See our [migration guide](build-with-claude/working-with-messages.md) for guidance in migrating from Text Completions to Messages.

##### ParametersExpand Collapse



CompletionCreateParams = CompletionCreateParamsNonStreaming { stream }  | CompletionCreateParamsStreaming { stream } 



CompletionCreateParamsBase { max\_tokens\_to\_sample, model, prompt, 7 more } 



max\_tokens\_to\_sample: number

Body param: The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.

minimum1



model: [Model](api/messages.md)

Body param: The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



prompt: string

Body param: The prompt that you want Claude to complete.

For proper response generation you will need to format your prompt using alternating `

Human:`and`

Assistant:` conversational turns. For example:

```
"

Human: {userQuestion}

Assistant:"
```

See [prompt validation](build-with-claude/working-with-messages.md) and our guide to [prompt design](build-with-claude/prompt-engineering/overview.md) for more details.

minLength1



metadata?: [Metadata](api/messages.md) { user\_id } 

Body param: An object describing metadata about the request.



user\_id?: string | null

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



stop\_sequences?: Array<string>

Body param: Sequences that will cause the model to stop generating.

Our models stop on `"

Human:"`, and may include additional built-in stop sequences in the future. By providing the stop\_sequences parameter, you may include additional strings that will cause the model to stop generating.



stream?: false

Body param: Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.



betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

One of the following:

(string & {})



"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 26 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

"agent-memory-2026-07-22"



temperature?: number⁠Deprecated

Body param: Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.

maximum1

minimum0



top\_k?: number⁠Deprecated

Body param: Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.

minimum0



top\_p?: number⁠Deprecated

Body param: Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

maximum1

minimum0



CompletionCreateParamsNonStreaming extends CompletionCreateParamsBase { max\_tokens\_to\_sample, model, prompt, 7 more }  { stream } 



stream?: false

Body param: Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.



CompletionCreateParamsStreaming extends CompletionCreateParamsBase { max\_tokens\_to\_sample, model, prompt, 7 more }  { stream } 



stream: true

Body param: Whether to incrementally stream the response using server-sent events.

See [streaming](build-with-claude/streaming.md) for details.

##### ReturnsExpand Collapse



Completion { id, completion, model, 2 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.

completion: string

The resulting completion up to and excluding the stop sequences.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



stop\_reason: string | null

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum



type: "completion"

Object type.

For Text Completions, this is always `"completion"`.



Completion { id, completion, model, 2 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.

completion: string

The resulting completion up to and excluding the stop sequences.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



"claude-sonnet-5" | "claude-fable-5" | "claude-mythos-5" | 13 more

"claude-sonnet-5"

High-performance model for coding and agents

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

(string & {})



stop\_reason: string | null

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum



type: "completion"

Object type.

For Text Completions, this is always `"completion"`.

Create a Text Completion

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const completion = await client.completions.create({
  max_tokens_to_sample: 256,
  model: 'claude-2.1',
  prompt: '\n\nHuman: Hello, world!\n\nAssistant:',
});

console.log(completion.id);
```

Response 200



```shiki
{
  "id": "compl_018CKm6gsux7P8yMcwZbeCPw",
  "completion": " Hello! My name is Claude.",
  "model": "claude-2.1",
  "stop_reason": "stop_sequence",
  "type": "completion"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "compl_018CKm6gsux7P8yMcwZbeCPw",
  "completion": " Hello! My name is Claude.",
  "model": "claude-2.1",
  "stop_reason": "stop_sequence",
  "type": "completion"
}
```

---

*Copyright © Anthropic. All rights reserved.*
