# Vaults

Copy page



Go

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

client.Beta.Vaults.New(ctx, params) (\*[BetaManagedAgentsVault](api/beta/vaults.md), error)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

client.Beta.Vaults.List(ctx, params) (\*PageCursor[[BetaManagedAgentsVault](api/beta/vaults.md)], error)

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

client.Beta.Vaults.Get(ctx, vaultID, query) (\*[BetaManagedAgentsVault](api/beta/vaults.md), error)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

client.Beta.Vaults.Update(ctx, vaultID, params) (\*[BetaManagedAgentsVault](api/beta/vaults.md), error)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

client.Beta.Vaults.Delete(ctx, vaultID, body) (\*[BetaManagedAgentsDeletedVault](api/beta/vaults.md), error)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

client.Beta.Vaults.Archive(ctx, vaultID, body) (\*[BetaManagedAgentsVault](api/beta/vaults.md), error)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse



type BetaManagedAgentsDeletedVault struct{…}

Confirmation of a deleted vault.

ID string

Unique identifier of the deleted vault.

Type BetaManagedAgentsDeletedVaultType



type BetaManagedAgentsVault struct{…}

A vault that stores credentials for use by agents during sessions.

ID string

Unique identifier for the vault.

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

DisplayName string

Human-readable name for the vault.

Metadata map[string, string]

Arbitrary key-value metadata attached to the vault.

Type BetaManagedAgentsVaultType

UpdatedAt Time

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

client.Beta.Vaults.Credentials.New(ctx, vaultID, params) (\*[BetaManagedAgentsCredential](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

client.Beta.Vaults.Credentials.List(ctx, vaultID, params) (\*PageCursor[[BetaManagedAgentsCredential](api/beta/vaults/credentials.md)], error)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

client.Beta.Vaults.Credentials.Get(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta/vaults/credentials.md), error)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

client.Beta.Vaults.Credentials.Update(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

client.Beta.Vaults.Credentials.Delete(ctx, credentialID, params) (\*[BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md), error)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

client.Beta.Vaults.Credentials.Archive(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

client.Beta.Vaults.Credentials.MCPOAuthValidate(ctx, credentialID, params) (\*[BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

---

*Copyright © Anthropic. All rights reserved.*
