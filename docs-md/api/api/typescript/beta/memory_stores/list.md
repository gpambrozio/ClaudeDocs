# ListMemoryStores

Copy page

TypeScript

# ListMemoryStores

client.beta.memoryStores.list(MemoryStoreListParams { createdAtGte, createdAtLte, include\_archived, 3 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more } >

GET/v1/memory\_stores

ListMemoryStores

##### ParametersExpand Collapse

params: MemoryStoreListParams { createdAtGte, createdAtLte, include\_archived, 3 more }

createdAtGte?: string

Query param: Return stores created at or after this time (inclusive).

createdAtLte?: string

Query param: Return stores created at or before this time (inclusive).

include\_archived?: boolean

Query param: Query parameter for include\_archived

limit?: number

Query param: Query parameter for limit

page?: string

Query param: Query parameter for page

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

BetaManagedAgentsMemoryStore { id, type, archived\_at, 5 more }

id: string

type: "memory\_store"

archived\_at?: string | null

A timestamp in RFC 3339 format

created\_at?: string

A timestamp in RFC 3339 format

description?: string

metadata?: Record<string, string>

name?: string

updated\_at?: string

A timestamp in RFC 3339 format

ListMemoryStores

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsMemoryStore of client.beta.memoryStores.list()) {
  console.log(betaManagedAgentsMemoryStore.id);
}
```

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "type": "memory_store",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "updated_at": "2019-12-27T18:11:19.117Z"
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
      "type": "memory_store",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
