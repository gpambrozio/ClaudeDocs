# Authenticate with vaults

Copy page

Vaults and credentials are authentication primitives that let you register credentials for third-party services once and reference them by ID at session creation. This means you don't need to run your own secret store, transmit tokens on every call, or lose track of which end user an agent acted on behalf of.

The vault reference is a per-session parameter, so you can manage your product at the agent level and your users at the session level.

All Managed Agents API requests require the `managed-agents-2026-04-01` beta header. The SDK sets the beta header automatically.

## Create a vault

Vaults and credentials are workspace-scoped, meaning anyone with API key access can use them for authorizing an agent to complete a task. To revoke access, delete the vault or credential.

A vault is the collection of `credentials` associated with an end-user. Give it a `display_name` and optionally tag it with `metadata` so you can map it back to your own user records.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
VAULT_ID=$(ant beta:vaults create \
  --display-name "Alice" \
  --metadata '{external_user_id: usr_abc123}' \
  --transform id --format yaml)
```

The response is the full vault record:

```shiki
{
  "type": "vault",
  "id": "vlt_01ABC...",
  "display_name": "Alice",
  "metadata": { "external_user_id": "usr_abc123" },
  "created_at": "2026-03-18T10:00:00Z",
  "updated_at": "2026-03-18T10:00:00Z",
  "archived_at": null
}
```

## Add a credential

Each credential binds to a single `mcp_server_url`. When the agent connects to an MCP server at session runtime, the API matches the server URL against active credentials on the referenced vault and injects the token.

MCP OAuth credential

MCP OAuth credential

Static bearer credential

Static bearer credential

Use `mcp_oauth` when the MCP server uses OAuth 2.0. If you supply a `refresh` block, Anthropic refreshes the access token on your behalf when it expires.

The `refresh.token_endpoint_auth.type` field indicates how to authenticate the refresh call:

- `none`: public client
- `client_secret_basic`: HTTP Basic auth with the client secret
- `client_secret_post`: client secret in the POST body

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
CREDENTIAL_ID=$(ant beta:vaults:credentials create \
  --vault-id "$VAULT_ID" \
  --display-name "Alice's Slack" \
  --transform id --format yaml <<'EOF'
auth:
  type: mcp_oauth
  mcp_server_url: https://mcp.slack.com/mcp
  access_token: xoxp-...
  expires_at: "2026-04-15T00:00:00Z"
  refresh:
    token_endpoint: https://slack.com/api/oauth.v2.access
    client_id: "1234567890.0987654321"
    scope: channels:read chat:write
    refresh_token: xoxe-1-...
    token_endpoint_auth:
      type: client_secret_post
      client_secret: abc123...
EOF
)
```

Secret fields (`token`, `access_token`, `refresh_token`, `client_secret`) are write-only. They are never returned in API responses.

Credentials are stored as provided and are not validated until session runtime. A bad token surfaces as an MCP auth error during the session, which is emitted but does not block the session from continuing.

Constraints:

- **One active credential per `mcp_server_url` per vault.** Creating a second credential for the same URL returns a 409.
- **`mcp_server_url` is immutable.** To point at a different server, archive this credential and create a new one.
- **Maximum 20 credentials per vault.** This matches the maximum amount of MCP servers per agent.

## Rotate a credential

Only the secret payload and a handful of metadata fields are mutable. `mcp_server_url`, `token_endpoint`, and `client_id` are locked after creation.

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
ant beta:vaults:credentials update \
  --vault-id "$VAULT_ID" \
  --credential-id "$CREDENTIAL_ID" <<'EOF'
auth:
  type: mcp_oauth
  access_token: xoxp-new-...
  expires_at: "2026-05-15T00:00:00Z"
  refresh:
    refresh_token: xoxe-1-new-...
EOF
```

## Reference the vault at session creation

Pass `vault_ids` when creating a session:

curlCLIPythonTypeScriptC#GoJavaPHPRuby

```shiki
session = client.beta.sessions.create(
    agent=agent.id,
    environment_id=environment.id,
    vault_ids=[vault.id],
    title="Alice's Slack digest",
)
```

Runtime behavior:

- Credentials are re-resolved periodically during the session, so a rotation or archive propagates to running sessions without a restart.
- When a vault has no credential for the MCP server, the connection is attempted unauthenticated and produces an error.
- When multiple vaults cover the the MCP server, the first vault with a match wins.

## Other operations

- **List vaults or credentials:** Paginated, newest first. Archived records are excluded by default (pass `include_archived=true` to include them).
- **Archive a vault:** `POST /v1/vaults/{id}/archive`. Cascades to all credentials. Secrets are purged; records are retained for auditing. Future sessions referencing this vault fail; running sessions continue.
- **Archive a credential:** `POST /v1/vaults/{id}/credentials/{cred_id}/archive`. Purges the secret payload; `mcp_server_url` remains visible. Frees the `mcp_server_url` for a replacement credential.
- **Delete a vault or credential:** Hard delete. The record is not retained. Use archive if you need an audit trail.

Was this page helpful?

---

*Copyright © Anthropic. All rights reserved.*
