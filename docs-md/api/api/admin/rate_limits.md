# Rate Limits

Copy page

# Rate Limits

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

---

*Copyright © Anthropic. All rights reserved.*
