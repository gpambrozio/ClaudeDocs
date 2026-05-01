# Memories

Copy page

Java

# Memories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

[BetaManagedAgentsMemory](api/beta.md) beta().memoryStores().memories().create(MemoryCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

MemoryListPage beta().memoryStores().memories().list(MemoryListParamsparams = MemoryListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

[BetaManagedAgentsMemory](api/beta.md) beta().memoryStores().memories().retrieve(MemoryRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

[BetaManagedAgentsMemory](api/beta.md) beta().memoryStores().memories().update(MemoryUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

[BetaManagedAgentsDeletedMemory](api/beta.md) beta().memoryStores().memories().delete(MemoryDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsConflictError:

Type type

Optional<String> message

class BetaManagedAgentsContentSha256Precondition:

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

Type type

Optional<String> contentSha256

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

class BetaManagedAgentsDeletedMemory:

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

String id

ID of the deleted memory (a `mem_...` value).

Type type

class BetaManagedAgentsError: A class that can be one of several variants.union

class BetaInvalidRequestError:

String message

JsonValue; type "invalid\_request\_error"constant"invalid\_request\_error"constant

class BetaAuthenticationError:

String message

JsonValue; type "authentication\_error"constant"authentication\_error"constant

class BetaBillingError:

String message

JsonValue; type "billing\_error"constant"billing\_error"constant

class BetaPermissionError:

String message

JsonValue; type "permission\_error"constant"permission\_error"constant

class BetaNotFoundError:

String message

JsonValue; type "not\_found\_error"constant"not\_found\_error"constant

class BetaRateLimitError:

String message

JsonValue; type "rate\_limit\_error"constant"rate\_limit\_error"constant

class BetaGatewayTimeoutError:

String message

JsonValue; type "timeout\_error"constant"timeout\_error"constant

class BetaApiError:

String message

JsonValue; type "api\_error"constant"api\_error"constant

class BetaOverloadedError:

String message

JsonValue; type "overloaded\_error"constant"overloaded\_error"constant

class BetaManagedAgentsMemoryPreconditionFailedError:

Type type

Optional<String> message

class BetaManagedAgentsMemoryPathConflictError:

Type type

Optional<String> conflictingMemoryId

Optional<String> conflictingPath

Optional<String> message

class BetaManagedAgentsConflictError:

Type type

Optional<String> message

class BetaManagedAgentsMemory:

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

String id

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

String contentSha256

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

long contentSizeBytes

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

LocalDateTime createdAt

A timestamp in RFC 3339 format

String memoryStoreId

ID of the memory store this memory belongs to (a `memstore_...` value).

String memoryVersionId

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

String path

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

Optional<String> content

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

class BetaManagedAgentsMemoryListItem: A class that can be one of several variants.union

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

class BetaManagedAgentsMemory:

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

String id

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

String contentSha256

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

long contentSizeBytes

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

LocalDateTime createdAt

A timestamp in RFC 3339 format

String memoryStoreId

ID of the memory store this memory belongs to (a `memstore_...` value).

String memoryVersionId

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

String path

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

Optional<String> content

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

class BetaManagedAgentsMemoryPrefix:

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

String path

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type type

class BetaManagedAgentsMemoryPathConflictError:

Type type

Optional<String> conflictingMemoryId

Optional<String> conflictingPath

Optional<String> message

class BetaManagedAgentsMemoryPreconditionFailedError:

Type type

Optional<String> message

class BetaManagedAgentsMemoryPrefix:

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

String path

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type type

enum BetaManagedAgentsMemoryView:

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

BASIC("basic")

FULL("full")

class BetaManagedAgentsPrecondition:

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

Type type

Optional<String> contentSha256

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

---

*Copyright © Anthropic. All rights reserved.*
