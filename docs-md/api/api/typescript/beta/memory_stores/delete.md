# Delete a memory store

Copy page

TypeScript

# Delete a memory store

client.beta.memoryStores.delete(stringmemoryStoreID, MemoryStoreDeleteParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeletedMemoryStore](api/beta.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}

Delete a memory store

##### ParametersExpand Collapse

memoryStoreID: string

params: MemoryStoreDeleteParams { betas }

betas?: Array<[AnthropicBeta](api/beta.md)>

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 20 more

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

"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

BetaManagedAgentsDeletedMemoryStore { id, type }

Confirmation that a `memory_store` was deleted.

id: string

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

type: "memory\_store\_deleted"

Delete a memory store

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeletedMemoryStore = await client.beta.memoryStores.delete(
  'memory_store_id',
);

console.log(betaManagedAgentsDeletedMemoryStore.id);
```

Response 200

```shiki
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
