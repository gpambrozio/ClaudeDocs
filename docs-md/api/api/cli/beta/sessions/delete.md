# Delete Session

Copy page

CLI

# Delete Session

$ ant beta:sessions delete

DELETE/v1/sessions/{session\_id}

Delete Session

##### ParametersExpand Collapse

--session-id: string

Path parameter session\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_deleted\_session: object { id, type }

Confirmation that a `session` has been permanently deleted.

id: string

type: "session\_deleted"

"session\_deleted"

Delete Session

CLI

```shiki
ant beta:sessions delete \
  --api-key my-anthropic-api-key \
  --session-id sesn_011CZkZAtmR3yMPDzynEDxu7
```

Response 200

```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "sesn_011CZkZAtmR3yMPDzynEDxu7",
  "type": "session_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
