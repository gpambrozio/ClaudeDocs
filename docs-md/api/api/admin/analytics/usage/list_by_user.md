# Get Per-User Token Usage

Copy page



# Get Per-User Token Usage

GET/v1/organizations/analytics/user\_usage\_report

Get per-user token usage across a date range.

Returns one row per user, ranked by the chosen token metric. Use this to
see which users consume the most tokens. Available to organizations on
a Claude Enterprise plan. Requires an API key with the `read:analytics`
scope.

##### Query ParametersExpand Collapse

starting\_at: string

Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00

.



bucket\_width: optional "1m" or "1h" or "1d"

Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

One of the following:

"1m"

"1h"

"1d"



context\_windows: optional array of "0-200k" or "200k-1M"

Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

One of the following:

"0-200k"

"200k-1M"

ending\_at: optional string

End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

exclude\_deleted\_users: optional boolean

If true, omit rows for deleted accounts. Pages may return fewer than `limit` rows when deleted users were filtered.



group\_by: optional array of "product" or "model" or "context\_window" or 2 more

Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/usage_report` endpoint. `limit` bounds (actor × time bucket × dimension) rows — with dimensions or `bucket_width` present, one actor may span several rows.

One of the following:

"product"

"model"

"context\_window"

"inference\_geo"

"speed"



inference\_geos: optional array of "global" or "us" or "not\_available"

Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

One of the following:

"global"

"us"

"not\_available"

limit: optional number

Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

models: optional array of string

Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.



order: optional "desc" or "asc"

Sort direction. Defaults to `desc`.

One of the following:

"desc"

"asc"



order\_by: optional "output\_tokens" or "uncached\_input\_tokens" or "total\_tokens" or "requests"

Metric to rank actors by. Defaults to `total_tokens`.

One of the following:

"output\_tokens"

"uncached\_input\_tokens"

"total\_tokens"

"requests"

page: optional string

Opaque cursor from a previous response's `next_page` field.

products: optional array of string

Product surfaces to include. Defaults to all products. Values include "chat", "claude\_code", "cowork", "office\_agent", "claude\_in\_chrome", and "claude\_design".

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

Get Per-User Token Usage



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/user_usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 500
      },
      "cache_read_input_tokens": 3200000,
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "model",
      "output_tokens": 891000,
      "product": "product",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "total_tokens": 5377000,
      "uncached_input_tokens": 1284500
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
      "actor": {
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt",
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 500
      },
      "cache_read_input_tokens": 3200000,
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "model",
      "output_tokens": 891000,
      "product": "product",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "speed": "fast",
      "starting_at": "2019-12-27T18:11:19.117Z",
      "total_tokens": 5377000,
      "uncached_input_tokens": 1284500
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
