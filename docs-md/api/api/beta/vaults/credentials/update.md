# Update Credential

Copy page



cURL

# Update Credential

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

Update Credential

##### Path parameters

vault\_id: string

credential\_id: string

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 31 more

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

##### Body



auth: optional [BetaManagedAgentsMCPOAuthUpdateParams](api/http/beta/vaults/credentials.md) { type, access\_token, expires\_at, refresh } or [BetaManagedAgentsStaticBearerUpdateParams](api/http/beta/vaults/credentials.md) { type, token } or [BetaManagedAgentsEnvironmentVariableUpdateParams](api/http/beta/vaults/credentials.md) { type, injection\_location, networking, secret\_value }

Updated authentication details for a credential.

One of the following:

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

BetaManagedAgentsStaticBearerUpdateParams object{ type, token }

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static\_bearer"



token: optional string or null

Updated static bearer token value.

minLength1

maxLength8192



BetaManagedAgentsEnvironmentVariableUpdateParams object{ type, injection\_location, networking, secret\_value }

Parameters for updating an environment variable credential. `secret_name` is immutable.



display\_name: optional string or null

Updated human-readable name for the credential. 1-255 characters.

minLength1

maxLength255

metadata: optional map[string] or null

Metadata patch. Set a key to a string to upsert it, or to null to delete it. Omitted keys are preserved.

##### Returns



BetaManagedAgentsCredential object{ id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

### Update Credential

cURL



```shiki
curl https://api.anthropic.com/v1/vaults/$VAULT_ID/credentials/$CREDENTIAL_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
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
