# Issuers

Copy page



cURL

# Issuers

##### [Create Federation Issuer](api/http/beta/organization/federation/issuers/create.md)

POST/v1/organizations/federation\_issuers

##### [List Federation Issuers](api/http/beta/organization/federation/issuers/list.md)

GET/v1/organizations/federation\_issuers

##### [Get Federation Issuer](api/http/beta/organization/federation/issuers/retrieve.md)

GET/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Update Federation Issuer](api/http/beta/organization/federation/issuers/update.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Archive Federation Issuer](api/http/beta/organization/federation/issuers/archive.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}/archive

##### Models



BetaFederationIssuer object{ id, archived\_at, archived\_by\_actor\_id, 12 more }

Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523
jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.



BetaFederationIssuerPollStatus object{ consecutive\_failures, last\_fetched\_at, next\_poll\_at }

Status of automatic JWKS polling for a federation issuer.

Anthropic periodically fetches the issuer's signing keys in the
background. These fields summarize the most recent fetches so the
health of the JWKS endpoint can be monitored.

consecutive\_failures: number

Consecutive fetch failures since the last success.



last\_fetched\_at: string or null

When the last successful fetch completed.

formatdate-time



next\_poll\_at: string or null

When the next fetch is scheduled. Null if paused.

formatdate-time



BetaJWKSDiscovery object{ type, ca\_cert\_pem, discovery\_base }

JWKS via the issuer's OIDC discovery document.

type: "discovery"



ca\_cert\_pem: optional string or null

Optional custom CA (PEM) for TLS verification of the JWKS fetch.

maxLength8192

discovery\_base: optional string or null

Set when the discovery URL differs from `issuer_url`.



BetaJWKSExplicitURL object{ type, url, ca\_cert\_pem }

JWKS fetched from a fixed endpoint.

type: "explicit\_url"



url: string

JWKS endpoint.

minLength1



ca\_cert\_pem: optional string or null

Optional custom CA (PEM) for TLS verification of the JWKS fetch.

maxLength8192



BetaJWKSInline object{ keys, type }

JWKS supplied directly; no network fetch.



keys: array of map[unknown]

Inline JWK objects.

minItems1

type: "inline"

---

*Copyright © Anthropic. All rights reserved.*
