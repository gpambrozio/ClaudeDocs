# List Federation Rule Workspaces

Copy page



# List Federation Rule Workspaces

GET/v1/organizations/federation\_rules/{federation\_rule\_id}/workspaces

List workspaces where this federation rule is enabled.

Returns all workspace enablements in a single response; the `limit` and
`page` parameters are accepted but have no effect, and `next_page` is
always `null`. Returns explicit per-workspace enablements only; for
rules with `applies_to_all_workspaces` or a legacy single
`workspace_id`, check those fields on the rule itself.

##### Path ParametersExpand Collapse

federation\_rule\_id: string

ID of the federation rule.

##### Query ParametersExpand Collapse

limit: optional number

Number of results per page.

page: optional string

Opaque cursor from a previous response's `next_page`.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### ReturnsExpand Collapse



data: array of object { created\_at, created\_by\_actor\_id, federation\_rule\_id, 3 more } 

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

next\_page: string

Opaque cursor for the next page; null when there are no more results.

List Federation Rule Workspaces



```shiki
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/workspaces \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
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
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "federation_rule_id": "federation_rule_id",
      "type": "federation_rule_workspace",
      "workspace_id": "workspace_id",
      "workspace_name": "workspace_name"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
