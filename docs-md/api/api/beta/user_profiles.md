# User Profiles

Copy page

cURL

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

GET/v1/user\_profiles/{id}

##### [Update User Profile](api/beta/user_profiles/update.md)

POST/v1/user\_profiles/{id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

POST/v1/user\_profiles/{id}/enrollment\_url

##### ModelsExpand Collapse

BetaUserProfile = object { id, created\_at, metadata, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

trust\_grants: map[[BetaUserProfileTrustGrant](api/beta.md) { status } ]

status: string

type: string

updated\_at: string

A timestamp in RFC 3339 format

external\_id: optional string

BetaUserProfileEnrollmentURL = object { expires\_at, type, url }

expires\_at: string

A timestamp in RFC 3339 format

type: string

url: string

BetaUserProfileTrustGrant = object { status }

status: string

---

*Copyright © Anthropic. All rights reserved.*
