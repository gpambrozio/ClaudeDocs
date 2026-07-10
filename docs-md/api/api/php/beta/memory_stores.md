# Memory Stores

Copy page



PHP

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

$client->beta->memoryStores->create(string name, ?string description, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

$client->beta->memoryStores->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)>

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

$client->beta->memoryStores->retrieve(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

$client->beta->memoryStores->update(string memoryStoreID, ?string description, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

$client->beta->memoryStores->archive(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse



[BetaManagedAgentsDeletedMemoryStore](api/beta/memory_stores.md)

string id

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

Type type



[BetaManagedAgentsMemoryStore](api/beta/memory_stores.md)

string id

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

\Datetime createdAt

A timestamp in RFC 3339 format

string name

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?\Datetime archivedAt

A timestamp in RFC 3339 format

?string description

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

?array<string,string> metadata

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta/memory_stores/memories.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?string page, ?string pathPrefix, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryListItem](api/beta/memory_stores/memories.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

$client->beta->memoryStores->memories->retrieve(string memoryID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta/memory_stores/memories.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

$client->beta->memoryStores->memories->update(string memoryID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?string content, ?string path, ?[ManagedAgentsPrecondition](api/beta/memory_stores/memories.md) precondition, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta/memory_stores/memories.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedMemory](api/beta/memory_stores/memories.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?[ManagedAgentsMemoryVersionOperation](api/beta/memory_stores/memory_versions.md) operation, ?string page, ?string sessionID, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

$client->beta->memoryStores->memoryVersions->retrieve(string memoryVersionID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta/memory_stores/memories.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

$client->beta->memoryStores->memoryVersions->redact(string memoryVersionID, string memoryStoreID, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta/memory_stores/memory_versions.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

---

*Copyright © Anthropic. All rights reserved.*
