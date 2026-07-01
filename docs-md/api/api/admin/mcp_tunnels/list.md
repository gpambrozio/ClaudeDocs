# List Tunnels

Copy page



# List Tunnels

Deprecated

GET/v1/organizations/tunnels

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](api/beta/tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

List the organization's tunnels.

Results span the caller's organization, ordered by creation time
(newest first). Use `workspace_id` to filter to a single workspace;
archived tunnels are excluded unless `include_archived` is set.

##### Query ParametersExpand Collapse

include\_archived: optional boolean

Include archived tunnels in the results. Archived tunnels are excluded by
default.

limit: optional number

Maximum number of tunnels to return in a single page.

page: optional string

Opaque pagination cursor from a previous response's `next_page`. Omit to
fetch the first page.

workspace\_id: optional string

Return only tunnels in this Workspace. Accepts a `wrkspc_`-prefixed
Workspace ID; omit to list tunnels across all Workspaces.

##### Header ParametersExpand Collapse

"anthropic-beta": array of "mcp-tunnels-2026-05-19"

Required for all Tunnel endpoints.

##### ReturnsExpand Collapse



data: array of object { id, archived\_at, created\_at, 4 more } 

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.

next\_page: string

Opaque cursor for the next page, or `null` if there are no more results.

List Tunnels



```shiki
curl https://api.anthropic.com/v1/organizations/tunnels \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Production",
      "domain": "a1b2c3d4.tunnel.anthropic.com",
      "type": "tunnel",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
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
      "id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_name": "Production",
      "domain": "a1b2c3d4.tunnel.anthropic.com",
      "type": "tunnel",
      "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
