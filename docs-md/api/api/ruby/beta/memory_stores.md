# Memory Stores

Copy page

Ruby

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

beta.memory\_stores.create(\*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

beta.memory\_stores.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryStore](api/beta.md) { id, created\_at, name, 5 more } >

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

beta.memory\_stores.retrieve(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta.md) { id, created\_at, name, 5 more }

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

beta.memory\_stores.update(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

beta.memory\_stores.delete(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedMemoryStore](api/beta.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

beta.memory\_stores.archive(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryStore](api/beta.md) { id, created\_at, name, 5 more }

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedMemoryStore { id, type }

Confirmation that a `memory_store` was deleted.

id: String

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

type: :memory\_store\_deleted

class BetaManagedAgentsMemoryStore { id, created\_at, name, 5 more }

A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

id: String

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

created\_at: Time

A timestamp in RFC 3339 format

name: String

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

type: :memory\_store

updated\_at: Time

A timestamp in RFC 3339 format

archived\_at: Time

A timestamp in RFC 3339 format

description: String

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

metadata: Hash[Symbol, String]

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

beta.memory\_stores.memories.create(memory\_store\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

beta.memory\_stores.memories.list(memory\_store\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryListItem](api/beta.md)>

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

beta.memory\_stores.memories.retrieve(memory\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

beta.memory\_stores.memories.update(memory\_id, \*\*kwargs) -> [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

beta.memory\_stores.memories.delete(memory\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedMemory](api/beta.md) { id, type }

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsConflictError { type, message }

type: :conflict\_error

message: String

class BetaManagedAgentsContentSha256Precondition { type, content\_sha256 }

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: :content\_sha256

content\_sha256: String

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

class BetaManagedAgentsDeletedMemory { id, type }

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

id: String

ID of the deleted memory (a `mem_...` value).

type: :memory\_deleted

BetaManagedAgentsError = [BetaInvalidRequestError](api/beta.md) { message, type }  | [BetaAuthenticationError](api/beta.md) { message, type }  | [BetaBillingError](api/beta.md) { message, type }  | 9 more

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

class BetaManagedAgentsMemoryPreconditionFailedError { type, message }

type: :memory\_precondition\_failed\_error

message: String

class BetaManagedAgentsMemoryPathConflictError { type, conflicting\_memory\_id, conflicting\_path, message }

type: :memory\_path\_conflict\_error

conflicting\_memory\_id: String

conflicting\_path: String

message: String

class BetaManagedAgentsConflictError { type, message }

type: :conflict\_error

message: String

class BetaManagedAgentsMemory { id, content\_sha256, content\_size\_bytes, 7 more }

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: String

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: String

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: Integer

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: Time

A timestamp in RFC 3339 format

memory\_store\_id: String

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: String

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: String

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

type: :memory

updated\_at: Time

A timestamp in RFC 3339 format

content: String

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }  | [BetaManagedAgentsMemoryPrefix](api/beta.md) { path, type }

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

Accepts one of the following:

class BetaManagedAgentsMemory { id, content\_sha256, content\_size\_bytes, 7 more }

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: String

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: String

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: Integer

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: Time

A timestamp in RFC 3339 format

memory\_store\_id: String

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: String

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: String

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

type: :memory

updated\_at: Time

A timestamp in RFC 3339 format

content: String

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

class BetaManagedAgentsMemoryPrefix { path, type }

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: String

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: :memory\_prefix

class BetaManagedAgentsMemoryPathConflictError { type, conflicting\_memory\_id, conflicting\_path, message }

type: :memory\_path\_conflict\_error

conflicting\_memory\_id: String

conflicting\_path: String

message: String

class BetaManagedAgentsMemoryPreconditionFailedError { type, message }

type: :memory\_precondition\_failed\_error

message: String

class BetaManagedAgentsMemoryPrefix { path, type }

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: String

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: :memory\_prefix

BetaManagedAgentsMemoryView = :basic | :full

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

Accepts one of the following:

:basic

:full

class BetaManagedAgentsPrecondition { type, content\_sha256 }

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: :content\_sha256

content\_sha256: String

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

beta.memory\_stores.memory\_versions.list(memory\_store\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more } >

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

beta.memory\_stores.memory\_versions.retrieve(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

beta.memory\_stores.memory\_versions.redact(memory\_version\_id, \*\*kwargs) -> [BetaManagedAgentsMemoryVersion](api/beta.md) { id, created\_at, memory\_id, 10 more }

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

BetaManagedAgentsActor = [BetaManagedAgentsSessionActor](api/beta.md) { session\_id, type }  | [BetaManagedAgentsAPIActor](api/beta.md) { api\_key\_id, type }  | [BetaManagedAgentsUserActor](api/beta.md) { type, user\_id }

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: String

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: :session\_actor

class BetaManagedAgentsAPIActor { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: String

ID of the API key that performed the write. This identifies the key, not the secret.

type: :api\_actor

class BetaManagedAgentsUserActor { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: :user\_actor

user\_id: String

ID of the user who performed the write (a `user_...` value).

class BetaManagedAgentsAPIActor { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: String

ID of the API key that performed the write. This identifies the key, not the secret.

type: :api\_actor

class BetaManagedAgentsMemoryVersion { id, created\_at, memory\_id, 10 more }

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

id: String

Unique identifier for this version (a `memver_...` value).

created\_at: Time

A timestamp in RFC 3339 format

memory\_id: String

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

memory\_store\_id: String

ID of the memory store this version belongs to (a `memstore_...` value).

operation: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

:created

:modified

:deleted

type: :memory\_version

content: String

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: String

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

content\_size\_bytes: Integer

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

created\_by: [BetaManagedAgentsActor](api/beta.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: String

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: :session\_actor

class BetaManagedAgentsAPIActor { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: String

ID of the API key that performed the write. This identifies the key, not the secret.

type: :api\_actor

class BetaManagedAgentsUserActor { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: :user\_actor

user\_id: String

ID of the user who performed the write (a `user_...` value).

path: String

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

redacted\_at: Time

A timestamp in RFC 3339 format

redacted\_by: [BetaManagedAgentsActor](api/beta.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: String

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: :session\_actor

class BetaManagedAgentsAPIActor { api\_key\_id, type }

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: String

ID of the API key that performed the write. This identifies the key, not the secret.

type: :api\_actor

class BetaManagedAgentsUserActor { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: :user\_actor

user\_id: String

ID of the user who performed the write (a `user_...` value).

BetaManagedAgentsMemoryVersionOperation = :created | :modified | :deleted

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

:created

:modified

:deleted

class BetaManagedAgentsSessionActor { session\_id, type }

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: String

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: :session\_actor

class BetaManagedAgentsUserActor { type, user\_id }

Attribution for a write made by a human user through the Anthropic Console.

type: :user\_actor

user\_id: String

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
