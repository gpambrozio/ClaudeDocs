# Collaborators

Copy page



# Collaborators

##### [List project collaborators](api/compliance/apps/projects/collaborators/list.md)

GET/v1/compliance/apps/projects/{project\_id}/collaborators

##### ModelsExpand Collapse



CollaboratorListResponse = object { granted\_at, role, type, user\_id }  or object { granted\_at, group\_id, role, type }  or object { granted\_at, organization\_uuid, role, type }  or object { granted\_at, organization\_role, role, type } 

An individual user granted a role on a project.

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

---

*Copyright © Anthropic. All rights reserved.*
