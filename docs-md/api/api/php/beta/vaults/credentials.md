# Credentials

Copy page

SDK language

PHP

# Credentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

$client->beta->vaults->credentials->create(string vaultID, [Auth](api/beta/vaults/credentials/create.md) auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

$client->beta->vaults->credentials->list(string vaultID, ?bool includeArchived, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[ManagedAgentsCredential](api/beta.md)>

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

$client->beta->vaults->credentials->retrieve(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

$client->beta->vaults->credentials->update(string credentialID, string vaultID, ?[Auth](api/beta/vaults/credentials/update.md) auth, ?string displayName, ?array<string,string> metadata, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

$client->beta->vaults->credentials->delete(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsDeletedCredential](api/beta.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

$client->beta->vaults->credentials->archive(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredential](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

$client->beta->vaults->credentials->mcpOAuthValidate(string credentialID, string vaultID, ?list<AnthropicBeta> betas): [ManagedAgentsCredentialValidation](api/beta.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### ModelsExpand Collapse

[ManagedAgentsCredential](api/beta.md)

string id

Unique identifier for the credential.

?\Datetime archivedAt

A timestamp in RFC 3339 format

Auth auth

Authentication details for a credential.

\Datetime createdAt

A timestamp in RFC 3339 format

array<string,string> metadata

Arbitrary key-value metadata attached to the credential.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string vaultID

Identifier of the vault this credential belongs to.

?string displayName

Human-readable name for the credential.

[ManagedAgentsCredentialValidation](api/beta.md)

string credentialID

Unique identifier of the credential that was validated.

bool hasRefreshToken

Whether the credential has a refresh token configured.

?[ManagedAgentsMCPProbe](api/beta.md) mcpProbe

The failing step of an MCP validation probe.

?[ManagedAgentsRefreshObject](api/beta.md) refresh

Outcome of a refresh-token exchange attempted during credential validation.

[ManagedAgentsCredentialValidationStatus](api/beta.md) status

Overall verdict of a credential validation probe.

Type type

\Datetime validatedAt

A timestamp in RFC 3339 format

string vaultID

Identifier of the vault containing the credential.

[ManagedAgentsCredentialValidationStatus](api/beta.md)

One of the following:

"valid"

"invalid"

"unknown"

[ManagedAgentsDeletedCredential](api/beta.md)

string id

Unique identifier of the deleted credential.

Type type

[ManagedAgentsMCPOAuthAuthResponse](api/beta.md)

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshResponse](api/beta.md) refresh

OAuth refresh token configuration returned in credential responses.

[ManagedAgentsMCPOAuthCreateParams](api/beta.md)

string accessToken

OAuth access token.

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshParams](api/beta.md) refresh

OAuth refresh token parameters for creating a credential with refresh support.

[ManagedAgentsMCPOAuthRefreshParams](api/beta.md)

string clientID

OAuth client ID.

string refreshToken

OAuth refresh token.

string tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

?string resource

OAuth resource indicator.

?string scope

OAuth scope for the refresh request.

[ManagedAgentsMCPOAuthRefreshResponse](api/beta.md)

string clientID

OAuth client ID.

string tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

?string resource

OAuth resource indicator.

?string scope

OAuth scope for the refresh request.

[ManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md)

?string refreshToken

Updated OAuth refresh token.

?string scope

Updated OAuth scope for the refresh request.

?TokenEndpointAuth tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

[ManagedAgentsMCPOAuthUpdateParams](api/beta.md)

Type type

?string accessToken

Updated OAuth access token.

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md) refresh

Parameters for updating OAuth refresh token configuration.

[ManagedAgentsMCPProbe](api/beta.md)

?[ManagedAgentsRefreshHTTPResponse](api/beta.md) httpResponse

An HTTP response captured during a credential validation probe.

string method

The MCP method that failed (for example `initialize` or `tools/list`).

[ManagedAgentsRefreshHTTPResponse](api/beta.md)

string body

Response body. May be truncated and has sensitive values scrubbed.

bool bodyTruncated

Whether `body` was truncated.

string contentType

Value of the `Content-Type` response header.

int statusCode

HTTP status code.

[ManagedAgentsRefreshObject](api/beta.md)

?[ManagedAgentsRefreshHTTPResponse](api/beta.md) httpResponse

An HTTP response captured during a credential validation probe.

Status status

Outcome of a refresh-token exchange attempted during credential validation.

[ManagedAgentsStaticBearerAuthResponse](api/beta.md)

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

[ManagedAgentsStaticBearerCreateParams](api/beta.md)

string token

Static bearer token value.

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

[ManagedAgentsStaticBearerUpdateParams](api/beta.md)

Type type

?string token

Updated static bearer token value.

[ManagedAgentsTokenEndpointAuthBasicParam](api/beta.md)

string clientSecret

OAuth client secret.

Type type

[ManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md)

Type type

[ManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md)

Type type

?string clientSecret

Updated OAuth client secret.

[ManagedAgentsTokenEndpointAuthNoneParam](api/beta.md)

Type type

[ManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md)

Type type

[ManagedAgentsTokenEndpointAuthPostParam](api/beta.md)

string clientSecret

OAuth client secret.

Type type

[ManagedAgentsTokenEndpointAuthPostResponse](api/beta.md)

Type type

[ManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md)

Type type

?string clientSecret

Updated OAuth client secret.

---

*Copyright © Anthropic. All rights reserved.*
