# Rotate Tunnel Token

Copy page



# Rotate Tunnel Token

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/rotate\_token

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](api/beta/tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

Invalidate the tunnel's current token for new connections and return a fresh value.

Established connections are not severed by rotation; a connector
restarted after rotation must use the new value. An optional
`reason` is captured for operational context.

##### Path ParametersExpand Collapse

tunnel\_id: string

ID of the Tunnel.

##### Header ParametersExpand Collapse

"anthropic-beta": array of "mcp-tunnels-2026-05-19"

Required for all Tunnel endpoints.

##### Body ParametersJSONExpand Collapse

reason: optional string

Optional free-text reason for the rotation, recorded for audit.

##### ReturnsExpand Collapse

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.

type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.

Rotate Tunnel Token



```shiki
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/rotate_token \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "ttkn_bb97000eaec162831399ca9b6684a4fdf5be49ace5683057b017aab5c87e19e0",
  "tunnel_token": "eyJhIjoiRVhBTVBMRSIsInQiOiJFWEFNUExFIiwicyI6IkVYQU1QTEUifQ==",
  "type": "tunnel_token"
}
```

---

*Copyright © Anthropic. All rights reserved.*
