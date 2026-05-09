# Get Compliance Role

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Get Compliance Role

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

Get Compliance Role

##### Path ParametersExpand Collapse

org\_uuid: string

The organization UUID

role\_id: string

The role ID (tagged ID, e.g., rbac\_role\_abc123)

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

id: string

Role identifier (tagged ID)

created\_at: string

Role creation timestamp (ISO 8601)

description: string

Role description

name: string

Role name

updated\_at: string

Role last-updated timestamp (ISO 8601)

Get Compliance Role

```shiki
curl https://api.anthropic.com/v1/compliance/organizations/$ORG_UUID/roles/$ROLE_ID \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```shiki
{
  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "updated_at": "updated_at"
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "id",
  "created_at": "created_at",
  "description": "description",
  "name": "name",
  "updated_at": "updated_at"
}
```

---

*Copyright © Anthropic. All rights reserved.*
