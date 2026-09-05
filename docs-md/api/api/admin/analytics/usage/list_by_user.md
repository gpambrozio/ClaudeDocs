# Get Per-User Token Usage

Copy page



# Get Per-User Token Usage

GET/v1/organizations/analytics/user\_usage\_report

Get per-user token usage across a date range.

Returns one row per user, ranked by the chosen token metric. Use this to
see which users consume the most tokens. Only usage attributable to a
seat user is included; for organization-wide totals including direct
API-key and automation traffic, use the bucketed
`/v1/organizations/analytics/usage_report` endpoint. Available to
organizations on a Claude Enterprise plan. Requires an API key with the
`read:analytics` scope.

##### Query parameters



starting\_at: string

Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

formatdate-time



bucket\_width: optional "1d" or "1h" or "1m"

Time-bucket granularity. When set, each row's `starting_at` and `ending_at` are populated and one actor may span several rows (one per time bucket with usage). The time bucket counts toward `limit`, so one page can return multiple rows for the same actor. `ending_at` is required when `bucket_width` is set, and with `bucket_width="1m"` the range may span at most 24 hours. When omitted, each row aggregates the full `[starting_at, ending_at)` range.

One of the following:

"1d"

"1h"

"1m"



claude\_tag\_categories: optional array of "dm" or "engaged" or "monitoring" or 2 more

Filter to Claude Tag (Claude in Slack) usage in specific spend categories. Usage with no category never matches. `dm` usage is reported under the user's product rather than `claude-tag`, so combining this filter with `products[]=claude-tag` excludes it. Use `group_by[]=claude_tag_category` to break out per-category values.

maxItems100

One of the following:

"dm"

"engaged"

"monitoring"

"proactive"

"scheduled"



claude\_tag\_user\_ids: optional array of string

Filter to Claude Tag (Claude in Slack) usage attributed to specific Slack users, by Slack user ID (for example `U0123ABCDEF`), not claude.ai user ID. Usage that is not Claude Tag, and Claude Tag usage not attributed to a single user, never matches. Use `group_by[]=claude_tag_user_id` to break out per-user values.

maxItems100



context\_windows: optional array of "0-200k" or "200k-1M"

Filter to specific context-window pricing tiers. Use `group_by[]=context_window` to break out per-tier values.

maxItems100

One of the following:

"0-200k"

"200k-1M"



ending\_at: optional string

End of range, exclusive. When omitted, defaults to the earlier of now and `starting_at` + 31 days. The range may span at most 31 days.

formatdate-time



exclude\_deleted\_users: optional boolean

If true, omit rows for users who are deleted (`deleted: true`). A page may contain fewer than `limit` rows; use `has_more` and `next_page` to paginate as usual.

defaultfalse



group\_by: optional array of "claude\_tag\_category" or "claude\_tag\_user\_id" or "context\_window" or 6 more

Break each actor's row out by the given dimensions. Accepts the same values as the bucketed `/usage_report` endpoint. `limit` bounds (actor × time bucket × dimension) rows — with dimensions or `bucket_width` present, one actor may span several rows.

maxItems100

One of the following:

"claude\_tag\_category"

"claude\_tag\_user\_id"

"context\_window"

"inference\_geo"

"model"

"product"

"rbac\_group\_id"

"slack\_channel\_id"

"speed"



inference\_geos: optional array of "global" or "not\_available" or "us"

Filter to specific inference regions. `not_available` matches rows where the region is unset. Use `group_by[]=inference_geo` to break out per-region values.

maxItems100

One of the following:

"global"

"not\_available"

"us"



limit: optional number

Number of rows per page (1-1000, default 20). One row per actor unless `group_by[]` or `bucket_width` splits an actor across rows; `cost_type`/`token_type` fan-out rows (cost endpoint only) are the exception — they do not count toward this limit, so `data` can exceed it.

default20

maximum1000

minimum1



models: optional array of string

Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

maxItems100



order: optional "asc" or "desc"

Sort direction. Defaults to `desc`.

defaultdesc

One of the following:

"asc"

"desc"



order\_by: optional "output\_tokens" or "requests" or "total\_tokens" or "uncached\_input\_tokens"

Metric to rank actors by. Defaults to `total_tokens`.

defaulttotal\_tokens

One of the following:

"output\_tokens"

"requests"

"total\_tokens"

"uncached\_input\_tokens"

page: optional string

Opaque cursor from a previous response's `next_page` field.



products: optional array of "chat" or "claude-tag" or "claude\_code" or 4 more

Product surfaces to include. Defaults to all products.

maxItems100

One of the following:

"chat"

"claude-tag"

"claude\_code"

"claude\_design"

"claude\_in\_chrome"

"cowork"

"office\_agent"



rbac\_group\_ids: optional array of string

Filter to usage attributed to specific RBAC groups. Accepts tagged RBAC group IDs (`rbac_group_...`) or bare group UUIDs. A row matches when the user belonged to any of the listed groups on the (UTC) day the usage occurred; usage with no group attribution never matches.

maxItems100



slack\_channel\_ids: optional array of string

Filter to usage originating from specific Slack channels. Use `group_by[]=slack_channel_id` to break out per-channel values.

maxItems100



speeds: optional array of "fast" or "standard"

Filter to fast or standard inference mode. Use `group_by[]=speed` to break out per-mode values.

maxItems100

One of the following:

"fast"

"standard"



user\_ids: optional array of string

Filter to specific users by tagged user ID.

maxItems100

##### Returns



UserUsage object{ data, data\_refreshed\_at, has\_more, 2 more }

Get Per-User Token Usage

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/analytics/user_usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "actor": {
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor",
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 500
      },
      "cache_read_input_tokens": 3200000,
      "claude_tag_category": "dm",
      "claude_tag_user_id": "U0123ABCDEF",
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "claude-opus-5",
      "output_tokens": 891000,
      "product": "chat",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "slack_channel_id": "C0123ABCDEF",
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
        "deleted": true,
        "email": "jane@example.com",
        "name": "Jane Smith",
        "type": "user_actor",
        "user_id": "user_01AbCdEfGhIjKlMnOpQrSt"
      },
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 500
      },
      "cache_read_input_tokens": 3200000,
      "claude_tag_category": "dm",
      "claude_tag_user_id": "U0123ABCDEF",
      "context_window": "0-200k",
      "ending_at": "2019-12-27T18:11:19.117Z",
      "inference_geo": "global",
      "model": "claude-opus-5",
      "output_tokens": 891000,
      "product": "chat",
      "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
      "requests": 128,
      "server_tool_use": {
        "web_search_requests": 10
      },
      "slack_channel_id": "C0123ABCDEF",
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
