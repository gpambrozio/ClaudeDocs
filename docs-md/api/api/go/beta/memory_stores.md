# Memory Stores

Copy page



Go

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

client.Beta.MemoryStores.New(ctx, params) (\*[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md), error)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

client.Beta.MemoryStores.List(ctx, params) (\*PageCursor[[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)], error)

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

client.Beta.MemoryStores.Get(ctx, memoryStoreID, query) (\*[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md), error)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

client.Beta.MemoryStores.Update(ctx, memoryStoreID, params) (\*[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md), error)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

client.Beta.MemoryStores.Delete(ctx, memoryStoreID, body) (\*[BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md), error)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

client.Beta.MemoryStores.Archive(ctx, memoryStoreID, body) (\*[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse



type BetaManagedAgentsDeletedMemoryStore struct{…}

Confirmation that a `memory_store` was deleted.

ID string

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

Type BetaManagedAgentsDeletedMemoryStoreType



type BetaManagedAgentsMemoryStore struct{…}

A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

ID string

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

CreatedAt Time

A timestamp in RFC 3339 format

Name string

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

Type BetaManagedAgentsMemoryStoreType

UpdatedAt Time

A timestamp in RFC 3339 format

ArchivedAt TimeOptional

A timestamp in RFC 3339 format

Description stringOptional

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

Metadata map[string, string]Optional

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

client.Beta.MemoryStores.Memories.New(ctx, memoryStoreID, params) (\*[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

client.Beta.MemoryStores.Memories.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryListItemUnion](api/beta/memory_stores/memories.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

client.Beta.MemoryStores.Memories.Get(ctx, memoryID, params) (\*[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

client.Beta.MemoryStores.Memories.Update(ctx, memoryID, params) (\*[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

client.Beta.MemoryStores.Memories.Delete(ctx, memoryID, params) (\*[BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md), error)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

client.Beta.MemoryStores.MemoryVersions.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

client.Beta.MemoryStores.MemoryVersions.Redact(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

---

*Copyright © Anthropic. All rights reserved.*
