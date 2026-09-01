# Federation Rules

Copy page



# Federation Rules

##### [Create Federation Rule](api/http/admin/federation_rules/create.md)

POST/v1/organizations/federation\_rules

##### [Get Federation Rule](api/http/admin/federation_rules/retrieve.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [List Federation Rules](api/http/admin/federation_rules/list.md)

GET/v1/organizations/federation\_rules

##### [Update Federation Rule](api/http/admin/federation_rules/update.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [Archive Federation Rule](api/http/admin/federation_rules/archive.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/archive

##### Models



FederationRule object{ id, applies\_to\_all\_workspaces, archived\_at, 17 more }

Authorization rule binding an external OIDC identity to Anthropic.

Evaluates the match conditions and mints an OAuth access token for the
resolved target, scoped to a single workspace where the rule is enabled
(chosen by the caller at exchange time when the rule is enabled for more
than one). For rules enabled via `workspace_ids` or
`applies_to_all_workspaces`, the target service account must be a member
of that workspace (it is implicitly a member of the default workspace);
rules carrying only the legacy `workspace_id` binding do not enforce
this.

#### Federation Rules[Workspaces](api/http/admin/federation_rules/workspaces.md)

##### [List Federation Rule Workspaces](api/http/admin/federation_rules/workspaces/list.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Add Federation Rule Workspace](api/http/admin/federation_rules/workspaces/create.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Remove Federation Rule Workspace](api/http/admin/federation_rules/workspaces/delete.md)

DELETE/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces/{workspace\_id}

---

*Copyright © Anthropic. All rights reserved.*
