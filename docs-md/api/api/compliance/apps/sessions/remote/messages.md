# Messages

Copy page



# Messages

##### [Retrieve remote session messages](api/compliance/apps/sessions/remote/messages/list.md)

GET/v1/compliance/apps/sessions/remote/{claude\_remote\_session\_id}/messages

##### ModelsExpand Collapse



MessageListResponse object { id, content, content\_unavailable, 3 more } 

A single user or assistant turn in a remote session transcript.

`content` is a discriminated union of `text`, `tool_use`, and
`tool_result` blocks.

id: string

Unique identifier for the message, e.g. `csev_abc123`



content: array of object { text, truncated, type }  or object { id, input, name, 2 more }  or object { content, is\_error, name, 3 more } 

Content blocks within the message

One of the following:



Text object { text, truncated, type } 

Text content block.

text: string

Text content from the user or the assistant

truncated: boolean

True when `text` exceeded the server-defined maximum (approximately 1 MiB) and was shortened.

type: "text"



ToolUse object { id, input, name, 2 more } 

Tool invocation requested by the assistant.

id: string or null

Tool-use ID, e.g. 'toolu\_01AbC...'

input: string

Arguments passed to the tool, as a JSON-encoded string. May be shortened — see the `truncated` field

name: string

Name of the tool invoked

truncated: boolean

True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request full content, subject to the server-side maximum.

type: "tool\_use"



ToolResult object { content, is\_error, name, 3 more } 

Result returned by a tool invocation.



content: array of object { text, type } 

Text content returned by the tool. Non-text item types are omitted.

text: string

Text returned by the tool

type: "text"

is\_error: boolean

True when the tool reported an error

name: string

Name of the tool that produced this result

tool\_use\_id: string or null

ID of the tool\_use block this result responds to

truncated: boolean

True when one or more text items in `content` were shortened. Pass `tool_result_max_bytes=-1` to request full content, subject to the server-side maximum.

type: "tool\_result"

content\_unavailable: boolean

True when the stored content could not be returned — it could not be decrypted, or it exceeded the server's per-event size bound. `content` is empty in that case; this distinguishes 'no content' from 'content withheld'.

created\_at: string

When the message was recorded (RFC 3339, UTC)



role: "assistant" or "user"

Message sender (`user` or `assistant`)

One of the following:

"assistant"

"user"

sent\_by\_user\_id: string or null

Identifier of the human account that sent this turn on an agent-owned session. Null on user-owned sessions, where every user-role turn was sent by the session's `user`.

---

*Copyright © Anthropic. All rights reserved.*
