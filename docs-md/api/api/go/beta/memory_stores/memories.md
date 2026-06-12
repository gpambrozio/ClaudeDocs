# Memories

Copy page

SDK language

Go

# Memories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

client.Beta.MemoryStores.Memories.New(ctx, memoryStoreID, params) (\*[BetaManagedAgentsMemory](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

client.Beta.MemoryStores.Memories.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryListItemUnion](api/beta.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

client.Beta.MemoryStores.Memories.Get(ctx, memoryID, params) (\*[BetaManagedAgentsMemory](api/beta.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

client.Beta.MemoryStores.Memories.Update(ctx, memoryID, params) (\*[BetaManagedAgentsMemory](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

client.Beta.MemoryStores.Memories.Delete(ctx, memoryID, params) (\*[BetaManagedAgentsDeletedMemory](api/beta.md), error)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse



type BetaManagedAgentsConflictError struct{…}

Type BetaManagedAgentsConflictErrorType

Message stringOptional



type BetaManagedAgentsContentSha256Precondition struct{…}

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

Type BetaManagedAgentsContentSha256PreconditionType

ContentSha256 stringOptional

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.



type BetaManagedAgentsDeletedMemory struct{…}

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

ID string

ID of the deleted memory (a `mem_...` value).

Type BetaManagedAgentsDeletedMemoryType



type BetaManagedAgentsErrorUnion interface{…}

One of the following:



type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError



type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError



type BetaBillingError struct{…}

Message string

Type BillingError



type BetaPermissionError struct{…}

Message string

Type PermissionError



type BetaNotFoundError struct{…}

Message string

Type NotFoundError



type BetaRateLimitError struct{…}

Message string

Type RateLimitError



type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError



type BetaAPIError struct{…}

Message string

Type APIError



type BetaOverloadedError struct{…}

Message string

Type OverloadedError



type BetaManagedAgentsMemoryPreconditionFailedError struct{…}

Type BetaManagedAgentsMemoryPreconditionFailedErrorType

Message stringOptional



type BetaManagedAgentsMemoryPathConflictError struct{…}

Type BetaManagedAgentsMemoryPathConflictErrorType

ConflictingMemoryID stringOptional

ConflictingPath stringOptional

Message stringOptional



type BetaManagedAgentsConflictError struct{…}

Type BetaManagedAgentsConflictErrorType

Message stringOptional



type BetaManagedAgentsMemory struct{…}

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

ID string

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

ContentSha256 string

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

ContentSizeBytes int64

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

CreatedAt Time

A timestamp in RFC 3339 format

MemoryStoreID string

ID of the memory store this memory belongs to (a `memstore_...` value).

MemoryVersionID string

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

Path string

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type BetaManagedAgentsMemoryType

UpdatedAt Time

A timestamp in RFC 3339 format

Content stringOptional

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).



type BetaManagedAgentsMemoryListItemUnion interface{…}

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

One of the following:



type BetaManagedAgentsMemory struct{…}

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

ID string

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

ContentSha256 string

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

ContentSizeBytes int64

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

CreatedAt Time

A timestamp in RFC 3339 format

MemoryStoreID string

ID of the memory store this memory belongs to (a `memstore_...` value).

MemoryVersionID string

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

Path string

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type BetaManagedAgentsMemoryType

UpdatedAt Time

A timestamp in RFC 3339 format

Content stringOptional

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).



type BetaManagedAgentsMemoryPrefix struct{…}

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

Path string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type BetaManagedAgentsMemoryPrefixType



type BetaManagedAgentsMemoryPathConflictError struct{…}

Type BetaManagedAgentsMemoryPathConflictErrorType

ConflictingMemoryID stringOptional

ConflictingPath stringOptional

Message stringOptional



type BetaManagedAgentsMemoryPreconditionFailedError struct{…}

Type BetaManagedAgentsMemoryPreconditionFailedErrorType

Message stringOptional



type BetaManagedAgentsMemoryPrefix struct{…}

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

Path string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type BetaManagedAgentsMemoryPrefixType



type BetaManagedAgentsMemoryView string

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

One of the following:

const BetaManagedAgentsMemoryViewBasic [BetaManagedAgentsMemoryView](api/beta.md) = "basic"

const BetaManagedAgentsMemoryViewFull [BetaManagedAgentsMemoryView](api/beta.md) = "full"



type BetaManagedAgentsPrecondition struct{…}

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

Type BetaManagedAgentsPreconditionType

ContentSha256 stringOptional

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

---

*Copyright © Anthropic. All rights reserved.*
