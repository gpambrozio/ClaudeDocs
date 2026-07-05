# Create Credential

Copy page



cURL

# Create Credential

POST/v1/vaults/{vault\_id}/credentials

Create Credential

##### Path ParametersExpand Collapse

vault\_id: string

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 25 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"fallback-credit-2026-06-01"

##### Body ParametersJSONExpand Collapse



auth: [BetaManagedAgentsMCPOAuthCreateParams](api/beta/vaults/credentials.md) { access\_token, mcp\_server\_url, type, 2 more }  or [BetaManagedAgentsStaticBearerCreateParams](api/beta/vaults/credentials.md) { token, mcp\_server\_url, type }  or [BetaManagedAgentsEnvironmentVariableCreateParams](api/beta/vaults/credentials.md) { networking, secret\_name, secret\_value, 2 more } 

Authentication details for creating a credential.

One of the following:



BetaManagedAgentsMCPOAuthCreateParams object { access\_token, mcp\_server\_url, type, 2 more } 

Parameters for creating an MCP OAuth credential.

access\_token: string

OAuth access token.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format



refresh: optional [BetaManagedAgentsMCPOAuthRefreshParams](api/beta/vaults/credentials.md) { client\_id, refresh\_token, token\_endpoint, 3 more } 

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

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneParam object { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthBasicParam object { client\_secret, type } 

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthPostParam object { client\_secret, type } 

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.



BetaManagedAgentsStaticBearerCreateParams object { token, mcp\_server\_url, type } 

Parameters for creating a static bearer token credential.

token: string

Static bearer token value.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"



BetaManagedAgentsEnvironmentVariableCreateParams object { networking, secret\_name, secret\_value, 2 more } 

Parameters for creating an environment variable credential.



networking: [BetaManagedAgentsCredentialNetworkingParams](api/beta/vaults/credentials.md)

Outbound hosts the secret value is substituted on.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingParams object { type } 

Substitute the secret on any host the session's Environment network policy permits egress to. The Environment's network policy is the only boundary on where the secret can reach.

type: "unrestricted"



BetaManagedAgentsLimitedCredentialNetworkingParams object { allowed\_hosts, type } 

Substitute the secret only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. Each entry is a bare hostname (`api.example.com`), an IPv4 address (`192.0.2.1`), or a `*.`-prefixed wildcard (`*.example.com`). URLs, ports, paths, and IPv6 addresses are not accepted. At most 16 entries.

type: "limited"

secret\_name: string

Name of the environment variable. Immutable after create.

secret\_value: string

Secret value. Write-only; never returned in responses.

type: "environment\_variable"



injection\_location: optional [BetaManagedAgentsInjectionLocationParams](api/beta/vaults/credentials.md) { body, header } 

Where in the outbound request the secret value may be substituted.

body: optional boolean

Substitute when the placeholder appears in the request body.

header: optional boolean

Substitute when the placeholder appears in a request header value.

display\_name: optional string

Human-readable name for the credential. Up to 255 characters.

metadata: optional map[string]

Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

##### ReturnsExpand Collapse



BetaManagedAgentsCredential object { id, archived\_at, auth, 6 more } 

A credential stored in a vault. Sensitive fields are never returned in responses.

id: string

Unique identifier for the credential.

archived\_at: string

A timestamp in RFC 3339 format



auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta/vaults/credentials.md) { mcp\_server\_url, type, expires\_at, refresh }  or [BetaManagedAgentsStaticBearerAuthResponse](api/beta/vaults/credentials.md) { mcp\_server\_url, type }  or [BetaManagedAgentsEnvironmentVariableAuthResponse](api/beta/vaults/credentials.md) { injection\_location, networking, secret\_name, type } 

Authentication details for a credential.

One of the following:



BetaManagedAgentsMCPOAuthAuthResponse object { mcp\_server\_url, type, expires\_at, refresh } 

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format



refresh: optional [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta/vaults/credentials.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more } 

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.



token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta/vaults/credentials.md) { type } 

Token endpoint requires no client authentication.

One of the following:



BetaManagedAgentsTokenEndpointAuthNoneResponse object { type } 

Token endpoint requires no client authentication.

type: "none"



BetaManagedAgentsTokenEndpointAuthBasicResponse object { type } 

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"



BetaManagedAgentsTokenEndpointAuthPostResponse object { type } 

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.



BetaManagedAgentsStaticBearerAuthResponse object { mcp\_server\_url, type } 

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"



BetaManagedAgentsEnvironmentVariableAuthResponse object { injection\_location, networking, secret\_name, type } 

Environment variable credential details. The secret value is never returned.



injection\_location: [BetaManagedAgentsInjectionLocationResponse](api/beta/vaults/credentials.md) { body, header } 

Where in the outbound request the secret value is substituted.

body: boolean

Whether the placeholder is substituted in the request body.

header: boolean

Whether the placeholder is substituted in request header values.



networking: [BetaManagedAgentsUnrestrictedCredentialNetworkingResponse](api/beta/vaults/credentials.md) { type }  or [BetaManagedAgentsLimitedCredentialNetworkingResponse](api/beta/vaults/credentials.md) { allowed\_hosts, type } 

Outbound hosts the secret value is substituted on.

One of the following:



BetaManagedAgentsUnrestrictedCredentialNetworkingResponse object { type } 

The secret is substituted on any host the session's Environment network policy permits egress to.

type: "unrestricted"



BetaManagedAgentsLimitedCredentialNetworkingResponse object { allowed\_hosts, type } 

The secret is substituted only on requests to the listed hosts.

allowed\_hosts: array of string

Hostnames on which the secret will be substituted. An entry matches the request host exactly; a `*.`-prefixed entry matches any subdomain of the named domain but not the domain itself.

type: "limited"

secret\_name: string

Name of the environment variable.

type: "environment\_variable"

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata attached to the credential.

type: "vault\_credential"

updated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name: optional string

Human-readable name for the credential.

Create Credential

cURL

```shiki
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "auth": {
            "token": "bearer_exampletoken",
            "mcp_server_url": "https://example-server.modelcontextprotocol.io/sse",
            "type": "static_bearer"
          },
          "display_name": "Example credential",
          "metadata": {
            "environment": "production"
          }
        }'
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
