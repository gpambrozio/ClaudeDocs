# Memories

Copy page



cURL

# Memories

##### [Create a memory](api/http/beta/memory_stores/memories/create.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/http/beta/memory_stores/memories/list.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/http/beta/memory_stores/memories/retrieve.md)

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/http/beta/memory_stores/memories/update.md)

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/http/beta/memory_stores/memories/delete.md)

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### Models



BetaManagedAgentsConflictError object{ type, message }

type: "conflict\_error"

message: optional string



BetaManagedAgentsContentSha256Precondition object{ type, content\_sha256 }

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: "content\_sha256"

content\_sha256: optional string

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.



BetaManagedAgentsDeletedMemory object{ id, type }

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

id: string

ID of the deleted memory (a `mem_...` value).

type: "memory\_deleted"



BetaManagedAgentsError = [BetaInvalidRequestError](api/http/beta.md) { message, type } or [BetaAuthenticationError](api/http/beta.md) { message, type } or [BetaBillingError](api/http/beta.md) { message, type } or 9 more

One of the following:



BetaManagedAgentsMemory object{ id, content\_sha256, content\_size\_bytes, 7 more }

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.



BetaManagedAgentsMemoryListItem = [BetaManagedAgentsMemory](api/http/beta/memory_stores/memories.md) { id, content\_sha256, content\_size\_bytes, 7 more } or [BetaManagedAgentsMemoryPrefix](api/http/beta/memory_stores/memories.md) { path, type }

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.

One of the following:



BetaManagedAgentsMemoryPathConflictError object{ type, conflicting\_memory\_id, conflicting\_path, message }

type: "memory\_path\_conflict\_error"

conflicting\_memory\_id: optional string

conflicting\_path: optional string

message: optional string



BetaManagedAgentsMemoryPreconditionFailedError object{ type, message }

type: "memory\_precondition\_failed\_error"

message: optional string



BetaManagedAgentsMemoryPrefix object{ path, type }

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.

type: "memory\_prefix"



BetaManagedAgentsMemoryView = "basic" or "full"

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

One of the following:

"basic"

"full"



BetaManagedAgentsPrecondition object{ type, content\_sha256 }

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.

type: "content\_sha256"

content\_sha256: optional string

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

---

*Copyright © Anthropic. All rights reserved.*
