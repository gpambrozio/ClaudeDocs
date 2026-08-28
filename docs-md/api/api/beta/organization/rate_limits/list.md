# List Organization Rate Limits

Copy page



cURL

# List Organization Rate Limits

GET/v1/organizations/rate\_limits

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

When `limit` is omitted, every matching entry is returned in a single
page; when `limit` truncates the result, follow `next_page` to fetch
the remaining entries.

##### Query parameters



group\_type: optional "batch" or "files" or "model\_group" or 3 more

Filter by group type.

One of the following:

"batch"

"files"

"model\_group"

"skills"

"token\_count"

"web\_search"



limit: optional number

Maximum number of items to return per page. Ranges from `1` to `1000`.

When omitted, every remaining entry is returned in a single page and `next_page` is `null`.

maximum1000

minimum1

model: optional string

Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

page: optional string

Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of [BetaOrganizationRateLimit](api/http/beta/organization/rate_limits.md) { id, group\_type, limits, 2 more }

Rate-limit entries for the organization, one per group.

id: string

Stable identifier for this rate-limit group within the organization.



group\_type: "batch" or "files" or "model\_group" or 3 more

The kind of rate-limit group this entry represents. `model_group` entries apply to a family of models (listed in `models`); other values apply to an API-surface category and have `models` set to `null`.

One of the following:

"batch"

"files"

"model\_group"

"skills"

"token\_count"

"web\_search"



limits: array of [BetaOrganizationRateLimitValue](api/http/beta/organization/rate_limits.md) { type, value }

The limiter values that apply to this group.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The configured limit value for this limiter type.

models: array of string or null

Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.



type: "rate\_limit"

Object type. Always `rate_limit` for organization rate-limit entries.

defaultrate\_limit

next\_page: string or null

Opaque cursor for the next page of results, or `null` when no entries remain beyond this response.



### List Organization Rate Limits

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "group_type": "batch",
      "limits": [
        {
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
    }
  ],
  "next_page": "next_page"
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "group_type": "batch",
      "limits": [
        {
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "type": "rate_limit"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
