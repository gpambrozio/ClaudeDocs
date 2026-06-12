# List Skill Versions

Copy page

SDK language

CLI

# List Skill Versions

$ ant beta:skills:versions list

GET/v1/skills/{skill\_id}/versions

List Skill Versions

##### ParametersExpand Collapse



--skill-id: string

Path param: Unique identifier for the skill.

The format and length of IDs may change over time.



--limit: optional number

Query param: Number of items to return per page.

Defaults to `20`. Ranges from `1` to `1000`.

--page: optional string

Query param: Optionally set to the `next_page` token from the previous response.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



BetaListSkillVersionsResponse: object { data, has\_more, next\_page } 



data: array of object { id, created\_at, description, 5 more } 

List of skill versions.



id: string

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill version was created.



description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.



directory: string

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.



name: string

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: string

Identifier for the skill that this version belongs to.



type: string

Object type.

For Skill Versions, this is always `"skill_version"`.



version: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

has\_more: boolean

Indicates if there are more results in the requested page direction.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

List Skill Versions

CLI

```shiki
ant beta:skills:versions list \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
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
