# User Profiles

Copy page

Go

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

client.Beta.UserProfiles.New(ctx, params) (\*[BetaUserProfile](api/beta.md), error)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

client.Beta.UserProfiles.List(ctx, params) (\*PageCursor[[BetaUserProfile](api/beta.md)], error)

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

client.Beta.UserProfiles.Get(ctx, userProfileID, query) (\*[BetaUserProfile](api/beta.md), error)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

client.Beta.UserProfiles.Update(ctx, userProfileID, params) (\*[BetaUserProfile](api/beta.md), error)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

client.Beta.UserProfiles.NewEnrollmentURL(ctx, userProfileID, body) (\*[BetaUserProfileEnrollmentURL](api/beta.md), error)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse

type BetaUserProfile struct{…}

ID string

Unique identifier for this user profile, prefixed `uprof_`.

CreatedAt Time

A timestamp in RFC 3339 format

Metadata map[string, string]

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

TrustGrants map[string, [BetaUserProfileTrustGrant](api/beta.md)]

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

Status BetaUserProfileTrustGrantStatus

Status of the trust grant.

Accepts one of the following:

const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"

const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"

const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"

Type BetaUserProfileType

Object type. Always `user_profile`.

UpdatedAt Time

A timestamp in RFC 3339 format

ExternalID stringoptional

Platform's own identifier for this user. Not enforced unique.

type BetaUserProfileEnrollmentURL struct{…}

ExpiresAt Time

A timestamp in RFC 3339 format

Type BetaUserProfileEnrollmentURLType

Object type. Always `enrollment_url`.

URL string

Enrollment URL to send to the end user. Valid until `expires_at`.

type BetaUserProfileTrustGrant struct{…}

Status BetaUserProfileTrustGrantStatus

Status of the trust grant.

Accepts one of the following:

const BetaUserProfileTrustGrantStatusActive BetaUserProfileTrustGrantStatus = "active"

const BetaUserProfileTrustGrantStatusPending BetaUserProfileTrustGrantStatus = "pending"

const BetaUserProfileTrustGrantStatusRejected BetaUserProfileTrustGrantStatus = "rejected"

---

*Copyright © Anthropic. All rights reserved.*
