# Credentials

Copy page



PHP

# Credentials

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

##### ModelsExpand Collapse



[ManagedAgentsCredential](api/beta/vaults/credentials.md)

string id

Unique identifier for the credential.

?\Datetime archivedAt

A timestamp in RFC 3339 format

Auth auth

Authentication details for a credential.

\Datetime createdAt

A timestamp in RFC 3339 format

array<string,string> metadata

Arbitrary key-value metadata attached to the credential.

Type type

\Datetime updatedAt

A timestamp in RFC 3339 format

string vaultID

Identifier of the vault this credential belongs to.

?string displayName

Human-readable name for the credential.



[ManagedAgentsCredentialNetworkingParams](api/beta/vaults/credentials.md)

One of the following:



[ManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta/vaults/credentials.md)

Type type



[ManagedAgentsLimitedCredentialNetworkingParams](api/beta/vaults/credentials.md)

list<string> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type



[ManagedAgentsCredentialValidation](api/beta/vaults/credentials.md)

string credentialID

Unique identifier of the credential that was validated.

bool hasRefreshToken

Whether the credential has a refresh token configured.

?[ManagedAgentsMCPProbe](api/beta/vaults/credentials.md) mcpProbe

The failing step of an MCP validation probe.

?[ManagedAgentsRefreshObject](api/beta/vaults/credentials.md) refresh

Outcome of a refresh-token exchange attempted during credential validation.

[ManagedAgentsCredentialValidationStatus](api/beta/vaults/credentials.md) status

Overall verdict of a credential validation probe.

Type type

\Datetime validatedAt

A timestamp in RFC 3339 format

string vaultID

Identifier of the vault containing the credential.



[ManagedAgentsCredentialValidationStatus](api/beta/vaults/credentials.md)

One of the following:

"valid"

"invalid"

"unknown"



[ManagedAgentsDeletedCredential](api/beta/vaults/credentials.md)

string id

Unique identifier of the deleted credential.

Type type



[ManagedAgentsEnvironmentVariableAuthResponse](api/beta/vaults/credentials.md)

[ManagedAgentsInjectionLocationResponse](api/beta/vaults/credentials.md) injectionLocation

Where in the outbound request the secret value is substituted.

Networking networking

Outbound hosts the secret value is substituted on.

string secretName

Name of the environment variable.

Type type



[ManagedAgentsEnvironmentVariableCreateParams](api/beta/vaults/credentials.md)

[ManagedAgentsCredentialNetworkingParams](api/beta/vaults/credentials.md) networking

Outbound hosts the secret value is substituted on.

string secretName

Name of the environment variable. Immutable after create.

string secretValue

Secret value. Write-only; never returned in responses.

Type type

?[ManagedAgentsInjectionLocationParams](api/beta/vaults/credentials.md) injectionLocation

Where in the outbound request the secret value may be substituted.



[ManagedAgentsEnvironmentVariableUpdateParams](api/beta/vaults/credentials.md)

Type type

?[ManagedAgentsInjectionLocationUpdateParams](api/beta/vaults/credentials.md) injectionLocation

Updated injection location.

?[ManagedAgentsCredentialNetworkingParams](api/beta/vaults/credentials.md) networking

Updated networking scope. Full replacement.

?string secretValue

Updated secret value.



[ManagedAgentsInjectionLocationParams](api/beta/vaults/credentials.md)

?bool body

Substitute when the placeholder appears in the request body.

?bool header

Substitute when the placeholder appears in a request header value.



[ManagedAgentsInjectionLocationResponse](api/beta/vaults/credentials.md)

bool body

Whether the placeholder is substituted in the request body.

bool header

Whether the placeholder is substituted in request header values.



[ManagedAgentsInjectionLocationUpdateParams](api/beta/vaults/credentials.md)

?bool body

Substitute when the placeholder appears in the request body.

?bool header

Substitute when the placeholder appears in a request header value.



[ManagedAgentsLimitedCredentialNetworkingParams](api/beta/vaults/credentials.md)

list<string> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type



[ManagedAgentsLimitedCredentialNetworkingResponse](api/beta/vaults/credentials.md)

list<string> allowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

Type type



[ManagedAgentsMCPOAuthAuthResponse](api/beta/vaults/credentials.md)

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshResponse](api/beta/vaults/credentials.md) refresh

OAuth refresh token configuration returned in credential responses.



[ManagedAgentsMCPOAuthCreateParams](api/beta/vaults/credentials.md)

string accessToken

OAuth access token.

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshParams](api/beta/vaults/credentials.md) refresh

OAuth refresh token parameters for creating a credential with refresh support.



[ManagedAgentsMCPOAuthRefreshParams](api/beta/vaults/credentials.md)

string clientID

OAuth client ID.

string refreshToken

OAuth refresh token.

string tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

?string resource

OAuth resource indicator.

?string scope

OAuth scope for the refresh request.



[ManagedAgentsMCPOAuthRefreshResponse](api/beta/vaults/credentials.md)

string clientID

OAuth client ID.

string tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

?string resource

OAuth resource indicator.

?string scope

OAuth scope for the refresh request.



[ManagedAgentsMCPOAuthRefreshUpdateParams](api/beta/vaults/credentials.md)

?string refreshToken

Updated OAuth refresh token.

?string scope

Updated OAuth scope for the refresh request.

?TokenEndpointAuth tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.



[ManagedAgentsMCPOAuthUpdateParams](api/beta/vaults/credentials.md)

Type type

?string accessToken

Updated OAuth access token.

?\Datetime expiresAt

A timestamp in RFC 3339 format

?[ManagedAgentsMCPOAuthRefreshUpdateParams](api/beta/vaults/credentials.md) refresh

Parameters for updating OAuth refresh token configuration.



[ManagedAgentsMCPProbe](api/beta/vaults/credentials.md)

?[ManagedAgentsRefreshHTTPResponse](api/beta/vaults/credentials.md) httpResponse

An HTTP response captured during a credential validation probe.

string method

The MCP method that failed (for example `initialize` or `tools/list`).



[ManagedAgentsRefreshHTTPResponse](api/beta/vaults/credentials.md)

string body

Response body. May be truncated and has sensitive values scrubbed.

bool bodyTruncated

Whether `body` was truncated.

string contentType

Value of the `Content-Type` response header.

int statusCode

HTTP status code.



[ManagedAgentsRefreshObject](api/beta/vaults/credentials.md)

?[ManagedAgentsRefreshHTTPResponse](api/beta/vaults/credentials.md) httpResponse

An HTTP response captured during a credential validation probe.

Status status

Outcome of a refresh-token exchange attempted during credential validation.



[ManagedAgentsStaticBearerAuthResponse](api/beta/vaults/credentials.md)

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type



[ManagedAgentsStaticBearerCreateParams](api/beta/vaults/credentials.md)

string token

Static bearer token value.

string mcpServerURL

URL of the MCP server this credential authenticates against.

Type type



[ManagedAgentsStaticBearerUpdateParams](api/beta/vaults/credentials.md)

Type type

?string token

Updated static bearer token value.



[ManagedAgentsTokenEndpointAuthBasicParam](api/beta/vaults/credentials.md)

string clientSecret

OAuth client secret.

Type type



[ManagedAgentsTokenEndpointAuthBasicResponse](api/beta/vaults/credentials.md)

Type type



[ManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta/vaults/credentials.md)

Type type

?string clientSecret

Updated OAuth client secret.



[ManagedAgentsTokenEndpointAuthNoneParam](api/beta/vaults/credentials.md)

Type type



[ManagedAgentsTokenEndpointAuthNoneResponse](api/beta/vaults/credentials.md)

Type type



[ManagedAgentsTokenEndpointAuthPostParam](api/beta/vaults/credentials.md)

string clientSecret

OAuth client secret.

Type type



[ManagedAgentsTokenEndpointAuthPostResponse](api/beta/vaults/credentials.md)

Type type



[ManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta/vaults/credentials.md)

Type type

?string clientSecret

Updated OAuth client secret.



[ManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta/vaults/credentials.md)

Type type



[ManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta/vaults/credentials.md)

Type type

---

*Copyright © Anthropic. All rights reserved.*
