# Delete Session Resource

Copy page

CLI

# Delete Session Resource

$ ant beta:sessions:resources delete

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

Delete Session Resource

##### ParametersExpand Collapse

--session-id: string

Path param: Path parameter session\_id

--resource-id: string

Path param: Path parameter resource\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_delete\_session\_resource: object { id, type }

Confirmation of resource deletion.

id: string

type: "session\_resource\_deleted"

"session\_resource\_deleted"

Delete Session Resource

CLI

```shiki
ant beta:sessions:resources delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7 \
  --resource-id sesrsc_011CZkZBJq5dWxk9fVLNcPht
```

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "sesrsc_011CZkZBJq5dWxk9fVLNcPht",
  "type": "session_resource_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
