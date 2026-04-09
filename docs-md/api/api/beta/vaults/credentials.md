# Credentials

Copy page

cURL

# Credentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### ModelsExpand Collapse

BetaManagedAgentsCredential = object { id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

id: string

Unique identifier for the credential.

archived\_at: string

A timestamp in RFC 3339 format

auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta.md) { mcp\_server\_url, type, expires\_at, refresh }  or [BetaManagedAgentsStaticBearerAuthResponse](api/beta.md) { mcp\_server\_url, type }

Authentication details for a credential.

Accepts one of the following:

BetaManagedAgentsMCPOAuthAuthResponse = object { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

BetaManagedAgentsStaticBearerAuthResponse = object { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata attached to the credential.

type: "vault\_credential"

updated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name: optional string

Human-readable name for the credential.

BetaManagedAgentsDeletedCredential = object { id, type }

Confirmation of a deleted credential.

id: string

Unique identifier of the deleted credential.

type: "vault\_credential\_deleted"

BetaManagedAgentsMCPOAuthAuthResponse = object { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

BetaManagedAgentsMCPOAuthCreateParams = object { access\_token, mcp\_server\_url, type, 2 more }

Parameters for creating an MCP OAuth credential.

access\_token: string

OAuth access token.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional [BetaManagedAgentsMCPOAuthRefreshParams](api/beta.md) { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  or [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneParam = object { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicParam = object { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostParam = object { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

BetaManagedAgentsMCPOAuthRefreshParams = object { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  or [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneParam = object { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicParam = object { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostParam = object { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

BetaManagedAgentsMCPOAuthRefreshResponse = object { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

BetaManagedAgentsMCPOAuthRefreshUpdateParams = object { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: optional string

Updated OAuth refresh token.

scope: optional string

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthBasicUpdateParam = object { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.

BetaManagedAgentsTokenEndpointAuthPostUpdateParam = object { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.

BetaManagedAgentsMCPOAuthUpdateParams = object { type, access\_token, expires\_at, refresh }

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: "mcp\_oauth"

access\_token: optional string

Updated OAuth access token.

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional [BetaManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md) { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: optional string

Updated OAuth refresh token.

scope: optional string

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

BetaManagedAgentsTokenEndpointAuthBasicUpdateParam = object { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.

BetaManagedAgentsTokenEndpointAuthPostUpdateParam = object { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.

BetaManagedAgentsStaticBearerAuthResponse = object { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

BetaManagedAgentsStaticBearerCreateParams = object { token, mcp\_server\_url, type }

Parameters for creating a static bearer token credential.

token: string

Static bearer token value.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

BetaManagedAgentsStaticBearerUpdateParams = object { type, token }

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static\_bearer"

token: optional string

Updated static bearer token value.

BetaManagedAgentsTokenEndpointAuthBasicParam = object { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthBasicResponse = object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

BetaManagedAgentsTokenEndpointAuthBasicUpdateParam = object { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.

BetaManagedAgentsTokenEndpointAuthNoneParam = object { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthNoneResponse = object { type }

Token endpoint requires no client authentication.

type: "none"

BetaManagedAgentsTokenEndpointAuthPostParam = object { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

BetaManagedAgentsTokenEndpointAuthPostResponse = object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

BetaManagedAgentsTokenEndpointAuthPostUpdateParam = object { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.

---

*Copyright © Anthropic. All rights reserved.*
