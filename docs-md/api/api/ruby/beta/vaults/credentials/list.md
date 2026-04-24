# List Credentials

Copy page

Ruby

# List Credentials

beta.vaults.credentials.list(vault\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more } >

GET/v1/vaults/{vault\_id}/credentials

List Credentials

##### ParametersExpand Collapse

vault\_id: String

include\_archived: bool

Whether to include archived credentials in the results.

limit: Integer

Maximum number of credentials to return per page. Defaults to 20, maximum 100.

page: String

Opaque pagination token from a previous `list_credentials` response.

betas: Array[[AnthropicBeta](api/beta.md)]

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 19 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

:"advisor-tool-2026-03-01"

##### ReturnsExpand Collapse

class BetaManagedAgentsCredential { id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

id: String

Unique identifier for the credential.

archived\_at: Time

A timestamp in RFC 3339 format

auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta.md) { mcp\_server\_url, type, expires\_at, refresh }  | [BetaManagedAgentsStaticBearerAuthResponse](api/beta.md) { mcp\_server\_url, type }

Authentication details for a credential.

Accepts one of the following:

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

Accepts one of the following:

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

List Credentials

Ruby

```shiki
require "anthropic"

anthropic = Anthropic::Client.new(api_key: "my-anthropic-api-key")

page = anthropic.beta.vaults.credentials.list("vlt_011CZkZDLs7fYzm1hXNPeRjv")

puts(page)
```

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
