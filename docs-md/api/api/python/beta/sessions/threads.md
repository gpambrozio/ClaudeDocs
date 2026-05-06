# Threads

Copy page

Python

# Threads

##### [List Session Threads](api/beta/sessions/threads/list.md)

beta.sessions.threads.list(strsession\_id, ThreadListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionThread](api/beta.md)]

GET/v1/sessions/{session\_id}/threads

##### [Get Session Thread](api/beta/sessions/threads/retrieve.md)

beta.sessions.threads.retrieve(strthread\_id, ThreadRetrieveParams\*\*kwargs)  -> [BetaManagedAgentsSessionThread](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}

##### [Archive Session Thread](api/beta/sessions/threads/archive.md)

beta.sessions.threads.archive(strthread\_id, ThreadArchiveParams\*\*kwargs)  -> [BetaManagedAgentsSessionThread](api/beta.md)

POST/v1/sessions/{session\_id}/threads/{thread\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsSessionThread: …

An execution thread within a `session`. Each session has one primary thread plus zero or more child threads spawned by the coordinator.

id: str

Unique identifier for this thread.

agent: [BetaManagedAgentsSessionThreadAgent](api/beta.md)

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: str

description: Optional[str]

mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str

model: [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: str

skills: List[Skill]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str

class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]

tools: List[Tool]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401: …

configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]

class BetaManagedAgentsMCPToolset: …

configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]

class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

properties: Optional[Dict[str, object]]

JSON Schema properties defining the tool's input parameters.

required: Optional[List[str]]

List of required property names.

type: Optional[Literal["object"]]

Must be 'object' for tool input schemas.

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

archived\_at: Optional[datetime]

A timestamp in RFC 3339 format

created\_at: datetime

A timestamp in RFC 3339 format

parent\_thread\_id: Optional[str]

Parent thread that spawned this thread. Null for the primary thread.

session\_id: str

The session this thread belongs to.

stats: Optional[BetaManagedAgentsSessionThreadStats]

Timing statistics for a session thread.

active\_seconds: Optional[float]

Cumulative time in seconds the thread spent actively running. Excludes idle time.

duration\_seconds: Optional[float]

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

startup\_seconds: Optional[float]

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

status: [BetaManagedAgentsSessionThreadStatus](api/beta.md)

SessionThreadStatus enum

Accepts one of the following:

"running"

"idle"

"rescheduling"

"terminated"

type: Literal["session\_thread"]

updated\_at: datetime

A timestamp in RFC 3339 format

usage: Optional[BetaManagedAgentsSessionThreadUsage]

Cumulative token usage for a session thread across all turns.

cache\_creation: Optional[BetaManagedAgentsCacheCreationUsage]

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Optional[int]

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Optional[int]

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Optional[int]

Total tokens read from prompt cache.

input\_tokens: Optional[int]

Total input tokens consumed across all turns.

output\_tokens: Optional[int]

Total output tokens generated across all turns.

class BetaManagedAgentsSessionThreadAgent: …

Resolved `agent` definition for a single `session_thread`. Snapshot of the agent at thread creation time. The multiagent roster is not repeated here; read it from `Session.agent`.

id: str

description: Optional[str]

mcp\_servers: List[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md)]

name: str

type: Literal["url"]

url: str

model: [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

Literal["claude-opus-4-7", "claude-opus-4-6", "claude-sonnet-4-6", 6 more]

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-6` - Most intelligent model for building agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding

Accepts one of the following:

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"

Most intelligent model for building agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

str

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: str

skills: List[Skill]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill: …

A resolved Anthropic-managed skill.

skill\_id: str

type: Literal["anthropic"]

version: str

class BetaManagedAgentsCustomSkill: …

A resolved user-created custom skill.

skill\_id: str

type: Literal["custom"]

version: str

system: Optional[str]

tools: List[Tool]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401: …

configs: List[[BetaManagedAgentsAgentToolConfig](api/beta.md)]

enabled: bool

name: Literal["bash", "edit", "read", 5 more]

Built-in agent tool identifier.

Accepts one of the following:

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

type: Literal["agent\_toolset\_20260401"]

class BetaManagedAgentsMCPToolset: …

configs: List[[BetaManagedAgentsMCPToolConfig](api/beta.md)]

enabled: bool

name: str

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy: …

Tool calls are automatically approved without user confirmation.

type: Literal["always\_allow"]

class BetaManagedAgentsAlwaysAskPolicy: …

Tool calls require user confirmation before execution.

type: Literal["always\_ask"]

mcp\_server\_name: str

type: Literal["mcp\_toolset"]

class BetaManagedAgentsCustomTool: …

A custom tool as returned in API responses.

description: str

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

properties: Optional[Dict[str, object]]

JSON Schema properties defining the tool's input parameters.

required: Optional[List[str]]

List of required property names.

type: Optional[Literal["object"]]

Must be 'object' for tool input schemas.

name: str

type: Literal["custom"]

type: Literal["agent"]

version: int

class BetaManagedAgentsSessionThreadStats: …

Timing statistics for a session thread.

active\_seconds: Optional[float]

Cumulative time in seconds the thread spent actively running. Excludes idle time.

duration\_seconds: Optional[float]

Elapsed time since thread creation in seconds. For archived threads, frozen at the final update.

startup\_seconds: Optional[float]

Time in seconds for the thread to begin running. Zero for child threads, which start immediately.

Literal["running", "idle", "rescheduling", "terminated"]

SessionThreadStatus enum

Accepts one of the following:

"running"

"idle"

"rescheduling"

"terminated"

class BetaManagedAgentsSessionThreadUsage: …

Cumulative token usage for a session thread across all turns.

cache\_creation: Optional[BetaManagedAgentsCacheCreationUsage]

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Optional[int]

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Optional[int]

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Optional[int]

Total tokens read from prompt cache.

input\_tokens: Optional[int]

Total input tokens consumed across all turns.

output\_tokens: Optional[int]

Total output tokens generated across all turns.

[BetaManagedAgentsStreamSessionThreadEvents](api/beta.md)

Server-sent event in a single thread's stream.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent: …

A user message event in the session conversation.

id: str

Unique identifier for this event.

content: List[Content]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

type: Literal["user.message"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent: …

An interrupt event that pauses agent execution and returns control to the user.

id: str

Unique identifier for this event.

type: Literal["user.interrupt"]

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.

class BetaManagedAgentsUserToolConfirmationEvent: …

A tool confirmation event that approves or denies a pending tool execution.

id: str

Unique identifier for this event.

result: Literal["allow", "deny"]

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: str

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.tool\_confirmation"]

deny\_message: Optional[str]

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.

class BetaManagedAgentsUserCustomToolResultEvent: …

Event sent by the client providing the result of a custom tool execution.

id: str

Unique identifier for this event.

custom\_tool\_use\_id: str

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: Literal["user.custom\_tool\_result"]

content: Optional[List[Content]]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

processed\_at: Optional[datetime]

A timestamp in RFC 3339 format

session\_thread\_id: Optional[str]

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.

class BetaManagedAgentsAgentCustomToolUseEvent: …

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

name: str

Name of the custom tool being called.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.custom\_tool\_use"]

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its custom tool use on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.custom_tool_result` event to route the result back.

class BetaManagedAgentsAgentMessageEvent: …

An agent response event in the session conversation.

id: str

Unique identifier for this event.

content: List[[BetaManagedAgentsTextBlock](api/beta.md)]

Array of text blocks comprising the agent response.

text: str

The text content.

type: Literal["text"]

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.message"]

class BetaManagedAgentsAgentThinkingEvent: …

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thinking"]

class BetaManagedAgentsAgentMCPToolUseEvent: …

Event emitted when the agent invokes a tool provided by an MCP server.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

mcp\_server\_name: str

Name of the MCP server providing the tool.

name: str

Name of the MCP tool being used.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.mcp\_tool\_use"]

evaluated\_permission: Optional[Literal["allow", "ask", "deny"]]

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentMCPToolResultEvent: …

Event representing the result of an MCP tool execution.

id: str

Unique identifier for this event.

mcp\_tool\_use\_id: str

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.mcp\_tool\_result"]

content: Optional[List[Content]]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent: …

Event emitted when the agent invokes a built-in agent tool.

id: str

Unique identifier for this event.

input: Dict[str, object]

Input parameters for the tool call.

name: str

Name of the agent tool being used.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.tool\_use"]

evaluated\_permission: Optional[Literal["allow", "ask", "deny"]]

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

session\_thread\_id: Optional[str]

When set, this event was cross-posted from a subagent's thread to surface its permission request on the primary thread's stream. Empty on the thread's own events. Echo this on a `user.tool_confirmation` event to route the approval back.

class BetaManagedAgentsAgentToolResultEvent: …

Event representing the result of an agent tool execution.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

tool\_use\_id: str

The id of the `agent.tool_use` event this result corresponds to.

type: Literal["agent.tool\_result"]

content: Optional[List[Content]]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

is\_error: Optional[bool]

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadMessageReceivedEvent: …

Delivery event written to the target thread's input stream when an agent-to-agent message arrives.

id: str

Unique identifier for this event.

content: List[Content]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

from\_session\_thread\_id: str

Public `sthr_` ID of the thread that sent the message.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thread\_message\_received"]

from\_agent\_name: Optional[str]

Name of the callable agent this message came from. Absent when received from the primary agent.

class BetaManagedAgentsAgentThreadMessageSentEvent: …

Observability event emitted to the sender's output stream when an agent-to-agent message is sent.

id: str

Unique identifier for this event.

content: List[Content]

Message content blocks.

Accepts one of the following:

class BetaManagedAgentsTextBlock: …

Regular text content.

text: str

The text content.

type: Literal["text"]

class BetaManagedAgentsImageBlock: …

Image content specified directly as base64 data or as a reference via a URL.

source: Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource: …

Base64-encoded image data.

data: str

Base64-encoded image data.

media\_type: str

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: Literal["base64"]

class BetaManagedAgentsURLImageSource: …

Image referenced by URL.

type: Literal["url"]

url: str

URL of the image to fetch.

class BetaManagedAgentsFileImageSource: …

Image referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["image"]

class BetaManagedAgentsDocumentBlock: …

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource: …

Base64-encoded document data.

data: str

Base64-encoded document data.

media\_type: str

MIME type of the document (e.g., "application/pdf").

type: Literal["base64"]

class BetaManagedAgentsPlainTextDocumentSource: …

Plain text document content.

data: str

The plain text content.

media\_type: Literal["text/plain"]

MIME type of the text content. Must be "text/plain".

type: Literal["text"]

class BetaManagedAgentsURLDocumentSource: …

Document referenced by URL.

type: Literal["url"]

url: str

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource: …

Document referenced by file ID.

file\_id: str

ID of a previously uploaded file.

type: Literal["file"]

type: Literal["document"]

context: Optional[str]

Additional context about the document for the model.

title: Optional[str]

The title of the document.

processed\_at: datetime

A timestamp in RFC 3339 format

to\_session\_thread\_id: str

Public `sthr_` ID of the thread the message was sent to.

type: Literal["agent.thread\_message\_sent"]

to\_agent\_name: Optional[str]

Name of the callable agent this message was sent to. Absent when sent to the primary agent.

class BetaManagedAgentsAgentThreadContextCompactedEvent: …

Indicates that context compaction (summarization) occurred during the session.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["agent.thread\_context\_compacted"]

class BetaManagedAgentsSessionErrorEvent: …

An error event indicating a problem occurred during session execution.

id: str

Unique identifier for this event.

error: Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError: …

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["unknown\_error"]

class BetaManagedAgentsModelOverloadedError: …

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_overloaded\_error"]

class BetaManagedAgentsModelRateLimitedError: …

The model request was rate-limited.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_rate\_limited\_error"]

class BetaManagedAgentsModelRequestFailedError: …

A model request failed for a reason other than overload or rate-limiting.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["model\_request\_failed\_error"]

class BetaManagedAgentsMCPConnectionFailedError: …

Failed to connect to an MCP server.

mcp\_server\_name: str

Name of the MCP server that failed to connect.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["mcp\_connection\_failed\_error"]

class BetaManagedAgentsMCPAuthenticationFailedError: …

Authentication to an MCP server failed.

mcp\_server\_name: str

Name of the MCP server that failed authentication.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["mcp\_authentication\_failed\_error"]

class BetaManagedAgentsBillingError: …

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: str

Human-readable error description.

retry\_status: RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying: …

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: Literal["retrying"]

class BetaManagedAgentsRetryStatusExhausted: …

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: Literal["exhausted"]

class BetaManagedAgentsRetryStatusTerminal: …

The session encountered a terminal error and will transition to `terminated` state.

type: Literal["terminal"]

type: Literal["billing\_error"]

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.error"]

class BetaManagedAgentsSessionStatusRescheduledEvent: …

Indicates the session is recovering from an error state and is rescheduled for execution.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_rescheduled"]

class BetaManagedAgentsSessionStatusRunningEvent: …

Indicates the session is actively running and the agent is working.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_running"]

class BetaManagedAgentsSessionStatusIdleEvent: …

Indicates the agent has paused and is awaiting user input.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

stop\_reason: StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn: …

The agent completed its turn naturally and is ready for the next user message.

type: Literal["end\_turn"]

class BetaManagedAgentsSessionRequiresAction: …

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: List[str]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: Literal["requires\_action"]

class BetaManagedAgentsSessionRetriesExhausted: …

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: Literal["retries\_exhausted"]

type: Literal["session.status\_idle"]

class BetaManagedAgentsSessionStatusTerminatedEvent: …

Indicates the session has terminated, either due to an error or completion.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.status\_terminated"]

class BetaManagedAgentsSessionThreadCreatedEvent: …

Emitted when a subagent is spawned as a new thread. Written to the parent thread's output stream so clients observing the session see child creation.

id: str

Unique identifier for this event.

agent\_name: str

Name of the callable agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public `sthr_` ID of the newly created thread.

type: Literal["session.thread\_created"]

class BetaManagedAgentsSpanOutcomeEvaluationStartEvent: …

Emitted when an outcome evaluation cycle begins.

id: str

Unique identifier for this event.

iteration: int

0-indexed revision cycle. 0 is the first evaluation; 1 is the re-evaluation after the first revision; etc.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.outcome\_evaluation\_start"]

class BetaManagedAgentsSpanOutcomeEvaluationEndEvent: …

Emitted when an outcome evaluation cycle completes. Carries the verdict and aggregate token usage. A verdict of `needs_revision` means another evaluation cycle follows; `satisfied`, `max_iterations_reached`, `failed`, or `interrupted` are terminal — no further evaluation cycles follow.

id: str

Unique identifier for this event.

explanation: str

Human-readable explanation of the verdict. For `needs_revision`, describes which criteria failed and why.

iteration: int

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_evaluation\_start\_id: str

The id of the corresponding `span.outcome_evaluation_start` event.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

result: str

Evaluation verdict. 'satisfied': criteria met, session goes idle. 'needs\_revision': criteria not met, another revision cycle follows. 'max\_iterations\_reached': evaluation budget exhausted with criteria still unmet — one final acknowledgment turn follows before the session goes idle, but no further evaluation runs. 'failed': grader determined the rubric does not apply to the deliverables. 'interrupted': user sent an interrupt while evaluation was in progress.

type: Literal["span.outcome\_evaluation\_end"]

usage: [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

cache\_creation\_input\_tokens: int

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: int

Tokens read from prompt cache in this request.

input\_tokens: int

Input tokens consumed by this request.

output\_tokens: int

Output tokens generated by this request.

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

class BetaManagedAgentsSpanModelRequestStartEvent: …

Emitted when a model request is initiated by the agent.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.model\_request\_start"]

class BetaManagedAgentsSpanModelRequestEndEvent: …

Emitted when a model request completes.

id: str

Unique identifier for this event.

is\_error: Optional[bool]

Whether the model request resulted in an error.

model\_request\_start\_id: str

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

cache\_creation\_input\_tokens: int

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: int

Tokens read from prompt cache in this request.

input\_tokens: int

Input tokens consumed by this request.

output\_tokens: int

Output tokens generated by this request.

speed: Optional[Literal["standard", "fast"]]

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.model\_request\_end"]

class BetaManagedAgentsSpanOutcomeEvaluationOngoingEvent: …

Periodic heartbeat emitted while an outcome evaluation cycle is in progress. Distinguishes 'evaluation is actively running' from 'evaluation is stuck' between the corresponding `span.outcome_evaluation_start` and `span.outcome_evaluation_end` events.

id: str

Unique identifier for this event.

iteration: int

0-indexed revision cycle, matching the corresponding `span.outcome_evaluation_start`.

outcome\_id: str

The `outc_` ID of the outcome being evaluated.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["span.outcome\_evaluation\_ongoing"]

class BetaManagedAgentsUserDefineOutcomeEvent: …

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

id: str

Unique identifier for this event.

description: str

What the agent should produce. Copied from the input event.

max\_iterations: Optional[int]

Evaluate-then-revise cycles before giving up. Default 3, max 20.

outcome\_id: str

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

processed\_at: datetime

A timestamp in RFC 3339 format

rubric: Rubric

Rubric for grading the quality of an outcome.

Accepts one of the following:

class BetaManagedAgentsFileRubric: …

Rubric referenced by a file uploaded via the Files API.

file\_id: str

ID of the rubric file.

type: Literal["file"]

class BetaManagedAgentsTextRubric: …

Rubric content provided inline as text.

content: str

Rubric content. Plain text or markdown — the grader treats it as freeform text.

type: Literal["text"]

type: Literal["user.define\_outcome"]

class BetaManagedAgentsSessionDeletedEvent: …

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: str

Unique identifier for this event.

processed\_at: datetime

A timestamp in RFC 3339 format

type: Literal["session.deleted"]

class BetaManagedAgentsSessionThreadStatusRunningEvent: …

A session thread has begun executing. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that started running.

type: Literal["session.thread\_status\_running"]

class BetaManagedAgentsSessionThreadStatusIdleEvent: …

A session thread has yielded and is awaiting input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that went idle.

stop\_reason: StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn: …

The agent completed its turn naturally and is ready for the next user message.

type: Literal["end\_turn"]

class BetaManagedAgentsSessionRequiresAction: …

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: List[str]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: Literal["requires\_action"]

class BetaManagedAgentsSessionRetriesExhausted: …

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: Literal["retries\_exhausted"]

type: Literal["session.thread\_status\_idle"]

class BetaManagedAgentsSessionThreadStatusTerminatedEvent: …

A session thread has terminated and will accept no further input. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that terminated.

type: Literal["session.thread\_status\_terminated"]

class BetaManagedAgentsSessionThreadStatusRescheduledEvent: …

A session thread hit a transient error and is retrying automatically. Emitted on the thread's own stream and cross-posted to the primary stream for child threads.

id: str

Unique identifier for this event.

agent\_name: str

Name of the agent the thread runs.

processed\_at: datetime

A timestamp in RFC 3339 format

session\_thread\_id: str

Public sthr\_ ID of the thread that is retrying.

type: Literal["session.thread\_status\_rescheduled"]

#### ThreadsEvents

##### [List Session Thread Events](api/beta/sessions/threads/events/list.md)

beta.sessions.threads.events.list(strthread\_id, EventListParams\*\*kwargs)  -> SyncPageCursor[[BetaManagedAgentsSessionEvent](api/beta.md)]

GET/v1/sessions/{session\_id}/threads/{thread\_id}/events

##### [Stream Session Thread Events](api/beta/sessions/threads/events/stream.md)

beta.sessions.threads.events.stream(strthread\_id, EventStreamParams\*\*kwargs)  -> [BetaManagedAgentsStreamSessionThreadEvents](api/beta.md)

GET/v1/sessions/{session\_id}/threads/{thread\_id}/stream

---

*Copyright © Anthropic. All rights reserved.*
