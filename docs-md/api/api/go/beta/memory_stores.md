# Memory Stores

Copy page

Go

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

client.Beta.MemoryStores.New(ctx, params) (\*[BetaManagedAgentsMemoryStore](api/beta.md), error)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

client.Beta.MemoryStores.List(ctx, params) (\*PageCursor[[BetaManagedAgentsMemoryStore](api/beta.md)], error)

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

client.Beta.MemoryStores.Get(ctx, memoryStoreID, query) (\*[BetaManagedAgentsMemoryStore](api/beta.md), error)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

client.Beta.MemoryStores.Update(ctx, memoryStoreID, params) (\*[BetaManagedAgentsMemoryStore](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

client.Beta.MemoryStores.Delete(ctx, memoryStoreID, body) (\*[BetaManagedAgentsDeletedMemoryStore](api/beta.md), error)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

client.Beta.MemoryStores.Archive(ctx, memoryStoreID, body) (\*[BetaManagedAgentsMemoryStore](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

type BetaManagedAgentsDeletedMemoryStore struct{…}

Confirmation that a `memory_store` was deleted.

ID string

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

Type BetaManagedAgentsDeletedMemoryStoreType

type BetaManagedAgentsMemoryStore struct{…}

A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

ID string

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

CreatedAt Time

A timestamp in RFC 3339 format

Name string

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

Type BetaManagedAgentsMemoryStoreType

UpdatedAt Time

A timestamp in RFC 3339 format

ArchivedAt Timeoptional

A timestamp in RFC 3339 format

Description stringoptional

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

Metadata map[string, string]optional

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory StoresMemories

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

type BetaManagedAgentsConflictError struct{…}

Type BetaManagedAgentsConflictErrorType

Message stringoptional

type BetaManagedAgentsContentSha256Precondition struct{…}

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

Type BetaManagedAgentsContentSha256PreconditionType

ContentSha256 stringoptional

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

type BetaManagedAgentsDeletedMemory struct{…}

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

ID string

ID of the deleted memory (a `mem_...` value).

Type BetaManagedAgentsDeletedMemoryType

type BetaManagedAgentsErrorUnion interface{…}

Accepts one of the following:

type BetaInvalidRequestError struct{…}

Message string

Type InvalidRequestError

type BetaAuthenticationError struct{…}

Message string

Type AuthenticationError

type BetaBillingError struct{…}

Message string

Type BillingError

type BetaPermissionError struct{…}

Message string

Type PermissionError

type BetaNotFoundError struct{…}

Message string

Type NotFoundError

type BetaRateLimitError struct{…}

Message string

Type RateLimitError

type BetaGatewayTimeoutError struct{…}

Message string

Type TimeoutError

type BetaAPIError struct{…}

Message string

Type APIError

type BetaOverloadedError struct{…}

Message string

Type OverloadedError

type BetaManagedAgentsMemoryPreconditionFailedError struct{…}

Type BetaManagedAgentsMemoryPreconditionFailedErrorType

Message stringoptional

type BetaManagedAgentsMemoryPathConflictError struct{…}

Type BetaManagedAgentsMemoryPathConflictErrorType

ConflictingMemoryID stringoptional

ConflictingPath stringoptional

Message stringoptional

type BetaManagedAgentsConflictError struct{…}

Type BetaManagedAgentsConflictErrorType

Message stringoptional

type BetaManagedAgentsMemory struct{…}

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

ID string

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

ContentSha256 string

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

ContentSizeBytes int64

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

CreatedAt Time

A timestamp in RFC 3339 format

MemoryStoreID string

ID of the memory store this memory belongs to (a `memstore_...` value).

MemoryVersionID string

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

Path string

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type BetaManagedAgentsMemoryType

UpdatedAt Time

A timestamp in RFC 3339 format

Content stringoptional

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

type BetaManagedAgentsMemoryListItemUnion interface{…}

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

Accepts one of the following:

type BetaManagedAgentsMemory struct{…}

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

ID string

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

ContentSha256 string

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

ContentSizeBytes int64

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

CreatedAt Time

A timestamp in RFC 3339 format

MemoryStoreID string

ID of the memory store this memory belongs to (a `memstore_...` value).

MemoryVersionID string

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

Path string

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

Type BetaManagedAgentsMemoryType

UpdatedAt Time

A timestamp in RFC 3339 format

Content stringoptional

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

type BetaManagedAgentsMemoryPrefix struct{…}

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

Path string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type BetaManagedAgentsMemoryPrefixType

type BetaManagedAgentsMemoryPathConflictError struct{…}

Type BetaManagedAgentsMemoryPathConflictErrorType

ConflictingMemoryID stringoptional

ConflictingPath stringoptional

Message stringoptional

type BetaManagedAgentsMemoryPreconditionFailedError struct{…}

Type BetaManagedAgentsMemoryPreconditionFailedErrorType

Message stringoptional

type BetaManagedAgentsMemoryPrefix struct{…}

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

Path string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

Type BetaManagedAgentsMemoryPrefixType

type BetaManagedAgentsMemoryView string

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

Accepts one of the following:

const BetaManagedAgentsMemoryViewBasic [BetaManagedAgentsMemoryView](api/beta.md) = "basic"

const BetaManagedAgentsMemoryViewFull [BetaManagedAgentsMemoryView](api/beta.md) = "full"

type BetaManagedAgentsPrecondition struct{…}

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

Type BetaManagedAgentsPreconditionType

ContentSha256 stringoptional

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

client.Beta.MemoryStores.MemoryVersions.List(ctx, memoryStoreID, params) (\*PageCursor[[BetaManagedAgentsMemoryVersion](api/beta.md)], error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

client.Beta.MemoryStores.MemoryVersions.Get(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta.md), error)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

client.Beta.MemoryStores.MemoryVersions.Redact(ctx, memoryVersionID, params) (\*[BetaManagedAgentsMemoryVersion](api/beta.md), error)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

type BetaManagedAgentsActorUnion interface{…}

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsMemoryVersion struct{…}

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

ID string

Unique identifier for this version (a `memver_...` value).

CreatedAt Time

A timestamp in RFC 3339 format

MemoryID string

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

MemoryStoreID string

ID of the memory store this version belongs to (a `memstore_...` value).

Operation [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

const BetaManagedAgentsMemoryVersionOperationCreated [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "created"

const BetaManagedAgentsMemoryVersionOperationModified [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "modified"

const BetaManagedAgentsMemoryVersionOperationDeleted [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "deleted"

Type BetaManagedAgentsMemoryVersionType

Content stringoptional

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

ContentSha256 stringoptional

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

ContentSizeBytes int64optional

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

CreatedBy [BetaManagedAgentsActorUnion](api/beta.md)optional

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

Path stringoptional

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

RedactedAt Timeoptional

A timestamp in RFC 3339 format

RedactedBy [BetaManagedAgentsActorUnion](api/beta.md)optional

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsAPIActor struct{…}

Attribution for a write made directly via the public API (outside of any session).

APIKeyID string

ID of the API key that performed the write. This identifies the key, not the secret.

Type BetaManagedAgentsAPIActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

type BetaManagedAgentsMemoryVersionOperation string

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

const BetaManagedAgentsMemoryVersionOperationCreated [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "created"

const BetaManagedAgentsMemoryVersionOperationModified [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "modified"

const BetaManagedAgentsMemoryVersionOperationDeleted [BetaManagedAgentsMemoryVersionOperation](api/beta.md) = "deleted"

type BetaManagedAgentsSessionActor struct{…}

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

SessionID string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

Type BetaManagedAgentsSessionActorType

type BetaManagedAgentsUserActor struct{…}

Attribution for a write made by a human user through the Anthropic Console.

Type BetaManagedAgentsUserActorType

UserID string

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
