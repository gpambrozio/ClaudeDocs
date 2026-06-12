# Memories

Copy page

SDK language

CLI

# Memories

##### [Create a memory](api/beta/memory_stores/memories/create.md)

$ ant beta:memory-stores:memories create

POST/v1/memory\_stores/{memory\_store\_id}/memories

##### [List memories](api/beta/memory_stores/memories/list.md)

$ ant beta:memory-stores:memories list

GET/v1/memory\_stores/{memory\_store\_id}/memories

##### [Retrieve a memory](api/beta/memory_stores/memories/retrieve.md)

$ ant beta:memory-stores:memories retrieve

GET/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Update a memory](api/beta/memory_stores/memories/update.md)

$ ant beta:memory-stores:memories update

POST/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### [Delete a memory](api/beta/memory_stores/memories/delete.md)

$ ant beta:memory-stores:memories delete

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

##### ModelsExpand Collapse



beta\_managed\_agents\_conflict\_error: object { type, message } 



type: "conflict\_error"

"conflict\_error"

message: optional string



beta\_managed\_agents\_content\_sha256\_precondition: object { type, content\_sha256 } 

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.



type: "content\_sha256"

"content\_sha256"

content\_sha256: optional string

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.



beta\_managed\_agents\_deleted\_memory: object { id, type } 

Tombstone returned by [Delete a memory](api/beta/memory_stores/memories/delete.md). The memory's version history persists and remains listable via [List memory versions](api/beta/memory_stores/memory_versions/list.md) until the store itself is deleted.

id: string

ID of the deleted memory (a `mem_...` value).



type: "memory\_deleted"

"memory\_deleted"



beta\_managed\_agents\_error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 9 more



beta\_invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



beta\_authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



beta\_billing\_error: object { message, type } 

message: string

type: "billing\_error"



beta\_permission\_error: object { message, type } 

message: string

type: "permission\_error"



beta\_not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



beta\_rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



beta\_gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



beta\_api\_error: object { message, type } 

message: string

type: "api\_error"



beta\_overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"



beta\_managed\_agents\_memory\_precondition\_failed\_error: object { type, message } 



type: "memory\_precondition\_failed\_error"

"memory\_precondition\_failed\_error"

message: optional string



beta\_managed\_agents\_memory\_path\_conflict\_error: object { type, conflicting\_memory\_id, conflicting\_path, message } 



type: "memory\_path\_conflict\_error"

"memory\_path\_conflict\_error"

conflicting\_memory\_id: optional string

conflicting\_path: optional string

message: optional string



beta\_managed\_agents\_conflict\_error: object { type, message } 



type: "conflict\_error"

"conflict\_error"

message: optional string



beta\_managed\_agents\_memory: object { id, content\_sha256, content\_size\_bytes, 7 more } 

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: string

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: string

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: number

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: string

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: string

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.



type: "memory"

"memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).



beta\_managed\_agents\_memory\_list\_item: [BetaManagedAgentsMemory](api/beta.md) { id, content\_sha256, content\_size\_bytes, 7 more }  or [BetaManagedAgentsMemoryPrefix](api/beta.md) { path, type } 

One item in a [List memories](api/beta/memory_stores/memories/list.md) response: either a `memory` object or, when `depth` is set, a `memory_prefix` rollup marker.



beta\_managed\_agents\_memory: object { id, content\_sha256, content\_size\_bytes, 7 more } 

A `memory` object: a single text document at a hierarchical path inside a memory store. The `content` field is populated when `view=full` and `null` when `view=basic`; the `content_size_bytes` and `content_sha256` fields are always populated so sync clients can diff without fetching content. Memories are addressed by their `mem_...` ID; the path is the create key and can be changed via update.

id: string

Unique identifier for this memory (a `mem_...` value). Stable across renames; use this ID, not the path, to read, update, or delete the memory.

content\_sha256: string

Lowercase hex SHA-256 digest of the UTF-8 `content` bytes (64 characters). The server applies no normalization, so clients can compute the same hash locally for staleness checks and as the value for a `content_sha256` precondition on update. Always populated, regardless of `view`.

content\_size\_bytes: number

Size of `content` in bytes (the UTF-8 plaintext length). Always populated, regardless of `view`.

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

ID of the memory store this memory belongs to (a `memstore_...` value).

memory\_version\_id: string

ID of the `memory_version` representing this memory's current content (a `memver_...` value). This is the authoritative head pointer; `memory_version` objects do not carry an `is_latest` flag, so compare against this field instead. Enumerate the full history via [List memory versions](api/beta/memory_stores/memory_versions/list.md).

path: string

Hierarchical path of the memory within the store, e.g. `/projects/foo/notes.md`. Always starts with `/`. Paths are case-sensitive and unique within a store. Maximum 1,024 bytes.



type: "memory"

"memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

The memory's UTF-8 text content. Populated when `view=full`; `null` when `view=basic`. Maximum 100 kB (102,400 bytes).



beta\_managed\_agents\_memory\_prefix: object { path, type } 

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.



type: "memory\_prefix"

"memory\_prefix"



beta\_managed\_agents\_memory\_path\_conflict\_error: object { type, conflicting\_memory\_id, conflicting\_path, message } 



type: "memory\_path\_conflict\_error"

"memory\_path\_conflict\_error"

conflicting\_memory\_id: optional string

conflicting\_path: optional string

message: optional string



beta\_managed\_agents\_memory\_precondition\_failed\_error: object { type, message } 



type: "memory\_precondition\_failed\_error"

"memory\_precondition\_failed\_error"

message: optional string



beta\_managed\_agents\_memory\_prefix: object { path, type } 

A rolled-up directory marker returned by [List memories](api/beta/memory_stores/memories/list.md) when `depth` is set. Indicates that one or more memories exist deeper than the requested depth under this prefix. This is a list-time rollup, not a stored resource; it has no ID and no lifecycle. Each prefix counts toward the page `limit` and interleaves with `memory` items in path order.

path: string

The rolled-up path prefix, including a trailing `/` (e.g. `/projects/foo/`). Pass this value as `path_prefix` on a subsequent list call to drill into the directory.



type: "memory\_prefix"

"memory\_prefix"



beta\_managed\_agents\_memory\_view: "basic" or "full"

Selects which projection of a `memory` or `memory_version` the server returns. `basic` returns the object with `content` set to `null`; `full` populates `content`. When omitted, the default is endpoint-specific: retrieve operations default to `full`; list, create, and update operations default to `basic`. Listing with `view=full` caps `limit` at 20.

"basic"

"full"



beta\_managed\_agents\_precondition: object { type, content\_sha256 } 

Optimistic-concurrency precondition: the update applies only if the memory's stored `content_sha256` equals the supplied value. On mismatch, the request returns `memory_precondition_failed_error` (HTTP 409); re-read the memory and retry against the fresh state. If the precondition fails but the stored state already exactly matches the requested `content` and `path`, the server returns 200 instead of 409.



type: "content\_sha256"

"content\_sha256"

content\_sha256: optional string

Expected `content_sha256` of the stored memory (64 lowercase hexadecimal characters). Typically the `content_sha256` returned by a prior read or list call. Because the server applies no content normalization, clients can also compute this locally as the SHA-256 of the UTF-8 content bytes.

---

*Copyright © Anthropic. All rights reserved.*
