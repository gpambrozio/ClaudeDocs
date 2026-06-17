# Get Compliance Group

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Get Compliance Group

GET/v1/compliance/groups/{group\_id}

Get Compliance Group

##### Path ParametersExpand Collapse

group\_id: string

The group ID (tagged ID, e.g., rbac\_group\_abc123)

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

id: string

Group identifier (tagged ID)

created\_at: string

Group creation timestamp (ISO 8601)

description: string

Group description

name: string

Group name

roles: array of string

Role IDs assigned to this group.

source\_type: string

How the group was created ('direct' or 'scim')

updated\_at: string

Group last-updated timestamp (ISO 8601)

Get Compliance Group



```shiki
curl https://api.anthropic.com/v1/compliance/groups/$GROUP_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "roles": [
    "string"
  ],
  "source_type": "source_type",
  "updated_at": "updated_at"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "roles": [
    "string"
  ],
  "source_type": "source_type",
  "updated_at": "updated_at"
}
```

---

*Copyright © Anthropic. All rights reserved.*
