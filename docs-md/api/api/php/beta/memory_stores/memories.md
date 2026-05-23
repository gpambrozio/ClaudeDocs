# Memories

Copy page

PHP

# Memories

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

[ManagedAgentsConflictError](api/beta.md)

Type type

?string message

[ManagedAgentsContentSha256Precondition](api/beta.md)

Type type

?string contentSha256

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

[ManagedAgentsDeletedMemory](api/beta.md)

string id

ID of the deleted memory (a `mem_...` value).

Type type

[ManagedAgentsError](api/beta.md)

One of the following:

[BetaInvalidRequestError](api/beta.md)

string message

"invalid\_request\_error" type

[BetaAuthenticationError](api/beta.md)

string message

"authentication\_error" type

[BetaBillingError](api/beta.md)

string message

"billing\_error" type

[BetaPermissionError](api/beta.md)

string message

"permission\_error" type

[BetaNotFoundError](api/beta.md)

string message

"not\_found\_error" type

[BetaRateLimitError](api/beta.md)

string message

"rate\_limit\_error" type

[BetaGatewayTimeoutError](api/beta.md)

string message

"timeout\_error" type

[BetaAPIError](api/beta.md)

string message

"api\_error" type

[BetaOverloadedError](api/beta.md)

string message

"overloaded\_error" type

[ManagedAgentsMemoryPreconditionFailedError](api/beta.md)

Type type

?string message

[ManagedAgentsMemoryPathConflictError](api/beta.md)

Type type

?string conflictingMemoryID

?string conflictingPath

?string message

[ManagedAgentsConflictError](api/beta.md)

Type type

?string message

[ManagedAgentsMemory](api/beta.md)

string id

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

string contentSha256

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

int contentSizeBytes

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryStoreID

ID of the memory store this memory belongs to (a `memstore_...` value).

string memoryVersionID

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

string path

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?string content

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

[ManagedAgentsMemoryListItem](api/beta.md)

One of the following:

[ManagedAgentsMemory](api/beta.md)

string id

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

string contentSha256

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

int contentSizeBytes

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

\Datetime createdAt

A timestamp in RFC 3339 format

string memoryStoreID

ID of the memory store this memory belongs to (a `memstore_...` value).

string memoryVersionID

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

string path

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

?string content

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

[ManagedAgentsMemoryPrefix](api/beta.md)

string path

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type type

[ManagedAgentsMemoryPathConflictError](api/beta.md)

Type type

?string conflictingMemoryID

?string conflictingPath

?string message

[ManagedAgentsMemoryPreconditionFailedError](api/beta.md)

Type type

?string message

[ManagedAgentsMemoryPrefix](api/beta.md)

string path

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type type

[ManagedAgentsMemoryView](api/beta.md)

One of the following:

"basic"

"full"

[ManagedAgentsPrecondition](api/beta.md)

Type type

?string contentSha256

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

---

*Copyright © Anthropic. All rights reserved.*
