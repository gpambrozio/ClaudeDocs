# Completions

Copy page



cURL

# Completions

##### [Create a Text Completion](api/http/completions/create.md)

POST/v1/complete

##### Models



Completion object{ id, completion, model, 2 more }



id: string

Unique object identifier.

The format and length of IDs may change over time.

completion: string

The resulting completion up to and excluding the stop sequences.



model: [Model](api/http/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



stop\_reason: string or null

The reason that we stopped.

This may be one the following values:

- `"stop_sequence"`: we reached a stop sequence — either provided by you via the `stop_sequences` parameter, or a stop sequence built into the model
- `"max_tokens"`: we exceeded `max_tokens_to_sample` or the model's maximum



type: "completion"

Object type.

For Text Completions, this is always `"completion"`.

defaultcompletion

---

*Copyright © Anthropic. All rights reserved.*
