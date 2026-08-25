# User Profiles

Copy page



cURL

# User Profiles

##### [Create User Profile](api/http/beta/user_profiles/create.md)

POST/v1/user\_profiles

##### [List User Profiles](api/http/beta/user_profiles/list.md)

GET/v1/user\_profiles

##### [Get User Profile](api/http/beta/user_profiles/retrieve.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/http/beta/user_profiles/update.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/http/beta/user_profiles/create_enrollment_url.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### Models



BetaUserProfile object{ id, created\_at, metadata, 7 more }



BetaUserProfileEnrollmentURL object{ expires\_at, type, url }



expires\_at: string

A timestamp in RFC 3339 format

formatdate-time

type: "enrollment\_url"

Object type. Always `enrollment_url`.

url: string

Enrollment URL to send to the end user. Valid until `expires_at`.



BetaUserProfileTrustGrant object{ status }



status: "active" or "pending" or "rejected"

Status of the trust grant.

One of the following:

"active"

"pending"

"rejected"

---

*Copyright © Anthropic. All rights reserved.*
