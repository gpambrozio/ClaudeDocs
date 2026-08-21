# List Skill Versions

Copy page



cURL

# List Skill Versions

GET/v1/skills/{skill\_id}/versions

List Skill Versions

##### Path ParametersExpand Collapse



skill\_id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

##### Query ParametersExpand Collapse



limit: optional number

Number of results to return per page.

Ranges from `1` to `1000`. Defaults to `20`.

minimum1

maximum1000

page: optional string

Optionally set to the `next_page` token from the previous response.

##### ReturnsExpand Collapse



data: array of [SkillVersion](api/skills/versions.md) { id, created\_at, description, 3 more } 

List of skills.

id: string

Unique identifier for this Skill Version. The id addresses the version in
paths and pins it in references.

created\_at: string

ISO 8601 timestamp of when the skill was created.



description: string

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

name: string

The Skill's immutable kebab-case slug, set at creation from the first
upload's SKILL.md frontmatter `name` (or its enclosing directory). Every
later upload must resolve to the same value. Also the top-level directory
of the Skill's mounted files and the base name of a downloaded archive.



skill\_id: string

Unique identifier for the skill.

The format and length of IDs may change over time.



type: "skill\_version"

Object type.

For Skill Versions, this is always `"skill_version"`.



next\_page: string or null

Token for fetching the next page of results.

If `null`, there are no more results available. Pass this value to the `page` parameter in the next request to get the next page.

List Skill Versions

cURL

```shiki
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "description",
      "name": "name",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "skill_version"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "created_at": "2024-10-30T23:58:27.427722Z",
      "description": "description",
      "name": "name",
      "skill_id": "skill_01JAbcdefghijklmnopqrstuvw",
      "type": "skill_version"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
