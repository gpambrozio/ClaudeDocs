# Federation Issuers

Copy page



# Federation Issuers

##### [Create Federation Issuer](api/http/admin/federation_issuers/create.md)

POST/v1/organizations/federation\_issuers

##### [Get Federation Issuer](api/http/admin/federation_issuers/retrieve.md)

GET/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [List Federation Issuers](api/http/admin/federation_issuers/list.md)

GET/v1/organizations/federation\_issuers

##### [Update Federation Issuer](api/http/admin/federation_issuers/update.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Archive Federation Issuer](api/http/admin/federation_issuers/archive.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}/archive

##### Models



FederationIssuer object{ id, archived\_at, archived\_by\_actor\_id, 12 more }

Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523
jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

---

*Copyright © Anthropic. All rights reserved.*
