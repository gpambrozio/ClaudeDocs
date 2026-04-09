# Delete Vault

Copy page

CLI

# Delete Vault

$ ant beta:vaults delete

DELETE/v1/vaults/{vault\_id}

Delete Vault

##### ParametersExpand Collapse

--vault-id: string

Path parameter vault\_id

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

beta\_managed\_agents\_deleted\_vault: object { id, type }

Confirmation of a deleted vault.

id: string

Unique identifier of the deleted vault.

type: "vault\_deleted"

"vault\_deleted"

Delete Vault

CLI

```shiki
ant beta:vaults delete \
  --api-key my-anthropic-api-key \
  --vault-id vlt_011CZkZDLs7fYzm1hXNPeRjv
```

Response 200

```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "type": "vault_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
