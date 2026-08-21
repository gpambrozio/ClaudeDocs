# Skills

Copy page



cURL

# Skills

##### [Create Skill](api/skills/create.md)

POST/v1/skills

##### [List Skills](api/skills/list.md)

GET/v1/skills

##### [Get Skill](api/skills/retrieve.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/skills/delete.md)

DELETE/v1/skills/{skill\_id}

##### ModelsExpand Collapse



DeletedSkill object { id, type } 



id: string

Unique identifier for the skill.

The format and length of IDs may change over time.



type: "skill\_deleted"

Deleted object type.

For Skills, this is always `"skill_deleted"`.



Skill object { id, created\_at, display\_name, 4 more } 



id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: string

ISO 8601 timestamp of when the skill was created.

display\_name: string

Human-readable, single-line label for the Skill. Maximum 255 characters.
Always set: derived from the SKILL.md frontmatter `name` when omitted at
creation. Not unique.

latest\_version\_id: string

ID of the newest Skill Version — what `latest` references resolve to. Always set: a Skill holds at least one version.



source: [SkillSource](api/skills.md) { type } 

Where the Skill comes from.

Possible values:

- `"custom"`: authored by the platform user; private to their workspace
- `"anthropic"`: published by Anthropic; shared and read-only
- `"anthropic_example"`: Anthropic-published sample Skill
- `"plugin"`: resolved from an installed plugin



type: "custom" or "anthropic" or "anthropic\_example" or "plugin"

Where the Skill comes from.

Possible values:

- `"custom"`: authored by the platform user; private to their workspace
- `"anthropic"`: published by Anthropic; shared and read-only
- `"anthropic_example"`: Anthropic-published sample Skill
- `"plugin"`: resolved from an installed plugin

One of the following:

"custom"

"anthropic"

"anthropic\_example"

"plugin"



type: "skill"

Object type.

For Skills, this is always `"skill"`.

updated\_at: string

ISO 8601 timestamp of when the skill was last updated.



SkillSource object { type } 



type: "custom" or "anthropic" or "anthropic\_example" or "plugin"

Where the Skill comes from.

Possible values:

- `"custom"`: authored by the platform user; private to their workspace
- `"anthropic"`: published by Anthropic; shared and read-only
- `"anthropic_example"`: Anthropic-published sample Skill
- `"plugin"`: resolved from an installed plugin

One of the following:

"custom"

"anthropic"

"anthropic\_example"

"plugin"

#### SkillsVersions

##### [Create Skill Version](api/skills/versions/create.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/skills/versions/list.md)

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/skills/versions/retrieve.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/skills/versions/delete.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
