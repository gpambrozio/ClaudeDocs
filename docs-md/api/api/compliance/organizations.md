# Organizations

Copy page



# Organizations

##### [List organizations](api/http/compliance/organizations/list.md)

GET/v1/compliance/organizations

##### Models



OrganizationListResponse object{ created\_at, name, uuid }

Information about an organization.

created\_at: string

Organization creation time (RFC 3339 format)

name: string

Organization name

uuid: string

Unique identifier for the organization (UUID format)

#### Organizations[Users](api/http/compliance/organizations/users.md)

##### [List organization users](api/http/compliance/organizations/users/list.md)

GET/v1/compliance/organizations/{org\_uuid}/users

#### Organizations[Roles](api/http/compliance/organizations/roles.md)

##### [List Compliance Roles](api/http/compliance/organizations/roles/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles

##### [Get Compliance Role](api/http/compliance/organizations/roles/retrieve.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}

#### OrganizationsRoles[Permissions](api/http/compliance/organizations/roles/permissions.md)

##### [List Compliance Role Permissions](api/http/compliance/organizations/roles/permissions/list.md)

GET/v1/compliance/organizations/{org\_uuid}/roles/{role\_id}/permissions

#### Organizations[Settings](api/http/compliance/organizations/settings.md)

##### [Get effective organization settings](api/http/compliance/organizations/settings/retrieve.md)

GET/v1/compliance/organizations/{organization\_id}/settings

---

*Copyright © Anthropic. All rights reserved.*
