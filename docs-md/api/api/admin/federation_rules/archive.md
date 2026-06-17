# Archive Federation Rule

Copy page



# Archive Federation Rule

POST/v1/organizations/federation\_rules/{federation\_rule\_id}/archive

Archive a federation rule.

Token exchange through this rule stops immediately. Idempotent;
re-archiving returns the rule with its original `archived_at`. Archiving
clears the rule's workspace targeting (`workspace_id` and
`workspace_ids` are emptied). Tokens already minted before archive
remain valid until they expire. OAuth callers may only manage rules
whose `oauth_scope` is `workspace:developer` or `workspace:inference`;
other scopes require a Console session. Admin API keys are not accepted.

##### Path ParametersExpand Collapse

federation\_rule\_id: string

ID of the federation rule to archive.

##### Header ParametersExpand Collapse



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### ReturnsExpand Collapse

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

Archive Federation Rule



```shiki
curl https://api.anthropic.com/v1/organizations/federation_rules/$FEDERATION_RULE_ID/archive \
    -X POST \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
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
```

##### Returns Examples

Response 200



```shiki
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
```

---

*Copyright © Anthropic. All rights reserved.*
