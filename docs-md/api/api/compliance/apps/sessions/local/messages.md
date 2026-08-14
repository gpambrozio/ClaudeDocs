# Messages

Copy page



# Messages

##### [Retrieve local session messages](api/compliance/apps/sessions/local/messages/list.md)

GET/v1/compliance/apps/sessions/local/{local\_session\_id}/messages

##### ModelsExpand Collapse



MessageListResponse object { id, content, created\_at, 3 more } 

A single user or assistant turn in a local session transcript.

id: string

Message identifier, prefixed `clsm_`. Stable for as long as the message's turn is retained: identifiers of retained turns do not change as older turns age out of the organization's retention period. The `retention_elapsed` placeholder's identifier is distinct from every retained turn's and changes only when further turns age out.



content: array of object { text, truncated, type }  or object { id, input, name, 2 more }  or object { content, is\_error, name, 3 more } 

Content blocks within the message, discriminated on `type` (`text` / `tool_use` / `tool_result`: the same discriminator values as the claude.ai chat-messages endpoint; the tool variants omit `integration_name` and `mcp_server_url`, and `text` carries `truncated`). Extended-thinking content is never included. The request's `system` field is never included; a presence-only marker message is emitted when it was set. The request's `tools[]` definitions are never included as transcript messages. Project-level instructions (such as CLAUDE.md files) appear in the message stream as a user-role context block and are included. Empty when `provenance.type` is `content_unavailable`.

One of the following:



Text object { text, truncated, type } 

Text content block.

text: string

Text content from the user or the assistant

truncated: boolean

True when `text` was shortened by the server's fixed per-string bound (approximately 1 MiB), or when ancillary content the block carried (such as citations) was omitted, or when this block stands in for a non-text block whose content is not shown, or when it is an explanatory marker the server inserted (its text enclosed in square brackets, e.g. prefacing client-asserted history). There is no request parameter that raises the per-string bound.

type: "text"



ToolUse object { id, input, name, 2 more } 

Tool invocation requested by the assistant.

id: string or null

Tool-use ID, e.g. 'toolu\_01AbC...'

input: string

Arguments passed to the tool, as a JSON-encoded string. May be shortened (see the `truncated` field); a truncated value is cut mid-document and is not valid JSON.

name: string

Name of the tool invoked

truncated: boolean

True when `input` was shortened. Pass `tool_use_input_max_bytes=-1` to request the server maximum.

type: "tool\_use"



ToolResult object { content, is\_error, name, 3 more } 

Result returned by a tool invocation.



content: array of object { text, type } 

Text content returned by the tool. Non-text item types are omitted and signalled via `truncated` with an in-band item-count marker.

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

True when one or more text items in `content` were shortened or non-text items were omitted. Pass `tool_result_max_bytes=-1` to request the server maximum.

type: "tool\_result"

created\_at: string

When the message was recorded (RFC 3339, UTC)



provenance: object { reason, type }  or object { type }  or object { type }  or null

Where this turn's content came from, discriminated on `type`. Null (the common case) means verified content: on an assistant message, content Claude produced during this session; on a user message, content the user sent. `content_unavailable`: the turn's content cannot be returned and `content` is empty; `reason` says why. `client_asserted`: assistant content the client supplied as conversation history; `content` shows what the model received but its authorship is not verified; never on user-role messages. `synthetic_marker`: a transcript marker the endpoint generated rather than content either party sent during the session. Both `client_asserted` and `synthetic_marker` can result from normal request or client processing, not only client modification. Callers should tolerate unrecognized `type` values.

One of the following:



ContentUnavailable object { reason, type } 

The turn's content cannot be returned; `content` is empty.

reason: string

Why this turn's content cannot be returned, e.g. `not_captured` (the content was not captured for compliance retrieval), `cmek_key_revoked` (the content is encrypted under the organization's customer-managed key and that key is unavailable), `retention_elapsed` (the content lies past the organization's retention boundary; on the placeholder standing in for every pre-boundary turn), or `oversize` (the message exceeds the server's per-message size bound even after per-block truncation). Callers should tolerate unrecognized values. `not_captured` is not proof that no record was stored: content withheld by the storage layer's fail-closed access policies carries the same reason and is deliberately indistinguishable from content that was never captured.

type: "content\_unavailable"



ClientAsserted object { type } 

Assistant content the client supplied as conversation history
rather than produced by Claude during this session. `content` shows
what the model received but its authorship is not verified; this can
result from normal request or client processing, not only client
modification. Never on user-role messages.

type: "client\_asserted"



SyntheticMarker object { type } 

A transcript marker generated by the endpoint rather than sent by
either party during the session. Marker messages indicate that the
prompt history diverged from what was captured, that the request's
`system` field was present but is not shown, or that
prompt-carried history was suppressed because the session spans the
child organization's retention boundary and those turns cannot be
placed against it (the marker's text names the cause). Markers that
report a mismatch with captured history can result from normal request
or client processing, not only client modification.

type: "synthetic\_marker"



role: "assistant" or "user"

Message sender (`user` or `assistant`)

One of the following:

"assistant"

"user"

type: "compliance\_local\_session\_message"

---

*Copyright © Anthropic. All rights reserved.*
