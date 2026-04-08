# User Profiles

Copy page

Ruby

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

beta.user\_profiles.create(\*\*kwargs) -> [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

beta.user\_profiles.list(\*\*kwargs) -> PageCursorV2<[BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more } >

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

beta.user\_profiles.retrieve(id, \*\*kwargs) -> [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

GET/v1/user\_profiles/{id}

##### [Update User Profile](api/beta/user_profiles/update.md)

beta.user\_profiles.update(id, \*\*kwargs) -> [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

POST/v1/user\_profiles/{id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

beta.user\_profiles.create\_enrollment\_url(id, \*\*kwargs) -> [BetaUserProfileEnrollmentURL](api/beta.md) { expires\_at, type, url }

POST/v1/user\_profiles/{id}/enrollment\_url

##### ModelsExpand Collapse

class BetaUserProfile { id, created\_at, metadata, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

metadata: Hash[Symbol, String]

trust\_grants: Hash[Symbol, [BetaUserProfileTrustGrant](api/beta.md) { status } ]

status: String

type: String

updated\_at: Time

A timestamp in RFC 3339 format

external\_id: String

class BetaUserProfileEnrollmentURL { expires\_at, type, url }

expires\_at: Time

A timestamp in RFC 3339 format

type: String

url: String

class BetaUserProfileTrustGrant { status }

status: String

---

*Copyright © Anthropic. All rights reserved.*
