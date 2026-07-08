# Organizations

Copy page





To enable the Compliance API, see [Set up the Compliance API](manage-claude/compliance-api-access.md).

# Organizations

##### [List organizations](api/compliance/organizations/list.md)

GET/v1/compliance/organizations

##### ModelsExpand Collapse



OrganizationListResponse object { created\_at, name, uuid } 

Information about an organization.

created\_at: string

Organization creation time (RFC 3339 format)

name: string

Organization name

uuid: string

Unique identifier for the organization (UUID format)

#### OrganizationsUsers

##### [List organization users](api/compliance/organizations/users/list.md)

GET/v1/compliance/organizations/{org\_uuid}/users

#### OrganizationsRoles

##### [List Compliance Roles](api/compliance/organizations/roles/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles

##### [Get Compliance Role](api/compliance/organizations/roles/retrieve.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

#### OrganizationsRolesPermissions

##### [List Compliance Role Permissions](api/compliance/organizations/roles/permissions/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

#### OrganizationsSettings

##### [Get effective organization settings](api/compliance/organizations/settings/retrieve.md)

GET/v1/compliance/organizations/{organization\_id}/settings

---

*Copyright © Anthropic. All rights reserved.*
