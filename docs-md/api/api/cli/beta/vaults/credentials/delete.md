# Delete Credential

Copy page

CLI

# Delete Credential

$ ant beta:vaults:credentials delete

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

Delete Credential

##### ParametersExpand Collapse

--vault-id: string

Path param: Path parameter vault\_id

--credential-id: string

Path param: Path parameter credential\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_deleted\_credential: object { id, type }

Confirmation of a deleted credential.

id: string

Unique identifier of the deleted credential.

type: "vault\_credential\_deleted"

"vault\_credential\_deleted"

Delete Credential

CLI

```shiki
ant beta:vaults:credentials delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv \
  --credential-id vcrd_011CZkZEMt8gZan2iYOQfSkw
```

Response 200

```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "type": "vault_credential_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
