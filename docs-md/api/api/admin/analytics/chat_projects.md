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

data: array of object { distinct\_user\_count, message\_count, project\_id, 4 more } 

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

distinct\_conversation\_count: optional number

Number of distinct conversations in the project. Null on aggregated rows where a distinct count cannot be computed.

next\_page: string

Opaque cursor for the next page, or null if no more results

---

*Copyright © Anthropic. All rights reserved.*
