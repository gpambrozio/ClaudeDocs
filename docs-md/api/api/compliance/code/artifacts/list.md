# List Code Artifacts

Copy page



To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# List Code Artifacts

GET/v1/compliance/code/artifacts

List Claude Code Artifacts owned by organizations under the parent
organization.

Results are sorted by Artifact identifier within each batch of child
organizations. Pages may be short or empty while `next_page` is still
set — continue until `next_page` is absent. Artifacts are sorted by
identifier (not creation time): an
Artifact published during an export may land before the cursor and be
omitted, so for a point-in-time-complete export re-enumerate after
publishing quiesces.

Artifacts owned by a since-deleted child organization are not
returned.

##### Query ParametersExpand Collapse

limit: optional number

Maximum results (default: 20, max: 100)

organization\_ids: optional array of string

Filter by organization IDs (accepts `org_...` or organization UUID, up to 500). Enumerate IDs via `GET /v1/compliance/organizations`.

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



updated\_at: optional object { gt, gte, lt, lte } 

gt: optional string

Return only Artifacts updated after this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

gte: optional string

Return only Artifacts updated at or after this time (RFC 3339 format). Time filters match an eventually-consistent index and Artifacts published before this field was recorded never match — omit the time filter for compliance-complete enumeration. For incremental export, apply a generous overlap margin between windows and dedupe by `id`: adjacent tiling silently misses items whose index update lagged their publish.

lt: optional string

Return only Artifacts updated before this time (RFC 3339 format). Multiple time operators are AND-ed to the tightest bound. See `updated_at.gte` for the completeness caveat.

lte: optional string

Return only Artifacts updated at or before this time (RFC 3339 format). See `updated_at.gte` for the completeness caveat.

user\_ids: optional array of string

Filter by owner user IDs (up to 200). Enumerate IDs via `GET /v1/compliance/organizations/{org_uuid}/users`.

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse



data: array of object { id, organization\_id, organization\_uuid, 6 more } 

Page of Artifacts

id: string

Artifact identifier (tagged ID)

Deprecatedorganization\_id: string

Organization identifier (tagged ID)

organization\_uuid: string

Organization UUID this Artifact belongs to

owner\_user\_id: string

Artifact owner's user identifier (tagged ID). Always set, so attribution survives after the owner's account is deleted or the owner leaves every organization under the parent.

published\_version\_id: string

Identifier of the version a non-owner viewer would render when `read_mode` permits them — the version the owner has pinned for non-owner readers if one is pinned, otherwise the owner's latest. When `read_mode` is `owner` no non-owner renders any version; the field still reports which version would be served were read\_mode widened.



read\_mode: "org" or "owner" or "users"

Who can view this Artifact: only its owner, a named set of users, or every member of its organization

One of the following:

"org"

"owner"

"users"

updated\_at: string

Artifact last update timestamp, or null for Artifacts published before this field was recorded



user: object { id, email\_address } 

The user who owns a Code Artifact.

Fields that reference this type are null when the owner's account has
been deleted or the owner is no longer a member of any organization
under the parent organization.

id: string

User identifier (tagged ID)

email\_address: string

User's email address



versions: array of object { id, created\_at, name } 

Up to roughly 20 most-recently-published versions of this Artifact (older versions are not retained). Metadata only — use `GET /v1/compliance/code/artifacts/{artifact_id}/versions/{version_id}` to download a version's content.

id: string

Opaque version identifier

created\_at: string

When this version was published

name: string

Artifact title at this version. Falls back to the version identifier when the title for an older version is no longer retained.

has\_more: boolean

Whether `next_page` is set. When enumeration spans multiple organization batches this may be true for a page whose next page is empty — continue until `next_page` is absent.

next\_page: string

Token to retrieve the next page. Use this as the 'page' parameter in your next request

List Code Artifacts



```shiki
curl https://api.anthropic.com/v1/compliance/code/artifacts \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "owner_user_id": "owner_user_id",
      "published_version_id": "published_version_id",
      "read_mode": "org",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "user": {
        "id": "id",
        "email_address": "email_address"
      },
      "versions": [
        {
          "id": "id",
          "created_at": "2019-12-27T18:11:19.117Z",
          "name": "name"
        }
      ]
    }
  ],
  "has_more": true,
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
      "id": "id",
      "organization_id": "organization_id",
      "organization_uuid": "organization_uuid",
      "owner_user_id": "owner_user_id",
      "published_version_id": "published_version_id",
      "read_mode": "org",
      "updated_at": "2019-12-27T18:11:19.117Z",
      "user": {
        "id": "id",
        "email_address": "email_address"
      },
      "versions": [
        {
          "id": "id",
          "created_at": "2019-12-27T18:11:19.117Z",
          "name": "name"
        }
      ]
    }
  ],
  "has_more": true,
  "next_page": "next_page"
}
```

---

*Copyright © Anthropic. All rights reserved.*
