# List User Profiles

Copy page

SDK language

PHP

# List User Profiles

$client->beta->userProfiles->list(?int limit, ?[Order](api/beta/user_profiles/list.md) order, ?string page, ?list<AnthropicBeta> betas): PageCursor<[BetaUserProfile](api/beta.md)>

GET/v1/user\_profiles

List User Profiles

##### ParametersExpand Collapse

limit?:optional int

Query parameter for limit

order?:optional [Order](api/beta/user_profiles/list.md)

Query parameter for order

page?:optional string

Query parameter for page

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

[BetaUserProfile](api/beta.md)

string id

Unique identifier for this user profile, prefixed `uprof_`.

\Datetime createdAt

A timestamp in RFC 3339 format

array<string,string> metadata

Arbitrary key-value metadata. Maximum 16 pairs, keys up to 64 chars, values up to 512 chars.

Relationship relationship

How the entity behind a user profile relates to the platform that owns the API key. `external`: an individual end-user of the platform. `resold`: a company the platform resells Claude access to. `internal`: the platform's own usage.

array<string,[BetaUserProfileTrustGrant](api/beta.md)> trustGrants

Trust grants for this profile, keyed by grant name. Key omitted when no grant is active or in flight.

Type type

Object type. Always `user_profile`.

\Datetime updatedAt

A timestamp in RFC 3339 format

?string externalID

Platform's own identifier for this user. Not enforced unique.

?string name

Display name of the entity this profile represents. For `resold` this is the resold-to company's name.

List User Profiles

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->userProfiles->list(
  limit: 0, order: 'asc', page: 'page', betas: ['message-batches-2024-09-24']
);

var_dump($page);
```

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200

```shiki
{
  "data": [
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
  ],
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
