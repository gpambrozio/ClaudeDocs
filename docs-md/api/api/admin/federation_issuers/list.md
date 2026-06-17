# List Federation Issuers

Copy page



# List Federation Issuers

GET/v1/organizations/federation\_issuers

List federation issuers in your organization.

Archived issuers are excluded unless `include_archived=true`.

##### Query ParametersExpand Collapse

include\_archived: optional boolean

Include archived resources. Defaults to false.

limit: optional number

Number of results per page.

page: optional string

Opaque cursor from a previous response's `next_page`.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### ReturnsExpand Collapse



data: array of [FederationIssuer](api/admin.md) { id, archived\_at, archived\_by\_actor\_id, 12 more } 

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

next\_page: string

Opaque cursor for the next page, or null if no more results.

List Federation Issuers



```shiki
curl https://api.anthropic.com/v1/organizations/federation_issuers \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "check_jti": true,
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {
        "type": "discovery",
        "ca_cert_pem": "ca_cert_pem",
        "discovery_base": "discovery_base"
      },
      "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
      "max_jwt_lifetime_seconds": 0,
      "name": "github-actions",
      "poll_status": {
        "consecutive_failures": 0,
        "last_fetched_at": "2019-12-27T18:11:19.117Z",
        "next_poll_at": "2019-12-27T18:11:19.117Z"
      },
      "type": "federation_issuer",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "fdis_01SDCCSbTxrXDpWc1phhtcfK",
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "check_jti": true,
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "issuer_url": "https://token.actions.githubusercontent.com",
      "jwks": {
        "type": "discovery",
        "ca_cert_pem": "ca_cert_pem",
        "discovery_base": "discovery_base"
      },
      "jwks_polling_disabled_at": "2019-12-27T18:11:19.117Z",
      "max_jwt_lifetime_seconds": 0,
      "name": "github-actions",
      "poll_status": {
        "consecutive_failures": 0,
        "last_fetched_at": "2019-12-27T18:11:19.117Z",
        "next_poll_at": "2019-12-27T18:11:19.117Z"
      },
      "type": "federation_issuer",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
