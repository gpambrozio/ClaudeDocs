# Vaults

Copy page



Ruby

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

beta.vaults.create(\*\*kwargs) -> [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

beta.vaults.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more } >

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

beta.vaults.retrieve(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

beta.vaults.update(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

beta.vaults.delete(vault\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedVault](api/beta/vaults.md) { id, type }

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

beta.vaults.archive(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta/vaults.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsDeletedVault { id, type } 

Confirmation of a deleted vault.

id: String

Unique identifier of the deleted vault.

type: :vault\_deleted



class BetaManagedAgentsVault { id, archived\_at, created\_at, 4 more } 

A vault that stores credentials for use by agents during sessions.

id: String

Unique identifier for the vault.

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

display\_name: String

Human-readable name for the vault.

metadata: Hash[Symbol, String]

Arbitrary key-value metadata attached to the vault.

type: :vault

updated\_at: Time

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

beta.vaults.credentials.create(vault\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

beta.vaults.credentials.list(vault\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more } >

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

beta.vaults.credentials.retrieve(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

beta.vaults.credentials.update(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

beta.vaults.credentials.delete(credential\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md) { id, type }

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

beta.vaults.credentials.archive(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

beta.vaults.credentials.mcp\_oauth\_validate(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md) { credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

---

*Copyright © Anthropic. All rights reserved.*
