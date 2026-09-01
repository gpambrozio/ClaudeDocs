# Tunnel Certificates

Copy page



# Tunnel Certificates

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

##### Models



TunnelCertificateCreateResponse object{ id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.



archived\_at: string or null

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

formatdate-time



created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

formatdate-time



expires\_at: string or null

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

formatdate-time

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.



type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

defaulttunnel\_certificate



TunnelCertificateRetrieveResponse object{ id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.



archived\_at: string or null

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

formatdate-time



created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

formatdate-time



expires\_at: string or null

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

formatdate-time

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.



type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

defaulttunnel\_certificate



TunnelCertificateListResponse object{ id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.



archived\_at: string or null

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

formatdate-time



created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

formatdate-time



expires\_at: string or null

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

formatdate-time

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.



type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

defaulttunnel\_certificate



TunnelCertificateArchiveResponse object{ id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.



archived\_at: string or null

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

formatdate-time



created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

formatdate-time



expires\_at: string or null

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

formatdate-time

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.



type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

defaulttunnel\_certificate

---

*Copyright © Anthropic. All rights reserved.*
