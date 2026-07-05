# Get Artifact Activity

Copy page



# Get Artifact Activity

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.

Returns the full (artifact\_type, is\_shared) cube for the organization;
`next_page` is null except for grouped queries, which paginate. Requires
an API key with the `read:analytics` scope.

##### Query ParametersExpand Collapse

date: string

UTC date in YYYY-MM-DD format. The day to get artifact activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

filter: optional array of string

Filters as 'dimension

', e.g. filter[]=rbac\_group\_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Unsupported dimensions return 400. rbac\_group\_id accepts the tagged id (rbac\_group\_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution). At most 100 entries.

group\_by: optional array of string

Dimensions to break results out by: user\_id and/or rbac\_group\_id. The ungrouped artifact-type cube is finite and returned in full; grouped queries multiply the cube and paginate via next\_page. rbac\_group\_id attributes a user to every group they held at any point during the requested UTC day, so grouped rows are not an exclusive partition. At most 100 entries.

limit: optional number

Maximum rows to return (1-1000, default 100). The ungrouped artifact-type cube is finite and returned in full; limit is the page size only when group\_by[] multiplies the cube.

page: optional string

Opaque cursor from a previous response's next\_page field. Only valid with group\_by[] — the ungrouped cube is never paginated.

##### ReturnsExpand Collapse



ArtifactUsage object { data, next\_page } 

Response for GET /v1/organizations/analytics/artifacts.

`next_page` is null on ungrouped queries — the artifact-type cube is
finite and returned in full. Grouped queries (group\_by[] on user\_id /
rbac\_group\_id) multiply the cube and paginate like the other analytics
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

product: optional string

Product that produced this row's activity: one of chat, claude\_code, cowork, or office\_agent (the canonical Cost & Usage product naming; an office\_agent row's per-surface breakdown is in its office\_metrics). On /plugins only cowork and claude\_code occur (the only surfaces with plugin attribution); /artifacts and /apps/chat/projects do not support the product dimension (a product group\_by[] or filter[] there is rejected). Present only when the request grouped by product.

rbac\_group\_id: optional string

Tagged RBAC group identifier (rbac\_group\_...), matching the spend-limits API spelling. Present only when the request grouped by rbac\_group\_id.

rbac\_group\_name: optional string

Resolved RBAC group display name, alongside rbac\_group\_id when name resolution is available. Null if the group has been deleted or its name could not be resolved; rbac\_group\_id remains the stable key.

user\_id: optional string

Tagged user identifier (e.g. user\_...). Present only when the request grouped by user\_id.

next\_page: optional string

Cursor for the next page of a grouped query; always null for the ungrouped artifact-type cube, which is returned in full.

Get Artifact Activity



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/artifacts \
    -H 'anthropic-version: 2023-06-01' \
    -H "Authorization: Bearer $ANTHROPIC_OAUTH_TOKEN"
```

Response 200



```shiki
{
  "data": [
    {
      "artifact_type": "artifact_type",
      "artifacts_created_count": 0,
      "distinct_user_count": 0,
      "is_shared": true,
      "published_artifacts_created_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
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
      "artifact_type": "artifact_type",
      "artifacts_created_count": 0,
      "distinct_user_count": 0,
      "is_shared": true,
      "published_artifacts_created_count": 0,
      "product": "product",
      "rbac_group_id": "rbac_group_id",
      "rbac_group_name": "rbac_group_name",
      "user_id": "user_id"
    }
  ],
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
