# Dreams

Copy page



cURL

# Dreams

##### [Create a Dream](api/beta/dreams/create.md)

POST/v1/dreams

##### [List Dreams](api/beta/dreams/list.md)

GET/v1/dreams

##### [Get a Dream](api/beta/dreams/retrieve.md)

GET/v1/dreams/{dream\_id}

##### [Cancel a Dream](api/beta/dreams/cancel.md)

POST/v1/dreams/{dream\_id}/cancel

##### [Archive a Dream](api/beta/dreams/archive.md)

POST/v1/dreams/{dream\_id}/archive

##### ModelsExpand Collapse



BetaDream object { id, archived\_at, created\_at, 10 more } 

An asynchronous memory-consolidation job that reads a memory store plus a set of session transcripts and writes consolidated memories into a new output memory store. The Dreams API is in research preview: the request and response shapes are volatile and may change without the deprecation period that applies to generally-available endpoints.

id: string

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

ended\_at: string

A timestamp in RFC 3339 format



error: [BetaDreamError](api/beta/dreams.md) { message, type } 

Failure detail for a Dream whose `status` is `failed`.

message: string

type: string



inputs: array of [BetaDreamInput](api/beta/dreams.md)

One of the following:



BetaDreamMemoryStoreInput object { memory\_store\_id, type } 

An input memory store the dream reads from. The dream never mutates this store.

memory\_store\_id: string

type: "memory\_store"



BetaDreamSessionsInput object { session\_ids, type } 

Input session transcripts the dream reads.

session\_ids: array of string

type: "sessions"

instructions: string



model: [BetaDreamModelConfig](api/beta/dreams.md) { id, speed } 

Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

id: string

Model identifier, e.g. "claude-opus-4-7". 1-256 characters.



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



outputs: array of [BetaDreamOutput](api/beta/dreams.md) { memory\_store\_id, type } 

memory\_store\_id: string

type: "memory\_store"

session\_id: string



status: [BetaDreamStatus](api/beta/dreams.md)

Lifecycle status of a Dream.

One of the following:

"pending"

"running"

"completed"

"failed"

"canceled"

type: "dream"



usage: [BetaDreamUsage](api/beta/dreams.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for the dream across every pipeline stage.

cache\_creation\_input\_tokens: number

Total tokens used to create prompt-cache entries (sum of all TTL tiers).

cache\_read\_input\_tokens: number

Total tokens read from prompt cache.

input\_tokens: number

Total uncached input tokens consumed across every pipeline stage.

output\_tokens: number

Total output tokens generated across every pipeline stage.



BetaDreamError object { message, type } 

Failure detail for a Dream whose `status` is `failed`.

message: string

type: string



BetaDreamInput = [BetaDreamMemoryStoreInput](api/beta/dreams.md) { memory\_store\_id, type }  or [BetaDreamSessionsInput](api/beta/dreams.md) { session\_ids, type } 

An input memory store the dream reads from. The dream never mutates this store.

One of the following:



BetaDreamMemoryStoreInput object { memory\_store\_id, type } 

An input memory store the dream reads from. The dream never mutates this store.

memory\_store\_id: string

type: "memory\_store"



BetaDreamSessionsInput object { session\_ids, type } 

Input session transcripts the dream reads.

session\_ids: array of string

type: "sessions"



BetaDreamMemoryStoreInput object { memory\_store\_id, type } 

An input memory store the dream reads from. The dream never mutates this store.

memory\_store\_id: string

type: "memory\_store"



BetaDreamMemoryStoreOutput object { memory\_store\_id, type } 

An output memory store the dream writes consolidated memories into.

memory\_store\_id: string

type: "memory\_store"



BetaDreamModelConfig object { id, speed } 

Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.

id: string

Model identifier, e.g. "claude-opus-4-7". 1-256 characters.



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



BetaDreamModelConfigParam object { id, speed } 

Model identifier and configuration applied to every pipeline stage.

id: string

Model identifier, e.g. "claude-opus-4-7". 1-256 characters.



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



BetaDreamOutput object { memory\_store\_id, type } 

An output memory store the dream writes consolidated memories into.

memory\_store\_id: string

type: "memory\_store"



BetaDreamSessionsInput object { session\_ids, type } 

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

BetaDreamUsage object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, output\_tokens } 

Cumulative token usage for the dream across every pipeline stage.

cache\_creation\_input\_tokens: number

Total tokens used to create prompt-cache entries (sum of all TTL tiers).

cache\_read\_input\_tokens: number

Total tokens read from prompt cache.

input\_tokens: number

Total uncached input tokens consumed across every pipeline stage.

output\_tokens: number

Total output tokens generated across every pipeline stage.

---

*Copyright © Anthropic. All rights reserved.*
