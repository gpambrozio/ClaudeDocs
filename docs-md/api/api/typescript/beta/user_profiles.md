# User Profiles

Copy page

TypeScript

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

client.beta.userProfiles.create(UserProfileCreateParams { external\_id, metadata, betas } params, RequestOptionsoptions?): [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

client.beta.userProfiles.list(UserProfileListParams { limit, order, page, betas } params?, RequestOptionsoptions?): PageCursorV2<[BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more } >

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

client.beta.userProfiles.retrieve(stringid, UserProfileRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

GET/v1/user\_profiles/{id}

##### [Update User Profile](api/beta/user_profiles/update.md)

client.beta.userProfiles.update(stringid, UserProfileUpdateParams { external\_id, metadata, betas } params, RequestOptionsoptions?): [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

POST/v1/user\_profiles/{id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

client.beta.userProfiles.createEnrollmentURL(stringid, UserProfileCreateEnrollmentURLParams { betas } params?, RequestOptionsoptions?): [BetaUserProfileEnrollmentURL](api/beta.md) { expires\_at, type, url }

POST/v1/user\_profiles/{id}/enrollment\_url

##### ModelsExpand Collapse

BetaUserProfile { id, created\_at, metadata, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

metadata: Record<string, string>

trust\_grants: Record<string, [BetaUserProfileTrustGrant](api/beta.md) { status } >

status: string

type: string

updated\_at: string

A timestamp in RFC 3339 format

external\_id?: string | null

BetaUserProfileEnrollmentURL { expires\_at, type, url }

expires\_at: string

A timestamp in RFC 3339 format

type: string

url: string

BetaUserProfileTrustGrant { status }

status: string

---

*Copyright © Anthropic. All rights reserved.*
