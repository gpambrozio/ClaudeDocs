# List User Profiles

Copy page



CLI

# List User Profiles

$ ant beta:user-profiles list

GET/v1/user\_profiles

List User Profiles

##### ParametersExpand Collapse

--limit: optional number

Query param: Query parameter for limit

--order: optional "asc" or "desc"

Query param: Query parameter for order

--page: optional string

Query param: Query parameter for page

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



BetaListUserProfilesResponse: object { data, next\_page } 



data: array of [BetaUserProfile](api/beta/user_profiles.md) { id, created\_at, metadata, 6 more } 

User profiles on this page.

id: string

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



relationship: "external" or "resold" or "internal"

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

"external"

"resold"

"internal"



trust\_grants: map[[BetaUserProfileTrustGrant](api/beta/user_profiles.md) { status } ]

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.



status: "active" or "pending" or "rejected"

Status of the trust grant.

"active"

"pending"

"rejected"



type: "user\_profile"

Object type. Always `user_profile`.

"user\_profile"

updated\_at: string

A timestamp in RFC 3339 format

external\_id: optional string

Platform's own identifier for this user. Not enforced unique.

name: optional string

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

next\_page: string

Cursor for the next page, or `null` when there are no more results.

List User Profiles

CLI

```shiki
ant beta:user-profiles list \
  --api-key my-anthropic-api-key
```

Response 200



```shiki
{
  "data": [
    {
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "relationship": "external",
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "external_id": "user_12345",
      "name": "Example User"
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
      "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
      "created_at": "2026-03-15T10:00:00Z",
      "metadata": {},
      "relationship": "external",
      "trust_grants": {
        "cyber": {
          "status": "active"
        }
      },
      "type": "user_profile",
      "updated_at": "2026-03-15T10:00:00Z",
      "external_id": "user_12345",
      "name": "Example User"
    }
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
