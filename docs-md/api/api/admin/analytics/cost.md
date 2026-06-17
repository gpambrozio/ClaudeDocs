# Cost

Copy page



# Cost

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

---

*Copyright © Anthropic. All rights reserved.*
