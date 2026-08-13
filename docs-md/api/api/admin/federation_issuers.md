# Federation Issuers

Copy page



# Federation Issuers

##### [Create Federation Issuer](api/admin/federation_issuers/create.md)

POST/v1/organizations/federation\_issuers

##### [Get Federation Issuer](api/admin/federation_issuers/retrieve.md)

GET/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [List Federation Issuers](api/admin/federation_issuers/list.md)

GET/v1/organizations/federation\_issuers

##### [Update Federation Issuer](api/admin/federation_issuers/update.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Archive Federation Issuer](api/admin/federation_issuers/archive.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}/archive

##### ModelsExpand Collapse



FederationIssuer object { id, archived\_at, archived\_by\_actor\_id, 12 more } 

Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523
jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

id: string

Tagged ID of the federation issuer.

archived\_at: string

If set, all rules referencing this issuer reject token exchange.

archived\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

check\_jti: boolean

Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

created\_at: string

When this issuer was created.

created\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

issuer\_url: string

The `iss` claim value. Incoming JWTs must match exactly.



jwks: object { type, ca\_cert\_pem, discovery\_base }  or object { type, url, ca\_cert\_pem }  or object { keys, type } 

How signing keys are obtained for signature verification.

One of the following:



Discovery object { type, ca\_cert\_pem, discovery\_base } 

JWKS via the issuer's OIDC discovery document.

type: "discovery"

ca\_cert\_pem: optional string

Optional custom CA (PEM) for TLS verification of the JWKS fetch.

discovery\_base: optional string

Set when the discovery URL differs from `issuer_url`.



ExplicitURL object { type, url, ca\_cert\_pem } 

JWKS fetched from a fixed endpoint.

type: "explicit\_url"

url: string

JWKS endpoint.

ca\_cert\_pem: optional string

Optional custom CA (PEM) for TLS verification of the JWKS fetch.



Inline object { keys, type } 

JWKS supplied directly; no network fetch.

keys: array of map[unknown]

Inline JWK objects.

type: "inline"

jwks\_polling\_disabled\_at: string

If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

max\_jwt\_lifetime\_seconds: number

Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

name: string

Admin-chosen slug identifier.



poll\_status: object { consecutive\_failures, last\_fetched\_at, next\_poll\_at } 

Status of automatic JWKS polling for a federation issuer.

Anthropic periodically fetches the issuer's signing keys in the
background. These fields summarize the most recent fetches so the
health of the JWKS endpoint can be monitored.

consecutive\_failures: number

Consecutive fetch failures since the last success.

last\_fetched\_at: string

When the last successful fetch completed.

next\_poll\_at: string

When the next fetch is scheduled. Null if paused.

type: "federation\_issuer"

updated\_at: string

When this issuer was last updated.

updated\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

---

*Copyright © Anthropic. All rights reserved.*
