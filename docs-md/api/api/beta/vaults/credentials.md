# Credentials

Copy page



cURL

# Credentials

##### [Create Credential](api/http/beta/vaults/credentials/create.md)

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/http/beta/vaults/credentials/list.md)

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/http/beta/vaults/credentials/retrieve.md)

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/http/beta/vaults/credentials/update.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/http/beta/vaults/credentials/delete.md)

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/http/beta/vaults/credentials/archive.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/http/beta/vaults/credentials/mcp_oauth_validate.md)

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### Models



BetaManagedAgentsCredential object{ id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.



BetaManagedAgentsCredentialNetworkingParams = [BetaManagedAgentsUnrestrictedCredentialNetworkingParams](api/http/beta/vaults/credentials.md) { type } or [BetaManagedAgentsLimitedCredentialNetworkingParams](api/http/beta/vaults/credentials.md) { allowed\_hosts, type }

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object{ type }

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



BetaManagedAgentsLimitedCredentialNetworkingParams object{ allowed\_hosts, type }

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: "limited"



BetaManagedAgentsCredentialValidation object{ credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

Result of live-probing a credential against its configured MCP server.



BetaManagedAgentsCredentialValidationStatus = "valid" or "invalid" or "unknown"

Overall verdict of a credential validation probe.

One of the following:

"valid"

"invalid"

"unknown"



BetaManagedAgentsDeletedCredential object{ id, type }

Confirmation of a deleted credential.

id: string

Unique identifier of the deleted credential.

type: "vault\_credential\_deleted"



BetaManagedAgentsEnvironmentVariableAuthResponse object{ injection\_location, networking, secret\_name, type }

Environment variable credential details. The secret value is never returned.



BetaManagedAgentsEnvironmentVariableCreateParams object{ networking, secret\_name, secret\_value, 2 more }

Parameters for creating an environment variable credential.



BetaManagedAgentsEnvironmentVariableUpdateParams object{ type, injection\_location, networking, secret\_value }

Parameters for updating an environment variable credential. `secret_name` is immutable.



BetaManagedAgentsInjectionLocationParams object{ body, header }

Where in the outbound request the secret value may be substituted.

body: optional boolean

Substitute when the placeholder appears in the request body.

header: optional boolean

Substitute when the placeholder appears in a request header value.



BetaManagedAgentsInjectionLocationResponse object{ body, header }

Where in the outbound request the secret value is substituted.

body: boolean

Whether the placeholder is substituted in the request body.

header: boolean

Whether the placeholder is substituted in request header values.



BetaManagedAgentsInjectionLocationUpdateParams object{ body, header }

Updated injection location.

body: optional boolean

Substitute when the placeholder appears in the request body.

header: optional boolean

Substitute when the placeholder appears in a request header value.



BetaManagedAgentsLimitedCredentialNetworkingParams object{ allowed\_hosts, type }

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: "limited"



BetaManagedAgentsLimitedCredentialNetworkingResponse object{ allowed\_hosts, type }

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: "limited"



BetaManagedAgentsMCPOAuthAuthResponse object{ mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"



expires\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time



refresh: optional [BetaManagedAgentsMCPOAuthRefreshResponse](api/http/beta/vaults/credentials.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more } or null

OAuth refresh token configuration returned in credential responses.



BetaManagedAgentsMCPOAuthCreateParams object{ access\_token, mcp\_server\_url, type, 2 more }

Parameters for creating an MCP OAuth credential.



access\_token: string

OAuth access token.

minLength1

maxLength8192



mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

minLength1

maxLength2047

type: "mcp\_oauth"



expires\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time



refresh: optional [BetaManagedAgentsMCPOAuthRefreshParams](api/http/beta/vaults/credentials.md) { client\_id, refresh\_token, token\_endpoint, 3 more } or null

OAuth refresh token parameters for creating a credential with refresh support.



BetaManagedAgentsMCPOAuthRefreshParams object{ client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.



BetaManagedAgentsMCPOAuthRefreshResponse object{ client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.



BetaManagedAgentsMCPOAuthRefreshUpdateParams object{ refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.



BetaManagedAgentsMCPOAuthUpdateParams object{ type, access\_token, expires\_at, refresh }

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: "mcp\_oauth"



access\_token: optional string or null

Updated OAuth access token.

minLength1

maxLength8192



expires\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time



refresh: optional [BetaManagedAgentsMCPOAuthRefreshUpdateParams](api/http/beta/vaults/credentials.md) { refresh\_token, scope, token\_endpoint\_auth } or null

Parameters for updating OAuth refresh token configuration.



BetaManagedAgentsMCPProbe object{ http\_response, method }

The failing step of an MCP validation probe.



http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/http/beta/vaults/credentials.md) { body, body\_truncated, content\_type, status\_code } or null

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.



status\_code: number

HTTP status code.

formatint32

method: string

The MCP method that failed (for example `initialize` or `tools/list`).



BetaManagedAgentsRefreshHTTPResponse object{ body, body\_truncated, content\_type, status\_code }

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.



status\_code: number

HTTP status code.

formatint32



BetaManagedAgentsRefreshObject object{ http\_response, status }

Outcome of a refresh-token exchange attempted during credential validation.



http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/http/beta/vaults/credentials.md) { body, body\_truncated, content\_type, status\_code } or null

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.



status\_code: number

HTTP status code.

formatint32



status: "succeeded" or "failed" or "connect\_error" or "no\_refresh\_token"

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"



BetaManagedAgentsStaticBearerAuthResponse object{ mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"



BetaManagedAgentsStaticBearerCreateParams object{ token, mcp\_server\_url, type }

Parameters for creating a static bearer token credential.



token: string

Static bearer token value.

minLength1

maxLength8192



mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

minLength1

maxLength2047

type: "static\_bearer"



BetaManagedAgentsStaticBearerUpdateParams object{ type, token }

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static\_bearer"



token: optional string or null

Updated static bearer token value.

minLength1

maxLength8192



BetaManagedAgentsTokenEndpointAuthBasicParam object{ client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.



client\_secret: string

OAuth client secret.

minLength1

maxLength512

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthBasicResponse object{ type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthBasicUpdateParam object{ type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"



client\_secret: optional string or null

Updated OAuth client secret.

minLength1

maxLength512



BetaManagedAgentsTokenEndpointAuthNoneParam object{ type }

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthNoneResponse object{ type }

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthPostParam object{ client\_secret, type }

Token endpoint uses POST body authentication with client credentials.



client\_secret: string

OAuth client secret.

minLength1

maxLength512

type: "client\_secret\_post"



BetaManagedAgentsTokenEndpointAuthPostResponse object{ type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"



BetaManagedAgentsTokenEndpointAuthPostUpdateParam object{ type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"



client\_secret: optional string or null

Updated OAuth client secret.

minLength1

maxLength512



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object{ type }

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object{ type }

The secret is substituted on any host the session's Environment network policy permits egress to.

type: "unrestricted"

---

*Copyright © Anthropic. All rights reserved.*
