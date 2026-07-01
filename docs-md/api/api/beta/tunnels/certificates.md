# Certificates

Copy page



cURL

# Certificates

##### [Create Tunnel Certificate](api/beta/tunnels/certificates/create.md)

POST/v1/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/beta/tunnels/certificates/retrieve.md)

GET/v1/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/beta/tunnels/certificates/list.md)

GET/v1/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/beta/tunnels/certificates/archive.md)

POST/v1/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

##### ModelsExpand Collapse



BetaTunnelCertificate object { id, archived\_at, created\_at, 4 more } 

A CA certificate attached to a tunnel.

id: string

Unique identifier for the certificate, prefixed with `tcrt_`.

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

expires\_at: string

A timestamp in RFC 3339 format

fingerprint: string

Lowercase hex SHA-256 fingerprint of the certificate's DER encoding.

tunnel\_id: string

ID of the tunnel the certificate is registered against.

type: "tunnel\_certificate"

---

*Copyright © Anthropic. All rights reserved.*
