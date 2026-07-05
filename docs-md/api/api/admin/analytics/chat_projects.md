# Chat Projects

Copy page



# Chat Projects

##### [Get Chat Project Usage](api/admin/analytics/chat_projects/list.md)

GET/v1/organizations/analytics/apps/chat/projects

##### ModelsExpand Collapse



ChatProjectUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/apps/chat/projects.



data: array of object { distinct\_user\_count, message\_count, project\_id, 8 more } 

distinct\_user\_count: number

Number of distinct users who used the project on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

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

distinct\_conversation\_count: optional number

Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

product: optional string

Product that produced this row's activity: one of chat, claude\_code, cowork, or office\_agent (the canonical Cost & Usage product naming; an office\_agent row's per-surface breakdown is in its office\_metrics). On /plugins only cowork and claude\_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group\_by[] or filter[] there is rejected). Present only when the request grouped by product.

rbac\_group\_id: optional string

Tagged RBAC group identifier (rbac\_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac\_group\_id.

rbac\_group\_name: optional string

Resolved RBAC group display name, alongside rbac\_group\_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac\_group\_id remains the stable key.

user\_id: optional string

Tagged user identifier (e.g. user\_...). Present only when the request grouped by user\_id.

next\_page: string

Opaque cursor for the next page, or null if no more results

---

*Copyright © Anthropic. All rights reserved.*
