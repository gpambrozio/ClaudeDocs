# Get Messages Usage Report

Copy page



# Get Messages Usage Report

GET/v1/organizations/usage\_report/messages

Get Messages Usage Report

##### Query parameters



starting\_at: string

Time buckets that start on or after this RFC 3339 timestamp will be returned.
Each time bucket will be snapped to the start of the minute/hour/day in UTC.

formatdate-time

account\_ids: optional array of string

Restrict usage returned to the specified user account ID(s).

api\_key\_ids: optional array of string

Restrict usage returned to the specified API key ID(s).



bucket\_width: optional "1d" or "1h" or "1m"

Time granularity of the response data.

default1d

One of the following:

"1d"

"1h"

"1m"



context\_window: optional array of "0-200k" or "200k-1M"

Restrict usage returned to the specified context window(s).

One of the following:

"0-200k"

"200k-1M"



ending\_at: optional string

Time buckets that end before this RFC 3339 timestamp will be returned.

formatdate-time



group\_by: optional array of "account\_id" or "api\_key\_id" or "context\_window" or 6 more

Group by any subset of the available options. Grouping by `speed` requires the `fast-mode-2026-02-01` beta header.

One of the following:

"account\_id"

"api\_key\_id"

"context\_window"

"inference\_geo"

"model"

"service\_account\_id"

"service\_tier"

"speed"

"workspace\_id"



inference\_geos: optional array of "global" or "not\_available" or "us"

Restrict usage returned to the specified inference geo(s). Use `not_available` for models that do not support specifying `inference_geo`.

One of the following:

"global"

"not\_available"

"us"



limit: optional number

Maximum number of time buckets to return in the response.

The default and max limits depend on `bucket_width`:
• `"1d"`: Default of 7 days, maximum of 31 days
• `"1h"`: Default of 24 hours, maximum of 168 hours
• `"1m"`: Default of 60 minutes, maximum of 1440 minutes

models: optional array of string

Restrict usage returned to the specified model(s).

page: optional string

Optionally set to the `next_page` token from the previous response.

service\_account\_ids: optional array of string

Restrict usage returned to the specified service account ID(s).



service\_tiers: optional array of "batch" or "flex" or "flex\_discount" or 3 more

Restrict usage returned to the specified service tier(s).

One of the following:

"batch"

"flex"

"flex\_discount"

"priority"

"priority\_on\_demand"

"standard"



speeds: optional array of "fast" or "standard"

Restrict usage returned to the specified speed(s) (Claude Code research preview).
Requires the `fast-mode-2026-02-01` beta header.

One of the following:

"fast"

"standard"

workspace\_ids: optional array of string

Restrict usage returned to the specified workspace ID(s).

##### Headers



"anthropic-beta": optional array of string

Optional header to specify the beta version(s) you want to use.

To use multiple betas, use a comma separated list like `beta1,beta2` or specify the header multiple times for each beta.

##### Returns



MessagesUsageReport object{ data, has\_more, next\_page }

Get Messages Usage Report

cURL

```shiki
curl https://api.anthropic.com/v1/organizations/usage_report/messages \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-5",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "ending_at": "2025-08-02T00:00:00Z",
      "results": [
        {
          "account_id": "user_01WCz1FkmYMm4gnmykNKUu3Q",
          "api_key_id": "apikey_01Rj2N8SVvo6BePZj99NhmiT",
          "cache_creation": {
            "ephemeral_1h_input_tokens": 1000,
            "ephemeral_5m_input_tokens": 500
          },
          "cache_read_input_tokens": 200,
          "context_window": "0-200k",
          "inference_geo": "global",
          "model": "claude-opus-5",
          "output_tokens": 500,
          "server_tool_use": {
            "web_search_requests": 10
          },
          "service_account_id": "svac_01Hk3R9TWxq7CfQak00OiVw4",
          "service_tier": "standard",
          "uncached_input_tokens": 1500,
          "workspace_id": "wrkspc_01JwQvzr7rXLA5AGx3HKfFUJ"
        }
      ],
      "starting_at": "2025-08-01T00:00:00Z"
    }
  ],
  "has_more": true,
  "next_page": "page_MjAyNS0wNS0xNFQwMDowMDowMFo="
}
```

---

*Copyright © Anthropic. All rights reserved.*
