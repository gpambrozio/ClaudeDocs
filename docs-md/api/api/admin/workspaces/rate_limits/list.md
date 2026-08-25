# List Workspace Rate Limits

Copy page



# List Workspace Rate Limits

GET/v1/organizations/workspaces/{workspace\_id}/rate\_limits

List rate-limit overrides configured for a workspace.

Returns only the groups and limiter types that have a workspace-level
override. Groups without overrides inherit the organization limits and
are not listed; use `GET /v1/organizations/rate_limits` to see those.

##### Path parameters

workspace\_id: string

The ID of the workspace.

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

page: optional string

Opaque cursor from a previous response's `next_page`.

##### Returns



data: array of object{ group\_type, limits, models, 3 more }

Rate-limit entries for the workspace, one per group that has at least one override.

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

limits: array of object{ org\_limit, type, value }

The limiter values overridden for this group in this workspace. Limiter types without a workspace override are omitted and inherit the organization value.

org\_limit: number or null

The organization-level value for the same limiter type, for reference. `null` when the organization has no limit configured for this limiter type.

type: string

The limiter type (for example, `requests_per_minute` or `input_tokens_per_minute`).

value: number

The workspace-level override value for this limiter type.

models: array of string or null

Model names this entry's limits apply to, including aliases. `null` when `group_type` is not `"model_group"`.

rate\_limit\_id: string

The `id` of the RateLimit group this override applies to.



type: "workspace\_rate\_limit"

Object type. Always `workspace_rate_limit` for workspace rate-limit entries.

defaultworkspace\_rate\_limit

workspace\_id: string

ID of the Workspace this override applies to.

next\_page: string or null

Token to provide in as `page` in the subsequent request to retrieve the next page of data.

### List Workspace Rate Limits

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/workspaces/$WORKSPACE_ID/rate_limits \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
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
      "group_type": "batch",
      "limits": [
        {
          "org_limit": 0,
          "type": "type",
          "value": 0
        }
      ],
      "models": [
        "string"
      ],
      "rate_limit_id": "rate_limit_id",
      "type": "workspace_rate_limit",
      "workspace_id": "workspace_id"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
