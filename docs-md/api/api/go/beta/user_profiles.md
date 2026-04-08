# User Profiles

Copy page

Go

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

client.Beta.UserProfiles.New(ctx, params) (\*[BetaUserProfile](api/beta.md), error)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

client.Beta.UserProfiles.List(ctx, params) (\*PageCursorV2[[BetaUserProfile](api/beta.md)], error)

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

client.Beta.UserProfiles.Get(ctx, id, query) (\*[BetaUserProfile](api/beta.md), error)

GET/v1/user\_profiles/{id}

##### [Update User Profile](api/beta/user_profiles/update.md)

client.Beta.UserProfiles.Update(ctx, id, params) (\*[BetaUserProfile](api/beta.md), error)

POST/v1/user\_profiles/{id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

client.Beta.UserProfiles.NewEnrollmentURL(ctx, id, body) (\*[BetaUserProfileEnrollmentURL](api/beta.md), error)

POST/v1/user\_profiles/{id}/enrollment\_url

##### ModelsExpand Collapse

type BetaUserProfile struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

Metadata map[string, string]

TrustGrants map[string, [BetaUserProfileTrustGrant](api/beta.md)]

Status string

Type string

UpdatedAt Time

A timestamp in RFC 3339 format

ExternalID stringoptional

type BetaUserProfileEnrollmentURL struct{…}

ExpiresAt Time

A timestamp in RFC 3339 format

Type string

URL string

type BetaUserProfileTrustGrant struct{…}

Status string

---

*Copyright © Anthropic. All rights reserved.*
