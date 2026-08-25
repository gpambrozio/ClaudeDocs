# Artifacts

Copy page



# Artifacts

##### [Get Artifact Activity](api/http/admin/analytics/artifacts/list.md)

GET/v1/organizations/analytics/artifacts

##### Models



ArtifactUsage object{ data, next\_page }

Response for GET /v1/organizations/analytics/artifacts.

`next_page` is null on ungrouped queries — the artifact-type cube is
finite and returned in full. Grouped queries (`group_by[]` on `user_id` /
`rbac_group_id`) multiply the cube and paginate like the other analytics
list endpoints.

---

*Copyright © Anthropic. All rights reserved.*
