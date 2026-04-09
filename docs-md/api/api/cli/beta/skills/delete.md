# Delete Skill

Copy page

CLI

# Delete Skill

$ ant beta:skills delete

DELETE/v1/skills/{skill\_id}

Delete Skill

##### ParametersExpand Collapse

--skill-id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

--beta: optional array of [AnthropicBeta](api/beta.md)

Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaSkillDeleteResponse: object { id, type }

id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

type: string

Deleted object type.

For Skills, this is always `"skill_deleted"`.

Delete Skill

CLI

```shiki
ant beta:skills delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id
```

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "type"
}
```

---

*Copyright © Anthropic. All rights reserved.*
