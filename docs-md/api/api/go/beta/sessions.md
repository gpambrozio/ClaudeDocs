# Sessions

Copy page

Go

# Sessions

##### [Create Session](api/beta/sessions/create.md)

client.Beta.Sessions.New(ctx, params) (\*[BetaManagedAgentsSession](api/beta.md), error)

POST/v1/sessions

##### [List Sessions](api/beta/sessions/list.md)

client.Beta.Sessions.List(ctx, params) (\*PageCursor[[BetaManagedAgentsSession](api/beta.md)], error)

GET/v1/sessions

##### [Get Session](api/beta/sessions/retrieve.md)

client.Beta.Sessions.Get(ctx, sessionID, query) (\*[BetaManagedAgentsSession](api/beta.md), error)

GET/v1/sessions/{session\_id}

##### [Update Session](api/beta/sessions/update.md)

client.Beta.Sessions.Update(ctx, sessionID, params) (\*[BetaManagedAgentsSession](api/beta.md), error)

POST/v1/sessions/{session\_id}

##### [Delete Session](api/beta/sessions/delete.md)

client.Beta.Sessions.Delete(ctx, sessionID, body) (\*[BetaManagedAgentsDeletedSession](api/beta.md), error)

DELETE/v1/sessions/{session\_id}

##### [Archive Session](api/beta/sessions/archive.md)

client.Beta.Sessions.Archive(ctx, sessionID, body) (\*[BetaManagedAgentsSession](api/beta.md), error)

POST/v1/sessions/{session\_id}/archive

##### ModelsExpand Collapse

type BetaManagedAgentsAgentParamsResp struct{…}

Specification for an Agent. Provide a specific `version` or use the short-form `agent="agent_id"` for the most recent version

ID string

The `agent` ID.

Type BetaManagedAgentsAgentParamsType

Version int64optional

The specific `agent` version to use. Omit to use the latest version. Must be at least 1 if specified.

type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType

type BetaManagedAgentsCacheCreationUsage struct{…}

Prompt-cache creation token usage broken down by cache lifetime.

Ephemeral1hInputTokens int64optional

Tokens used to create 1-hour ephemeral cache entries.

Ephemeral5mInputTokens int64optional

Tokens used to create 5-minute ephemeral cache entries.

type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

type BetaManagedAgentsDeletedSession struct{…}

Confirmation that a `session` has been permanently deleted.

ID string

Type BetaManagedAgentsDeletedSessionType

type BetaManagedAgentsFileResourceParamsResp struct{…}

Mount a file uploaded via the Files API into the session.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileResourceParamsType

MountPath stringoptional

Mount path in the container. Defaults to `/mnt/session/uploads/<file_id>`.

type BetaManagedAgentsGitHubRepositoryResourceParamsResp struct{…}

Mount a GitHub repository into the session's container.

AuthorizationToken string

GitHub authorization token used to clone the repository.

Type BetaManagedAgentsGitHubRepositoryResourceParamsType

URL string

Github URL of the repository

Checkout BetaManagedAgentsGitHubRepositoryResourceParamsCheckoutUnionRespoptional

Branch or commit to check out. Defaults to the repository's default branch.

Accepts one of the following:

type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType

type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

MountPath stringoptional

Mount path in the container. Defaults to `/workspace/<repo-name>`.

type BetaManagedAgentsSession struct{…}

A Managed Agents `session`.

ID string

Agent [BetaManagedAgentsSessionAgent](api/beta.md)

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

ID string

Description string

MCPServers [][BetaManagedAgentsMCPServerURLDefinition](api/beta.md)

Name string

Type BetaManagedAgentsMCPServerURLDefinitionType

URL string

Model [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.

ID BetaManagedAgentsModel

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type BetaManagedAgentsModel string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const BetaManagedAgentsModelClaudeOpus4\_6 BetaManagedAgentsModel = "claude-opus-4-6"

Most intelligent model for building agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_6 BetaManagedAgentsModel = "claude-sonnet-4-6"

Best combination of speed and intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5 BetaManagedAgentsModel = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5\_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeOpus4\_5 BetaManagedAgentsModel = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeOpus4\_5\_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeSonnet4\_5 BetaManagedAgentsModel = "claude-sonnet-4-5"

High-performance model for agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_5\_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

Speed BetaManagedAgentsModelConfigSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"

const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"

Name string

Skills []BetaManagedAgentsSessionAgentSkillUnion

Accepts one of the following:

type BetaManagedAgentsAnthropicSkill struct{…}

A resolved Anthropic-managed skill.

SkillID string

Type BetaManagedAgentsAnthropicSkillType

Version string

type BetaManagedAgentsCustomSkill struct{…}

A resolved user-created custom skill.

SkillID string

Type BetaManagedAgentsCustomSkillType

Version string

System string

Tools []BetaManagedAgentsSessionAgentToolUnion

Accepts one of the following:

type BetaManagedAgentsAgentToolset20260401 struct{…}

Configs [][BetaManagedAgentsAgentToolConfig](api/beta.md)

Enabled bool

Name BetaManagedAgentsAgentToolConfigName

Built-in agent tool identifier.

Accepts one of the following:

const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"

const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"

const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"

const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"

const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"

const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"

const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web\_fetch"

const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web\_search"

PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

DefaultConfig [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

Enabled bool

PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

Type BetaManagedAgentsAgentToolset20260401Type

type BetaManagedAgentsMCPToolset struct{…}

Configs [][BetaManagedAgentsMCPToolConfig](api/beta.md)

Enabled bool

Name string

PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

DefaultConfig [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

Enabled bool

PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

MCPServerName string

Type BetaManagedAgentsMCPToolsetType

type BetaManagedAgentsCustomTool struct{…}

A custom tool as returned in API responses.

Description string

InputSchema [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

Properties map[string, any]optional

JSON Schema properties defining the tool's input parameters.

Required []stringoptional

List of required property names.

Type BetaManagedAgentsCustomToolInputSchemaTypeoptional

Must be 'object' for tool input schemas.

Name string

Type BetaManagedAgentsCustomToolType

Type BetaManagedAgentsSessionAgentType

Version int64

ArchivedAt Time

A timestamp in RFC 3339 format

CreatedAt Time

A timestamp in RFC 3339 format

EnvironmentID string

Metadata map[string, string]

Resources [][BetaManagedAgentsSessionResourceUnion](api/beta.md)

Accepts one of the following:

type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string

Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionoptional

Accepts one of the following:

type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType

type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

Stats [BetaManagedAgentsSessionStats](api/beta.md)

Timing statistics for a session.

ActiveSeconds float64optional

Cumulative time in seconds the session spent in running status. Excludes idle time.

DurationSeconds float64optional

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

Status BetaManagedAgentsSessionStatus

SessionStatus enum

Accepts one of the following:

const BetaManagedAgentsSessionStatusRescheduling BetaManagedAgentsSessionStatus = "rescheduling"

const BetaManagedAgentsSessionStatusRunning BetaManagedAgentsSessionStatus = "running"

const BetaManagedAgentsSessionStatusIdle BetaManagedAgentsSessionStatus = "idle"

const BetaManagedAgentsSessionStatusTerminated BetaManagedAgentsSessionStatus = "terminated"

Title string

Type BetaManagedAgentsSessionType

UpdatedAt Time

A timestamp in RFC 3339 format

Usage [BetaManagedAgentsSessionUsage](api/beta.md)

Cumulative token usage for a session across all turns.

CacheCreation [BetaManagedAgentsCacheCreationUsage](api/beta.md)optional

Prompt-cache creation token usage broken down by cache lifetime.

Ephemeral1hInputTokens int64optional

Tokens used to create 1-hour ephemeral cache entries.

Ephemeral5mInputTokens int64optional

Tokens used to create 5-minute ephemeral cache entries.

CacheReadInputTokens int64optional

Total tokens read from prompt cache.

InputTokens int64optional

Total input tokens consumed across all turns.

OutputTokens int64optional

Total output tokens generated across all turns.

VaultIDs []string

Vault IDs attached to the session at creation. Empty when no vaults were supplied.

type BetaManagedAgentsSessionAgent struct{…}

Resolved `agent` definition for a `session`. Snapshot of the `agent` at `session` creation time.

ID string

Description string

MCPServers [][BetaManagedAgentsMCPServerURLDefinition](api/beta.md)

Name string

Type BetaManagedAgentsMCPServerURLDefinitionType

URL string

Model [BetaManagedAgentsModelConfig](api/beta.md)

Model identifier and configuration.

ID BetaManagedAgentsModel

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

type BetaManagedAgentsModel string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

const BetaManagedAgentsModelClaudeOpus4\_6 BetaManagedAgentsModel = "claude-opus-4-6"

Most intelligent model for building agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_6 BetaManagedAgentsModel = "claude-sonnet-4-6"

Best combination of speed and intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5 BetaManagedAgentsModel = "claude-haiku-4-5"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeHaiku4\_5\_20251001 BetaManagedAgentsModel = "claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

const BetaManagedAgentsModelClaudeOpus4\_5 BetaManagedAgentsModel = "claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeOpus4\_5\_20251101 BetaManagedAgentsModel = "claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

const BetaManagedAgentsModelClaudeSonnet4\_5 BetaManagedAgentsModel = "claude-sonnet-4-5"

High-performance model for agents and coding

const BetaManagedAgentsModelClaudeSonnet4\_5\_20250929 BetaManagedAgentsModel = "claude-sonnet-4-5-20250929"

High-performance model for agents and coding

string

Speed BetaManagedAgentsModelConfigSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsModelConfigSpeedStandard BetaManagedAgentsModelConfigSpeed = "standard"

const BetaManagedAgentsModelConfigSpeedFast BetaManagedAgentsModelConfigSpeed = "fast"

Name string

Skills []BetaManagedAgentsSessionAgentSkillUnion

Accepts one of the following:

type BetaManagedAgentsAnthropicSkill struct{…}

A resolved Anthropic-managed skill.

SkillID string

Type BetaManagedAgentsAnthropicSkillType

Version string

type BetaManagedAgentsCustomSkill struct{…}

A resolved user-created custom skill.

SkillID string

Type BetaManagedAgentsCustomSkillType

Version string

System string

Tools []BetaManagedAgentsSessionAgentToolUnion

Accepts one of the following:

type BetaManagedAgentsAgentToolset20260401 struct{…}

Configs [][BetaManagedAgentsAgentToolConfig](api/beta.md)

Enabled bool

Name BetaManagedAgentsAgentToolConfigName

Built-in agent tool identifier.

Accepts one of the following:

const BetaManagedAgentsAgentToolConfigNameBash BetaManagedAgentsAgentToolConfigName = "bash"

const BetaManagedAgentsAgentToolConfigNameEdit BetaManagedAgentsAgentToolConfigName = "edit"

const BetaManagedAgentsAgentToolConfigNameRead BetaManagedAgentsAgentToolConfigName = "read"

const BetaManagedAgentsAgentToolConfigNameWrite BetaManagedAgentsAgentToolConfigName = "write"

const BetaManagedAgentsAgentToolConfigNameGlob BetaManagedAgentsAgentToolConfigName = "glob"

const BetaManagedAgentsAgentToolConfigNameGrep BetaManagedAgentsAgentToolConfigName = "grep"

const BetaManagedAgentsAgentToolConfigNameWebFetch BetaManagedAgentsAgentToolConfigName = "web\_fetch"

const BetaManagedAgentsAgentToolConfigNameWebSearch BetaManagedAgentsAgentToolConfigName = "web\_search"

PermissionPolicy BetaManagedAgentsAgentToolConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

DefaultConfig [BetaManagedAgentsAgentToolsetDefaultConfig](api/beta.md)

Resolved default configuration for agent tools.

Enabled bool

PermissionPolicy BetaManagedAgentsAgentToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

Type BetaManagedAgentsAgentToolset20260401Type

type BetaManagedAgentsMCPToolset struct{…}

Configs [][BetaManagedAgentsMCPToolConfig](api/beta.md)

Enabled bool

Name string

PermissionPolicy BetaManagedAgentsMCPToolConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

DefaultConfig [BetaManagedAgentsMCPToolsetDefaultConfig](api/beta.md)

Resolved default configuration for all tools from an MCP server.

Enabled bool

PermissionPolicy BetaManagedAgentsMCPToolsetDefaultConfigPermissionPolicyUnion

Permission policy for tool execution.

Accepts one of the following:

type BetaManagedAgentsAlwaysAllowPolicy struct{…}

Tool calls are automatically approved without user confirmation.

Type BetaManagedAgentsAlwaysAllowPolicyType

type BetaManagedAgentsAlwaysAskPolicy struct{…}

Tool calls require user confirmation before execution.

Type BetaManagedAgentsAlwaysAskPolicyType

MCPServerName string

Type BetaManagedAgentsMCPToolsetType

type BetaManagedAgentsCustomTool struct{…}

A custom tool as returned in API responses.

Description string

InputSchema [BetaManagedAgentsCustomToolInputSchema](api/beta.md)

JSON Schema for custom tool input parameters.

Properties map[string, any]optional

JSON Schema properties defining the tool's input parameters.

Required []stringoptional

List of required property names.

Type BetaManagedAgentsCustomToolInputSchemaTypeoptional

Must be 'object' for tool input schemas.

Name string

Type BetaManagedAgentsCustomToolType

Type BetaManagedAgentsSessionAgentType

Version int64

type BetaManagedAgentsSessionStats struct{…}

Timing statistics for a session.

ActiveSeconds float64optional

Cumulative time in seconds the session spent in running status. Excludes idle time.

DurationSeconds float64optional

Elapsed time since session creation in seconds. For terminated sessions, frozen at the final update.

type BetaManagedAgentsSessionUsage struct{…}

Cumulative token usage for a session across all turns.

CacheCreation [BetaManagedAgentsCacheCreationUsage](api/beta.md)optional

Prompt-cache creation token usage broken down by cache lifetime.

Ephemeral1hInputTokens int64optional

Tokens used to create 1-hour ephemeral cache entries.

Ephemeral5mInputTokens int64optional

Tokens used to create 5-minute ephemeral cache entries.

CacheReadInputTokens int64optional

Total tokens read from prompt cache.

InputTokens int64optional

Total input tokens consumed across all turns.

OutputTokens int64optional

Total output tokens generated across all turns.

#### SessionsEvents

##### [List Events](api/beta/sessions/events/list.md)

client.Beta.Sessions.Events.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionEventUnion](api/beta.md)], error)

GET/v1/sessions/{session\_id}/events

##### [Send Events](api/beta/sessions/events/send.md)

client.Beta.Sessions.Events.Send(ctx, sessionID, params) (\*[BetaManagedAgentsSendSessionEvents](api/beta.md), error)

POST/v1/sessions/{session\_id}/events

##### [Stream Events](api/beta/sessions/events/stream.md)

client.Beta.Sessions.Events.Stream(ctx, sessionID, query) (\*[BetaManagedAgentsStreamSessionEventsUnion](api/beta.md), error)

GET/v1/sessions/{session\_id}/events/stream

##### ModelsExpand Collapse

type BetaManagedAgentsAgentCustomToolUseEvent struct{…}

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the custom tool being called.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentCustomToolUseEventType

type BetaManagedAgentsAgentMCPToolResultEvent struct{…}

Event representing the result of an MCP tool execution.

ID string

Unique identifier for this event.

MCPToolUseID string

The id of the `agent.mcp_tool_use` event this result corresponds to.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolResultEventType

Content []BetaManagedAgentsAgentMCPToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentMCPToolUseEvent struct{…}

Event emitted when the agent invokes a tool provided by an MCP server.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

MCPServerName string

Name of the MCP server providing the tool.

Name string

Name of the MCP tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"

type BetaManagedAgentsAgentMessageEvent struct{…}

An agent response event in the session conversation.

ID string

Unique identifier for this event.

Content [][BetaManagedAgentsTextBlock](api/beta.md)

Array of text blocks comprising the agent response.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMessageEventType

type BetaManagedAgentsAgentThinkingEvent struct{…}

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThinkingEventType

type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}

Indicates that context compaction (summarization) occurred during the session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadContextCompactedEventType

type BetaManagedAgentsAgentToolResultEvent struct{…}

Event representing the result of an agent tool execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to.

Type BetaManagedAgentsAgentToolResultEventType

Content []BetaManagedAgentsAgentToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentToolUseEvent struct{…}

Event emitted when the agent invokes a built-in agent tool.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the agent tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsBillingError struct{…}

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsBillingErrorType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

type BetaManagedAgentsEventParamsUnionResp interface{…}

Union type for event parameters that can be sent to a session.

Accepts one of the following:

type BetaManagedAgentsUserMessageEventParamsResp struct{…}

Parameters for sending a user message to the session.

Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp

Array of content blocks for the user message.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

Type BetaManagedAgentsUserMessageEventParamsType

type BetaManagedAgentsUserInterruptEventParamsResp struct{…}

Parameters for sending an interrupt to pause the agent.

Type BetaManagedAgentsUserInterruptEventParamsType

type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}

Parameters for confirming or denying a tool execution request.

Result BetaManagedAgentsUserToolConfirmationEventParamsResult

UserToolConfirmationResult enum

Accepts one of the following:

const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventParamsType

DenyMessage stringoptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}

Parameters for providing the result of a custom tool execution.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventParamsType

Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionRespoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsMCPAuthenticationFailedError struct{…}

Authentication to an MCP server failed.

MCPServerName string

Name of the MCP server that failed authentication.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPAuthenticationFailedErrorType

type BetaManagedAgentsMCPConnectionFailedError struct{…}

Failed to connect to an MCP server.

MCPServerName string

Name of the MCP server that failed to connect.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPConnectionFailedErrorType

type BetaManagedAgentsModelOverloadedError struct{…}

The model is currently overloaded. Emitted after automatic retries are exhausted.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelOverloadedErrorType

type BetaManagedAgentsModelRateLimitedError struct{…}

The model request was rate-limited.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRateLimitedErrorType

type BetaManagedAgentsModelRequestFailedError struct{…}

A model request failed for a reason other than overload or rate-limiting.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRequestFailedErrorType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

type BetaManagedAgentsSendSessionEvents struct{…}

Events that were successfully sent to the session.

Data []BetaManagedAgentsSendSessionEventsDataUnionoptional

Sent events

Accepts one of the following:

type BetaManagedAgentsUserMessageEvent struct{…}

A user message event in the session conversation.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsUserMessageEventContentUnion

Array of content blocks comprising the user message.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

Type BetaManagedAgentsUserMessageEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserInterruptEvent struct{…}

An interrupt event that pauses agent execution and returns control to the user.

ID string

Unique identifier for this event.

Type BetaManagedAgentsUserInterruptEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserToolConfirmationEvent struct{…}

A tool confirmation event that approves or denies a pending tool execution.

ID string

Unique identifier for this event.

Result BetaManagedAgentsUserToolConfirmationEventResult

UserToolConfirmationResult enum

Accepts one of the following:

const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventType

DenyMessage stringoptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserCustomToolResultEvent struct{…}

Event sent by the client providing the result of a custom tool execution.

ID string

Unique identifier for this event.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventType

Content []BetaManagedAgentsUserCustomToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsSessionDeletedEvent struct{…}

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionDeletedEventType

type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

type BetaManagedAgentsSessionErrorEvent struct{…}

An error event indicating a problem occurred during session execution.

ID string

Unique identifier for this event.

Error BetaManagedAgentsSessionErrorEventErrorUnion

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

type BetaManagedAgentsUnknownError struct{…}

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsUnknownErrorType

type BetaManagedAgentsModelOverloadedError struct{…}

The model is currently overloaded. Emitted after automatic retries are exhausted.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelOverloadedErrorType

type BetaManagedAgentsModelRateLimitedError struct{…}

The model request was rate-limited.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRateLimitedErrorType

type BetaManagedAgentsModelRequestFailedError struct{…}

A model request failed for a reason other than overload or rate-limiting.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRequestFailedErrorType

type BetaManagedAgentsMCPConnectionFailedError struct{…}

Failed to connect to an MCP server.

MCPServerName string

Name of the MCP server that failed to connect.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPConnectionFailedErrorType

type BetaManagedAgentsMCPAuthenticationFailedError struct{…}

Authentication to an MCP server failed.

MCPServerName string

Name of the MCP server that failed authentication.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPAuthenticationFailedErrorType

type BetaManagedAgentsBillingError struct{…}

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsBillingErrorType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionErrorEventType

type BetaManagedAgentsSessionEventUnion interface{…}

Union type for all event types in a session.

Accepts one of the following:

type BetaManagedAgentsUserMessageEvent struct{…}

A user message event in the session conversation.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsUserMessageEventContentUnion

Array of content blocks comprising the user message.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

Type BetaManagedAgentsUserMessageEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserInterruptEvent struct{…}

An interrupt event that pauses agent execution and returns control to the user.

ID string

Unique identifier for this event.

Type BetaManagedAgentsUserInterruptEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserToolConfirmationEvent struct{…}

A tool confirmation event that approves or denies a pending tool execution.

ID string

Unique identifier for this event.

Result BetaManagedAgentsUserToolConfirmationEventResult

UserToolConfirmationResult enum

Accepts one of the following:

const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventType

DenyMessage stringoptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserCustomToolResultEvent struct{…}

Event sent by the client providing the result of a custom tool execution.

ID string

Unique identifier for this event.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventType

Content []BetaManagedAgentsUserCustomToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsAgentCustomToolUseEvent struct{…}

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the custom tool being called.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentCustomToolUseEventType

type BetaManagedAgentsAgentMessageEvent struct{…}

An agent response event in the session conversation.

ID string

Unique identifier for this event.

Content [][BetaManagedAgentsTextBlock](api/beta.md)

Array of text blocks comprising the agent response.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMessageEventType

type BetaManagedAgentsAgentThinkingEvent struct{…}

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThinkingEventType

type BetaManagedAgentsAgentMCPToolUseEvent struct{…}

Event emitted when the agent invokes a tool provided by an MCP server.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

MCPServerName string

Name of the MCP server providing the tool.

Name string

Name of the MCP tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"

type BetaManagedAgentsAgentMCPToolResultEvent struct{…}

Event representing the result of an MCP tool execution.

ID string

Unique identifier for this event.

MCPToolUseID string

The id of the `agent.mcp_tool_use` event this result corresponds to.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolResultEventType

Content []BetaManagedAgentsAgentMCPToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentToolUseEvent struct{…}

Event emitted when the agent invokes a built-in agent tool.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the agent tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"

type BetaManagedAgentsAgentToolResultEvent struct{…}

Event representing the result of an agent tool execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to.

Type BetaManagedAgentsAgentToolResultEventType

Content []BetaManagedAgentsAgentToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}

Indicates that context compaction (summarization) occurred during the session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadContextCompactedEventType

type BetaManagedAgentsSessionErrorEvent struct{…}

An error event indicating a problem occurred during session execution.

ID string

Unique identifier for this event.

Error BetaManagedAgentsSessionErrorEventErrorUnion

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

type BetaManagedAgentsUnknownError struct{…}

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsUnknownErrorType

type BetaManagedAgentsModelOverloadedError struct{…}

The model is currently overloaded. Emitted after automatic retries are exhausted.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelOverloadedErrorType

type BetaManagedAgentsModelRateLimitedError struct{…}

The model request was rate-limited.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRateLimitedErrorType

type BetaManagedAgentsModelRequestFailedError struct{…}

A model request failed for a reason other than overload or rate-limiting.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRequestFailedErrorType

type BetaManagedAgentsMCPConnectionFailedError struct{…}

Failed to connect to an MCP server.

MCPServerName string

Name of the MCP server that failed to connect.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPConnectionFailedErrorType

type BetaManagedAgentsMCPAuthenticationFailedError struct{…}

Authentication to an MCP server failed.

MCPServerName string

Name of the MCP server that failed authentication.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPAuthenticationFailedErrorType

type BetaManagedAgentsBillingError struct{…}

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsBillingErrorType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionErrorEventType

type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}

Indicates the session is recovering from an error state and is rescheduled for execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRescheduledEventType

type BetaManagedAgentsSessionStatusRunningEvent struct{…}

Indicates the session is actively running and the agent is working.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRunningEventType

type BetaManagedAgentsSessionStatusIdleEvent struct{…}

Indicates the agent has paused and is awaiting user input.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType

type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionStatusIdleEventType

type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}

Indicates the session has terminated, either due to an error or completion.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusTerminatedEventType

type BetaManagedAgentsSpanModelRequestStartEvent struct{…}

Emitted when a model request is initiated by the agent.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestStartEventType

type BetaManagedAgentsSpanModelRequestEndEvent struct{…}

Emitted when a model request completes.

ID string

Unique identifier for this event.

IsError bool

Whether the model request resulted in an error.

ModelRequestStartID string

The id of the corresponding `span.model_request_start` event.

ModelUsage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.

Speed BetaManagedAgentsSpanModelUsageSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestEndEventType

type BetaManagedAgentsSessionDeletedEvent struct{…}

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionDeletedEventType

type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType

type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

type BetaManagedAgentsSessionStatusIdleEvent struct{…}

Indicates the agent has paused and is awaiting user input.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType

type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionStatusIdleEventType

type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}

Indicates the session is recovering from an error state and is rescheduled for execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRescheduledEventType

type BetaManagedAgentsSessionStatusRunningEvent struct{…}

Indicates the session is actively running and the agent is working.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRunningEventType

type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}

Indicates the session has terminated, either due to an error or completion.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusTerminatedEventType

type BetaManagedAgentsSpanModelRequestEndEvent struct{…}

Emitted when a model request completes.

ID string

Unique identifier for this event.

IsError bool

Whether the model request resulted in an error.

ModelRequestStartID string

The id of the corresponding `span.model_request_start` event.

ModelUsage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.

Speed BetaManagedAgentsSpanModelUsageSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestEndEventType

type BetaManagedAgentsSpanModelRequestStartEvent struct{…}

Emitted when a model request is initiated by the agent.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestStartEventType

type BetaManagedAgentsSpanModelUsage struct{…}

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.

Speed BetaManagedAgentsSpanModelUsageSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

type BetaManagedAgentsStreamSessionEventsUnion interface{…}

Server-sent event in the session stream.

Accepts one of the following:

type BetaManagedAgentsUserMessageEvent struct{…}

A user message event in the session conversation.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsUserMessageEventContentUnion

Array of content blocks comprising the user message.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

Type BetaManagedAgentsUserMessageEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserInterruptEvent struct{…}

An interrupt event that pauses agent execution and returns control to the user.

ID string

Unique identifier for this event.

Type BetaManagedAgentsUserInterruptEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserToolConfirmationEvent struct{…}

A tool confirmation event that approves or denies a pending tool execution.

ID string

Unique identifier for this event.

Result BetaManagedAgentsUserToolConfirmationEventResult

UserToolConfirmationResult enum

Accepts one of the following:

const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventType

DenyMessage stringoptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserCustomToolResultEvent struct{…}

Event sent by the client providing the result of a custom tool execution.

ID string

Unique identifier for this event.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventType

Content []BetaManagedAgentsUserCustomToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsAgentCustomToolUseEvent struct{…}

Event emitted when the agent calls a custom tool. The session goes idle until the client sends a `user.custom_tool_result` event with the result.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the custom tool being called.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentCustomToolUseEventType

type BetaManagedAgentsAgentMessageEvent struct{…}

An agent response event in the session conversation.

ID string

Unique identifier for this event.

Content [][BetaManagedAgentsTextBlock](api/beta.md)

Array of text blocks comprising the agent response.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMessageEventType

type BetaManagedAgentsAgentThinkingEvent struct{…}

Indicates the agent is making forward progress via extended thinking. A progress signal, not a content carrier.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThinkingEventType

type BetaManagedAgentsAgentMCPToolUseEvent struct{…}

Event emitted when the agent invokes a tool provided by an MCP server.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

MCPServerName string

Name of the MCP server providing the tool.

Name string

Name of the MCP tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentMCPToolUseEventEvaluatedPermission = "deny"

type BetaManagedAgentsAgentMCPToolResultEvent struct{…}

Event representing the result of an MCP tool execution.

ID string

Unique identifier for this event.

MCPToolUseID string

The id of the `agent.mcp_tool_use` event this result corresponds to.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentMCPToolResultEventType

Content []BetaManagedAgentsAgentMCPToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentToolUseEvent struct{…}

Event emitted when the agent invokes a built-in agent tool.

ID string

Unique identifier for this event.

Input map[string, any]

Input parameters for the tool call.

Name string

Name of the agent tool being used.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentToolUseEventType

EvaluatedPermission BetaManagedAgentsAgentToolUseEventEvaluatedPermissionoptional

AgentEvaluatedPermission enum

Accepts one of the following:

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAllow BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "allow"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionAsk BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "ask"

const BetaManagedAgentsAgentToolUseEventEvaluatedPermissionDeny BetaManagedAgentsAgentToolUseEventEvaluatedPermission = "deny"

type BetaManagedAgentsAgentToolResultEvent struct{…}

Event representing the result of an agent tool execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

ToolUseID string

The id of the `agent.tool_use` event this result corresponds to.

Type BetaManagedAgentsAgentToolResultEventType

Content []BetaManagedAgentsAgentToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsAgentThreadContextCompactedEvent struct{…}

Indicates that context compaction (summarization) occurred during the session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsAgentThreadContextCompactedEventType

type BetaManagedAgentsSessionErrorEvent struct{…}

An error event indicating a problem occurred during session execution.

ID string

Unique identifier for this event.

Error BetaManagedAgentsSessionErrorEventErrorUnion

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Accepts one of the following:

type BetaManagedAgentsUnknownError struct{…}

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsUnknownErrorType

type BetaManagedAgentsModelOverloadedError struct{…}

The model is currently overloaded. Emitted after automatic retries are exhausted.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelOverloadedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelOverloadedErrorType

type BetaManagedAgentsModelRateLimitedError struct{…}

The model request was rate-limited.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRateLimitedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRateLimitedErrorType

type BetaManagedAgentsModelRequestFailedError struct{…}

A model request failed for a reason other than overload or rate-limiting.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsModelRequestFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsModelRequestFailedErrorType

type BetaManagedAgentsMCPConnectionFailedError struct{…}

Failed to connect to an MCP server.

MCPServerName string

Name of the MCP server that failed to connect.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPConnectionFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPConnectionFailedErrorType

type BetaManagedAgentsMCPAuthenticationFailedError struct{…}

Authentication to an MCP server failed.

MCPServerName string

Name of the MCP server that failed authentication.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsMCPAuthenticationFailedErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsMCPAuthenticationFailedErrorType

type BetaManagedAgentsBillingError struct{…}

The caller's organization or workspace cannot make model requests — out of credits or spend limit reached. Retrying with the same credentials will not succeed; the caller must resolve the billing state.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsBillingErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsBillingErrorType

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionErrorEventType

type BetaManagedAgentsSessionStatusRescheduledEvent struct{…}

Indicates the session is recovering from an error state and is rescheduled for execution.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRescheduledEventType

type BetaManagedAgentsSessionStatusRunningEvent struct{…}

Indicates the session is actively running and the agent is working.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusRunningEventType

type BetaManagedAgentsSessionStatusIdleEvent struct{…}

Indicates the agent has paused and is awaiting user input.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

StopReason BetaManagedAgentsSessionStatusIdleEventStopReasonUnion

The agent completed its turn naturally and is ready for the next user message.

Accepts one of the following:

type BetaManagedAgentsSessionEndTurn struct{…}

The agent completed its turn naturally and is ready for the next user message.

Type BetaManagedAgentsSessionEndTurnType

type BetaManagedAgentsSessionRequiresAction struct{…}

The agent is idle waiting on one or more blocking user-input events (tool confirmation, custom tool result, etc.). Resolving all of them transitions the session back to running.

EventIDs []string

The ids of events the agent is blocked on. Resolving fewer than all re-emits `session.status_idle` with the remainder.

Type BetaManagedAgentsSessionRequiresActionType

type BetaManagedAgentsSessionRetriesExhausted struct{…}

The turn ended because the retry budget was exhausted (`max_iterations` hit or an error escalated to `retry_status: 'exhausted'`).

Type BetaManagedAgentsSessionRetriesExhaustedType

Type BetaManagedAgentsSessionStatusIdleEventType

type BetaManagedAgentsSessionStatusTerminatedEvent struct{…}

Indicates the session has terminated, either due to an error or completion.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionStatusTerminatedEventType

type BetaManagedAgentsSpanModelRequestStartEvent struct{…}

Emitted when a model request is initiated by the agent.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestStartEventType

type BetaManagedAgentsSpanModelRequestEndEvent struct{…}

Emitted when a model request completes.

ID string

Unique identifier for this event.

IsError bool

Whether the model request resulted in an error.

ModelRequestStartID string

The id of the corresponding `span.model_request_start` event.

ModelUsage [BetaManagedAgentsSpanModelUsage](api/beta.md)

Token usage for a single model request.

CacheCreationInputTokens int64

Tokens used to create prompt cache in this request.

CacheReadInputTokens int64

Tokens read from prompt cache in this request.

InputTokens int64

Input tokens consumed by this request.

OutputTokens int64

Output tokens generated by this request.

Speed BetaManagedAgentsSpanModelUsageSpeedoptional

Inference speed mode. `fast` provides significantly faster output token generation at premium pricing. Not all models support `fast`; invalid combinations are rejected at create time.

Accepts one of the following:

const BetaManagedAgentsSpanModelUsageSpeedStandard BetaManagedAgentsSpanModelUsageSpeed = "standard"

const BetaManagedAgentsSpanModelUsageSpeedFast BetaManagedAgentsSpanModelUsageSpeed = "fast"

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSpanModelRequestEndEventType

type BetaManagedAgentsSessionDeletedEvent struct{…}

Emitted when a session has been deleted. Terminates any active event stream — no further events will be emitted for this session.

ID string

Unique identifier for this event.

ProcessedAt Time

A timestamp in RFC 3339 format

Type BetaManagedAgentsSessionDeletedEventType

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsUnknownError struct{…}

An unknown or unexpected error occurred during session execution. A fallback variant; clients that don't recognize a new error code can match on `retry_status` and `message` alone.

Message string

Human-readable error description.

RetryStatus BetaManagedAgentsUnknownErrorRetryStatusUnion

What the client should do next in response to this error.

Accepts one of the following:

type BetaManagedAgentsRetryStatusRetrying struct{…}

The server is retrying automatically. Client should wait; the same error type may fire again as retrying, then once as exhausted when the retry budget runs out.

Type BetaManagedAgentsRetryStatusRetryingType

type BetaManagedAgentsRetryStatusExhausted struct{…}

This turn is dead; queued inputs are flushed and the session returns to idle. Client may send a new prompt.

Type BetaManagedAgentsRetryStatusExhaustedType

type BetaManagedAgentsRetryStatusTerminal struct{…}

The session encountered a terminal error and will transition to `terminated` state.

Type BetaManagedAgentsRetryStatusTerminalType

Type BetaManagedAgentsUnknownErrorType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsUserCustomToolResultEvent struct{…}

Event sent by the client providing the result of a custom tool execution.

ID string

Unique identifier for this event.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventType

Content []BetaManagedAgentsUserCustomToolResultEventContentUnionoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserCustomToolResultEventParamsResp struct{…}

Parameters for providing the result of a custom tool execution.

CustomToolUseID string

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserCustomToolResultEventParamsType

Content []BetaManagedAgentsUserCustomToolResultEventParamsContentUnionRespoptional

The result content returned by the tool.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

IsError booloptional

Whether the tool execution resulted in an error.

type BetaManagedAgentsUserInterruptEvent struct{…}

An interrupt event that pauses agent execution and returns control to the user.

ID string

Unique identifier for this event.

Type BetaManagedAgentsUserInterruptEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserInterruptEventParamsResp struct{…}

Parameters for sending an interrupt to pause the agent.

Type BetaManagedAgentsUserInterruptEventParamsType

type BetaManagedAgentsUserMessageEvent struct{…}

A user message event in the session conversation.

ID string

Unique identifier for this event.

Content []BetaManagedAgentsUserMessageEventContentUnion

Array of content blocks comprising the user message.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

Type BetaManagedAgentsUserMessageEventType

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserMessageEventParamsResp struct{…}

Parameters for sending a user message to the session.

Content []BetaManagedAgentsUserMessageEventParamsContentUnionResp

Array of content blocks for the user message.

Accepts one of the following:

type BetaManagedAgentsTextBlock struct{…}

Regular text content.

Text string

The text content.

Type BetaManagedAgentsTextBlockType

type BetaManagedAgentsImageBlock struct{…}

Image content specified directly as base64 data or as a reference via a URL.

Source BetaManagedAgentsImageBlockSourceUnion

Union type for image source variants.

Accepts one of the following:

type BetaManagedAgentsBase64ImageSource struct{…}

Base64-encoded image data.

Data string

Base64-encoded image data.

MediaType string

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

Type BetaManagedAgentsBase64ImageSourceType

type BetaManagedAgentsURLImageSource struct{…}

Image referenced by URL.

Type BetaManagedAgentsURLImageSourceType

URL string

URL of the image to fetch.

type BetaManagedAgentsFileImageSource struct{…}

Image referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileImageSourceType

Type BetaManagedAgentsImageBlockType

type BetaManagedAgentsDocumentBlock struct{…}

Document content, either specified directly as base64 data, as text, or as a reference via a URL.

Source BetaManagedAgentsDocumentBlockSourceUnion

Union type for document source variants.

Accepts one of the following:

type BetaManagedAgentsBase64DocumentSource struct{…}

Base64-encoded document data.

Data string

Base64-encoded document data.

MediaType string

MIME type of the document (e.g., "application/pdf").

Type BetaManagedAgentsBase64DocumentSourceType

type BetaManagedAgentsPlainTextDocumentSource struct{…}

Plain text document content.

Data string

The plain text content.

MediaType BetaManagedAgentsPlainTextDocumentSourceMediaType

MIME type of the text content. Must be "text/plain".

Type BetaManagedAgentsPlainTextDocumentSourceType

type BetaManagedAgentsURLDocumentSource struct{…}

Document referenced by URL.

Type BetaManagedAgentsURLDocumentSourceType

URL string

URL of the document to fetch.

type BetaManagedAgentsFileDocumentSource struct{…}

Document referenced by file ID.

FileID string

ID of a previously uploaded file.

Type BetaManagedAgentsFileDocumentSourceType

Type BetaManagedAgentsDocumentBlockType

Context stringoptional

Additional context about the document for the model.

Title stringoptional

The title of the document.

Type BetaManagedAgentsUserMessageEventParamsType

type BetaManagedAgentsUserToolConfirmationEvent struct{…}

A tool confirmation event that approves or denies a pending tool execution.

ID string

Unique identifier for this event.

Result BetaManagedAgentsUserToolConfirmationEventResult

UserToolConfirmationResult enum

Accepts one of the following:

const BetaManagedAgentsUserToolConfirmationEventResultAllow BetaManagedAgentsUserToolConfirmationEventResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventResultDeny BetaManagedAgentsUserToolConfirmationEventResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventType

DenyMessage stringoptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

ProcessedAt Timeoptional

A timestamp in RFC 3339 format

type BetaManagedAgentsUserToolConfirmationEventParamsResp struct{…}

Parameters for confirming or denying a tool execution request.

Result BetaManagedAgentsUserToolConfirmationEventParamsResult

UserToolConfirmationResult enum

Accepts one of the following:

const BetaManagedAgentsUserToolConfirmationEventParamsResultAllow BetaManagedAgentsUserToolConfirmationEventParamsResult = "allow"

const BetaManagedAgentsUserToolConfirmationEventParamsResultDeny BetaManagedAgentsUserToolConfirmationEventParamsResult = "deny"

ToolUseID string

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

Type BetaManagedAgentsUserToolConfirmationEventParamsType

DenyMessage stringoptional

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

#### SessionsResources

##### [Add Session Resource](api/beta/sessions/resources/add.md)

client.Beta.Sessions.Resources.Add(ctx, sessionID, params) (\*[BetaManagedAgentsFileResource](api/beta.md), error)

POST/v1/sessions/{session\_id}/resources

##### [List Session Resources](api/beta/sessions/resources/list.md)

client.Beta.Sessions.Resources.List(ctx, sessionID, params) (\*PageCursor[[BetaManagedAgentsSessionResourceUnion](api/beta.md)], error)

GET/v1/sessions/{session\_id}/resources

##### [Get Session Resource](api/beta/sessions/resources/retrieve.md)

client.Beta.Sessions.Resources.Get(ctx, resourceID, params) (\*[BetaSessionResourceGetResponseUnion](api/beta.md), error)

GET/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Update Session Resource](api/beta/sessions/resources/update.md)

client.Beta.Sessions.Resources.Update(ctx, resourceID, params) (\*[BetaSessionResourceUpdateResponseUnion](api/beta.md), error)

POST/v1/sessions/{session\_id}/resources/{resource\_id}

##### [Delete Session Resource](api/beta/sessions/resources/delete.md)

client.Beta.Sessions.Resources.Delete(ctx, resourceID, params) (\*[BetaManagedAgentsDeleteSessionResource](api/beta.md), error)

DELETE/v1/sessions/{session\_id}/resources/{resource\_id}

##### ModelsExpand Collapse

type BetaManagedAgentsDeleteSessionResource struct{…}

Confirmation of resource deletion.

ID string

Type BetaManagedAgentsDeleteSessionResourceType

type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string

Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionoptional

Accepts one of the following:

type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType

type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

type BetaManagedAgentsSessionResourceUnion interface{…}

Accepts one of the following:

type BetaManagedAgentsGitHubRepositoryResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

MountPath string

Type BetaManagedAgentsGitHubRepositoryResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

URL string

Checkout BetaManagedAgentsGitHubRepositoryResourceCheckoutUnionoptional

Accepts one of the following:

type BetaManagedAgentsBranchCheckout struct{…}

Name string

Branch name to check out.

Type BetaManagedAgentsBranchCheckoutType

type BetaManagedAgentsCommitCheckout struct{…}

Sha string

Full commit SHA to check out.

Type BetaManagedAgentsCommitCheckoutType

type BetaManagedAgentsFileResource struct{…}

ID string

CreatedAt Time

A timestamp in RFC 3339 format

FileID string

MountPath string

Type BetaManagedAgentsFileResourceType

UpdatedAt Time

A timestamp in RFC 3339 format

---

*Copyright © Anthropic. All rights reserved.*
