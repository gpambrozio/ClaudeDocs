# Delete Skill Version

Copy page



cURL

# Delete Skill Version

DELETE/v1/skills/{skill\_id}/versions/{version}

Delete Skill Version

##### Path ParametersExpand Collapse



skill\_id: string

Unique identifier for the skill.

The format and length of IDs may change over time.



version: string

Identifies the skill version: a version ID, or — where the endpoint accepts it — the literal `latest` for the skill's most recent version.

Requests carrying the `skills-2025-10-02` beta header address versions by their Unix epoch timestamp instead (e.g., "1759178010641129").

##### ReturnsExpand Collapse



DeletedSkillVersion object { id, type } 

id: string

Unique identifier for this Skill Version. The id addresses the version in
paths and pins it in references.



type: "skill\_version\_deleted"

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

Delete Skill Version

cURL

```shiki
curl https://api.anthropic.com/v1/skills/$SKILL_ID/versions/$VERSION \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "id": "id",
  "type": "skill_version_deleted"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "type": "skill_version_deleted"
}
```

---

*Copyright © Anthropic. All rights reserved.*
