# Connectors

Copy page



# Connectors

##### [Get Connector Usage](api/admin/analytics/connectors/list.md)

GET/v1/organizations/analytics/connectors

##### ModelsExpand Collapse



ConnectorUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/connectors.



data: array of object { chat\_metrics, claude\_code\_metrics, connector\_name, 10 more } 



chat\_metrics: object { distinct\_conversation\_connector\_used\_count } 

Claude.ai activity metrics for a single connector on a given day.

distinct\_conversation\_connector\_used\_count: number

Number of distinct conversations in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



claude\_code\_metrics: object { distinct\_session\_connector\_used\_count } 

Claude Code activity metrics for a single connector on a given day.

distinct\_session\_connector\_used\_count: number

Number of distinct Claude Code sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

connector\_name: string

Name of the connector



cowork\_metrics: object { distinct\_session\_connector\_used\_count } 

Cowork activity metrics for a single connector on a given day.

distinct\_session\_connector\_used\_count: number

Number of distinct Cowork sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

distinct\_user\_count: number

Number of distinct users who used the connector on the requested day, or, in date-range mode, over the requested window — recomputed as an exact distinct count over the window's per-member daily rows, never a sum of per-day values.



office\_metrics: object { excel, outlook, powerpoint, word } 

Office Agent activity metrics for a single connector on a given day, broken out by Office product.



excel: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



outlook: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



powerpoint: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.



word: [ConnectorOfficeProductMetrics](api/admin/analytics.md) { distinct\_session\_connector\_used\_count } 

Office Agent activity metrics for a single connector on a given day within one Office product.

distinct\_session\_connector\_used\_count: number

Number of distinct Office Agent sessions in which the connector was used. Approximate (HLL, typical error <2%) in date-range mode. Null on aggregated rows where a distinct count cannot be computed.

product: optional string

Product that produced this row's activity: one of chat, claude\_code, cowork, or office\_agent (the canonical Cost & Usage product naming; an office\_agent row's per-surface breakdown is in its office\_metrics). On /plugins only cowork and claude\_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group\_by[] or filter[] there is rejected). Present only when the request grouped by product.

rbac\_group\_id: optional string

Tagged RBAC group identifier (rbac\_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac\_group\_id.

rbac\_group\_name: optional string

Resolved RBAC group display name, alongside rbac\_group\_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac\_group\_id remains the stable key.

read\_call\_count: optional number

Number of connector tool calls on the requested day whose trusted read-only annotation marked them read-only. Call count, not distinct users. Every call recorded on a classified surface lands in exactly one of read\_call\_count, write\_call\_count, or unclassified\_call\_count, so the three sum to the day's classified calls. Classification is forward-only per surface: claude.ai from 2026-06-01, Claude Code from 2026-05-30, Claude in Office from 2026-05-29, Cowork from 2026-06-02 (Cowork clients predating annotation forwarding land in unclassified\_call\_count). Null, never 0, when the value cannot be stated: the read/write split is not enabled for this organization, or the day predates 2026-05-29. For a date-range total, sum the per-day values, but treat a window that extends before 2026-05-29 as null rather than summing only its covered days — date-range rollup mode (starting\_date/ending\_date) applies both rules server-side.

unclassified\_call\_count: optional number

Number of connector tool calls on the requested day with no trusted read-only annotation — the annotation is optional in the MCP spec and is discarded when connector access controls are active, so unclassified calls are common. This field shows how much of the day's classified activity the read/write split actually covers. Call count, not distinct users. One of the three call-classification buckets; see read\_call\_count for the per-surface data-start dates, null conditions, and date-range guidance.

user\_id: optional string

Tagged user identifier (e.g. user\_...). Present only when the request grouped by user\_id.

write\_call\_count: optional number

Number of connector tool calls on the requested day whose trusted read-only annotation marked them not read-only. Call count, not distinct users. One of the three call-classification buckets; see read\_call\_count for the per-surface data-start dates, null conditions, and date-range guidance.

next\_page: string

Opaque cursor for the next page, or null if no more results

---

*Copyright © Anthropic. All rights reserved.*
