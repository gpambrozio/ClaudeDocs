# List Organization Rate Limits

Copy page

# List Organization Rate Limits

GET/v1/organizations/rate\_limits

List Messages API rate limits for your organization.

Each entry corresponds to one rate-limit group (either a model family
or an API-surface category such as the Files API or Message Batches)
and contains the set of limiter values that apply to it.

##### Query ParametersExpand Collapse



group\_type: optional "model\_group" or "batch" or "token\_count" or 3 more

Filter by group type.

One of the following:

"model\_group"

"batch"

"token\_count"

"files"

"skills"

"web\_search"

model: optional string

Filter to the single entry containing this model. Accepts full model names and aliases. Returns 404 if the model is not found or has no rate limits for this organization.

page: optional string

Opaque cursor from a previous response's `next_page`.

##### ReturnsExpand Collapse

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

List Organization Rate Limits



```shiki
curl https://api.anthropic.com/v1/organizations/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "group_type": "model_group",
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
      "group_type": "model_group",
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
