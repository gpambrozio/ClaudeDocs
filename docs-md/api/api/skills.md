# Skills

Copy page



cURL

# Skills

##### [Create Skill](api/http/skills/create.md)

POST/v1/skills

##### [List Skills](api/http/skills/list.md)

GET/v1/skills

##### [Get Skill](api/http/skills/retrieve.md)

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/http/skills/delete.md)

DELETE/v1/skills/{skill\_id}

##### Models



DeletedSkill object{ id, type }



id: string

Unique identifier for the skill.

The format and length of IDs may change over time.



type: "skill\_deleted"

Deleted object type.

For Skills, this is always `"skill_deleted"`.

defaultskill\_deleted



Skill object{ id, created\_at, display\_name, 4 more }



SkillSource object{ type }



type: "custom" or "anthropic" or "anthropic\_example" or "plugin"

Where the Skill comes from.

Possible values:

- `"custom"`: authored by the platform user; private to their workspace
- `"anthropic"`: published by Anthropic; shared and read-only
- `"anthropic_example"`: Anthropic-published sample Skill
- `"plugin"`: resolved from an installed plugin

One of the following:

"custom"

"anthropic"

"anthropic\_example"

"plugin"

#### Skills[Versions](api/http/skills/versions.md)

##### [Create Skill Version](api/http/skills/versions/create.md)

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/http/skills/versions/list.md)

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/http/skills/versions/retrieve.md)

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/http/skills/versions/delete.md)

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
