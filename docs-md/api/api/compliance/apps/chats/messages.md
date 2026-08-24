# Messages

Copy page



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

artifacts: array of object { id, artifact\_type, title, version\_id }  or null

Versioned documents generated or updated by the assistant in this message. Download via `GET /v1/compliance/apps/artifacts/{artifact_version_id}/content`.

id: string

Artifact ID e.g. 'claude\_artifact\_abc123'

artifact\_type: string or null

MIME-like artifact type e.g. 'application/vnd.ant.code'

title: string or null

Artifact title

version\_id: string

Artifact version ID e.g. 'claude\_artifact\_version\_abc123'



content: array of object { text, thinking\_redacted, truncated, type }  or object { id, input, integration\_name, 4 more }  or object { content, integration\_name, is\_error, 5 more } 

Content blocks within the message

One of the following:



Text object { text, thinking\_redacted, truncated, type } 

Text content block.

text: string

Text content from human or assistant

thinking\_redacted: boolean

True when content enclosed in the assistant's internal-reasoning tags (or the tag markup itself) was removed from `text` during export. Removal never occurs with this field false. Always false on human messages, whose text is exported verbatim.

truncated: boolean

True when `text` was shortened by the server's fixed per-string bound (1 MiB). Always false on chat text blocks.

type: "text"



ToolUse object { id, input, integration\_name, 4 more } 

Tool invocation requested by the assistant.

id: string or null

Tool-use ID, e.g. 'toolu\_01AbC...'

input: string

Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

integration\_name: string or null

Name of the integration that provides this tool, when applicable

mcp\_server\_url: string or null

Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string

Name of the tool invoked

truncated: boolean

True when `input` was shortened. Pass the endpoint's tool-use input max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

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

integration\_name: string or null

Name of the integration that provides this tool, when applicable

is\_error: boolean

True when the tool reported an error

mcp\_server\_url: string or null

Base URL (scheme, host, and path only) of the MCP server that provides this tool, when applicable

name: string

Name of the tool that produced this result

tool\_use\_id: string or null

ID of the tool\_use block this result responds to

truncated: boolean

True when one or more text items in `content` were shortened. Pass the endpoint's tool-result max parameter as -1 to request full content, subject to any server-side maximum the endpoint enforces.

type: "tool\_result"

created\_at: string

Message creation timestamp - For human: when they sent the message, For assistant: when it completed the last content block



files: array of object { id, created\_at, filename, 3 more }  or null

Binary file attachments uploaded by the user. Download via `GET /v1/compliance/apps/chats/files/{claude_file_id}/content`.

id: string

File ID

created\_at: string

File creation timestamp

filename: string

Display name of the file

md5: string or null

Lowercase hex MD5 of the file's preferred downloadable variant, as recorded at upload time. Null when no stored hash is available.

mime\_type: string or null

MIME type of the file's preferred downloadable variant (e.g. 'application/pdf')

size\_bytes: number or null

Size in bytes of the file's preferred downloadable variant, if known. Null for older files uploaded before size was recorded.



generated\_files: array of object { id, filename, md5, 2 more }  or null

Downloadable files the assistant created via tool use (e.g. PDF, spreadsheet, slide deck). Distinct from `files`, which are uploads attached to the message. Download via `GET /v1/compliance/apps/chats/generated-files/{claude_gen_file_id}/content`.

id: string

Opaque generated-file id, e.g. 'claude\_gen\_file\_abc123'. Treat as an opaque string; the encoding may change without notice.

filename: string

Display name of the generated file

md5: string or null

Lowercase hex MD5 of the generated file, when available. Null when no stored hash is available.

mime\_type: string or null

MIME type reported by the tool that produced the file

size\_bytes: number or null

Size in bytes of the generated file, when available. Null when the file has expired or size is not recorded.



role: "assistant" or "user"

Message sender (user or assistant)

One of the following:

"assistant"

"user"

---

*Copyright © Anthropic. All rights reserved.*
