# User Profiles

Copy page

C#

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

[BetaUserProfile](api/beta.md) Beta.UserProfiles.Create(UserProfileCreateParams?parameters, CancellationTokencancellationToken = default)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

[UserProfileListPageResponse](api/beta.md) Beta.UserProfiles.List(UserProfileListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

[BetaUserProfile](api/beta.md) Beta.UserProfiles.Retrieve(UserProfileRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

[BetaUserProfile](api/beta.md) Beta.UserProfiles.Update(UserProfileUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

[BetaUserProfileEnrollmentUrl](api/beta.md) Beta.UserProfiles.CreateEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparameters, CancellationTokencancellationToken = default)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse

class BetaUserProfile:

required string ID

Unique identifier for this user profile, prefixed `uprof_`.

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required IReadOnlyDictionary<string, string> Metadata

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

required IReadOnlyDictionary<string, [BetaUserProfileTrustGrant](api/beta.md)> TrustGrants

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

required Status Status

Status of the trust grant.

Accepts one of the following:

"active"Active

"pending"Pending

"rejected"Rejected

required Type Type

Object type. Always `user_profile`.

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

string? ExternalID

Platform's own identifier for this user. Not enforced unique.

class BetaUserProfileEnrollmentUrl:

required DateTimeOffset ExpiresAt

A timestamp in RFC 3339 format

required Type Type

Object type. Always `enrollment_url`.

required string Url

Enrollment URL to send to the end user. Valid until `expires_at`.

class BetaUserProfileTrustGrant:

required Status Status

Status of the trust grant.

Accepts one of the following:

"active"Active

"pending"Pending

"rejected"Rejected

---

*Copyright © Anthropic. All rights reserved.*
