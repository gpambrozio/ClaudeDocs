# Users

Copy page



# Users

##### [List User Activity](api/admin/analytics/users/list.md)

GET/v1/organizations/analytics/users

##### ModelsExpand Collapse



UserActivity object { data, next\_page } 

Response for GET /v1/organizations/analytics/users.



data: array of object { chat\_metrics, claude\_code\_metrics, cowork\_metrics, 4 more } 



chat\_metrics: object { connectors\_used\_count, distinct\_artifacts\_created\_count, distinct\_conversation\_count, 8 more } 

Claude.ai activity metrics for a single user on a given day.

connectors\_used\_count: number

Number of MCP connectors used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_artifacts\_created\_count: number

Number of distinct artifacts created

distinct\_conversation\_count: number

Number of distinct conversations the user participated in. Null on aggregated rows where a distinct count cannot be computed.

distinct\_files\_uploaded\_count: number

Number of distinct files uploaded. Null on aggregated rows where a distinct count cannot be computed.

distinct\_projects\_created\_count: number

Number of distinct projects created

distinct\_projects\_used\_count: number

Number of distinct projects used. Null on aggregated rows where a distinct count cannot be computed.

distinct\_shared\_artifacts\_viewed\_count: number

Number of distinct shared artifacts the user viewed. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

shared\_conversations\_viewed\_count: number

Number of times the user opened a shared conversation in a project

thinking\_message\_count: number

Number of messages that used extended thinking



claude\_code\_metrics: object { core\_metrics, tool\_actions } 

Claude Code activity metrics for a single user on a given day.



core\_metrics: object { commit\_count, distinct\_session\_count, lines\_of\_code, pull\_request\_count } 

Core Claude Code activity metrics for a single user on a given day.

commit\_count: number

Number of commits made via Claude Code

distinct\_session\_count: number

Number of distinct Claude Code sessions. Null on aggregated rows where a distinct count cannot be computed.



lines\_of\_code: object { added\_count, removed\_count } 

Lines of code added and removed via Claude Code.

added\_count: number

Lines of code added

removed\_count: number

Lines of code removed

pull\_request\_count: number

Number of pull requests created via Claude Code



tool\_actions: object { edit\_tool, multi\_edit\_tool, notebook\_edit\_tool, write\_tool } 

Per-tool accepted/rejected counts for Claude Code file modification tools.



edit\_tool: [ToolActionCounts](api/admin.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



multi\_edit\_tool: [ToolActionCounts](api/admin.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



notebook\_edit\_tool: [ToolActionCounts](api/admin.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



write\_tool: [ToolActionCounts](api/admin.md) { accepted\_count, rejected\_count } 

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected



cowork\_metrics: object { action\_count, connectors\_used\_count, dispatch\_turn\_count, 5 more } 

Cowork activity metrics for a single user on a given day.

action\_count: number

Number of tool actions completed in Cowork sessions

connectors\_used\_count: number

Total number of connector invocations in Cowork sessions

dispatch\_turn\_count: number

Number of Dispatch (background agent) turns completed

distinct\_connectors\_used\_count: number

Number of distinct connectors used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number

Number of distinct skills used in Cowork sessions. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Cowork sessions

skills\_used\_count: number

Total number of skill invocations in Cowork sessions



design\_metrics: object { distinct\_projects\_created\_count, distinct\_projects\_used\_count, distinct\_session\_count, message\_count } 

Claude Design activity metrics for a single user on a given day.

distinct\_projects\_created\_count: number

Number of distinct Claude Design projects created

distinct\_projects\_used\_count: number

Number of distinct Claude Design projects the user worked in. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number

Number of distinct Claude Design sessions. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent in Claude Design sessions



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single user on a given day, broken out by Office product.



excel: [OfficeProductMetrics](api/admin.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

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

outlook: [OfficeProductMetrics](api/admin.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

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

powerpoint: [OfficeProductMetrics](api/admin.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

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

word: [OfficeProductMetrics](api/admin.md) { connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more } 

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

web\_search\_count: number

Number of web searches performed



user: optional [AnalyticsUser](api/admin.md) { id, email\_address } 

User identifier.

id: string

Tagged user identifier (e.g. user\_...)

email\_address: string

Email address of the user

next\_page: string

Opaque cursor for the next page, or null if no more results

---

*Copyright © Anthropic. All rights reserved.*
