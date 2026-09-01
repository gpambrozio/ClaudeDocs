# List Tunnel Certificates

Copy page



# List Tunnel Certificates

Deprecated

GET/v1/organizations/tunnels/{tunnel\_id}/certificates

**Deprecated.** This Admin API endpoint is superseded by `/v1/tunnels` on the Claude API and will be removed after a migration window. New integrations should use [`/v1/tunnels`](api/beta/tunnels.md) with the `anthropic-beta: mcp-tunnels-2026-06-22` header and a WIF token carrying the `workspace:manage_tunnels` scope. Existing integrations continue to work with the `mcp-tunnels-2026-05-19` header and `org:manage_tunnels` scope during the migration window.

List the certificates registered on a tunnel.

Archived certificates are excluded unless `include_archived` is set.

##### Path parameters

tunnel\_id: string

ID of the Tunnel.

##### Query parameters



include\_archived: optional boolean

Include archived certificates in the results. Archived certificates are
excluded by default.

defaultfalse



limit: optional number

Maximum number of certificates to return.

default20

maximum1000

minimum1

page: optional string

A tunnel has at most two active certificates, so this list is not
paginated.

##### Headers

"anthropic-beta": array of "mcp-tunnels-2026-05-19"

Required for all Tunnel endpoints.

##### Returns



data: array of object{ id, archived\_at, created\_at, 4 more }

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

next\_page: string or null

Opaque cursor for the next page, or `null` if there are no more results.

List Tunnel Certificates

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/tunnels/$TUNNEL_ID/certificates \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
      "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "type": "tunnel_certificate"
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
      "id": "tcrt_01JmWq4ZxnBvR7tKpY2sLdH9",
      "archived_at": "2024-11-01T23:59:27.427722Z",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "expires_at": "2024-10-30T23:58:27.427722Z",
      "fingerprint": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08",
      "tunnel_id": "tnl_01Hx9Kp2RtQvMn3sWbYdLcF8",
      "type": "tunnel_certificate"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
