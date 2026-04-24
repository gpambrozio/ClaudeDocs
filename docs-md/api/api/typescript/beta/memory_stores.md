# Memory Stores

Copy page

TypeScript

# Memory Stores

##### [CreateMemoryStore](api/beta/memory_stores/create.md)

client.beta.memoryStores.create(MemoryStoreCreateParams { name, description, metadata, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

POST/v1/memory\_stores

##### [ListMemoryStores](api/beta/memory_stores/list.md)

client.beta.memoryStores.list(MemoryStoreListParams { createdAtGte, createdAtLte, include\_archived, 3 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more } >

GET/v1/memory\_stores

##### [GetMemoryStore](api/beta/memory_stores/retrieve.md)

client.beta.memoryStores.retrieve(stringmemoryStoreID, MemoryStoreRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

GET/v1/memory\_stores/{memory\_store\_id}

##### [UpdateMemoryStore](api/beta/memory_stores/update.md)

client.beta.memoryStores.update(stringmemoryStoreID, MemoryStoreUpdateParams { description, metadata, name, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}

##### [DeleteMemoryStore](api/beta/memory_stores/delete.md)

client.beta.memoryStores.delete(stringmemoryStoreID, MemoryStoreDeleteParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeletedMemoryStore](api/beta.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [ArchiveMemoryStore](api/beta/memory_stores/archive.md)

client.beta.memoryStores.archive(stringmemoryStoreID, MemoryStoreArchiveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

BetaManagedAgentsDeletedMemoryStore { id, type }

id: string

type: "memory\_store\_deleted"

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

#### Memory StoresMemories

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

#### Memory StoresMemory Versions

##### [ListMemoryVersions](api/beta/memory_stores/memory_versions/list.md)

client.beta.memoryStores.memoryVersions.list(stringmemoryStoreID, MemoryVersionListParams { api\_key\_id, createdAtGte, createdAtLte, 7 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more } >

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [GetMemoryVersion](api/beta/memory_stores/memory_versions/retrieve.md)

client.beta.memoryStores.memoryVersions.retrieve(stringmemoryVersionID, MemoryVersionRetrieveParams { memory\_store\_id, view, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [RedactMemoryVersion](api/beta/memory_stores/memory_versions/redact.md)

client.beta.memoryStores.memoryVersions.redact(stringmemoryVersionID, MemoryVersionRedactParams { memory\_store\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  | [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  | [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

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

BetaManagedAgentsAPIActor { api\_key\_id, type }

api\_key\_id: string

type: "api\_actor"

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

BetaManagedAgentsMemoryVersionOperation = "created" | "modified" | "deleted"

MemoryVersionOperation enum

Accepts one of the following:

"created"

"modified"

"deleted"

BetaManagedAgentsSessionActor { session\_id, type }

session\_id: string

type: "session\_actor"

BetaManagedAgentsUserActor { type, user\_id }

type: "user\_actor"

user\_id: string

---

*Copyright © Anthropic. All rights reserved.*
