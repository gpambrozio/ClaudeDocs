# Sessions

Copy page

CLI

# Sessions

##### [Create Session](api/beta/sessions/create.md)

$ ant beta:sessions create

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

$ ant beta:sessions list

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

$ ant beta:sessions retrieve

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

$ ant beta:sessions update

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

$ ant beta:sessions delete

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

$ ant beta:sessions archive

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

beta\_managed\_agents\_agent\_params: object { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

"agent"

version: optional number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

beta\_managed\_agents\_branch\_checkout: object { name, type }

name: string

Branch name to check out.

type: "branch"

"branch"

beta\_managed\_agents\_cache\_creation\_usage: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

beta\_managed\_agents\_commit\_checkout: object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

"commit"

beta\_managed\_agents\_deleted\_session: object { id, type }

Confirmation that a `session` has been permanently deleted.

id: string

type: "session\_deleted"

"session\_deleted"

beta\_managed\_agents\_file\_resource\_params: object { file\_id, type, mount\_path }

Mount a file uploaded via the Files API into the session.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

mount\_path: optional string

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

beta\_managed\_agents\_github\_repository\_resource\_params: object { authorization\_token, type, url, 2 more }

Mount a GitHub repository into the session's container.

authorization\_token: string

GitHub authorization token used to clone the repository.

type: "github\_repository"

"github\_repository"

url: string

Github URL of the repository

checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Branch or commit to check out. Defaults to the repository's default branch.

beta\_managed\_agents\_branch\_checkout: object { name, type }

name: string

Branch name to check out.

type: "branch"

"branch"

beta\_managed\_agents\_commit\_checkout: object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

"commit"

mount\_path: optional string

Mount path in the container. Defaults to `/workspace/<repo-name>`.

beta\_managed\_agents\_session: object { id, agent, archived\_at, 11 more }

A Managed Agents `session`.

id: string

agent: object { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url }

name: string

type: "url"

"url"

url: string

model: object { id, speed }

Model identifier and configuration.

id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version }

beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

"anthropic"

version: string

beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

"custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type }

beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

default\_config: object { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"

beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

default\_config: object { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

"mcp\_toolset"

beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: object { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

"object"

name: string

type: "custom"

"custom"

type: "agent"

"agent"

version: number

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

environment\_id: string

metadata: map[string]

resources: array of [BetaManagedAgentsSessionResource](api/beta.md)

beta\_managed\_agents\_github\_repository\_resource: object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

"github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

beta\_managed\_agents\_branch\_checkout: object { name, type }

name: string

Branch name to check out.

type: "branch"

"branch"

beta\_managed\_agents\_commit\_checkout: object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

"commit"

beta\_managed\_agents\_file\_resource: object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

"file"

updated\_at: string

A timestamp in RFC 3339 format

stats: object { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

status: "rescheduling" or "running" or "idle" or "terminated"

SessionStatus enum

"rescheduling"

"running"

"idle"

"terminated"

title: string

type: "session"

"session"

updated\_at: string

A timestamp in RFC 3339 format

usage: object { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation: optional object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.

vault\_ids: array of string

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

beta\_managed\_agents\_session\_agent: object { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url }

name: string

type: "url"

"url"

url: string

model: object { id, speed }

Model identifier and configuration.

id: "claude-opus-4-7" or "claude-opus-4-6" or "claude-sonnet-4-6" or 6 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

name: string

skills: array of [BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version }

beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

"anthropic"

version: string

beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

"custom"

version: string

system: string

tools: array of [BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  or [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  or [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type }

beta\_managed\_agents\_agent\_toolset20260401: object { configs, default\_config, type }

configs: array of [BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy }

enabled: boolean

name: "bash" or "edit" or "read" or 5 more

Built-in agent tool identifier.

"bash"

"edit"

"read"

"write"

"glob"

"grep"

"web\_fetch"

"web\_search"

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

default\_config: object { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"

beta\_managed\_agents\_mcp\_toolset: object { configs, default\_config, mcp\_server\_name, type }

configs: array of [BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy }

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

default\_config: object { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

"mcp\_toolset"

beta\_managed\_agents\_custom\_tool: object { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: object { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

"object"

name: string

type: "custom"

"custom"

type: "agent"

"agent"

version: number

beta\_managed\_agents\_session\_stats: object { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds: optional number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: optional number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

beta\_managed\_agents\_session\_usage: object { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation: optional object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: optional number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: optional number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: optional number

Total tokens read from prompt cache.

input\_tokens: optional number

Total input tokens consumed across all turns.

output\_tokens: optional number

Total output tokens generated across all turns.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

$ ant beta:sessions:events list

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

$ ant beta:sessions:events send

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

$ ant beta:sessions:events stream

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

beta\_managed\_agents\_agent\_custom\_tool\_use\_event: object { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

"agent.custom\_tool\_use"

beta\_managed\_agents\_agent\_mcp\_tool\_result\_event: object { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

"agent.mcp\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_agent\_mcp\_tool\_use\_event: object { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

"agent.mcp\_tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

beta\_managed\_agents\_agent\_message\_event: object { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

"text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

"agent.message"

beta\_managed\_agents\_agent\_thinking\_event: object { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

"agent.thinking"

beta\_managed\_agents\_agent\_thread\_context\_compacted\_event: object { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

"agent.thread\_context\_compacted"

beta\_managed\_agents\_agent\_tool\_result\_event: object { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

"agent.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_agent\_tool\_use\_event: object { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

"agent.tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_billing\_error: object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "billing\_error"

"billing\_error"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

beta\_managed\_agents\_event\_params: [BetaManagedAgentsUserMessageEventParams](api/beta.md) { content, type }  or [BetaManagedAgentsUserInterruptEventParams](api/beta.md) { type }  or [BetaManagedAgentsUserToolConfirmationEventParams](api/beta.md) { result, tool\_use\_id, type, deny\_message }  or [BetaManagedAgentsUserCustomToolResultEventParams](api/beta.md) { custom\_tool\_use\_id, type, content, is\_error }

Union type for event parameters that can be sent to a session.

beta\_managed\_agents\_user\_message\_event\_params: object { content, type }

Parameters for sending a user message to the session.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks for the user message.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

"user.message"

beta\_managed\_agents\_user\_interrupt\_event\_params: object { type }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

"user.interrupt"

beta\_managed\_agents\_user\_tool\_confirmation\_event\_params: object { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

beta\_managed\_agents\_user\_custom\_tool\_result\_event\_params: object { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

"user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_mcp\_authentication\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_authentication\_failed\_error"

"mcp\_authentication\_failed\_error"

beta\_managed\_agents\_mcp\_connection\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_connection\_failed\_error"

"mcp\_connection\_failed\_error"

beta\_managed\_agents\_model\_overloaded\_error: object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_overloaded\_error"

"model\_overloaded\_error"

beta\_managed\_agents\_model\_rate\_limited\_error: object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_rate\_limited\_error"

"model\_rate\_limited\_error"

beta\_managed\_agents\_model\_request\_failed\_error: object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_request\_failed\_error"

"model\_request\_failed\_error"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

beta\_managed\_agents\_send\_session\_events: object { data }

Events that were successfully sent to the session.

data: optional array of [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  or [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  or [BetaManagedAgentsUserCustomToolResultEvent](api/beta.md) { id, custom\_tool\_use\_id, type, 3 more }

Sent events

beta\_managed\_agents\_user\_message\_event: object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks comprising the user message.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

"user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_interrupt\_event: object { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

"user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_tool\_confirmation\_event: object { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_custom\_tool\_result\_event: object { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

"user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_session\_deleted\_event: object { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

"session.deleted"

beta\_managed\_agents\_session\_end\_turn: object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

"end\_turn"

beta\_managed\_agents\_session\_error\_event: object { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  or 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

beta\_managed\_agents\_unknown\_error: object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "unknown\_error"

"unknown\_error"

beta\_managed\_agents\_model\_overloaded\_error: object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_overloaded\_error"

"model\_overloaded\_error"

beta\_managed\_agents\_model\_rate\_limited\_error: object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_rate\_limited\_error"

"model\_rate\_limited\_error"

beta\_managed\_agents\_model\_request\_failed\_error: object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_request\_failed\_error"

"model\_request\_failed\_error"

beta\_managed\_agents\_mcp\_connection\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_connection\_failed\_error"

"mcp\_connection\_failed\_error"

beta\_managed\_agents\_mcp\_authentication\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_authentication\_failed\_error"

"mcp\_authentication\_failed\_error"

beta\_managed\_agents\_billing\_error: object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "billing\_error"

"billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

"session.error"

beta\_managed\_agents\_session\_event: [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  or [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  or 17 more

Union type for all event types in a session.

beta\_managed\_agents\_user\_message\_event: object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks comprising the user message.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

"user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_interrupt\_event: object { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

"user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_tool\_confirmation\_event: object { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_custom\_tool\_result\_event: object { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

"user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_agent\_custom\_tool\_use\_event: object { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

"agent.custom\_tool\_use"

beta\_managed\_agents\_agent\_message\_event: object { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

"text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

"agent.message"

beta\_managed\_agents\_agent\_thinking\_event: object { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

"agent.thinking"

beta\_managed\_agents\_agent\_mcp\_tool\_use\_event: object { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

"agent.mcp\_tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

beta\_managed\_agents\_agent\_mcp\_tool\_result\_event: object { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

"agent.mcp\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_agent\_tool\_use\_event: object { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

"agent.tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

beta\_managed\_agents\_agent\_tool\_result\_event: object { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

"agent.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_agent\_thread\_context\_compacted\_event: object { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

"agent.thread\_context\_compacted"

beta\_managed\_agents\_session\_error\_event: object { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  or 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

beta\_managed\_agents\_unknown\_error: object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "unknown\_error"

"unknown\_error"

beta\_managed\_agents\_model\_overloaded\_error: object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_overloaded\_error"

"model\_overloaded\_error"

beta\_managed\_agents\_model\_rate\_limited\_error: object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_rate\_limited\_error"

"model\_rate\_limited\_error"

beta\_managed\_agents\_model\_request\_failed\_error: object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_request\_failed\_error"

"model\_request\_failed\_error"

beta\_managed\_agents\_mcp\_connection\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_connection\_failed\_error"

"mcp\_connection\_failed\_error"

beta\_managed\_agents\_mcp\_authentication\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_authentication\_failed\_error"

"mcp\_authentication\_failed\_error"

beta\_managed\_agents\_billing\_error: object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "billing\_error"

"billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

"session.error"

beta\_managed\_agents\_session\_status\_rescheduled\_event: object { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

"session.status\_rescheduled"

beta\_managed\_agents\_session\_status\_running\_event: object { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

"session.status\_running"

beta\_managed\_agents\_session\_status\_idle\_event: object { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  or [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

beta\_managed\_agents\_session\_end\_turn: object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

"end\_turn"

beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

"requires\_action"

beta\_managed\_agents\_session\_retries\_exhausted: object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

"retries\_exhausted"

type: "session.status\_idle"

"session.status\_idle"

beta\_managed\_agents\_session\_status\_terminated\_event: object { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

"session.status\_terminated"

beta\_managed\_agents\_span\_model\_request\_start\_event: object { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

"span.model\_request\_start"

beta\_managed\_agents\_span\_model\_request\_end\_event: object { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

"span.model\_request\_end"

beta\_managed\_agents\_session\_deleted\_event: object { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

"session.deleted"

beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

"requires\_action"

beta\_managed\_agents\_session\_retries\_exhausted: object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

"retries\_exhausted"

beta\_managed\_agents\_session\_status\_idle\_event: object { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  or [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

beta\_managed\_agents\_session\_end\_turn: object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

"end\_turn"

beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

"requires\_action"

beta\_managed\_agents\_session\_retries\_exhausted: object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

"retries\_exhausted"

type: "session.status\_idle"

"session.status\_idle"

beta\_managed\_agents\_session\_status\_rescheduled\_event: object { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

"session.status\_rescheduled"

beta\_managed\_agents\_session\_status\_running\_event: object { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

"session.status\_running"

beta\_managed\_agents\_session\_status\_terminated\_event: object { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

"session.status\_terminated"

beta\_managed\_agents\_span\_model\_request\_end\_event: object { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

"span.model\_request\_end"

beta\_managed\_agents\_span\_model\_request\_start\_event: object { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

"span.model\_request\_start"

beta\_managed\_agents\_span\_model\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

beta\_managed\_agents\_stream\_session\_events: [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  or [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  or [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  or 17 more

Server-sent event in the session stream.

beta\_managed\_agents\_user\_message\_event: object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks comprising the user message.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

"user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_interrupt\_event: object { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

"user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_tool\_confirmation\_event: object { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_custom\_tool\_result\_event: object { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

"user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_agent\_custom\_tool\_use\_event: object { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

"agent.custom\_tool\_use"

beta\_managed\_agents\_agent\_message\_event: object { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

"text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

"agent.message"

beta\_managed\_agents\_agent\_thinking\_event: object { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

"agent.thinking"

beta\_managed\_agents\_agent\_mcp\_tool\_use\_event: object { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

"agent.mcp\_tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

beta\_managed\_agents\_agent\_mcp\_tool\_result\_event: object { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

"agent.mcp\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_agent\_tool\_use\_event: object { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: map[unknown]

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

"agent.tool\_use"

evaluated\_permission: optional "allow" or "ask" or "deny"

AgentEvaluatedPermission enum

"allow"

"ask"

"deny"

beta\_managed\_agents\_agent\_tool\_result\_event: object { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

"agent.tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_agent\_thread\_context\_compacted\_event: object { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

"agent.thread\_context\_compacted"

beta\_managed\_agents\_session\_error\_event: object { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  or [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  or [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  or 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

beta\_managed\_agents\_unknown\_error: object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "unknown\_error"

"unknown\_error"

beta\_managed\_agents\_model\_overloaded\_error: object { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_overloaded\_error"

"model\_overloaded\_error"

beta\_managed\_agents\_model\_rate\_limited\_error: object { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_rate\_limited\_error"

"model\_rate\_limited\_error"

beta\_managed\_agents\_model\_request\_failed\_error: object { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "model\_request\_failed\_error"

"model\_request\_failed\_error"

beta\_managed\_agents\_mcp\_connection\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_connection\_failed\_error"

"mcp\_connection\_failed\_error"

beta\_managed\_agents\_mcp\_authentication\_failed\_error: object { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "mcp\_authentication\_failed\_error"

"mcp\_authentication\_failed\_error"

beta\_managed\_agents\_billing\_error: object { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "billing\_error"

"billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

"session.error"

beta\_managed\_agents\_session\_status\_rescheduled\_event: object { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

"session.status\_rescheduled"

beta\_managed\_agents\_session\_status\_running\_event: object { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

"session.status\_running"

beta\_managed\_agents\_session\_status\_idle\_event: object { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  or [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  or [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

beta\_managed\_agents\_session\_end\_turn: object { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

"end\_turn"

beta\_managed\_agents\_session\_requires\_action: object { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: array of string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

"requires\_action"

beta\_managed\_agents\_session\_retries\_exhausted: object { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

"retries\_exhausted"

type: "session.status\_idle"

"session.status\_idle"

beta\_managed\_agents\_session\_status\_terminated\_event: object { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

"session.status\_terminated"

beta\_managed\_agents\_span\_model\_request\_start\_event: object { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

"span.model\_request\_start"

beta\_managed\_agents\_span\_model\_request\_end\_event: object { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed: optional "standard" or "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

"span.model\_request\_end"

beta\_managed\_agents\_session\_deleted\_event: object { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

"session.deleted"

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_unknown\_error: object { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  or [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

beta\_managed\_agents\_retry\_status\_retrying: object { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

"retrying"

beta\_managed\_agents\_retry\_status\_exhausted: object { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

"exhausted"

beta\_managed\_agents\_retry\_status\_terminal: object { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

"terminal"

type: "unknown\_error"

"unknown\_error"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_user\_custom\_tool\_result\_event: object { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

"user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_custom\_tool\_result\_event\_params: object { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

"user.custom\_tool\_result"

content: optional array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

The result content returned by the tool.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

is\_error: optional boolean

Whether the tool execution resulted in an error.

beta\_managed\_agents\_user\_interrupt\_event: object { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

"user.interrupt"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_interrupt\_event\_params: object { type }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

"user.interrupt"

beta\_managed\_agents\_user\_message\_event: object { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks comprising the user message.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

"user.message"

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_message\_event\_params: object { content, type }

Parameters for sending a user message to the session.

content: array of [BetaManagedAgentsTextBlock](api/beta.md) { text, type }  or [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  or [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title }

Array of content blocks for the user message.

beta\_managed\_agents\_text\_block: object { text, type }

Regular text content.

text: string

The text content.

type: "text"

"text"

beta\_managed\_agents\_image\_block: object { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

beta\_managed\_agents\_base64\_image\_source: object { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

"base64"

beta\_managed\_agents\_url\_image\_source: object { type, url }

Image referenced by URL.

type: "url"

"url"

url: string

URL of the image to fetch.

beta\_managed\_agents\_file\_image\_source: object { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "image"

"image"

beta\_managed\_agents\_document\_block: object { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  or [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  or [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

beta\_managed\_agents\_base64\_document\_source: object { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

"base64"

beta\_managed\_agents\_plain\_text\_document\_source: object { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

"text/plain"

type: "text"

"text"

beta\_managed\_agents\_url\_document\_source: object { type, url }

Document referenced by URL.

type: "url"

"url"

url: string

URL of the document to fetch.

beta\_managed\_agents\_file\_document\_source: object { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

"file"

type: "document"

"document"

context: optional string

Additional context about the document for the model.

title: optional string

The title of the document.

type: "user.message"

"user.message"

beta\_managed\_agents\_user\_tool\_confirmation\_event: object { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: optional string

A timestamp in RFC 3339 format

beta\_managed\_agents\_user\_tool\_confirmation\_event\_params: object { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: "allow" or "deny"

UserToolConfirmationResult enum

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

"user.tool\_confirmation"

deny\_message: optional string

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

$ ant beta:sessions:resources add

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

$ ant beta:sessions:resources list

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

$ ant beta:sessions:resources retrieve

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

$ ant beta:sessions:resources update

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

$ ant beta:sessions:resources delete

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

beta\_managed\_agents\_delete\_session\_resource: object { id, type }

Confirmation of resource deletion.

id: string

type: "session\_resource\_deleted"

"session\_resource\_deleted"

beta\_managed\_agents\_file\_resource: object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

"file"

updated\_at: string

A timestamp in RFC 3339 format

beta\_managed\_agents\_github\_repository\_resource: object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

"github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

beta\_managed\_agents\_branch\_checkout: object { name, type }

name: string

Branch name to check out.

type: "branch"

"branch"

beta\_managed\_agents\_commit\_checkout: object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

"commit"

beta\_managed\_agents\_session\_resource: [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  or [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

beta\_managed\_agents\_github\_repository\_resource: object { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

"github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout: optional [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  or [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

beta\_managed\_agents\_branch\_checkout: object { name, type }

name: string

Branch name to check out.

type: "branch"

"branch"

beta\_managed\_agents\_commit\_checkout: object { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

"commit"

beta\_managed\_agents\_file\_resource: object { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

"file"

updated\_at: string

A timestamp in RFC 3339 format

---

*Copyright © Anthropic. All rights reserved.*
