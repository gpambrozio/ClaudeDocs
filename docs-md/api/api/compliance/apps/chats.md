# Chats

Copy page

The Compliance API is available only on the Claude Enterprise plan and must be enabled before use. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Chats

##### [List chats](api/compliance/apps/chats/list.md)

GET/v1/compliance/apps/chats

##### [Delete chat](api/compliance/apps/chats/delete.md)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

##### [Get chat messages](api/compliance/apps/chats/messages.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

##### ModelsExpand Collapse

ChatListResponse = object { id, created\_at, deleted\_at, 8 more }

Chat metadata for listing chats (without messages).

id: string

Chat ID

created\_at: string

Creation timestamp

deleted\_at: string

Deletion timestamp if deleted

href: string

URL to view this chat in claude.ai

model: string

Model selected for this chat (e.g. 'claude-opus-4-7'). May be null for legacy chats that never had a model recorded.

name: string

Chat name/title

organization\_id: string

Organization ID this chat belongs to

organization\_uuid: string

Organization UUID this chat belongs to

project\_id: string

Project ID this chat belongs to

updated\_at: string

Last update timestamp

user: object { id, email\_address }

User information for the chat creator

id: string

User identifier

email\_address: string

User's email address

ChatDeleteResponse = object { id, type }

Response for deleting a Claude chat.

id: string

The ID of the Claude chat that was deleted

type: optional "claude\_chat\_deleted"

Constant string confirming deletion

ChatMessagesResponse = object { id, chat\_messages, created\_at, 12 more }

Complete chat conversation data for compliance purposes.

id: string

Chat ID

chat\_messages: array of object { id, artifacts, content, 4 more }

Array of chat messages in order of created\_at

id: string

Unique identifier for the message e.g. 'claude\_chat\_msg\_abcd1234'

artifacts: array of object { id, artifact\_type, title, version\_id }

Artifacts generated or updated by this message

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'

content: array of object { text, type }

Content blocks within the message

text: string

Text content from human or assistant

type: "text"

created\_at: string

Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block

files: array of object { id, filename, mime\_type }

File attachments

id: string

File ID

filename: string

Display name of the file

mime\_type: string

MIME type of the file when it was uploaded (e.g. 'application/pdf')

generated\_files: array of object { id, filename, mime\_type }

Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'. Treat as an opaque string; the encoding may change without notice.

filename: string

Display name of the generated file

mime\_type: string

MIME type reported by the tool that produced the file

role: "user" or "assistant"

Message sender (user or assistant)

Accepts one of the following:

"user"

"assistant"

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

organization\_id: string

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

#### ChatsFiles

##### [Get file metadata](api/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/compliance/apps/chats/files/content.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

##### ModelsExpand Collapse

FileRetrieveResponse = object { id, created\_at, filename, 3 more }

File metadata for GET /v1/compliance/apps/chats/files/{claude\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the file bytes.

id: string

File ID

created\_at: string

File creation timestamp

filename: string

Display name of the file, if set

message\_ids: array of string

Chat message IDs this file is attached to. A file can be referenced by multiple messages.

mime\_type: string

MIME type of the file's preferred downloadable variant (e.g. 'application/pdf'). May be null for files with no downloadable content (e.g. code-interpreter outputs).

size\_bytes: number

Size in bytes of the file's preferred downloadable variant, if known

FileDeleteResponse = object { id, type }

Response for deleting a compliance file.

id: string

The ID of the file that was deleted

type: optional "claude\_file\_deleted"

Constant string confirming deletion

FileContentResponse = unknown

#### ChatsGenerated Files

##### [Download a Claude-generated file](api/compliance/apps/chats/generated_files/content.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

##### ModelsExpand Collapse

GeneratedFileContentResponse = unknown

---

*Copyright © Anthropic. All rights reserved.*
