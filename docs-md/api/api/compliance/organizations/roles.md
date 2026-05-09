# Roles

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Roles

##### [List Compliance Roles](api/compliance/organizations/roles/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles

##### [Get Compliance Role](api/compliance/organizations/roles/retrieve.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

##### ModelsExpand Collapse

RoleListResponse = object { id, created\_at, description, 2 more }

Role information for compliance responses.

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

RoleRetrieveResponse = object { id, created\_at, description, 2 more }

Role information for compliance responses.

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

#### RolesPermissions

##### [List Compliance Role Permissions](api/compliance/organizations/roles/permissions/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

##### ModelsExpand Collapse

PermissionListResponse = object { action, resource\_id, resource\_type }

Permission granted by a role.

action: string

Action permitted on the resource

resource\_id: string

Identifier of the resource the permission applies to

resource\_type: string

Type of resource the permission applies to

---

*Copyright © Anthropic. All rights reserved.*
