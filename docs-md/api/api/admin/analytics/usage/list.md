# Get Token Usage Over Time

Copy page



# Get Token Usage Over Time

GET/v1/organizations/analytics/usage\_report

Get token usage over time across a date range.

Returns token usage bucketed by minute, hour, or day, optionally broken
down by product, model, context window, inference region, or speed.
Available to organizations on a Claude Enterprise plan. Requires an API
key with the `read:analytics` scope.

##### Query parameters



starting\_at: string

Start of range, inclusive. RFC 3339 tz-aware. Must be within the last 365 days and no earlier than 2026-01-01T00:00:00Z.

formatdate-time



bucket\_width: optional "1d" or "1h" or "1m"

Time bucket granularity.

default1d

One of the following:

"1d"

"1h"

"1m"

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

group\_by: optional array of "context\_window" or "inference\_geo" or "model" or 4 more

Dimensions to break each time bucket out by. Defaults to no grouping (one total per bucket). Each bucket reports at most its top 100 groups; a group beyond that cap has no row in that bucket (there is no remainder row), so grouped buckets are not exhaustive when a dimension has more than 100 distinct values.

maxItems100

One of the following:

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

Maximum number of time buckets per page. Defaults and caps vary by `bucket_width` (`1d`: default 7, max 31; `1h`: default 24, max 168; `1m`: default 60, max 256).

minimum1



models: optional array of string

Models to include. Defaults to all models. Use `group_by[]=model` to break out per-model values.

maxItems100

page: optional string

Opaque cursor from a previous response's `next_page` field.



products: optional array of "chat" or "claude-tag" or "claude\_code" or 4 more

Product surfaces to include. Defaults to all products. Use `group_by[]=product` to break out per-product values.

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

UsageBucket object{ data, data\_refreshed\_at, has\_more, 2 more }

Get Token Usage Over Time

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/analytics/usage_report \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 0,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-5",
          "output_tokens": 0,
          "product": "chat",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "slack_channel_id": "C0123ABCDEF",
          "speed": "fast",
          "uncached_input_tokens": 0
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
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 0,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-5",
          "output_tokens": 0,
          "product": "chat",
          "rbac_group_id": "rbac_group_012rppKaSVsmTo6NqRDXQXNF",
          "requests": 0,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "slack_channel_id": "C0123ABCDEF",
          "speed": "fast",
          "uncached_input_tokens": 0
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
