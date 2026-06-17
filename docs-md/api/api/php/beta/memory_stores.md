# Memory Stores

Copy page



PHP

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

$client->beta->memoryStores->create(string name, ?string description, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

$client->beta->memoryStores->list(?\Datetime createdAtGte, ?\Datetime createdAtLte, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsMemoryStore](api/beta.md)>

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

$client->beta->memoryStores->retrieve(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

$client->beta->memoryStores->update(string memoryStoreID, ?string description, ?array<string,string> metadata, ?string name, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

$client->beta->memoryStores->delete(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedMemoryStore](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

$client->beta->memoryStores->archive(string memoryStoreID, ?list<AnthropicBeta> betas): [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse



[BetaManagedAgentsDeletedMemoryStore](api/beta.md)

string id

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

Type type



[BetaManagedAgentsMemoryStore](api/beta.md)

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

$client->beta->memoryStores->memories->create(string memoryStoreID, ?string content, string path, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

$client->beta->memoryStores->memories->list(string memoryStoreID, ?int depth, ?int limit, ?[Order](api/beta/memory_stores/memories/list.md) order, ?string orderBy, ?string page, ?string pathPrefix, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryListItem](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

$client->beta->memoryStores->memories->retrieve(string memoryID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

$client->beta->memoryStores->memories->update(string memoryID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?string content, ?string path, ?[ManagedAgentsPrecondition](api/beta.md) precondition, ?list<AnthropicBeta> betas): [ManagedAgentsMemory](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

$client->beta->memoryStores->memories->delete(string memoryID, string memoryStoreID, ?string expectedContentSha256, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedMemory](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse



[ManagedAgentsConflictError](api/beta.md)

Type type

?string message



[ManagedAgentsContentSha256Precondition](api/beta.md)

Type type

?string contentSha256

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.



[ManagedAgentsDeletedMemory](api/beta.md)

string id

ID of the deleted memory (a `mem_...` value).

Type type



[ManagedAgentsError](api/beta.md)

One of the following:



[BetaInvalidRequestError](api/beta.md)

string message

"invalid\_request\_error" type



[BetaAuthenticationError](api/beta.md)

string message

"authentication\_error" type



[BetaBillingError](api/beta.md)

string message

"billing\_error" type



[BetaPermissionError](api/beta.md)

string message

"permission\_error" type



[BetaNotFoundError](api/beta.md)

string message

"not\_found\_error" type



[BetaRateLimitError](api/beta.md)

string message

"rate\_limit\_error" type



[BetaGatewayTimeoutError](api/beta.md)

string message

"timeout\_error" type



[BetaAPIError](api/beta.md)

string message

"api\_error" type



[BetaOverloadedError](api/beta.md)

string message

"overloaded\_error" type



[ManagedAgentsMemoryPreconditionFailedError](api/beta.md)

Type type

?string message



[ManagedAgentsMemoryPathConflictError](api/beta.md)

Type type

?string conflictingMemoryID

?string conflictingPath

?string message



[ManagedAgentsConflictError](api/beta.md)

Type type

?string message



[ManagedAgentsMemory](api/beta.md)

string id

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

string contentSha256

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

int contentSizeBytes

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryStoreID

ID of the memory store this memory belongs to (a `memstore_...` value).

string memoryVersionID

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

string path

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?string content

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).



[ManagedAgentsMemoryListItem](api/beta.md)

One of the following:



[ManagedAgentsMemory](api/beta.md)

string id

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

string contentSha256

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

int contentSizeBytes

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryStoreID

ID of the memory store this memory belongs to (a `memstore_...` value).

string memoryVersionID

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

string path

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?string content

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).



[ManagedAgentsMemoryPrefix](api/beta.md)

string path

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type type



[ManagedAgentsMemoryPathConflictError](api/beta.md)

Type type

?string conflictingMemoryID

?string conflictingPath

?string message



[ManagedAgentsMemoryPreconditionFailedError](api/beta.md)

Type type

?string message



[ManagedAgentsMemoryPrefix](api/beta.md)

string path

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type type



[ManagedAgentsMemoryView](api/beta.md)

One of the following:

"basic"

"full"



[ManagedAgentsPrecondition](api/beta.md)

Type type

?string contentSha256

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

$client->beta->memoryStores->memoryVersions->list(string memoryStoreID, ?string apiKeyID, ?\Datetime createdAtGte, ?\Datetime createdAtLte, ?int limit, ?string memoryID, ?[ManagedAgentsMemoryVersionOperation](api/beta.md) operation, ?string page, ?string sessionID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsMemoryVersion](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

$client->beta->memoryStores->memoryVersions->retrieve(string memoryVersionID, string memoryStoreID, ?[ManagedAgentsMemoryView](api/beta.md) view, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

$client->beta->memoryStores->memoryVersions->redact(string memoryVersionID, string memoryStoreID, ?list<AnthropicBeta> betas): [ManagedAgentsMemoryVersion](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse



[ManagedAgentsActor](api/beta.md)

One of the following:



[ManagedAgentsSessionActor](api/beta.md)

string sessionID

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type



[ManagedAgentsAPIActor](api/beta.md)

string apiKeyID

ID of the API key that performed the write. This identifies the key, not the secret.

Type type



[ManagedAgentsUserActor](api/beta.md)

Type type

string userID

ID of the user who performed the write (a `user_...` value).



[ManagedAgentsAPIActor](api/beta.md)

string apiKeyID

ID of the API key that performed the write. This identifies the key, not the secret.

Type type



[ManagedAgentsMemoryVersion](api/beta.md)

string id

Unique identifier for this version (a `memver_...` value).

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryID

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

string memoryStoreID

ID of the memory store this version belongs to (a `memstore_...` value).

[ManagedAgentsMemoryVersionOperation](api/beta.md) operation

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Type type

?string content

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

?string contentSha256

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

?int contentSizeBytes

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

?[ManagedAgentsActor](api/beta.md) createdBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

?string path

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

?\Datetime redactedAt

A timestamp in RFC 3339 format

?[ManagedAgentsActor](api/beta.md) redactedBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).



[ManagedAgentsMemoryVersionOperation](api/beta.md)

One of the following:

"created"

"modified"

"deleted"



[ManagedAgentsSessionActor](api/beta.md)

string sessionID

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type



[ManagedAgentsUserActor](api/beta.md)

Type type

string userID

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
