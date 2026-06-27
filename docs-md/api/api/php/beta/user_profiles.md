# User Profiles

Copy page



PHP

# User Profiles

##### [Create User Profile](api/beta/user_profiles/create.md)

$client->beta->userProfiles->create(?string externalID, ?array<string,string> metadata, ?string name, ?[Relationship](api/beta/user_profiles/create.md) relationship, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta/user_profiles.md)

POST/v1/user\_profiles

##### [List User Profiles](api/beta/user_profiles/list.md)

$client->beta->userProfiles->list(?int limit, ?[Order](api/beta/user_profiles/list.md) order, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaUserProfile](api/beta/user_profiles.md)>

GET/v1/user\_profiles

##### [Get User Profile](api/beta/user_profiles/retrieve.md)

$client->beta->userProfiles->retrieve(string userProfileID, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta/user_profiles.md)

GET/v1/user\_profiles/{user\_profile\_id}

##### [Update User Profile](api/beta/user_profiles/update.md)

$client->beta->userProfiles->update(string userProfileID, ?string externalID, ?array<string,string> metadata, ?string name, ?[Relationship](api/beta/user_profiles/update.md) relationship, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta/user_profiles.md)

POST/v1/user\_profiles/{user\_profile\_id}

##### [Create Enrollment URL](api/beta/user_profiles/create_enrollment_url.md)

$client->beta->userProfiles->createEnrollmentURL(string userProfileID, ?list<AnthropicBeta> betas): [BetaUserProfileEnrollmentURL](api/beta/user_profiles.md)

POST/v1/user\_profiles/{user\_profile\_id}/enrollment\_url

##### ModelsExpand Collapse



[BetaUserProfile](api/beta/user_profiles.md)

string id

Unique identifier for this user profile, prefixed `uprof_`.

\Datetime createdAt

A timestamp in RFC 3339 format

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

Relationship relationship

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

array<string,[BetaUserProfileTrustGrant](api/beta/user_profiles.md)> trustGrants

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

Type type

Object type. Always `user_profile`.

\Datetime updatedAt

A timestamp in RFC 3339 format

?string externalID

Platform's own identifier for this user. Not enforced unique.

?string name

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.



[BetaUserProfileEnrollmentURL](api/beta/user_profiles.md)

\Datetime expiresAt

A timestamp in RFC 3339 format

Type type

Object type. Always `enrollment_url`.

string url

Enrollment URL to send to the end user. Valid until `expires_at`.



[BetaUserProfileTrustGrant](api/beta/user_profiles.md)

Status status

Status of the trust grant.

---

*Copyright © Anthropic. All rights reserved.*
