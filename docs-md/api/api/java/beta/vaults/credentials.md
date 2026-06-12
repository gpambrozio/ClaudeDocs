# Credentials

Copy page

SDK language

Java

# Credentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().create(CredentialCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

CredentialListPage beta().vaults().credentials().list(CredentialListParamsparams = CredentialListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().retrieve(CredentialRetrieveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().update(CredentialUpdateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

[BetaManagedAgentsDeletedCredential](api/beta.md) beta().vaults().credentials().delete(CredentialDeleteParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

[BetaManagedAgentsCredential](api/beta.md) beta().vaults().credentials().archive(CredentialArchiveParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

[BetaManagedAgentsCredentialValidation](api/beta.md) beta().vaults().credentials().mcpOAuthValidate(CredentialMcpOAuthValidateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### ModelsExpand Collapse



class BetaManagedAgentsCredential:

A credential stored in a vault. Sensitive fields are never returned in responses.

String id

Unique identifier for the credential.

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format



Auth auth

Authentication details for a credential.

One of the following:



class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format



Optional<[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)> refresh

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.



TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.



class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type



class BetaManagedAgentsEnvironmentVariableAuthResponse:

Environment variable credential details. The secret value is never returned.



Networking networking

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:

The secret is substituted on any host the session's Environment network policy permits egress to.

Type type



class BetaManagedAgentsLimitedCredentialNetworkingResponse:

The secret is substituted only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

Type type

String secretName

Name of the environment variable.

Type type

LocalDateTime createdAt

A timestamp in RFC 3339 format

Metadata metadata

Arbitrary key-value metadata attached to the credential.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String vaultId

Identifier of the vault this credential belongs to.

Optional<String> displayName

Human-readable name for the credential.



class BetaManagedAgentsCredentialNetworkingParams: A class that can be one of several variants.union 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

Type type



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type



class BetaManagedAgentsCredentialValidation:

Result of live-probing a credential against its configured MCP server.

String credentialId

Unique identifier of the credential that was validated.

boolean hasRefreshToken

Whether the credential has a refresh token configured.



Optional<[BetaManagedAgentsMcpProbe](api/beta.md)> mcpProbe

The failing step of an MCP validation probe.



Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.

String method

The MCP method that failed (for example `initialize` or `tools/list`).



Optional<[BetaManagedAgentsRefreshObject](api/beta.md)> refresh

Outcome of a refresh-token exchange attempted during credential validation.



Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.



Status status

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

SUCCEEDED("succeeded")

FAILED("failed")

CONNECT\_ERROR("connect\_error")

NO\_REFRESH\_TOKEN("no\_refresh\_token")



[BetaManagedAgentsCredentialValidationStatus](api/beta.md) status

Overall verdict of a credential validation probe.

One of the following:

VALID("valid")

INVALID("invalid")

UNKNOWN("unknown")

Type type

LocalDateTime validatedAt

A timestamp in RFC 3339 format

String vaultId

Identifier of the vault containing the credential.



enum BetaManagedAgentsCredentialValidationStatus:

Overall verdict of a credential validation probe.

VALID("valid")

INVALID("invalid")

UNKNOWN("unknown")



class BetaManagedAgentsDeletedCredential:

Confirmation of a deleted credential.

String id

Unique identifier of the deleted credential.

Type type



class BetaManagedAgentsEnvironmentVariableAuthResponse:

Environment variable credential details. The secret value is never returned.



Networking networking

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:

The secret is substituted on any host the session's Environment network policy permits egress to.

Type type



class BetaManagedAgentsLimitedCredentialNetworkingResponse:

The secret is substituted only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

Type type

String secretName

Name of the environment variable.

Type type



class BetaManagedAgentsEnvironmentVariableCreateParams:

Parameters for creating an environment variable credential.



[BetaManagedAgentsCredentialNetworkingParams](api/beta.md) networking

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

Type type



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type

String secretName

Name of the environment variable. Immutable after create.

String secretValue

Secret value. Write-only; never returned in responses.

Type type



class BetaManagedAgentsEnvironmentVariableUpdateParams:

Parameters for updating an environment variable credential. `secret_name` is immutable.

Type type



Optional<[BetaManagedAgentsCredentialNetworkingParams](api/beta.md)> networking

Updated networking scope. Full replacement.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

Type type



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type

Optional<String> secretValue

Updated secret value.



class BetaManagedAgentsLimitedCredentialNetworkingParams:

Substitute the secret only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

Type type



class BetaManagedAgentsLimitedCredentialNetworkingResponse:

The secret is substituted only on requests to the listed hosts.

List<String> allowedHosts

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

Type type



class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format



Optional<[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)> refresh

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.



TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.



class BetaManagedAgentsMcpOAuthCreateParams:

Parameters for creating an MCP OAuth credential.

String accessToken

OAuth access token.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format



Optional<[BetaManagedAgentsMcpOAuthRefreshParams](api/beta.md)> refresh

OAuth refresh token parameters for creating a credential with refresh support.

String clientId

OAuth client ID.

String refreshToken

OAuth refresh token.

String tokenEndpoint

Token endpoint URL used to refresh the access token.



TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type



class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.



class BetaManagedAgentsMcpOAuthRefreshParams:

OAuth refresh token parameters for creating a credential with refresh support.

String clientId

OAuth client ID.

String refreshToken

OAuth refresh token.

String tokenEndpoint

Token endpoint URL used to refresh the access token.



TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type



class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.



class BetaManagedAgentsMcpOAuthRefreshResponse:

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.



TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.



class BetaManagedAgentsMcpOAuthRefreshUpdateParams:

Parameters for updating OAuth refresh token configuration.

Optional<String> refreshToken

Updated OAuth refresh token.

Optional<String> scope

Updated OAuth scope for the refresh request.



Optional<TokenEndpointAuth> tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.



class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.



class BetaManagedAgentsMcpOAuthUpdateParams:

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

Type type

Optional<String> accessToken

Updated OAuth access token.

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format



Optional<[BetaManagedAgentsMcpOAuthRefreshUpdateParams](api/beta.md)> refresh

Parameters for updating OAuth refresh token configuration.

Optional<String> refreshToken

Updated OAuth refresh token.

Optional<String> scope

Updated OAuth scope for the refresh request.



Optional<TokenEndpointAuth> tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.



class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.



class BetaManagedAgentsMcpProbe:

The failing step of an MCP validation probe.



Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.

String method

The MCP method that failed (for example `initialize` or `tools/list`).



class BetaManagedAgentsRefreshHttpResponse:

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.



class BetaManagedAgentsRefreshObject:

Outcome of a refresh-token exchange attempted during credential validation.



Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.



Status status

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

SUCCEEDED("succeeded")

FAILED("failed")

CONNECT\_ERROR("connect\_error")

NO\_REFRESH\_TOKEN("no\_refresh\_token")



class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type



class BetaManagedAgentsStaticBearerCreateParams:

Parameters for creating a static bearer token credential.

String token

Static bearer token value.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type



class BetaManagedAgentsStaticBearerUpdateParams:

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

Type type

Optional<String> token

Updated static bearer token value.



class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type



class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.



class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type



class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type



class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type



class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams:

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

Type type



class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse:

The secret is substituted on any host the session's Environment network policy permits egress to.

Type type

---

*Copyright © Anthropic. All rights reserved.*
