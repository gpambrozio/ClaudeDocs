# Vaults

Copy page

Go

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

client.Beta.Vaults.New(ctx, params) (\*[BetaManagedAgentsVault](api/beta.md), error)

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

client.Beta.Vaults.List(ctx, params) (\*PageCursor[[BetaManagedAgentsVault](api/beta.md)], error)

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

client.Beta.Vaults.Get(ctx, vaultID, query) (\*[BetaManagedAgentsVault](api/beta.md), error)

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

client.Beta.Vaults.Update(ctx, vaultID, params) (\*[BetaManagedAgentsVault](api/beta.md), error)

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

client.Beta.Vaults.Delete(ctx, vaultID, body) (\*[BetaManagedAgentsDeletedVault](api/beta.md), error)

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

client.Beta.Vaults.Archive(ctx, vaultID, body) (\*[BetaManagedAgentsVault](api/beta.md), error)

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

type BetaManagedAgentsDeletedVault struct{…}

Confirmation of a deleted vault.

ID string

Unique identifier of the deleted vault.

Type BetaManagedAgentsDeletedVaultType

type BetaManagedAgentsVault struct{…}

A vault that stores credentials for use by agents during sessions.

ID string

Unique identifier for the vault.

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

DisplayName string

Human-readable name for the vault.

Metadata map[string, string]

Arbitrary key-value metadata attached to the vault.

Type BetaManagedAgentsVaultType

UpdatedAt Time

A timestamp in RFC 3339 format

#### VaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

client.Beta.Vaults.Credentials.New(ctx, vaultID, params) (\*[BetaManagedAgentsCredential](api/beta.md), error)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

client.Beta.Vaults.Credentials.List(ctx, vaultID, params) (\*PageCursor[[BetaManagedAgentsCredential](api/beta.md)], error)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

client.Beta.Vaults.Credentials.Get(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta.md), error)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

client.Beta.Vaults.Credentials.Update(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

client.Beta.Vaults.Credentials.Delete(ctx, credentialID, params) (\*[BetaManagedAgentsDeletedCredential](api/beta.md), error)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

client.Beta.Vaults.Credentials.Archive(ctx, credentialID, params) (\*[BetaManagedAgentsCredential](api/beta.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

client.Beta.Vaults.Credentials.MCPOAuthValidate(ctx, credentialID, params) (\*[BetaManagedAgentsCredentialValidation](api/beta.md), error)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### ModelsExpand Collapse

type BetaManagedAgentsCredential struct{…}

A credential stored in a vault. Sensitive fields are never returned in responses.

ID string

Unique identifier for the credential.

ArchivedAt Time

A timestamp in RFC 3339 format

Auth BetaManagedAgentsCredentialAuthUnion

Authentication details for a credential.

Accepts one of the following:

type BetaManagedAgentsMCPOAuthAuthResponse struct{…}

OAuth credential details for an MCP server.

MCPServerURL string

URL of the MCP server this credential authenticates against.

Type BetaManagedAgentsMCPOAuthAuthResponseType

ExpiresAt Timeoptional

A timestamp in RFC 3339 format

Refresh [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md)optional

OAuth refresh token configuration returned in credential responses.

ClientID string

OAuth client ID.

TokenEndpoint string

Token endpoint URL used to refresh the access token.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion

Token endpoint requires no client authentication.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}

Token endpoint requires no client authentication.

Type BetaManagedAgentsTokenEndpointAuthNoneResponseType

type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}

Token endpoint uses HTTP Basic authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthBasicResponseType

type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}

Token endpoint uses POST body authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthPostResponseType

Resource stringoptional

OAuth resource indicator.

Scope stringoptional

OAuth scope for the refresh request.

type BetaManagedAgentsStaticBearerAuthResponse struct{…}

Static bearer token credential details for an MCP server.

MCPServerURL string

URL of the MCP server this credential authenticates against.

Type BetaManagedAgentsStaticBearerAuthResponseType

CreatedAt Time

A timestamp in RFC 3339 format

Metadata map[string, string]

Arbitrary key-value metadata attached to the credential.

Type BetaManagedAgentsCredentialType

UpdatedAt Time

A timestamp in RFC 3339 format

VaultID string

Identifier of the vault this credential belongs to.

DisplayName stringoptional

Human-readable name for the credential.

type BetaManagedAgentsCredentialValidation struct{…}

Result of live-probing a credential against its configured MCP server.

CredentialID string

Unique identifier of the credential that was validated.

HasRefreshToken bool

Whether the credential has a refresh token configured.

MCPProbe [BetaManagedAgentsMCPProbe](api/beta.md)

The failing step of an MCP validation probe.

HTTPResponse [BetaManagedAgentsRefreshHTTPResponse](api/beta.md)

An HTTP response captured during a credential validation probe.

Body string

Response body. May be truncated and has sensitive values scrubbed.

BodyTruncated bool

Whether `body` was truncated.

ContentType string

Value of the `Content-Type` response header.

StatusCode int64

HTTP status code.

Method string

The MCP method that failed (for example `initialize` or `tools/list`).

Refresh [BetaManagedAgentsRefreshObject](api/beta.md)

Outcome of a refresh-token exchange attempted during credential validation.

HTTPResponse [BetaManagedAgentsRefreshHTTPResponse](api/beta.md)

An HTTP response captured during a credential validation probe.

Body string

Response body. May be truncated and has sensitive values scrubbed.

BodyTruncated bool

Whether `body` was truncated.

ContentType string

Value of the `Content-Type` response header.

StatusCode int64

HTTP status code.

Status BetaManagedAgentsRefreshObjectStatus

Outcome of a refresh-token exchange attempted during credential validation.

Accepts one of the following:

const BetaManagedAgentsRefreshObjectStatusSucceeded BetaManagedAgentsRefreshObjectStatus = "succeeded"

const BetaManagedAgentsRefreshObjectStatusFailed BetaManagedAgentsRefreshObjectStatus = "failed"

const BetaManagedAgentsRefreshObjectStatusConnectError BetaManagedAgentsRefreshObjectStatus = "connect\_error"

const BetaManagedAgentsRefreshObjectStatusNoRefreshToken BetaManagedAgentsRefreshObjectStatus = "no\_refresh\_token"

Status [BetaManagedAgentsCredentialValidationStatus](api/beta.md)

Overall verdict of a credential validation probe.

Accepts one of the following:

const BetaManagedAgentsCredentialValidationStatusValid [BetaManagedAgentsCredentialValidationStatus](api/beta.md) = "valid"

const BetaManagedAgentsCredentialValidationStatusInvalid [BetaManagedAgentsCredentialValidationStatus](api/beta.md) = "invalid"

const BetaManagedAgentsCredentialValidationStatusUnknown [BetaManagedAgentsCredentialValidationStatus](api/beta.md) = "unknown"

Type BetaManagedAgentsCredentialValidationType

ValidatedAt Time

A timestamp in RFC 3339 format

VaultID string

Identifier of the vault containing the credential.

type BetaManagedAgentsCredentialValidationStatus string

Overall verdict of a credential validation probe.

Accepts one of the following:

const BetaManagedAgentsCredentialValidationStatusValid [BetaManagedAgentsCredentialValidationStatus](api/beta.md) = "valid"

const BetaManagedAgentsCredentialValidationStatusInvalid [BetaManagedAgentsCredentialValidationStatus](api/beta.md) = "invalid"

const BetaManagedAgentsCredentialValidationStatusUnknown [BetaManagedAgentsCredentialValidationStatus](api/beta.md) = "unknown"

type BetaManagedAgentsDeletedCredential struct{…}

Confirmation of a deleted credential.

ID string

Unique identifier of the deleted credential.

Type BetaManagedAgentsDeletedCredentialType

type BetaManagedAgentsMCPOAuthAuthResponse struct{…}

OAuth credential details for an MCP server.

MCPServerURL string

URL of the MCP server this credential authenticates against.

Type BetaManagedAgentsMCPOAuthAuthResponseType

ExpiresAt Timeoptional

A timestamp in RFC 3339 format

Refresh [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md)optional

OAuth refresh token configuration returned in credential responses.

ClientID string

OAuth client ID.

TokenEndpoint string

Token endpoint URL used to refresh the access token.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion

Token endpoint requires no client authentication.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}

Token endpoint requires no client authentication.

Type BetaManagedAgentsTokenEndpointAuthNoneResponseType

type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}

Token endpoint uses HTTP Basic authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthBasicResponseType

type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}

Token endpoint uses POST body authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthPostResponseType

Resource stringoptional

OAuth resource indicator.

Scope stringoptional

OAuth scope for the refresh request.

type BetaManagedAgentsMCPOAuthCreateParamsResp struct{…}

Parameters for creating an MCP OAuth credential.

AccessToken string

OAuth access token.

MCPServerURL string

URL of the MCP server this credential authenticates against.

Type BetaManagedAgentsMCPOAuthCreateParamsType

ExpiresAt Timeoptional

A timestamp in RFC 3339 format

Refresh [BetaManagedAgentsMCPOAuthRefreshParamsResp](api/beta.md)optional

OAuth refresh token parameters for creating a credential with refresh support.

ClientID string

OAuth client ID.

RefreshToken string

OAuth refresh token.

TokenEndpoint string

Token endpoint URL used to refresh the access token.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp

Token endpoint requires no client authentication.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}

Token endpoint requires no client authentication.

Type BetaManagedAgentsTokenEndpointAuthNoneParamType

type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}

Token endpoint uses HTTP Basic authentication with client credentials.

ClientSecret string

OAuth client secret.

Type BetaManagedAgentsTokenEndpointAuthBasicParamType

type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}

Token endpoint uses POST body authentication with client credentials.

ClientSecret string

OAuth client secret.

Type BetaManagedAgentsTokenEndpointAuthPostParamType

Resource stringoptional

OAuth resource indicator.

Scope stringoptional

OAuth scope for the refresh request.

type BetaManagedAgentsMCPOAuthRefreshParamsResp struct{…}

OAuth refresh token parameters for creating a credential with refresh support.

ClientID string

OAuth client ID.

RefreshToken string

OAuth refresh token.

TokenEndpoint string

Token endpoint URL used to refresh the access token.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshParamsTokenEndpointAuthUnionResp

Token endpoint requires no client authentication.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}

Token endpoint requires no client authentication.

Type BetaManagedAgentsTokenEndpointAuthNoneParamType

type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}

Token endpoint uses HTTP Basic authentication with client credentials.

ClientSecret string

OAuth client secret.

Type BetaManagedAgentsTokenEndpointAuthBasicParamType

type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}

Token endpoint uses POST body authentication with client credentials.

ClientSecret string

OAuth client secret.

Type BetaManagedAgentsTokenEndpointAuthPostParamType

Resource stringoptional

OAuth resource indicator.

Scope stringoptional

OAuth scope for the refresh request.

type BetaManagedAgentsMCPOAuthRefreshResponse struct{…}

OAuth refresh token configuration returned in credential responses.

ClientID string

OAuth client ID.

TokenEndpoint string

Token endpoint URL used to refresh the access token.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshResponseTokenEndpointAuthUnion

Token endpoint requires no client authentication.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}

Token endpoint requires no client authentication.

Type BetaManagedAgentsTokenEndpointAuthNoneResponseType

type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}

Token endpoint uses HTTP Basic authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthBasicResponseType

type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}

Token endpoint uses POST body authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthPostResponseType

Resource stringoptional

OAuth resource indicator.

Scope stringoptional

OAuth scope for the refresh request.

type BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp struct{…}

Parameters for updating OAuth refresh token configuration.

RefreshToken stringoptional

Updated OAuth refresh token.

Scope stringoptional

Updated OAuth scope for the refresh request.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionRespoptional

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}

Updated HTTP Basic authentication parameters for the token endpoint.

Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType

ClientSecret stringoptional

Updated OAuth client secret.

type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}

Updated POST body authentication parameters for the token endpoint.

Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType

ClientSecret stringoptional

Updated OAuth client secret.

type BetaManagedAgentsMCPOAuthUpdateParamsResp struct{…}

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

Type BetaManagedAgentsMCPOAuthUpdateParamsType

AccessToken stringoptional

Updated OAuth access token.

ExpiresAt Timeoptional

A timestamp in RFC 3339 format

Refresh [BetaManagedAgentsMCPOAuthRefreshUpdateParamsResp](api/beta.md)optional

Parameters for updating OAuth refresh token configuration.

RefreshToken stringoptional

Updated OAuth refresh token.

Scope stringoptional

Updated OAuth scope for the refresh request.

TokenEndpointAuth BetaManagedAgentsMCPOAuthRefreshUpdateParamsTokenEndpointAuthUnionRespoptional

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}

Updated HTTP Basic authentication parameters for the token endpoint.

Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType

ClientSecret stringoptional

Updated OAuth client secret.

type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}

Updated POST body authentication parameters for the token endpoint.

Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType

ClientSecret stringoptional

Updated OAuth client secret.

type BetaManagedAgentsMCPProbe struct{…}

The failing step of an MCP validation probe.

HTTPResponse [BetaManagedAgentsRefreshHTTPResponse](api/beta.md)

An HTTP response captured during a credential validation probe.

Body string

Response body. May be truncated and has sensitive values scrubbed.

BodyTruncated bool

Whether `body` was truncated.

ContentType string

Value of the `Content-Type` response header.

StatusCode int64

HTTP status code.

Method string

The MCP method that failed (for example `initialize` or `tools/list`).

type BetaManagedAgentsRefreshHTTPResponse struct{…}

An HTTP response captured during a credential validation probe.

Body string

Response body. May be truncated and has sensitive values scrubbed.

BodyTruncated bool

Whether `body` was truncated.

ContentType string

Value of the `Content-Type` response header.

StatusCode int64

HTTP status code.

type BetaManagedAgentsRefreshObject struct{…}

Outcome of a refresh-token exchange attempted during credential validation.

HTTPResponse [BetaManagedAgentsRefreshHTTPResponse](api/beta.md)

An HTTP response captured during a credential validation probe.

Body string

Response body. May be truncated and has sensitive values scrubbed.

BodyTruncated bool

Whether `body` was truncated.

ContentType string

Value of the `Content-Type` response header.

StatusCode int64

HTTP status code.

Status BetaManagedAgentsRefreshObjectStatus

Outcome of a refresh-token exchange attempted during credential validation.

Accepts one of the following:

const BetaManagedAgentsRefreshObjectStatusSucceeded BetaManagedAgentsRefreshObjectStatus = "succeeded"

const BetaManagedAgentsRefreshObjectStatusFailed BetaManagedAgentsRefreshObjectStatus = "failed"

const BetaManagedAgentsRefreshObjectStatusConnectError BetaManagedAgentsRefreshObjectStatus = "connect\_error"

const BetaManagedAgentsRefreshObjectStatusNoRefreshToken BetaManagedAgentsRefreshObjectStatus = "no\_refresh\_token"

type BetaManagedAgentsStaticBearerAuthResponse struct{…}

Static bearer token credential details for an MCP server.

MCPServerURL string

URL of the MCP server this credential authenticates against.

Type BetaManagedAgentsStaticBearerAuthResponseType

type BetaManagedAgentsStaticBearerCreateParamsResp struct{…}

Parameters for creating a static bearer token credential.

Token string

Static bearer token value.

MCPServerURL string

URL of the MCP server this credential authenticates against.

Type BetaManagedAgentsStaticBearerCreateParamsType

type BetaManagedAgentsStaticBearerUpdateParamsResp struct{…}

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

Type BetaManagedAgentsStaticBearerUpdateParamsType

Token stringoptional

Updated static bearer token value.

type BetaManagedAgentsTokenEndpointAuthBasicParamResp struct{…}

Token endpoint uses HTTP Basic authentication with client credentials.

ClientSecret string

OAuth client secret.

Type BetaManagedAgentsTokenEndpointAuthBasicParamType

type BetaManagedAgentsTokenEndpointAuthBasicResponse struct{…}

Token endpoint uses HTTP Basic authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthBasicResponseType

type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamResp struct{…}

Updated HTTP Basic authentication parameters for the token endpoint.

Type BetaManagedAgentsTokenEndpointAuthBasicUpdateParamType

ClientSecret stringoptional

Updated OAuth client secret.

type BetaManagedAgentsTokenEndpointAuthNoneParamResp struct{…}

Token endpoint requires no client authentication.

Type BetaManagedAgentsTokenEndpointAuthNoneParamType

type BetaManagedAgentsTokenEndpointAuthNoneResponse struct{…}

Token endpoint requires no client authentication.

Type BetaManagedAgentsTokenEndpointAuthNoneResponseType

type BetaManagedAgentsTokenEndpointAuthPostParamResp struct{…}

Token endpoint uses POST body authentication with client credentials.

ClientSecret string

OAuth client secret.

Type BetaManagedAgentsTokenEndpointAuthPostParamType

type BetaManagedAgentsTokenEndpointAuthPostResponse struct{…}

Token endpoint uses POST body authentication with client credentials.

Type BetaManagedAgentsTokenEndpointAuthPostResponseType

type BetaManagedAgentsTokenEndpointAuthPostUpdateParamResp struct{…}

Updated POST body authentication parameters for the token endpoint.

Type BetaManagedAgentsTokenEndpointAuthPostUpdateParamType

ClientSecret stringoptional

Updated OAuth client secret.

---

*Copyright © Anthropic. All rights reserved.*
