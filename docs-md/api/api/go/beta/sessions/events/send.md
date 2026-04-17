# Send Events

Copy page

Go

# Send Events

client.Beta.Sessions.Events.Send(ctx, sessionID, params) (\*[BetaManagedAgentsSendSessionEvents](api/beta.md), error)

POST/v1/sessions/{session\_id}/events

Send Events

##### ParametersExpand Collapse

sessionID string

params BetaSessionEventSendParams

Events param.Field[[][BetaManagedAgentsEventParamsUnionResp](api/beta.md)]

Body param: Events to send to the `session`.

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

Betas param.Field[[]AnthropicBeta]optional

Header param: Optional header to specify the beta version(s) you want to use.

string

type AnthropicBeta string

Accepts one of the following:

const AnthropicBetaMessageBatches2024\_09\_24 AnthropicBeta = "message-batches-2024-09-24"

const AnthropicBetaPromptCaching2024\_07\_31 AnthropicBeta = "prompt-caching-2024-07-31"

const AnthropicBetaComputerUse2024\_10\_22 AnthropicBeta = "computer-use-2024-10-22"

const AnthropicBetaComputerUse2025\_01\_24 AnthropicBeta = "computer-use-2025-01-24"

const AnthropicBetaPDFs2024\_09\_25 AnthropicBeta = "pdfs-2024-09-25"

const AnthropicBetaTokenCounting2024\_11\_01 AnthropicBeta = "token-counting-2024-11-01"

const AnthropicBetaTokenEfficientTools2025\_02\_19 AnthropicBeta = "token-efficient-tools-2025-02-19"

const AnthropicBetaOutput128k2025\_02\_19 AnthropicBeta = "output-128k-2025-02-19"

const AnthropicBetaFilesAPI2025\_04\_14 AnthropicBeta = "files-api-2025-04-14"

const AnthropicBetaMCPClient2025\_04\_04 AnthropicBeta = "mcp-client-2025-04-04"

const AnthropicBetaMCPClient2025\_11\_20 AnthropicBeta = "mcp-client-2025-11-20"

const AnthropicBetaDevFullThinking2025\_05\_14 AnthropicBeta = "dev-full-thinking-2025-05-14"

const AnthropicBetaInterleavedThinking2025\_05\_14 AnthropicBeta = "interleaved-thinking-2025-05-14"

const AnthropicBetaCodeExecution2025\_05\_22 AnthropicBeta = "code-execution-2025-05-22"

const AnthropicBetaExtendedCacheTTL2025\_04\_11 AnthropicBeta = "extended-cache-ttl-2025-04-11"

const AnthropicBetaContext1m2025\_08\_07 AnthropicBeta = "context-1m-2025-08-07"

const AnthropicBetaContextManagement2025\_06\_27 AnthropicBeta = "context-management-2025-06-27"

const AnthropicBetaModelContextWindowExceeded2025\_08\_26 AnthropicBeta = "model-context-window-exceeded-2025-08-26"

const AnthropicBetaSkills2025\_10\_02 AnthropicBeta = "skills-2025-10-02"

const AnthropicBetaFastMode2026\_02\_01 AnthropicBeta = "fast-mode-2026-02-01"

const AnthropicBetaOutput300k2026\_03\_24 AnthropicBeta = "output-300k-2026-03-24"

const AnthropicBetaAdvisorTool2026\_03\_01 AnthropicBeta = "advisor-tool-2026-03-01"

const AnthropicBetaUserProfiles2026\_03\_24 AnthropicBeta = "user-profiles-2026-03-24"

##### ReturnsExpand Collapse

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

Send Events

Go

```shiki
package main

import (
  "context"
  "fmt"

  "github.com/anthropics/anthropic-sdk-go"
  "github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
  client := anthropic.NewClient(
    option.WithAPIKey("my-anthropic-api-key"),
  )
  betaManagedAgentsSendSessionEvents, err := client.Beta.Sessions.Events.Send(
    context.TODO(),
    "sesn_011CZkZAtmR3yMPDzynEDxu7",
    anthropic.BetaSessionEventSendParams{
      Events: []anthropic.BetaManagedAgentsEventParamsUnion{anthropic.BetaManagedAgentsEventParamsUnion{
        OfUserMessage: &anthropic.BetaManagedAgentsUserMessageEventParams{
          Content: []anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{anthropic.BetaManagedAgentsUserMessageEventParamsContentUnion{
            OfText: &anthropic.BetaManagedAgentsTextBlockParam{
              Text: "Where is my order #1234?",
              Type: anthropic.BetaManagedAgentsTextBlockTypeText,
            },
          }},
          Type: anthropic.BetaManagedAgentsUserMessageEventParamsTypeUserMessage,
        },
      }},
    },
  )
  if err != nil {
    panic(err.Error())
  }
  fmt.Printf("%+v\n", betaManagedAgentsSendSessionEvents.Data)
}
```

Response 200

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
