# Versions

Copy page



cURL

# Versions

##### [Create Skill Version](api/http/beta/skills/versions/create.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/http/beta/skills/versions/list.md)

GET/v1/skills/{skill\_id}/versions

##### [Download Skill Version Content](api/http/beta/skills/versions/download.md)

GET/v1/skills/{skill\_id}/versions/{version}/content

##### [Get Skill Version](api/http/beta/skills/versions/retrieve.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/http/beta/skills/versions/delete.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

##### Models



BetaDeletedSkillVersion object{ id, type }

id: string

Unique identifier for this Skill Version. The id addresses the version in
paths and pins it in references.



type: "skill\_version\_deleted"

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

defaultskill\_version\_deleted



BetaSkillVersion object{ id, created\_at, description, 3 more }

id: string

Unique identifier for this Skill Version. The id addresses the version in
paths and pins it in references.



created\_at: string

ISO 8601 timestamp of when the skill was created.

formatdate-time

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

defaultskill\_version

---

*Copyright © Anthropic. All rights reserved.*
