# Credentials

Copy page



C#

# Credentials

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

##### ModelsExpand Collapse



class BetaManagedAgentsCredential:

A credential stored in a vault. Sensitive fields are never returned in responses.

required string ID

Unique identifier for the credential.

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format



required Auth Auth

Authentication details for a credential.

One of the following:



class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format



[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta/vaults/credentials.md)? Refresh

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.



required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.



class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type



class BetaManagedAgentsEnvironmentVariableAuthResponse:

Environment variable credential details. The secret value is never returned.



required Networking Networking

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:

The secret is substituted on any host the session's Environment network policy permits egress to.

required Type Type



class BetaManagedAgentsLimitedCredentialNetworkingResponse:

The secret is substituted only on requests to the listed hosts.

required IReadOnlyList<string> AllowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

required Type Type

required string SecretName

Name of the environment variable.

required Type Type

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata attached to the credential.

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string VaultID

Identifier of the vault this credential belongs to.

string? DisplayName

Human-readable name for the credential.



class BetaManagedAgentsCredentialNetworkingParams: A class that can be one of several variants.union 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

required Type Type



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

required IReadOnlyList<string> AllowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

required Type Type



class BetaManagedAgentsCredentialValidation:

Result of live-probing a credential against its configured MCP server.

required string CredentialID

Unique identifier of the credential that was validated.

required Boolean HasRefreshToken

Whether the credential has a refresh token configured.



required [BetaManagedAgentsMcpProbe](api/beta/vaults/credentials.md)? McpProbe

The failing step of an MCP validation probe.



required [BetaManagedAgentsRefreshHttpResponse](api/beta/vaults/credentials.md)? HttpResponse

An HTTP response captured during a credential validation probe.

required string Body

Response body. May be truncated and has sensitive values scrubbed.

required Boolean BodyTruncated

Whether `body` was truncated.

required string ContentType

Value of the `Content-Type` response header.

required Int StatusCode

HTTP status code.

required string Method

The MCP method that failed (for example `initialize` or `tools/list`).



required [BetaManagedAgentsRefreshObject](api/beta/vaults/credentials.md)? Refresh

Outcome of a refresh-token exchange attempted during credential validation.



required [BetaManagedAgentsRefreshHttpResponse](api/beta/vaults/credentials.md)? HttpResponse

An HTTP response captured during a credential validation probe.

required string Body

Response body. May be truncated and has sensitive values scrubbed.

required Boolean BodyTruncated

Whether `body` was truncated.

required string ContentType

Value of the `Content-Type` response header.

required Int StatusCode

HTTP status code.



required Status Status

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"Succeeded

"failed"Failed

"connect\_error"ConnectError

"no\_refresh\_token"NoRefreshToken



required [BetaManagedAgentsCredentialValidationStatus](api/beta/vaults/credentials.md) Status

Overall verdict of a credential validation probe.

One of the following:

"valid"Valid

"invalid"Invalid

"unknown"Unknown

required Type Type

required DateTimeOffset ValidatedAt

A timestamp in RFC 3339 format

required string VaultID

Identifier of the vault containing the credential.



enum BetaManagedAgentsCredentialValidationStatus:

Overall verdict of a credential validation probe.

"valid"Valid

"invalid"Invalid

"unknown"Unknown



class BetaManagedAgentsDeletedCredential:

Confirmation of a deleted credential.

required string ID

Unique identifier of the deleted credential.

required Type Type



class BetaManagedAgentsEnvironmentVariableAuthResponse:

Environment variable credential details. The secret value is never returned.



required Networking Networking

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:

The secret is substituted on any host the session's Environment network policy permits egress to.

required Type Type



class BetaManagedAgentsLimitedCredentialNetworkingResponse:

The secret is substituted only on requests to the listed hosts.

required IReadOnlyList<string> AllowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

required Type Type

required string SecretName

Name of the environment variable.

required Type Type



class BetaManagedAgentsEnvironmentVariableCreateParams:

Parameters for creating an environment variable credential.



required [BetaManagedAgentsCredentialNetworkingParams](api/beta/vaults/credentials.md) Networking

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

required Type Type



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

required IReadOnlyList<string> AllowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

required Type Type

required string SecretName

Name of the environment variable. Immutable after create.

required string SecretValue

Secret value. Write-only; never returned in responses.

required Type Type



class BetaManagedAgentsEnvironmentVariableUpdateParams:

Parameters for updating an environment variable credential. `secret_name` is immutable.

required Type Type



[BetaManagedAgentsCredentialNetworkingParams](api/beta/vaults/credentials.md)? Networking

Updated networking scope. Full replacement.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

required Type Type



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

required IReadOnlyList<string> AllowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

required Type Type

string? SecretValue

Updated secret value.



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

required IReadOnlyList<string> AllowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

required Type Type



class BetaManagedAgentsLimitedCredentialNetworkingResponse:

The secret is substituted only on requests to the listed hosts.

required IReadOnlyList<string> AllowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

required Type Type



class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format



[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta/vaults/credentials.md)? Refresh

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.



required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.



class BetaManagedAgentsMcpOAuthCreateParams:

Parameters for creating an MCP OAuth credential.

required string AccessToken

OAuth access token.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format



[BetaManagedAgentsMcpOAuthRefreshParams](api/beta/vaults/credentials.md)? Refresh

OAuth refresh token parameters for creating a credential with refresh support.

required string ClientID

OAuth client ID.

required string RefreshToken

OAuth refresh token.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.



required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type



class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type



class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.



class BetaManagedAgentsMcpOAuthRefreshParams:

OAuth refresh token parameters for creating a credential with refresh support.

required string ClientID

OAuth client ID.

required string RefreshToken

OAuth refresh token.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.



required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type



class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type



class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.



class BetaManagedAgentsMcpOAuthRefreshResponse:

OAuth refresh token configuration returned in credential responses.

required string ClientID

OAuth client ID.

required string TokenEndpoint

Token endpoint URL used to refresh the access token.



required TokenEndpointAuth TokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type

string? Resource

OAuth resource indicator.

string? Scope

OAuth scope for the refresh request.



class BetaManagedAgentsMcpOAuthRefreshUpdateParams:

Parameters for updating OAuth refresh token configuration.

string? RefreshToken

Updated OAuth refresh token.

string? Scope

Updated OAuth scope for the refresh request.



TokenEndpointAuth TokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.



class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.



class BetaManagedAgentsMcpOAuthUpdateParams:

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

required Type Type

string? AccessToken

Updated OAuth access token.

DateTimeOffset? ExpiresAt

A timestamp in RFC 3339 format



[BetaManagedAgentsMcpOAuthRefreshUpdateParams](api/beta/vaults/credentials.md)? Refresh

Parameters for updating OAuth refresh token configuration.

string? RefreshToken

Updated OAuth refresh token.

string? Scope

Updated OAuth scope for the refresh request.



TokenEndpointAuth TokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.



class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.



class BetaManagedAgentsMcpProbe:

The failing step of an MCP validation probe.



required [BetaManagedAgentsRefreshHttpResponse](api/beta/vaults/credentials.md)? HttpResponse

An HTTP response captured during a credential validation probe.

required string Body

Response body. May be truncated and has sensitive values scrubbed.

required Boolean BodyTruncated

Whether `body` was truncated.

required string ContentType

Value of the `Content-Type` response header.

required Int StatusCode

HTTP status code.

required string Method

The MCP method that failed (for example `initialize` or `tools/list`).



class BetaManagedAgentsRefreshHttpResponse:

An HTTP response captured during a credential validation probe.

required string Body

Response body. May be truncated and has sensitive values scrubbed.

required Boolean BodyTruncated

Whether `body` was truncated.

required string ContentType

Value of the `Content-Type` response header.

required Int StatusCode

HTTP status code.



class BetaManagedAgentsRefreshObject:

Outcome of a refresh-token exchange attempted during credential validation.



required [BetaManagedAgentsRefreshHttpResponse](api/beta/vaults/credentials.md)? HttpResponse

An HTTP response captured during a credential validation probe.

required string Body

Response body. May be truncated and has sensitive values scrubbed.

required Boolean BodyTruncated

Whether `body` was truncated.

required string ContentType

Value of the `Content-Type` response header.

required Int StatusCode

HTTP status code.



required Status Status

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"Succeeded

"failed"Failed

"connect\_error"ConnectError

"no\_refresh\_token"NoRefreshToken



class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type



class BetaManagedAgentsStaticBearerCreateParams:

Parameters for creating a static bearer token credential.

required string Token

Static bearer token value.

required string McpServerUrl

URL of the MCP server this credential authenticates against.

required Type Type



class BetaManagedAgentsStaticBearerUpdateParams:

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

required Type Type

string? Token

Updated static bearer token value.



class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

required Type Type



class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.



class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

required Type Type



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

required Type Type



class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

required string ClientSecret

OAuth client secret.

required Type Type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

required Type Type



class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

required Type Type

string? ClientSecret

Updated OAuth client secret.



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

required Type Type



class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:

The secret is substituted on any host the session's Environment network policy permits egress to.

required Type Type

---

*Copyright © Anthropic. All rights reserved.*
