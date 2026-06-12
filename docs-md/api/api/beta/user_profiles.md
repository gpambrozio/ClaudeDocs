# User Profiles

Copy page

SDK language

cURL

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse



BetaUserProfile object { id, created\_at, metadata, 6 more } 

id: string

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



relationship: "external" or "resold" or "internal"

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

One of the following:

"external"

"resold"

"internal"



trust\_grants: map[[BetaUserProfileTrustGrant](api/beta.md) { status } ]

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.



status: "active" or "pending" or "rejected"

Status of the trust grant.

One of the following:

"active"

"pending"

"rejected"

type: "user\_profile"

Object type. Always `user_profile`.

updated\_at: string

A timestamp in RFC 3339 format

external\_id: optional string

Platform's own identifier for this user. Not enforced unique.

name: optional string

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.



BetaUserProfileEnrollmentURL object { expires\_at, type, url } 

expires\_at: string

A timestamp in RFC 3339 format

type: "enrollment\_url"

Object type. Always `enrollment_url`.

url: string

Enrollment URL to send to the end user. Valid until `expires_at`.



BetaUserProfileTrustGrant object { status } 



status: "active" or "pending" or "rejected"

Status of the trust grant.

One of the following:

"active"

"pending"

"rejected"

---

*Copyright © Anthropic. All rights reserved.*
