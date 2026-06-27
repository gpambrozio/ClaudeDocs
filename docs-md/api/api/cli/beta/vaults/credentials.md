# Credentials

Copy page



CLI

# Credentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

$ ant beta:vaults:credentials create

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

$ ant beta:vaults:credentials list

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

$ ant beta:vaults:credentials retrieve

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

$ ant beta:vaults:credentials update

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

$ ant beta:vaults:credentials delete

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

$ ant beta:vaults:credentials archive

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

$ ant beta:vaults:credentials mcp-oauth-validate

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### ModelsExpand Collapse



beta\_managed\_agents\_credential: object { id, archived\_at, auth, 6 more } 

A credential stored in a vault. Sensitive fields are never returned in responses.

id: string

Unique identifier for the credential.

archived\_at: string

A timestamp in RFC 3339 format



auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta/vaults/credentials.md) { mcp\_server\_url, type, expires\_at, refresh }  or [BetaManagedAgentsStaticBearerAuthResponse](api/beta/vaults/credentials.md) { mcp\_server\_url, type }  or [BetaManagedAgentsEnvironmentVariableAuthResponse](api/beta/vaults/credentials.md) { networking, secret\_name, type } 

Authentication details for a credential.



beta\_managed\_agents\_mcp\_oauth\_auth\_response: object { mcp\_server\_url, type, expires\_at, refresh } 

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.



type: "mcp\_oauth"

"mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format



refresh: optional object { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more } 

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta/vaults/credentials.md) { type } 

Token endpoint requires no client authentication.



beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type } 

Token endpoint requires no client authentication.



type: "none"

"none"



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type } 

Token endpoint uses HTTP Basic authentication with client credentials.



type: "client\_secret\_basic"

"client\_secret\_basic"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type } 

Token endpoint uses POST body authentication with client credentials.



type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.



beta\_managed\_agents\_static\_bearer\_auth\_response: object { mcp\_server\_url, type } 

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.



type: "static\_bearer"

"static\_bearer"



beta\_managed\_agents\_environment\_variable\_auth\_response: object { networking, secret\_name, type } 

Environment variable credential details. The secret value is never returned.



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta/vaults/credentials.md) { allowed\_hosts, type } 

Outbound hosts the secret value is substituted on.



beta\_managed\_agents\_unrestricted\_credential\_networking\_response: object { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.



type: "unrestricted"

"unrestricted"



beta\_managed\_agents\_limited\_credential\_networking\_response: object { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.



type: "limited"

"limited"

secret\_name: string

Name of the environment variable.



type: "environment\_variable"

"environment\_variable"

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata attached to the credential.



type: "vault\_credential"

"vault\_credential"

updated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name: optional string

Human-readable name for the credential.



beta\_managed\_agents\_credential\_networking\_params: [BetaManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsLimitedCredentialNetworkingParams](api/beta/vaults/credentials.md) { allowed\_hosts, type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.



beta\_managed\_agents\_unrestricted\_credential\_networking\_params: object { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.



type: "unrestricted"

"unrestricted"



beta\_managed\_agents\_limited\_credential\_networking\_params: object { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.



type: "limited"

"limited"



beta\_managed\_agents\_credential\_validation: object { credential\_id, has\_refresh\_token, mcp\_probe, 5 more } 

Result of live-probing a credential against its configured MCP server.

credential\_id: string

Unique identifier of the credential that was validated.

has\_refresh\_token: boolean

Whether the credential has a refresh token configured.



mcp\_probe: object { http\_response, method } 

The failing step of an MCP validation probe.



http\_response: object { body, body\_truncated, content\_type, status\_code } 

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.

method: string

The MCP method that failed (for example `initialize` or `tools/list`).



refresh: object { http\_response, status } 

Outcome of a refresh-token exchange attempted during credential validation.



http\_response: object { body, body\_truncated, content\_type, status\_code } 

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.



status: "succeeded" or "failed" or "connect\_error" or "no\_refresh\_token"

Outcome of a refresh-token exchange attempted during credential validation.

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"



status: "valid" or "invalid" or "unknown"

Overall verdict of a credential validation probe.

"valid"

"invalid"

"unknown"



type: "vault\_credential\_validation"

"vault\_credential\_validation"

validated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault containing the credential.



beta\_managed\_agents\_credential\_validation\_status: "valid" or "invalid" or "unknown"

Overall verdict of a credential validation probe.

"valid"

"invalid"

"unknown"



beta\_managed\_agents\_deleted\_credential: object { id, type } 

Confirmation of a deleted credential.

id: string

Unique identifier of the deleted credential.



type: "vault\_credential\_deleted"

"vault\_credential\_deleted"



beta\_managed\_agents\_environment\_variable\_auth\_response: object { networking, secret\_name, type } 

Environment variable credential details. The secret value is never returned.



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta/vaults/credentials.md) { allowed\_hosts, type } 

Outbound hosts the secret value is substituted on.



beta\_managed\_agents\_unrestricted\_credential\_networking\_response: object { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.



type: "unrestricted"

"unrestricted"



beta\_managed\_agents\_limited\_credential\_networking\_response: object { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.



type: "limited"

"limited"

secret\_name: string

Name of the environment variable.



type: "environment\_variable"

"environment\_variable"



beta\_managed\_agents\_environment\_variable\_create\_params: object { networking, secret\_name, secret\_value, type } 

Parameters for creating an environment variable credential.



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsLimitedCredentialNetworkingParams](api/beta/vaults/credentials.md) { allowed\_hosts, type } 

Outbound hosts the secret value is substituted on.



beta\_managed\_agents\_unrestricted\_credential\_networking\_params: object { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.



type: "unrestricted"

"unrestricted"



beta\_managed\_agents\_limited\_credential\_networking\_params: object { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.



type: "limited"

"limited"

secret\_name: string

Name of the environment variable. Immutable after create.

secret\_value: string

Secret value. Write-only; never returned in responses.



type: "environment\_variable"

"environment\_variable"



beta\_managed\_agents\_environment\_variable\_update\_params: object { type, networking, secret\_value } 

Parameters for updating an environment variable credential. `secret_name` is immutable.



type: "environment\_variable"

"environment\_variable"



networking: optional [BetaManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsLimitedCredentialNetworkingParams](api/beta/vaults/credentials.md) { allowed\_hosts, type } 

Updated networking scope. Full replacement.



beta\_managed\_agents\_unrestricted\_credential\_networking\_params: object { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.



type: "unrestricted"

"unrestricted"



beta\_managed\_agents\_limited\_credential\_networking\_params: object { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.



type: "limited"

"limited"

secret\_value: optional string

Updated secret value.



beta\_managed\_agents\_limited\_credential\_networking\_params: object { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.



type: "limited"

"limited"



beta\_managed\_agents\_limited\_credential\_networking\_response: object { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.



type: "limited"

"limited"



beta\_managed\_agents\_mcp\_oauth\_auth\_response: object { mcp\_server\_url, type, expires\_at, refresh } 

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.



type: "mcp\_oauth"

"mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format



refresh: optional object { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more } 

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta/vaults/credentials.md) { type } 

Token endpoint requires no client authentication.



beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type } 

Token endpoint requires no client authentication.



type: "none"

"none"



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type } 

Token endpoint uses HTTP Basic authentication with client credentials.



type: "client\_secret\_basic"

"client\_secret\_basic"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type } 

Token endpoint uses POST body authentication with client credentials.



type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.



beta\_managed\_agents\_mcp\_oauth\_create\_params: object { access\_token, mcp\_server\_url, type, 2 more } 

Parameters for creating an MCP OAuth credential.

access\_token: string

OAuth access token.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.



type: "mcp\_oauth"

"mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format



refresh: optional object { client\_id, refresh\_token, token\_endpoint, 3 more } 

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta/vaults/credentials.md) { client\_secret, type }  or [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta/vaults/credentials.md) { client\_secret, type } 

Token endpoint requires no client authentication.



beta\_managed\_agents\_token\_endpoint\_auth\_none\_param: object { type } 

Token endpoint requires no client authentication.



type: "none"

"none"



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_param: object { client\_secret, type } 

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.



type: "client\_secret\_basic"

"client\_secret\_basic"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_param: object { client\_secret, type } 

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.



type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.



beta\_managed\_agents\_mcp\_oauth\_refresh\_params: object { client\_id, refresh\_token, token\_endpoint, 3 more } 

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta/vaults/credentials.md) { client\_secret, type }  or [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta/vaults/credentials.md) { client\_secret, type } 

Token endpoint requires no client authentication.



beta\_managed\_agents\_token\_endpoint\_auth\_none\_param: object { type } 

Token endpoint requires no client authentication.



type: "none"

"none"



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_param: object { client\_secret, type } 

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.



type: "client\_secret\_basic"

"client\_secret\_basic"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_param: object { client\_secret, type } 

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.



type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.



beta\_managed\_agents\_mcp\_oauth\_refresh\_response: object { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more } 

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta/vaults/credentials.md) { type } 

Token endpoint requires no client authentication.



beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type } 

Token endpoint requires no client authentication.



type: "none"

"none"



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type } 

Token endpoint uses HTTP Basic authentication with client credentials.



type: "client\_secret\_basic"

"client\_secret\_basic"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type } 

Token endpoint uses POST body authentication with client credentials.



type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.



beta\_managed\_agents\_mcp\_oauth\_refresh\_update\_params: object { refresh\_token, scope, token\_endpoint\_auth } 

Parameters for updating OAuth refresh token configuration.

refresh\_token: optional string

Updated OAuth refresh token.

scope: optional string

Updated OAuth scope for the refresh request.



token\_endpoint\_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta/vaults/credentials.md) { type, client\_secret }  or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta/vaults/credentials.md) { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_update\_param: object { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.



type: "client\_secret\_basic"

"client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.



beta\_managed\_agents\_token\_endpoint\_auth\_post\_update\_param: object { type, client\_secret } 

Updated POST body authentication parameters for the token endpoint.



type: "client\_secret\_post"

"client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.



beta\_managed\_agents\_mcp\_oauth\_update\_params: object { type, access\_token, expires\_at, refresh } 

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.



type: "mcp\_oauth"

"mcp\_oauth"

access\_token: optional string

Updated OAuth access token.

expires\_at: optional string

A timestamp in RFC 3339 format



refresh: optional object { refresh\_token, scope, token\_endpoint\_auth } 

Parameters for updating OAuth refresh token configuration.

refresh\_token: optional string

Updated OAuth refresh token.

scope: optional string

Updated OAuth scope for the refresh request.



token\_endpoint\_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta/vaults/credentials.md) { type, client\_secret }  or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta/vaults/credentials.md) { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_update\_param: object { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.



type: "client\_secret\_basic"

"client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.



beta\_managed\_agents\_token\_endpoint\_auth\_post\_update\_param: object { type, client\_secret } 

Updated POST body authentication parameters for the token endpoint.



type: "client\_secret\_post"

"client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.



beta\_managed\_agents\_mcp\_probe: object { http\_response, method } 

The failing step of an MCP validation probe.



http\_response: object { body, body\_truncated, content\_type, status\_code } 

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.

method: string

The MCP method that failed (for example `initialize` or `tools/list`).



beta\_managed\_agents\_refresh\_http\_response: object { body, body\_truncated, content\_type, status\_code } 

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.



beta\_managed\_agents\_refresh\_object: object { http\_response, status } 

Outcome of a refresh-token exchange attempted during credential validation.



http\_response: object { body, body\_truncated, content\_type, status\_code } 

An HTTP response captured during a credential validation probe.

body: string

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: boolean

Whether `body` was truncated.

content\_type: string

Value of the `Content-Type` response header.

status\_code: number

HTTP status code.



status: "succeeded" or "failed" or "connect\_error" or "no\_refresh\_token"

Outcome of a refresh-token exchange attempted during credential validation.

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"



beta\_managed\_agents\_static\_bearer\_auth\_response: object { mcp\_server\_url, type } 

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.



type: "static\_bearer"

"static\_bearer"



beta\_managed\_agents\_static\_bearer\_create\_params: object { token, mcp\_server\_url, type } 

Parameters for creating a static bearer token credential.

token: string

Static bearer token value.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.



type: "static\_bearer"

"static\_bearer"



beta\_managed\_agents\_static\_bearer\_update\_params: object { type, token } 

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.



type: "static\_bearer"

"static\_bearer"

token: optional string

Updated static bearer token value.



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_param: object { client\_secret, type } 

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.



type: "client\_secret\_basic"

"client\_secret\_basic"



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type } 

Token endpoint uses HTTP Basic authentication with client credentials.



type: "client\_secret\_basic"

"client\_secret\_basic"



beta\_managed\_agents\_token\_endpoint\_auth\_basic\_update\_param: object { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.



type: "client\_secret\_basic"

"client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.



beta\_managed\_agents\_token\_endpoint\_auth\_none\_param: object { type } 

Token endpoint requires no client authentication.



type: "none"

"none"



beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type } 

Token endpoint requires no client authentication.



type: "none"

"none"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_param: object { client\_secret, type } 

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.



type: "client\_secret\_post"

"client\_secret\_post"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type } 

Token endpoint uses POST body authentication with client credentials.



type: "client\_secret\_post"

"client\_secret\_post"



beta\_managed\_agents\_token\_endpoint\_auth\_post\_update\_param: object { type, client\_secret } 

Updated POST body authentication parameters for the token endpoint.



type: "client\_secret\_post"

"client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.



beta\_managed\_agents\_unrestricted\_credential\_networking\_params: object { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.



type: "unrestricted"

"unrestricted"



beta\_managed\_agents\_unrestricted\_credential\_networking\_response: object { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.



type: "unrestricted"

"unrestricted"

---

*Copyright © Anthropic. All rights reserved.*
