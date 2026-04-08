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

GET/v1/user\_profiles/{id}

##### [Update User Profile](api/beta/user_profiles/update.md)

[BetaUserProfile](api/beta.md) beta().userProfiles().update(UserProfileUpdateParamsparams = UserProfileUpdateParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles/{id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

[BetaUserProfileEnrollmentUrl](api/beta.md) beta().userProfiles().createEnrollmentUrl(UserProfileCreateEnrollmentUrlParamsparams = UserProfileCreateEnrollmentUrlParams.none(), RequestOptionsrequestOptions = RequestOptions.none())

POST/v1/user\_profiles/{id}/enrollment\_url

##### ModelsExpand Collapse

class BetaUserProfile:

String id

LocalDateTime createdAt

A timestamp in RFC 3339 format

Metadata metadata

TrustGrants trustGrants

String status

String type

LocalDateTime updatedAt

A timestamp in RFC 3339 format

Optional<String> externalId

class BetaUserProfileEnrollmentUrl:

LocalDateTime expiresAt

A timestamp in RFC 3339 format

String type

String url

class BetaUserProfileTrustGrant:

String status

---

*Copyright © Anthropic. All rights reserved.*
