# UpdateMemoryStore

Copy page

CLI

# UpdateMemoryStore

$ ant beta:memory-stores update

POST/v1/memory\_stores/{memory\_store\_id}

UpdateMemoryStore

##### ParametersExpand Collapse

--memory-store-id: string

Path param: Path parameter memory\_store\_id

--description: optional string

Body param

--metadata: optional map[string]

Body param: Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omit the field to preserve. The stored bag is limited to 16 keys (up to 64 chars each) with values up to 512 chars.

--name: optional string

Body param

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

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

UpdateMemoryStore

CLI

```shiki
ant beta:memory-stores update \
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
