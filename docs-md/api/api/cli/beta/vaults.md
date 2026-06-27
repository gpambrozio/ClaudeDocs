# Vaults

Copy page



CLI

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

$ ant beta:vaults create

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

$ ant beta:vaults list

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

$ ant beta:vaults retrieve

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

$ ant beta:vaults update

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

$ ant beta:vaults delete

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

$ ant beta:vaults archive

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse



beta\_managed\_agents\_deleted\_vault: object { id, type } 

Confirmation of a deleted vault.

id: string

Unique identifier of the deleted vault.



type: "vault\_deleted"

"vault\_deleted"



beta\_managed\_agents\_vault: object { id, archived\_at, created\_at, 4 more } 

A vault that stores credentials for use by agents during sessions.

id: string

Unique identifier for the vault.

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

display\_name: string

Human-readable name for the vault.

metadata: map[string]

Arbitrary key-value metadata attached to the vault.



type: "vault"

"vault"

updated\_at: string

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

$ ant beta:vaults:credentials create

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

$ ant beta:vaults:credentials list

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

$ ant beta:vaults:credentials retrieve

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

$ ant beta:vaults:credentials update

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

$ ant beta:vaults:credentials delete

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

$ ant beta:vaults:credentials archive

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

$ ant beta:vaults:credentials mcp-oauth-validate

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

---

*Copyright © Anthropic. All rights reserved.*
