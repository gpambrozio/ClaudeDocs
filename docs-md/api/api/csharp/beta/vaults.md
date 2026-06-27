# Vaults

Copy page



C#

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

[BetaManagedAgentsVault](api/beta/vaults.md) Beta.Vaults.Create(VaultCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

[VaultListPageResponse](api/beta/vaults.md) Beta.Vaults.List(VaultListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

[BetaManagedAgentsVault](api/beta/vaults.md) Beta.Vaults.Retrieve(VaultRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

[BetaManagedAgentsVault](api/beta/vaults.md) Beta.Vaults.Update(VaultUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

[BetaManagedAgentsDeletedVault](api/beta/vaults.md) Beta.Vaults.Delete(VaultDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

[BetaManagedAgentsVault](api/beta/vaults.md) Beta.Vaults.Archive(VaultArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse



class BetaManagedAgentsDeletedVault:

Confirmation of a deleted vault.

required string ID

Unique identifier of the deleted vault.

required Type Type



class BetaManagedAgentsVault:

A vault that stores credentials for use by agents during sessions.

required string ID

Unique identifier for the vault.

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string DisplayName

Human-readable name for the vault.

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata attached to the vault.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Create(CredentialCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

[CredentialListPageResponse](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.List(CredentialListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Retrieve(CredentialRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Update(CredentialUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

[BetaManagedAgentsDeletedCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Delete(CredentialDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

[BetaManagedAgentsCredential](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.Archive(CredentialArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

[BetaManagedAgentsCredentialValidation](api/beta/vaults/credentials.md) Beta.Vaults.Credentials.McpOAuthValidate(CredentialMcpOAuthValidateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

---

*Copyright © Anthropic. All rights reserved.*
