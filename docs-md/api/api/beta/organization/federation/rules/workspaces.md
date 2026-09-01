# Workspaces

Copy page



cURL

# Workspaces

##### [Add Federation Rule Workspace](api/http/beta/organization/federation/rules/workspaces/add.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [List Federation Rule Workspaces](api/http/beta/organization/federation/rules/workspaces/list.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Remove Federation Rule Workspace](api/http/beta/organization/federation/rules/workspaces/remove.md)

DELETE/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces/{workspace\_id}

##### Models



WorkspaceRemoveResponse object{ federation\_rule\_id, type, workspace\_id }

federation\_rule\_id: string

Tagged ID of the federation rule.



type: "federation\_rule\_workspace\_deleted"

defaultfederation\_rule\_workspace\_deleted

workspace\_id: string

Tagged ID of the workspace named in the delete request. Removal is idempotent.

---

*Copyright © Anthropic. All rights reserved.*
