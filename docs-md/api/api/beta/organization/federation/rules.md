# Rules

Copy page



cURL

# Rules

##### [Create Federation Rule](api/http/beta/organization/federation/rules/create.md)

POST/v1/organizations/federation\_rules

##### [List Federation Rules](api/http/beta/organization/federation/rules/list.md)

GET/v1/organizations/federation\_rules

##### [Get Federation Rule](api/http/beta/organization/federation/rules/retrieve.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [Update Federation Rule](api/http/beta/organization/federation/rules/update.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}

##### [Archive Federation Rule](api/http/beta/organization/federation/rules/archive.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/archive

##### Models



BetaFederationRule object{ id, applies\_to\_all\_workspaces, archived\_at, 17 more }

Authorization rule binding an external OIDC identity to Anthropic.

Evaluates the match conditions and mints an OAuth access token for the
resolved target, scoped to a single workspace where the rule is enabled
(chosen by the caller at exchange time when the rule is enabled for more
than one). For rules enabled via `workspace_ids` or
`applies_to_all_workspaces`, the target service account must be a member
of that workspace (it is implicitly a member of the default workspace);
rules carrying only the legacy `workspace_id` binding do not enforce
this.



BetaFederationRuleMatch object{ audience, claims, condition, subject\_prefix }

Does the incoming JWT qualify?

All populated fields must pass; omitted fields are skipped. At least one
of `subject_prefix` (other than a wildcard-only value like `*`), `claims`,
or `condition` is required; `audience` alone is not sufficient.



audience: optional string or null

Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

maxLength1024

claims: optional map[string] or null

Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.



condition: optional string or null

CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

maxLength4096



subject\_prefix: optional string or null

Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

maxLength1024



BetaFederationRuleWorkspace object{ created\_at, created\_by\_actor\_id, federation\_rule\_id, 3 more }



created\_at: string

When this workspace was enabled for the rule.

formatdate-time

created\_by\_actor\_id: string or null

Tagged ID (`user_...` or `svac_...`) of the actor that enabled this workspace for the rule, if known.

federation\_rule\_id: string

Tagged ID of the federation rule.



type: "federation\_rule\_workspace"

defaultfederation\_rule\_workspace

workspace\_id: string

Tagged ID of the workspace this rule is enabled for.

workspace\_name: string or null

Workspace display name. Populated when listing; null in the enable response.



BetaServiceAccountTarget object{ service\_account\_id, type, service\_account\_name }

Bind to a fixed service account by ID.

service\_account\_id: string

Tagged ID of the service account to mint tokens for.

type: "service\_account"

service\_account\_name: optional string or null

Service account's display name at read time. Ignored on writes.

#### Rules[Workspaces](api/http/beta/organization/federation/rules/workspaces.md)

##### [Add Federation Rule Workspace](api/http/beta/organization/federation/rules/workspaces/add.md)

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [List Federation Rule Workspaces](api/http/beta/organization/federation/rules/workspaces/list.md)

GET/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

##### [Remove Federation Rule Workspace](api/http/beta/organization/federation/rules/workspaces/remove.md)

DELETE/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces/{workspace\_id}

---

*Copyright © Anthropic. All rights reserved.*
