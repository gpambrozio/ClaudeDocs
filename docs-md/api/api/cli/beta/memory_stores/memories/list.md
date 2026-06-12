# List memories

Copy page

SDK language

CLI

# List memories

$ ant beta:memory-stores:memories list

GET/v1/memory\_stores/{memory\_store\_id}/memories

List memories

##### ParametersExpand Collapse

--memory-store-id: string

Path param: Path parameter memory\_store\_id

--depth: optional number

Query param: Query parameter for depth

--limit: optional number

Query param: Query parameter for limit

--order: optional "asc" or "desc"

Query param: Query parameter for order

--order-by: optional string

Query param: Query parameter for order\_by

--page: optional string

Query param: Query parameter for page

--path-prefix: optional string

Query param: Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

--view: optional "basic" or "full"

Query param: Query parameter for view

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



BetaManagedAgentsListMemoriesResult: object { data, next\_page } 

Response payload for [List memories](api/beta/memory_stores/memories/list.md).



data: optional array of [BetaManagedAgentsMemoryListItem](api/beta.md)

One page of results. Each item is either a `memory` object or, when `depth` was set, a `memory_prefix` rollup marker. Items appear in the requested `order_by`/`order`.

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

next\_page: optional string

Opaque cursor for the next page (a `page_...` value), or `null` if there are no more results. Pass as `page` on the next request.

List memories

CLI

```shiki
ant beta:memory-stores:memories list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_store_id": "memory_store_id",
      "memory_version_id": "memory_version_id",
      "path": "path",
      "type": "memory",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "content": "content"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "content_sha256": "content_sha256",
      "content_size_bytes": 0,
      "created_at": "2019-12-27T18:11:19.117Z",
      "memory_store_id": "memory_store_id",
      "memory_version_id": "memory_version_id",
      "path": "path",
      "type": "memory",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "content": "content"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
