# Sessions

Copy page

TypeScript

# Sessions

##### [Create Session](api/beta/sessions/create.md)

client.beta.sessions.create(SessionCreateParams { agent, environment\_id, metadata, 4 more } params, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

client.beta.sessions.list(SessionListParams { agent\_id, agent\_version, createdAtGt, 8 more } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more } >

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

client.beta.sessions.retrieve(stringsessionID, SessionRetrieveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

client.beta.sessions.update(stringsessionID, SessionUpdateParams { metadata, title, vault\_ids, betas } params, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

client.beta.sessions.delete(stringsessionID, SessionDeleteParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsDeletedSession](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

client.beta.sessions.archive(stringsessionID, SessionArchiveParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

BetaManagedAgentsAgentParams { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: string

The `agent` ID.

type: "agent"

version?: number

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCacheCreationUsage { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens?: number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens?: number

Tokens used to create 5-minute ephemeral cache entries.

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsDeletedSession { id, type }

Confirmation that a `session` has been permanently deleted.

id: string

type: "session\_deleted"

BetaManagedAgentsFileResourceParams { file\_id, type, mount\_path }

Mount a file uploaded via the Files API into the session.

file\_id: string

ID of a previously uploaded file.

type: "file"

mount\_path?: string | null

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

BetaManagedAgentsGitHubRepositoryResourceParams { authorization\_token, type, url, 2 more }

Mount a GitHub repository into the session's container.

authorization\_token: string

GitHub authorization token used to clone the repository.

type: "github\_repository"

url: string

Github URL of the repository

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Branch or commit to check out. Defaults to the repository's default branch.

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

mount\_path?: string | null

Mount path in the container. Defaults to `/workspace/<repo-name>`.

BetaManagedAgentsSession { id, agent, archived\_at, 11 more }

A Managed Agents `session`.

id: string

agent: [BetaManagedAgentsSessionAgent](api/beta.md) { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string | null

mcp\_servers: Array<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } >

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more

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

(string & {})

speed?: "standard" | "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: string

skills: Array<[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } >

Accepts one of the following:

BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string | null

tools: Array<[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } >

Accepts one of the following:

BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array<[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } >

enabled: boolean

name: "bash" | "edit" | "read" | 5 more

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array<[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } >

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties?: Record<string, unknown> | null

JSON Schema properties defining the tool's input parameters.

required?: Array<string>

List of required property names.

type?: "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

archived\_at: string | null

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

environment\_id: string

metadata: Record<string, string>

resources: Array<[BetaManagedAgentsSessionResource](api/beta.md)>

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

stats: [BetaManagedAgentsSessionStats](api/beta.md) { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds?: number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds?: number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

status: "rescheduling" | "running" | "idle" | "terminated"

SessionStatus enum

Accepts one of the following:

"rescheduling"

"running"

"idle"

"terminated"

title: string | null

type: "session"

updated\_at: string

A timestamp in RFC 3339 format

usage: [BetaManagedAgentsSessionUsage](api/beta.md) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation?: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens?: number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens?: number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens?: number

Total tokens read from prompt cache.

input\_tokens?: number

Total input tokens consumed across all turns.

output\_tokens?: number

Total output tokens generated across all turns.

vault\_ids: Array<string>

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

BetaManagedAgentsSessionAgent { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: string

description: string | null

mcp\_servers: Array<[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } >

name: string

type: "url"

url: string

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-6" | "claude-sonnet-4-6" | "claude-haiku-4-5" | 5 more

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

(string & {})

speed?: "standard" | "fast"

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

name: string

skills: Array<[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } >

Accepts one of the following:

BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

version: string

BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

version: string

system: string | null

tools: Array<[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } >

Accepts one of the following:

BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array<[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } >

enabled: boolean

name: "bash" | "edit" | "read" | 5 more

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

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

type: "agent\_toolset\_20260401"

BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array<[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } >

enabled: boolean

name: string

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: boolean

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

mcp\_server\_name: string

type: "mcp\_toolset"

BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: string

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties?: Record<string, unknown> | null

JSON Schema properties defining the tool's input parameters.

required?: Array<string>

List of required property names.

type?: "object"

Must be 'object' for tool input schemas.

name: string

type: "custom"

type: "agent"

version: number

BetaManagedAgentsSessionStats { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds?: number

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds?: number

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

BetaManagedAgentsSessionUsage { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation?: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens?: number

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens?: number

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens?: number

Total tokens read from prompt cache.

input\_tokens?: number

Total input tokens consumed across all turns.

output\_tokens?: number

Total output tokens generated across all turns.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

client.beta.sessions.events.list(stringsessionID, EventListParams { limit, order, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

client.beta.sessions.events.send(stringsessionID, EventSendParams { events, betas } params, RequestOptionsoptions?): [BetaManagedAgentsSendSessionEvents](api/beta.md) { data }

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

client.beta.sessions.events.stream(stringsessionID, EventStreamParams { betas } params?, RequestOptionsoptions?): [BetaManagedAgentsStreamSessionEvents](api/beta.md) | Stream<[BetaManagedAgentsStreamSessionEvents](api/beta.md)>

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

evaluated\_permission?: "allow" | "ask" | "deny"

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type } >

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

evaluated\_permission?: "allow" | "ask" | "deny"

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

BetaManagedAgentsEventParams = [BetaManagedAgentsUserMessageEventParams](api/beta.md) { content, type }  | [BetaManagedAgentsUserInterruptEventParams](api/beta.md) { type }  | [BetaManagedAgentsUserToolConfirmationEventParams](api/beta.md) { result, tool\_use\_id, type, deny\_message }  | [BetaManagedAgentsUserCustomToolResultEventParams](api/beta.md) { custom\_tool\_use\_id, type, content, is\_error }

Union type for event parameters that can be sent to a session.

Accepts one of the following:

BetaManagedAgentsUserMessageEventParams { content, type }

Parameters for sending a user message to the session.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

Array of content blocks for the user message.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

type: "user.message"

BetaManagedAgentsUserInterruptEventParams { type }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: "allow" | "deny"

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message?: string | null

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

BetaManagedAgentsSendSessionEvents { data }

Events that were successfully sent to the session.

data?: Array<[BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | [BetaManagedAgentsUserCustomToolResultEvent](api/beta.md) { id, custom\_tool\_use\_id, type, 3 more } >

Sent events

Accepts one of the following:

BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

Array of content blocks comprising the user message.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

type: "user.message"

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" | "deny"

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message?: string | null

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

BetaManagedAgentsSessionEvent = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | 17 more

Union type for all event types in a session.

Accepts one of the following:

BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

Array of content blocks comprising the user message.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

type: "user.message"

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" | "deny"

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message?: string | null

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type } >

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

evaluated\_permission?: "allow" | "ask" | "deny"

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

evaluated\_permission?: "allow" | "ask" | "deny"

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array<string>

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.status\_idle"

BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean | null

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed?: "standard" | "fast" | null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array<string>

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array<string>

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.status\_idle"

BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean | null

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed?: "standard" | "fast" | null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

BetaManagedAgentsSpanModelUsage { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed?: "standard" | "fast" | null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

BetaManagedAgentsStreamSessionEvents = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | 17 more

Server-sent event in the session stream.

Accepts one of the following:

BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

Array of content blocks comprising the user message.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

type: "user.message"

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" | "deny"

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message?: string | null

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

name: string

Name of the custom tool being called.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.custom\_tool\_use"

BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: string

Unique identifier for this event.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type } >

Array of text blocks comprising the agent response.

text: string

The text content.

type: "text"

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.message"

BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thinking"

BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

mcp\_server\_name: string

Name of the MCP server providing the tool.

name: string

Name of the MCP tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_use"

evaluated\_permission?: "allow" | "ask" | "deny"

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: string

Unique identifier for this event.

mcp\_tool\_use\_id: string

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.mcp\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: string

Unique identifier for this event.

input: Record<string, unknown>

Input parameters for the tool call.

name: string

Name of the agent tool being used.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.tool\_use"

evaluated\_permission?: "allow" | "ask" | "deny"

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"

"ask"

"deny"

BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

tool\_use\_id: string

The id of the `agent.tool_use` event this result corresponds to.

type: "agent.tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "agent.thread\_context\_compacted"

BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: string

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_overloaded\_error"

BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_rate\_limited\_error"

BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "model\_request\_failed\_error"

BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: string

Name of the MCP server that failed to connect.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_connection\_failed\_error"

BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: string

Name of the MCP server that failed authentication.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "mcp\_authentication\_failed\_error"

BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "billing\_error"

processed\_at: string

A timestamp in RFC 3339 format

type: "session.error"

BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_rescheduled"

BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_running"

BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: "end\_turn"

BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array<string>

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: "requires\_action"

BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: "retries\_exhausted"

type: "session.status\_idle"

BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.status\_terminated"

BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_start"

BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: string

Unique identifier for this event.

is\_error: boolean | null

Whether the model request resulted in an error.

model\_request\_start\_id: string

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: number

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: number

Tokens read from prompt cache in this request.

input\_tokens: number

Input tokens consumed by this request.

output\_tokens: number

Output tokens generated by this request.

speed?: "standard" | "fast" | null

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"

"fast"

processed\_at: string

A timestamp in RFC 3339 format

type: "span.model\_request\_end"

BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: string

Unique identifier for this event.

processed\_at: string

A timestamp in RFC 3339 format

type: "session.deleted"

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: string

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: "retrying"

BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: "exhausted"

BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: "terminal"

type: "unknown\_error"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: string

Unique identifier for this event.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.custom\_tool\_result"

content?: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

The result content returned by the tool.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

is\_error?: boolean | null

Whether the tool execution resulted in an error.

BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: string

Unique identifier for this event.

type: "user.interrupt"

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserInterruptEventParams { type }

Parameters for sending an interrupt to pause the agent.

type: "user.interrupt"

BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: string

Unique identifier for this event.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

Array of content blocks comprising the user message.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

type: "user.message"

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserMessageEventParams { content, type }

Parameters for sending a user message to the session.

content: Array<[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } >

Array of content blocks for the user message.

Accepts one of the following:

BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: string

The text content.

type: "text"

BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: string

Base64-encoded image data.

media\_type: string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: "base64"

BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: "url"

url: string

URL of the image to fetch.

BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "image"

BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: string

Base64-encoded document data.

media\_type: string

MIME type of the document (e.g., "application/pdf").

type: "base64"

BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: string

The plain text content.

media\_type: "text/plain"

MIME type of the text content. Must be "text/plain".

type: "text"

BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: "url"

url: string

URL of the document to fetch.

BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: string

ID of a previously uploaded file.

type: "file"

type: "document"

context?: string | null

Additional context about the document for the model.

title?: string | null

The title of the document.

type: "user.message"

BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: string

Unique identifier for this event.

result: "allow" | "deny"

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message?: string | null

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at?: string | null

A timestamp in RFC 3339 format

BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: "allow" | "deny"

UserToolConfirmationResult enum

Accepts one of the following:

"allow"

"deny"

tool\_use\_id: string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: "user.tool\_confirmation"

deny\_message?: string | null

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

client.beta.sessions.resources.add(stringsessionID, ResourceAddParams { file\_id, type, mount\_path, betas } params, RequestOptionsoptions?): [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

client.beta.sessions.resources.list(stringsessionID, ResourceListParams { limit, page, betas } params?, RequestOptionsoptions?): PageCursor<[BetaManagedAgentsSessionResource](api/beta.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

client.beta.sessions.resources.retrieve(stringresourceID, ResourceRetrieveParams { session\_id, betas } params, RequestOptionsoptions?): [ResourceRetrieveResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

client.beta.sessions.resources.update(stringresourceID, ResourceUpdateParams { session\_id, authorization\_token, betas } params, RequestOptionsoptions?): [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

client.beta.sessions.resources.delete(stringresourceID, ResourceDeleteParams { session\_id, betas } params, RequestOptionsoptions?): [BetaManagedAgentsDeleteSessionResource](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

BetaManagedAgentsDeleteSessionResource { id, type }

Confirmation of resource deletion.

id: string

type: "session\_resource\_deleted"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

The requested session resource.

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

The updated session resource.

Accepts one of the following:

BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

mount\_path: string

type: "github\_repository"

updated\_at: string

A timestamp in RFC 3339 format

url: string

checkout?: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }  | null

Accepts one of the following:

BetaManagedAgentsBranchCheckout { name, type }

name: string

Branch name to check out.

type: "branch"

BetaManagedAgentsCommitCheckout { sha, type }

sha: string

Full commit SHA to check out.

type: "commit"

BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: string

created\_at: string

A timestamp in RFC 3339 format

file\_id: string

mount\_path: string

type: "file"

updated\_at: string

A timestamp in RFC 3339 format

---

*Copyright © Anthropic. All rights reserved.*
