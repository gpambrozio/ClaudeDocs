# Get Compliance Group

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

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
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2025-03-12T18:22:41.123456",
  "description": "All members of the engineering organization",
  "name": "Engineering Team",
  "roles": [
    "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
    "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
  ],
  "source_type": "scim",
  "updated_at": "2025-03-14T09:05:17.456789"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
  "created_at": "2025-03-12T18:22:41.123456",
  "description": "All members of the engineering organization",
  "name": "Engineering Team",
  "roles": [
    "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
    "rbac_role_01HtCd4mFoAseWS3RnzKcwE7"
  ],
  "source_type": "scim",
  "updated_at": "2025-03-14T09:05:17.456789"
}
```

---

*Copyright © Anthropic. All rights reserved.*
