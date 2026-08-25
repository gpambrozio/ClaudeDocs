# List local sessions

Copy page



# List local sessions

GET/v1/compliance/apps/sessions/local

List local sessions across the organizations the key may read.

Results are ordered by `created_at` descending. Pagination is
forward-only via `next_page`; there is no reverse cursor.

##### Query parameters



created\_at: optional object{ gte, lt }



gte: optional string

Only return sessions whose first inference call is at or after this time (RFC 3339; a UTC offset is required).

formatdate-time



lt: optional string

Only return sessions whose first inference call is strictly before this time (RFC 3339; a UTC offset is required).

formatdate-time



limit: optional number

Maximum results (default: 100, max: 500)

default100

maximum500

minimum1

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



updated\_at: optional object{ gte }



gte: optional string

Only return sessions whose last inference call is at or after this time (RFC 3339; a UTC offset is required). Combines with `created_at.gte` / `created_at.lt`; the ordering and pagination are unchanged. Use it to poll for sessions that have been active since a previous pass — a session that becomes active later can only enter the result, never leave it.

formatdate-time

##### Headers

"x-api-key": optional string

##### Returns



data: array of object{ id, created\_at, organization\_uuid, 5 more }

Page of local sessions, ordered by `created_at` descending; ties are broken by a fixed server-side order. `updated_at` never participates in the ordering; the `updated_at.gte` query parameter filters on it without changing the order or the pagination cursor.

id: string

Local session identifier, prefixed `clls_`. Unique within the parent organization. Treat as an opaque string; the format may change without notice.



created\_at: string

Timestamp of the session's first retained inference call (RFC 3339, UTC). When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected, so this value is the timestamp of the earliest retained call: always strictly after the boundary, never the boundary itself.

formatdate-time

organization\_uuid: string

UUID of the child organization the session belongs to

product\_surface: string or null

The product the session ran in: `cowork` for Cowork sessions in Claude Desktop, or `claude_code` for Claude Code sessions. New values appear as coverage expands; treat unrecognized values as opaque. `null` when the surface was not recorded.



type: "compliance\_local\_session"

defaultcompliance\_local\_session



updated\_at: string

Timestamp of the session's last retained inference call (RFC 3339, UTC). Always at or after `created_at`. When a session's activity spans the child organization's retention boundary, calls older than the boundary are no longer reflected — but because retention removes only the oldest calls, this value (unlike `created_at`) is unaffected until the entire session has aged out. On the list endpoint this value is a lower bound: for a session still active at a page or `created_at.lt` window boundary it can momentarily lag the session's true last activity. Retrieving the session, or its messages, always reflects the exact latest retained call.

formatdate-time



user: object{ id, email\_address }

The authenticated user at the time of the session. Always set; `user.id` is always populated. `user.email_address` is null when the user's account has been deleted or the user is no longer a member of an organization the key may read.

id: string

User identifier (tagged ID, prefixed `user_`). Always set, so attribution survives after the user's account is deleted or the user leaves the organizations the key may read.

email\_address: string or null

User's email address. Null when the user's account has been deleted or the user is no longer a member of an organization the key may read. The messages endpoint does not resolve email addresses; this field is always null there.

workspace\_id: string or null

Workspace identifier (tagged ID, prefixed `wrkspc_`). Null for sessions not attributed to a workspace.

next\_page: string or null

Opaque pagination cursor (prefixed `page_`) for the next page. Null when there is no further page. Treat as an opaque string; the format may change without notice.

### List local sessions

cURL



```shiki
curl https://api.anthropic.com/v1/compliance/apps/sessions/local \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "type": "compliance_local_session",
      "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
      "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
      "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
      "user": {
        "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
        "email_address": "engineer@example.com"
      },
      "product_surface": "cowork",
      "created_at": "2026-07-09T14:02:11Z",
      "updated_at": "2026-07-09T15:47:33Z"
    }
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "type": "compliance_local_session",
      "id": "clls_eyJ2IjoxLCJvIjoiOWEx…",
      "organization_uuid": "9a1e0000-0000-0000-0000-000000000000",
      "workspace_id": "wrkspc_01SvYKoWVRVHoEbwESNvzYdR",
      "user": {
        "id": "user_01GpKpLmNoPqRsTuVwXyZaBc",
        "email_address": "engineer@example.com"
      },
      "product_surface": "cowork",
      "created_at": "2026-07-09T14:02:11Z",
      "updated_at": "2026-07-09T15:47:33Z"
    }
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
