# Update Federation Issuer

Copy page



# Update Federation Issuer

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}

Partially update a federation issuer.

Setting `jwks` replaces the full JWKS shape at once. Archived issuers
cannot be updated; this returns 400. Create a new issuer instead.

Updating an issuer that backs a rule with a scope outside
`workspace:developer` or `workspace:inference` requires a Console
session. Requires an OAuth bearer or Console session; Admin API keys
are not accepted.

##### Path parameters

federation\_issuer\_id: string

ID of the federation issuer to update.

##### Headers



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Body

check\_jti: optional boolean or null

Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.



issuer\_url: optional string or null

Replaces the `iss` claim value to match against. For discovery-mode issuers without a `discovery_base`, this is also the URL Anthropic fetches the OIDC discovery document and signing keys from, so changing it repoints the JWKS source. Changing the issuer URL to a well-known shared platform is rejected while any live rule under this issuer would not constrain tenant identity.

minLength1



jwks: optional object{ type, ca\_cert\_pem, discovery\_base } or object{ type, url, ca\_cert\_pem } or object{ keys, type } or null

Replaces the entire JWKS configuration.

One of the following:



Discovery object{ type, ca\_cert\_pem, discovery\_base }

JWKS via the issuer's OIDC discovery document.

type: "discovery"



ca\_cert\_pem: optional string or null

Optional custom CA (PEM) for TLS verification of the JWKS fetch.

maxLength8192

discovery\_base: optional string or null

Set when the discovery URL differs from `issuer_url`.



ExplicitURL object{ type, url, ca\_cert\_pem }

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

Inline object{ keys, type }

JWKS supplied directly; no network fetch.



keys: array of map[unknown]

Inline JWK objects.

minItems1

type: "inline"

jwks\_polling\_disabled: optional boolean or null

Only `false` is accepted, to re-enable polling after the system pauses it. Polling is paused automatically; sending `true` is rejected.



max\_jwt\_lifetime\_seconds: optional number or null

Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

maximum176400

exclusiveMinimum0



name: optional string or null

Replaces the slug identifier (lowercase, digits, hyphens). Unique within the organization; a duplicate name returns 409.

maxLength255

minLength1

##### Returns



FederationIssuer object{ id, archived\_at, archived\_by\_actor\_id, 12 more }

Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523
jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

### Update Federation Issuer

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/federation_issuers/$FEDERATION_ISSUER_ID \
    -H 'Content-Type: application/json' \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN" \
    -d '{}'
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
