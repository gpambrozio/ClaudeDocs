# Analytics

Copy page



# Analytics

##### [Get Activity Summaries](api/admin/analytics/retrieve_summaries.md)

GET/v1/organizations/analytics/summaries

##### ModelsExpand Collapse



ActivitySummary object { summaries } 

Response for GET /v1/organizations/analytics/summaries.



summaries: array of object { assigned\_seat\_count, cowork\_daily\_active\_user\_count, cowork\_monthly\_active\_user\_count, 10 more } 

assigned\_seat\_count: number

Number of seats currently assigned to members. Null when the response is scoped to an RBAC group — seat assignment is org-wide and has no per-group analogue.

cowork\_daily\_active\_user\_count: number

Number of users with Cowork activity on the requested day

cowork\_monthly\_active\_user\_count: number

Number of users with Cowork activity in the 30-day rolling window

cowork\_weekly\_active\_user\_count: number

Number of users with Cowork activity in the 7-day rolling window

daily\_active\_user\_count: number

Number of users with token consumption on the requested day

daily\_adoption\_rate: number

Percentage of assigned seats with activity on the requested day (DAU / assigned\_seat\_count \* 100). Null when the response is scoped to an RBAC group.

ending\_at: string

End time in UTC of aggregation period (e.g. 2026-01-16T00:00

)

monthly\_active\_user\_count: number

Number of users with token consumption in the 30-day rolling window

monthly\_adoption\_rate: number

Percentage of assigned seats with activity in the 30-day rolling window (MAU / assigned\_seat\_count \* 100). Null when the response is scoped to an RBAC group.

pending\_invite\_count: number

Number of pending invitations to join the organization. Null when the response is scoped to an RBAC group.

starting\_at: string

Start time in UTC of aggregation period (e.g. 2026-01-15T00:00

)

weekly\_active\_user\_count: number

Number of users with token consumption in the 7-day rolling window

weekly\_adoption\_rate: number

Percentage of assigned seats with activity in the 7-day rolling window (WAU / assigned\_seat\_count \* 100). Null when the response is scoped to an RBAC group.



AnalyticsUser object { id, email\_address } 

User identifier.

id: string

Tagged user identifier (e.g. user\_...)

email\_address: string

Email address of the user



AnalyticsUserActor object { user\_id, deleted, email, 2 more } 

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

ConnectorOfficeProductMetrics object { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Null on aggregated rows where a distinct count cannot be computed.



OfficeProductMetrics object { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number

Number of distinct MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Office Agent sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



SkillOfficeProductMetrics object { distinct\_session\_skill\_used\_count } 

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number

Number of distinct Office Agent sessions in which the skill was used. Null on aggregated rows where a distinct count cannot be computed.



ToolActionCounts object { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected

#### AnalyticsUsage

##### [Get Token Usage Over Time](api/admin/analytics/usage/list.md)

GET/v1/organizations/analytics/usage\_report

##### [Get Per-User Token Usage](api/admin/analytics/usage/list_by_user.md)

GET/v1/organizations/analytics/user\_usage\_report

#### AnalyticsCost

##### [Get Cost Over Time](api/admin/analytics/cost/list.md)

GET/v1/organizations/analytics/cost\_report

##### [Get Per-User Cost](api/admin/analytics/cost/list_by_user.md)

GET/v1/organizations/analytics/user\_cost\_report

#### AnalyticsUsers

##### [List User Activity](api/admin/analytics/users/list.md)

GET/v1/organizations/analytics/users

#### AnalyticsSkills

##### [Get Skill Usage](api/admin/analytics/skills/list.md)

GET/v1/organizations/analytics/skills

#### AnalyticsConnectors

##### [Get Connector Usage](api/admin/analytics/connectors/list.md)

GET/v1/organizations/analytics/connectors

#### AnalyticsChat Projects

##### [Get Chat Project Usage](api/admin/analytics/chat_projects/list.md)

GET/v1/organizations/analytics/apps/chat/projects

---

*Copyright © Anthropic. All rights reserved.*
