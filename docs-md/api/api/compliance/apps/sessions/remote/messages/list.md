# Retrieve remote session messages

Copy page



# Retrieve remote session messages

GET/v1/compliance/apps/sessions/remote/{claude\_remote\_session\_id}/messages

Retrieve one remote session's transcript: user prompts, assistant
responses, and tool calls and results. Thinking blocks and images are
not included.

Messages are returned oldest first by default; pass `order=desc` to
reverse. Pagination uses the same `page`/`next_page` scheme as the
list endpoint, with at most `limit` messages per page (default 100,
maximum 1000); keep paginating until `next_page` is null.
`tool_use_input_max_bytes` and `tool_result_max_bytes` cap how many
bytes of each tool-use input and each tool-result text item are
returned; a block shortened by either cap carries `truncated: true`.

The response embeds the session's metadata under `session` alongside
the paginated `data` array. On this endpoint `session.user.email_address`
and `session.started_by_user` are always null; read them from the list
endpoint instead.

Returns 404 while the session is still `pending`, for deleted sessions,
and for sessions outside the organizations the key may read. A
malformed session identifier returns 400.

##### Path parameters

claude\_remote\_session\_id: string

The remote session identifier (`cse_...`) to retrieve

##### Query parameters



limit: optional number

Maximum results (default: 100, max: 1000)

default100

maximum1000

minimum1



order: optional "asc" or "desc"

Sort direction. `asc` (oldest-first) or `desc`.

defaultasc

One of the following:

"asc"

"desc"

page: optional string

Opaque pagination token from a previous response's `next_page` field. Pass this to retrieve the next page of results. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.



tool\_result\_max\_bytes: optional number

Truncate each text item inside a tool result to at most this many bytes (cut on a code-point boundary). Pass `-1` to request the server maximum. `0` is not a valid value.

default10000

maximum2147483647

minimum-1



tool\_use\_input\_max\_bytes: optional number

Truncate each tool-use input to at most this many bytes (cut on a code-point boundary so the result is valid UTF-8). Pass `-1` to request the server maximum. `0` is not a valid value.

default10000

maximum2147483647

minimum-1

##### Headers

"x-api-key": optional string

##### Returns



data: array of object{ id, content, content\_unavailable, 3 more }

Transcript turns for this page, ordered by transcript position. `created_at` is a commit timestamp and may tie or invert under concurrent writes; do not re-sort by it.

id: string

Unique identifier for the message, e.g. `csev_abc123`



content: array of object{ text, truncated, type } or object{ id, input, name, 2 more } or object{ content, is\_error, name, 3 more }

Content blocks within the message

One of the following:



Text object{ text, truncated, type }

Text content block.

text: string

Text content from the user or the assistant



truncated: boolean

True when `text` exceeded the server-defined maximum (approximately 1 MiB) and was shortened.

defaultfalse



type: "text"

defaulttext



ToolUse object{ id, input, name, 2 more }

Tool invocation requested by the assistant.

id: string or null

Tool-use ID, e.g. 'toolu\_01AbC...'

input: string

Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

name: string

Name of the tool invoked



truncated: boolean

True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request full content, subject to the server-side maximum.

defaultfalse



type: "tool\_use"

defaulttool\_use



ToolResult object{ content, is\_error, name, 3 more }

Result returned by a tool invocation.



content: array of object{ text, type }

Text content returned by the tool. Non-text item types are omitted.

text: string

Text returned by the tool



type: "text"

defaulttext

is\_error: boolean

True when the tool reported an error

name: string

Name of the tool that produced this result

tool\_use\_id: string or null

ID of the tool\_use block this result responds to



truncated: boolean

True when one or more text items in `content` were shortened. Pass `tool_result_max_bytes=-1` to request full content, subject to the server-side maximum.

defaultfalse



type: "tool\_result"

defaulttool\_result



content\_unavailable: boolean

True when the stored content could not be returned — it could not be decrypted, or it exceeded the server's per-event size bound. `content` is empty in that case; this distinguishes 'no content' from 'content withheld'.

defaultfalse



created\_at: string

When the message was recorded (RFC 3339, UTC)

formatdate-time



role: "assistant" or "user"

Message sender (`user` or `assistant`)

One of the following:

"assistant"

"user"

sent\_by\_user\_id: string or null

Identifier of the human account that sent this turn on an agent-owned session. Null on user-owned sessions, where every user-role turn was sent by the session's `user`.

next\_page: string or null

Opaque page token; pass as `page` to retrieve the next page. Null when no rows exist after this page. Treat this value as opaque; do not parse or store it long-term, as the format may change without notice.



session: object{ id, agent\_id, claude\_project\_id, 7 more }

Session metadata. `started_by_user`, `user.email_address`, and `claude_project_id` are always null on this endpoint; the messages endpoint resolves neither email addresses nor project bindings.

id: string

Remote session identifier

agent\_id: string or null

Identifier of the automated agent that owns the session. Null for user-owned sessions. At most one of `user` and `agent_id` is set.

claude\_project\_id: string or null

ID of the project the session is bound to. Null when the session has no project binding.



created\_at: string

When the session was created (RFC 3339, UTC)

formatdate-time

organization\_uuid: string

UUID of the organization the session belongs to

product\_surface: string or null

The Claude product the session was created from. Currently `cowork_remote`, for Cowork sessions started on claude.ai web or mobile. More values will appear as other surfaces launch, so treat any unrecognized value as an unclassified surface rather than an error. Null for sessions created before this field was recorded, for surfaces that do not stamp it, and for unrecognized tag values.



started\_by\_user: object{ id, email\_address } or null

A user associated with a remote session.

id: string

User identifier

email\_address: string or null

User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

status: string

Session lifecycle state. One of `active`, `paused`, `archived`, or `failed` — the lifecycle states the owning product surface exposes — plus `pending`, a brief transient state that resolves before any transcript content exists. The list endpoint includes `pending`; the messages endpoint returns 404 for it. Deleted sessions are not returned on either endpoint. Treat unrecognized values as an unknown state rather than an error.



updated\_at: string

When the session was last modified (RFC 3339, UTC)

formatdate-time



user: object{ id, email\_address } or null

A user associated with a remote session.

id: string

User identifier

email\_address: string or null

User's email address. Null when the user is no longer a member of an organization the key may read — `id` remains set so attribution is preserved. The messages endpoint does not resolve email addresses; this field is always null there.

Retrieve remote session messages

cURL

```shiki
curl https://api.anthropic.com/v1/compliance/apps/sessions/remote/$CLAUDE_REMOTE_SESSION_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200



```shiki
{
  "data": [
    {
      "id": "id",
      "content": [
        {
          "text": "text",
          "truncated": true,
          "type": "text"
        }
      ],
      "content_unavailable": true,
      "created_at": "2019-12-27T18:11:19.117Z",
      "role": "assistant",
      "sent_by_user_id": "sent_by_user_id"
    }
  ],
  "next_page": "next_page",
  "session": {
    "id": "id",
    "agent_id": "agent_id",
    "claude_project_id": "claude_project_id",
    "created_at": "2019-12-27T18:11:19.117Z",
    "organization_uuid": "organization_uuid",
    "product_surface": "product_surface",
    "started_by_user": {
      "id": "id",
      "email_address": "email_address"
    },
    "status": "status",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "user": {
      "id": "id",
      "email_address": "email_address"
    }
  }
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
      "content": [
        {
          "text": "text",
          "truncated": true,
          "type": "text"
        }
      ],
      "content_unavailable": true,
      "created_at": "2019-12-27T18:11:19.117Z",
      "role": "assistant",
      "sent_by_user_id": "sent_by_user_id"
    }
  ],
  "next_page": "next_page",
  "session": {
    "id": "id",
    "agent_id": "agent_id",
    "claude_project_id": "claude_project_id",
    "created_at": "2019-12-27T18:11:19.117Z",
    "organization_uuid": "organization_uuid",
    "product_surface": "product_surface",
    "started_by_user": {
      "id": "id",
      "email_address": "email_address"
    },
    "status": "status",
    "updated_at": "2019-12-27T18:11:19.117Z",
    "user": {
      "id": "id",
      "email_address": "email_address"
    }
  }
}
```

---

*Copyright © Anthropic. All rights reserved.*
