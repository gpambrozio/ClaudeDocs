# Memory Stores

Copy page

cURL

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

BetaManagedAgentsDeletedMemoryStore = object { id, type }

Confirmation that a `memory_store` was deleted.

id: string

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

type: "memory\_store\_deleted"

BetaManagedAgentsMemoryStore = object { id, created\_at, name, 5 more }

A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

id: string

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

created\_at: string

A timestamp in RFC 3339 format

name: string

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

type: "memory\_store"

updated\_at: string

A timestamp in RFC 3339 format

archived\_at: optional string

A timestamp in RFC 3339 format

description: optional string

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

metadata: optional map[string]

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

BetaManagedAgentsConflictError = object { type, message }

type: "conflict\_error"

message: optional string

BetaManagedAgentsContentSha256Precondition = object { type, content\_sha256 }

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: "content\_sha256"

content\_sha256: optional string

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

BetaManagedAgentsDeletedMemory = object { id, type }

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

id: string

ID of the deleted memory (a `mem_...` value).

type: "memory\_deleted"

BetaManagedAgentsError = [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 9 more

Accepts one of the following:

BetaInvalidRequestError = object { message, type }

message: string

type: "invalid\_request\_error"

BetaAuthenticationError = object { message, type }

message: string

type: "authentication\_error"

BetaBillingError = object { message, type }

message: string

type: "billing\_error"

BetaPermissionError = object { message, type }

message: string

type: "permission\_error"

BetaNotFoundError = object { message, type }

message: string

type: "not\_found\_error"

BetaRateLimitError = object { message, type }

message: string

type: "rate\_limit\_error"

BetaGatewayTimeoutError = object { message, type }

message: string

type: "timeout\_error"

BetaAPIError = object { message, type }

message: string

type: "api\_error"

BetaOverloadedError = object { message, type }

message: string

type: "overloaded\_error"

BetaManagedAgentsMemoryPreconditionFailedError = object { type, message }

type: "memory\_precondition\_failed\_error"

message: optional string

BetaManagedAgentsMemoryPathConflictError = object { type, conflicting\_memory\_id, conflicting\_path, message }

type: "memory\_path\_conflict\_error"

conflicting\_memory\_id: optional string

conflicting\_path: optional string

message: optional string

BetaManagedAgentsConflictError = object { type, message }

type: "conflict\_error"

message: optional string

BetaManagedAgentsMemory = object { id, content\_sha256, content\_size\_bytes, 7 more }

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: string

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: string

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: number

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: string

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: string

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

type: "memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }  or [BetaManagedAgentsMemoryPrefix](api/beta.md) { path, type }

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

Accepts one of the following:

BetaManagedAgentsMemory = object { id, content\_sha256, content\_size\_bytes, 7 more }

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: string

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: string

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: number

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: string

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: string

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

type: "memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

BetaManagedAgentsMemoryPrefix = object { path, type }

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: "memory\_prefix"

BetaManagedAgentsMemoryPathConflictError = object { type, conflicting\_memory\_id, conflicting\_path, message }

type: "memory\_path\_conflict\_error"

conflicting\_memory\_id: optional string

conflicting\_path: optional string

message: optional string

BetaManagedAgentsMemoryPreconditionFailedError = object { type, message }

type: "memory\_precondition\_failed\_error"

message: optional string

BetaManagedAgentsMemoryPrefix = object { path, type }

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: "memory\_prefix"

BetaManagedAgentsMemoryView = "basic" or "full"

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

Accepts one of the following:

"basic"

"full"

BetaManagedAgentsPrecondition = object { type, content\_sha256 }

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: "content\_sha256"

content\_sha256: optional string

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  or [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  or [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

BetaManagedAgentsSessionActor = object { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"

BetaManagedAgentsAPIActor = object { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"

BetaManagedAgentsUserActor = object { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

BetaManagedAgentsAPIActor = object { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"

BetaManagedAgentsMemoryVersion = object { id, created\_at, memory\_id, 10 more }

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

id: string

Unique identifier for this version (a `memver_...` value).

created\_at: string

A timestamp in RFC 3339 format

memory\_id: string

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

memory\_store\_id: string

ID of the memory store this version belongs to (a `memstore_...` value).

operation: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

"created"

"modified"

"deleted"

type: "memory\_version"

content: optional string

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: optional string

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

content\_size\_bytes: optional number

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

created\_by: optional [BetaManagedAgentsActor](api/beta.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

BetaManagedAgentsSessionActor = object { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"

BetaManagedAgentsAPIActor = object { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"

BetaManagedAgentsUserActor = object { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

path: optional string

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

redacted\_at: optional string

A timestamp in RFC 3339 format

redacted\_by: optional [BetaManagedAgentsActor](api/beta.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

BetaManagedAgentsSessionActor = object { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"

BetaManagedAgentsAPIActor = object { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: string

ID of the API key that performed the write. This identifies the key, not the secret.

type: "api\_actor"

BetaManagedAgentsUserActor = object { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

BetaManagedAgentsMemoryVersionOperation = "created" or "modified" or "deleted"

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

"created"

"modified"

"deleted"

BetaManagedAgentsSessionActor = object { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: string

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: "session\_actor"

BetaManagedAgentsUserActor = object { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: "user\_actor"

user\_id: string

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
