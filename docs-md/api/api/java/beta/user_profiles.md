# User Profiles

Copy page

Java

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

[BetaUserProfile](api/beta.md) beta().userProfiles().create(UserProfileCreateParamsparams = UserProfileCreateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

UserProfileListPage beta().userProfiles().list(UserProfileListParamsparams = UserProfileListParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

[BetaUserProfile](api/beta.md) beta().userProfiles().retrieve(UserProfileRetrieveParamsparams = UserProfileRetrieveParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

[BetaUserProfile](api/beta.md) beta().userProfiles().update(UserProfileUpdateParamsparams = UserProfileUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

[BetaUserProfileEnrollmentUrl](api/beta.md) beta().userProfiles().createEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparams = UserProfileCreateEnrollmentUrlParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse

class BetaUserProfile:

String id

Unique identifier for this user profile, prefixed `uprof_`.

LocalDateTime createdAt

A timestamp in RFC 3339 format

Metadata metadata

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

Relationship relationship

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

Accepts one of the following:

EXTERNAL("external")

RESOLD("resold")

INTERNAL("internal")

TrustGrants trustGrants

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

Status status

Status of the trust grant.

Accepts one of the following:

ACTIVE("active")

PENDING("pending")

REJECTED("rejected")

Type type

Object type. Always `user_profile`.

LocalDateTime updatedAt

A timestamp in RFC 3339 format

Optional<String> externalId

Platform's own identifier for this user. Not enforced unique.

Optional<String> name

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

class BetaUserProfileEnrollmentUrl:

LocalDateTime expiresAt

A timestamp in RFC 3339 format

Type type

Object type. Always `enrollment_url`.

String url

Enrollment URL to send to the end user. Valid until `expires_at`.

class BetaUserProfileTrustGrant:

Status status

Status of the trust grant.

Accepts one of the following:

ACTIVE("active")

PENDING("pending")

REJECTED("rejected")

---

*Copyright © Anthropic. All rights reserved.*
