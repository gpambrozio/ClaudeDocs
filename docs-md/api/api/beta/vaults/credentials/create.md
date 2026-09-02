# Create Credential

Copy page



cURL

# Create Credential

POST/v1/vaults/{vault\_id}/credentials

Create Credential

##### Path parameters

vault\_id: string

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 41 more

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

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

"mid-conversation-output-config-2026-07-01"

"thinking-binding-controls-2026-08-01"

"mid-conversation-system-clear-at-2026-08-21"

##### Body



auth: [BetaManagedAgentsMCPOAuthCreateParams](api/http/beta/vaults/credentials.md) { access\_token, mcp\_server\_url, type, 2 more } or [BetaManagedAgentsStaticBearerCreateParams](api/http/beta/vaults/credentials.md) { token, mcp\_server\_url, type } or [BetaManagedAgentsEnvironmentVariableCreateParams](api/http/beta/vaults/credentials.md) { networking, secret\_name, secret\_value, 2 more }

Authentication details for creating a credential.

One of the following:



BetaManagedAgentsMCPOAuthCreateParams object{ access\_token, mcp\_server\_url, type, 2 more }

Parameters for creating an MCP OAuth credential.



access\_token: string

OAuth access token.

minLength1

maxLength8192



mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

minLength1

maxLength2047

type: "mcp\_oauth"



expires\_at: optional string or null

A timestamp in RFC 3339 format

formatdate-time



refresh: optional [BetaManagedAgentsMCPOAuthRefreshParams](api/http/beta/vaults/credentials.md) { client\_id, refresh\_token, token\_endpoint, 3 more } or null

OAuth refresh token parameters for creating a credential with refresh support.



BetaManagedAgentsStaticBearerCreateParams object{ token, mcp\_server\_url, type }

Parameters for creating a static bearer token credential.



token: string

Static bearer token value.

minLength1

maxLength8192



mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

minLength1

maxLength2047

type: "static\_bearer"



BetaManagedAgentsEnvironmentVariableCreateParams object{ networking, secret\_name, secret\_value, 2 more }

Parameters for creating an environment variable credential.



display\_name: optional string or null

Human-readable name for the credential. Up to 255 characters.

maxLength255

metadata: optional map[string]

Arbitrary key-value metadata to attach to the credential. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

##### Returns



BetaManagedAgentsCredential object{ id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

Create Credential

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
