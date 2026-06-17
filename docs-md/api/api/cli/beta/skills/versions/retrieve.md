# Get Skill Version

Copy page



CLI

# Get Skill Version

$ ant beta:skills:versions retrieve

GET/v1/skills/{skill\_id}/versions/{version}

Get Skill Version

##### ParametersExpand Collapse



--skill-id: string

Path param: Unique identifier for the skill.

The format and length of IDs may change over time.



--version: string

Path param: Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse



BetaSkillVersionGetResponse: object { id, created\_at, description, 5 more } 

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

Get Skill Version

CLI

```shiki
ant beta:skills:versions retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
