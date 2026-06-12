# User Profiles

Copy page

SDK language

Python

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

beta.user\_profiles.create(UserProfileCreateParams\*\*kwargs)  -> [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

beta.user\_profiles.list(UserProfileListParams\*\*kwargs)  -> SyncPageCursor[[BetaUserProfile](api/beta.md)]

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

beta.user\_profiles.retrieve(struser\_profile\_id, UserProfileRetrieveParams\*\*kwargs)  -> [BetaUserProfile](api/beta.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

beta.user\_profiles.update(struser\_profile\_id, UserProfileUpdateParams\*\*kwargs)  -> [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

beta.user\_profiles.create\_enrollment\_url(struser\_profile\_id, UserProfileCreateEnrollmentURLParams\*\*kwargs)  -> [BetaUserProfileEnrollmentURL](api/beta.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse



class BetaUserProfile: …

id: str

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: datetime

A timestamp in RFC 3339 format

metadata: Dict[str, str]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.



relationship: Literal["external", "resold", "internal"]

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

One of the following:

"external"

"resold"

"internal"



trust\_grants: Dict[str, [BetaUserProfileTrustGrant](api/beta.md)]

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.



status: Literal["active", "pending", "rejected"]

Status of the trust grant.

One of the following:

"active"

"pending"

"rejected"

type: Literal["user\_profile"]

Object type. Always `user_profile`.

updated\_at: datetime

A timestamp in RFC 3339 format

external\_id: Optional[str]

Platform's own identifier for this user. Not enforced unique.

name: Optional[str]

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.



class BetaUserProfileEnrollmentURL: …

expires\_at: datetime

A timestamp in RFC 3339 format

type: Literal["enrollment\_url"]

Object type. Always `enrollment_url`.

url: str

Enrollment URL to send to the end user. Valid until `expires_at`.



class BetaUserProfileTrustGrant: …



status: Literal["active", "pending", "rejected"]

Status of the trust grant.

One of the following:

"active"

"pending"

"rejected"

---

*Copyright © Anthropic. All rights reserved.*
