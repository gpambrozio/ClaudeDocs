# Credentials

Copy page

SDK language

Ruby

# Credentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

beta.vaults.credentials.create(vault\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

beta.vaults.credentials.list(vault\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more } >

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

beta.vaults.credentials.retrieve(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

beta.vaults.credentials.update(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

beta.vaults.credentials.delete(credential\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedCredential](api/beta.md) { id, type }

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

beta.vaults.credentials.archive(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

beta.vaults.credentials.mcp\_oauth\_validate(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredentialValidation](api/beta.md) { credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### ModelsExpand Collapse

class BetaManagedAgentsCredential { id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

id: String

Unique identifier for the credential.

archived\_at: Time

A timestamp in RFC 3339 format

auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta.md) { mcp\_server\_url, type, expires\_at, refresh }  | [BetaManagedAgentsStaticBearerAuthResponse](api/beta.md) { mcp\_server\_url, type }  | [BetaManagedAgentsEnvironmentVariableAuthResponse](api/beta.md) { networking, secret\_name, type }

Authentication details for a credential.

One of the following:

class BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :mcp\_oauth

expires\_at: Time

A timestamp in RFC 3339 format

refresh: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: String

OAuth client ID.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

One of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :static\_bearer

class BetaManagedAgentsEnvironmentVariableAuthResponse { networking, secret\_name, type }

Environment variable credential details. The secret value is never returned.

networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta.md) { type }  | [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta.md) { allowed\_hosts, type }

Outbound hosts the secret value is substituted on.

One of the following:

class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse { type }

The secret is substituted on any host the session's Environment network policy permits egress to.

type: :unrestricted

class BetaManagedAgentsLimitedCredentialNetworkingResponse { allowed\_hosts, type }

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: :limited

secret\_name: String

Name of the environment variable.

type: :environment\_variable

created\_at: Time

A timestamp in RFC 3339 format

metadata: Hash[Symbol, String]

Arbitrary key-value metadata attached to the credential.

type: :vault\_credential

updated\_at: Time

A timestamp in RFC 3339 format

vault\_id: String

Identifier of the vault this credential belongs to.

display\_name: String

Human-readable name for the credential.

BetaManagedAgentsCredentialNetworkingParams = [BetaManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta.md) { type }  | [BetaManagedAgentsLimitedCredentialNetworkingParams](api/beta.md) { allowed\_hosts, type }

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

One of the following:

class BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type }

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: :unrestricted

class BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type }

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: :limited

class BetaManagedAgentsCredentialValidation { credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

Result of live-probing a credential against its configured MCP server.

credential\_id: String

Unique identifier of the credential that was validated.

has\_refresh\_token: bool

Whether the credential has a refresh token configured.

mcp\_probe: [BetaManagedAgentsMCPProbe](api/beta.md) { http\_response, method\_ }

The failing step of an MCP validation probe.

http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta.md) { body, body\_truncated, content\_type, status\_code }

An HTTP response captured during a credential validation probe.

body: String

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: String

Value of the `Content-Type` response header.

status\_code: Integer

HTTP status code.

method\_: String

The MCP method that failed (for example `initialize` or `tools/list`).

refresh: [BetaManagedAgentsRefreshObject](api/beta.md) { http\_response, status }

Outcome of a refresh-token exchange attempted during credential validation.

http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta.md) { body, body\_truncated, content\_type, status\_code }

An HTTP response captured during a credential validation probe.

body: String

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: String

Value of the `Content-Type` response header.

status\_code: Integer

HTTP status code.

status: :succeeded | :failed | :connect\_error | :no\_refresh\_token

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

:succeeded

:failed

:connect\_error

:no\_refresh\_token

status: [BetaManagedAgentsCredentialValidationStatus](api/beta.md)

Overall verdict of a credential validation probe.

One of the following:

:valid

:invalid

:unknown

type: :vault\_credential\_validation

validated\_at: Time

A timestamp in RFC 3339 format

vault\_id: String

Identifier of the vault containing the credential.

BetaManagedAgentsCredentialValidationStatus = :valid | :invalid | :unknown

Overall verdict of a credential validation probe.

One of the following:

:valid

:invalid

:unknown

class BetaManagedAgentsDeletedCredential { id, type }

Confirmation of a deleted credential.

id: String

Unique identifier of the deleted credential.

type: :vault\_credential\_deleted

class BetaManagedAgentsEnvironmentVariableAuthResponse { networking, secret\_name, type }

Environment variable credential details. The secret value is never returned.

networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta.md) { type }  | [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta.md) { allowed\_hosts, type }

Outbound hosts the secret value is substituted on.

One of the following:

class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse { type }

The secret is substituted on any host the session's Environment network policy permits egress to.

type: :unrestricted

class BetaManagedAgentsLimitedCredentialNetworkingResponse { allowed\_hosts, type }

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: :limited

secret\_name: String

Name of the environment variable.

type: :environment\_variable

class BetaManagedAgentsEnvironmentVariableCreateParams { networking, secret\_name, secret\_value, type }

Parameters for creating an environment variable credential.

networking: [BetaManagedAgentsCredentialNetworkingParams](api/beta.md)

Outbound hosts the secret value is substituted on.

One of the following:

class BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type }

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: :unrestricted

class BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type }

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: :limited

secret\_name: String

Name of the environment variable. Immutable after create.

secret\_value: String

Secret value. Write-only; never returned in responses.

type: :environment\_variable

class BetaManagedAgentsEnvironmentVariableUpdateParams { type, networking, secret\_value }

Parameters for updating an environment variable credential. `secret_name` is immutable.

type: :environment\_variable

networking: [BetaManagedAgentsCredentialNetworkingParams](api/beta.md)

Updated networking scope. Full replacement.

One of the following:

class BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type }

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: :unrestricted

class BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type }

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: :limited

secret\_value: String

Updated secret value.

class BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type }

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: :limited

class BetaManagedAgentsLimitedCredentialNetworkingResponse { allowed\_hosts, type }

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: :limited

class BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :mcp\_oauth

expires\_at: Time

A timestamp in RFC 3339 format

refresh: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: String

OAuth client ID.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

One of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthCreateParams { access\_token, mcp\_server\_url, type, 2 more }

Parameters for creating an MCP OAuth credential.

access\_token: String

OAuth access token.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :mcp\_oauth

expires\_at: Time

A timestamp in RFC 3339 format

refresh: [BetaManagedAgentsMCPOAuthRefreshParams](api/beta.md) { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: String

OAuth client ID.

refresh\_token: String

OAuth refresh token.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  | [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

One of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthRefreshParams { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: String

OAuth client ID.

refresh\_token: String

OAuth refresh token.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  | [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

One of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthRefreshResponse { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: String

OAuth client ID.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

One of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthRefreshUpdateParams { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: String

Updated OAuth refresh token.

scope: String

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: :client\_secret\_basic

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: :client\_secret\_post

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsMCPOAuthUpdateParams { type, access\_token, expires\_at, refresh }

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: :mcp\_oauth

access\_token: String

Updated OAuth access token.

expires\_at: Time

A timestamp in RFC 3339 format

refresh: [BetaManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md) { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: String

Updated OAuth refresh token.

scope: String

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: :client\_secret\_basic

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: :client\_secret\_post

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsMCPProbe { http\_response, method\_ }

The failing step of an MCP validation probe.

http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta.md) { body, body\_truncated, content\_type, status\_code }

An HTTP response captured during a credential validation probe.

body: String

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: String

Value of the `Content-Type` response header.

status\_code: Integer

HTTP status code.

method\_: String

The MCP method that failed (for example `initialize` or `tools/list`).

class BetaManagedAgentsRefreshHTTPResponse { body, body\_truncated, content\_type, status\_code }

An HTTP response captured during a credential validation probe.

body: String

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: String

Value of the `Content-Type` response header.

status\_code: Integer

HTTP status code.

class BetaManagedAgentsRefreshObject { http\_response, status }

Outcome of a refresh-token exchange attempted during credential validation.

http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta.md) { body, body\_truncated, content\_type, status\_code }

An HTTP response captured during a credential validation probe.

body: String

Response body. May be truncated and has sensitive values scrubbed.

body\_truncated: bool

Whether `body` was truncated.

content\_type: String

Value of the `Content-Type` response header.

status\_code: Integer

HTTP status code.

status: :succeeded | :failed | :connect\_error | :no\_refresh\_token

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

:succeeded

:failed

:connect\_error

:no\_refresh\_token

class BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :static\_bearer

class BetaManagedAgentsStaticBearerCreateParams { token, mcp\_server\_url, type }

Parameters for creating a static bearer token credential.

token: String

Static bearer token value.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :static\_bearer

class BetaManagedAgentsStaticBearerUpdateParams { type, token }

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: :static\_bearer

token: String

Updated static bearer token value.

class BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: :client\_secret\_basic

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_post

class BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: :client\_secret\_post

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type }

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: :unrestricted

class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse { type }

The secret is substituted on any host the session's Environment network policy permits egress to.

type: :unrestricted

---

*Copyright © Anthropic. All rights reserved.*
