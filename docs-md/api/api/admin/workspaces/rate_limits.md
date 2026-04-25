# Rate Limits

Copy page

# Rate Limits

##### [List Workspace Rate Limits](api/admin/workspaces/rate_limits/list.md)

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

##### ModelsExpand Collapse

RateLimitListResponse = object { data, next\_page }

data: array of object { group\_type, limits, models, type }

Rate-limit entries for the workspace, one per group that has at least one override.

group\_type: "model\_group" or "batch" or "token\_count" or 3 more

The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

Accepts one of the following:

"model\_group"

"batch"

"token\_count"

"files"

"skills"

"web\_search"

limits: array of object { org\_limit, type, value }

The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

org\_limit: number

The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The workspace-level override value for this limiter type.

models: array of string

Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

type: "workspace\_rate\_limit"

Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

next\_page: string

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

---

*Copyright © Anthropic. All rights reserved.*
