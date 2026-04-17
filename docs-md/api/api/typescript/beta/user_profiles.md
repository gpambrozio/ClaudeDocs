# User Profiles

Copy page

TypeScript

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

client.beta.userProfiles.create(UserProfileCreateParams { external\_id, metadata, betas } params, RequestOptionsoptions?): [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

client.beta.userProfiles.list(UserProfileListParams { limit, order, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more } >

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

client.beta.userProfiles.retrieve(stringuserProfileID, UserProfileRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

client.beta.userProfiles.update(stringuserProfileID, UserProfileUpdateParams { external\_id, metadata, betas } params, RequestOptionsoptions?): [BetaUserProfile](api/beta.md) { id, created\_at, metadata, 4 more }

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

client.beta.userProfiles.createEnrollmentURL(stringuserProfileID, UserProfileCreateEnrollmentURLParams { betas } params?, RequestOptionsoptions?): [BetaUserProfileEnrollmentURL](api/beta.md) { expires\_at, type, url }

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse

BetaUserProfile { id, created\_at, metadata, 4 more }

id: string

Unique identifier for this user profile, prefixed `uprof_`.

created\_at: string

A timestamp in RFC 3339 format

metadata: Record<string, string>

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

trust\_grants: Record<string, [BetaUserProfileTrustGrant](api/beta.md) { status } >

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

status: "active" | "pending" | "rejected"

Status of the trust grant.

Accepts one of the following:

"active"

"pending"

"rejected"

type: "user\_profile"

Object type. Always `user_profile`.

updated\_at: string

A timestamp in RFC 3339 format

external\_id?: string | null

Platform's own identifier for this user. Not enforced unique.

BetaUserProfileEnrollmentURL { expires\_at, type, url }

expires\_at: string

A timestamp in RFC 3339 format

type: "enrollment\_url"

Object type. Always `enrollment_url`.

url: string

Enrollment URL to send to the end user. Valid until `expires_at`.

BetaUserProfileTrustGrant { status }

status: "active" | "pending" | "rejected"

Status of the trust grant.

Accepts one of the following:

"active"

"pending"

"rejected"

---

*Copyright © Anthropic. All rights reserved.*
