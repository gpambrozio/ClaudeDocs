# Create User Profile

Copy page

SDK language

CLI

# Create User Profile

$ ant beta:user-profiles create

POST/v1/user\_profiles

Create User Profile

##### ParametersExpand Collapse

--external-id: optional string

Body param: Platform's own identifier for this user. Not enforced unique. Maximum 255 characters.

--metadata: optional map[string]

Body param: Free-form key-value data to attach to this user profile. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters. Values must be non-empty strings.

--name: optional string

Body param: Display name of the entity this profile represents. Required when relationship is `resold` (the resold-to company's name); optional otherwise. Maximum 255 characters.

--relationship: optional "external" or "resold" or "internal"

Body param: How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



beta\_user\_profile: object { id, created\_at, metadata, 6 more } 

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

trust\_grants: map[[BetaUserProfileTrustGrant](api/beta.md) { status } ]

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

Create User Profile

CLI

```shiki
ant beta:user-profiles create \
  --api-key my-anthropic-api-key
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
