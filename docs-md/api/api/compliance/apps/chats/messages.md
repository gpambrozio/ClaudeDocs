# Messages

Copy page





To enable the Compliance API, see [Get access to the Compliance API](manage-claude/compliance-api-access.md).

# Messages

##### [Get chat messages](api/compliance/apps/chats/messages/list.md)

GET/v1/compliance/apps/chats/{claude\_chat\_id}/messages

##### ModelsExpand Collapse



MessageListResponse object { id, artifacts, content, 4 more } 

A single message in a chat conversation.

id: string

Unique identifier for the message e.g. 'claude\_chat\_msg\_abcd1234'



artifacts: array of object { id, artifact\_type, title, version\_id } 

Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string

MIME-like artifact type e.g. 'application/vnd.ant.code'

title: string

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'



content: array of object { text, type }  or object { id, input, integration\_name, 4 more }  or object { content, integration\_name, is\_error, 5 more } 

Content blocks within the message

One of the following:



Text object { text, type } 

Text content block.

text: string

Text content from human or assistant

type: "text"



ToolUse object { id, input, integration\_name, 4 more } 

Tool invocation requested by the assistant.

id: string

Tool-use ID, e.g. 'toolu\_01AbC...'

input: string

Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

integration\_name: string

Name of the integration that provides this tool, when applicable

mcp\_server\_url: string

Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string

Name of the tool invoked

truncated: boolean

True when `input` was shortened. Pass tool\_use\_input\_max\_chars=-1 to disable the limit

type: "tool\_use"



ToolResult object { content, integration\_name, is\_error, 5 more } 

Result returned by a tool invocation.



content: array of object { text, type } 

Text content returned by the tool. Generated files are surfaced via the message's `generated_files` list; other non-text item types (including images and links) are omitted.

text: string

Text returned by the tool

type: "text"

integration\_name: string

Name of the integration that provides this tool, when applicable

is\_error: boolean

True when the tool reported an error

mcp\_server\_url: string

Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string

Name of the tool that produced this result

tool\_use\_id: string

ID of the tool\_use block this result responds to

truncated: boolean

True when one or more text items in `content` were shortened. Pass tool\_result\_max\_chars=-1 to retrieve full content.

type: "tool\_result"

created\_at: string

Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block



files: array of object { id, created\_at, filename, 3 more } 

Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

id: string

File ID

created\_at: string

File creation timestamp

filename: string

Display name of the file

md5: string

Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.

mime\_type: string

MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')

size\_bytes: number

Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.



generated\_files: array of object { id, filename, md5, 2 more } 

Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'. Treat as an opaque string; the encoding may change without notice.

filename: string

Display name of the generated file

md5: string

Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.

mime\_type: string

MIME type reported by the tool that produced the file

size\_bytes: number

Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.



role: "assistant" or "user"

Message sender (user or assistant)

One of the following:

"assistant"

"user"

---

*Copyright © Anthropic. All rights reserved.*
