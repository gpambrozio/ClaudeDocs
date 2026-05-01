# Memory Stores

Copy page

Java

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

[BetaManagedAgentsMemoryStore](api/beta.md) beta().memoryStores().create(MemoryStoreCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

MemoryStoreListPage beta().memoryStores().list(MemoryStoreListParamsparams = MemoryStoreListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

[BetaManagedAgentsMemoryStore](api/beta.md) beta().memoryStores().retrieve(MemoryStoreRetrieveParamsparams = MemoryStoreRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

[BetaManagedAgentsMemoryStore](api/beta.md) beta().memoryStores().update(MemoryStoreUpdateParamsparams = MemoryStoreUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

[BetaManagedAgentsDeletedMemoryStore](api/beta.md) beta().memoryStores().delete(MemoryStoreDeleteParamsparams = MemoryStoreDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

[BetaManagedAgentsMemoryStore](api/beta.md) beta().memoryStores().archive(MemoryStoreArchiveParamsparams = MemoryStoreArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedMemoryStore:

Confirmation that a `memory_store` was deleted.

String id

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

Type type

class BetaManagedAgentsMemoryStore:

A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

String id

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

LocalDateTime createdAt

A timestamp in RFC 3339 format

String name

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

Optional<String> description

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

Optional<Metadata> metadata

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory StoresMemories

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

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

MemoryVersionListPage beta().memoryStores().memoryVersions().list(MemoryVersionListParamsparams = MemoryVersionListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

[BetaManagedAgentsMemoryVersion](api/beta.md) beta().memoryStores().memoryVersions().retrieve(MemoryVersionRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

[BetaManagedAgentsMemoryVersion](api/beta.md) beta().memoryStores().memoryVersions().redact(MemoryVersionRedactParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

class BetaManagedAgentsActor: A class that can be one of several variants.union

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

String sessionId

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type

class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

String apiKeyId

ID of the API key that performed the write. This identifies the key, not the secret.

Type type

class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

Type type

String userId

ID of the user who performed the write (a `user_...` value).

class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

String apiKeyId

ID of the API key that performed the write. This identifies the key, not the secret.

Type type

class BetaManagedAgentsMemoryVersion:

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

String id

Unique identifier for this version (a `memver_...` value).

LocalDateTime createdAt

A timestamp in RFC 3339 format

String memoryId

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

String memoryStoreId

ID of the memory store this version belongs to (a `memstore_...` value).

[BetaManagedAgentsMemoryVersionOperation](api/beta.md) operation

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

CREATED("created")

MODIFIED("modified")

DELETED("deleted")

Type type

Optional<String> content

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

Optional<String> contentSha256

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

Optional<Long> contentSizeBytes

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

Optional<[BetaManagedAgentsActor](api/beta.md)> createdBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

String sessionId

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type

class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

String apiKeyId

ID of the API key that performed the write. This identifies the key, not the secret.

Type type

class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

Type type

String userId

ID of the user who performed the write (a `user_...` value).

Optional<String> path

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

Optional<LocalDateTime> redactedAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsActor](api/beta.md)> redactedBy

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

String sessionId

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type

class BetaManagedAgentsApiActor:

Attribution for a write made directly via the public API (outside of any session).

String apiKeyId

ID of the API key that performed the write. This identifies the key, not the secret.

Type type

class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

Type type

String userId

ID of the user who performed the write (a `user_...` value).

enum BetaManagedAgentsMemoryVersionOperation:

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

CREATED("created")

MODIFIED("modified")

DELETED("deleted")

class BetaManagedAgentsSessionActor:

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

String sessionId

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type type

class BetaManagedAgentsUserActor:

Attribution for a write made by a human user through the Anthropic Console.

Type type

String userId

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
