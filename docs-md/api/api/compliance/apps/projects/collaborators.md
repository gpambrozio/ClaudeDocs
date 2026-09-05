# Collaborators

To enable the Compliance API, see the setup guide.

[Set up the Compliance API](manage-claude/compliance-api-access.md)

Copy page



# Collaborators

##### [List project collaborators](api/http/compliance/apps/projects/collaborators/list.md)

GET/v1/compliance/apps/projects/{project\_id}/collaborators

##### Models



CollaboratorListResponse = object{ granted\_at, role, type, user\_id } or object{ granted\_at, group\_id, role, type } or object{ granted\_at, organization\_uuid, role, type } or object{ granted\_at, organization\_role, role, type }

An individual user granted a role on a project.

One of the following:

---

*Copyright © Anthropic. All rights reserved.*
