# Tunnels

Copy page



cURL

# Tunnels

##### [Create Tunnel](api/http/beta/tunnels/create.md)

POST/v1/tunnels

##### [Get Tunnel](api/http/beta/tunnels/retrieve.md)

GET/v1/tunnels/{tunnel\_id}

##### [List Tunnels](api/http/beta/tunnels/list.md)

GET/v1/tunnels

##### [Archive Tunnel](api/http/beta/tunnels/archive.md)

POST/v1/tunnels/{tunnel\_id}/archive

##### [Reveal Tunnel Token](api/http/beta/tunnels/reveal_token.md)

POST/v1/tunnels/{tunnel\_id}/reveal\_token

##### [Rotate Tunnel Token](api/http/beta/tunnels/rotate_token.md)

POST/v1/tunnels/{tunnel\_id}/rotate\_token

##### Models



BetaTunnel object{ id, archived\_at, created\_at, 3 more }

An MCP tunnel.

id: string

Unique identifier for the tunnel, prefixed with `tnl_`.



archived\_at: string or null

A timestamp in RFC 3339 format

formatdate-time



created\_at: string

A timestamp in RFC 3339 format

formatdate-time

display\_name: string or null

Human-readable name for the tunnel (1-255 characters). Null if unset.

domain: string

Anthropic-assigned hostname for the tunnel. MCP server URLs whose host is a subdomain of this value are routed through the tunnel. Globally unique and never reused, even after the tunnel is archived.

type: "tunnel"



BetaTunnelToken object{ id, tunnel\_token, type }

A tunnel's connector token.

id: string

Stable identifier for the current token value. Changes when the token is rotated.

tunnel\_token: string

The connector token used to run the tunnel. Treat as a credential.

type: "tunnel\_token"

#### Tunnels[Certificates](api/http/beta/tunnels/certificates.md)

##### [Create Tunnel Certificate](api/http/beta/tunnels/certificates/create.md)

POST/v1/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/http/beta/tunnels/certificates/retrieve.md)

GET/v1/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/http/beta/tunnels/certificates/list.md)

GET/v1/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/http/beta/tunnels/certificates/archive.md)

POST/v1/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

---

*Copyright © Anthropic. All rights reserved.*
