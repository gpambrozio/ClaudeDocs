# Workspaces

Copy page



# Workspaces

##### [List Federation Rule Workspaces](api/admin/federation_rules/workspaces/list.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Add Federation Rule Workspace](api/admin/federation_rules/workspaces/create.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Remove Federation Rule Workspace](api/admin/federation_rules/workspaces/delete.md)

DELETE/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces/{workspace\_id}

##### ModelsExpand Collapse



WorkspaceListResponse object { created\_at, created\_by\_actor\_id, federation\_rule\_id, 3 more } 

created\_at: string

When this workspace was enabled for the rule.

created\_by\_actor\_id: string

Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

federation\_rule\_id: string

Tagged ID of the federation rule.

type: "federation\_rule\_workspace"

workspace\_id: string

Tagged ID of the workspace this rule is enabled for.

workspace\_name: string

Workspace display name. Populated when listing; null in the enable response.



WorkspaceCreateResponse object { created\_at, created\_by\_actor\_id, federation\_rule\_id, 3 more } 

created\_at: string

When this workspace was enabled for the rule.

created\_by\_actor\_id: string

Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

federation\_rule\_id: string

Tagged ID of the federation rule.

type: "federation\_rule\_workspace"

workspace\_id: string

Tagged ID of the workspace this rule is enabled for.

workspace\_name: string

Workspace display name. Populated when listing; null in the enable response.



WorkspaceDeleteResponse object { federation\_rule\_id, type, workspace\_id } 

federation\_rule\_id: string

Tagged ID of the federation rule.

type: "federation\_rule\_workspace\_deleted"

workspace\_id: string

Tagged ID of the workspace named in the delete request. Removal is idempotent.

---

*Copyright © Anthropic. All rights reserved.*
