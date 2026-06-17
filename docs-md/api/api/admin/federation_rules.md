# Federation Rules

Copy page



# Federation Rules

##### [Create Federation Rule](api/admin/federation_rules/create.md)

POST/v1/organizations/federation\_rules

##### [Get Federation Rule](api/admin/federation_rules/retrieve.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [List Federation Rules](api/admin/federation_rules/list.md)

GET/v1/organizations/federation\_rules

##### [Update Federation Rule](api/admin/federation_rules/update.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [Archive Federation Rule](api/admin/federation_rules/archive.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/archive

##### ModelsExpand Collapse



FederationRule object { id, applies\_to\_all\_workspaces, archived\_at, 17 more } 

Authorization rule binding an external OIDC identity to Anthropic.

Evaluates the match conditions and mints an OAuth access token for the
resolved target, scoped to a single workspace where the rule is enabled
(chosen by the caller at exchange time when the rule is enabled for more
than one). For rules enabled via `workspace_ids` or
`applies_to_all_workspaces`, the target service account must be a member
of that workspace (it is implicitly a member of the default workspace);
rules carrying only the legacy `workspace_id` binding do not enforce
this.

id: string

Tagged ID of the federation rule.

applies\_to\_all\_workspaces: boolean

When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.

archived\_at: string

If set, this rule is archived and rejects token exchange.

archived\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

attributes: map[string]

CEL expressions extracting named values from claims. Not yet supported; always null.

created\_at: string

When this rule was created.

created\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that created this rule.

description: string

Optional free-text description.

issuer\_id: string

Tagged ID of the issuer whose tokens this rule accepts.

issuer\_name: string

Issuer's display name at read time.



match: object { audience, claims, condition, subject\_prefix } 

Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.

audience: optional string

Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

claims: optional map[string]

Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.

condition: optional string

CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

subject\_prefix: optional string

Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

name: string

Admin-chosen slug identifier.

oauth\_scope: string

Space-separated OAuth scopes granted on the minted token.



target: object { service\_account\_id, type, service\_account\_name } 

Identity that tokens minted via this rule act as. Currently always a `service_account` target.

service\_account\_id: string

Tagged ID of the service account to mint tokens for.

type: "service\_account"

service\_account\_name: optional string

Service account's display name at read time. Ignored on writes.

token\_lifetime\_seconds: number

Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.

type: "federation\_rule"

updated\_at: string

When this rule was last updated.

updated\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

workspace\_id: string

Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

workspace\_ids: array of string

Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

#### Federation RulesWorkspaces

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
