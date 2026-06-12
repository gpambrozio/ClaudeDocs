# Vaults

Copy page

SDK language

TypeScript

# Vaults

##### [Create Vault](api/beta/vaults/create.md)

client.beta.vaults.create(VaultCreateParams { display\_name, metadata, betas } params, RequestOptionsoptions?): [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

client.beta.vaults.list(VaultListParams { include\_archived, limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more } >

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

client.beta.vaults.retrieve(stringvaultID, VaultRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

client.beta.vaults.update(stringvaultID, VaultUpdateParams { display\_name, metadata, betas } params, RequestOptionsoptions?): [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

client.beta.vaults.delete(stringvaultID, VaultDeleteParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeletedVault](api/beta.md) { id, type }

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

client.beta.vaults.archive(stringvaultID, VaultArchiveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse



BetaManagedAgentsDeletedVault { id, type } 

Confirmation of a deleted vault.

id: string

Unique identifier of the deleted vault.

type: "vault\_deleted"



BetaManagedAgentsVault { id, archived\_at, created\_at, 4 more } 

A vault that stores credentials for use by agents during sessions.

id: string

Unique identifier for the vault.

archived\_at: string | null

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

display\_name: string

Human-readable name for the vault.

metadata: Record<string, string>

Arbitrary key-value metadata attached to the vault.

type: "vault"

updated\_at: string

A timestamp in RFC 3339 format

#### VaultsCredentials

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

##### [Validate Credential](api/beta/vaults/credentials/mcp_oauth_validate.md)

client.beta.vaults.credentials.mcpOAuthValidate(stringcredentialID, CredentialMCPOAuthValidateParams { vault\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsCredentialValidation](api/beta.md) { credential\_id, has\_refresh\_token, mcp\_probe, 5 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/mcp\_oauth\_validate

##### ModelsExpand Collapse



BetaManagedAgentsCredential { id, archived\_at, auth, 6 more } 

A credential stored in a vault. Sensitive fields are never returned in responses.

id: string

Unique identifier for the credential.

archived\_at: string | null

A timestamp in RFC 3339 format



auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta.md) { mcp\_server\_url, type, expires\_at, refresh }  | [BetaManagedAgentsStaticBearerAuthResponse](api/beta.md) { mcp\_server\_url, type }  | [BetaManagedAgentsEnvironmentVariableAuthResponse](api/beta.md) { networking, secret\_name, type } 

Authentication details for a credential.

One of the following:



BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh } 

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at?: string | null

A timestamp in RFC 3339 format



refresh?: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }  | null

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type } 

Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneResponse { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthBasicResponse { type } 

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthPostResponse { type } 

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.



BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type } 

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"



BetaManagedAgentsEnvironmentVariableAuthResponse { networking, secret\_name, type } 

Environment variable credential details. The secret value is never returned.



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta.md) { type }  | [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta.md) { allowed\_hosts, type } 

Outbound hosts the secret value is substituted on.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingResponse { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.

type: "unrestricted"



BetaManagedAgentsLimitedCredentialNetworkingResponse { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: Array<string>

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: "limited"

secret\_name: string

Name of the environment variable.

type: "environment\_variable"

created\_at: string

A timestamp in RFC 3339 format

metadata: Record<string, string>

Arbitrary key-value metadata attached to the credential.

type: "vault\_credential"

updated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name?: string | null

Human-readable name for the credential.



BetaManagedAgentsCredentialNetworkingParams = [BetaManagedAgentsUnrestrictedCredentialNetworkingParams](api/beta.md) { type }  | [BetaManagedAgentsLimitedCredentialNetworkingParams](api/beta.md) { allowed\_hosts, type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array<string>

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: "limited"



BetaManagedAgentsCredentialValidation { credential\_id, has\_refresh\_token, mcp\_probe, 5 more } 

Result of live-probing a credential against its configured MCP server.

credential\_id: string

Unique identifier of the credential that was validated.

has\_refresh\_token: boolean

Whether the credential has a refresh token configured.



mcp\_probe: [BetaManagedAgentsMCPProbe](api/beta.md) { http\_response, method }  | null

The failing step of an MCP validation probe.



http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta.md) { body, body\_truncated, content\_type, status\_code }  | null

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

refresh: [BetaManagedAgentsRefreshObject](api/beta.md) { http\_response, status }  | null

Outcome of a refresh-token exchange attempted during credential validation.



http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta.md) { body, body\_truncated, content\_type, status\_code }  | null

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

status: "succeeded" | "failed" | "connect\_error" | "no\_refresh\_token"

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"



status: [BetaManagedAgentsCredentialValidationStatus](api/beta.md)

Overall verdict of a credential validation probe.

One of the following:

"valid"

"invalid"

"unknown"

type: "vault\_credential\_validation"

validated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault containing the credential.



BetaManagedAgentsCredentialValidationStatus = "valid" | "invalid" | "unknown"

Overall verdict of a credential validation probe.

One of the following:

"valid"

"invalid"

"unknown"



BetaManagedAgentsDeletedCredential { id, type } 

Confirmation of a deleted credential.

id: string

Unique identifier of the deleted credential.

type: "vault\_credential\_deleted"



BetaManagedAgentsEnvironmentVariableAuthResponse { networking, secret\_name, type } 

Environment variable credential details. The secret value is never returned.



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta.md) { type }  | [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta.md) { allowed\_hosts, type } 

Outbound hosts the secret value is substituted on.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingResponse { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.

type: "unrestricted"



BetaManagedAgentsLimitedCredentialNetworkingResponse { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: Array<string>

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: "limited"

secret\_name: string

Name of the environment variable.

type: "environment\_variable"



BetaManagedAgentsEnvironmentVariableCreateParams { networking, secret\_name, secret\_value, type } 

Parameters for creating an environment variable credential.



networking: [BetaManagedAgentsCredentialNetworkingParams](api/beta.md)

Outbound hosts the secret value is substituted on.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array<string>

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: "limited"

secret\_name: string

Name of the environment variable. Immutable after create.

secret\_value: string

Secret value. Write-only; never returned in responses.

type: "environment\_variable"



BetaManagedAgentsEnvironmentVariableUpdateParams { type, networking, secret\_value } 

Parameters for updating an environment variable credential. `secret_name` is immutable.

type: "environment\_variable"



networking?: [BetaManagedAgentsCredentialNetworkingParams](api/beta.md) | null

Updated networking scope. Full replacement.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array<string>

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: "limited"

secret\_value?: string | null

Updated secret value.



BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array<string>

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: "limited"



BetaManagedAgentsLimitedCredentialNetworkingResponse { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: Array<string>

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: "limited"



BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh } 

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at?: string | null

A timestamp in RFC 3339 format



refresh?: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }  | null

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type } 

Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneResponse { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthBasicResponse { type } 

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthPostResponse { type } 

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.



BetaManagedAgentsMCPOAuthCreateParams { access\_token, mcp\_server\_url, type, 2 more } 

Parameters for creating an MCP OAuth credential.

access\_token: string

OAuth access token.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at?: string | null

A timestamp in RFC 3339 format



refresh?: [BetaManagedAgentsMCPOAuthRefreshParams](api/beta.md) { client\_id, refresh\_token, token\_endpoint, 3 more }  | null

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  | [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type } 

Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneParam { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type } 

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type } 

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.



BetaManagedAgentsMCPOAuthRefreshParams { client\_id, refresh\_token, token\_endpoint, 3 more } 

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  | [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type } 

Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneParam { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type } 

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type } 

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.



BetaManagedAgentsMCPOAuthRefreshResponse { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more } 

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type } 

Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneResponse { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthBasicResponse { type } 

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthPostResponse { type } 

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource?: string | null

OAuth resource indicator.

scope?: string | null

OAuth scope for the refresh request.



BetaManagedAgentsMCPOAuthRefreshUpdateParams { refresh\_token, scope, token\_endpoint\_auth } 

Parameters for updating OAuth refresh token configuration.

refresh\_token?: string | null

Updated OAuth refresh token.

scope?: string | null

Updated OAuth scope for the refresh request.



token\_endpoint\_auth?: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret?: string | null

Updated OAuth client secret.



BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret } 

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret?: string | null

Updated OAuth client secret.



BetaManagedAgentsMCPOAuthUpdateParams { type, access\_token, expires\_at, refresh } 

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: "mcp\_oauth"

access\_token?: string | null

Updated OAuth access token.

expires\_at?: string | null

A timestamp in RFC 3339 format



refresh?: [BetaManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md) { refresh\_token, scope, token\_endpoint\_auth }  | null

Parameters for updating OAuth refresh token configuration.

refresh\_token?: string | null

Updated OAuth refresh token.

scope?: string | null

Updated OAuth scope for the refresh request.



token\_endpoint\_auth?: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret?: string | null

Updated OAuth client secret.



BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret } 

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret?: string | null

Updated OAuth client secret.



BetaManagedAgentsMCPProbe { http\_response, method } 

The failing step of an MCP validation probe.



http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta.md) { body, body\_truncated, content\_type, status\_code }  | null

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

BetaManagedAgentsRefreshHTTPResponse { body, body\_truncated, content\_type, status\_code } 

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

BetaManagedAgentsRefreshObject { http\_response, status } 

Outcome of a refresh-token exchange attempted during credential validation.



http\_response: [BetaManagedAgentsRefreshHTTPResponse](api/beta.md) { body, body\_truncated, content\_type, status\_code }  | null

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

status: "succeeded" | "failed" | "connect\_error" | "no\_refresh\_token"

Outcome of a refresh-token exchange attempted during credential validation.

One of the following:

"succeeded"

"failed"

"connect\_error"

"no\_refresh\_token"



BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type } 

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"



BetaManagedAgentsStaticBearerCreateParams { token, mcp\_server\_url, type } 

Parameters for creating a static bearer token credential.

token: string

Static bearer token value.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"



BetaManagedAgentsStaticBearerUpdateParams { type, token } 

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static\_bearer"

token?: string | null

Updated static bearer token value.



BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type } 

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthBasicResponse { type } 

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

client\_secret?: string | null

Updated OAuth client secret.



BetaManagedAgentsTokenEndpointAuthNoneParam { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthNoneResponse { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type } 

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"



BetaManagedAgentsTokenEndpointAuthPostResponse { type } 

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"



BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret } 

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

client\_secret?: string | null

Updated OAuth client secret.



BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



BetaManagedAgentsUnrestrictedCredentialNetworkingResponse { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.

type: "unrestricted"

---

*Copyright © Anthropic. All rights reserved.*
