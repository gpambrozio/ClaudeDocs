# Delete Skill Version

Copy page

CLI

# Delete Skill Version

$ ant beta:skills:versions delete

DELETE/v1/skills/{skill\_id}/versions/{version}

Delete Skill Version

##### ParametersExpand Collapse

--skill-id: string

Path param: Unique identifier for the skill.

The format and length of IDs may change over time.

--version: string

Path param: Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

--beta: optional array of [AnthropicBeta](api/beta.md)

Header param: Optional header to specify the beta version(s) you want to use.

##### ReturnsExpand Collapse

BetaSkillVersionDeleteResponse: object { id, type }

id: string

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

type: string

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

Delete Skill Version

CLI

```shiki
ant beta:skills:versions delete \
  --api-key my-anthropic-api-key \
  --skill-id skill_id \
  --version version
```

Response 200

```shiki
{
  "id": "1759178010641129",
  "type": "type"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "1759178010641129",
  "type": "type"
}
```

---

*Copyright © Anthropic. All rights reserved.*
