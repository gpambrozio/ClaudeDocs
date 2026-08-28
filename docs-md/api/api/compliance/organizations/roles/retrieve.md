# Get Compliance Role

Copy page



# Get Compliance Role

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

Get Compliance Role

##### Path parameters

org\_uuid: string

The organization UUID

role\_id: string

The role ID (tagged ID, e.g., rbac\_role\_abc123)

##### Headers

"x-api-key": optional string

##### Returns

id: string

Role identifier (tagged ID)

created\_at: string or null

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string or null

Role last-updated timestamp (ISO 8601)



### Get Compliance Role

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789"
}
```

##### Returns Examples

Response 200



```shiki
{
  "id": "rbac_role_01SGBg3kEnZrdsVR2QmyJbvD",
  "created_at": "2025-03-12T18:22:41.123456",
  "description": "Full administrative access to organization settings and members",
  "name": "Organization Admin",
  "updated_at": "2025-03-14T09:05:17.456789"
}
```

---

*Copyright © Anthropic. All rights reserved.*
