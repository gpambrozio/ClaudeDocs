# Credentials

Copy page

TypeScript

# Credentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

client.beta.vaults.credentials.create(stringvaultID, CredentialCreateParams { auth, display\_name, metadata, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

client.beta.vaults.credentials.list(stringvaultID, CredentialListParams { include\_archived, limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more } >

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

client.beta.vaults.credentials.retrieve(stringcredentialID, CredentialRetrieveParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

client.beta.vaults.credentials.update(stringcredentialID, CredentialUpdateParams { vault\_id, auth, display\_name, 2 more } params, RequestOptionsoptions?): [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

client.beta.vaults.credentials.delete(stringcredentialID, CredentialDeleteParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsDeletedCredential](api/beta.md) { id, type }

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

client.beta.vaults.credentials.archive(stringcredentialID, CredentialArchiveParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### ModelsExpand Collapse

BetaManagedAgentsCredential { id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

id: string

Unique identifier for the credential.

archived\_at: string | null

A timestamp in RFC 3339 format

auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta.md) { mcp\_server\_url, type, expires\_at, refresh }  | [BetaManagedAgentsStaticBearerAuthResponse](api/beta.md) { mcp\_server\_url, type }

Authentication details for a credential.

Accepts one of the following:

BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at?: string | null

A timestamp in RFC 3339 format

refresh?: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }  | null

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.

BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

created\_at: string

A timestamp in RFC 3339 format

metadata: Record<string, string>

Arbitrary key-value metadata attached to the credential.

type: "vault\_credential"

updated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name?: string | null

Human-readable name for the credential.

BetaManagedAgentsDeletedCredential { id, type }

Confirmation of a deleted credential.

id: string

Unique identifier of the deleted credential.

type: "vault\_credential\_deleted"

BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at?: string | null

A timestamp in RFC 3339 format

refresh?: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }  | null

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.

BetaManagedAgentsMCPOAuthCreateParams { access\_token, mcp\_server\_url, type, 2 more }

Parameters for creating an MCP OAuth credential.

access\_token: string

OAuth access token.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at?: string | null

A timestamp in RFC 3339 format

refresh?: [BetaManagedAgentsMCPOAuthRefreshParams](api/beta.md) { client\_id, refresh\_token, token\_endpoint, 3 more }  | null

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  | [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.

BetaManagedAgentsMCPOAuthRefreshParams { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  | [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.

BetaManagedAgentsMCPOAuthRefreshResponse { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.

BetaManagedAgentsMCPOAuthRefreshUpdateParams { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token?: string | null

Updated OAuth refresh token.

scope?: string | null

Updated OAuth scope for the refresh request.

token\_endpoint\_auth?: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret?: string | null

Updated OAuth client secret.

BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret?: string | null

Updated OAuth client secret.

BetaManagedAgentsMCPOAuthUpdateParams { type, access\_token, expires\_at, refresh }

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: "mcp\_oauth"

access\_token?: string | null

Updated OAuth access token.

expires\_at?: string | null

A timestamp in RFC 3339 format

refresh?: [BetaManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md) { refresh\_token, scope, token\_endpoint\_auth }  | null

Parameters for updating OAuth refresh token configuration.

refresh\_token?: string | null

Updated OAuth refresh token.

scope?: string | null

Updated OAuth scope for the refresh request.

token\_endpoint\_auth?: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret?: string | null

Updated OAuth client secret.

BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret?: string | null

Updated OAuth client secret.

BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

BetaManagedAgentsStaticBearerCreateParams { token, mcp\_server\_url, type }

Parameters for creating a static bearer token credential.

token: string

Static bearer token value.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

BetaManagedAgentsStaticBearerUpdateParams { type, token }

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static\_bearer"

token?: string | null

Updated static bearer token value.

BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret?: string | null

Updated OAuth client secret.

BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret?: string | null

Updated OAuth client secret.

---

*Copyright © Anthropic. All rights reserved.*
