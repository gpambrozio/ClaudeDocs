# User Profiles

Copy page

Python

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

beta.user\_profiles.create(UserProfileCreateParams\*\*kwargs)  -> [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

beta.user\_profiles.list(UserProfileListParams\*\*kwargs)  -> SyncPageCursorV2[[BetaUserProfile](api/beta.md)]

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

beta.user\_profiles.retrieve(strid, UserProfileRetrieveParams\*\*kwargs)  -> [BetaUserProfile](api/beta.md)

GET/v1/user\_profiles/{id}

##### [Update User Profile](api/beta/user_profiles/update.md)

beta.user\_profiles.update(strid, UserProfileUpdateParams\*\*kwargs)  -> [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles/{id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

beta.user\_profiles.create\_enrollment\_url(strid, UserProfileCreateEnrollmentURLParams\*\*kwargs)  -> [BetaUserProfileEnrollmentURL](api/beta.md)

POST/v1/user\_profiles/{id}/enrollment\_url

##### ModelsExpand Collapse

class BetaUserProfile: …

id: str

created\_at: datetime

A timestamp in RFC 3339 format

metadata: Dict[str, str]

trust\_grants: Dict[str, [BetaUserProfileTrustGrant](api/beta.md)]

status: str

type: str

updated\_at: datetime

A timestamp in RFC 3339 format

external\_id: Optional[str]

class BetaUserProfileEnrollmentURL: …

expires\_at: datetime

A timestamp in RFC 3339 format

type: str

url: str

class BetaUserProfileTrustGrant: …

status: str

---

*Copyright © Anthropic. All rights reserved.*
