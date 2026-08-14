# Artifacts

Copy page



# Artifacts

##### [Get Artifact Activity](api/admin/analytics/artifacts/list.md)

GET/v1/organizations/analytics/artifacts

##### ModelsExpand Collapse



ArtifactUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/artifacts.

`next_page` is null on ungrouped queries — the artifact-type cube is
finite and returned in full. Grouped queries (`group_by[]` on `user_id` /
`rbac_group_id`) multiply the cube and paginate like the other analytics
list endpoints.



data: array of object { artifact\_type, artifacts\_created\_count, distinct\_user\_count, 6 more } 

artifact\_type: string

Canonical artifact MIME type (e.g. text/markdown, application/vnd.ant.react, image/svg+xml), or 'other'.

artifacts\_created\_count: number

Number of artifacts created in this bucket on the requested day

distinct\_user\_count: number

Number of distinct users who created artifacts in this bucket on the requested day

is\_shared: boolean

Whether the artifacts in this bucket have ever been shared.

published\_artifacts\_created\_count: number

Number of those artifacts that have been published

product: optional string or null

Product that produced this row's activity: one of chat, claude\_code, cowork, or office\_agent (the canonical Cost & Usage product naming; an office\_agent row's per-surface breakdown is in its office\_metrics). On /plugins only cowork and claude\_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product `group_by[]` or `filter[]` there is rejected). Present only when the request grouped by product.

rbac\_group\_id: optional string or null

Tagged RBAC group identifier (`rbac_group_...`), matching the spend-limits API spelling. Present only when the request grouped by `rbac_group_id`.

rbac\_group\_name: optional string or null

Resolved RBAC group display name, alongside `rbac_group_id` when name resolution is available. Null if the group has been deleted or its name could not be resolved; `rbac_group_id` remains the stable key.

user\_id: optional string or null

Tagged user identifier (e.g. `user_...`). Present only when the request grouped by `user_id`.

next\_page: optional string or null

Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

---

*Copyright © Anthropic. All rights reserved.*
