# Beta

Copy page

Ruby

# Beta

##### ModelsExpand Collapse

AnthropicBeta = String | :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 18 more

Accepts one of the following:

:"message-batches-2024-09-24"

:"prompt-caching-2024-07-31"

:"computer-use-2024-10-22"

:"computer-use-2025-01-24"

:"pdfs-2024-09-25"

:"token-counting-2024-11-01"

:"token-efficient-tools-2025-02-19"

:"output-128k-2025-02-19"

:"files-api-2025-04-14"

:"mcp-client-2025-04-04"

:"mcp-client-2025-11-20"

:"dev-full-thinking-2025-05-14"

:"interleaved-thinking-2025-05-14"

:"code-execution-2025-05-22"

:"extended-cache-ttl-2025-04-11"

:"context-1m-2025-08-07"

:"context-management-2025-06-27"

:"model-context-window-exceeded-2025-08-26"

:"skills-2025-10-02"

:"fast-mode-2026-02-01"

:"output-300k-2026-03-24"

class BetaAPIError { message, type }

message: String

type: :api\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

BetaError = [BetaInvalidRequestError](api/beta.md) { message, type }  | [BetaAuthenticationError](api/beta.md) { message, type }  | [BetaBillingError](api/beta.md) { message, type }  | 6 more

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

class BetaErrorResponse { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

request\_id: String

type: :error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

#### BetaModels

##### [List Models](api/beta/models/list.md)

beta.models.list(\*\*kwargs) -> Page<[BetaModelInfo](api/beta.md) { id, capabilities, created\_at, 4 more } >

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

beta.models.retrieve(model\_id, \*\*kwargs) -> [BetaModelInfo](api/beta.md) { id, capabilities, created\_at, 4 more }

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaCapabilitySupport { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

class BetaContextManagementCapability { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management capability details.

clear\_thinking\_20251015: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class BetaEffortCapability { high, low, max, 2 more }

Effort (reasoning\_effort) capability details.

high: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

class BetaModelCapabilities { batch, citations, code\_execution, 6 more }

Model capability information.

batch: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code\_execution: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context\_management: [BetaContextManagementCapability](api/beta.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management support and available strategies.

clear\_thinking\_20251015: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [BetaEffortCapability](api/beta.md) { high, low, max, 2 more }

Effort (reasoning\_effort) support and available levels.

high: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

image\_input: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf\_input: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured\_outputs: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [BetaThinkingCapability](api/beta.md) { supported, types }

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](api/beta.md) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class BetaModelInfo { id, capabilities, created\_at, 4 more }

id: String

Unique model identifier.

capabilities: [BetaModelCapabilities](api/beta.md) { batch, citations, code\_execution, 6 more }

Model capability information.

batch: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports the Batch API.

supported: bool

Whether this capability is supported by the model.

citations: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports citation generation.

supported: bool

Whether this capability is supported by the model.

code\_execution: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports code execution tools.

supported: bool

Whether this capability is supported by the model.

context\_management: [BetaContextManagementCapability](api/beta.md) { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management support and available strategies.

clear\_thinking\_20251015: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

compact\_20260112: [BetaCapabilitySupport](api/beta.md) { supported }

Indicates whether a capability is supported.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

effort: [BetaEffortCapability](api/beta.md) { high, low, max, 2 more }

Effort (reasoning\_effort) support and available levels.

high: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports high effort level.

supported: bool

Whether this capability is supported by the model.

low: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports low effort level.

supported: bool

Whether this capability is supported by the model.

max: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports max effort level.

supported: bool

Whether this capability is supported by the model.

medium: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports medium effort level.

supported: bool

Whether this capability is supported by the model.

supported: bool

Whether this capability is supported by the model.

image\_input: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model accepts image content blocks.

supported: bool

Whether this capability is supported by the model.

pdf\_input: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model accepts PDF content blocks.

supported: bool

Whether this capability is supported by the model.

structured\_outputs: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: bool

Whether this capability is supported by the model.

thinking: [BetaThinkingCapability](api/beta.md) { supported, types }

Thinking capability and supported type configurations.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](api/beta.md) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

created\_at: Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: String

A human-readable name for the model.

max\_input\_tokens: Integer

Maximum input context window size in tokens for this model.

max\_tokens: Integer

Maximum value for the `max_tokens` parameter when using this model.

type: :model

Object type.

For Models, this is always `"model"`.

class BetaThinkingCapability { supported, types }

Thinking capability details.

supported: bool

Whether this capability is supported by the model.

types: [BetaThinkingTypes](api/beta.md) { adaptive, enabled }

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

class BetaThinkingTypes { adaptive, enabled }

Supported thinking type configurations.

adaptive: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: bool

Whether this capability is supported by the model.

enabled: [BetaCapabilitySupport](api/beta.md) { supported }

Whether the model supports thinking with type 'enabled'.

supported: bool

Whether this capability is supported by the model.

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

beta.messages.create(\*\*kwargs) -> [BetaMessage](api/beta.md) { id, container, content, 8 more }

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

beta.messages.count\_tokens(\*\*kwargs) -> [BetaMessageTokensCount](api/beta.md) { context\_management, input\_tokens }

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

class BetaAllThinkingTurns { type }

type: :all

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaBashCodeExecutionOutputBlock { file\_id, type }

file\_id: String

type: :bash\_code\_execution\_output

class BetaBashCodeExecutionOutputBlockParam { file\_id, type }

file\_id: String

type: :bash\_code\_execution\_output

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaCacheControlEphemeral { type, ttl }

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaCacheCreation { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationConfig { enabled }

enabled: bool

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationsConfigParam { enabled }

enabled: bool

class BetaCitationsDelta { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

type: :citations\_delta

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaClearThinking20251015Edit { type, keep }

type: :clear\_thinking\_20251015

keep: [BetaThinkingTurns](api/beta.md) { type, value }  | [BetaAllThinkingTurns](api/beta.md) { type }  | :all

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns { type, value }

type: :thinking\_turns

value: Integer

class BetaAllThinkingTurns { type }

type: :all

Keep = :all

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

class BetaClearToolUses20250919Edit { type, clear\_at\_least, clear\_tool\_inputs, 3 more }

type: :clear\_tool\_uses\_20250919

clear\_at\_least: [BetaInputTokensClearAtLeast](api/beta.md) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: :input\_tokens

value: Integer

clear\_tool\_inputs: bool | Array[String]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

bool

Array[String]

exclude\_tools: Array[String]

Tool names whose uses are preserved from clearing

keep: [BetaToolUsesKeep](api/beta.md) { type, value }

Number of tool uses to retain in the conversation

type: :tool\_uses

value: Integer

trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }  | [BetaToolUsesTrigger](api/beta.md) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger { type, value }

type: :input\_tokens

value: Integer

class BetaToolUsesTrigger { type, value }

type: :tool\_uses

value: Integer

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaCodeExecutionOutputBlock { file\_id, type }

file\_id: String

type: :code\_execution\_output

class BetaCodeExecutionOutputBlockParam { file\_id, type }

file\_id: String

type: :code\_execution\_output

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaCodeExecutionTool20250522 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250522

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250825

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20260120 { name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260120

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  | [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  | [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

BetaCodeExecutionToolResultErrorCode = :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCompact20260112Edit { type, instructions, pause\_after\_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: :compact\_20260112

instructions: String

Additional instructions for summarization.

pause\_after\_compaction: bool

Whether to pause after compaction and return the compaction block to the user.

trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: :input\_tokens

value: Integer

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

class BetaCompactionBlockParam { content, type, cache\_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: String

Summary of previously compacted content, or null if compaction failed

type: :compaction

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaCompactionContentBlockDelta { content, type }

content: String

type: :compaction\_delta

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

class BetaContainer { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

class BetaContainerParams { id, skills }

Container parameters with skills to be loaded.

id: String

Container id

skills: Array[[BetaSkillParams](api/beta.md) { skill\_id, type, version } ]

List of skills to load in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaContainerUploadBlockParam { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

BetaContentBlock = [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

BetaContentBlockParam = [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }  | 16 more

Regular text content.

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

class BetaThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

class BetaToolReferenceBlockParam { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

is\_error: bool

class BetaServerToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more }

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String

class BetaWebSearchToolRequestError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  | [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaBashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaTextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :mcp\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

is\_error: bool

class BetaContainerUploadBlockParam { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaCompactionBlockParam { content, type, cache\_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: String

Summary of previously compacted content, or null if compaction failed

type: :compaction

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

BetaContentBlockSourceContent = [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaContextManagementConfig { edits }

edits: Array[[BetaClearToolUses20250919Edit](api/beta.md) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  | [BetaClearThinking20251015Edit](api/beta.md) { type, keep }  | [BetaCompact20260112Edit](api/beta.md) { type, instructions, pause\_after\_compaction, trigger } ]

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit { type, clear\_at\_least, clear\_tool\_inputs, 3 more }

type: :clear\_tool\_uses\_20250919

clear\_at\_least: [BetaInputTokensClearAtLeast](api/beta.md) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: :input\_tokens

value: Integer

clear\_tool\_inputs: bool | Array[String]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

Accepts one of the following:

bool

Array[String]

exclude\_tools: Array[String]

Tool names whose uses are preserved from clearing

keep: [BetaToolUsesKeep](api/beta.md) { type, value }

Number of tool uses to retain in the conversation

type: :tool\_uses

value: Integer

trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }  | [BetaToolUsesTrigger](api/beta.md) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger { type, value }

type: :input\_tokens

value: Integer

class BetaToolUsesTrigger { type, value }

type: :tool\_uses

value: Integer

class BetaClearThinking20251015Edit { type, keep }

type: :clear\_thinking\_20251015

keep: [BetaThinkingTurns](api/beta.md) { type, value }  | [BetaAllThinkingTurns](api/beta.md) { type }  | :all

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns { type, value }

type: :thinking\_turns

value: Integer

class BetaAllThinkingTurns { type }

type: :all

Keep = :all

class BetaCompact20260112Edit { type, instructions, pause\_after\_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: :compact\_20260112

instructions: String

Additional instructions for summarization.

pause\_after\_compaction: bool

Whether to pause after compaction and return the compaction block to the user.

trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: :input\_tokens

value: Integer

class BetaContextManagementResponse { applied\_edits }

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

class BetaCountTokensContextManagementResponse { original\_input\_tokens }

original\_input\_tokens: Integer

The original token count before context management was applied

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaDocumentBlock { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaInputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

class BetaInputTokensClearAtLeast { type, value }

type: :input\_tokens

value: Integer

class BetaInputTokensTrigger { type, value }

type: :input\_tokens

value: Integer

Array[[BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  | [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } ]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

class BetaJSONOutputFormat { schema, type }

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema

class BetaMCPToolConfig { defer\_loading, enabled }

Configuration for a specific tool in an MCP toolset.

defer\_loading: bool

enabled: bool

class BetaMCPToolDefaultConfig { defer\_loading, enabled }

Default configuration for tools in an MCP toolset.

defer\_loading: bool

enabled: bool

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaMCPToolset { mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: String

Name of the MCP server to configure tools for

type: :mcp\_toolset

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

configs: Hash[Symbol, [BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: bool

enabled: bool

default\_config: [BetaMCPToolDefaultConfig](api/beta.md) { defer\_loading, enabled }

Default configuration applied to all tools from this server

defer\_loading: bool

enabled: bool

class BetaMemoryTool20250818 { name, type, allowed\_callers, 4 more }

name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :memory\_20250818

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

BetaMemoryTool20250818Command = [BetaMemoryTool20250818ViewCommand](api/beta.md) { command, path, view\_range }  | [BetaMemoryTool20250818CreateCommand](api/beta.md) { command, file\_text, path }  | [BetaMemoryTool20250818StrReplaceCommand](api/beta.md) { command, new\_str, old\_str, path }  | 3 more

Accepts one of the following:

class BetaMemoryTool20250818ViewCommand { command, path, view\_range }

command: :view

Command type identifier

path: String

Path to directory or file to view

view\_range: Array[Integer]

Optional line range for viewing specific lines

class BetaMemoryTool20250818CreateCommand { command, file\_text, path }

command: :create

Command type identifier

file\_text: String

Content to write to the file

path: String

Path where the file should be created

class BetaMemoryTool20250818StrReplaceCommand { command, new\_str, old\_str, path }

command: :str\_replace

Command type identifier

new\_str: String

Text to replace with

old\_str: String

Text to search for and replace

path: String

Path to the file where text should be replaced

class BetaMemoryTool20250818InsertCommand { command, insert\_line, insert\_text, path }

command: :insert

Command type identifier

insert\_line: Integer

Line number where text should be inserted

insert\_text: String

Text to insert at the specified line

path: String

Path to the file where text should be inserted

class BetaMemoryTool20250818DeleteCommand { command, path }

command: :delete

Command type identifier

path: String

Path to the file or directory to delete

class BetaMemoryTool20250818RenameCommand { command, new\_path, old\_path }

command: :rename

Command type identifier

new\_path: String

New path for the file or directory

old\_path: String

Current path of the file or directory

class BetaMemoryTool20250818CreateCommand { command, file\_text, path }

command: :create

Command type identifier

file\_text: String

Content to write to the file

path: String

Path where the file should be created

class BetaMemoryTool20250818DeleteCommand { command, path }

command: :delete

Command type identifier

path: String

Path to the file or directory to delete

class BetaMemoryTool20250818InsertCommand { command, insert\_line, insert\_text, path }

command: :insert

Command type identifier

insert\_line: Integer

Line number where text should be inserted

insert\_text: String

Text to insert at the specified line

path: String

Path to the file where text should be inserted

class BetaMemoryTool20250818RenameCommand { command, new\_path, old\_path }

command: :rename

Command type identifier

new\_path: String

New path for the file or directory

old\_path: String

Current path of the file or directory

class BetaMemoryTool20250818StrReplaceCommand { command, new\_str, old\_str, path }

command: :str\_replace

Command type identifier

new\_str: String

Text to replace with

old\_str: String

Text to search for and replace

path: String

Path to the file where text should be replaced

class BetaMemoryTool20250818ViewCommand { command, path, view\_range }

command: :view

Command type identifier

path: String

Path to directory or file to view

view\_range: Array[Integer]

Optional line range for viewing specific lines

class BetaMessage { id, container, content, 8 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array[[BetaContentBlock](api/beta.md)]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 13 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard | :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

class BetaMessageDeltaUsage { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

input\_tokens: Integer

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaMessageParam { content, role }

content: String | Array[[BetaContentBlockParam](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockParam](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

class BetaThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

class BetaToolReferenceBlockParam { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

is\_error: bool

class BetaServerToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more }

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String

class BetaWebSearchToolRequestError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  | [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaBashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaTextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :mcp\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

is\_error: bool

class BetaContainerUploadBlockParam { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaCompactionBlockParam { content, type, cache\_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: String

Summary of previously compacted content, or null if compaction failed

type: :compaction

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

role: :user | :assistant

Accepts one of the following:

:user

:assistant

class BetaMessageTokensCount { context\_management, input\_tokens }

context\_management: [BetaCountTokensContextManagementResponse](api/beta.md) { original\_input\_tokens }

Information about context management applied to the message.

original\_input\_tokens: Integer

The original token count before context management was applied

input\_tokens: Integer

The total number of tokens across the provided list of messages, system prompt, and tools.

class BetaMetadata { user\_id }

user\_id: String

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512

class BetaOutputConfig { effort, format\_ }

effort: :low | :medium | :high | :max

All possible effort levels.

Accepts one of the following:

:low

:medium

:high

:max

format\_: [BetaJSONOutputFormat](api/beta.md) { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

BetaRawContentBlockDelta = [BetaTextDelta](api/beta.md) { text, type }  | [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  | [BetaCitationsDelta](api/beta.md) { citation, type }  | 3 more

Accepts one of the following:

class BetaTextDelta { text, type }

text: String

type: :text\_delta

class BetaInputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

class BetaCitationsDelta { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

type: :citations\_delta

class BetaThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

class BetaSignatureDelta { signature, type }

signature: String

type: :signature\_delta

class BetaCompactionContentBlockDelta { content, type }

content: String

type: :compaction\_delta

class BetaRawContentBlockDeltaEvent { delta, index, type }

delta: [BetaRawContentBlockDelta](api/beta.md)

Accepts one of the following:

class BetaTextDelta { text, type }

text: String

type: :text\_delta

class BetaInputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

class BetaCitationsDelta { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

type: :citations\_delta

class BetaThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

class BetaSignatureDelta { signature, type }

signature: String

type: :signature\_delta

class BetaCompactionContentBlockDelta { content, type }

content: String

type: :compaction\_delta

index: Integer

type: :content\_block\_delta

class BetaRawContentBlockStartEvent { content\_block, index, type }

content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

index: Integer

type: :content\_block\_start

class BetaRawContentBlockStopEvent { index, type }

index: Integer

type: :content\_block\_stop

class BetaRawMessageDeltaEvent { context\_management, delta, type, usage }

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

delta: { container, stop\_details, stop\_reason, stop\_sequence}

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [BetaStopReason](api/beta.md)

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

type: :message\_delta

usage: [BetaMessageDeltaUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

input\_tokens: Integer

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

class BetaRawMessageStartEvent { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 8 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array[[BetaContentBlock](api/beta.md)]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 13 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard | :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

type: :message\_start

class BetaRawMessageStopEvent { type }

type: :message\_stop

BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](api/beta.md) { message, type }  | [BetaRawMessageDeltaEvent](api/beta.md) { context\_management, delta, type, usage }  | [BetaRawMessageStopEvent](api/beta.md) { type }  | 3 more

Accepts one of the following:

class BetaRawMessageStartEvent { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 8 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array[[BetaContentBlock](api/beta.md)]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 13 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard | :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

type: :message\_start

class BetaRawMessageDeltaEvent { context\_management, delta, type, usage }

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

delta: { container, stop\_details, stop\_reason, stop\_sequence}

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [BetaStopReason](api/beta.md)

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

type: :message\_delta

usage: [BetaMessageDeltaUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

input\_tokens: Integer

The cumulative number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

class BetaRawMessageStopEvent { type }

type: :message\_stop

class BetaRawContentBlockStartEvent { content\_block, index, type }

content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 12 more

Response model for a file uploaded to the container.

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

index: Integer

type: :content\_block\_start

class BetaRawContentBlockDeltaEvent { delta, index, type }

delta: [BetaRawContentBlockDelta](api/beta.md)

Accepts one of the following:

class BetaTextDelta { text, type }

text: String

type: :text\_delta

class BetaInputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

class BetaCitationsDelta { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

type: :citations\_delta

class BetaThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

class BetaSignatureDelta { signature, type }

signature: String

type: :signature\_delta

class BetaCompactionContentBlockDelta { content, type }

content: String

type: :compaction\_delta

index: Integer

type: :content\_block\_delta

class BetaRawContentBlockStopEvent { index, type }

index: Integer

type: :content\_block\_stop

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaRedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

class BetaRefusalStopDetails { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

class BetaRequestMCPServerToolConfiguration { allowed\_tools, enabled }

allowed\_tools: Array[String]

enabled: bool

class BetaRequestMCPServerURLDefinition { name, type, url, 2 more }

name: String

type: :url

url: String

authorization\_token: String

tool\_configuration: [BetaRequestMCPServerToolConfiguration](api/beta.md) { allowed\_tools, enabled }

allowed\_tools: Array[String]

enabled: bool

class BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :mcp\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

is\_error: bool

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUsage { web\_fetch\_requests, web\_search\_requests }

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaSignatureDelta { signature, type }

signature: String

type: :signature\_delta

class BetaSkill { skill\_id, type, version }

A skill that was loaded in a container (response model).

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

class BetaSkillParams { skill\_id, type, version }

Specification for a skill to be loaded in a container (request model).

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

BetaStopReason = :end\_turn | :max\_tokens | :stop\_sequence | 5 more

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

BetaTextCitation = [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

BetaTextCitationParam = [BetaCitationCharLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | [BetaCitationPageLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | [BetaCitationContentBlockLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | 2 more

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaTextDelta { text, type }

text: String

type: :text\_delta

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaThinkingConfigAdaptive { type, display\_ }

type: :adaptive

display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

:summarized

:omitted

class BetaThinkingConfigDisabled { type }

type: :disabled

class BetaThinkingConfigEnabled { budget\_tokens, type, display\_ }

budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

:summarized

:omitted

BetaThinkingConfigParam = [BetaThinkingConfigEnabled](api/beta.md) { budget\_tokens, type, display\_ }  | [BetaThinkingConfigDisabled](api/beta.md) { type }  | [BetaThinkingConfigAdaptive](api/beta.md) { type, display\_ }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class BetaThinkingConfigEnabled { budget\_tokens, type, display\_ }

budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

:summarized

:omitted

class BetaThinkingConfigDisabled { type }

type: :disabled

class BetaThinkingConfigAdaptive { type, display\_ }

type: :adaptive

display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

Accepts one of the following:

:summarized

:omitted

class BetaThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

class BetaThinkingTurns { type, value }

type: :thinking\_turns

value: Integer

class BetaTool { input\_schema, name, allowed\_callers, 7 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: bool

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

type: :custom

class BetaToolBash20241022 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

BetaToolChoice = [BetaToolChoiceAuto](api/beta.md) { type, disable\_parallel\_tool\_use }  | [BetaToolChoiceAny](api/beta.md) { type, disable\_parallel\_tool\_use }  | [BetaToolChoiceTool](api/beta.md) { name, type, disable\_parallel\_tool\_use }  | [BetaToolChoiceNone](api/beta.md) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class BetaToolChoiceAuto { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: :auto

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: :any

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

class BetaToolChoiceAny { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: :any

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceAuto { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: :auto

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

class BetaToolChoiceTool { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolComputerUse20241022 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124 { display\_height\_px, display\_width\_px, name, 8 more }

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20251124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: bool

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolReferenceBlock { tool\_name, type }

tool\_name: String

type: :tool\_reference

class BetaToolReferenceBlockParam { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

String

Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

class BetaToolReferenceBlockParam { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

is\_error: bool

class BetaToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

Accepts one of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

Accepts one of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

class BetaToolTextEditor20241022 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250429

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728 { name, type, allowed\_callers, 5 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250728

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: bool

When true, guarantees schema validation on tool names and inputs

BetaToolUnion = [BetaTool](api/beta.md) { input\_schema, name, allowed\_callers, 7 more }  | [BetaToolBash20241022](api/beta.md) { name, type, allowed\_callers, 4 more }  | [BetaToolBash20250124](api/beta.md) { name, type, allowed\_callers, 4 more }  | 19 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

Accepts one of the following:

class BetaTool { input\_schema, name, allowed\_callers, 7 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: bool

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

type: :custom

class BetaToolBash20241022 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolBash20250124 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250522 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250522

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20250825 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250825

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaCodeExecutionTool20260120 { name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260120

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20241022 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaMemoryTool20250818 { name, type, allowed\_callers, 4 more }

name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :memory\_20250818

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20250124 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20241022 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolComputerUse20251124 { display\_height\_px, display\_width\_px, name, 8 more }

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20251124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: bool

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250124 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250429 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250429

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolTextEditor20250728 { name, type, allowed\_callers, 5 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250728

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20250305 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20250305

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

user\_location: [BetaUserLocation](api/beta.md) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchTool20250910 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20250910

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaWebSearchTool20260209 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20260209

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

user\_location: [BetaUserLocation](api/beta.md) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchTool20260209 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260209

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260309 { name, type, allowed\_callers, 9 more }

Web fetch tool with use\_cache parameter for bypassing cached content.

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260309

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

use\_cache: bool

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class BetaToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

Accepts one of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

Accepts one of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaMCPToolset { mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: String

Name of the MCP server to configure tools for

type: :mcp\_toolset

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

configs: Hash[Symbol, [BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: bool

enabled: bool

default\_config: [BetaMCPToolDefaultConfig](api/beta.md) { defer\_loading, enabled }

Default configuration applied to all tools from this server

defer\_loading: bool

enabled: bool

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaToolUsesKeep { type, value }

type: :tool\_uses

value: Integer

class BetaToolUsesTrigger { type, value }

type: :tool\_uses

value: Integer

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard | :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

class BetaUserLocation { type, city, country, 2 more }

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

class BetaWebFetchTool20250910 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20250910

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260209 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260209

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

class BetaWebFetchTool20260309 { name, type, allowed\_callers, 9 more }

Web fetch tool with use\_cache parameter for bypassing cached content.

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260309

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

use\_cache: bool

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  | [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlockParam { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: Array[[BetaTextCitationParam](api/beta.md)]

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

class BetaImageBlockParam { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type }

Accepts one of the following:

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

class BetaURLImageSource { type, url }

type: :url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

type: :image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

type: :content

class BetaURLPDFSource { type, url }

type: :url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

type: :document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

citations: [BetaCitationsConfigParam](api/beta.md) { enabled }

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchToolResultErrorBlockParam { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

BetaWebFetchToolResultErrorCode = :invalid\_tool\_input | :url\_too\_long | :url\_not\_allowed | 5 more

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

class BetaWebSearchResultBlock { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

class BetaWebSearchResultBlockParam { encrypted\_content, title, type, 2 more }

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String

class BetaWebSearchTool20250305 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20250305

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

user\_location: [BetaUserLocation](api/beta.md) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebSearchTool20260209 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20260209

allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120]

Accepts one of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

user\_location: [BetaUserLocation](api/beta.md) { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

class BetaWebSearchToolRequestError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

BetaWebSearchToolResultBlockContent = [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  | Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more }

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String

class BetaWebSearchToolRequestError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

BetaWebSearchToolResultBlockParamContent = Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ] | [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type }

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String

class BetaWebSearchToolRequestError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

BetaWebSearchToolResultErrorCode = :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 3 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

beta.messages.batches.create(\*\*kwargs) -> [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

beta.messages.batches.retrieve(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

beta.messages.batches.list(\*\*kwargs) -> Page<[BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more } >

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

beta.messages.batches.cancel(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

beta.messages.batches.delete(message\_batch\_id, \*\*kwargs) -> [BetaDeletedMessageBatch](api/beta.md) { id, type }

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

beta.messages.batches.results(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatchIndividualResponse](api/beta.md) { custom\_id, result }

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class BetaDeletedMessageBatch { id, type }

id: String

ID of the Message Batch.

type: :message\_batch\_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

class BetaMessageBatch { id, archived\_at, cancel\_initiated\_at, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

ended\_at: Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

processing\_status: :in\_progress | :canceling | :ended

Processing status of the Message Batch.

Accepts one of the following:

:in\_progress

:canceling

:ended

request\_counts: [BetaMessageBatchRequestCounts](api/beta.md) { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.

succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results\_url: String

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: :message\_batch

Object type.

For Message Batches, this is always `"message_batch"`.

class BetaMessageBatchCanceledResult { type }

type: :canceled

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored

class BetaMessageBatchExpiredResult { type }

type: :expired

class BetaMessageBatchIndividualResponse { custom\_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom\_id: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchResult](api/beta.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 8 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array[[BetaContentBlock](api/beta.md)]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 13 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard | :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

type: :succeeded

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored

class BetaMessageBatchCanceledResult { type }

type: :canceled

class BetaMessageBatchExpiredResult { type }

type: :expired

class BetaMessageBatchRequestCounts { canceled, errored, expired, 2 more }

canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.

succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

BetaMessageBatchResult = [BetaMessageBatchSucceededResult](api/beta.md) { message, type }  | [BetaMessageBatchErroredResult](api/beta.md) { error, type }  | [BetaMessageBatchCanceledResult](api/beta.md) { type }  | [BetaMessageBatchExpiredResult](api/beta.md) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

Accepts one of the following:

class BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 8 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array[[BetaContentBlock](api/beta.md)]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 13 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard | :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

type: :succeeded

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored

class BetaMessageBatchCanceledResult { type }

type: :canceled

class BetaMessageBatchExpiredResult { type }

type: :expired

class BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 8 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

content: Array[[BetaContentBlock](api/beta.md)]

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```

If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```

Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```

Accepts one of the following:

class BetaTextBlock { citations, text, type }

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaServerToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: :web\_search | :web\_fetch | :code\_execution | 4 more

Accepts one of the following:

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebSearchToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

Accepts one of the following:

class BetaWebFetchToolResultErrorBlock { error\_code, type }

error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error

class BetaWebFetchBlock { content, retrieved\_at, type, url }

content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

type: :base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

class BetaServerToolCaller20260120 { tool\_id, type }

tool\_id: String

type: :code\_execution\_20260120

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaBashCodeExecutionToolResultError { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

Accepts one of the following:

class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

class BetaToolSearchToolResultBlock { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

Accepts one of the following:

class BetaToolSearchToolResultError { error\_code, error\_message, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type }

content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

Accepts one of the following:

String

Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

Accepts one of the following:

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

class BetaCompactionBlock { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

type: :compaction

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview" | :"claude-opus-4-6" | :"claude-sonnet-4-6" | 13 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

:"claude-opus-4-0"

Powerful model for complex tasks

:"claude-opus-4-20250514"

Powerful model for complex tasks

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-3-haiku-20240307"

Fast and cost-effective model

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, type }

Structured information about a refusal.

category: :cyber | :bio

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

Accepts one of the following:

:cyber

:bio

explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: :refusal

stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.

iterations: [BetaIterationsUsage](api/beta.md) { ,  }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

Accepts one of the following:

class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration

class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration

output\_tokens: Integer

The number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

speed: :standard | :fast

The inference speed mode used for this request.

Accepts one of the following:

:standard

:fast

type: :succeeded

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

beta.agents.create(\*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more }

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

beta.agents.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more } >

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

beta.agents.retrieve(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more }

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

beta.agents.update(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more }

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

beta.agents.archive(agent\_id, \*\*kwargs) -> [BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more }

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsAgent { id, archived\_at, created\_at, 11 more }

A Managed Agents `agent`.

id: String

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

description: String

mcp\_servers: Array[[BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url } ]

name: String

type: :url

url: String

metadata: Hash[Symbol, String]

model: [BetaManagedAgentsModelConfig](api/beta.md) { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

updated\_at: Time

A timestamp in RFC 3339 format

version: Integer

The agent's current version. Starts at 1 and increments when the agent is modified.

class BetaManagedAgentsAgentToolConfig { enabled, name, permission\_policy }

Configuration for a specific agent tool.

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

class BetaManagedAgentsAgentToolConfigParams { name, enabled, permission\_policy }

Configuration override for a specific tool within a toolset.

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

enabled: bool

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

class BetaManagedAgentsAgentToolsetDefaultConfig { enabled, permission\_policy }

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

class BetaManagedAgentsAgentToolsetDefaultConfigParams { enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: bool

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

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

class BetaManagedAgentsAgentToolset20260401Params { type, configs, default\_config }

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: :agent\_toolset\_20260401

configs: Array[[BetaManagedAgentsAgentToolConfigParams](api/beta.md) { name, enabled, permission\_policy } ]

Per-tool configuration overrides.

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

enabled: bool

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsAgentToolsetDefaultConfigParams](api/beta.md) { enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: bool

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

class BetaManagedAgentsAnthropicSkill { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: String

type: :anthropic

version: String

class BetaManagedAgentsAnthropicSkillParams { skill\_id, type, version }

An Anthropic-managed skill.

skill\_id: String

Identifier of the Anthropic skill (e.g., "xlsx").

type: :anthropic

version: String

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkill { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: String

type: :custom

version: String

class BetaManagedAgentsCustomSkillParams { skill\_id, type, version }

A user-created custom skill.

skill\_id: String

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: :custom

version: String

Version to pin. Defaults to latest if omitted.

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

class BetaManagedAgentsCustomToolInputSchema { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

class BetaManagedAgentsCustomToolParams { description, input\_schema, name, type }

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: String

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

input\_schema: [BetaManagedAgentsCustomToolInputSchema](api/beta.md) { properties, required, type }

JSON Schema for custom tool input parameters.

properties: Hash[Symbol, untyped]

JSON Schema properties defining the tool's input parameters.

required: Array[String]

List of required property names.

type: :object

Must be 'object' for tool input schemas.

name: String

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: :custom

class BetaManagedAgentsMCPServerURLDefinition { name, type, url }

URL-based MCP server connection as returned in API responses.

name: String

type: :url

url: String

class BetaManagedAgentsMCPToolConfig { enabled, name, permission\_policy }

Resolved configuration for a specific MCP tool.

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

class BetaManagedAgentsMCPToolConfigParams { name, enabled, permission\_policy }

Configuration override for a specific MCP tool.

name: String

Name of the MCP tool to configure. 1-128 characters.

enabled: bool

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

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

class BetaManagedAgentsMCPToolsetDefaultConfig { enabled, permission\_policy }

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

class BetaManagedAgentsMCPToolsetDefaultConfigParams { enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: bool

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

class BetaManagedAgentsMCPToolsetParams { mcp\_server\_name, type, configs, default\_config }

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: String

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: :mcp\_toolset

configs: Array[[BetaManagedAgentsMCPToolConfigParams](api/beta.md) { name, enabled, permission\_policy } ]

Per-tool configuration overrides.

name: String

Name of the MCP tool to configure. 1-128 characters.

enabled: bool

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

default\_config: [BetaManagedAgentsMCPToolsetDefaultConfigParams](api/beta.md) { enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: bool

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  | [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

Accepts one of the following:

class BetaManagedAgentsAlwaysAllowPolicy { type }

Tool calls are automatically approved without user confirmation.

type: :always\_allow

class BetaManagedAgentsAlwaysAskPolicy { type }

Tool calls require user confirmation before execution.

type: :always\_ask

BetaManagedAgentsModel = :"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more | String

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

class BetaManagedAgentsModelConfig { id, speed }

Model identifier and configuration.

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

class BetaManagedAgentsModelConfigParams { id, speed }

An object that defines additional configuration control over model use

id: [BetaManagedAgentsModel](api/beta.md)

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

BetaManagedAgentsSkillParams = [BetaManagedAgentsAnthropicSkillParams](api/beta.md) { skill\_id, type, version }  | [BetaManagedAgentsCustomSkillParams](api/beta.md) { skill\_id, type, version }

Skill to load in the session container.

Accepts one of the following:

class BetaManagedAgentsAnthropicSkillParams { skill\_id, type, version }

An Anthropic-managed skill.

skill\_id: String

Identifier of the Anthropic skill (e.g., "xlsx").

type: :anthropic

version: String

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsCustomSkillParams { skill\_id, type, version }

A user-created custom skill.

skill\_id: String

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: :custom

version: String

Version to pin. Defaults to latest if omitted.

class BetaManagedAgentsURLMCPServerParams { name, type, url }

URL-based MCP server connection.

name: String

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: :url

url: String

Endpoint URL for the MCP server.

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

beta.agents.versions.list(agent\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsAgent](api/beta.md) { id, archived\_at, created\_at, 11 more } >

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

beta.environments.create(\*\*kwargs) -> [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

beta.environments.list(\*\*kwargs) -> PageCursor<[BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more } >

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

beta.environments.retrieve(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

beta.environments.update(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

beta.environments.delete(environment\_id, \*\*kwargs) -> [BetaEnvironmentDeleteResponse](api/beta.md) { id, type }

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

beta.environments.archive(environment\_id, \*\*kwargs) -> [BetaEnvironment](api/beta.md) { id, archived\_at, config, 6 more }

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

class BetaCloudConfig { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: :unrestricted

Network policy type

class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type

packages: [BetaPackages](api/beta.md) { apt, cargo, gem\_, 4 more }

Package manager configuration.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

type: :cloud

Environment type

class BetaCloudConfigParams { type, networking, packages }

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :cloud

Environment type

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetworkParams](api/beta.md) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Network configuration policy. Omit on update to preserve the existing value.

Accepts one of the following:

class BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: :unrestricted

Network policy type

class BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :limited

Network policy type

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

packages: [BetaPackagesParams](api/beta.md) { apt, cargo, gem\_, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

class BetaEnvironment { id, archived\_at, config, 6 more }

Unified Environment resource for both cloud and BYOC environments.

id: String

Environment identifier (e.g., 'env\_...')

archived\_at: String

RFC 3339 timestamp when environment was archived, or null if not archived

config: [BetaCloudConfig](api/beta.md) { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  | [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

Accepts one of the following:

class BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: :unrestricted

Network policy type

class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type

packages: [BetaPackages](api/beta.md) { apt, cargo, gem\_, 4 more }

Package manager configuration.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

type: :cloud

Environment type

created\_at: String

RFC 3339 timestamp when environment was created

description: String

User-provided description for the environment

metadata: Hash[Symbol, String]

User-provided metadata key-value pairs

name: String

Human-readable name for the environment

type: :environment

The type of object (always 'environment')

updated\_at: String

RFC 3339 timestamp when environment was last updated

class BetaEnvironmentDeleteResponse { id, type }

Response after deleting an environment.

id: String

Environment identifier

type: :environment\_deleted

The type of response

class BetaLimitedNetwork { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

type: :limited

Network policy type

class BetaLimitedNetworkParams { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: :limited

Network policy type

allow\_mcp\_servers: bool

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: bool

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: Array[String]

Specifies domains the container can reach.

class BetaPackages { apt, cargo, gem\_, 4 more }

Packages (and their versions) available in this environment.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

class BetaPackagesParams { apt, cargo, gem\_, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: Array[String]

Ubuntu/Debian packages to install

cargo: Array[String]

Rust packages to install

gem\_: Array[String]

Ruby packages to install

go: Array[String]

Go packages to install

npm: Array[String]

Node.js packages to install

pip: Array[String]

Python packages to install

type: :packages

Package configuration type

class BetaUnrestrictedNetwork { type }

Unrestricted network access.

type: :unrestricted

Network policy type

#### BetaSessions

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

:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

:"claude-opus-4-6" | :"claude-sonnet-4-6" | :"claude-haiku-4-5" | 5 more

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

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

#### BetaSessionsEvents

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

#### BetaSessionsResources

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

BetaManagedAgentsSessionResource = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

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

ResourceRetrieveResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

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

ResourceUpdateResponse = [BetaManagedAgentsGitHubRepositoryResource](api/beta.md) { id, created\_at, mount\_path, 4 more }  | [BetaManagedAgentsFileResource](api/beta.md) { id, created\_at, file\_id, 3 more }

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

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

beta.vaults.create(\*\*kwargs) -> [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

beta.vaults.list(\*\*kwargs) -> PageCursor<[BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more } >

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

beta.vaults.retrieve(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

beta.vaults.update(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

beta.vaults.delete(vault\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedVault](api/beta.md) { id, type }

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

beta.vaults.archive(vault\_id, \*\*kwargs) -> [BetaManagedAgentsVault](api/beta.md) { id, archived\_at, created\_at, 4 more }

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsDeletedVault { id, type }

Confirmation of a deleted vault.

id: String

Unique identifier of the deleted vault.

type: :vault\_deleted

class BetaManagedAgentsVault { id, archived\_at, created\_at, 4 more }

A vault that stores credentials for use by agents during sessions.

id: String

Unique identifier for the vault.

archived\_at: Time

A timestamp in RFC 3339 format

created\_at: Time

A timestamp in RFC 3339 format

display\_name: String

Human-readable name for the vault.

metadata: Hash[Symbol, String]

Arbitrary key-value metadata attached to the vault.

type: :vault

updated\_at: Time

A timestamp in RFC 3339 format

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

beta.vaults.credentials.create(vault\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

beta.vaults.credentials.list(vault\_id, \*\*kwargs) -> PageCursor<[BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more } >

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

beta.vaults.credentials.retrieve(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

beta.vaults.credentials.update(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

beta.vaults.credentials.delete(credential\_id, \*\*kwargs) -> [BetaManagedAgentsDeletedCredential](api/beta.md) { id, type }

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

beta.vaults.credentials.archive(credential\_id, \*\*kwargs) -> [BetaManagedAgentsCredential](api/beta.md) { id, archived\_at, auth, 6 more }

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### ModelsExpand Collapse

class BetaManagedAgentsCredential { id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

id: String

Unique identifier for the credential.

archived\_at: Time

A timestamp in RFC 3339 format

auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta.md) { mcp\_server\_url, type, expires\_at, refresh }  | [BetaManagedAgentsStaticBearerAuthResponse](api/beta.md) { mcp\_server\_url, type }

Authentication details for a credential.

Accepts one of the following:

class BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :mcp\_oauth

expires\_at: Time

A timestamp in RFC 3339 format

refresh: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: String

OAuth client ID.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :static\_bearer

created\_at: Time

A timestamp in RFC 3339 format

metadata: Hash[Symbol, String]

Arbitrary key-value metadata attached to the credential.

type: :vault\_credential

updated\_at: Time

A timestamp in RFC 3339 format

vault\_id: String

Identifier of the vault this credential belongs to.

display\_name: String

Human-readable name for the credential.

class BetaManagedAgentsDeletedCredential { id, type }

Confirmation of a deleted credential.

id: String

Unique identifier of the deleted credential.

type: :vault\_credential\_deleted

class BetaManagedAgentsMCPOAuthAuthResponse { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :mcp\_oauth

expires\_at: Time

A timestamp in RFC 3339 format

refresh: [BetaManagedAgentsMCPOAuthRefreshResponse](api/beta.md) { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: String

OAuth client ID.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthCreateParams { access\_token, mcp\_server\_url, type, 2 more }

Parameters for creating an MCP OAuth credential.

access\_token: String

OAuth access token.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :mcp\_oauth

expires\_at: Time

A timestamp in RFC 3339 format

refresh: [BetaManagedAgentsMCPOAuthRefreshParams](api/beta.md) { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: String

OAuth client ID.

refresh\_token: String

OAuth refresh token.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  | [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthRefreshParams { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: String

OAuth client ID.

refresh\_token: String

OAuth refresh token.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  | [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthRefreshResponse { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: String

OAuth client ID.

token\_endpoint: String

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  | [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

resource: String

OAuth resource indicator.

scope: String

OAuth scope for the refresh request.

class BetaManagedAgentsMCPOAuthRefreshUpdateParams { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: String

Updated OAuth refresh token.

scope: String

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: :client\_secret\_basic

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: :client\_secret\_post

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsMCPOAuthUpdateParams { type, access\_token, expires\_at, refresh }

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: :mcp\_oauth

access\_token: String

Updated OAuth access token.

expires\_at: Time

A timestamp in RFC 3339 format

refresh: [BetaManagedAgentsMCPOAuthRefreshUpdateParams](api/beta.md) { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: String

Updated OAuth refresh token.

scope: String

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  | [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

Accepts one of the following:

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: :client\_secret\_basic

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: :client\_secret\_post

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsStaticBearerAuthResponse { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :static\_bearer

class BetaManagedAgentsStaticBearerCreateParams { token, mcp\_server\_url, type }

Parameters for creating a static bearer token credential.

token: String

Static bearer token value.

mcp\_server\_url: String

URL of the MCP server this credential authenticates against.

type: :static\_bearer

class BetaManagedAgentsStaticBearerUpdateParams { type, token }

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: :static\_bearer

token: String

Updated static bearer token value.

class BetaManagedAgentsTokenEndpointAuthBasicParam { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthBasicResponse { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: :client\_secret\_basic

class BetaManagedAgentsTokenEndpointAuthBasicUpdateParam { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: :client\_secret\_basic

client\_secret: String

Updated OAuth client secret.

class BetaManagedAgentsTokenEndpointAuthNoneParam { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthNoneResponse { type }

Token endpoint requires no client authentication.

type: :none

class BetaManagedAgentsTokenEndpointAuthPostParam { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: String

OAuth client secret.

type: :client\_secret\_post

class BetaManagedAgentsTokenEndpointAuthPostResponse { type }

Token endpoint uses POST body authentication with client credentials.

type: :client\_secret\_post

class BetaManagedAgentsTokenEndpointAuthPostUpdateParam { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: :client\_secret\_post

client\_secret: String

Updated OAuth client secret.

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

beta.files.upload(\*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 5 more }

POST/v1/files

##### [List Files](api/beta/files/list.md)

beta.files.list(\*\*kwargs) -> Page<[FileMetadata](api/beta.md) { id, created\_at, filename, 5 more } >

GET/v1/files

##### [Download File](api/beta/files/download.md)

beta.files.download(file\_id, \*\*kwargs) -> StringIO

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta.files.retrieve\_metadata(file\_id, \*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 5 more }

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta.files.delete(file\_id, \*\*kwargs) -> [DeletedFile](api/beta.md) { id, type }

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

class BetaFileScope { id, type }

id: String

The ID of the scoping resource (e.g., the session ID).

type: :session

The type of scope (e.g., `"session"`).

class DeletedFile { id, type }

id: String

ID of the deleted file.

type: :file\_deleted

Deleted object type.

For file deletion, this is always `"file_deleted"`.

class FileMetadata { id, created\_at, filename, 5 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

created\_at: Time

RFC 3339 datetime string representing when the file was created.

filename: String

Original filename of the uploaded file.

mime\_type: String

MIME type of the file.

size\_bytes: Integer

Size of the file in bytes.

type: :file

Object type.

For files, this is always `"file"`.

downloadable: bool

Whether the file can be downloaded.

scope: [BetaFileScope](api/beta.md) { id, type }

The scope of this file, indicating the context in which it was created (e.g., a session).

id: String

The ID of the scoping resource (e.g., the session ID).

type: :session

The type of scope (e.g., `"session"`).

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

beta.skills.create(\*\*kwargs) -> [SkillCreateResponse](api/beta.md) { id, created\_at, display\_title, 4 more }

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

beta.skills.list(\*\*kwargs) -> PageCursor<[SkillListResponse](api/beta.md) { id, created\_at, display\_title, 4 more } >

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

beta.skills.retrieve(skill\_id, \*\*kwargs) -> [SkillRetrieveResponse](api/beta.md) { id, created\_at, display\_title, 4 more }

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

beta.skills.delete(skill\_id, \*\*kwargs) -> [SkillDeleteResponse](api/beta.md) { id, type }

DELETE/v1/skills/{skill\_id}

##### ModelsExpand Collapse

class SkillCreateResponse { id, created\_at, display\_title, 4 more }

id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill was created.

display\_title: String

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest\_version: String

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: String

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: String

Object type.

For Skills, this is always `"skill"`.

updated\_at: String

ISO 8601 timestamp of when the skill was last updated.

class SkillListResponse { id, created\_at, display\_title, 4 more }

id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill was created.

display\_title: String

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest\_version: String

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: String

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: String

Object type.

For Skills, this is always `"skill"`.

updated\_at: String

ISO 8601 timestamp of when the skill was last updated.

class SkillRetrieveResponse { id, created\_at, display\_title, 4 more }

id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill was created.

display\_title: String

Display title for the skill.

This is a human-readable label that is not included in the prompt sent to the model.

latest\_version: String

The latest version identifier for the skill.

This represents the most recent version of the skill that has been created.

source: String

Source of the skill.

This may be one of the following values:

- `"custom"`: the skill was created by a user
- `"anthropic"`: the skill was created by Anthropic

type: String

Object type.

For Skills, this is always `"skill"`.

updated\_at: String

ISO 8601 timestamp of when the skill was last updated.

class SkillDeleteResponse { id, type }

id: String

Unique identifier for the skill.

The format and length of IDs may change over time.

type: String

Deleted object type.

For Skills, this is always `"skill_deleted"`.

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta.skills.versions.create(skill\_id, \*\*kwargs) -> [VersionCreateResponse](api/beta.md) { id, created\_at, description, 5 more }

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(skill\_id, \*\*kwargs) -> PageCursor<[VersionListResponse](api/beta.md) { id, created\_at, description, 5 more } >

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(version, \*\*kwargs) -> [VersionRetrieveResponse](api/beta.md) { id, created\_at, description, 5 more }

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(version, \*\*kwargs) -> [VersionDeleteResponse](api/beta.md) { id, type }

DELETE/v1/skills/{skill\_id}/versions/{version}

##### ModelsExpand Collapse

class VersionCreateResponse { id, created\_at, description, 5 more }

id: String

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill version was created.

description: String

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: String

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: String

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: String

Identifier for the skill that this version belongs to.

type: String

Object type.

For Skill Versions, this is always `"skill_version"`.

version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

class VersionListResponse { id, created\_at, description, 5 more }

id: String

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill version was created.

description: String

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: String

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: String

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: String

Identifier for the skill that this version belongs to.

type: String

Object type.

For Skill Versions, this is always `"skill_version"`.

version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

class VersionRetrieveResponse { id, created\_at, description, 5 more }

id: String

Unique identifier for the skill version.

The format and length of IDs may change over time.

created\_at: String

ISO 8601 timestamp of when the skill version was created.

description: String

Description of the skill version.

This is extracted from the SKILL.md file in the skill upload.

directory: String

Directory name of the skill version.

This is the top-level directory name that was extracted from the uploaded files.

name: String

Human-readable name of the skill version.

This is extracted from the SKILL.md file in the skill upload.

skill\_id: String

Identifier for the skill that this version belongs to.

type: String

Object type.

For Skill Versions, this is always `"skill_version"`.

version: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

class VersionDeleteResponse { id, type }

id: String

Version identifier for the skill.

Each version is identified by a Unix epoch timestamp (e.g., "1759178010641129").

type: String

Deleted object type.

For Skill Versions, this is always `"skill_version_deleted"`.

---

*Copyright © Anthropic. All rights reserved.*
