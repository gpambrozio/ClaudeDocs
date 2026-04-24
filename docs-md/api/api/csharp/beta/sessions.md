# Sessions

Copy page

C#

# Sessions

##### [Create Session](api/beta/sessions/create.md)

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Create(SessionCreateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

[SessionListPageResponse](api/beta.md) Beta.Sessions.List(SessionListParams?parameters, CancellationTokencancellationToken = default)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Retrieve(SessionRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Update(SessionUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

[BetaManagedAgentsDeletedSession](api/beta.md) Beta.Sessions.Delete(SessionDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

[BetaManagedAgentsSession](api/beta.md) Beta.Sessions.Archive(SessionArchiveParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgentParams:

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

required string ID

The `agent` ID.

required Type Type

Int Version

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCacheCreationUsage:

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsDeletedSession:

Confirmation that a `session` has been permanently deleted.

required string ID

required Type Type

class BetaManagedAgentsFileResourceParams:

Mount a file uploaded via the Files API into the session.

required string FileID

ID of a previously uploaded file.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

class BetaManagedAgentsGitHubRepositoryResourceParams:

Mount a GitHub repository into the session's container.

required string AuthorizationToken

GitHub authorization token used to clone the repository.

required Type Type

required string Url

Github URL of the repository

Checkout? Checkout

Branch or commit to check out. Defaults to the repository's default branch.

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

string? MountPath

Mount path in the container. Defaults to `/workspace/<repo-name>`.

class BetaManagedAgentsMemoryStoreResourceParam:

Parameters for attaching a memory store to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type

Access? Access

Access mode for an attached memory store.

Accepts one of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

class BetaManagedAgentsSession:

A Managed Agents `session`.

required string ID

required [BetaManagedAgentsSessionAgent](api/beta.md) Agent

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description

required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> McpServers

required string Name

required Type Type

required string Url

required [BetaManagedAgentsModelConfig](api/beta.md) Model

Model identifier and configuration.

required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required string Name

required IReadOnlyList<Skill> Skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System

required IReadOnlyList<Tool> Tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type

class BetaManagedAgentsMcpToolset:

required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description

required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

required string Name

required Type Type

required Type Type

required Int Version

required DateTimeOffset? ArchivedAt

A timestamp in RFC 3339 format

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string EnvironmentID

required IReadOnlyDictionary<string, string> Metadata

required IReadOnlyList<[BetaManagedAgentsSessionResource](api/beta.md)> Resources

Accepts one of the following:

class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url

Checkout? Checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type

Access? Access

Access mode for an attached memory store.

Accepts one of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string Description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

string? MountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

string? Name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

required [BetaManagedAgentsSessionStats](api/beta.md) Stats

Timing statistics for a session.

Double ActiveSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Double DurationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

required Status Status

SessionStatus enum

Accepts one of the following:

"rescheduling"Rescheduling

"running"Running

"idle"Idle

"terminated"Terminated

required string? Title

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required [BetaManagedAgentsSessionUsage](api/beta.md) Usage

Cumulative token usage for a session across all turns.

[BetaManagedAgentsCacheCreationUsage](api/beta.md) CacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Int CacheReadInputTokens

Total tokens read from prompt cache.

Int InputTokens

Total input tokens consumed across all turns.

Int OutputTokens

Total output tokens generated across all turns.

required IReadOnlyList<string> VaultIds

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

class BetaManagedAgentsSessionAgent:

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

required string ID

required string? Description

required IReadOnlyList<[BetaManagedAgentsMcpServerUrlDefinition](api/beta.md)> McpServers

required string Name

required Type Type

required string Url

required [BetaManagedAgentsModelConfig](api/beta.md) Model

Model identifier and configuration.

required [BetaManagedAgentsModel](api/beta.md) ID

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

"claude-opus-4-7"ClaudeOpus4\_7

Frontier intelligence for long-running agents and coding

"claude-opus-4-6"ClaudeOpus4\_6

Most intelligent model for building agents and coding

"claude-sonnet-4-6"ClaudeSonnet4\_6

Best combination of speed and intelligence

"claude-haiku-4-5"ClaudeHaiku4\_5

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"ClaudeHaiku4\_5\_20251001

Fastest model with near-frontier intelligence

"claude-opus-4-5"ClaudeOpus4\_5

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"ClaudeOpus4\_5\_20251101

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"ClaudeSonnet4\_5

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"ClaudeSonnet4\_5\_20250929

High-performance model for agents and coding

Speed Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required string Name

required IReadOnlyList<Skill> Skills

Accepts one of the following:

class BetaManagedAgentsAnthropicSkill:

A resolved Anthropic-managed skill.

required string SkillID

required Type Type

required string Version

class BetaManagedAgentsCustomSkill:

A resolved user-created custom skill.

required string SkillID

required Type Type

required string Version

required string? System

required IReadOnlyList<Tool> Tools

Accepts one of the following:

class BetaManagedAgentsAgentToolset20260401:

required IReadOnlyList<[BetaManagedAgentsAgentToolConfig](api/beta.md)> Configs

required Boolean Enabled

required Name Name

Built-in agent tool identifier.

Accepts one of the following:

"bash"Bash

"edit"Edit

"read"Read

"write"Write

"glob"Glob

"grep"Grep

"web\_fetch"WebFetch

"web\_search"WebSearch

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for agent tools.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required Type Type

class BetaManagedAgentsMcpToolset:

required IReadOnlyList<[BetaManagedAgentsMcpToolConfig](api/beta.md)> Configs

required Boolean Enabled

required string Name

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required [BetaManagedAgentsMcpToolsetDefaultConfig](api/beta.md) DefaultConfig

Resolved default configuration for all tools from an MCP server.

required Boolean Enabled

required PermissionPolicy PermissionPolicy

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy:

Tool calls are automatically approved without user confirmation.

required Type Type

class BetaManagedAgentsAlwaysAskPolicy:

Tool calls require user confirmation before execution.

required Type Type

required string McpServerName

required Type Type

class BetaManagedAgentsCustomTool:

A custom tool as returned in API responses.

required string Description

required [BetaManagedAgentsCustomToolInputSchema](api/beta.md) InputSchema

JSON Schema for custom tool input parameters.

IReadOnlyDictionary<string, JsonElement>? Properties

JSON Schema properties defining the tool's input parameters.

IReadOnlyList<string> Required

List of required property names.

Type Type

Must be 'object' for tool input schemas.

required string Name

required Type Type

required Type Type

required Int Version

class BetaManagedAgentsSessionStats:

Timing statistics for a session.

Double ActiveSeconds

Cumulative time in seconds the session spent in running status. Excludes idle time.

Double DurationSeconds

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

class BetaManagedAgentsSessionUsage:

Cumulative token usage for a session across all turns.

[BetaManagedAgentsCacheCreationUsage](api/beta.md) CacheCreation

Prompt-cache creation token usage broken down by cache lifetime.

Int Ephemeral1hInputTokens

Tokens used to create 1-hour ephemeral cache entries.

Int Ephemeral5mInputTokens

Tokens used to create 5-minute ephemeral cache entries.

Int CacheReadInputTokens

Total tokens read from prompt cache.

Int InputTokens

Total input tokens consumed across all turns.

Int OutputTokens

Total output tokens generated across all turns.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

[EventListPageResponse](api/beta.md) Beta.Sessions.Events.List(EventListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

[BetaManagedAgentsSendSessionEvents](api/beta.md) Beta.Sessions.Events.Send(EventSendParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

[BetaManagedAgentsStreamSessionEvents](api/beta.md) Beta.Sessions.Events.StreamStreaming(EventStreamParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

class BetaManagedAgentsEventParams: A class that can be one of several variants.union

Union type for event parameters that can be sent to a session.

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

required IReadOnlyList<Content> Content

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

required Type Type

class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

class BetaManagedAgentsSendSessionEvents:

Events that were successfully sent to the session.

IReadOnlyList<Data> Data

Sent events

Accepts one of the following:

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionEvent: A class that can be one of several variants.union

Union type for all event types in a session.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelUsage:

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

class BetaManagedAgentsStreamSessionEvents: A class that can be one of several variants.union

Server-sent event in the session stream.

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsAgentCustomToolUseEvent:

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the custom tool being called.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMessageEvent:

An agent response event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<[BetaManagedAgentsTextBlock](api/beta.md)> Content

Array of text blocks comprising the agent response.

required string Text

The text content.

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentThinkingEvent:

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsAgentMcpToolUseEvent:

Event emitted when the agent invokes a tool provided by an MCP server.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string McpServerName

Name of the MCP server providing the tool.

required string Name

Name of the MCP tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentMcpToolResultEvent:

Event representing the result of an MCP tool execution.

required string ID

Unique identifier for this event.

required string McpToolUseID

The id of the `agent.mcp_tool_use` event this result corresponds to.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentToolUseEvent:

Event emitted when the agent invokes a built-in agent tool.

required string ID

Unique identifier for this event.

required IReadOnlyDictionary<string, JsonElement> Input

Input parameters for the tool call.

required string Name

Name of the agent tool being used.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

EvaluatedPermission EvaluatedPermission

AgentEvaluatedPermission enum

Accepts one of the following:

"allow"Allow

"ask"Ask

"deny"Deny

class BetaManagedAgentsAgentToolResultEvent:

Event representing the result of an agent tool execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsAgentThreadContextCompactedEvent:

Indicates that context compaction (summarization) occurred during the session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionErrorEvent:

An error event indicating a problem occurred during session execution.

required string ID

Unique identifier for this event.

required Error Error

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelOverloadedError:

The model is currently overloaded. Emitted after automatic retries are exhausted.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRateLimitedError:

The model request was rate-limited.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsModelRequestFailedError:

A model request failed for a reason other than overload or rate-limiting.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpConnectionFailedError:

Failed to connect to an MCP server.

required string McpServerName

Name of the MCP server that failed to connect.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsMcpAuthenticationFailedError:

Authentication to an MCP server failed.

required string McpServerName

Name of the MCP server that failed authentication.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsBillingError:

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRescheduledEvent:

Indicates the session is recovering from an error state and is rescheduled for execution.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusRunningEvent:

Indicates the session is actively running and the agent is working.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionStatusIdleEvent:

Indicates the agent has paused and is awaiting user input.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required StopReason StopReason

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

class BetaManagedAgentsSessionEndTurn:

The agent completed its turn naturally and is ready for the next user message.

required Type Type

class BetaManagedAgentsSessionRequiresAction:

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

required IReadOnlyList<string> EventIds

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

required Type Type

class BetaManagedAgentsSessionRetriesExhausted:

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

required Type Type

required Type Type

class BetaManagedAgentsSessionStatusTerminatedEvent:

Indicates the session has terminated, either due to an error or completion.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestStartEvent:

Emitted when a model request is initiated by the agent.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSpanModelRequestEndEvent:

Emitted when a model request completes.

required string ID

Unique identifier for this event.

required Boolean? IsError

Whether the model request resulted in an error.

required string ModelRequestStartID

The id of the corresponding `span.model_request_start` event.

required [BetaManagedAgentsSpanModelUsage](api/beta.md) ModelUsage

Token usage for a single model request.

required Int CacheCreationInputTokens

Tokens used to create prompt cache in this request.

required Int CacheReadInputTokens

Tokens read from prompt cache in this request.

required Int InputTokens

Input tokens consumed by this request.

required Int OutputTokens

Output tokens generated by this request.

Speed? Speed

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

"standard"Standard

"fast"Fast

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsSessionDeletedEvent:

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

required string ID

Unique identifier for this event.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format

required Type Type

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsUnknownError:

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

required string Message

Human-readable error description.

required RetryStatus RetryStatus

What the client should do next in response to this error.

Accepts one of the following:

class BetaManagedAgentsRetryStatusRetrying:

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

required Type Type

class BetaManagedAgentsRetryStatusExhausted:

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

required Type Type

class BetaManagedAgentsRetryStatusTerminal:

The session encountered a terminal error and will transition to `terminated` state.

required Type Type

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

IReadOnlyList<Content> Content

The result content returned by the tool.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

Boolean? IsError

Whether the tool execution resulted in an error.

class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

required Type Type

class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.

required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.

required IReadOnlyList<Content> Content

Array of content blocks for the user message.

Accepts one of the following:

class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type

class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.

required Source Source

Union type for image source variants.

Accepts one of the following:

class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type

class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.

class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

required Source Source

Union type for document source variants.

Accepts one of the following:

class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type

class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type

class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.

class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.

required Result Result

UserToolConfirmationResult enum

Accepts one of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

[BetaManagedAgentsFileResource](api/beta.md) Beta.Sessions.Resources.Add(ResourceAddParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

[ResourceListPageResponse](api/beta.md) Beta.Sessions.Resources.List(ResourceListParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

[ResourceRetrieveResponse](api/beta.md) Beta.Sessions.Resources.Retrieve(ResourceRetrieveParamsparameters, CancellationTokencancellationToken = default)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

[ResourceUpdateResponse](api/beta.md) Beta.Sessions.Resources.Update(ResourceUpdateParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

[BetaManagedAgentsDeleteSessionResource](api/beta.md) Beta.Sessions.Resources.Delete(ResourceDeleteParamsparameters, CancellationTokencancellationToken = default)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

class BetaManagedAgentsDeleteSessionResource:

Confirmation of resource deletion.

required string ID

required Type Type

class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url

Checkout? Checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type

Access? Access

Access mode for an attached memory store.

Accepts one of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string Description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

string? MountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

string? Name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

class BetaManagedAgentsSessionResource: A class that can be one of several variants.union

A memory store attached to an agent session.

class BetaManagedAgentsGitHubRepositoryResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

required string Url

Checkout? Checkout

Accepts one of the following:

class BetaManagedAgentsBranchCheckout:

required string Name

Branch name to check out.

required Type Type

class BetaManagedAgentsCommitCheckout:

required string Sha

Full commit SHA to check out.

required Type Type

class BetaManagedAgentsFileResource:

required string ID

required DateTimeOffset CreatedAt

A timestamp in RFC 3339 format

required string FileID

required string MountPath

required Type Type

required DateTimeOffset UpdatedAt

A timestamp in RFC 3339 format

class BetaManagedAgentsMemoryStoreResource:

A memory store attached to an agent session.

required string MemoryStoreID

The memory store ID (memstore\_...). Must belong to the caller's organization and workspace.

required Type Type

Access? Access

Access mode for an attached memory store.

Accepts one of the following:

"read\_write"ReadWrite

"read\_only"ReadOnly

string Description

Description of the memory store, snapshotted at attach time. Rendered into the agent's system prompt. Empty string when the store has no description.

string? Instructions

Per-attachment guidance for the agent on how to use this store. Rendered into the memory section of the system prompt. Max 4096 chars.

string? MountPath

Filesystem path where the store is mounted in the session container, e.g. /mnt/memory/user-preferences. Derived from the store's name. Output-only.

string? Name

Display name of the memory store, snapshotted at attach time. Later edits to the store's name do not propagate to this resource.

---

*Copyright © Anthropic. All rights reserved.*
