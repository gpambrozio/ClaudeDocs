# List Skills

Copy page

CLI

# List Skills

$ ant beta:skills list

GET/v1/skills

List Skills

##### ParametersExpand Collapse

--limit: optional number

Query param: Number of results to return per page.

Maximum value is 100. Defaults to 20.

--page: optional string

Query param: Pagination token for fetching a specific page of results.

Pass the value from a previous response's `next_page` field to get the next page of results.

--source: optional string

Query param: Filter skills by source.

If provided, only skills from the specified source will be returned:

- `"custom"`: only return user-created skills
- `"anthropic"`: only return Anthropic-created skills

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaListSkillsResponse: object { data, has\_more, next\_page }

data: array of object { id, created\_at, display\_title, 4 more }

List of skills.

id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.

display\_title: string

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest\_version: string

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: string

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: string

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.

has\_more: boolean

Whether there are more results available.

If `true`, there are additional results that can be fetched using the `next_page` token.

next\_page: string

Token for fetching the next page of results.

If `null`, there are no more results available. Pass this value to the `page_token` parameter in the next request to get the next page.

List Skills

CLI

```shiki
ant beta:skills list \
  --api-key my-anthropic-api-key
```

Response 200

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
