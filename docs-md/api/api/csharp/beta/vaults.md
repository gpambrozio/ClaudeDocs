# Vaults

Copy page

C#

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

[BetaManagedAgentsVault](api/beta.md) Beta.Vaults.Create(VaultCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

[VaultListPageResponse](api/beta.md) Beta.Vaults.List(VaultListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

[BetaManagedAgentsVault](api/beta.md) Beta.Vaults.Retrieve(VaultRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

[BetaManagedAgentsVault](api/beta.md) Beta.Vaults.Update(VaultUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

[BetaManagedAgentsDeletedVault](api/beta.md) Beta.Vaults.Delete(VaultDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

[BetaManagedAgentsVault](api/beta.md) Beta.Vaults.Archive(VaultArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedVault:

Confirmation of a deleted vault.

required string ID

Unique identifier of the deleted vault.

required Type Type

class BetaManagedAgentsVault:

A vault that stores credentials for use by agents during sessions.

required string ID

Unique identifier for the vault.

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string DisplayName

Human-readable name for the vault.

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata attached to the vault.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Create(CredentialCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

[CredentialListPageResponse](api/beta.md) Beta.Vaults.Credentials.List(CredentialListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Retrieve(CredentialRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Update(CredentialUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

[BetaManagedAgentsDeletedCredential](api/beta.md) Beta.Vaults.Credentials.Delete(CredentialDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

[BetaManagedAgentsCredential](api/beta.md) Beta.Vaults.Credentials.Archive(CredentialArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsCredential:

A credential stored in a vault. Sensitive fields are never returned in responses.

required string ID

Unique identifier for the credential.

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required Auth Auth

Authentication details for a credential.

Accepts one of the following:

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)? Refresh

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata attached to the credential.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string VaultID

Identifier of the vault this credential belongs to.

string? DisplayName

Human-readable name for the credential.

class BetaManagedAgentsDeletedCredential:

Confirmation of a deleted credential.

required string ID

Unique identifier of the deleted credential.

required Type Type

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)? Refresh

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthCreateParams:

Parameters for creating an MCP OAuth credential.

required string AccessToken

OAuth access token.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshParams](api/beta.md)? Refresh

OAuth refresh token parameters for creating a credential with refresh support.

required string ClientID

OAuth client ID.

required string RefreshToken

OAuth refresh token.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshParams:

OAuth refresh token parameters for creating a credential with refresh support.

required string ClientID

OAuth client ID.

required string RefreshToken

OAuth refresh token.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshResponse:

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.

required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshUpdateParams:

Parameters for updating OAuth refresh token configuration.

string? RefreshToken

Updated OAuth refresh token.

string? Scope

Updated OAuth scope for the refresh request.

TokenEndpointAuth TokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsMcpOAuthUpdateParams:

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

required Type Type

string? AccessToken

Updated OAuth access token.

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format

[BetaManagedAgentsMcpOAuthRefreshUpdateParams](api/beta.md)? Refresh

Parameters for updating OAuth refresh token configuration.

string? RefreshToken

Updated OAuth refresh token.

string? Scope

Updated OAuth scope for the refresh request.

TokenEndpointAuth TokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

class BetaManagedAgentsStaticBearerCreateParams:

Parameters for creating a static bearer token credential.

required string Token

Static bearer token value.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

class BetaManagedAgentsStaticBearerUpdateParams:

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

required Type Type

string? Token

Updated static bearer token value.

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.

---

*Copyright © Anthropic. All rights reserved.*
