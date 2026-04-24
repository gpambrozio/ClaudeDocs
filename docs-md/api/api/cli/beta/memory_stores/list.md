# ListMemoryStores

Copy page

CLI

# ListMemoryStores

$ ant beta:memory-stores list

GET/v1/memory\_stores

ListMemoryStores

##### ParametersExpand Collapse

--created-at-gte: optional string

Query param: Return stores created at or after this time (inclusive).

--created-at-lte: optional string

Query param: Return stores created at or before this time (inclusive).

--include-archived: optional boolean

Query param: Query parameter for include\_archived

--limit: optional number

Query param: Query parameter for limit

--page: optional string

Query param: Query parameter for page

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaManagedAgentsListMemoryStoresResponse: object { data, next\_page }

data: optional array of [BetaManagedAgentsMemoryStore](api/beta.md) { id, type, archived\_at, 5 more }

id: string

type: "memory\_store"

"memory\_store"

archived\_at: optional string

A timestamp in RFC 3339 format

created\_at: optional string

A timestamp in RFC 3339 format

description: optional string

metadata: optional map[string]

name: optional string

updated\_at: optional string

A timestamp in RFC 3339 format

next\_page: optional string

ListMemoryStores

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
      "type": "memory_store",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "updated_at": "2019-12-27T18:11:19.117Z"
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
      "type": "memory_store",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "created_at": "2019-12-27T18:11:19.117Z",
      "description": "description",
      "metadata": {
        "foo": "string"
      },
      "name": "name",
      "updated_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
