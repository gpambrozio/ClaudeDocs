# Memory Stores

Copy page

Python

# Memory Stores

##### [Create a memory store](api/beta/memory_stores/create.md)

beta.memory\_stores.create(MemoryStoreCreateParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores

##### [List memory stores](api/beta/memory_stores/list.md)

beta.memory\_stores.list(MemoryStoreListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryStore](api/beta.md)]

GET/v1/memory\_stores

##### [Retrieve a memory store](api/beta/memory_stores/retrieve.md)

beta.memory\_stores.retrieve(strmemory\_store\_id, MemoryStoreRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}

##### [Update a memory store](api/beta/memory_stores/update.md)

beta.memory\_stores.update(strmemory\_store\_id, MemoryStoreUpdateParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}

##### [Delete a memory store](api/beta/memory_stores/delete.md)

beta.memory\_stores.delete(strmemory\_store\_id, MemoryStoreDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedMemoryStore](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}

##### [Archive a memory store](api/beta/memory_stores/archive.md)

beta.memory\_stores.archive(strmemory\_store\_id, MemoryStoreArchiveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryStore](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedMemoryStore: …

Confirmation that a `memory_store` was deleted.

id: str

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.

type: Literal["memory\_store\_deleted"]

class BetaManagedAgentsMemoryStore: …

A `memory_store`: a named container for agent memories, scoped to a workspace. Attach a store to a session via `resources[]` to mount it as a directory the agent can read and write.

id: str

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

created\_at: datetime

A timestamp in RFC 3339 format

name: str

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

type: Literal["memory\_store"]

updated\_at: datetime

A timestamp in RFC 3339 format

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

description: Optional[str]

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

metadata: Optional[Dict[str, str]]

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

#### Memory StoresMemories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

beta.memory\_stores.memories.create(strmemory\_store\_id, MemoryCreateParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

beta.memory\_stores.memories.list(strmemory\_store\_id, MemoryListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryListItem](api/beta.md)]

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

beta.memory\_stores.memories.retrieve(strmemory\_id, MemoryRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

beta.memory\_stores.memories.update(strmemory\_id, MemoryUpdateParams\*\*kwargs)  -> [BetaManagedAgentsMemory](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

beta.memory\_stores.memories.delete(strmemory\_id, MemoryDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedMemory](api/beta.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsConflictError: …

type: Literal["conflict\_error"]

message: Optional[str]

class BetaManagedAgentsContentSha256Precondition: …

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: Literal["content\_sha256"]

content\_sha256: Optional[str]

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

class BetaManagedAgentsDeletedMemory: …

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

id: str

ID of the deleted memory (a `mem_...` value).

type: Literal["memory\_deleted"]

[BetaManagedAgentsError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError: …

message: str

type: Literal["invalid\_request\_error"]

class BetaAuthenticationError: …

message: str

type: Literal["authentication\_error"]

class BetaBillingError: …

message: str

type: Literal["billing\_error"]

class BetaPermissionError: …

message: str

type: Literal["permission\_error"]

class BetaNotFoundError: …

message: str

type: Literal["not\_found\_error"]

class BetaRateLimitError: …

message: str

type: Literal["rate\_limit\_error"]

class BetaGatewayTimeoutError: …

message: str

type: Literal["timeout\_error"]

class BetaAPIError: …

message: str

type: Literal["api\_error"]

class BetaOverloadedError: …

message: str

type: Literal["overloaded\_error"]

class BetaManagedAgentsMemoryPreconditionFailedError: …

type: Literal["memory\_precondition\_failed\_error"]

message: Optional[str]

class BetaManagedAgentsMemoryPathConflictError: …

type: Literal["memory\_path\_conflict\_error"]

conflicting\_memory\_id: Optional[str]

conflicting\_path: Optional[str]

message: Optional[str]

class BetaManagedAgentsConflictError: …

type: Literal["conflict\_error"]

message: Optional[str]

class BetaManagedAgentsMemory: …

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: str

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: str

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: int

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: datetime

A timestamp in RFC 3339 format

memory\_store\_id: str

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: str

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: str

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

type: Literal["memory"]

updated\_at: datetime

A timestamp in RFC 3339 format

content: Optional[str]

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

[BetaManagedAgentsMemoryListItem](api/beta.md)

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

Accepts one of the following:

class BetaManagedAgentsMemory: …

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: str

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: str

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: int

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: datetime

A timestamp in RFC 3339 format

memory\_store\_id: str

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: str

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: str

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

type: Literal["memory"]

updated\_at: datetime

A timestamp in RFC 3339 format

content: Optional[str]

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).

class BetaManagedAgentsMemoryPrefix: …

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: str

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: Literal["memory\_prefix"]

class BetaManagedAgentsMemoryPathConflictError: …

type: Literal["memory\_path\_conflict\_error"]

conflicting\_memory\_id: Optional[str]

conflicting\_path: Optional[str]

message: Optional[str]

class BetaManagedAgentsMemoryPreconditionFailedError: …

type: Literal["memory\_precondition\_failed\_error"]

message: Optional[str]

class BetaManagedAgentsMemoryPrefix: …

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: str

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: Literal["memory\_prefix"]

Literal["basic", "full"]

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

Accepts one of the following:

"basic"

"full"

class BetaManagedAgentsPrecondition: …

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: Literal["content\_sha256"]

content\_sha256: Optional[str]

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

#### Memory StoresMemory Versions

##### [List memory versions](api/beta/memory_stores/memory_versions/list.md)

beta.memory\_stores.memory\_versions.list(strmemory\_store\_id, MemoryVersionListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsMemoryVersion](api/beta.md)]

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions

##### [Retrieve a memory version](api/beta/memory_stores/memory_versions/retrieve.md)

beta.memory\_stores.memory\_versions.retrieve(strmemory\_version\_id, MemoryVersionRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta.md)

GET/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}

##### [Redact a memory version](api/beta/memory_stores/memory_versions/redact.md)

beta.memory\_stores.memory\_versions.redact(strmemory\_version\_id, MemoryVersionRedactParams\*\*kwargs)  -> [BetaManagedAgentsMemoryVersion](api/beta.md)

POST/v1/memory\_stores/{memory\_store\_id}/memory\_versions/{memory\_version\_id}/redact

##### ModelsExpand Collapse

[BetaManagedAgentsActor](api/beta.md)

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor: …

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: str

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: Literal["session\_actor"]

class BetaManagedAgentsAPIActor: …

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: str

ID of the API key that performed the write. This identifies the key, not the secret.

type: Literal["api\_actor"]

class BetaManagedAgentsUserActor: …

Attribution for a write made by a human user through the Anthropic Console.

type: Literal["user\_actor"]

user\_id: str

ID of the user who performed the write (a `user_...` value).

class BetaManagedAgentsAPIActor: …

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: str

ID of the API key that performed the write. This identifies the key, not the secret.

type: Literal["api\_actor"]

class BetaManagedAgentsMemoryVersion: …

A `memory_version` object: one immutable, attributed row in a memory's append-only history. Every non-no-op mutation to a memory produces a new version. Versions belong to the store (not the individual memory) and persist after the memory is deleted. Retrieving a redacted version returns 200 with `content`, `path`, `content_size_bytes`, and `content_sha256` set to `null`; branch on `redacted_at`, not HTTP status.

id: str

Unique identifier for this version (a `memver_...` value).

created\_at: datetime

A timestamp in RFC 3339 format

memory\_id: str

ID of the memory this version snapshots (a `mem_...` value). Remains valid after the memory is deleted; pass it as `memory_id` to [List memory versions](api/beta/memory_stores/memory_versions/list.md) to retrieve the full lineage including the `deleted` row.

memory\_store\_id: str

ID of the memory store this version belongs to (a `memstore_...` value).

operation: [BetaManagedAgentsMemoryVersionOperation](api/beta.md)

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

"created"

"modified"

"deleted"

type: Literal["memory\_version"]

content: Optional[str]

The memory's UTF-8 text content as of this version. `null` when `view=basic`, when `operation` is `deleted`, or when `redacted_at` is set.

content\_sha256: Optional[str]

Lowercase hex SHA-256 digest of `content` as of this version (64 characters). `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

content\_size\_bytes: Optional[int]

Size of `content` in bytes as of this version. `null` when `redacted_at` is set or `operation` is `deleted`. Populated regardless of `view` otherwise.

created\_by: Optional[BetaManagedAgentsActor]

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor: …

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: str

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: Literal["session\_actor"]

class BetaManagedAgentsAPIActor: …

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: str

ID of the API key that performed the write. This identifies the key, not the secret.

type: Literal["api\_actor"]

class BetaManagedAgentsUserActor: …

Attribution for a write made by a human user through the Anthropic Console.

type: Literal["user\_actor"]

user\_id: str

ID of the user who performed the write (a `user_...` value).

path: Optional[str]

The memory's path at the time of this write. `null` if and only if `redacted_at` is set.

redacted\_at: Optional[datetime]

A timestamp in RFC 3339 format

redacted\_by: Optional[BetaManagedAgentsActor]

Identifies who performed a write or redact operation. Captured at write time on the `memory_version` row. The API key that created a session is not recorded on agent writes; attribution answers who made the write, not who is ultimately responsible. Look up session provenance separately via the [Sessions API](api/sessions-retrieve.md).

Accepts one of the following:

class BetaManagedAgentsSessionActor: …

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: str

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: Literal["session\_actor"]

class BetaManagedAgentsAPIActor: …

Attribution for a write made directly via the public API (outside of any session).

api\_key\_id: str

ID of the API key that performed the write. This identifies the key, not the secret.

type: Literal["api\_actor"]

class BetaManagedAgentsUserActor: …

Attribution for a write made by a human user through the Anthropic Console.

type: Literal["user\_actor"]

user\_id: str

ID of the user who performed the write (a `user_...` value).

Literal["created", "modified", "deleted"]

The kind of mutation a `memory_version` records. Every non-no-op mutation to a memory appends exactly one version row with one of these values.

Accepts one of the following:

"created"

"modified"

"deleted"

class BetaManagedAgentsSessionActor: …

Attribution for a write made by an agent during a session, through the mounted filesystem at `/mnt/memory/`.

session\_id: str

ID of the session that performed the write (a `sesn_...` value). Look up the session via [Retrieve a session](api/sessions-retrieve.md) for further provenance.

type: Literal["session\_actor"]

class BetaManagedAgentsUserActor: …

Attribution for a write made by a human user through the Anthropic Console.

type: Literal["user\_actor"]

user\_id: str

ID of the user who performed the write (a `user_...` value).

---

*Copyright © Anthropic. All rights reserved.*
