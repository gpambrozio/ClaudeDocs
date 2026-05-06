# Vaults

Copy page

Java

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

[BetaManagedAgentsVault](api/beta.md) beta().vaults().create(VaultCreateParamsparams, RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

VaultListPage beta().vaults().list(VaultListParamsparams = VaultListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

[BetaManagedAgentsVault](api/beta.md) beta().vaults().retrieve(VaultRetrieveParamsparams = VaultRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

[BetaManagedAgentsVault](api/beta.md) beta().vaults().update(VaultUpdateParamsparams = VaultUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

[BetaManagedAgentsDeletedVault](api/beta.md) beta().vaults().delete(VaultDeleteParamsparams = VaultDeleteParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

[BetaManagedAgentsVault](api/beta.md) beta().vaults().archive(VaultArchiveParamsparams = VaultArchiveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedVault:

Confirmation of a deleted vault.

String id

Unique identifier of the deleted vault.

Type type

class BetaManagedAgentsVault:

A vault that stores credentials for use by agents during sessions.

String id

Unique identifier for the vault.

Optional<LocalDateTime> archivedAt

A timestamp in RFC 3339 format

LocalDateTime createdAt

A timestamp in RFC 3339 format

String displayName

Human-readable name for the vault.

Metadata metadata

Arbitrary key-value metadata attached to the vault.

Type type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

#### VaultsCredentials

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

class BetaManagedAgentsCredentialValidation:

Result of live-probing a credential against its configured MCP server.

String credentialId

Unique identifier of the credential that was validated.

boolean hasRefreshToken

Whether the credential has a refresh token configured.

Optional<[BetaManagedAgentsMcpProbe](api/beta.md)> mcpProbe

The failing step of an MCP validation probe.

Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.

String method

The MCP method that failed (for example `initialize` or `tools/list`).

Optional<[BetaManagedAgentsRefreshObject](api/beta.md)> refresh

Outcome of a refresh-token exchange attempted during credential validation.

Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.

Status status

Outcome of a refresh-token exchange attempted during credential validation.

Accepts one of the following:

SUCCEEDED("succeeded")

FAILED("failed")

CONNECT\_ERROR("connect\_error")

NO\_REFRESH\_TOKEN("no\_refresh\_token")

[BetaManagedAgentsCredentialValidationStatus](api/beta.md) status

Overall verdict of a credential validation probe.

Accepts one of the following:

VALID("valid")

INVALID("invalid")

UNKNOWN("unknown")

Type type

LocalDateTime validatedAt

A timestamp in RFC 3339 format

String vaultId

Identifier of the vault containing the credential.

enum BetaManagedAgentsCredentialValidationStatus:

Overall verdict of a credential validation probe.

VALID("valid")

INVALID("invalid")

UNKNOWN("unknown")

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

class BetaManagedAgentsMcpProbe:

The failing step of an MCP validation probe.

Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.

String method

The MCP method that failed (for example `initialize` or `tools/list`).

class BetaManagedAgentsRefreshHttpResponse:

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.

class BetaManagedAgentsRefreshObject:

Outcome of a refresh-token exchange attempted during credential validation.

Optional<[BetaManagedAgentsRefreshHttpResponse](api/beta.md)> httpResponse

An HTTP response captured during a credential validation probe.

String body

Response body. May be truncated and has sensitive values scrubbed.

boolean bodyTruncated

Whether `body` was truncated.

String contentType

Value of the `Content-Type` response header.

long statusCode

HTTP status code.

Status status

Outcome of a refresh-token exchange attempted during credential validation.

Accepts one of the following:

SUCCEEDED("succeeded")

FAILED("failed")

CONNECT\_ERROR("connect\_error")

NO\_REFRESH\_TOKEN("no\_refresh\_token")

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
