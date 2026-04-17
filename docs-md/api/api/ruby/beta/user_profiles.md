# User Profiles

Copy page

Ruby

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

beta.user\_profiles.create(\*\*kwargs) -> [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

beta.user\_profiles.list(\*\*kwargs) -> PageCursor<[BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more } >

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

beta.user\_profiles.retrieve(user\_profile\_id, \*\*kwargs) -> [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

beta.user\_profiles.update(user\_profile\_id, \*\*kwargs) -> [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

beta.user\_profiles.create\_enrollment\_url(user\_profile\_id, \*\*kwargs) -> [BetaUserProfileEnrollmentURL](api/beta.md) { expires\_at, type, url }

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse

class BetaUserProfile { id, created\_at, metadata, 4 more }

id: String

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: Time

A timestamp in RFC 3339 format

metadata: Hash[Symbol, String]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

trust\_grants: Hash[Symbol, [BetaUserProfileTrustGrant](api/beta.md) { status } ]

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

status: :active | :pending | :rejected

Status of the trust grant.

Accepts one of the following:

:active

:pending

:rejected

type: :user\_profile

Object type. Always `user_profile`.

updated\_at: Time

A timestamp in RFC 3339 format

external\_id: String

Platform's own identifier for this user. Not enforced unique.

class BetaUserProfileEnrollmentURL { expires\_at, type, url }

expires\_at: Time

A timestamp in RFC 3339 format

type: :enrollment\_url

Object type. Always `enrollment_url`.

url: String

Enrollment URL to send to the end user. Valid until `expires_at`.

class BetaUserProfileTrustGrant { status }

status: :active | :pending | :rejected

Status of the trust grant.

Accepts one of the following:

:active

:pending

:rejected

---

*Copyright © Anthropic. All rights reserved.*
