# Get Artifact Activity

Copy page



# Get Artifact Activity

GET/v1/organizations/analytics/artifacts

Get artifact-creation activity for a given day, broken out by MIME type.

Returns the full (artifact\_type, is\_shared) cube for the organization;
`next_page` is null except for grouped queries, which paginate. The cube
can be broken out per member or per RBAC group via group\_by[], and scoped
via filter[]. Requires an API key with the `read:analytics` scope.

##### Query parameters



date: string

UTC date in YYYY-MM-DD format. The day to get artifact activity for. Data is typically available with a 1-day lag (varies by query; the error for a too-recent date names the latest available day) and may be revised by a few percent over the following days. No earlier than 2026-01-01.

formatdate



filter: optional array of string

Filters as 'dimension:value', e.g. filter[]=rbac\_group\_id:<id>. Repeat the param for OR within a dimension and across dimensions for AND. Supported dimensions on this endpoint: artifact\_type, is\_shared, rbac\_group\_id, user\_id. Value forms: artifact\_type is a canonical artifact MIME type (e.g. text/markdown) or 'other'; is\_shared is 'true' or 'false'; rbac\_group\_id takes the tagged id (rbac\_group\_..., as emitted in responses and by the spend-limits API) or a bare group UUID, and matches users who held the group at any point during each covered UTC day (time-of-usage attribution); user\_id takes a tagged user id (user\_...), as emitted in responses. An unsupported dimension returns 400. At most 100 entries.

maxItems100



group\_by: optional array of "rbac\_group\_id" or "user\_id"

Dimensions to break results out by: user\_id and/or rbac\_group\_id. The ungrouped artifact-type cube is finite and returned in full; grouped queries multiply the cube and paginate via next\_page. rbac\_group\_id attributes a user to every group they held at any point during the requested UTC day, so grouped rows are not an exclusive partition. At most 100 entries.

maxItems100

One of the following:

"rbac\_group\_id"

"user\_id"



limit: optional number

Maximum rows to return (1-1000, default 100). The ungrouped artifact-type cube is finite and returned in full; limit is the page size only when group\_by[] multiplies the cube.

minimum1

maximum1000

page: optional string

Opaque cursor from a previous response's next\_page field. Only valid with group\_by[] — the ungrouped cube is never paginated.

##### Returns



ArtifactUsage object{ data, next\_page }

Response for GET /v1/organizations/analytics/artifacts.

`next_page` is null on ungrouped queries — the artifact-type cube is
finite and returned in full. Grouped queries (`group_by[]` on `user_id` /
`rbac_group_id`) multiply the cube and paginate like the other analytics
list endpoints.

### Get Artifact Activity

cURL



```shiki
curl https://api.anthropic.com/v1/organizations/analytics/artifacts \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_ADMIN_API_KEY"
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
