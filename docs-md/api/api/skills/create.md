# Create Skill

Copy page



cURL

# Create Skill

POST/v1/skills

Create Skill

##### Body (form-data)



files: array of string

Files to upload for the skill.

All files must be in the same top-level directory and must include a SKILL.md file at the root of that directory.

display\_name: optional string or null

Human-readable, single-line label for the Skill. Maximum 255 characters.
Always set: derived from the SKILL.md frontmatter `name` when omitted at
creation. Not unique.

##### Returns



Skill object{ id, created\_at, display\_name, 4 more }



### Create Skill

cURL



```shiki
curl https://api.anthropic.com/v1/skills \
    -H 'Content-Type: multipart/form-data' \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY" \
    -F files='["Example data"]'
```

Response 200



```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "latest_version_id": "latest_version_id",
  "source": {
    "type": "custom"
  },
  "type": "skill",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "skill_01JAbcdefghijklmnopqrstuvw",
  "created_at": "2024-10-30T23:58:27.427722Z",
  "display_name": "display_name",
  "latest_version_id": "latest_version_id",
  "source": {
    "type": "custom"
  },
  "type": "skill",
  "updated_at": "2024-10-30T23:58:27.427722Z"
}
```

---

*Copyright © Anthropic. All rights reserved.*
