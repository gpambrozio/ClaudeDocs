# Admin

Copy page



# Admin

#### AdminOrganizations

##### [Get Current Organization](api/admin/organizations/me.md)

GET/v1/organizations/me

##### ModelsExpand Collapse



Organization object { id, name, type } 

id: string

ID of the Organization.

name: string

Name of the Organization.



type: "organization"

Object type.

For Organizations, this is always `"organization"`.

#### AdminInvites

##### [Create Invite](api/admin/invites/create.md)

POST/v1/organizations/invites

##### [Get Invite](api/admin/invites/retrieve.md)

GET/v1/organizations/invites/{invite\_id}

##### [List Invites](api/admin/invites/list.md)

GET/v1/organizations/invites

##### [Delete Invite](api/admin/invites/delete.md)

DELETE/v1/organizations/invites/{invite\_id}

##### ModelsExpand Collapse



Invite object { id, email, expires\_at, 4 more } 

id: string

ID of the Invite.

email: string

Email of the User being invited.

expires\_at: string

RFC 3339 datetime string indicating when the Invite expires.

invited\_at: string

RFC 3339 datetime string indicating when the Invite was created.



role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

One of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"



status: "accepted" or "expired" or "deleted" or "pending"

Status of the Invite.

One of the following:

"accepted"

"expired"

"deleted"

"pending"



type: "invite"

Object type.

For Invites, this is always `"invite"`.



InviteDeleteResponse object { id, type } 

id: string

ID of the Invite.



type: "invite\_deleted"

Deleted object type.

For Invites, this is always `"invite_deleted"`.

#### AdminUsers

##### [Get User](api/admin/users/retrieve.md)

GET/v1/organizations/users/{user\_id}

##### [List Users](api/admin/users/list.md)

GET/v1/organizations/users

##### [Update User](api/admin/users/update.md)

POST/v1/organizations/users/{user\_id}

##### [Remove User](api/admin/users/delete.md)

DELETE/v1/organizations/users/{user\_id}

##### ModelsExpand Collapse



User object { id, added\_at, email, 3 more } 

id: string

ID of the User.

added\_at: string

RFC 3339 datetime string indicating when the User joined the Organization.

email: string

Email of the User.

name: string

Name of the User.



role: "user" or "developer" or "billing" or 2 more

Organization role of the User.

One of the following:

"user"

"developer"

"billing"

"admin"

"claude\_code\_user"



type: "user"

Object type.

For Users, this is always `"user"`.



UserDeleteResponse object { id, type } 

id: string

ID of the User.



type: "user\_deleted"

Deleted object type.

For Users, this is always `"user_deleted"`.

#### AdminWorkspaces

##### [Create Workspace](api/admin/workspaces/create.md)

POST/v1/organizations/workspaces

##### [Get Workspace](api/admin/workspaces/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}

##### [List Workspaces](api/admin/workspaces/list.md)

GET/v1/organizations/workspaces

##### [Update Workspace](api/admin/workspaces/update.md)

POST/v1/organizations/workspaces/{workspace\_id}

##### [Archive Workspace](api/admin/workspaces/archive.md)

POST/v1/organizations/workspaces/{workspace\_id}/archive

#### AdminWorkspacesMembers

##### [Create Workspace Member](api/admin/workspaces/members/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/members

##### [Get Workspace Member](api/admin/workspaces/members/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [List Workspace Members](api/admin/workspaces/members/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/members

##### [Update Workspace Member](api/admin/workspaces/members/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### [Delete Workspace Member](api/admin/workspaces/members/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/members/{user\_id}

##### ModelsExpand Collapse



WorkspaceMember object { type, user\_id, workspace\_id, workspace\_role } 



type: "workspace\_member"

Object type.

For Workspace Members, this is always `"workspace_member"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the Workspace Member.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



MemberDeleteResponse object { type, user\_id, workspace\_id } 



type: "workspace\_member\_deleted"

Deleted object type.

For Workspace Members, this is always `"workspace_member_deleted"`.

user\_id: string

ID of the User.

workspace\_id: string

ID of the Workspace.

#### AdminWorkspacesRate Limits

##### [List Workspace Rate Limits](api/admin/workspaces/rate_limits/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

##### ModelsExpand Collapse



RateLimitListResponse object { data, next\_page } 



data: array of object { group\_type, limits, models, type } 

Rate-limit entries for the workspace, one per group that has at least one override.



group\_type: "model\_group" or "batch" or "token\_count" or 3 more

The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

One of the following:

"model\_group"

"batch"

"token\_count"

"files"

"skills"

"web\_search"



limits: array of object { org\_limit, type, value } 

The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

org\_limit: number

The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The workspace-level override value for this limiter type.

models: array of string

Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

type: "workspace\_rate\_limit"

Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### AdminWorkspacesService Accounts

##### [Create Service Account Workspace Member](api/admin/workspaces/service_accounts/create.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Get Service Account Workspace Member](api/admin/workspaces/service_accounts/retrieve.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [List Service Account Workspace Members](api/admin/workspaces/service_accounts/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/service\_accounts

##### [Update Service Account Workspace Member](api/admin/workspaces/service_accounts/update.md)

POST/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### [Delete Service Account Workspace Member](api/admin/workspaces/service_accounts/delete.md)

DELETE/v1/organizations/workspaces/{workspace\_id}/service\_accounts/{service\_account\_id}

##### ModelsExpand Collapse



ServiceAccountCreateResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



ServiceAccountRetrieveResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



ServiceAccountListResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



ServiceAccountUpdateResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



ServiceAccountDeleteResponse object { service\_account\_id, type, workspace\_id } 

service\_account\_id: string

Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

type: "service\_account\_workspace\_member\_deleted"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### AdminAPI Keys

##### [Get API Key](api/admin/api_keys/retrieve.md)

GET/v1/organizations/api\_keys/{api\_key\_id}

##### [List API Keys](api/admin/api_keys/list.md)

GET/v1/organizations/api\_keys

##### [Update API Key](api/admin/api_keys/update.md)

POST/v1/organizations/api\_keys/{api\_key\_id}

#### AdminExternal Keys

##### [Create External Key](api/admin/external_keys/create.md)

POST/v1/organizations/external\_keys

##### [List External Keys](api/admin/external_keys/list.md)

GET/v1/organizations/external\_keys

##### [Get External Key](api/admin/external_keys/retrieve.md)

GET/v1/organizations/external\_keys/{external\_key\_id}

##### [Update External Key](api/admin/external_keys/update.md)

POST/v1/organizations/external\_keys/{external\_key\_id}

##### [Delete External Key](api/admin/external_keys/delete.md)

DELETE/v1/organizations/external\_keys/{external\_key\_id}

##### [Validate External Key](api/admin/external_keys/validate.md)

POST/v1/organizations/external\_keys/{external\_key\_id}/validate

##### ModelsExpand Collapse



ExternalKeyCreateResponse object { id, created\_at, display\_name, 4 more } 

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Tagged ID of the external key config.

created\_at: string

display\_name: string

Human-friendly display name.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: object { kms\_arn, role\_arn, type, region }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, role\_arn, type, region } 

kms\_arn: string

Full ARN of the AWS KMS key.

role\_arn: string

IAM role ARN that Anthropic assumes to access the KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault URI.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string



ExternalKeyListResponse object { id, created\_at, display\_name, 4 more } 

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Tagged ID of the external key config.

created\_at: string

display\_name: string

Human-friendly display name.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: object { kms\_arn, role\_arn, type, region }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, role\_arn, type, region } 

kms\_arn: string

Full ARN of the AWS KMS key.

role\_arn: string

IAM role ARN that Anthropic assumes to access the KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault URI.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string



ExternalKeyRetrieveResponse object { id, created\_at, display\_name, 4 more } 

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Tagged ID of the external key config.

created\_at: string

display\_name: string

Human-friendly display name.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: object { kms\_arn, role\_arn, type, region }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, role\_arn, type, region } 

kms\_arn: string

Full ARN of the AWS KMS key.

role\_arn: string

IAM role ARN that Anthropic assumes to access the KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault URI.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string



ExternalKeyUpdateResponse object { id, created\_at, display\_name, 4 more } 

CMEK external key config belonging to the caller's organization.

Configs are organization-scoped. Workspaces attach to a config; once any
workspace references it, the provider fields become effectively immutable
(existing encrypted data needs the config for decrypt).

id: string

Tagged ID of the external key config.

created\_at: string

display\_name: string

Human-friendly display name.

geo: string

Data residency geo. Selects which regional validator handles this key's encrypt/decrypt roundtrips.



provider\_config: object { kms\_arn, role\_arn, type, region }  or object { key\_name, type }  or object { key\_name, tenant\_id, type, 2 more } 

KMS provider identity and auth coordinates.

One of the following:



Aws object { kms\_arn, role\_arn, type, region } 

kms\_arn: string

Full ARN of the AWS KMS key.

role\_arn: string

IAM role ARN that Anthropic assumes to access the KMS key.

type: "aws"

region: optional string

AWS region. Derived from kms\_arn if omitted.



Gcp object { key\_name, type } 

key\_name: string

Full resource name of the Cloud KMS key.

type: "gcp"



Azure object { key\_name, tenant\_id, type, 2 more } 

key\_name: string

Name of the key within the vault.

tenant\_id: string

Azure AD tenant ID.

type: "azure"

vault\_uri: string

Key Vault URI.

client\_id: optional string

Azure AD application (client) ID. Omit to use Anthropic's multi-tenant app. Provide only if using a single-tenant app registration in the customer's directory.

type: "external\_key"

updated\_at: string



ExternalKeyDeleteResponse object { id, type } 

id: string

ID of the deleted External Key.

type: "external\_key\_deleted"



ExternalKeyValidateResponse object { error, status, type } 

Result of a validation roundtrip against the customer's KMS.

HTTP 200 for both outcomes — the operation completed; `status` says
whether the key works.

error: string

Error message when status is `failure`. Null otherwise.



status: "success" or "failure"

`success` — encrypt/decrypt roundtrip succeeded. `failure` — the roundtrip failed or timed out; see `error`.

One of the following:

"success"

"failure"

type: "external\_key\_validation"

#### AdminUsage Report

##### [Get Messages Usage Report](api/admin/usage_report/retrieve_messages.md)

GET/v1/organizations/usage\_report/messages

##### [Get Claude Code Usage Report](api/admin/usage_report/retrieve_claude_code.md)

GET/v1/organizations/usage\_report/claude\_code

##### ModelsExpand Collapse



ClaudeCodeUsageReport object { data, has\_more, next\_page } 



data: array of object { actor, core\_metrics, customer\_type, 6 more } 

List of Claude Code usage records for the requested date.



actor: object { email\_address, type }  or object { api\_key\_name, type } 

The user or API key that performed the Claude Code actions.

One of the following:



UserActor object { email\_address, type } 

email\_address: string

Email address of the user who performed Claude Code actions.

type: "user\_actor"



APIActor object { api\_key\_name, type } 

api\_key\_name: string

Name of the API key used to perform Claude Code actions.

type: "api\_actor"



core\_metrics: object { commits\_by\_claude\_code, lines\_of\_code, num\_sessions, pull\_requests\_by\_claude\_code } 

Core productivity metrics measuring Claude Code usage and impact.

commits\_by\_claude\_code: number

Number of git commits created through Claude Code's commit functionality.



lines\_of\_code: object { added, removed } 

Statistics on code changes made through Claude Code.

added: number

Total number of lines of code added across all files by Claude Code.

removed: number

Total number of lines of code removed across all files by Claude Code.

num\_sessions: number

Number of distinct Claude Code sessions initiated by this actor.

pull\_requests\_by\_claude\_code: number

Number of pull requests created through Claude Code's PR functionality.



customer\_type: "api" or "subscription"

Type of customer account (api for API customers, subscription for Pro/Team customers).

One of the following:

"api"

"subscription"

date: string

UTC date for the usage metrics in YYYY-MM-DD format.



model\_breakdown: array of object { estimated\_cost, model, tokens } 

Token usage and cost breakdown by AI model used.



estimated\_cost: object { amount, currency } 

Estimated cost for using this model

amount: number

Estimated cost amount in minor currency units (e.g., cents for USD).

currency: string

Currency code for the estimated cost (e.g., 'USD').

model: string

Name of the AI model used for Claude Code interactions.



tokens: object { cache\_creation, cache\_read, input, output } 

Token usage breakdown for this model

cache\_creation: number

Number of cache creation tokens consumed by this model.

cache\_read: number

Number of cache read tokens consumed by this model.

input: number

Number of input tokens consumed by this model.

output: number

Number of output tokens generated by this model.

organization\_id: string

ID of the organization that owns the Claude Code usage.

terminal\_type: string

Type of terminal or environment where Claude Code was used.



tool\_actions: map[object { accepted, rejected } ]

Breakdown of tool action acceptance and rejection rates by tool type.

accepted: number

Number of tool action proposals that the user accepted.

rejected: number

Number of tool action proposals that the user rejected.



subscription\_type: optional "enterprise" or "team"

Subscription tier for subscription customers. `null` for API customers.

One of the following:

"enterprise"

"team"

has\_more: boolean

True if there are more records available beyond the current page.

next\_page: string

Opaque cursor token for fetching the next page of results, or null if no more pages are available.



MessagesUsageReport object { data, has\_more, next\_page } 



data: array of object { ending\_at, results, starting\_at } 

ending\_at: string

End of the time bucket (exclusive) in RFC 3339 format.



results: array of object { account\_id, api\_key\_id, cache\_creation, 10 more } 

List of usage items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

account\_id: string

ID of the user account that made the request. `null` if not grouping by account or for non-OAuth requests.

api\_key\_id: string

ID of the API key used. `null` if not grouping by API key or for usage in the Anthropic Console.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

The number of input tokens for cache creation.

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.



context\_window: "0-200k" or "200k-1M"

Context window used. `null` if not grouping by context window.

One of the following:

"0-200k"

"200k-1M"

inference\_geo: string

Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

model: string

Model used. `null` if not grouping by model.

output\_tokens: number

The number of output tokens generated.



server\_tool\_use: object { web\_search\_requests } 

Server-side tool usage metrics.

web\_search\_requests: number

The number of web search requests made.

service\_account\_id: string

ID of the service account that made the request. `null` if not grouping by service account or for non-OIDC-federation requests.



service\_tier: "standard" or "batch" or "priority" or 3 more

Service tier used. `null` if not grouping by service tier.

One of the following:

"standard"

"batch"

"priority"

"priority\_on\_demand"

"flex"

"flex\_discount"

uncached\_input\_tokens: number

The number of uncached input tokens processed.

workspace\_id: string

ID of the Workspace used. `null` if not grouping by workspace or for the default workspace.

starting\_at: string

Start of the time bucket (inclusive) in RFC 3339 format.

has\_more: boolean

Indicates if there are more results.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### AdminCost Report

##### [Get Cost Report](api/admin/cost_report/retrieve.md)

GET/v1/organizations/cost\_report

##### ModelsExpand Collapse



CostReport object { data, has\_more, next\_page } 



data: array of object { ending\_at, results, starting\_at } 

ending\_at: string

End of the time bucket (exclusive) in RFC 3339 format.



results: array of object { amount, context\_window, cost\_type, 7 more } 

List of cost items for this time bucket. There may be multiple items if one or more `group_by[]` parameters are specified.

amount: string

Cost amount in lowest currency units (e.g. cents) as a decimal string. For example, `"123.45"` in `"USD"` represents `$1.23`.



context\_window: "0-200k" or "200k-1M"

Input context window used. `null` if not grouping by description or for non-token costs.

One of the following:

"0-200k"

"200k-1M"



cost\_type: "tokens" or "web\_search" or "code\_execution" or "session\_usage"

Type of cost. `null` if not grouping by description.

One of the following:

"tokens"

"web\_search"

"code\_execution"

"session\_usage"

currency: string

Currency code for the cost amount. Currently always `"USD"`.

description: string

Description of the cost item. `null` if not grouping by description.

inference\_geo: string

Inference geo used matching requests' `inference_geo` parameter if set, otherwise the workspace's `default_inference_geo`.
For models that do not support specifying `inference_geo` the value is `"not_available"`. Always `null` if not grouping by inference geo.

model: string

Model name used. `null` if not grouping by description or for non-token costs.



service\_tier: "standard" or "batch"

Service tier used. `null` if not grouping by description or for non-token costs.

One of the following:

"standard"

"batch"



token\_type: "uncached\_input\_tokens" or "output\_tokens" or "cache\_read\_input\_tokens" or 2 more

Type of token. `null` if not grouping by description or for non-token costs.

One of the following:

"uncached\_input\_tokens"

"output\_tokens"

"cache\_read\_input\_tokens"

"cache\_creation.ephemeral\_1h\_input\_tokens"

"cache\_creation.ephemeral\_5m\_input\_tokens"

workspace\_id: string

ID of the Workspace this cost is associated with. `null` if not grouping by workspace or for the default workspace.

starting\_at: string

Start of the time bucket (inclusive) in RFC 3339 format.

has\_more: boolean

Indicates if there are more results.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### AdminAnalytics

##### [Get Activity Summaries](api/admin/analytics/retrieve_summaries.md)

GET/v1/organizations/analytics/summaries

##### ModelsExpand Collapse



ActivitySummary object { summaries } 

Response for GET /v1/organizations/analytics/summaries.



summaries: array of object { assigned\_seat\_count, cowork\_daily\_active\_user\_count, cowork\_monthly\_active\_user\_count, 10 more } 

assigned\_seat\_count: number

Number of seats currently assigned to members

cowork\_daily\_active\_user\_count: number

Number of users with Cowork activity on the requested day

cowork\_monthly\_active\_user\_count: number

Number of users with Cowork activity in the 30-day rolling window

cowork\_weekly\_active\_user\_count: number

Number of users with Cowork activity in the 7-day rolling window

daily\_active\_user\_count: number

Number of users with token consumption on the requested day

daily\_adoption\_rate: number

Percentage of assigned seats with activity on the requested day (DAU / assigned\_seat\_count \* 100)

ending\_at: string

End time in UTC of aggregation period (e.g. 2026-01-16T00:00

)

monthly\_active\_user\_count: number

Number of users with token consumption in the 30-day rolling window

monthly\_adoption\_rate: number

Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned\_seat\_count \* 100)

pending\_invite\_count: number

Number of pending invitations to join the organization

starting\_at: string

Start time in UTC of aggregation period (e.g. 2026-01-15T00:00

)

weekly\_active\_user\_count: number

Number of users with token consumption in the 7-day rolling window

weekly\_adoption\_rate: number

Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned\_seat\_count \* 100)



AnalyticsUser object { id, email\_address } 

User identifier.

id: string

Tagged user identifier (e.g. user\_...)

email\_address: string

Email address of the user



AnalyticsUserActor object { user\_id, deleted, email, 2 more } 

user\_id: string

Tagged user ID.

deleted: optional boolean

True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

email: optional string

The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

name: optional string

The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

type: optional "user\_actor"



ConnectorOfficeProductMetrics object { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



OfficeProductMetrics object { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



SkillOfficeProductMetrics object { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



ToolActionCounts object { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected

#### AdminAnalyticsUsage

##### [Get Token Usage Over Time](api/admin/analytics/usage/list.md)

GET/v1/organizations/analytics/usage\_report

##### [Get Per-User Token Usage](api/admin/analytics/usage/list_by_user.md)

GET/v1/organizations/analytics/user\_usage\_report

##### ModelsExpand Collapse



UsageBucket object { data, data\_refreshed\_at, has\_more, 2 more } 



data: array of object { ending\_at, results, starting\_at } 

ending\_at: string



results: array of object { cache\_creation, cache\_read\_input\_tokens, context\_window, 8 more } 



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.



context\_window: "0-200k" or "200k-1M"

One of the following:

"0-200k"

"200k-1M"



inference\_geo: "global" or "us"

One of the following:

"global"

"us"

model: string

output\_tokens: number

The number of output tokens generated.

product: string

Product surface that produced the usage or cost. Null unless product is in group\_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude\_code", "cowork", "office\_agent", "claude\_in\_chrome", and "claude\_design". Some unattributed usage is reported as "other".

requests: number

Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).



server\_tool\_use: object { web\_search\_requests } 

web\_search\_requests: number

The number of web search requests made.



speed: "fast" or "standard"

One of the following:

"fast"

"standard"

uncached\_input\_tokens: number

The number of uncached input tokens processed.

starting\_at: string

data\_refreshed\_at: string

RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

has\_more: boolean

next\_page: string

organization\_id: string

ID of the Organization.



UserUsage object { data, data\_refreshed\_at, has\_more, 2 more } 



data: array of object { actor, cache\_creation, cache\_read\_input\_tokens, 12 more } 



actor: [AnalyticsUserActor](api/admin.md) { user\_id, deleted, email, 2 more } 

user\_id: string

Tagged user ID.

deleted: optional boolean

True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

email: optional string

The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

name: optional string

The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

type: optional "user\_actor"



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.



context\_window: "0-200k" or "200k-1M"

One of the following:

"0-200k"

"200k-1M"

ending\_at: string



inference\_geo: "global" or "us"

One of the following:

"global"

"us"

model: string

output\_tokens: number

The number of output tokens generated.

product: string

Product surface that produced the usage or cost. Null unless product is in group\_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude\_code", "cowork", "office\_agent", "claude\_in\_chrome", and "claude\_design". Some unattributed usage is reported as "other".

requests: number

Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).



server\_tool\_use: object { web\_search\_requests } 

web\_search\_requests: number

The number of web search requests made.



speed: "fast" or "standard"

One of the following:

"fast"

"standard"

starting\_at: string

total\_tokens: number

Total token count across all token types. This is the value the default order\_by='total\_tokens' sorts on.

uncached\_input\_tokens: number

The number of uncached input tokens processed.

data\_refreshed\_at: string

RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

has\_more: boolean

next\_page: string

organization\_id: string

ID of the Organization.

#### AdminAnalyticsCost

##### [Get Cost Over Time](api/admin/analytics/cost/list.md)

GET/v1/organizations/analytics/cost\_report

##### [Get Per-User Cost](api/admin/analytics/cost/list_by_user.md)

GET/v1/organizations/analytics/user\_cost\_report

##### ModelsExpand Collapse



CostBucket object { data, data\_refreshed\_at, has\_more, 2 more } 



data: array of object { ending\_at, results, starting\_at } 

ending\_at: string



results: array of object { amount, context\_window, cost\_type, 8 more } 

amount: string

Amount (post-discount, pre-credit) in fractional cents.



context\_window: "0-200k" or "200k-1M"

One of the following:

"0-200k"

"200k-1M"



cost\_type: "tokens" or "web\_search" or "code\_execution"

Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

One of the following:

"tokens"

"web\_search"

"code\_execution"

currency: "USD"



inference\_geo: "global" or "us"

One of the following:

"global"

"us"

list\_amount: string

List-price amount (pre-discount) in fractional cents.

model: string

product: string

Product surface that produced the usage or cost. Null unless product is in group\_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude\_code", "cowork", "office\_agent", "claude\_in\_chrome", and "claude\_design". Some unattributed usage is reported as "other".

requests: number

Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).



speed: "fast" or "standard"

One of the following:

"fast"

"standard"



token\_type: "uncached\_input\_tokens" or "output\_tokens" or "cache\_read\_input\_tokens" or 2 more

Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

One of the following:

"uncached\_input\_tokens"

"output\_tokens"

"cache\_read\_input\_tokens"

"cache\_creation.ephemeral\_1h\_input\_tokens"

"cache\_creation.ephemeral\_5m\_input\_tokens"

starting\_at: string

data\_refreshed\_at: string

RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

has\_more: boolean

next\_page: string

organization\_id: string

ID of the Organization.



UserCost object { data, data\_refreshed\_at, has\_more, 2 more } 



data: array of object { actor, amount, context\_window, 11 more } 



actor: [AnalyticsUserActor](api/admin.md) { user\_id, deleted, email, 2 more } 

user\_id: string

Tagged user ID.

deleted: optional boolean

True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

email: optional string

The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

name: optional string

The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

type: optional "user\_actor"

amount: string

Amount (post-discount, pre-credit) in fractional cents (minor units).



context\_window: "0-200k" or "200k-1M"

One of the following:

"0-200k"

"200k-1M"



cost\_type: "tokens" or "web\_search" or "code\_execution"

Cost component breakdown; null when returning the combined total.

One of the following:

"tokens"

"web\_search"

"code\_execution"

currency: "USD"

ending\_at: string



inference\_geo: "global" or "us"

One of the following:

"global"

"us"

list\_amount: string

List-price amount (pre-discount) in fractional cents.

model: string

product: string

Product surface that produced the usage or cost. Null unless product is in group\_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude\_code", "cowork", "office\_agent", "claude\_in\_chrome", and "claude\_design". Some unattributed usage is reported as "other".

requests: number

Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).



speed: "fast" or "standard"

One of the following:

"fast"

"standard"

starting\_at: string



token\_type: "uncached\_input\_tokens" or "output\_tokens" or "cache\_read\_input\_tokens" or 2 more

Token type when cost\_type=tokens; null otherwise.

One of the following:

"uncached\_input\_tokens"

"output\_tokens"

"cache\_read\_input\_tokens"

"cache\_creation.ephemeral\_1h\_input\_tokens"

"cache\_creation.ephemeral\_5m\_input\_tokens"

data\_refreshed\_at: string

RFC 3339 timestamp of the export this response was served from. Data beyond this watermark is incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

has\_more: boolean

next\_page: string

organization\_id: string

ID of the Organization.

#### AdminAnalyticsUsers

##### [List User Activity](api/admin/analytics/users/list.md)

GET/v1/organizations/analytics/users

##### ModelsExpand Collapse



UserActivity object { data, next\_page } 

Response for GET /v1/organizations/analytics/users.



data: array of object { chat\_metrics, claude\_code\_metrics, cowork\_metrics, 4 more } 



chat\_metrics: object { connectors\_used\_count, distinct\_artifacts\_created\_count, distinct\_conversation\_count, 8 more } 

Claude.ai activity metrics for a single user on a given day.

connectors\_used\_count: number

Number of MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_artifacts\_created\_count: number

Number of distinct artifacts created

distinct\_conversation\_count: number

Number of distinct conversations the user participated in. Null on aggregated rows where a distinct count cannot be computed.

distinct\_files\_uploaded\_count: number

Number of distinct files uploaded. Null on aggregated rows where a distinct count cannot be computed.

distinct\_projects\_created\_count: number

Number of distinct projects created

distinct\_projects\_used\_count: number

Number of distinct projects used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_shared\_artifacts\_viewed\_count: number

Number of distinct shared artifacts the user viewed. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

shared\_conversations\_viewed\_count: number

Number of times the user opened a shared conversation in a project

thinking\_message\_count: number

Number of messages that used extended thinking



claude\_code\_metrics: object { core\_metrics, tool\_actions } 

Claude Code activity metrics for a single user on a given day.



core\_metrics: object { commit\_count, distinct\_session\_count, lines\_of\_code, pull\_request\_count } 

Core Claude Code activity metrics for a single user on a given day.

commit\_count: number

Number of commits made via Claude Code

distinct\_session\_count: number

Number of distinct Claude Code sessions. Null on aggregated rows where a distinct count cannot be computed.



lines\_of\_code: object { added\_count, removed\_count } 

Lines of code added and removed via Claude Code.

added\_count: number

Lines of code added

removed\_count: number

Lines of code removed

pull\_request\_count: number

Number of pull requests created via Claude Code



tool\_actions: object { edit\_tool, multi\_edit\_tool, notebook\_edit\_tool, write\_tool } 

Per-tool accepted/rejected counts for Claude Code file modification tools.



edit\_tool: [ToolActionCounts](api/admin.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



multi\_edit\_tool: [ToolActionCounts](api/admin.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



notebook\_edit\_tool: [ToolActionCounts](api/admin.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



write\_tool: [ToolActionCounts](api/admin.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



cowork\_metrics: object { action\_count, connectors\_used\_count, dispatch\_turn\_count, 5 more } 

Cowork activity metrics for a single user on a given day.

action\_count: number

Number of tool actions completed in Cowork sessions

connectors\_used\_count: number

Total number of connector invocations in Cowork sessions

dispatch\_turn\_count: number

Number of Dispatch (background agent) turns completed

distinct\_connectors\_used\_count: number

Number of distinct connectors used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Cowork sessions

skills\_used\_count: number

Total number of skill invocations in Cowork sessions



design\_metrics: object { distinct\_projects\_created\_count, distinct\_projects\_used\_count, distinct\_session\_count, message\_count } 

Claude Design activity metrics for a single user on a given day.

distinct\_projects\_created\_count: number

Number of distinct Claude Design projects created

distinct\_projects\_used\_count: number

Number of distinct Claude Design projects the user worked in. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Claude Design sessions. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Claude Design sessions



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single user on a given day, broken out by Office product.



excel: [OfficeProductMetrics](api/admin.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



outlook: [OfficeProductMetrics](api/admin.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



powerpoint: [OfficeProductMetrics](api/admin.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



word: [OfficeProductMetrics](api/admin.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations

web\_search\_count: number

Number of web searches performed



user: optional [AnalyticsUser](api/admin.md) { id, email\_address } 

User identifier.

id: string

Tagged user identifier (e.g. user\_...)

email\_address: string

Email address of the user

next\_page: string

Opaque cursor for the next page, or null if no more results

#### AdminAnalyticsSkills

##### [Get Skill Usage](api/admin/analytics/skills/list.md)

GET/v1/organizations/analytics/skills

##### ModelsExpand Collapse



SkillUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/skills.



data: array of object { chat\_metrics, claude\_code\_metrics, cowork\_metrics, 3 more } 



chat\_metrics: object { distinct\_conversation\_skill\_used\_count } 

Claude.ai activity metrics for a single skill on a given day.

distinct\_conversation\_skill\_used\_count: number

Number of distinct conversations in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



claude\_code\_metrics: object { distinct\_session\_skill\_used\_count } 

Claude Code activity metrics for a single skill on a given day.

distinct\_session\_skill\_used\_count: number

Number of distinct Claude Code sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



cowork\_metrics: object { distinct\_session\_skill\_used\_count } 

Cowork activity metrics for a single skill on a given day.

distinct\_session\_skill\_used\_count: number

Number of distinct Cowork sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_user\_count: number

Number of distinct users who used the skill on the requested day



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single skill on a given day, broken out by Office product.



excel: [SkillOfficeProductMetrics](api/admin.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



outlook: [SkillOfficeProductMetrics](api/admin.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



powerpoint: [SkillOfficeProductMetrics](api/admin.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



word: [SkillOfficeProductMetrics](api/admin.md) { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.

skill\_name: string

Name of the skill

next\_page: string

Opaque cursor for the next page, or null if no more results

#### AdminAnalyticsConnectors

##### [Get Connector Usage](api/admin/analytics/connectors/list.md)

GET/v1/organizations/analytics/connectors

##### ModelsExpand Collapse



ConnectorUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/connectors.



data: array of object { chat\_metrics, claude\_code\_metrics, connector\_name, 3 more } 



chat\_metrics: object { distinct\_conversation\_connector\_used\_count } 

Claude.ai activity metrics for a single connector on a given day.

distinct\_conversation\_connector\_used\_count: number

Number of distinct conversations in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



claude\_code\_metrics: object { distinct\_session\_connector\_used\_count } 

Claude Code activity metrics for a single connector on a given day.

distinct\_session\_connector\_used\_count: number

Number of distinct Claude Code sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

connector\_name: string

Name of the connector



cowork\_metrics: object { distinct\_session\_connector\_used\_count } 

Cowork activity metrics for a single connector on a given day.

distinct\_session\_connector\_used\_count: number

Number of distinct Cowork sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_user\_count: number

Number of distinct users who used the connector on the requested day



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single connector on a given day, broken out by Office product.



excel: [ConnectorOfficeProductMetrics](api/admin.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



outlook: [ConnectorOfficeProductMetrics](api/admin.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



powerpoint: [ConnectorOfficeProductMetrics](api/admin.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



word: [ConnectorOfficeProductMetrics](api/admin.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.

next\_page: string

Opaque cursor for the next page, or null if no more results

#### AdminAnalyticsChat Projects

##### [Get Chat Project Usage](api/admin/analytics/chat_projects/list.md)

GET/v1/organizations/analytics/apps/chat/projects

##### ModelsExpand Collapse



ChatProjectUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/apps/chat/projects.



data: array of object { distinct\_conversation\_count, distinct\_user\_count, message\_count, 4 more } 

distinct\_conversation\_count: number

Number of distinct conversations in the project on the requested day

distinct\_user\_count: number

Number of distinct users who used the project on the requested day

message\_count: number

Number of messages sent in the project on the requested day

project\_id: string

Tagged project identifier (e.g. claude\_proj\_...)

project\_name: string

Name of the project

created\_at: optional string

Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.



created\_by: optional [AnalyticsUser](api/admin.md) { id, email\_address } 

User identifier.

id: string

Tagged user identifier (e.g. user\_...)

email\_address: string

Email address of the user

next\_page: string

Opaque cursor for the next page, or null if no more results

#### AdminSpend Limits

##### [Set Spend Limit](api/admin/spend_limits/create.md)

POST/v1/organizations/spend\_limits

##### [Get Spend Limit](api/admin/spend_limits/retrieve.md)

GET/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [Delete Spend Limit](api/admin/spend_limits/delete.md)

DELETE/v1/organizations/spend\_limits/{spend\_limit\_id}

##### [List Effective Spend Limits](api/admin/spend_limits/list_effective.md)

GET/v1/organizations/spend\_limits/effective

##### ModelsExpand Collapse



SpendLimit object { id, amount, created\_at, 5 more } 

id: string

amount: string

created\_at: string

currency: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"



scope: object { type, user\_id }  or object { seat\_tier, type }  or object { rbac\_group\_id, type }  or 2 more

One of the following:



User object { type, user\_id } 

type: "user"

user\_id: string



SeatTier object { seat\_tier, type } 

seat\_tier: string

type: "seat\_tier"



RbacGroup object { rbac\_group\_id, type } 

rbac\_group\_id: string

type: "rbac\_group"



OrganizationService object { service, type } 

service: string

type: "organization\_service"



Organization object { type } 

type: "organization"

type: "spend\_limit"

updated\_at: string



SpendSummary object { actor, amount, currency, 5 more } 

Per-member effective-limit report row (GET /spend\_limits/effective).



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string

amount: string

currency: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

period\_to\_date\_spend: string



scope: object { type, user\_id } 

type: "user"

user\_id: string



source: object { type, user\_id }  or object { seat\_tier, type }  or object { rbac\_group\_id, type }  or 2 more

One of the following:



User object { type, user\_id } 

type: "user"

user\_id: string



SeatTier object { seat\_tier, type } 

seat\_tier: string

type: "seat\_tier"



RbacGroup object { rbac\_group\_id, type } 

rbac\_group\_id: string

type: "rbac\_group"



OrganizationService object { service, type } 

service: string

type: "organization\_service"



Organization object { type } 

type: "organization"

spend\_limit\_id: string



SpendLimitDeleteResponse object { id, type } 

id: string

type: "spend\_limit\_deleted"

#### AdminSpend LimitsIncrease Requests

##### [List Spend Limit Increase Requests](api/admin/spend_limits/increase_requests/list.md)

GET/v1/organizations/spend\_limit\_increase\_requests

##### [Get Spend Limit Increase Request](api/admin/spend_limits/increase_requests/retrieve.md)

GET/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}

##### [Approve Spend Limit Increase Request](api/admin/spend_limits/increase_requests/approve.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/approve

##### [Deny Spend Limit Increase Request](api/admin/spend_limits/increase_requests/deny.md)

POST/v1/organizations/spend\_limit\_increase\_requests/{spend\_limit\_increase\_request\_id}/deny

##### ModelsExpand Collapse



SpendLimitIncreaseRequest object { id, actor, created\_at, 6 more } 

id: string



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string

created\_at: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

resolved\_at: string



resolved\_by: object { deleted, email\_address, name, 2 more }  or object { scoped\_api\_key\_id, type } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

One of the following:



UserActor object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string



ScopedAPIKeyActor object { scoped\_api\_key\_id, type } 

A scoped Admin API key acting on behalf of the organization.

scoped\_api\_key\_id: string

type: "scoped\_api\_key\_actor"



spend\_summary: [SpendSummary](api/admin.md) { actor, amount, currency, 5 more } 

Per-member effective-limit report row (GET /spend\_limits/effective).



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string

amount: string

currency: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

period\_to\_date\_spend: string



scope: object { type, user\_id } 

type: "user"

user\_id: string



source: object { type, user\_id }  or object { seat\_tier, type }  or object { rbac\_group\_id, type }  or 2 more

One of the following:



User object { type, user\_id } 

type: "user"

user\_id: string



SeatTier object { seat\_tier, type } 

seat\_tier: string

type: "seat\_tier"



RbacGroup object { rbac\_group\_id, type } 

rbac\_group\_id: string

type: "rbac\_group"



OrganizationService object { service, type } 

service: string

type: "organization\_service"



Organization object { type } 

type: "organization"

spend\_limit\_id: string



status: "pending" or "approved" or "denied"

One of the following:

"pending"

"approved"

"denied"

type: "spend\_limit\_increase\_request"



IncreaseRequestApproveResponse object { id, actor, created\_at, 7 more } 

id: string



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string

created\_at: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

resolved\_at: string



resolved\_by: object { deleted, email\_address, name, 2 more }  or object { scoped\_api\_key\_id, type } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

One of the following:



UserActor object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string



ScopedAPIKeyActor object { scoped\_api\_key\_id, type } 

A scoped Admin API key acting on behalf of the organization.

scoped\_api\_key\_id: string

type: "scoped\_api\_key\_actor"



spend\_limit: [SpendLimit](api/admin.md) { id, amount, created\_at, 5 more } 

id: string

amount: string

created\_at: string

currency: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"



scope: object { type, user\_id }  or object { seat\_tier, type }  or object { rbac\_group\_id, type }  or 2 more

One of the following:



User object { type, user\_id } 

type: "user"

user\_id: string



SeatTier object { seat\_tier, type } 

seat\_tier: string

type: "seat\_tier"



RbacGroup object { rbac\_group\_id, type } 

rbac\_group\_id: string

type: "rbac\_group"



OrganizationService object { service, type } 

service: string

type: "organization\_service"



Organization object { type } 

type: "organization"

type: "spend\_limit"

updated\_at: string



spend\_summary: [SpendSummary](api/admin.md) { actor, amount, currency, 5 more } 

Per-member effective-limit report row (GET /spend\_limits/effective).



actor: object { deleted, email\_address, name, 2 more } 

A user within the organization. `name` and `email_address` are
null when the underlying account is unavailable or has been deleted;
`deleted` is true only for deleted accounts.

deleted: boolean

email\_address: string

name: string

type: "user\_actor"

user\_id: string

amount: string

currency: string



period: "monthly" or "daily" or "weekly"

One of the following:

"monthly"

"daily"

"weekly"

period\_to\_date\_spend: string



scope: object { type, user\_id } 

type: "user"

user\_id: string



source: object { type, user\_id }  or object { seat\_tier, type }  or object { rbac\_group\_id, type }  or 2 more

One of the following:



User object { type, user\_id } 

type: "user"

user\_id: string



SeatTier object { seat\_tier, type } 

seat\_tier: string

type: "seat\_tier"



RbacGroup object { rbac\_group\_id, type } 

rbac\_group\_id: string

type: "rbac\_group"



OrganizationService object { service, type } 

service: string

type: "organization\_service"



Organization object { type } 

type: "organization"

spend\_limit\_id: string



status: "pending" or "approved" or "denied"

One of the following:

"pending"

"approved"

"denied"

type: "spend\_limit\_increase\_request"

#### AdminRate Limits

##### [List Organization Rate Limits](api/admin/rate_limits/list.md)

GET/v1/organizations/rate\_limits

##### ModelsExpand Collapse



RateLimitListResponse object { data, next\_page } 



data: array of object { group\_type, limits, models, type } 

Rate-limit entries for the organization, one per group.



group\_type: "model\_group" or "batch" or "token\_count" or 3 more

The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

One of the following:

"model\_group"

"batch"

"token\_count"

"files"

"skills"

"web\_search"



limits: array of object { type, value } 

The limiter values that apply to this group.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The configured limit value for this limiter type.

models: array of string

Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

type: "rate\_limit"

Object type. Always `rate_limit` for organization rate-limit entries.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

#### AdminService Accounts

##### [Create Service Account](api/admin/service_accounts/create.md)

POST/v1/organizations/service\_accounts

##### [Get Service Account](api/admin/service_accounts/retrieve.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}

##### [List Service Accounts](api/admin/service_accounts/list.md)

GET/v1/organizations/service\_accounts

##### [Update Service Account](api/admin/service_accounts/update.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}

##### [Archive Service Account](api/admin/service_accounts/archive.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/archive

##### ModelsExpand Collapse



ServiceAccount object { id, archived\_at, archived\_by\_actor\_id, 8 more } 

Named non-human identity within the caller's organization.

A service account is a pure identity: name + org. Authorization lives on
whatever references it (federation rules).

id: string

Tagged ID of the service account.

archived\_at: string

If set, this service account is archived.

archived\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that archived this service account.

created\_at: string

When this service account was created.

created\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that created this service account.

description: string

Optional free-text description.

name: string

Admin-chosen slug identifier.



organization\_role: "developer" or "admin"

Org-level role. A federation rule may only be created or retargeted to grant `org:admin` scope when this is `admin`. A rule granting `org:admin` whose target is later demoted to `developer` is rejected at token exchange. Rules granting `org:admin` are managed in the Console.

One of the following:

"developer"

"admin"

type: "service\_account"

updated\_at: string

When this service account was last updated.

updated\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that last updated this service account.

#### AdminService AccountsWorkspaces

##### [Add Workspace To Service Account](api/admin/service_accounts/workspaces/create.md)

POST/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [List Workspaces For Service Account](api/admin/service_accounts/workspaces/list.md)

GET/v1/organizations/service\_accounts/{service\_account\_id}/workspaces

##### [Remove Workspace From Service Account](api/admin/service_accounts/workspaces/delete.md)

DELETE/v1/organizations/service\_accounts/{service\_account\_id}/workspaces/{workspace\_id}

##### ModelsExpand Collapse



WorkspaceCreateResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



WorkspaceListResponse object { created\_by\_actor\_id, implicit, service\_account\_id, 3 more } 

created\_by\_actor\_id: string

Tagged ID (`user_...`/`svac_...`) of the actor who created this membership.

implicit: boolean

True when this is the implicit default-workspace membership every service account has when no explicit membership exists. Implicit memberships have role workspace\_user and cannot be removed.

service\_account\_id: string

Tagged service account ID (`svac_...`).

type: "service\_account\_workspace\_member"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`).



workspace\_role: "workspace\_user" or "workspace\_developer" or "workspace\_restricted\_developer" or 2 more

Role of the service account in this workspace. Service accounts cannot hold the `workspace_billing` role.

One of the following:

"workspace\_user"

"workspace\_developer"

"workspace\_restricted\_developer"

"workspace\_admin"

"workspace\_billing"



WorkspaceDeleteResponse object { service\_account\_id, type, workspace\_id } 

service\_account\_id: string

Tagged service account ID (`svac_...`) named in the delete request. Removal is idempotent; see the endpoint description for the implicit-membership no-op.

type: "service\_account\_workspace\_member\_deleted"

workspace\_id: string

Tagged workspace ID (`wrkspc_...`) named in the delete request.

#### AdminFederation Issuers

##### [Create Federation Issuer](api/admin/federation_issuers/create.md)

POST/v1/organizations/federation\_issuers

##### [Get Federation Issuer](api/admin/federation_issuers/retrieve.md)

GET/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [List Federation Issuers](api/admin/federation_issuers/list.md)

GET/v1/organizations/federation\_issuers

##### [Update Federation Issuer](api/admin/federation_issuers/update.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}

##### [Archive Federation Issuer](api/admin/federation_issuers/archive.md)

POST/v1/organizations/federation\_issuers/{federation\_issuer\_id}/archive

##### ModelsExpand Collapse



FederationIssuer object { id, archived\_at, archived\_by\_actor\_id, 12 more } 

Registered external OIDC identity provider.

Records an external IdP the organization trusts for the RFC 7523
jwt-bearer grant. The `issuer_url` must match the JWT `iss` claim exactly.

id: string

Tagged ID of the federation issuer.

archived\_at: string

If set, all rules referencing this issuer reject token exchange.

archived\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that archived this issuer.

check\_jti: boolean

Whether the jwt-bearer exchange enforces JTI single-use (replay protection) for tokens from this issuer. Applies only to assertions carrying a `jti` claim; tokens without one are accepted without single-use enforcement.

created\_at: string

When this issuer was created.

created\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that created this issuer.

issuer\_url: string

The `iss` claim value. Incoming JWTs must match exactly.



jwks: object { type, ca\_cert\_pem, discovery\_base }  or object { type, url, ca\_cert\_pem }  or object { keys, type } 

How signing keys are obtained for signature verification.

One of the following:



Discovery object { type, ca\_cert\_pem, discovery\_base } 

JWKS via the issuer's OIDC discovery document.

type: "discovery"

ca\_cert\_pem: optional string

Optional custom CA (PEM) for TLS verification of the JWKS fetch.

discovery\_base: optional string

Set when the discovery URL differs from `issuer_url`.



ExplicitURL object { type, url, ca\_cert\_pem } 

JWKS fetched from a fixed endpoint.

type: "explicit\_url"

url: string

JWKS endpoint.

ca\_cert\_pem: optional string

Optional custom CA (PEM) for TLS verification of the JWKS fetch.



Inline object { keys, type } 

JWKS supplied directly; no network fetch.

keys: array of map[unknown]

Inline JWK objects.

type: "inline"

jwks\_polling\_disabled\_at: string

If set, Anthropic's JWKS poller has paused polling for this issuer after repeated fetch failures. Re-enable by sending `jwks_polling_disabled: false` via the issuer update endpoint (POST) once the upstream JWKS endpoint is fixed. An OAuth caller cannot send this when the issuer backs a rule with any scope other than `workspace:developer` or `workspace:inference`; use a Console session.

max\_jwt\_lifetime\_seconds: number

Maximum allowed iat→exp spread for assertions from this issuer (1-176400 seconds, i.e. up to 49h). Assertions must carry both `iat` and `exp`; a missing `iat` is rejected.

name: string

Admin-chosen slug identifier.



poll\_status: object { consecutive\_failures, last\_fetched\_at, next\_poll\_at } 

Status of automatic JWKS polling for a federation issuer.

Anthropic periodically fetches the issuer's signing keys in the
background. These fields summarize the most recent fetches so the
health of the JWKS endpoint can be monitored.

consecutive\_failures: number

Consecutive fetch failures since the last success.

last\_fetched\_at: string

When the last successful fetch completed.

next\_poll\_at: string

When the next fetch is scheduled. Null if paused.

type: "federation\_issuer"

updated\_at: string

When this issuer was last updated.

updated\_by\_actor\_id: string

Tagged ID (`user_`/`svac_`) of the actor that last updated this issuer.

#### AdminFederation Rules

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

#### AdminFederation RulesWorkspaces

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

#### AdminMCP Tunnels

##### [Get Tunnel](api/admin/mcp_tunnels/retrieve.md)

GET/v1/organizations/tunnels/{tunnel\_id}

##### [List Tunnels](api/admin/mcp_tunnels/list.md)

GET/v1/organizations/tunnels

##### [Reveal Tunnel Token](api/admin/mcp_tunnels/reveal_token.md)

POST/v1/organizations/tunnels/{tunnel\_id}/reveal\_token

##### [Rotate Tunnel Token](api/admin/mcp_tunnels/rotate_token.md)

POST/v1/organizations/tunnels/{tunnel\_id}/rotate\_token

##### [Archive Tunnel](api/admin/mcp_tunnels/archive.md)

POST/v1/organizations/tunnels/{tunnel\_id}/archive

##### ModelsExpand Collapse



MCPTunnelRetrieveResponse object { id, archived\_at, created\_at, 4 more } 

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.



MCPTunnelListResponse object { id, archived\_at, created\_at, 4 more } 

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.



MCPTunnelRevealTokenResponse object { id, tunnel\_token, type } 

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.

type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.



MCPTunnelRotateTokenResponse object { id, tunnel\_token, type } 

id: string

Stable identifier for the current token value. Changes when the token is
rotated.

tunnel\_token: string

The tunnel's connection token.

type: "tunnel\_token"

Object type. Always `tunnel_token` for Tunnel Tokens.



MCPTunnelArchiveResponse object { id, archived\_at, created\_at, 4 more } 

id: string

ID of the Tunnel.

archived\_at: string

RFC 3339 datetime string indicating when the Tunnel was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the Tunnel was created.

display\_name: string

Human-readable name for the Tunnel (1–255 characters), or `null` if unset.

domain: string

Anthropic-assigned hostname for the Tunnel. MCP server URLs whose host is a
subdomain of this value are routed through the Tunnel. Globally unique and
never reused, even after the Tunnel is archived.

type: "tunnel"

Object type. Always `tunnel` for Tunnels.

workspace\_id: string

ID of the Workspace this Tunnel belongs to, or `null` for the default
Workspace. Immutable after creation.

#### AdminMCP TunnelsTunnel Certificates

##### [Create Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/create.md)

POST/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Get Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/retrieve.md)

GET/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}

##### [List Tunnel Certificates](api/admin/mcp_tunnels/tunnel_certificates/list.md)

GET/v1/organizations/tunnels/{tunnel\_id}/certificates

##### [Archive Tunnel Certificate](api/admin/mcp_tunnels/tunnel_certificates/archive.md)

POST/v1/organizations/tunnels/{tunnel\_id}/certificates/{certificate\_id}/archive

##### ModelsExpand Collapse



TunnelCertificateCreateResponse object { id, archived\_at, created\_at, 4 more } 

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.



TunnelCertificateRetrieveResponse object { id, archived\_at, created\_at, 4 more } 

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.



TunnelCertificateListResponse object { id, archived\_at, created\_at, 4 more } 

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.



TunnelCertificateArchiveResponse object { id, archived\_at, created\_at, 4 more } 

id: string

ID of the Tunnel Certificate.

archived\_at: string

RFC 3339 datetime string indicating when the certificate was archived, or
`null` if it is not archived.

created\_at: string

RFC 3339 datetime string indicating when the certificate was registered.

expires\_at: string

RFC 3339 datetime string indicating when the certificate expires, or
`null` if it does not expire.

fingerprint: string

The certificate's SHA-256 fingerprint, as a lowercase hex string.

tunnel\_id: string

ID of the Tunnel this certificate is registered against.

type: "tunnel\_certificate"

Object type. Always `tunnel_certificate` for Tunnel Certificates.

---

*Copyright © Anthropic. All rights reserved.*
