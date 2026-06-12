# List project collaborators

Copy page



To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# List project collaborators

GET/v1/compliance/apps/projects/{project\_id}/collaborators

List the users, groups, and organization-wide grants on a project.

Each entry represents one active role assignment on the project. Principals
are returned as a discriminated union on `type` — an individual user, an
RBAC group, the whole organization, or all holders of an organization-level
role.

##### Path ParametersExpand Collapse

project\_id: string

The project ID (tagged ID, e.g., claude\_proj\_abc123)

##### Query ParametersExpand Collapse

limit: optional number

Maximum results (default: 20, max: 100)

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse



data: array of object { granted\_at, role, type, user\_id }  or object { granted\_at, group\_id, role, type }  or object { granted\_at, organization\_uuid, role, type }  or object { granted\_at, organization\_role, role, type } 

List of collaborators sorted chronologically by granted\_at, tie break by the underlying role-assignment UUID

One of the following:



ComplianceProjectUserCollaborator object { granted\_at, role, type, user\_id } 

An individual user granted a role on a project.

granted\_at: string

When this collaborator was granted access (RFC 3339 format)



role: "admin" or "editor" or "owner" or "viewer"

Role granted on the project

One of the following:

"admin"

"editor"

"owner"

"viewer"

type: "user"

Discriminator marking this as an individual user collaborator

user\_id: string

Identifier of the user granted access (tagged ID), or null if their account has since been deleted



ComplianceProjectGroupCollaborator object { granted\_at, group\_id, role, type } 

An RBAC group granted a role on a project.

granted\_at: string

When this collaborator was granted access (RFC 3339 format)

group\_id: string

Identifier of the group granted access (tagged ID)



role: "admin" or "editor" or "owner" or "viewer"

Role granted on the project

One of the following:

"admin"

"editor"

"owner"

"viewer"

type: "group"

Discriminator marking this as a group collaborator



ComplianceProjectOrganizationCollaborator object { granted\_at, organization\_uuid, role, type } 

An entire organization granted a role on a project.

granted\_at: string

When this collaborator was granted access (RFC 3339 format)

organization\_uuid: string

UUID of the organization granted access



role: "admin" or "editor" or "owner" or "viewer"

Role granted on the project

One of the following:

"admin"

"editor"

"owner"

"viewer"

type: "organization"

Discriminator marking this as an organization-wide grant



ComplianceProjectOrganizationRoleCollaborator object { granted\_at, organization\_role, role, type } 

All holders of an organization-level role granted a role on a project.

granted\_at: string

When this collaborator was granted access (RFC 3339 format)

organization\_role: string

The organization-level role whose holders are granted access



role: "admin" or "editor" or "owner" or "viewer"

Role granted on the project

One of the following:

"admin"

"editor"

"owner"

"viewer"

type: "organization\_role"

Discriminator marking this as a grant to all organization members holding a specific org-level role

has\_more: boolean

Whether more records exist beyond the current result set

next\_page: string

To get the next page, use the 'next\_page' from the current response as the 'page' in your next request

List project collaborators



```shiki
curl https://api.anthropic.com/v1/compliance/apps/projects/$PROJECT_ID/collaborators \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "granted_at": "2019-12-27T18:11:19.117Z",
      "role": "admin",
      "type": "user",
      "user_id": "user_id"
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
