# Get Chat Project Usage

Copy page



# Get Chat Project Usage

GET/v1/organizations/analytics/apps/chat/projects

Get per-project activity for a given day, with cursor-based pagination.

Returns activity metrics for each project in the organization, sorted by
project ID. Available to organizations on a Claude Enterprise plan.
Requires an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse

date: string

UTC date in YYYY-MM-DD format. The day to get project activity for. Must be at least 3 days in the past (data is finalized with a 3-day lag) and no earlier than 2026-01-01.

limit: optional number

Number of results per page (1-1000, default 100).

page: optional string

Opaque cursor from a previous response's next\_page field.

##### ReturnsExpand Collapse



ChatProjectUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/apps/chat/projects.



data: array of object { distinct\_conversation\_count, distinct\_user\_count, message\_count, 4 more } 

distinct\_conversation\_count: number

Number of distinct conversations in the project on the requested day

distinct\_user\_count: number

Number of distinct users who used the project on the requested day

message\_count: number

Number of messages sent in the project on the requested day

project\_id: string

Tagged project identifier (e.g. claude\_proj\_...)

project\_name: string

Name of the project

created\_at: optional string

Project creation timestamp, RFC 3339. Null if the project was deleted before attribution was recorded.



created\_by: optional [AnalyticsUser](api/admin/analytics.md) { id, email\_address } 

User identifier.

id: string

Tagged user identifier (e.g. user\_...)

email\_address: string

Email address of the user

next\_page: string

Opaque cursor for the next page, or null if no more results

Get Chat Project Usage



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/apps/chat/projects \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "distinct_conversation_count": 0,
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
      }
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
      "distinct_conversation_count": 0,
      "distinct_user_count": 0,
      "message_count": 0,
      "project_id": "project_id",
      "project_name": "project_name",
      "created_at": "created_at",
      "created_by": {
        "id": "id",
        "email_address": "email_address"
      }
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
