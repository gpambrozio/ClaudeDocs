# List Vaults

Copy page

CLI

# List Vaults

$ ant beta:vaults list

GET/v1/vaults

List Vaults

##### ParametersExpand Collapse

--include-archived: optional boolean

Query param: Whether to include archived vaults in the results.

--limit: optional number

Query param: Maximum number of vaults to return per page. Defaults to 20, maximum 100.

--page: optional string

Query param: Opaque pagination token from a previous `list_vaults` response.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaManagedAgentsListVaultsResponse: object { data, next\_page }

Response containing a paginated list of vaults.

data: optional array of [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

List of vaults.

id: string

Unique identifier for the vault.

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

display\_name: string

Human-readable name for the vault.

metadata: map[string]

Arbitrary key-value metadata attached to the vault.

type: "vault"

"vault"

updated\_at: string

A timestamp in RFC 3339 format

next\_page: optional string

Pagination token for the next page, or null if no more results.

List Vaults

CLI

```shiki
ant beta:vaults list \
  --api-key my-anthropic-api-key
```

Response 200

```shiki
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
    {
      "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
      "archived_at": null,
      "created_at": "2026-03-15T10:00:00Z",
      "display_name": "Example vault",
      "metadata": {
        "environment": "production"
      },
      "type": "vault",
      "updated_at": "2026-03-15T10:00:00Z"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
