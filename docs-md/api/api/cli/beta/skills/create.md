# Create Skill

Copy page

CLI

# Create Skill

$ ant beta:skills create

POST/v1/skills

Create Skill

##### ParametersExpand Collapse

--display-title: optional string

Body param: Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

--file: optional array of string

Body param: Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaSkillNewResponse: object { id, created\_at, display\_title, 4 more }

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

Create Skill

CLI

```shiki
ant beta:skills create \
  --api-key my-anthropic-api-key
```

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_title": "My Custom Skill",
  "latest_version": "1759178010641129",
  "source": "custom",
  "type": "type",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
