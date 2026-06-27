# Memory Stores

Copy page



C#

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Create(MemoryStoreCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

[MemoryStoreListPageResponse](api/beta/memory_stores.md) Beta.MemoryStores.List(MemoryStoreListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Retrieve(MemoryStoreRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Update(MemoryStoreUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

[BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Delete(MemoryStoreDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md) Beta.MemoryStores.Archive(MemoryStoreArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsDeletedMemoryStore:

Confirmation that a `memory_store` was deleted.

required string ID

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

required Type Type



class BetaManagedAgentsMemoryStore:

A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

required string ID

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string Name

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

string Description

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.Create(MemoryCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

[MemoryListPageResponse](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.List(MemoryListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.Retrieve(MemoryRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

[BetaManagedAgentsMemory](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.Update(MemoryUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

[BetaManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md) Beta.MemoryStores.Memories.Delete(MemoryDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

[MemoryVersionListPageResponse](api/beta/memory_stores/memory_versions.md) Beta.MemoryStores.MemoryVersions.List(MemoryVersionListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) Beta.MemoryStores.MemoryVersions.Retrieve(MemoryVersionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

[BetaManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md) Beta.MemoryStores.MemoryVersions.Redact(MemoryVersionRedactParamsparameters, CancellationTokencancellationToken = default)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

---

*Copyright © Anthropic. All rights reserved.*
