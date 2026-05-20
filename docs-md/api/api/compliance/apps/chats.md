# Chats

Copy page

The Compliance API is enabled on request. Claude Enterprise organizations have access to the full API; Claude Console organizations have access to the [Activity Feed](manage-claude/compliance-activity-feed.md) only. See [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Chats

##### [List chats](api/compliance/apps/chats/list.md)

GET/v1/compliance/apps/chats

##### [Delete chat](api/compliance/apps/chats/delete.md)

DELETE/v1/compliance/apps/chats/{claude\_chat\_id}

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

Deprecatedorganization\_id: string

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

#### ChatsMessages

##### [Get chat messages](api/compliance/apps/chats/messages/list.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

##### ModelsExpand Collapse

MessageListResponse = object { id, artifacts, content, 4 more }

A single message in a chat conversation.

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

content: array of object { text, type }

Content blocks within the message

text: string

Text content from human or assistant

type: "text"

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

Accepts one of the following:

"assistant"

"user"

#### ChatsFiles

##### [Get file metadata](api/compliance/apps/chats/files/retrieve.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Delete file](api/compliance/apps/chats/files/delete.md)

DELETE/v1/compliance/apps/chats/files/{claude\_file\_id}

##### [Download file content](api/compliance/apps/chats/files/download.md)

GET/v1/compliance/apps/chats/files/{claude\_file\_id}/content

##### ModelsExpand Collapse

FileRetrieveResponse = object { id, created\_at, filename, 4 more }

File metadata for GET /v1/compliance/apps/chats/files/{claude\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the file bytes.

id: string

File ID

created\_at: string

File creation timestamp

filename: string

Display name of the file, if set

md5: string

Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes; when the two disagree, the header is authoritative.

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

#### ChatsGenerated Files

##### [Get Claude-generated file metadata](api/compliance/apps/chats/generated_files/retrieve.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}

##### [Download a Claude-generated file](api/compliance/apps/chats/generated_files/download.md)

GET/v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}/content

##### ModelsExpand Collapse

GeneratedFileRetrieveResponse = object { id, claude\_chat\_id, created\_at, 4 more }

Metadata for GET /v1/compliance/apps/chats/generated-files/{claude\_gen\_file\_id}.

Returns metadata only. Use the sibling `/content` endpoint to download
the bytes. The owning chat is included since the id is opaque; to find the
specific message that produced the file, fetch
`/v1/compliance/apps/chats/{claude_chat_id}/messages` and match on
`generated_files[].id`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'.

claude\_chat\_id: string

The chat this generated file belongs to

created\_at: string

File creation timestamp from Filestore

filename: string

Display name of the generated file

md5: string

Lowercase hex MD5 of the stored file, as recorded by Filestore. Null when no stored hash is available. The sibling `/content` endpoint also sets a `Content-MD5` header (base64 per RFC 1864) computed over the exact served bytes.

mime\_type: string

MIME type as recorded by Filestore, when available

size\_bytes: number

Size in bytes of the stored file, when available

---

*Copyright © Anthropic. All rights reserved.*
