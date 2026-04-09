# Get Skill

Copy page

CLI

# Get Skill

$ ant beta:skills retrieve

GET/v1/skills/{skill\_id}

Get Skill

##### ParametersExpand Collapse

--skill-id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaSkillGetResponse: object { id, created\_at, display\_title, 4 more }

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

Get Skill

CLI

```shiki
ant beta:skills retrieve \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
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
