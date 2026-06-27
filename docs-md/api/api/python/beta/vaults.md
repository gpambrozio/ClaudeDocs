# Vaults

Copy page



Python

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

beta.vaults.create(VaultCreateParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

beta.vaults.list(VaultListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsVault](api/beta/vaults.md)]

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

beta.vaults.retrieve(strvault\_id, VaultRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta/vaults.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

beta.vaults.update(strvault\_id, VaultUpdateParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

beta.vaults.delete(strvault\_id, VaultDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedVault](api/beta/vaults.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

beta.vaults.archive(strvault\_id, VaultArchiveParams\*\*kwargs)  -> [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsDeletedVault: …

Confirmation of a deleted vault.

id: str

Unique identifier of the deleted vault.

type: Literal["vault\_deleted"]



class BetaManagedAgentsVault: …

A vault that stores credentials for use by agents during sessions.

id: str

Unique identifier for the vault.

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: datetime

A timestamp in RFC 3339 format

display\_name: str

Human-readable name for the vault.

metadata: Dict[str, str]

Arbitrary key-value metadata attached to the vault.

type: Literal["vault"]

updated\_at: datetime

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

beta.vaults.credentials.create(strvault\_id, CredentialCreateParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

beta.vaults.credentials.list(strvault\_id, CredentialListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsCredential](api/beta/vaults/credentials.md)]

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

beta.vaults.credentials.retrieve(strcredential\_id, CredentialRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

beta.vaults.credentials.update(strcredential\_id, CredentialUpdateParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

beta.vaults.credentials.delete(strcredential\_id, CredentialDeleteParams\*\*kwargs)  -> [BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

beta.vaults.credentials.archive(strcredential\_id, CredentialArchiveParams\*\*kwargs)  -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

beta.vaults.credentials.mcp\_oauth\_validate(strcredential\_id, CredentialMCPOAuthValidateParams\*\*kwargs)  -> [BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

---

*Copyright © Anthropic. All rights reserved.*
