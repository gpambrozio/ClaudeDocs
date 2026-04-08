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

GET/v1/user\_profiles/{id}

##### [Update User Profile](api/beta/user_profiles/update.md)

[BetaUserProfile](api/beta.md) Beta.UserProfiles.Update(UserProfileUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/user\_profiles/{id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

[BetaUserProfileEnrollmentUrl](api/beta.md) Beta.UserProfiles.CreateEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparameters, CancellationTokencancellationToken = default)

POST/v1/user\_profiles/{id}/enrollment\_url

##### ModelsExpand Collapse

class BetaUserProfile:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required IReadOnlyDictionary<string, string> Metadata

required IReadOnlyDictionary<string, [BetaUserProfileTrustGrant](api/beta.md)> TrustGrants

required string Status

required string Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

string? ExternalID

class BetaUserProfileEnrollmentUrl:

required DateTimeOffset ExpiresAt

A timestamp in RFC 3339 format

required string Type

required string Url

class BetaUserProfileTrustGrant:

required string Status

---

*Copyright © Anthropic. All rights reserved.*
