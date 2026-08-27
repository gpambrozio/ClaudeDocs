# List Dreams

Copy page



cURL

# List Dreams

GET/v1/dreams

List Dreams

##### Query parameters



"created\_at[gt]": optional string

Return dreams with `created_at` strictly after this timestamp (exclusive lower bound, RFC 3339). Unset applies no lower bound.

formatdate-time



"created\_at[lt]": optional string

Return dreams with `created_at` strictly before this timestamp (exclusive upper bound, RFC 3339). Unset applies no upper bound.

formatdate-time

include\_archived: optional boolean

Query parameter for include\_archived



limit: optional number

Query parameter for limit

formatint32

page: optional string

Query parameter for page



statuses: optional array of [BetaDreamStatus](api/http/beta/dreams.md)

Filter by lifecycle status. Repeat the parameter to match any of multiple statuses. Empty applies no status filter.

One of the following:

"pending"

"running"

"completed"

"failed"

"canceled"

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

##### Returns



data: array of [BetaDream](api/http/beta/dreams.md) { id, archived\_at, created\_at, 11 more }

id: string



archived\_at: string or null

A timestamp in RFC 3339 format

formatdate-time



created\_at: string

A timestamp in RFC 3339 format

formatdate-time



ended\_at: string or null

A timestamp in RFC 3339 format

formatdate-time



error: [BetaDreamError](api/http/beta/dreams.md) { message, type } or null

Failure detail for a Dream whose `status` is `failed`.

message: string

type: string



inputs: array of [BetaDreamInput](api/http/beta/dreams.md)

One of the following:



BetaDreamMemoryStoreInput object{ memory\_store\_id, type }

An input memory store the dream reads from. The dream never mutates this store unless it is also the destination: with output\_behavior {type: "update\_existing"} the job consolidates this store in place.



memory\_store\_id: string

minLength1

type: "memory\_store"



BetaDreamSessionsInput object{ session\_ids, type }

Input session transcripts the dream reads.

session\_ids: array of string

type: "sessions"

instructions: string or null



model: [BetaDreamModelConfig](api/http/beta/dreams.md) { id, speed }

Model identifier and configuration applied to every pipeline stage. Same wire shape as the Agents API ModelConfig.



id: string

Model identifier, e.g. "claude-opus-5". 1-256 characters.

minLength1

maxLength256



speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

One of the following:

"standard"

"fast"



output\_behavior: [BetaOutputBehavior](api/http/beta/dreams.md)

The default destination: the job creates a new output memory store as a clone of the memory\_store input and writes the consolidated memories into it. The input store is never mutated.

One of the following:



BetaOutputBehaviorCreateNew object{ type }

The default destination: the job creates a new output memory store as a clone of the memory\_store input and writes the consolidated memories into it. The input store is never mutated.

type: "create\_new"



BetaOutputBehaviorUpdateExisting object{ memory\_store\_id, type }

The job writes the consolidated memories into this existing memory store instead of creating one. In EAP the store must be the job's own memory\_store input, so the job consolidates the store in place.



memory\_store\_id: string

minLength1

type: "update\_existing"



outputs: array of [BetaDreamOutput](api/http/beta/dreams.md) { memory\_store\_id, type }

memory\_store\_id: string

type: "memory\_store"

session\_id: string or null



status: [BetaDreamStatus](api/http/beta/dreams.md)

Lifecycle status of a Dream.

One of the following:

"pending"

"running"

"completed"

"failed"

"canceled"

type: "dream"



usage: [BetaDreamUsage](api/http/beta/dreams.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for the dream across every pipeline stage.



cache\_creation\_input\_tokens: number

Total tokens used to create prompt-cache entries (sum of all TTL tiers).

formatint32



cache\_read\_input\_tokens: number

Total tokens read from prompt cache.

formatint32



input\_tokens: number

Total uncached input tokens consumed across every pipeline stage.

formatint32



output\_tokens: number

Total output tokens generated across every pipeline stage.

formatint32

next\_page: string or null

### List Dreams

cURL



```shiki
curl https://api.anthropic.com/v1/dreams \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: dreaming-2026-04-21' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "ended_at": "2019-12-27T18:11:19.117Z",
      "error": {
        "message": "message",
        "type": "type"
      },
      "inputs": [
        {
          "memory_store_id": "x",
          "type": "memory_store"
        }
      ],
      "instructions": "instructions",
      "model": {
        "id": "x",
        "speed": "standard"
      },
      "output_behavior": {
        "type": "create_new"
      },
      "outputs": [
        {
          "memory_store_id": "memory_store_id",
          "type": "memory_store"
        }
      ],
      "session_id": "session_id",
      "status": "pending",
      "type": "dream",
      "usage": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "ended_at": "2019-12-27T18:11:19.117Z",
      "error": {
        "message": "message",
        "type": "type"
      },
      "inputs": [
        {
          "memory_store_id": "x",
          "type": "memory_store"
        }
      ],
      "instructions": "instructions",
      "model": {
        "id": "x",
        "speed": "standard"
      },
      "output_behavior": {
        "type": "create_new"
      },
      "outputs": [
        {
          "memory_store_id": "memory_store_id",
          "type": "memory_store"
        }
      ],
      "session_id": "session_id",
      "status": "pending",
      "type": "dream",
      "usage": {
        "cache_creation_input_tokens": 0,
        "cache_read_input_tokens": 0,
        "input_tokens": 0,
        "output_tokens": 0
      }
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
