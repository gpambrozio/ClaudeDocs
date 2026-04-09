# Credentials

Copy page

Java

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

##### ModelsExpand Collapse

class BetaManagedAgentsCredential:

A credential stored in a vault. Sensitive fields are never returned in responses.

String id

Unique identifier for the credential.

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

Auth auth

Authentication details for a credential.

Accepts one of the following:

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)> refresh

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

LocalDateTime createdAt

A timestamp in RFC 3339 format

Metadata metadata

Arbitrary key-value metadata attached to the credential.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

String vaultId

Identifier of the vault this credential belongs to.

Optional<String> displayName

Human-readable name for the credential.

class BetaManagedAgentsDeletedCredential:

Confirmation of a deleted credential.

String id

Unique identifier of the deleted credential.

Type type

class BetaManagedAgentsMcpOAuthAuthResponse:

OAuth credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsMcpOAuthRefreshResponse](api/beta.md)> refresh

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthCreateParams:

Parameters for creating an MCP OAuth credential.

String accessToken

OAuth access token.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsMcpOAuthRefreshParams](api/beta.md)> refresh

OAuth refresh token parameters for creating a credential with refresh support.

String clientId

OAuth client ID.

String refreshToken

OAuth refresh token.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshParams:

OAuth refresh token parameters for creating a credential with refresh support.

String clientId

OAuth client ID.

String refreshToken

OAuth refresh token.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshResponse:

OAuth refresh token configuration returned in credential responses.

String clientId

OAuth client ID.

String tokenEndpoint

Token endpoint URL used to refresh the access token.

TokenEndpointAuth tokenEndpointAuth

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

Optional<String> resource

OAuth resource indicator.

Optional<String> scope

OAuth scope for the refresh request.

class BetaManagedAgentsMcpOAuthRefreshUpdateParams:

Parameters for updating OAuth refresh token configuration.

Optional<String> refreshToken

Updated OAuth refresh token.

Optional<String> scope

Updated OAuth scope for the refresh request.

Optional<TokenEndpointAuth> tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsMcpOAuthUpdateParams:

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

Type type

Optional<String> accessToken

Updated OAuth access token.

Optional<LocalDateTime> expiresAt

A timestamp in RFC 3339 format

Optional<[BetaManagedAgentsMcpOAuthRefreshUpdateParams](api/beta.md)> refresh

Parameters for updating OAuth refresh token configuration.

Optional<String> refreshToken

Updated OAuth refresh token.

Optional<String> scope

Updated OAuth scope for the refresh request.

Optional<TokenEndpointAuth> tokenEndpointAuth

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsStaticBearerAuthResponse:

Static bearer token credential details for an MCP server.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

class BetaManagedAgentsStaticBearerCreateParams:

Parameters for creating a static bearer token credential.

String token

Static bearer token value.

String mcpServerUrl

URL of the MCP server this credential authenticates against.

Type type

class BetaManagedAgentsStaticBearerUpdateParams:

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

Type type

Optional<String> token

Updated static bearer token value.

class BetaManagedAgentsTokenEndpointAuthBasicParam:

Token endpoint uses HTTP Basic authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicResponse:

Token endpoint uses HTTP Basic authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam:

Updated HTTP Basic authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthNoneParam:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthNoneResponse:

Token endpoint requires no client authentication.

Type type

class BetaManagedAgentsTokenEndpointAuthPostParam:

Token endpoint uses POST body authentication with client credentials.

String clientSecret

OAuth client secret.

Type type

class BetaManagedAgentsTokenEndpointAuthPostResponse:

Token endpoint uses POST body authentication with client credentials.

Type type

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam:

Updated POST body authentication parameters for the token endpoint.

Type type

Optional<String> clientSecret

Updated OAuth client secret.

---

*Copyright © Anthropic. All rights reserved.*
