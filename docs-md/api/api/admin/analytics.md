# Analytics

Copy page



# Analytics

##### [Get Activity Summaries](api/http/admin/analytics/retrieve_summaries.md)

GET/v1/organizations/analytics/summaries

##### Models



ActivitySummary object{ summaries }

Response for GET /v1/organizations/analytics/summaries.



AnalyticsUser object{ id, email\_address, type }

A user in the organization, identified by tagged id and email address.

id: string

Tagged user identifier (e.g. `user_...`)

email\_address: string

Email address of the user



type: "user"

Object type. Always `user`.

defaultuser



AnalyticsUserActor object{ deleted, email, name, 2 more }

deleted: boolean

True when the account has been deleted, or when the user is no longer a member of the organization or its associated organizations (for example, their membership was removed or they were deprovisioned via your identity provider). `email` stays populated for removed users and is null when the account has been deleted. `name` follows the rules described on that field. The `user_id` is still populated for reconciliation.

email: string or null

The user's email address, including for users who are no longer members of the organization or its associated organizations. Null when the account has been deleted (check `deleted`) and for system-minted service accounts, which have no person's mailbox behind them (check `name`).

name: string or null

The user's full name. Null when the user has not set a name. Returns `"Deleted User"` when the account itself has been deleted, or when the user is no longer a member of the organization or its associated organizations and the organization has chosen to hide the names of removed users. Otherwise, the name stays populated for removed users. Rows for system-minted service accounts render the service name (for example, `"Claude Security"` for usage by Anthropic's security-patching service) or null.

type: "user\_actor"

Actor type. Always `"user_actor"`.

user\_id: string

Tagged user ID.



ConnectorOfficeProductMetrics object{ distinct\_session\_connector\_used\_count }

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number or null

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



OfficeProductMetrics object{ connectors\_used\_count, distinct\_connectors\_used\_count, distinct\_session\_count, 3 more }

Office Agent activity metrics for a single user on a given day within one Office product.

connectors\_used\_count: number

Number of MCP connector invocations

distinct\_connectors\_used\_count: number or null

Number of distinct MCP connectors used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_session\_count: number or null

Number of distinct Office Agent sessions. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_skills\_used\_count: number or null

Number of distinct skills used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

message\_count: number

Number of messages sent

skills\_used\_count: number

Number of skill invocations



SkillOfficeProductMetrics object{ distinct\_session\_skill\_used\_count }

Office Agent activity metrics for a single skill on a given day within one Office product.

distinct\_session\_skill\_used\_count: number or null

Number of distinct Office Agent sessions in which the skill was used. A skill counts as used only when it is explicitly activated — the model (or the user, via the skill's slash command) invokes it, reading its instructions into context as part of that activation. Skills that are merely installed or listed as available, or whose content reaches the context without an activation (preloaded, hook-injected, or read as a plain file), are not counted. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



ToolActionCounts object{ accepted\_count, rejected\_count }

Accepted/rejected counts for a single Claude Code tool type.

accepted\_count: number

Number of tool proposals accepted

rejected\_count: number

Number of tool proposals rejected

#### Analytics[Usage](api/http/admin/analytics/usage.md)

##### [Get Token Usage Over Time](api/http/admin/analytics/usage/list.md)

GET/v1/organizations/analytics/usage\_report

##### [Get Per-User Token Usage](api/http/admin/analytics/usage/list_by_user.md)

GET/v1/organizations/analytics/user\_usage\_report

#### Analytics[Cost](api/http/admin/analytics/cost.md)

##### [Get Cost Over Time](api/http/admin/analytics/cost/list.md)

GET/v1/organizations/analytics/cost\_report

##### [Get Per-User Cost](api/http/admin/analytics/cost/list_by_user.md)

GET/v1/organizations/analytics/user\_cost\_report

#### Analytics[Users](api/http/admin/analytics/users.md)

##### [List User Activity](api/http/admin/analytics/users/list.md)

GET/v1/organizations/analytics/users

#### Analytics[Skills](api/http/admin/analytics/skills.md)

##### [Get Skill Usage](api/http/admin/analytics/skills/list.md)

GET/v1/organizations/analytics/skills

#### Analytics[Connectors](api/http/admin/analytics/connectors.md)

##### [Get Connector Usage](api/http/admin/analytics/connectors/list.md)

GET/v1/organizations/analytics/connectors

#### Analytics[Chat Projects](api/http/admin/analytics/chat_projects.md)

##### [Get Chat Project Usage](api/http/admin/analytics/chat_projects/list.md)

GET/v1/organizations/analytics/apps/chat/projects

#### Analytics[Plugins](api/http/admin/analytics/plugins.md)

##### [Get Plugin Usage](api/http/admin/analytics/plugins/list.md)

GET/v1/organizations/analytics/plugins

#### Analytics[Artifacts](api/http/admin/analytics/artifacts.md)

##### [Get Artifact Activity](api/http/admin/analytics/artifacts/list.md)

GET/v1/organizations/analytics/artifacts

---

*Copyright © Anthropic. All rights reserved.*
