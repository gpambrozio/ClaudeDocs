# Send Events

Copy page



C#

# Send Events

[BetaManagedAgentsSendSessionEvents](api/beta/sessions/events.md) Beta.Sessions.Events.Send(EventSendParamsparameters, CancellationTokencancellationToken = default)

POST/v1/sessions/{session\_id}/events

Send Events

##### ParametersExpand Collapse



EventSendParams parameters

required string sessionID

Path param: Path parameter session\_id



required IReadOnlyList<[BetaManagedAgentsEventParams](api/beta/sessions/events.md)> events

Body param: Events to send to the `session`.



class BetaManagedAgentsUserMessageEventParams:

Parameters for sending a user message to the session.



required IReadOnlyList<Content> Content

Array of content blocks for the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type



class BetaManagedAgentsUserInterruptEventParams:

Parameters for sending an interrupt to pause the agent.

required Type Type

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEventParams:

Parameters for confirming or denying a tool execution request.



required Result Result

UserToolConfirmationResult enum

One of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.



class BetaManagedAgentsUserCustomToolResultEventParams:

Parameters for providing the result of a custom tool execution.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.



class BetaManagedAgentsUserDefineOutcomeEventParams:

Parameters for defining an outcome the agent should work toward. The agent begins work on receipt.

required string Description

What the agent should produce. This is the task specification.



required Rubric Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubricParams:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type



class BetaManagedAgentsTextRubricParams:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text. Maximum 262144 characters.

required Type Type

required Type Type

Int? MaxIterations

Eval→revision cycles before giving up. Default 3, max 20.



class BetaManagedAgentsUserToolResultEventParams:

Parameters for providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.



class BetaManagedAgentsSystemMessageEventParams:

Privileged context for the accompanying turn and all subsequent turns, appended to the session's system context as a `role: "system"` turn rather than replacing the top-level system prompt. At most one per request: it must be the final event and immediately follow the `user.message`, `user.tool_result`, or `user.custom_tool_result` it accompanies. Only supported on models that accept mid-conversation system messages.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> Content

System content blocks to append. Text-only.

required string Text

The text content.

required Type Type

required Type Type



IReadOnlyList<[AnthropicBeta](api/beta.md)> betas

Header param: Optional header to specify the beta version(s) you want to use.

"message-batches-2024-09-24"MessageBatches2024\_09\_24

"prompt-caching-2024-07-31"PromptCaching2024\_07\_31

"computer-use-2024-10-22"ComputerUse2024\_10\_22

"computer-use-2025-01-24"ComputerUse2025\_01\_24

"pdfs-2024-09-25"Pdfs2024\_09\_25

"token-counting-2024-11-01"TokenCounting2024\_11\_01

"token-efficient-tools-2025-02-19"TokenEfficientTools2025\_02\_19

"output-128k-2025-02-19"Output128k2025\_02\_19

"files-api-2025-04-14"FilesApi2025\_04\_14

"mcp-client-2025-04-04"McpClient2025\_04\_04

"mcp-client-2025-11-20"McpClient2025\_11\_20

"dev-full-thinking-2025-05-14"DevFullThinking2025\_05\_14

"interleaved-thinking-2025-05-14"InterleavedThinking2025\_05\_14

"code-execution-2025-05-22"CodeExecution2025\_05\_22

"extended-cache-ttl-2025-04-11"ExtendedCacheTtl2025\_04\_11

"context-1m-2025-08-07"Context1m2025\_08\_07

"context-management-2025-06-27"ContextManagement2025\_06\_27

"model-context-window-exceeded-2025-08-26"ModelContextWindowExceeded2025\_08\_26

"skills-2025-10-02"Skills2025\_10\_02

"fast-mode-2026-02-01"FastMode2026\_02\_01

"output-300k-2026-03-24"Output300k2026\_03\_24

"user-profiles-2026-03-24"UserProfiles2026\_03\_24

"advisor-tool-2026-03-01"AdvisorTool2026\_03\_01

"managed-agents-2026-04-01"ManagedAgents2026\_04\_01

"cache-diagnosis-2026-04-07"CacheDiagnosis2026\_04\_07

"thinking-token-count-2026-05-13"ThinkingTokenCount2026\_05\_13

"server-side-fallback-2026-06-01"ServerSideFallback2026\_06\_01

"fallback-credit-2026-06-01"FallbackCredit2026\_06\_01

"agent-memory-2026-07-22"AgentMemory2026\_07\_22

##### ReturnsExpand Collapse



class BetaManagedAgentsSendSessionEvents:

Events that were successfully sent to the session.



IReadOnlyList<Data> Data

Sent events

One of the following:



class BetaManagedAgentsUserMessageEvent:

A user message event in the session conversation.

required string ID

Unique identifier for this event.



required IReadOnlyList<Content> Content

Array of content blocks comprising the user message.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format



class BetaManagedAgentsUserInterruptEvent:

An interrupt event that pauses agent execution and returns control to the user.

required string ID

Unique identifier for this event.

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

If absent, interrupts every non-archived thread in a multiagent session (or the primary alone in a single-agent session). If present, interrupts only the named thread.



class BetaManagedAgentsUserToolConfirmationEvent:

A tool confirmation event that approves or denies a pending tool execution.

required string ID

Unique identifier for this event.



required Result Result

UserToolConfirmationResult enum

One of the following:

"allow"Allow

"deny"Deny

required string ToolUseID

The id of the `agent.tool_use` or `agent.mcp_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type

string? DenyMessage

Optional message providing context for a 'deny' decision. Only allowed when result is 'deny'.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

When set, the confirmation routes to this subagent's thread rather than the primary. Echo this from the `session_thread_id` on the `agent.tool_use` or `agent.mcp_tool_use` event that prompted the approval.



class BetaManagedAgentsUserCustomToolResultEvent:

Event sent by the client providing the result of a custom tool execution.

required string ID

Unique identifier for this event.

required string CustomToolUseID

The id of the `agent.custom_tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.custom_tool_use` event's `session_thread_id`.



class BetaManagedAgentsUserDefineOutcomeEvent:

Echo of a `user.define_outcome` input event. Carries the server-generated `outcome_id` that subsequent `span.outcome_evaluation_*` events reference.

required string ID

Unique identifier for this event.

required string Description

What the agent should produce. Copied from the input event.

required Int? MaxIterations

Evaluate-then-revise cycles before giving up. Default 3, max 20.

required string OutcomeID

Server-generated `outc_` ID for this outcome. Referenced by `span.outcome_evaluation_*` events and the session's `outcome_evaluations` list.

required DateTimeOffset ProcessedAt

A timestamp in RFC 3339 format



required Rubric Rubric

Rubric for grading the quality of an outcome.

One of the following:



class BetaManagedAgentsFileRubric:

Rubric referenced by a file uploaded via the Files API.

required string FileID

ID of the rubric file.

required Type Type



class BetaManagedAgentsTextRubric:

Rubric content provided inline as text.

required string Content

Rubric content. Plain text or markdown — the grader treats it as freeform text.

required Type Type

required Type Type



class BetaManagedAgentsUserToolResultEvent:

Event sent by the client providing the result of an agent-toolset tool execution. Only valid on `self_hosted` environments, where sandbox-routed tools are executed by the client rather than the server.

required string ID

Unique identifier for this event.

required string ToolUseID

The id of the `agent.tool_use` event this result corresponds to, which can be found in the last `session.status_idle` [event's](api/beta/sessions/events/list.md) `stop_reason.event_ids` field.

required Type Type



IReadOnlyList<Content> Content

The result content returned by the tool.

One of the following:



class BetaManagedAgentsTextBlock:

Regular text content.

required string Text

The text content.

required Type Type



class BetaManagedAgentsImageBlock:

Image content specified directly as base64 data or as a reference via a URL.



required Source Source

Union type for image source variants.

One of the following:



class BetaManagedAgentsBase64ImageSource:

Base64-encoded image data.

required string Data

Base64-encoded image data.

required string MediaType

MIME type of the image (e.g., "image/png", "image/jpeg", "image/gif", "image/webp").

required Type Type



class BetaManagedAgentsUrlImageSource:

Image referenced by URL.

required Type Type

required string Url

URL of the image to fetch.



class BetaManagedAgentsFileImageSource:

Image referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type



class BetaManagedAgentsDocumentBlock:

Document content, either specified directly as base64 data, as text, or as a reference via a URL.



required Source Source

Union type for document source variants.

One of the following:



class BetaManagedAgentsBase64DocumentSource:

Base64-encoded document data.

required string Data

Base64-encoded document data.

required string MediaType

MIME type of the document (e.g., "application/pdf").

required Type Type



class BetaManagedAgentsPlainTextDocumentSource:

Plain text document content.

required string Data

The plain text content.

required MediaType MediaType

MIME type of the text content. Must be "text/plain".

required Type Type



class BetaManagedAgentsUrlDocumentSource:

Document referenced by URL.

required Type Type

required string Url

URL of the document to fetch.



class BetaManagedAgentsFileDocumentSource:

Document referenced by file ID.

required string FileID

ID of a previously uploaded file.

required Type Type

required Type Type

string? Context

Additional context about the document for the model.

string? Title

The title of the document.



class BetaManagedAgentsSearchResultBlock:

A block containing a web search result.



required [BetaManagedAgentsSearchResultCitations](api/beta/sessions/events.md) Citations

Citation settings for a search result.

required Boolean Enabled

Whether citations are enabled for this search result.



required IReadOnlyList<[BetaManagedAgentsSearchResultContent](api/beta/sessions/events.md)> Content

Array of text content blocks from the search result.

required string Text

The text content.

required Type Type

required string Source

The URL source of the search result.

required string Title

The title of the search result.

required Type Type

Boolean? IsError

Whether the tool execution resulted in an error.

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

string? SessionThreadID

Routes this result to a subagent thread. Copy from the `agent.tool_use` event's `session_thread_id`.



class BetaManagedAgentsSystemMessageEvent:

A mid-conversation system message event. Carries system-role content that is appended to the session as a `role: "system"` turn.

required string ID

Unique identifier for this event.



required IReadOnlyList<[BetaManagedAgentsSystemContentBlock](api/beta/sessions.md)> Content

System content blocks. Text-only.

required string Text

The text content.

required Type Type

required Type Type

DateTimeOffset? ProcessedAt

A timestamp in RFC 3339 format

Send Events

C#

```shiki
EventSendParams parameters = new()
{
    SessionID = "sesn_011CZkZAtmR3yMPDzynEDxu7",
    Events =
    [
        new BetaManagedAgentsUserMessageEventParams()
        {
            Content =
            [
                new BetaManagedAgentsTextBlock()
                {
                    Text = "Where is my order #1234?",
                    Type = Type.Text,
                },
            ],
            Type = Type.UserMessage,
        },
    ],
};

var betaManagedAgentsSendSessionEvents = await client.Beta.Sessions.Events.Send(parameters);

Console.WriteLine(betaManagedAgentsSendSessionEvents);
```

Response 200



```shiki
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

##### Returns Examples

Response 200



```shiki
{
  "data": [
    {
      "id": "sevt_011CZkZGOp0iBcp4kaQSihUmy",
      "content": [
        {
          "text": "Where is my order #1234?",
          "type": "text"
        }
      ],
      "type": "user.message",
      "processed_at": "2026-03-15T10:00:00Z"
    }
  ]
}
```

---

*Copyright © Anthropic. All rights reserved.*
