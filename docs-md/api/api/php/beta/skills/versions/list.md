# List Skill Versions

Copy page



PHP

# List Skill Versions

$client->beta->skills->versions->list(string skillID, ?int limit, ?string page, ?list<AnthropicBeta> betas): PageCursor<[VersionListResponse](api/beta.md)>

GET/v1/skills/{skill\_id}/versions

List Skill Versions

##### ParametersExpand Collapse



skillID: string

Unique identifier for the skill.

The format and length of IDs may change over time.



limit?:optional int

Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

page?:optional string

Optionally set to the `next_page` token from the previous response.

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[VersionListResponse](api/beta.md)



string id

Unique identifier for the skill version.

The format and length of IDs may change over time.

string createdAt

ISO 8601 timestamp of when the skill version was created.



string description

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



string directory

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



string name

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

string skillID

Identifier for the skill that this version belongs to.



string type

Object type.

For Skill Versions, this is always `"skill_version"`.



string version

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

List Skill Versions

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->skills->versions->list(
  'skill_id', limit: 0, page: 'page', betas: ['message-batches-2024-09-24']
);

var_dump($page);
```

Response 200



```shiki
{
  "data": [
    {
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "skillver_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "A custom skill for doing something useful",
      "directory": "my-skill",
      "name": "my-skill",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "type",
      "version": "1759178010641129"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
