# Delete a memory

Copy page



TypeScript

# Delete a memory

client.beta.memoryStores.memories.delete(stringmemoryID, MemoryDeleteParams { memory\_store\_id, expected\_content\_sha256, betas } params, RequestOptionsoptions?): [BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

Delete a memory

##### ParametersExpand Collapse

memoryID: string



params: MemoryDeleteParams { memory\_store\_id, expected\_content\_sha256, betas } 

memory\_store\_id: string

Path param: Path parameter memory\_store\_id

expected\_content\_sha256?: string

Query param: Query parameter for expected\_content\_sha256

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

##### ReturnsExpand Collapse



BetaManagedAgentsDeletedMemory { id, type } 

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

id: string

ID of the deleted memory (a `mem_...` value).

type: "memory\_deleted"

Delete a memory

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

const betaManagedAgentsDeletedMemory = await client.beta.memoryStores.memories.delete('memory_id', {
  memory_store_id: 'memory_store_id',
});

console.log(betaManagedAgentsDeletedMemory.id);
```

Response 200



```shiki
{
  "id": "id",
  "type": "memory_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "type": "memory_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
