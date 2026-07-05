# Update Credential

Copy page



Ruby

# Update Credential

beta.vaults.credentials.update(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

Update Credential

##### ParametersExpand Collapse

vault\_id: String

credential\_id: String



auth: [BetaManagedAgentsMCPOAuthUpdateParams](api/beta/vaults/credentials.md) { type, access\_token, expires\_at, refresh }  | [BetaManagedAgentsStaticBearerUpdateParams](api/beta/vaults/credentials.md) { type, token }  | [BetaManagedAgentsEnvironmentVariableUpdateParams](api/beta/vaults/credentials.md) { type, injection\_location, networking, secret\_value } 

Updated authentication details for a credential.

One of the following:



class BetaManagedAgentsMCPOAuthUpdateParams { type, access\_token, expires\_at, refresh } 

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: :mcp\_oauth

access\_token: String

Updated OAuth access token.

expires\_at: Time

A timestamp in RFC 3339 format



refresh: [BetaManagedAgentsMCPOAuthRefreshUpdateParams](api/beta/vaults/credentials.md) { refresh\_token, scope, token\_endpoint\_auth } 

Parameters for updating OAuth refresh token configuration.

refresh\_token: String

Updated OAuth refresh token.

scope: String

Updated OAuth scope for the refresh request.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta/vaults/credentials.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta/vaults/credentials.md) { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.

One of the following:



class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret } 

Updated HTTP Basic authentication parameters for the token endpoint.

type: :client\_secret\_basic

client\_secret: String

Updated OAuth client secret.



class BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret } 

Updated POST body authentication parameters for the token endpoint.

type: :client\_secret\_post

client\_secret: String

Updated OAuth client secret.



class BetaManagedAgentsStaticBearerUpdateParams { type, token } 

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: :static\_bearer

token: String

Updated static bearer token value.



class BetaManagedAgentsEnvironmentVariableUpdateParams { type, injection\_location, networking, secret\_value } 

Parameters for updating an environment variable credential. `secret_name` is immutable.

type: :environment\_variable



injection\_location: [BetaManagedAgentsInjectionLocationUpdateParams](api/beta/vaults/credentials.md) { body, header } 

Updated injection location.

body: bool

Substitute when the placeholder appears in the request body.

header: bool

Substitute when the placeholder appears in a request header value.



networking: [BetaManagedAgentsCredentialNetworkingParams](api/beta/vaults/credentials.md)

Updated networking scope. Full replacement.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingParams { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: :unrestricted



class BetaManagedAgentsLimitedCredentialNetworkingParams { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: :limited

secret\_value: String

Updated secret value.

display\_name: String

Updated human-readable name for the credential. 1-255 characters.

metadata: Hash[Symbol, String]

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.



betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

One of the following:

String = String



AnthropicBeta = :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 25 more

One of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"user-profiles-2026-03-24"

:"advisor-tool-2026-03-01"

:"managed-agents-2026-04-01"

:"cache-diagnosis-2026-04-07"

:"thinking-token-count-2026-05-13"

:"server-side-fallback-2026-06-01"

:"fallback-credit-2026-06-01"

##### ReturnsExpand Collapse



class BetaManagedAgentsCredential { id, archived\_at, auth, 6 more } 

A credential stored in a vault. Sensitive fields are never returned in responses.

id: String

Unique identifier for the credential.

archived\_at: Time

A timestamp in RFC 3339 format



auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta/vaults/credentials.md) { mcp\_server\_url, type, expires\_at, refresh }  | [BetaManagedAgentsStaticBearerAuthResponse](api/beta/vaults/credentials.md) { mcp\_server\_url, type }  | [BetaManagedAgentsEnvironmentVariableAuthResponse](api/beta/vaults/credentials.md) { injection\_location, networking, secret\_name, type } 

Authentication details for a credential.

One of the following:



class BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh } 

OAuth credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :mcp\_oauth

expires\_at: Time

A timestamp in RFC 3339 format



refresh: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta/vaults/credentials.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more } 

OAuth refresh token configuration returned in credential responses.

client\_id: String

OAuth client ID.

token\_endpoint: String

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta/vaults/credentials.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta/vaults/credentials.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta/vaults/credentials.md) { type } 

Token endpoint requires no client authentication.

One of the following:



class BetaManagedAgentsTokenEndpointAuthNoneResponse { type } 

Token endpoint requires no client authentication.

type: :none



class BetaManagedAgentsTokenEndpointAuthBasicResponse { type } 

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic



class BetaManagedAgentsTokenEndpointAuthPostResponse { type } 

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.



class BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type } 

Static bearer token credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :static\_bearer



class BetaManagedAgentsEnvironmentVariableAuthResponse { injection\_location, networking, secret\_name, type } 

Environment variable credential details. The secret value is never returned.



injection\_location: [BetaManagedAgentsInjectionLocationResponse](api/beta/vaults/credentials.md) { body, header } 

Where in the outbound request the secret value is substituted.

body: bool

Whether the placeholder is substituted in the request body.

header: bool

Whether the placeholder is substituted in request header values.



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta/vaults/credentials.md) { type }  | [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta/vaults/credentials.md) { allowed\_hosts, type } 

Outbound hosts the secret value is substituted on.

One of the following:



class BetaManagedAgentsUnrestrictedCredentialNetworkingResponse { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.

type: :unrestricted



class BetaManagedAgentsLimitedCredentialNetworkingResponse { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: Array[String]

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: :limited

secret\_name: String

Name of the environment variable.

type: :environment\_variable

created\_at: Time

A timestamp in RFC 3339 format

metadata: Hash[Symbol, String]

Arbitrary key-value metadata attached to the credential.

type: :vault\_credential

updated\_at: Time

A timestamp in RFC 3339 format

vault\_id: String

Identifier of the vault this credential belongs to.

display\_name: String

Human-readable name for the credential.

Update Credential

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

beta_managed_agents_credential = anthropic.beta.vaults.credentials.update(
  "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  vault_id: "vlt_011CZkZDLs7fYzm1hXNPeRjv"
)

puts(beta_managed_agents_credential)
```

Response 200



```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "vcrd_011CZkZEMt8gZan2iYOQfSkw",
  "archived_at": null,
  "auth": {
    "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
    "type": "static_bearer"
  },
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {
    "environment": "production"
  },
  "type": "vault_credential",
  "updated_at": "2026-03-15T10:00:00Z",
  "vault_id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "display_name": "Example credential"
}
```

---

*Copyright © Anthropic. All rights reserved.*
