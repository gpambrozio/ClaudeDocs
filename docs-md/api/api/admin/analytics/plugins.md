# Plugins

Copy page



# Plugins

##### [Get Plugin Usage](api/admin/analytics/plugins/list.md)

GET/v1/organizations/analytics/plugins

##### ModelsExpand Collapse



PluginUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/plugins.



data: array of object { claude\_code\_metrics, cowork\_metrics, distinct\_user\_count, 8 more } 



claude\_code\_metrics: object { distinct\_session\_plugin\_used\_count } 

Claude Code activity metrics for a single plugin on a given day.

distinct\_session\_plugin\_used\_count: number

Number of distinct Claude Code sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.



cowork\_metrics: object { distinct\_session\_plugin\_used\_count } 

Cowork activity metrics for a single plugin on a given day.

distinct\_session\_plugin\_used\_count: number

Number of distinct Cowork sessions in which the plugin was invoked. Null on aggregated rows where a distinct count cannot be computed.

distinct\_user\_count: number

Number of distinct users with recorded install or invocation activity for the plugin on the requested day (install-only users count), or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

install\_count: number

Number of distinct users who installed the plugin on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.

invocation\_count: number

Number of plugin invocations on the requested day

plugin\_name: string

Name of the plugin

plugin\_id: optional string

Stable plugin identifier when available (e.g. serena@claude-plugins-official). Null for third-party Claude Code plugins (redacted at the source) and Cowork slash commands that carry only a hashed id.

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
