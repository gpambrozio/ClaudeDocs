# Tunnel Certificates

Copy page

# Tunnel Certificates

##### [Create Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/create.md)

POST/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/retrieve.md)

GET/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/admin/mcp_tunnels/tunnel_certificates/list.md)

GET/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/archive.md)

POST/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

##### ModelsExpand Collapse

TunnelCertificateCreateResponse = object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

TunnelCertificateRetrieveResponse = object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

TunnelCertificateListResponse = object { data, next\_page }

data: array of object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

next\_page: string

Opaque cursor for the next page, or `null` if there are no more results.

TunnelCertificateArchiveResponse = object { id, archived\_at, created\_at, 4 more }

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

---

*Copyright © Anthropic. All rights reserved.*
