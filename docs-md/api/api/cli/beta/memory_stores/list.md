# List memory stores

Copy page

CLI

# List memory stores

$ ant beta:memory-stores list

GET/v1/memory\_stores

List memory stores

##### ParametersExpand Collapse

--created-at-gte: optional string

Query param: Return only stores whose `created_at` is at or after this time (inclusive). Sent on the wire as `created_at[gte]`.

--created-at-lte: optional string

Query param: Return only stores whose `created_at` is at or before this time (inclusive). Sent on the wire as `created_at[lte]`.

--include-archived: optional boolean

Query param: When `true`, archived stores are included in the results. Defaults to `false` (archived stores are excluded).

--limit: optional number

Query param: Maximum number of stores to return per page. Must be between 1 and 100. Defaults to 20 when omitted.

--page: optional string

Query param: Opaque pagination cursor (a `page_...` value). Pass the `next_page` value from a previous response to fetch the next page; omit for the first page.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaManagedAgentsListMemoryStoresResponse: object { data, next\_page }

A page of `memory_store` results, ordered by `created_at` descending (newest first).

data: optional array of [BetaManagedAgentsMemoryStore](api/beta.md) { id, created\_at, name, 5 more }

Memory stores on this page, newest first. Empty when there are no stores matching the filters.

id: string

Unique identifier for the memory store (a `memstore_...` tagged ID). Use this when attaching the store to a session, or in the `{memory_store_id}` path parameter of subsequent calls.

created\_at: string

A timestamp in RFC 3339 format

name: string

Human-readable name for the store. 1–255 characters. The store's mount-path slug under `/mnt/memory/` is derived from this name.

type: "memory\_store"

"memory\_store"

updated\_at: string

A timestamp in RFC 3339 format

archived\_at: optional string

A timestamp in RFC 3339 format

description: optional string

Free-text description of what the store contains, up to 1024 characters. Included in the agent's system prompt when the store is attached, so word it to be useful to the agent. Empty string when unset.

metadata: optional map[string]

Arbitrary key-value tags for your own bookkeeping (such as the end user a store belongs to). Up to 16 pairs; keys 1–64 characters; values up to 512 characters. Returned on retrieve/list but not filterable.

next\_page: optional string

Opaque cursor for the next page (a `page_...` value). Pass as `page` on the next request. `null` when there are no more results.

List memory stores

CLI

```shiki
ant beta:memory-stores list \
  --api-key my-anthropic-api-key
```

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "name": "name",
      "type": "memory_store",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      }
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2019-12-27T18:11:19.117Z",
      "name": "name",
      "type": "memory_store",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      }
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
