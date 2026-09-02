# Dreams

Copy page



cURL

# Dreams

##### [Create a Dream](api/http/beta/dreams/create.md)

POST/v1/dreams

##### [List Dreams](api/http/beta/dreams/list.md)

GET/v1/dreams

##### [Get a Dream](api/http/beta/dreams/retrieve.md)

GET/v1/dreams/{dream\_id}

##### [Cancel a Dream](api/http/beta/dreams/cancel.md)

POST/v1/dreams/{dream\_id}/cancel

##### [Archive a Dream](api/http/beta/dreams/archive.md)

POST/v1/dreams/{dream\_id}/archive

##### Models



BetaDream object{ id, archived\_at, created\_at, 11 more }

An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into an output memory store — a new store by default, or an existing store chosen via output\_behavior. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.



BetaDreamError object{ message, type }

Failure detail for a Dream whose `status` is `failed`.

message: string

type: string



BetaDreamInput = [BetaDreamMemoryStoreInput](api/http/beta/dreams.md) { memory\_store\_id, type } or [BetaDreamSessionsInput](api/http/beta/dreams.md) { session\_ids, type }

An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output\_behavior {type: "update\_existing"} the job consolidates this store in place.

One of the following:



BetaDreamMemoryStoreInput object{ memory\_store\_id, type }

An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output\_behavior {type: "update\_existing"} the job consolidates this store in place.



memory\_store\_id: string

minLength1

type: "memory\_store"



BetaDreamSessionsInput object{ session\_ids, type }

Input session transcripts the dream reads.

session\_ids: array of string

type: "sessions"



BetaDreamMemoryStoreInput object{ memory\_store\_id, type }

An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output\_behavior {type: "update\_existing"} the job consolidates this store in place.



memory\_store\_id: string

minLength1

type: "memory\_store"



BetaDreamMemoryStoreOutput object{ memory\_store\_id, type }

An output memory store the dream writes consolidated memories into.

memory\_store\_id: string

type: "memory\_store"



BetaDreamModelConfig object{ id, speed }

Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.



id: string

Model identifier, e.g. "claude-opus-5". 1-256 characters.

minLength1

maxLength256



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



BetaDreamModelConfigParam object{ id, speed }

Model identifier and configuration applied to every pipeline stage.



id: string

Model identifier, e.g. "claude-opus-5". 1-256 characters.

minLength1

maxLength256



speed: optional "standard" or "fast" or null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



BetaDreamOutput object{ memory\_store\_id, type }

An output memory store the dream writes consolidated memories into.

memory\_store\_id: string

type: "memory\_store"



BetaDreamSessionsInput object{ session\_ids, type }

Input session transcripts the dream reads.

session\_ids: array of string

type: "sessions"



BetaDreamStatus = "pending" or "running" or "completed" or 2 more

Lifecycle status of a Dream.

One of the following:

"pending"

"running"

"completed"

"failed"

"canceled"



BetaDreamUsage object{ cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for the dream across every pipeline stage.



cache\_creation\_input\_tokens: number

Total tokens used to create prompt-cache entries (sum of all TTL tiers).

formatint32



cache\_read\_input\_tokens: number

Total tokens read from prompt cache.

formatint32



input\_tokens: number

Total uncached input tokens consumed across every pipeline stage.

formatint32



output\_tokens: number

Total output tokens generated across every pipeline stage.

formatint32



BetaDreamingError = [BetaInvalidRequestError](api/http/beta.md) { message, type } or [BetaAuthenticationError](api/http/beta.md) { message, type } or [BetaBillingError](api/http/beta.md) { message, type } or 7 more

The `output_behavior.memory_store_id` target is still held by a prior `{type: "update_existing"}` dream — one that is `pending` or `running`, or was canceled with its final writes still landing. Rarely the named dream has just finished (`completed`/`failed`) and its execution is still closing; an immediate retry then almost always succeeds. The message names the holding dream when the server can identify it (rarely omitted); poll it to a terminal state or cancel it, then retry. Carried with `x-should-retry: false`.

One of the following:



BetaOutputBehavior = [BetaOutputBehaviorCreateNew](api/http/beta/dreams.md) { type } or [BetaOutputBehaviorUpdateExisting](api/http/beta/dreams.md) { memory\_store\_id, type }

The default destination: the job creates a new output memory store as a clone of the memory\_store input and writes the consolidated memories into it. The input store is never mutated.

One of the following:



BetaOutputBehaviorCreateNew object{ type }

The default destination: the job creates a new output memory store as a clone of the memory\_store input and writes the consolidated memories into it. The input store is never mutated.

type: "create\_new"



BetaOutputBehaviorUpdateExisting object{ memory\_store\_id, type }

The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory\_store input, so the job consolidates the store in place.



memory\_store\_id: string

minLength1

type: "update\_existing"



BetaOutputBehaviorCreateNew object{ type }

The default destination: the job creates a new output memory store as a clone of the memory\_store input and writes the consolidated memories into it. The input store is never mutated.

type: "create\_new"



BetaOutputBehaviorUpdateExisting object{ memory\_store\_id, type }

The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory\_store input, so the job consolidates the store in place.



memory\_store\_id: string

minLength1

type: "update\_existing"



BetaTargetStoreHeldError object{ type, message }

The `output_behavior.memory_store_id` target is still held by a prior `{type: "update_existing"}` dream — one that is `pending` or `running`, or was canceled with its final writes still landing. Rarely the named dream has just finished (`completed`/`failed`) and its execution is still closing; an immediate retry then almost always succeeds. The message names the holding dream when the server can identify it (rarely omitted); poll it to a terminal state or cancel it, then retry. Carried with `x-should-retry: false`.

type: "conflict\_error"

message: optional string

Human-readable description of the conflict, naming the dream that holds the target store when the server can identify it.

---

*Copyright © Anthropic. All rights reserved.*
