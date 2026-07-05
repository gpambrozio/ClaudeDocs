# Get Cost Over Time

Copy page



# Get Cost Over Time

GET/v1/organizations/analytics/cost\_report

Get cost in USD over time across a date range.

Returns cost bucketed by minute, hour, or day, optionally broken down by
product, model, context window, inference region, speed, cost type, or
token type. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse

starting\_at: string

Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00

.



bucket\_width: optional "1d" or "1h" or "1m"

Time bucket granularity.

One of the following:

"1d"

"1h"

"1m"



context\_windows: optional array of "0-200k" or "200k-1M"

Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

One of the following:

"0-200k"

"200k-1M"

ending\_at: optional string

End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.



group\_by: optional array of "context\_window" or "cost\_type" or "inference\_geo" or 5 more

Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

One of the following:

"context\_window"

"cost\_type"

"inference\_geo"

"model"

"product"

"rbac\_group\_id"

"speed"

"token\_type"



inference\_geos: optional array of "global" or "not\_available" or "us"

Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

One of the following:

"global"

"not\_available"

"us"

limit: optional number

Maximum number of time buckets per page. Defaults and caps vary by bucket\_width (1d: default 7, max 31; 1h: default 24, max 168; 1m: default 60, max 256).

models: optional array of string

Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

page: optional string

Opaque cursor from a previous response's `next_page` field.

products: optional array of string

Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values. Values include "chat", "claude\_code", "cowork", "office\_agent", "claude\_in\_chrome", and "claude\_design".

rbac\_group\_ids: optional array of string

Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.



speeds: optional array of "fast" or "standard"

Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

One of the following:

"fast"

"standard"

user\_ids: optional array of string

Filter to specific users by tagged user ID.

##### ReturnsExpand Collapse



CostBucket object { data, data\_refreshed\_at, has\_more, 2 more } 



data: array of object { ending\_at, results, starting\_at } 

ending\_at: string



results: array of object { amount, context\_window, cost\_type, 9 more } 

amount: string

Amount (post-discount, pre-credit) in fractional cents.



context\_window: "0-200k" or "200k-1M"

One of the following:

"0-200k"

"200k-1M"



cost\_type: "code\_execution" or "tokens" or "web\_search"

Cost component when `group_by[]=cost_type`; null otherwise (amount is the combined total).

One of the following:

"code\_execution"

"tokens"

"web\_search"

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

rbac\_group\_id: string

RBAC group (team) the usage is attributed to, in the public tagged `rbac_group_...` spelling — the same spelling the activity resources use for this key, so the same team has ONE id across resources and it round-trips as an `rbac_group_ids[]` filter value. Populated only when `rbac_group_id` is in `group_by[]`. Any-membership semantics: a user in several groups contributes their full usage to each of those groups' rows, so the named-group rows overlap and their sum can exceed the org total. A null value is the single unassigned row: users in no group on that (UTC) day. For the true org total, run the same query with no group\_by.

requests: number

Number of API requests in this row's scope. Null when `group_by` includes `cost_type` or `token_type` (the count has no per-component attribution; read it from the ungrouped response). For sandbox / code-execution events, this counts execution spans rather than HTTP requests (these rows surface with `product: null`).



speed: "fast" or "standard"

One of the following:

"fast"

"standard"



token\_type: "cache\_creation.ephemeral\_1h\_input\_tokens" or "cache\_creation.ephemeral\_5m\_input\_tokens" or "cache\_read\_input\_tokens" or 2 more

Token type when `group_by[]=token_type` and `cost_type=tokens`; null otherwise.

One of the following:

"cache\_creation.ephemeral\_1h\_input\_tokens"

"cache\_creation.ephemeral\_5m\_input\_tokens"

"cache\_read\_input\_tokens"

"output\_tokens"

"uncached\_input\_tokens"

starting\_at: string

data\_refreshed\_at: string

RFC 3339 timestamp of the export this response was served from. Buckets beyond this watermark are incomplete; for stable results, set `ending_at` to this value or earlier. Data is typically refreshed every 4 hours but not final until about 30 days after the usage date (late-arriving events, reconciliation adjustments).

has\_more: boolean

next\_page: string

organization\_id: string

ID of the Organization.

Get Cost Over Time



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/cost_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "amount": "amount",
          "context_window": "0-200k",
          "cost_type": "code_execution",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "speed": "fast",
          "token_type": "cache_creation.ephemeral_1h_input_tokens"
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "ending_at": "2019-12-27T18:11:19.117Z",
      "results": [
        {
          "amount": "amount",
          "context_window": "0-200k",
          "cost_type": "code_execution",
          "currency": "USD",
          "inference_geo": "global",
          "list_amount": "list_amount",
          "model": "model",
          "product": "product",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "speed": "fast",
          "token_type": "cache_creation.ephemeral_1h_input_tokens"
        }
      ],
      "starting_at": "2019-12-27T18:11:19.117Z"
    }
  ],
  "data_refreshed_at": "2019-12-27T18:11:19.117Z",
  "has_more": true,
  "next_page": "next_page",
  "organization_id": "org_013FP9SaFPBg7Kw7fetjn6cF"
}
```

---

*Copyright © Anthropic. All rights reserved.*
