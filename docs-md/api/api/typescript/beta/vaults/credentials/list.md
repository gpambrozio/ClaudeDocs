# List Credentials

Copy page

TypeScript

# List Credentials

client.beta.vaults.credentials.list(stringvaultID, CredentialListParams { include\_archived, limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more } >

GET/v1/vaults/{vault\_id}/credentials

List Credentials

##### ParametersExpand Collapse

vaultID: string

params: CredentialListParams { include\_archived, limit, page, betas }

include\_archived?: boolean

Query param: Whether to include archived credentials in the results.

limit?: number

Query param: Maximum number of credentials to return per page. Defaults to 20, maximum 100.

page?: string

Query param: Opaque pagination token from a previous `list_credentials` response.

betas?: Array<[AnthropicBeta](api/beta.md)>

Header param: Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

(string & {})

"message-batches-2024-09-24" | "prompt-caching-2024-07-31" | "computer-use-2024-10-22" | 18 more

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

##### ReturnsExpand Collapse

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

List Credentials

TypeScript

```shiki
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic({
  apiKey: process.env['ANTHROPIC_API_KEY'], // This is the default and can be omitted
});

// Automatically fetches more pages as needed.
for await (const betaManagedAgentsCredential of client.beta.vaults.credentials.list(
  'vlt_011CZkZDLs7fYzm1hXNPeRjv',
)) {
  console.log(betaManagedAgentsCredential.id);
}
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
