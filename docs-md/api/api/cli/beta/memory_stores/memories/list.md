# ListMemories

Copy page

CLI

# ListMemories

$ ant beta:memory-stores:memories list

GET/v1/memory\_stores/{memory\_store\_id}/memories

ListMemories

##### ParametersExpand Collapse

--memory-store-id: string

Path param: Path parameter memory\_store\_id

--depth: optional number

Query param: Query parameter for depth

--limit: optional number

Query param: Query parameter for limit

--order: optional "asc" or "desc"

Query param: Query parameter for order

--order-by: optional string

Query param: Query parameter for order\_by

--page: optional string

Query param: Query parameter for page

--path-prefix: optional string

Query param: Optional path prefix filter (raw string-prefix match; include a trailing slash for directory-scoped lists). This value appears in request URLs. Do not include secrets or personally identifiable information.

--view: optional "basic" or "full"

Query param: Query parameter for view

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaManagedAgentsListMemoriesResult: object { data, next\_page }

data: optional array of [BetaManagedAgentsMemoryListItem](api/beta.md)

beta\_managed\_agents\_memory: object { id, content\_sha256, content\_size\_bytes, 7 more }

id: string

content\_sha256: string

content\_size\_bytes: number

created\_at: string

A timestamp in RFC 3339 format

memory\_store\_id: string

memory\_version\_id: string

path: string

type: "memory"

"memory"

updated\_at: string

A timestamp in RFC 3339 format

content: optional string

beta\_managed\_agents\_memory\_prefix: object { path, type }

path: string

type: "memory\_prefix"

"memory\_prefix"

next\_page: optional string

ListMemories

CLI

```shiki
ant beta:memory-stores:memories list \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

Response 200

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
