# DeleteMemoryStore

Copy page

CLI

# DeleteMemoryStore

$ ant beta:memory-stores delete

DELETE/v1/memory\_stores/{memory\_store\_id}

DeleteMemoryStore

##### ParametersExpand Collapse

--memory-store-id: string

Path parameter memory\_store\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_deleted\_memory\_store: object { id, type }

id: string

type: "memory\_store\_deleted"

"memory\_store\_deleted"

DeleteMemoryStore

CLI

```shiki
ant beta:memory-stores delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

Response 200

```shiki
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
