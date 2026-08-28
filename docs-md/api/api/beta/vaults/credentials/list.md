# List Credentials

Copy page



cURL

# List Credentials

GET/v1/vaults/{vault\_id}/credentials

List Credentials

##### Path parameters

vault\_id: string

##### Query parameters

include\_archived: optional boolean

Whether to include archived credentials in the results.



limit: optional number

Maximum number of credentials to return per page. Defaults to 20, maximum 100.

formatint32

page: optional string

Opaque pagination token from a previous `list_credentials` response.

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more

One of the following:

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

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

##### Returns



data: optional array of [BetaManagedAgentsCredential](api/http/beta/vaults/credentials.md) { id, archived\_at, auth, 6 more }

List of credentials.

id: string

Unique identifier for the credential.



archived\_at: string or null

A timestamp in RFC 3339 format

formatdate-time



auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/http/beta/vaults/credentials.md) { mcp\_server\_url, type, expires\_at, refresh } or [BetaManagedAgentsStaticBearerAuthResponse](api/http/beta/vaults/credentials.md) { mcp\_server\_url, type } or [BetaManagedAgentsEnvironmentVariableAuthResponse](api/http/beta/vaults/credentials.md) { injection\_location, networking, secret\_name, type }

Authentication details for a credential.

One of the following:

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

BetaManagedAgentsStaticBearerAuthResponse object{ mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"



BetaManagedAgentsEnvironmentVariableAuthResponse object{ injection\_location, networking, secret\_name, type }

Environment variable credential details. The secret value is never returned.



created\_at: string

A timestamp in RFC 3339 format

formatdate-time

metadata: map[string]

Arbitrary key-value metadata attached to the credential.

type: "vault\_credential"



updated\_at: string

A timestamp in RFC 3339 format

formatdate-time

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name: optional string or null

Human-readable name for the credential.

next\_page: optional string or null

Pagination token for the next page, or null if no more results.



### List Credentials

cURL



```shiki
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



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



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
