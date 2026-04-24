# Sessions

Copy page

Ruby

# Sessions

##### [Create Session](api/beta/sessions/create.md)

beta.sessions.create(\*\*kwargs) -> [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

beta.sessions.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more } >

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

beta.sessions.retrieve(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

beta.sessions.update(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

beta.sessions.delete(session\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedSession](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

beta.sessions.archive(session\_id, \*\*kwargs) -> [BetaManagedAgentsSession](api/beta.md) { id, agent, archived\_at, 11 more }

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgentParams { id, type, version }

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

id: String

The `agent` ID.

type: :agent

version: Integer

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCacheCreationUsage { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsDeletedSession { id, type }

Confirmation that a `session` has been permanently deleted.

id: String

type: :session\_deleted

class BetaManagedAgentsFileResourceParams { file\_id, type, mount\_path }

Mount a file uploaded via the Files API into the session.

file\_id: String

ID of a previously uploaded file.

type: :file

mount\_path: String

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

class BetaManagedAgentsGitHubRepositoryResourceParams { authorization\_token, type, url, 2 more }

Mount a GitHub repository into the session's container.

authorization\_token: String

GitHub authorization token used to clone the repository.

type: :github\_repository

url: String

Github URL of the repository

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Branch or commit to check out. Defaults to the repository's default branch.

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

mount\_path: String

Mount path in the container. Defaults to `/workspace/<repo-name>`.

class BetaManagedAgentsMemoryStoreResourceParam { memory\_store\_id, type, access, instructions }

Parameters for attaching a memory store to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

class BetaManagedAgentsSession { id, agent, archived\_at, 11 more }

A Managed Agents `session`.

id: String

agent: [BetaManagedAgentsSessionAgent](api/beta.md) { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

environment\_id: String

metadata: Hash[Symbol, String]

resources: Array[[BetaManagedAgentsSessionResource](api/beta.md)]

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

stats: [BetaManagedAgentsSessionStats](api/beta.md) { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds: Float

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: Float

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

status: :rescheduling | :running | :idle | :terminated

SessionStatus enum

Accepts one of the following:

:rescheduling

:running

:idle

:terminated

title: String

type: :session

updated\_at: Time

A timestamp in RFC 3339 format

usage: [BetaManagedAgentsSessionUsage](api/beta.md) { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Integer

Total tokens read from prompt cache.

input\_tokens: Integer

Total input tokens consumed across all turns.

output\_tokens: Integer

Total output tokens generated across all turns.

vault\_ids: Array[String]

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

class BetaManagedAgentsSessionAgent { id, description, mcp\_servers, 7 more }

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

id: String

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 6 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-6"

Most intelligent model for building agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

String

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

name: String

skills: Array[[BetaManagedAgentsAnthropicSkill](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkill](api/beta.md) { skill\_id, type, version } ]

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

system\_: String

tools: Array[[BetaManagedAgentsAgentToolset20260401](api/beta.md) { configs, default\_config, type }  | [BetaManagedAgentsMCPToolset](api/beta.md) { configs, default\_config, mcp\_server\_name, type }  | [BetaManagedAgentsCustomTool](api/beta.md) { description, input\_schema, name, type } ]

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401 { configs, default\_config, type }

configs: Array[[BetaManagedAgentsAgentToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: :bash | :edit | :read | 5 more

Built-in agent tool identifier.

Accepts one of the following:

:bash

:edit

:read

:write

:glob

:grep

:web\_fetch

:web\_search

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for agent tools.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

type: :agent\_toolset\_20260401

class BetaManagedAgentsMCPToolset { configs, default\_config, mcp\_server\_name, type }

configs: Array[[BetaManagedAgentsMCPToolConfig](api/beta.md) { enabled, name, permission\_policy } ]

enabled: bool

name: String

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md) { enabled, permission\_policy }

Resolved default configuration for all tools from an MCP server.

enabled: bool

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

mcp\_server\_name: String

type: :mcp\_toolset

class BetaManagedAgentsCustomTool { description, input\_schema, name, type }

A custom tool as returned in API responses.

description: String

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

type: :custom

type: :agent

version: Integer

class BetaManagedAgentsSessionStats { active\_seconds, duration\_seconds }

Timing statistics for a session.

active\_seconds: Float

Cumulative time in seconds the session spent in running status. Excludes idle time.

duration\_seconds: Float

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

class BetaManagedAgentsSessionUsage { cache\_creation, cache\_read\_input\_tokens, input\_tokens, output\_tokens }

Cumulative token usage for a session across all turns.

cache\_creation: [BetaManagedAgentsCacheCreationUsage](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Prompt-cache creation token usage broken down by cache lifetime.

ephemeral\_1h\_input\_tokens: Integer

Tokens used to create 1-hour ephemeral cache entries.

ephemeral\_5m\_input\_tokens: Integer

Tokens used to create 5-minute ephemeral cache entries.

cache\_read\_input\_tokens: Integer

Total tokens read from prompt cache.

input\_tokens: Integer

Total input tokens consumed across all turns.

output\_tokens: Integer

Total output tokens generated across all turns.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

beta.sessions.events.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionEvent](api/beta.md)>

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

beta.sessions.events.send\_(session\_id, \*\*kwargs) -> [BetaManagedAgentsSendSessionEvents](api/beta.md) { data }

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

beta.sessions.events.stream(session\_id, \*\*kwargs) -> [BetaManagedAgentsStreamSessionEvents](api/beta.md)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

BetaManagedAgentsEventParams = [BetaManagedAgentsUserMessageEventParams](api/beta.md) { content, type }  | [BetaManagedAgentsUserInterruptEventParams](api/beta.md) { type }  | [BetaManagedAgentsUserToolConfirmationEventParams](api/beta.md) { result, tool\_use\_id, type, deny\_message }  | [BetaManagedAgentsUserCustomToolResultEventParams](api/beta.md) { custom\_tool\_use\_id, type, content, is\_error }

Union type for event parameters that can be sent to a session.

Accepts one of the following:

class BetaManagedAgentsUserMessageEventParams { content, type }

Parameters for sending a user message to the session.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

class BetaManagedAgentsUserInterruptEventParams { type }

Parameters for sending an interrupt to pause the agent.

type: :"user.interrupt"

class BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

class BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

class BetaManagedAgentsSendSessionEvents { data }

Events that were successfully sent to the session.

data: Array[[BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | [BetaManagedAgentsUserCustomToolResultEvent](api/beta.md) { id, custom\_tool\_use\_id, type, 3 more } ]

Sent events

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

BetaManagedAgentsSessionEvent = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | 17 more

Union type for all event types in a session.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelUsage { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

BetaManagedAgentsStreamSessionEvents = [BetaManagedAgentsUserMessageEvent](api/beta.md) { id, content, type, processed\_at }  | [BetaManagedAgentsUserInterruptEvent](api/beta.md) { id, type, processed\_at }  | [BetaManagedAgentsUserToolConfirmationEvent](api/beta.md) { id, result, tool\_use\_id, 3 more }  | 17 more

Server-sent event in the session stream.

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent { id, input, name, 2 more }

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the custom tool being called.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.custom\_tool\_use"

class BetaManagedAgentsAgentMessageEvent { id, content, processed\_at, type }

An agent response event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type } ]

Array of text blocks comprising the agent response.

text: String

The text content.

type: :text

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.message"

class BetaManagedAgentsAgentThinkingEvent { id, processed\_at, type }

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thinking"

class BetaManagedAgentsAgentMCPToolUseEvent { id, input, mcp\_server\_name, 4 more }

Event emitted when the agent invokes a tool provided by an MCP server.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

mcp\_server\_name: String

Name of the MCP server providing the tool.

name: String

Name of the MCP tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentMCPToolResultEvent { id, mcp\_tool\_use\_id, processed\_at, 3 more }

Event representing the result of an MCP tool execution.

id: String

Unique identifier for this event.

mcp\_tool\_use\_id: String

The id of the `agent.mcp_tool_use` event this result corresponds to.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.mcp\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent { id, input, name, 3 more }

Event emitted when the agent invokes a built-in agent tool.

id: String

Unique identifier for this event.

input: Hash[Symbol, untyped]

Input parameters for the tool call.

name: String

Name of the agent tool being used.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.tool\_use"

evaluated\_permission: :allow | :ask | :deny

AgentEvaluatedPermission enum

Accepts one of the following:

:allow

:ask

:deny

class BetaManagedAgentsAgentToolResultEvent { id, processed\_at, tool\_use\_id, 3 more }

Event representing the result of an agent tool execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

tool\_use\_id: String

The id of the `agent.tool_use` event this result corresponds to.

type: :"agent.tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent { id, processed\_at, type }

Indicates that context compaction (summarization) occurred during the session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"agent.thread\_context\_compacted"

class BetaManagedAgentsSessionErrorEvent { id, error, processed\_at, type }

An error event indicating a problem occurred during session execution.

id: String

Unique identifier for this event.

error: [BetaManagedAgentsUnknownError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelOverloadedError](api/beta.md) { message, retry\_status, type }  | [BetaManagedAgentsModelRateLimitedError](api/beta.md) { message, retry\_status, type }  | 4 more

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsModelOverloadedError { message, retry\_status, type }

The model is currently overloaded. Emitted after automatic retries are exhausted.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_overloaded\_error

class BetaManagedAgentsModelRateLimitedError { message, retry\_status, type }

The model request was rate-limited.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_rate\_limited\_error

class BetaManagedAgentsModelRequestFailedError { message, retry\_status, type }

A model request failed for a reason other than overload or rate-limiting.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :model\_request\_failed\_error

class BetaManagedAgentsMCPConnectionFailedError { mcp\_server\_name, message, retry\_status, type }

Failed to connect to an MCP server.

mcp\_server\_name: String

Name of the MCP server that failed to connect.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_connection\_failed\_error

class BetaManagedAgentsMCPAuthenticationFailedError { mcp\_server\_name, message, retry\_status, type }

Authentication to an MCP server failed.

mcp\_server\_name: String

Name of the MCP server that failed authentication.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :mcp\_authentication\_failed\_error

class BetaManagedAgentsBillingError { message, retry\_status, type }

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :billing\_error

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.error"

class BetaManagedAgentsSessionStatusRescheduledEvent { id, processed\_at, type }

Indicates the session is recovering from an error state and is rescheduled for execution.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_rescheduled"

class BetaManagedAgentsSessionStatusRunningEvent { id, processed\_at, type }

Indicates the session is actively running and the agent is working.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_running"

class BetaManagedAgentsSessionStatusIdleEvent { id, processed\_at, stop\_reason, type }

Indicates the agent has paused and is awaiting user input.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

stop\_reason: [BetaManagedAgentsSessionEndTurn](api/beta.md) { type }  | [BetaManagedAgentsSessionRequiresAction](api/beta.md) { event\_ids, type }  | [BetaManagedAgentsSessionRetriesExhausted](api/beta.md) { type }

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn { type }

The agent completed its turn naturally and is ready for the next user message.

type: :end\_turn

class BetaManagedAgentsSessionRequiresAction { event\_ids, type }

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

event\_ids: Array[String]

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

type: :requires\_action

class BetaManagedAgentsSessionRetriesExhausted { type }

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

type: :retries\_exhausted

type: :"session.status\_idle"

class BetaManagedAgentsSessionStatusTerminatedEvent { id, processed\_at, type }

Indicates the session has terminated, either due to an error or completion.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.status\_terminated"

class BetaManagedAgentsSpanModelRequestStartEvent { id, processed\_at, type }

Emitted when a model request is initiated by the agent.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_start"

class BetaManagedAgentsSpanModelRequestEndEvent { id, is\_error, model\_request\_start\_id, 3 more }

Emitted when a model request completes.

id: String

Unique identifier for this event.

is\_error: bool

Whether the model request resulted in an error.

model\_request\_start\_id: String

The id of the corresponding `span.model_request_start` event.

model\_usage: [BetaManagedAgentsSpanModelUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Token usage for a single model request.

cache\_creation\_input\_tokens: Integer

Tokens used to create prompt cache in this request.

cache\_read\_input\_tokens: Integer

Tokens read from prompt cache in this request.

input\_tokens: Integer

Input tokens consumed by this request.

output\_tokens: Integer

Output tokens generated by this request.

speed: :standard | :fast

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

:standard

:fast

processed\_at: Time

A timestamp in RFC 3339 format

type: :"span.model\_request\_end"

class BetaManagedAgentsSessionDeletedEvent { id, processed\_at, type }

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

id: String

Unique identifier for this event.

processed\_at: Time

A timestamp in RFC 3339 format

type: :"session.deleted"

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsUnknownError { message, retry\_status, type }

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

message: String

Human-readable error description.

retry\_status: [BetaManagedAgentsRetryStatusRetrying](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusExhausted](api/beta.md) { type }  | [BetaManagedAgentsRetryStatusTerminal](api/beta.md) { type }

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying { type }

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

type: :retrying

class BetaManagedAgentsRetryStatusExhausted { type }

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

type: :exhausted

class BetaManagedAgentsRetryStatusTerminal { type }

The session encountered a terminal error and will transition to `terminated` state.

type: :terminal

type: :unknown\_error

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsUserCustomToolResultEvent { id, custom\_tool\_use\_id, type, 3 more }

Event sent by the client providing the result of a custom tool execution.

id: String

Unique identifier for this event.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEventParams { custom\_tool\_use\_id, type, content, is\_error }

Parameters for providing the result of a custom tool execution.

custom\_tool\_use\_id: String

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.custom\_tool\_result"

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

is\_error: bool

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserInterruptEvent { id, type, processed\_at }

An interrupt event that pauses agent execution and returns control to the user.

id: String

Unique identifier for this event.

type: :"user.interrupt"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEventParams { type }

Parameters for sending an interrupt to pause the agent.

type: :"user.interrupt"

class BetaManagedAgentsUserMessageEvent { id, content, type, processed\_at }

A user message event in the session conversation.

id: String

Unique identifier for this event.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserMessageEventParams { content, type }

Parameters for sending a user message to the session.

content: Array[[BetaManagedAgentsTextBlock](api/beta.md) { text, type }  | [BetaManagedAgentsImageBlock](api/beta.md) { source, type }  | [BetaManagedAgentsDocumentBlock](api/beta.md) { source, type, context, title } ]

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock { text, type }

Regular text content.

text: String

The text content.

type: :text

class BetaManagedAgentsImageBlock { source, type }

Image content specified directly as base64 data or as a reference via a URL.

source: [BetaManagedAgentsBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLImageSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileImageSource](api/beta.md) { file\_id, type }

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource { data, media\_type, type }

Base64-encoded image data.

data: String

Base64-encoded image data.

media\_type: String

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

type: :base64

class BetaManagedAgentsURLImageSource { type, url }

Image referenced by URL.

type: :url

url: String

URL of the image to fetch.

class BetaManagedAgentsFileImageSource { file\_id, type }

Image referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :image

class BetaManagedAgentsDocumentBlock { source, type, context, title }

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

source: [BetaManagedAgentsBase64DocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsPlainTextDocumentSource](api/beta.md) { data, media\_type, type }  | [BetaManagedAgentsURLDocumentSource](api/beta.md) { type, url }  | [BetaManagedAgentsFileDocumentSource](api/beta.md) { file\_id, type }

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource { data, media\_type, type }

Base64-encoded document data.

data: String

Base64-encoded document data.

media\_type: String

MIME type of the document (e.g., "application/pdf").

type: :base64

class BetaManagedAgentsPlainTextDocumentSource { data, media\_type, type }

Plain text document content.

data: String

The plain text content.

media\_type: :"text/plain"

MIME type of the text content. Must be "text/plain".

type: :text

class BetaManagedAgentsURLDocumentSource { type, url }

Document referenced by URL.

type: :url

url: String

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource { file\_id, type }

Document referenced by file ID.

file\_id: String

ID of a previously uploaded file.

type: :file

type: :document

context: String

Additional context about the document for the model.

title: String

The title of the document.

type: :"user.message"

class BetaManagedAgentsUserToolConfirmationEvent { id, result, tool\_use\_id, 3 more }

A tool confirmation event that approves or denies a pending tool execution.

id: String

Unique identifier for this event.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

processed\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEventParams { result, tool\_use\_id, type, deny\_message }

Parameters for confirming or denying a tool execution request.

result: :allow | :deny

UserToolConfirmationResult enum

Accepts one of the following:

:allow

:deny

tool\_use\_id: String

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

type: :"user.tool\_confirmation"

deny\_message: String

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

beta.sessions.resources.add(session\_id, \*\*kwargs) -> [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

beta.sessions.resources.list(session\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsSessionResource](api/beta.md)>

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

beta.sessions.resources.retrieve(resource\_id, \*\*kwargs) -> [ResourceRetrieveResponse](api/beta.md)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

beta.sessions.resources.update(resource\_id, \*\*kwargs) -> [ResourceUpdateResponse](api/beta.md)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

beta.sessions.resources.delete(resource\_id, \*\*kwargs) -> [BetaManagedAgentsDeleteSessionResource](api/beta.md) { id, type }

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource { id, type }

Confirmation of resource deletion.

id: String

type: :session\_resource\_deleted

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }  | [BetaManagedAgentsMemoryStoreResource](api/beta.md) { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }  | [BetaManagedAgentsMemoryStoreResource](api/beta.md) { memory\_store\_id, type, access, 4 more }

The requested session resource.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }  | [BetaManagedAgentsMemoryStoreResource](api/beta.md) { memory\_store\_id, type, access, 4 more }

The updated session resource.

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource { id, created\_at, mount\_path, 4 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

mount\_path: String

type: :github\_repository

updated\_at: Time

A timestamp in RFC 3339 format

url: String

checkout: [BetaManagedAgentsBranchCheckout](api/beta.md) { name, type }  | [BetaManagedAgentsCommitCheckout](api/beta.md) { sha, type }

Accepts one of the following:

class BetaManagedAgentsBranchCheckout { name, type }

name: String

Branch name to check out.

type: :branch

class BetaManagedAgentsCommitCheckout { sha, type }

sha: String

Full commit SHA to check out.

type: :commit

class BetaManagedAgentsFileResource { id, created\_at, file\_id, 3 more }

id: String

created\_at: Time

A timestamp in RFC 3339 format

file\_id: String

mount\_path: String

type: :file

updated\_at: Time

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource { memory\_store\_id, type, access, 4 more }

A memory store attached to an agent session.

memory\_store\_id: String

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

type: :memory\_store

access: :read\_write | :read\_only

Access mode for an attached memory store.

Accepts one of the following:

:read\_write

:read\_only

description: String

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

instructions: String

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

mount\_path: String

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

name: String

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

---

*Copyright © Anthropic. All rights reserved.*
