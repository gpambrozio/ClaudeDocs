# Delete a memory store

Copy page



CLI

# Delete a memory store

$ ant beta:memory-stores delete

DELETE/v1/memory\_stores/{memory\_store\_id}

Delete a memory store

##### ParametersExpand Collapse

--memory-store-id: string

Path parameter memory\_store\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



beta\_managed\_agents\_deleted\_memory\_store: object { id, type } 

Confirmation that a `memory_store` was deleted.

id: string

ID of the deleted memory store (a `memstore_...` identifier). The store and all its memories and versions are no longer retrievable.



type: "memory\_store\_deleted"

"memory\_store\_deleted"

Delete a memory store

CLI

```shiki
ant beta:memory-stores delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id
```

Response 200



```shiki
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "type": "memory_store_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
