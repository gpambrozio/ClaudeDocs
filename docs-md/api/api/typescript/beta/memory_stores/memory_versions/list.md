# ListMemoryVersions

Copy page

TypeScript

# ListMemoryVersions

client.beta.memoryStores.memoryVersions.list(stringmemoryStoreID, MemoryVersionListParams { api\_key\_id, createdAtGte, createdAtLte, 7 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more } >

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

ListMemoryVersions

##### ParametersExpand Collapse

memoryStoreID: string

params: MemoryVersionListParams { api\_key\_id, createdAtGte, createdAtLte, 7 more }

api\_key\_id?: string

Query param: Query parameter for api\_key\_id

createdAtGte?: string

Query param: Return versions created at or after this time (inclusive).

createdAtLte?: string

Query param: Return versions created at or before this time (inclusive).

limit?: number

Query param: Query parameter for limit

memory\_id?: string

Query param: Query parameter for memory\_id

operation?: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

Query param: Query parameter for operation

Accepts one of the following:

"created"

"modified"

"deleted"

page?: string

Query param: Query parameter for page

session\_id?: string

Query param: Query parameter for session\_id

view?: [BetaManagedAgentsMemoryView](api/beta.md)

Query param: Query parameter for view

Accepts one of the following:

"basic"

"full"

betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 19 more

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

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

BetaManagedAgentsMemoryVersion { id, created\_at, memory\_id, 10 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

memory\_id: string

memory\_store\_id: string

operation: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

MemoryVersionOperation enum

Accepts one of the following:

"created"

"modified"

"deleted"

type: "memory\_version"

content?: string | null

content\_sha256?: string | null

content\_size\_bytes?: number | null

created\_by?: [BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

BetaManagedAgentsSessionActor { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsUserActor { type, user\_id }

type: "user\_actor"

user\_id: string

path?: string | null

redacted\_at?: string | null

A timestamp in RFC 3339 format

redacted\_by?: [BetaManagedAgentsActor](api/beta.md)

Accepts one of the following:

BetaManagedAgentsSessionActor { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

BetaManagedAgentsUserActor { type, user\_id }

type: "user\_actor"

user\_id: string

ListMemoryVersions

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryVersion of client.beta.memoryStores.memoryVersions.list(
  'memory_store_id',
)) {
  console.log(betaManagedAgentsMemoryVersion.id);
}
```

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_id": "memory_id",
      "memory_store_id": "memory_store_id",
      "operation": "created",
      "type": "memory_version",
      "content": "content",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_by": {
        "session_id": "x",
        "type": "session_actor"
      },
      "path": "path",
      "redacted_at": "2019-12-27T18:11:19.117Z",
      "redacted_by": {
        "session_id": "x",
        "type": "session_actor"
      }
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
