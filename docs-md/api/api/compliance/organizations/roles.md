# Roles

Copy page



# Roles

##### [List Compliance Roles](api/http/compliance/organizations/roles/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles

##### [Get Compliance Role](api/http/compliance/organizations/roles/retrieve.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

##### Models



RoleListResponse object{ id, created\_at, description, 2 more }

Role information for compliance responses.

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



RoleRetrieveResponse object{ id, created\_at, description, 2 more }

Role information for compliance responses.

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

#### Roles[Permissions](api/http/compliance/organizations/roles/permissions.md)

##### [List Compliance Role Permissions](api/http/compliance/organizations/roles/permissions/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

---

*Copyright © Anthropic. All rights reserved.*
