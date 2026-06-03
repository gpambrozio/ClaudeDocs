# Get chat messages

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](manage-claude/compliance-activity-feed.md) only. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Get chat messages

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

Retrieves message history and file metadata for a specific chat.

##### Path ParametersExpand Collapse

claude\_chat\_id: string

The chat ID (tagged ID, e.g., claude\_chat\_abc123)

##### Query ParametersExpand Collapse

after\_id: optional string

Pagination cursor for retrieving the next page of results (heading backwards in time). To paginate, pass the `last_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

before\_id: optional string

Pagination cursor for retrieving the previous page of results (heading forwards in time). To paginate, pass the `first_id` value from the most recent response. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

created\_at: optional object { gt, gte, lt, lte }

gt: optional string

Filter messages created after this time (RFC 3339 format)

gte: optional string

Filter messages created at or after this time (RFC 3339 format)

lt: optional string

Filter messages created before this time (RFC 3339 format)

lte: optional string

Filter messages created at or before this time (RFC 3339 format)

limit: optional number

Maximum results (max: 1000). When omitted, the full result set is returned in one response.

order: optional "asc" or "desc"

Sort direction for messages within the response. `asc` (the default) returns oldest-first; `desc` returns newest-first.

One of the following:

"asc"

"desc"

tool\_result\_max\_chars: optional number

Maximum characters returned per tool-result text item. Items longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

tool\_use\_input\_max\_chars: optional number

Maximum characters of JSON-encoded tool input returned per tool\_use block. Inputs longer than this are shortened and the block's `truncated` field is set. Pass -1 to disable the limit.

updated\_at: optional object { gt, gte, lt, lte }

gt: optional string

Filter messages updated after this time (RFC 3339 format)

gte: optional string

Filter messages updated at or after this time (RFC 3339 format)

lt: optional string

Filter messages updated before this time (RFC 3339 format)

lte: optional string

Filter messages updated at or before this time (RFC 3339 format)

##### Header ParametersExpand Collapse

"x-api-key": optional string

##### ReturnsExpand Collapse

id: string

Chat ID

chat\_messages: array of object { id, artifacts, content, 4 more }

Array of chat messages in order of created\_at

id: string

Unique identifier for the message e.g. 'claude\_chat\_msg\_abcd1234'

artifacts: array of object { id, artifact\_type, title, version\_id }

Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'

content: array of object { text, type }  or object { id, input, integration\_name, 4 more }  or object { content, integration\_name, is\_error, 5 more }

Content blocks within the message

One of the following:

Text object { text, type }

Text content block.

text: string

Text content from human or assistant

type: "text"

ToolUse object { id, input, integration\_name, 4 more }

Tool invocation requested by the assistant.

id: string

Tool-use ID, e.g. 'toolu\_01AbC...'

input: string

Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

integration\_name: string

Name of the integration that provides this tool, when applicable

mcp\_server\_url: string

Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string

Name of the tool invoked

truncated: boolean

True when `input` was shortened. Pass tool\_use\_input\_max\_chars=-1 to disable the limit

type: "tool\_use"

ToolResult object { content, integration\_name, is\_error, 5 more }

Result returned by a tool invocation.

content: array of object { text, type }

Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

text: string

Text returned by the tool

type: "text"

integration\_name: string

Name of the integration that provides this tool, when applicable

is\_error: boolean

True when the tool reported an error

mcp\_server\_url: string

Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string

Name of the tool that produced this result

tool\_use\_id: string

ID of the tool\_use block this result responds to

truncated: boolean

True when one or more text items in `content` were shortened. Pass tool\_result\_max\_chars=-1 to retrieve full content.

type: "tool\_result"

created\_at: string

Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

files: array of object { id, filename, mime\_type }

Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

id: string

File ID

filename: string

Display name of the file

mime\_type: string

MIME type of the file when it was uploaded (e.g. 'application/pdf')

generated\_files: array of object { id, filename, mime\_type }

Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'. Treat as an opaque string; the encoding may change without notice.

filename: string

Display name of the generated file

mime\_type: string

MIME type reported by the tool that produced the file

role: "assistant" or "user"

Message sender (user or assistant)

One of the following:

"assistant"

"user"

created\_at: string

Creation timestamp

deleted\_at: string

Deletion timestamp if deleted

first\_id: string

Opaque pagination cursor for the first message in the current result set. Pass as `before_id` on the next request to page backwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

has\_more: boolean

Whether more chat messages exist beyond the current result set. Use `last_id` as `after_id` in a follow-up request to page forward.

href: string

URL to view this chat in claude.ai

last\_id: string

Opaque pagination cursor for the last message in the current result set. Pass as `after_id` on the next request to page forwards. Clients should treat this value as an opaque string and not attempt to parse or interpret its contents, as the format may change without notice.

model: string

Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

name: string

Chat name

Deprecatedorganization\_id: string

Organization ID this chat belongs to

organization\_uuid: string

Organization UUID this chat belongs to

project\_id: string

Project ID this chat belongs to

updated\_at: string

Last update timestamp

user: object { id, email\_address }

User information

id: string

User identifier

email\_address: string

User's email address

Get chat messages

```shiki
curl https://api.anthropic.com/v1/compliance/apps/chats/$CLAUDE_CHAT_ID/messages \
    -H "Authorization: Bearer $ANTHROPIC_COMPLIANCE_API_KEY"
```

Response 200

```shiki
{
  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-4-7",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  },
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
    {
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf"
        }
      ]
    },
    {
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
}
```

##### Returns Examples

Response 200

```shiki
{
  "id": "claude_chat_abc123",
  "name": "Product Requirements Discussion",
  "created_at": "2025-06-07T08:09:10Z",
  "updated_at": "2025-06-07T08:09:11Z",
  "organization_id": "org_abc123",
  "organization_uuid": "abcdef0123-4567-89ab-cdef-0123456789ab",
  "project_id": "claude_proj_xyz789",
  "model": "claude-opus-4-7",
  "user": {
    "id": "user_xyz456",
    "email_address": "user@example.com"
  },
  "href": "https://claude.ai/chat/abcdef01-2345-6789-abcd-ef0123456789",
  "chat_messages": [
    {
      "id": "claude_chat_msg_abc123",
      "role": "user",
      "created_at": "2025-06-07T08:09:10Z",
      "content": [
        {
          "type": "text",
          "text": "Can you help me draft requirements for our new dashboard feature?"
        }
      ],
      "files": [
        {
          "id": "claude_file_xyz789",
          "filename": "dashboard_mockup_v1.pdf",
          "mime_type": "application/pdf"
        }
      ]
    },
    {
      "id": "claude_chat_msg_def456",
      "role": "assistant",
      "created_at": "2025-06-07T08:09:11Z",
      "content": [
        {
          "type": "text",
          "text": "I'd be happy to help you draft requirements for your dashboard feature..."
        }
      ],
      "artifacts": [
        {
          "id": "claude_artifact_abc123",
          "version_id": "claude_artifact_version_xyz789",
          "title": "Dashboard Requirements Draft",
          "artifact_type": "text/markdown"
        }
      ]
    }
  ],
  "has_more": false,
  "first_id": "eyJtc2dfdXVpZCI6ICIwZjcwYjA2Ni0uLi4ifQ==",
  "last_id": "eyJtc2dfdXVpZCI6ICJhNGUwYjE3Mi0uLi4ifQ=="
}
```

---

*Copyright © Anthropic. All rights reserved.*
