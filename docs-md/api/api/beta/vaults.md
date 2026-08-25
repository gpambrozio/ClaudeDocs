# Vaults

Copy page



cURL

# Vaults

##### [Create Vault](api/http/beta/vaults/create.md)

POST/v1/vaults

##### [List Vaults](api/http/beta/vaults/list.md)

GET/v1/vaults

##### [Get Vault](api/http/beta/vaults/retrieve.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/http/beta/vaults/update.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/http/beta/vaults/delete.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/http/beta/vaults/archive.md)

POST/v1/vaults/{vault\_id}/archive

##### Models



BetaManagedAgentsDeletedVault object{ id, type }

Confirmation of a deleted vault.

id: string

Unique identifier of the deleted vault.

type: "vault\_deleted"



BetaManagedAgentsVault object{ id, archived\_at, created\_at, 4 more }

A vault that stores credentials for use by agents during sessions.

id: string

Unique identifier for the vault.



archived\_at: string or null

A timestamp in RFC 3339 format

formatdate-time



created\_at: string

A timestamp in RFC 3339 format

formatdate-time

display\_name: string

Human-readable name for the vault.

metadata: map[string]

Arbitrary key-value metadata attached to the vault.

type: "vault"



updated\_at: string

A timestamp in RFC 3339 format

formatdate-time

#### Vaults[Credentials](api/http/beta/vaults/credentials.md)

##### [Create Credential](api/http/beta/vaults/credentials/create.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/http/beta/vaults/credentials/list.md)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/http/beta/vaults/credentials/retrieve.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/http/beta/vaults/credentials/update.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/http/beta/vaults/credentials/delete.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/http/beta/vaults/credentials/archive.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/http/beta/vaults/credentials/mcp_oauth_validate.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

---

*Copyright © Anthropic. All rights reserved.*
