# MCP Tunnels

Copy page



# MCP Tunnels

##### [Get Tunnel](api/http/admin/mcp_tunnels/retrieve.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}

##### [List Tunnels](api/http/admin/mcp_tunnels/list.md)

Deprecated

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](api/http/admin/mcp_tunnels/reveal_token.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/reveal\_token

##### [Rotate Tunnel Token](api/http/admin/mcp_tunnels/rotate_token.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/rotate\_token

##### [Archive Tunnel](api/http/admin/mcp_tunnels/archive.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/archive

##### Models



MCPTunnelRetrieveResponse object{ id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.



archived\_at: string or null

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

formatdate-time



created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

formatdate-time

display\_name: string or null

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.



type: "tunnel"

Object type. Always `tunnel` for Tunnels.

defaulttunnel

workspace\_id: string or null

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.



MCPTunnelListResponse object{ id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.



archived\_at: string or null

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

formatdate-time



created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

formatdate-time

display\_name: string or null

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.



type: "tunnel"

Object type. Always `tunnel` for Tunnels.

defaulttunnel

workspace\_id: string or null

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.



MCPTunnelArchiveResponse object{ id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel.



archived\_at: string or null

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

formatdate-time



created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

formatdate-time

display\_name: string or null

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.



type: "tunnel"

Object type. Always `tunnel` for Tunnels.

defaulttunnel

workspace\_id: string or null

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.



MCPTunnelRevealTokenResponse object{ id, tunnel\_token, type }

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.



type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.

defaulttunnel\_token



MCPTunnelRotateTokenResponse object{ id, tunnel\_token, type }

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.



type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.

defaulttunnel\_token

#### MCP Tunnels[Tunnel Certificates](api/http/admin/mcp_tunnels/tunnel_certificates.md)

##### [Create Tunnel Certificate](api/http/admin/mcp_tunnels/tunnel_certificates/create.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/http/admin/mcp_tunnels/tunnel_certificates/retrieve.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/http/admin/mcp_tunnels/tunnel_certificates/list.md)

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/http/admin/mcp_tunnels/tunnel_certificates/archive.md)

Deprecated

POST/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

---

*Copyright © Anthropic. All rights reserved.*
