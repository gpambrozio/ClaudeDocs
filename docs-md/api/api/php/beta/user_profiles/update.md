# Update User Profile

Copy page



PHP

# Update User Profile

$client->beta->userProfiles->update(string userProfileID, ?string externalID, ?array<string,string> metadata, ?string name, ?[Relationship](api/beta/user_profiles/update.md) relationship, ?list<AnthropicBeta> betas): [BetaUserProfile](api/beta.md)

POST/v1/user\_profiles/{user\_profile\_id}

Update User Profile

##### ParametersExpand Collapse

userProfileID: string

externalID?:optional string

If present, replaces the stored external\_id. Omit to leave unchanged. Maximum 255 characters.

metadata?:optional array<string,string>

Key-value pairs to merge into the stored metadata. Keys provided overwrite existing values. To remove a key, set its value to an empty string. Keys not provided are left unchanged. Maximum 16 keys, with keys up to 64 characters and values up to 512 characters.

name?:optional string

If present, replaces the stored name. Omit to leave unchanged. Maximum 255 characters.

relationship?:optional [Relationship](api/beta/user_profiles/update.md)

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[BetaUserProfile](api/beta.md)

string id

Unique identifier for this user profile, prefixed `uprof_`.

\Datetime createdAt

A timestamp in RFC 3339 format

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

Relationship relationship

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

array<string,[BetaUserProfileTrustGrant](api/beta.md)> trustGrants

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

Type type

Object type. Always `user_profile`.

\Datetime updatedAt

A timestamp in RFC 3339 format

?string externalID

Platform's own identifier for this user. Not enforced unique.

?string name

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

Update User Profile

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$betaUserProfile = $client->beta->userProfiles->update(
  'uprof_011CZkZCu8hGbp5mYRQgUmz9',
  externalID: 'user_12345',
  metadata: ['foo' => 'string'],
  name: 'x',
  relationship: 'external',
  betas: ['message-batches-2024-09-24'],
);

var_dump($betaUserProfile);
```

Response 200



```shiki
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "uprof_011CZkZCu8hGbp5mYRQgUmz9",
  "created_at": "2026-03-15T10:00:00Z",
  "metadata": {},
  "relationship": "external",
  "trust_grants": {
    "cyber": {
      "status": "active"
    }
  },
  "type": "user_profile",
  "updated_at": "2026-03-15T10:00:00Z",
  "external_id": "user_12345",
  "name": "Example User"
}
```

---

*Copyright © Anthropic. All rights reserved.*
