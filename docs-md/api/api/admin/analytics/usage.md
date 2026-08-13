# Usage

Copy page



# Usage

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

results: array of object { cache\_creation, cache\_read\_input\_tokens, context\_window, 10 more } 

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

Product surface that produced the usage or cost. Null unless product is in group\_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude\_code", "cowork", "office\_agent", "claude\_in\_chrome", "claude\_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

rbac\_group\_id: string

RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group\_by.

requests: number

Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).



server\_tool\_use: object { web\_search\_requests } 

web\_search\_requests: number

The number of web search requests made.

slack\_channel\_id: string

Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

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

data: array of object { actor, cache\_creation, cache\_read\_input\_tokens, 14 more } 



actor: [AnalyticsUserActor](api/admin/analytics.md) { deleted, email, name, 2 more } 

deleted: boolean

True if the account has been deleted. `name` is `"Deleted User"` and `email` is null in that case; the `user_id` is still populated for reconciliation.

email: string

The user's email address. Null when unavailable or when the account has been deleted (check `deleted`).

name: string

The user's name. Returns `"Deleted User"` when the account has been deleted (`deleted: true`). Null when unavailable.

type: "user\_actor"

user\_id: string

Tagged user ID.

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

Product surface that produced the usage or cost. Null unless product is in group\_by[]; it can also be null on grouped rows whose usage cannot be attributed to a known surface. Values include "chat", "claude\_code", "cowork", "office\_agent", "claude\_in\_chrome", "claude\_design", and "claude-in-slack". "claude-in-slack" (with hyphens) is Claude Tag, the Claude product in Slack. A similarly spelled legacy value (underscores instead of hyphens) identifies the retiring v1 Slack chat bot and appears only for organizations that used it. Some unattributed usage is reported as "other".

rbac\_group\_id: string

RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group\_by.

requests: number

Number of API requests in this row's scope. For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).



server\_tool\_use: object { web\_search\_requests } 

web\_search\_requests: number

The number of web search requests made.

slack\_channel\_id: string

Slack channel the usage originated from. Populated only when `slack_channel_id` is in `group_by[]`; null for usage outside Slack (and for rows recorded before channel attribution was enabled).

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

---

*Copyright © Anthropic. All rights reserved.*
