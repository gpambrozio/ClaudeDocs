# List Skills

Copy page



PHP

# List Skills

$client->beta->skills->list(?int limit, ?string page, ?string source, ?list<AnthropicBeta> betas): PageCursor<[SkillListResponse](api/beta/skills.md)>

GET/v1/skills

List Skills

##### ParametersExpand Collapse



limit?:optional int

Number of results to return per page.

Maximum value is 100. Defaults to 20.



page?:optional string

Pagination token for fetching a specific page of results.

Pass the value from a previous response's `next_page` field to get the next page of results.



source?:optional string

Filter skills by source.

If provided, only skills from the specified source will be returned:

- `"custom"`: only return user-created skills
- `"anthropic"`: only return Anthropic-created skills

betas?:optional list<AnthropicBeta>

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



[SkillListResponse](api/beta/skills.md)



string id

Unique identifier for the skill.

The format and length of IDs may change over time.

string createdAt

ISO 8601 timestamp of when the skill was created.



?string displayTitle

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.



?string latestVersion

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.



string source

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic



string type

Object type.

For Skills, this is always `"skill"`.

string updatedAt

ISO 8601 timestamp of when the skill was last updated.

List Skills

PHP

```shiki
<?php

require_once dirname(__DIR__) . '/vendor/autoload.php';

$client = new Client(apiKey: 'my-anthropic-api-key');

$page = $client->beta->skills->list(
  limit: 0,
  page: 'page',
  source: 'source',
  betas: ['message-batches-2024-09-24'],
);

var_dump($page);
```

Response 200



```shiki
{
  "data": [
    {
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
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
      "id": "skill_01JAbcdefghijklmnopqrstuvw",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "display_title": "My Custom Skill",
      "latest_version": "1759178010641129",
      "source": "custom",
      "type": "type",
      "updated_at": "2024-10-30T23:58:27.427722Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
