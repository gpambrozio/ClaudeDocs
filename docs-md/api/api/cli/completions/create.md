# Create a Text Completion

Copy page



CLI

# Create a Text Completion

$ ant completions create

POST/v1/complete

[Legacy] Create a Text Completion.

The Text Completions API is a legacy API. We recommend using the [Messages API](api/messages.md) going forward.

Future models and features will not be compatible with Text Completions. See our [migration guide](build-with-claude/working-with-messages.md) for guidance in migrating from Text Completions to Messages.

##### ParametersExpand Collapse



--max-tokens-to-sample: number

Body param: The maximum number of tokens to generate before stopping.

Note that our models may stop *before* reaching this maximum. This parameter only specifies the absolute maximum number of tokens to generate.



--model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 13 more or string

Body param: The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.



--prompt: string

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

--metadata: optional object { user\_id } 

Body param: An object describing metadata about the request.



--stop-sequence: optional array of string

Body param: Sequences that will cause the model to stop generating.

Our models stop on `"

Human:"`, and may include additional built-in stop sequences in the future. By providing the stop\_sequences parameter, you may include additional strings that will cause the model to stop generating.



Deprecated--temperature: optional number

Body param: Amount of randomness injected into the response.

Deprecated. Models released after Claude Opus 4.6 do not support setting temperature. A value of 1.0 of will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

Defaults to `1.0`. Ranges from `0.0` to `1.0`. Use `temperature` closer to `0.0` for analytical / multiple choice, and closer to `1.0` for creative and generative tasks.

Note that even with `temperature` of `0.0`, the results will not be fully deterministic.



Deprecated--top-k: optional number

Body param: Only sample from the top K options for each subsequent token.

Deprecated. Models released after Claude Opus 4.6 do not accept top\_k; any value will be rejected with a 400 error.

Used to remove "long tail" low probability responses. [Learn more technical details here](https://towardsdatascience.com/how-to-sample-from-language-models-682bceb97277).

Recommended for advanced use cases only.



Deprecated--top-p: optional number

Body param: Use nucleus sampling.

Deprecated. Models released after Claude Opus 4.6 do not support setting top\_p. A value >= 0.99 will be accepted for backwards compatibility, all other values will be rejected with a 400 error.

In nucleus sampling, we compute the cumulative distribution over all the options for each subsequent token in decreasing probability order and cut it off once it reaches a particular probability specified by `top_p`.

Recommended for advanced use cases only.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



completion: object { id, completion, model, 2 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.

completion: string

The resulting completion up to and excluding the stop sequences.



model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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



stop\_reason: string

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum



type: "completion"

Object type.

For Text Completions, this is always `"completion"`.



completion: object { id, completion, model, 2 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.

completion: string

The resulting completion up to and excluding the stop sequences.



model: "claude-sonnet-5" or "claude-fable-5" or "claude-mythos-5" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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



stop\_reason: string

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum



type: "completion"

Object type.

For Text Completions, this is always `"completion"`.

Create a Text Completion

CLI

```shiki
ant completions create \
  --api-key my-anthropic-api-key \
  --max-tokens-to-sample 256 \
  --model claude-sonnet-5 \
  --prompt '

Human: Hello, world!

Assistant:'
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
