# Vaults

Copy page



PHP

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

$client->beta->vaults->create(string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

$client->beta->vaults->list(?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaManagedAgentsVault](api/beta/vaults.md)>

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

$client->beta->vaults->retrieve(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta/vaults.md)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

$client->beta->vaults->update(string vaultID, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

$client->beta->vaults->delete(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsDeletedVault](api/beta/vaults.md)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

$client->beta->vaults->archive(string vaultID, ?list<AnthropicBeta> betas): [BetaManagedAgentsVault](api/beta/vaults.md)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse



[BetaManagedAgentsDeletedVault](api/beta/vaults.md)

string id

Unique identifier of the deleted vault.

Type type



[BetaManagedAgentsVault](api/beta/vaults.md)

string id

Unique identifier for the vault.

?\Datetime archivedAt

A timestamp in RFC 3339 format

\Datetime createdAt

A timestamp in RFC 3339 format

string displayName

Human-readable name for the vault.

array<string,string> metadata

Arbitrary key-value metadata attached to the vault.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

$client->beta->vaults->credentials->create(string vaultID, [Auth](api/beta/vaults/credentials/create.md) auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsCredential](api/beta/vaults/credentials.md)>

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

$client->beta->vaults->credentials->retrieve(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta/vaults/credentials.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

$client->beta->vaults->credentials->update(string credentialID, string vaultID, ?[Auth](api/beta/vaults/credentials/update.md) auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedCredential](api/beta/vaults/credentials.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

$client->beta->vaults->credentials->archive(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredentialValidation](api/beta/vaults/credentials.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

---

*Copyright © Anthropic. All rights reserved.*
