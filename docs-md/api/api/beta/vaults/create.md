# Create Vault

Copy page

cURL

# Create Vault

POST/v1/vaults

Create Vault

##### Header ParametersExpand Collapse

"anthropic-beta": optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

Accepts one of the following:

UnionMember0 = string

UnionMember1 = "message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 18 more

Accepts one of the following:

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

##### Body ParametersJSONExpand Collapse

display\_name: string

Human-readable name for the vault. 1-255 characters.

metadata: optional map[string]

Arbitrary key-value metadata to attach to the vault.

##### ReturnsExpand Collapse

BetaManagedAgentsVault = object { id, archived\_at, created\_at, 4 more }

A vault that stores credentials for use by agents during sessions.

id: string

Unique identifier for the vault.

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

display\_name: string

Human-readable name for the vault.

metadata: map[string]

Arbitrary key-value metadata attached to the vault.

type: "vault"

updated\_at: string

A timestamp in RFC 3339 format

Create Vault

cURL

```shiki
curl https://api.anthropic.com/v1/vaults \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H 'anthropic-beta: managed-agents-2026-04-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -d '{
          "display_name": "Example vault"
        }'
```

Response 200

```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "vlt_011CZkZDLs7fYzm1hXNPeRjv",
  "archived_at": null,
  "created_at": "2026-03-15T10:00:00Z",
  "display_name": "Example vault",
  "metadata": {
    "environment": "production"
  },
  "type": "vault",
  "updated_at": "2026-03-15T10:00:00Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
