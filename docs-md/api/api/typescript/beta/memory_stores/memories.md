# Memories

Copy page

TypeScript

# Memories

##### [CreateMemory](api/beta/memory_stores/memories/create.md)

client.beta.memoryStores.memories.create(stringmemoryStoreID, MemoryCreateParams { content, path\_, view, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [ListMemories](api/beta/memory_stores/memories/list.md)

client.beta.memoryStores.memories.list(stringmemoryStoreID, MemoryListParams { depth, limit, order, 5 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryListItem](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [GetMemory](api/beta/memory_stores/memories/retrieve.md)

client.beta.memoryStores.memories.retrieve(stringmemoryID, MemoryRetrieveParams { memory\_store\_id, view, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [UpdateMemory](api/beta/memory_stores/memories/update.md)

client.beta.memoryStores.memories.update(stringmemoryID, MemoryUpdateParams { memory\_store\_id, view, content, 3 more } params, RequestOptionsoptions?): [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [DeleteMemory](api/beta/memory_stores/memories/delete.md)

client.beta.memoryStores.memories.delete(stringmemoryID, MemoryDeleteParams { memory\_store\_id, expected\_content\_sha256, betas } params, RequestOptionsoptions?): [BetaManagedAgentsDeletedMemory](api/beta.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

BetaManagedAgentsContentSha256Precondition { type, content\_sha256 }

type: "content\_sha256"

content\_sha256?: string

BetaManagedAgentsDeletedMemory { id, type }

id: string

type: "memory\_deleted"

BetaManagedAgentsMemory { id, content\_sha256, content\_size\_bytes, 7 more }

id: string

content\_sha256: string

content\_size\_bytes: number

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

memory\_version\_id: string

path: string

type: "memory"

updated\_at: string

A timestamp in RFC 3339 format

content?: string | null

BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }  | [BetaManagedAgentsMemoryPrefix](api/beta.md) { path, type }

Accepts one of the following:

BetaManagedAgentsMemory { id, content\_sha256, content\_size\_bytes, 7 more }

id: string

content\_sha256: string

content\_size\_bytes: number

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

memory\_version\_id: string

path: string

type: "memory"

updated\_at: string

A timestamp in RFC 3339 format

content?: string | null

BetaManagedAgentsMemoryPrefix { path, type }

path: string

type: "memory\_prefix"

BetaManagedAgentsMemoryPathConflictError { type, conflicting\_memory\_id, conflicting\_path, message }

type: "memory\_path\_conflict\_error"

conflicting\_memory\_id?: string

conflicting\_path?: string

message?: string

BetaManagedAgentsMemoryPreconditionFailedError { type, message }

type: "memory\_precondition\_failed\_error"

message?: string

BetaManagedAgentsMemoryPrefix { path, type }

path: string

type: "memory\_prefix"

BetaManagedAgentsMemoryView = "basic" | "full"

MemoryView enum

Accepts one of the following:

"basic"

"full"

BetaManagedAgentsPrecondition { type, content\_sha256 }

type: "content\_sha256"

content\_sha256?: string

---

*Copyright © Anthropic. All rights reserved.*
