# Delete Skill

Copy page



cURL

# Delete Skill

DELETE/v1/skills/{skill\_id}

Delete Skill

##### Path parameters



skill\_id: string

Unique identifier for the skill.

The format and length of IDs may change over time.

##### Returns

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

### Delete Skill

cURL



```shiki
curl https://api.anthropic.com/v1/skills/$SKILL_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "type": "skill_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
