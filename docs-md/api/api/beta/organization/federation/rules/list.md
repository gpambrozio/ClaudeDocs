# List Federation Rules

Copy page



cURL

# List Federation Rules

GET/v1/organizations/federation\_rules

**Requires an OAuth access token with the `org:admin` scope**, from `ant auth login --scope org:admin` or a workload identity federation rule; Admin API keys are not accepted. See [Manage WIF with the Admin API](manage-claude/wif-admin-api.md).

List federation rules in your organization.

Optionally filter by issuer with `issuer_id`. Archived rules are excluded
unless `include_archived=true`.

##### Query parameters



include\_archived: optional boolean

Include archived resources. Defaults to false.

defaultfalse

issuer\_id: optional string

Filter to rules referencing this federation issuer.



limit: optional number

Number of results per page.

default20

maximum100

minimum1

page: optional string

Opaque cursor from a previous response's `next_page`.

##### Headers



"anthropic-beta": optional array of [AnthropicBeta](api/http/beta.md)

Optional header to specify the beta version(s) you want to use.

One of the following:

string



"message-batches-2024-09-24" or "prompt-caching-2024-07-31" or "computer-use-2024-10-22" or 38 more

One of the following:

"message-batches-2024-09-24"

"prompt-caching-2024-07-31"

"computer-use-2024-10-22"

"computer-use-2025-01-24"

"pdfs-2024-09-25"

"token-counting-2024-11-01"

"token-efficient-tools-2025-02-19"

"output-128k-2025-02-19"

"files-api-2025-04-14"

"mcp-client-2025-04-04"

"mcp-client-2025-11-20"

"dev-full-thinking-2025-05-14"

"interleaved-thinking-2025-05-14"

"code-execution-2025-05-22"

"extended-cache-ttl-2025-04-11"

"context-1m-2025-08-07"

"context-management-2025-06-27"

"model-context-window-exceeded-2025-08-26"

"skills-2025-10-02"

"fast-mode-2026-02-01"

"output-300k-2026-03-24"

"user-profiles-2026-03-24"

"user-profiles-2026-08-18"

"advisor-tool-2026-03-01"

"managed-agents-2026-04-01"

"cache-diagnosis-2026-04-07"

"dreaming-2026-04-21"

"thinking-token-count-2026-05-13"

"server-side-fallback-2026-06-01"

"server-side-fallback-2026-07-01"

"fallback-credit-2026-06-01"

"fallback-credit-2026-07-01"

"agent-memory-2026-07-22"

"mid-conversation-tool-changes-2026-07-01"

"compact-2026-01-12"

"computer-use-2025-11-24"

"mcp-tunnels-2026-06-22"

"structured-outputs-2025-11-13"

"task-budgets-2026-03-13"

"thinking-display-updates-2026-08-18"

"ce-user-management-2026-07-13"

##### Returns



data: array of [BetaFederationRule](api/http/beta/organization/federation/rules.md) { id, applies\_to\_all\_workspaces, archived\_at, 17 more }

id: string

Tagged ID of the federation rule.

applies\_to\_all\_workspaces: boolean

When true, this rule is enabled for every workspace in the org (including ones created after the rule). `workspace_ids` is ignored at exchange time.



archived\_at: string or null

If set, this rule is archived and rejects token exchange.

formatdate-time

archived\_by\_actor\_id: string or null

Tagged ID (`user_`/`svac_`) of the actor that archived this rule.

attributes: map[string] or null

CEL expressions extracting named values from claims. Not yet supported; always null.



created\_at: string

When this rule was created.

formatdate-time

created\_by\_actor\_id: string or null

Tagged ID (`user_`/`svac_`) of the actor that created this rule.

description: string or null

Optional free-text description.

issuer\_id: string

Tagged ID of the issuer whose tokens this rule accepts.

issuer\_name: string or null

Issuer's display name at read time.



match: [BetaFederationRuleMatch](api/http/beta/organization/federation/rules.md) { audience, claims, condition, subject\_prefix }

Conditions the verified JWT must satisfy for this rule to apply. All populated matcher fields must pass.



audience: optional string or null

Exact match against the `aud` claim (any element if array). When omitted, the JWT's `aud` must still equal Anthropic's expected audience for the issuer; setting this field overrides that default.

maxLength1024

claims: optional map[string] or null

Exact-match `{claim: value}` pairs against top-level claims. Only string-valued claims can be matched; use `condition` for non-string claims.



condition: optional string or null

CEL expression over claims for logic the structural fields can't express. Must evaluate to a boolean and may reference only the `claims` variable; a constant-true expression (such as `true`) is rejected with 400.

maxLength4096



subject\_prefix: optional string or null

Match the verified JWT `sub` claim. Exact match unless the value ends with `*`, in which case it is a prefix match. Example: `repo:my-org/my-repo:ref:refs/heads/main`.

maxLength1024

name: string

Admin-chosen slug identifier.

oauth\_scope: string

Space-separated OAuth scopes granted on the minted token.



target: [BetaServiceAccountTarget](api/http/beta/organization/federation/rules.md) { service\_account\_id, type, service\_account\_name }

Identity that tokens minted via this rule act as. Currently always a `service_account` target.

service\_account\_id: string

Tagged ID of the service account to mint tokens for.

type: "service\_account"

service\_account\_name: optional string or null

Service account's display name at read time. Ignored on writes.

token\_lifetime\_seconds: number

Lifetime in seconds of access tokens minted via this rule. Minted tokens are capped at `max(60, min(this value, 2 × remaining assertion validity))` seconds.



type: "federation\_rule"

defaultfederation\_rule



updated\_at: string

When this rule was last updated.

formatdate-time

updated\_by\_actor\_id: string or null

Tagged ID (`user_`/`svac_`) of the actor that last updated this rule.

workspace\_id: string or null

Legacy single-workspace binding. Prefer `workspace_ids` and the `/federation_rules/{federation_rule_id}/workspaces` sub-resource for managing workspace enablement.

workspace\_ids: array of string

Tagged IDs of the workspaces this rule is enabled for. May be empty for older rules that only carry the legacy `workspace_id` binding. Ignored at exchange time when `applies_to_all_workspaces` is true (the list may still be non-empty).

next\_page: string or null

Opaque cursor for the next page, or null if no more results.

List Federation Rules

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/federation_rules \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
      "applies_to_all_workspaces": true,
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "attributes": {
        "foo": "string"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "issuer_id": "issuer_id",
      "issuer_name": "issuer_name",
      "match": {
        "audience": "audience",
        "claims": {
          "foo": "string"
        },
        "condition": "condition",
        "subject_prefix": "subject_prefix"
      },
      "name": "prod-deploy-pipeline",
      "oauth_scope": "oauth_scope",
      "target": {
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
        "service_account_name": "service_account_name"
      },
      "token_lifetime_seconds": 0,
      "type": "federation_rule",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id",
      "workspace_id": "workspace_id",
      "workspace_ids": [
        "string"
      ]
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
      "id": "fdrl_01SDCCSbTxrXDpWc1phhtcfK",
      "applies_to_all_workspaces": true,
      "archived_at": "2019-12-27T18:11:19.117Z",
      "archived_by_actor_id": "archived_by_actor_id",
      "attributes": {
        "foo": "string"
      },
      "created_at": "2024-10-30T23:58:27.427722Z",
      "created_by_actor_id": "created_by_actor_id",
      "description": "description",
      "issuer_id": "issuer_id",
      "issuer_name": "issuer_name",
      "match": {
        "audience": "audience",
        "claims": {
          "foo": "string"
        },
        "condition": "condition",
        "subject_prefix": "subject_prefix"
      },
      "name": "prod-deploy-pipeline",
      "oauth_scope": "oauth_scope",
      "target": {
        "service_account_id": "svac_01SDCCSbTxrXDpWc1phhtcfK",
        "type": "service_account",
        "service_account_name": "service_account_name"
      },
      "token_lifetime_seconds": 0,
      "type": "federation_rule",
      "updated_at": "2024-10-30T23:58:27.427722Z",
      "updated_by_actor_id": "updated_by_actor_id",
      "workspace_id": "workspace_id",
      "workspace_ids": [
        "string"
      ]
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
