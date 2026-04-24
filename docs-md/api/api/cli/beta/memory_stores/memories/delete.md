# DeleteMemory

Copy page

CLI

# DeleteMemory

$ ant beta:memory-stores:memories delete

DELETE/v1/memory\_stores/{memory\_store\_id}/memories/{memory\_id}

DeleteMemory

##### ParametersExpand Collapse

--memory-store-id: string

Path param: Path parameter memory\_store\_id

--memory-id: string

Path param: Path parameter memory\_id

--expected-content-sha256: optional string

Query param: Query parameter for expected\_content\_sha256

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_deleted\_memory: object { id, type }

id: string

type: "memory\_deleted"

"memory\_deleted"

DeleteMemory

CLI

```shiki
ant beta:memory-stores:memories delete \
  --api-key my-anthropic-api-key \
  --memory-store-id memory_store_id \
  --memory-id memory_id
```

Response 200

```shiki
{
  "id": "id",
  "type": "memory_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "type": "memory_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
