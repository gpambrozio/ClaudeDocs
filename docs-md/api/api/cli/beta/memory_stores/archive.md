# ArchiveMemoryStore

Copy page

CLI

# ArchiveMemoryStore

$ ant beta:memory-stores archive

POST/v1/memory\_stores/{memory\_store\_id}/archive

ArchiveMemoryStore

##### ParametersExpand Collapse

--memory-store-id: string

Path parameter memory\_store\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_memory\_store: object { id, type, archived\_at, 5 more }

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

ArchiveMemoryStore

CLI

```shiki
ant beta:memory-stores archive \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

Response 200

```shiki
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
```

##### Returns Examples

Response 200

```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
