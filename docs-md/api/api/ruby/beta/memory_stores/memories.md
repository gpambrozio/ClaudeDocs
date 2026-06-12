# Memories

Copy page

SDK language

Ruby

# Memories

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



class BetaManagedAgentsConflictError { type, message } 

type: :conflict\_error

message: String



class BetaManagedAgentsContentSha256Precondition { type, content\_sha256 } 

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: :content\_sha256

content\_sha256: String

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.



class BetaManagedAgentsDeletedMemory { id, type } 

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

id: String

ID of the deleted memory (a `mem_...` value).

type: :memory\_deleted



BetaManagedAgentsError = [BetaInvalidRequestError](api/beta.md) { message, type }  | [BetaAuthenticationError](api/beta.md) { message, type }  | [BetaBillingError](api/beta.md) { message, type }  | 9 more

One of the following:



class BetaInvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class BetaAuthenticationError { message, type } 

message: String

type: :authentication\_error



class BetaBillingError { message, type } 

message: String

type: :billing\_error



class BetaPermissionError { message, type } 

message: String

type: :permission\_error



class BetaNotFoundError { message, type } 

message: String

type: :not\_found\_error



class BetaRateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class BetaGatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class BetaAPIError { message, type } 

message: String

type: :api\_error



class BetaOverloadedError { message, type } 

message: String

type: :overloaded\_error



class BetaManagedAgentsMemoryPreconditionFailedError { type, message } 

type: :memory\_precondition\_failed\_error

message: String



class BetaManagedAgentsMemoryPathConflictError { type, conflicting\_memory\_id, conflicting\_path, message } 

type: :memory\_path\_conflict\_error

conflicting\_memory\_id: String

conflicting\_path: String

message: String



class BetaManagedAgentsConflictError { type, message } 

type: :conflict\_error

message: String



class BetaManagedAgentsMemory { id, content\_sha256, content\_size\_bytes, 7 more } 

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: String

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: String

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: Integer

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: Time

A timestamp in RFC 3339 format

memory\_store\_id: String

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: String

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: String

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

type: :memory

updated\_at: Time

A timestamp in RFC 3339 format

content: String

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).



BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }  | [BetaManagedAgentsMemoryPrefix](api/beta.md) { path, type } 

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

One of the following:



class BetaManagedAgentsMemory { id, content\_sha256, content\_size\_bytes, 7 more } 

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: String

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: String

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: Integer

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: Time

A timestamp in RFC 3339 format

memory\_store\_id: String

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: String

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: String

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.

type: :memory

updated\_at: Time

A timestamp in RFC 3339 format

content: String

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).



class BetaManagedAgentsMemoryPrefix { path, type } 

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: String

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: :memory\_prefix



class BetaManagedAgentsMemoryPathConflictError { type, conflicting\_memory\_id, conflicting\_path, message } 

type: :memory\_path\_conflict\_error

conflicting\_memory\_id: String

conflicting\_path: String

message: String



class BetaManagedAgentsMemoryPreconditionFailedError { type, message } 

type: :memory\_precondition\_failed\_error

message: String



class BetaManagedAgentsMemoryPrefix { path, type } 

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: String

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: :memory\_prefix



BetaManagedAgentsMemoryView = :basic | :full

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

One of the following:

:basic

:full



class BetaManagedAgentsPrecondition { type, content\_sha256 } 

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: :content\_sha256

content\_sha256: String

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

---

*Copyright © Anthropic. All rights reserved.*
