# Beta

Copy page

Ruby

# Beta

##### ModelsExpand Collapse

AnthropicBeta = String | :"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 16 more

Accepts one of the following:

String

:"message-batches-2024-09-24" | :"prompt-caching-2024-07-31" | :"computer-use-2024-10-22" | 16 more

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

class BetaAPIError { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

BetaError = [BetaInvalidRequestError](api/beta.md) { message, type }  | [BetaAuthenticationError](api/beta.md) { message, type }  | [BetaBillingError](api/beta.md) { message, type }  | 6 more

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

class BetaErrorResponse { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

request\_id: String

type: :error

Accepts one of the following:

:error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

#### BetaModels

##### [List Models](api/beta/models/list.md)

beta.models.list(\*\*kwargs) -> Page<[BetaModelInfo](api/beta.md) { id, created\_at, display\_name, type } >

get/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

beta.models.retrieve(model\_id, \*\*kwargs) -> [BetaModelInfo](api/beta.md) { id, created\_at, display\_name, type }

get/v1/models/{model\_id}

##### ModelsExpand Collapse

class BetaModelInfo { id, created\_at, display\_name, type }

id: String

Unique model identifier.

created\_at: Time

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

formatdate-time

display\_name: String

A human-readable name for the model.

type: :model

Object type.

For Models, this is always `"model"`.

Accepts one of the following:

:model

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

beta.messages.create(\*\*kwargs) -> [BetaMessage](api/beta.md) { id, container, content, 7 more }

post/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

beta.messages.count\_tokens(\*\*kwargs) -> [BetaMessageTokensCount](api/beta.md) { context\_management, input\_tokens }

post/v1/messages/count\_tokens

##### ModelsExpand Collapse

class BetaAllThinkingTurns { type }

type: :all

Accepts one of the following:

:all

class BetaBase64ImageSource { data, media\_type, type }

data: String

media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

Accepts one of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64

Accepts one of the following:

:base64

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaBashCodeExecutionOutputBlock { file\_id, type }

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

class BetaBashCodeExecutionOutputBlockParam { file\_id, type }

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaCacheControlEphemeral { type, ttl }

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

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

Accepts one of the following:

:content\_block\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

type: :citations\_delta

Accepts one of the following:

:citations\_delta

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaClearThinking20251015Edit { type, keep }

type: :clear\_thinking\_20251015

Accepts one of the following:

:clear\_thinking\_20251015

keep: [BetaThinkingTurns](api/beta.md) { type, value }  | [BetaAllThinkingTurns](api/beta.md) { type }  | :all

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns { type, value }

type: :thinking\_turns

Accepts one of the following:

:thinking\_turns

value: Integer

class BetaAllThinkingTurns { type }

type: :all

Accepts one of the following:

:all

Keep = :all

Accepts one of the following:

:all

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

class BetaClearToolUses20250919Edit { type, clear\_at\_least, clear\_tool\_inputs, 3 more }

type: :clear\_tool\_uses\_20250919

Accepts one of the following:

:clear\_tool\_uses\_20250919

clear\_at\_least: [BetaInputTokensClearAtLeast](api/beta.md) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: :input\_tokens

Accepts one of the following:

:input\_tokens

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

Accepts one of the following:

:tool\_uses

value: Integer

trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }  | [BetaToolUsesTrigger](api/beta.md) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger { type, value }

type: :input\_tokens

Accepts one of the following:

:input\_tokens

value: Integer

class BetaToolUsesTrigger { type, value }

type: :tool\_uses

Accepts one of the following:

:tool\_uses

value: Integer

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaCodeExecutionOutputBlock { file\_id, type }

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

class BetaCodeExecutionOutputBlockParam { file\_id, type }

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

class BetaCodeExecutionTool20250522 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:code\_execution

type: :code\_execution\_20250522

Accepts one of the following:

:code\_execution\_20250522

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaCodeExecutionTool20250825 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:code\_execution

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

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

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaContainer { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaContainerParams { id, skills }

Container parameters with skills to be loaded.

id: String

Container id

skills: Array[[BetaSkillParams](api/beta.md) { skill\_id, type, version } ]

List of skills to load in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

class BetaContainerUploadBlockParam { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

BetaContentBlock = [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 11 more

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

BetaContentBlockParam = [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }  | 15 more

Regular text content.

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

Accepts one of the following:

:tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:server\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:mcp\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:mcp\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

is\_error: bool

class BetaContainerUploadBlockParam { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

BetaContentBlockSourceContent = [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

edits: Array[[BetaClearToolUses20250919Edit](api/beta.md) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  | [BetaClearThinking20251015Edit](api/beta.md) { type, keep } ]

List of context management edits to apply

Accepts one of the following:

class BetaClearToolUses20250919Edit { type, clear\_at\_least, clear\_tool\_inputs, 3 more }

type: :clear\_tool\_uses\_20250919

Accepts one of the following:

:clear\_tool\_uses\_20250919

clear\_at\_least: [BetaInputTokensClearAtLeast](api/beta.md) { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: :input\_tokens

Accepts one of the following:

:input\_tokens

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

Accepts one of the following:

:tool\_uses

value: Integer

trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }  | [BetaToolUsesTrigger](api/beta.md) { type, value }

Condition that triggers the context management strategy

Accepts one of the following:

class BetaInputTokensTrigger { type, value }

type: :input\_tokens

Accepts one of the following:

:input\_tokens

value: Integer

class BetaToolUsesTrigger { type, value }

type: :tool\_uses

Accepts one of the following:

:tool\_uses

value: Integer

class BetaClearThinking20251015Edit { type, keep }

type: :clear\_thinking\_20251015

Accepts one of the following:

:clear\_thinking\_20251015

keep: [BetaThinkingTurns](api/beta.md) { type, value }  | [BetaAllThinkingTurns](api/beta.md) { type }  | :all

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

Accepts one of the following:

class BetaThinkingTurns { type, value }

type: :thinking\_turns

Accepts one of the following:

:thinking\_turns

value: Integer

class BetaAllThinkingTurns { type }

type: :all

Accepts one of the following:

:all

Keep = :all

Accepts one of the following:

:all

class BetaContextManagementResponse { applied\_edits }

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

class BetaCountTokensContextManagementResponse { original\_input\_tokens }

original\_input\_tokens: Integer

The original token count before context management was applied

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaDocumentBlock { citations, source, title, type }

citations: [BetaCitationConfig](api/beta.md) { enabled }

Citation configuration for the document

enabled: bool

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:input\_json\_delta

class BetaInputTokensClearAtLeast { type, value }

type: :input\_tokens

Accepts one of the following:

:input\_tokens

value: Integer

class BetaInputTokensTrigger { type, value }

type: :input\_tokens

Accepts one of the following:

:input\_tokens

value: Integer

class BetaJSONOutputFormat { schema, type }

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema

Accepts one of the following:

:json\_schema

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

class BetaMCPToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

maxLength255

minLength1

type: :mcp\_toolset

Accepts one of the following:

:mcp\_toolset

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:memory

type: :memory\_20250818

Accepts one of the following:

:memory\_20250818

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

BetaMemoryTool20250818Command = [BetaMemoryTool20250818ViewCommand](api/beta.md) { command, path, view\_range }  | [BetaMemoryTool20250818CreateCommand](api/beta.md) { command, file\_text, path }  | [BetaMemoryTool20250818StrReplaceCommand](api/beta.md) { command, new\_str, old\_str, path }  | 3 more

Accepts one of the following:

class BetaMemoryTool20250818ViewCommand { command, path, view\_range }

command: :view

Command type identifier

Accepts one of the following:

:view

path: String

Path to directory or file to view

view\_range: Array[Integer]

Optional line range for viewing specific lines

class BetaMemoryTool20250818CreateCommand { command, file\_text, path }

command: :create

Command type identifier

Accepts one of the following:

:create

file\_text: String

Content to write to the file

path: String

Path where the file should be created

class BetaMemoryTool20250818StrReplaceCommand { command, new\_str, old\_str, path }

command: :str\_replace

Command type identifier

Accepts one of the following:

:str\_replace

new\_str: String

Text to replace with

old\_str: String

Text to search for and replace

path: String

Path to the file where text should be replaced

class BetaMemoryTool20250818InsertCommand { command, insert\_line, insert\_text, path }

command: :insert

Command type identifier

Accepts one of the following:

:insert

insert\_line: Integer

Line number where text should be inserted

minimum1

insert\_text: String

Text to insert at the specified line

path: String

Path to the file where text should be inserted

class BetaMemoryTool20250818DeleteCommand { command, path }

command: :delete

Command type identifier

Accepts one of the following:

:delete

path: String

Path to the file or directory to delete

class BetaMemoryTool20250818RenameCommand { command, new\_path, old\_path }

command: :rename

Command type identifier

Accepts one of the following:

:rename

new\_path: String

New path for the file or directory

old\_path: String

Current path of the file or directory

class BetaMemoryTool20250818CreateCommand { command, file\_text, path }

command: :create

Command type identifier

Accepts one of the following:

:create

file\_text: String

Content to write to the file

path: String

Path where the file should be created

class BetaMemoryTool20250818DeleteCommand { command, path }

command: :delete

Command type identifier

Accepts one of the following:

:delete

path: String

Path to the file or directory to delete

class BetaMemoryTool20250818InsertCommand { command, insert\_line, insert\_text, path }

command: :insert

Command type identifier

Accepts one of the following:

:insert

insert\_line: Integer

Line number where text should be inserted

minimum1

insert\_text: String

Text to insert at the specified line

path: String

Path to the file where text should be inserted

class BetaMemoryTool20250818RenameCommand { command, new\_path, old\_path }

command: :rename

Command type identifier

Accepts one of the following:

:rename

new\_path: String

New path for the file or directory

old\_path: String

Current path of the file or directory

class BetaMemoryTool20250818StrReplaceCommand { command, new\_str, old\_str, path }

command: :str\_replace

Command type identifier

Accepts one of the following:

:str\_replace

new\_str: String

Text to replace with

old\_str: String

Text to search for and replace

path: String

Path to the file where text should be replaced

class BetaMemoryTool20250818ViewCommand { command, path, view\_range }

command: :view

Command type identifier

Accepts one of the following:

:view

path: String

Path to directory or file to view

view\_range: Array[Integer]

Optional line range for viewing specific lines

class BetaMessage { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

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

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

class BetaMessageDeltaUsage { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The cumulative number of input tokens which were used.

minimum0

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

class BetaMessageParam { content, role }

content: String | Array[[BetaContentBlockParam](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockParam](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :tool\_result

Accepts one of the following:

:tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:server\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultErrorParam { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:mcp\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:mcp\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

is\_error: bool

class BetaContainerUploadBlockParam { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

maxLength256

class BetaOutputConfig { effort }

effort: :low | :medium | :high

All possible effort levels.

Accepts one of the following:

:low

:medium

:high

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

BetaRawContentBlockDelta = [BetaTextDelta](api/beta.md) { text, type }  | [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  | [BetaCitationsDelta](api/beta.md) { citation, type }  | 2 more

Accepts one of the following:

class BetaTextDelta { text, type }

text: String

type: :text\_delta

Accepts one of the following:

:text\_delta

class BetaInputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

Accepts one of the following:

:input\_json\_delta

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

type: :citations\_delta

Accepts one of the following:

:citations\_delta

class BetaThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

Accepts one of the following:

:thinking\_delta

class BetaSignatureDelta { signature, type }

signature: String

type: :signature\_delta

Accepts one of the following:

:signature\_delta

class BetaRawContentBlockDeltaEvent { delta, index, type }

delta: [BetaRawContentBlockDelta](api/beta.md)

Accepts one of the following:

class BetaTextDelta { text, type }

text: String

type: :text\_delta

Accepts one of the following:

:text\_delta

class BetaInputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

Accepts one of the following:

:input\_json\_delta

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

type: :citations\_delta

Accepts one of the following:

:citations\_delta

class BetaThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

Accepts one of the following:

:thinking\_delta

class BetaSignatureDelta { signature, type }

signature: String

type: :signature\_delta

Accepts one of the following:

:signature\_delta

index: Integer

type: :content\_block\_delta

Accepts one of the following:

:content\_block\_delta

class BetaRawContentBlockStartEvent { content\_block, index, type }

content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 11 more

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

index: Integer

type: :content\_block\_start

Accepts one of the following:

:content\_block\_start

class BetaRawContentBlockStopEvent { index, type }

index: Integer

type: :content\_block\_stop

Accepts one of the following:

:content\_block\_stop

class BetaRawMessageDeltaEvent { context\_management, delta, type, usage }

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

delta: { container, stop\_reason, stop\_sequence}

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

stop\_reason: [BetaStopReason](api/beta.md)

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

type: :message\_delta

Accepts one of the following:

:message\_delta

usage: [BetaMessageDeltaUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The cumulative number of input tokens which were used.

minimum0

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

class BetaRawMessageStartEvent { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

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

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :message\_start

Accepts one of the following:

:message\_start

class BetaRawMessageStopEvent { type }

type: :message\_stop

Accepts one of the following:

:message\_stop

BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](api/beta.md) { message, type }  | [BetaRawMessageDeltaEvent](api/beta.md) { context\_management, delta, type, usage }  | [BetaRawMessageStopEvent](api/beta.md) { type }  | 3 more

Accepts one of the following:

class BetaRawMessageStartEvent { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

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

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :message\_start

Accepts one of the following:

:message\_start

class BetaRawMessageDeltaEvent { context\_management, delta, type, usage }

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

delta: { container, stop\_reason, stop\_sequence}

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

stop\_reason: [BetaStopReason](api/beta.md)

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

type: :message\_delta

Accepts one of the following:

:message\_delta

usage: [BetaMessageDeltaUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 2 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The cumulative number of input tokens which were used.

minimum0

output\_tokens: Integer

The cumulative number of output tokens which were used.

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

class BetaRawMessageStopEvent { type }

type: :message\_stop

Accepts one of the following:

:message\_stop

class BetaRawContentBlockStartEvent { content\_block, index, type }

content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 11 more

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

index: Integer

type: :content\_block\_start

Accepts one of the following:

:content\_block\_start

class BetaRawContentBlockDeltaEvent { delta, index, type }

delta: [BetaRawContentBlockDelta](api/beta.md)

Accepts one of the following:

class BetaTextDelta { text, type }

text: String

type: :text\_delta

Accepts one of the following:

:text\_delta

class BetaInputJSONDelta { partial\_json, type }

partial\_json: String

type: :input\_json\_delta

Accepts one of the following:

:input\_json\_delta

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

type: :citations\_delta

Accepts one of the following:

:citations\_delta

class BetaThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

Accepts one of the following:

:thinking\_delta

class BetaSignatureDelta { signature, type }

signature: String

type: :signature\_delta

Accepts one of the following:

:signature\_delta

index: Integer

type: :content\_block\_delta

Accepts one of the following:

:content\_block\_delta

class BetaRawContentBlockStopEvent { index, type }

index: Integer

type: :content\_block\_stop

Accepts one of the following:

:content\_block\_stop

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaRedactedThinkingBlockParam { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaRequestDocumentBlock { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:url

url: String

authorization\_token: String

tool\_configuration: [BetaRequestMCPServerToolConfiguration](api/beta.md) { allowed\_tools, enabled }

allowed\_tools: Array[String]

enabled: bool

class BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

is\_error: bool

class BetaSearchResultBlockParam { content, source, title, 3 more }

content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUsage { web\_fetch\_requests, web\_search\_requests }

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

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

Accepts one of the following:

:server\_tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaSignatureDelta { signature, type }

signature: String

type: :signature\_delta

Accepts one of the following:

:signature\_delta

class BetaSkill { skill\_id, type, version }

A skill that was loaded in a container (response model).

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

class BetaSkillParams { skill\_id, type, version }

Specification for a skill to be loaded in a container (request model).

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

BetaStopReason = :end\_turn | :max\_tokens | :stop\_sequence | 4 more

Accepts one of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

BetaTextCitationParam = [BetaCitationCharLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | [BetaCitationPageLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | [BetaCitationContentBlockLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | 2 more

Accepts one of the following:

class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

class BetaTextDelta { text, type }

text: String

type: :text\_delta

Accepts one of the following:

:text\_delta

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

error\_message: String

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more }

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more }

content: String

file\_type: :text | :image | :pdf

Accepts one of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaThinkingBlockParam { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaThinkingConfigDisabled { type }

type: :disabled

Accepts one of the following:

:disabled

class BetaThinkingConfigEnabled { budget\_tokens, type }

budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

Accepts one of the following:

:enabled

BetaThinkingConfigParam = [BetaThinkingConfigEnabled](api/beta.md) { budget\_tokens, type }  | [BetaThinkingConfigDisabled](api/beta.md) { type }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

Accepts one of the following:

class BetaThinkingConfigEnabled { budget\_tokens, type }

budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled

Accepts one of the following:

:enabled

class BetaThinkingConfigDisabled { type }

type: :disabled

Accepts one of the following:

:disabled

class BetaThinkingDelta { thinking, type }

thinking: String

type: :thinking\_delta

Accepts one of the following:

:thinking\_delta

class BetaThinkingTurns { type, value }

type: :thinking\_turns

Accepts one of the following:

:thinking\_turns

value: Integer

class BetaTool { input\_schema, name, allowed\_callers, 6 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

Accepts one of the following:

:object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

type: :custom

Accepts one of the following:

:custom

class BetaToolBash20241022 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20241022

Accepts one of the following:

:bash\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolBash20250124 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20250124

Accepts one of the following:

:bash\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

BetaToolChoice = [BetaToolChoiceAuto](api/beta.md) { type, disable\_parallel\_tool\_use }  | [BetaToolChoiceAny](api/beta.md) { type, disable\_parallel\_tool\_use }  | [BetaToolChoiceTool](api/beta.md) { name, type, disable\_parallel\_tool\_use }  | [BetaToolChoiceNone](api/beta.md) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

Accepts one of the following:

class BetaToolChoiceAuto { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: :auto

Accepts one of the following:

:auto

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceAny { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: :any

Accepts one of the following:

:any

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceTool { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

Accepts one of the following:

:tool

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

Accepts one of the following:

:none

class BetaToolChoiceAny { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: :any

Accepts one of the following:

:any

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolChoiceAuto { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: :auto

Accepts one of the following:

:auto

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

class BetaToolChoiceNone { type }

The model will not be allowed to use tools.

type: :none

Accepts one of the following:

:none

class BetaToolChoiceTool { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool

Accepts one of the following:

:tool

disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

class BetaToolComputerUse20241022 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20241022

Accepts one of the following:

:computer\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum0

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaToolComputerUse20250124 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20250124

Accepts one of the following:

:computer\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum0

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaToolComputerUse20251124 { display\_height\_px, display\_width\_px, name, 8 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20251124

Accepts one of the following:

:computer\_20251124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum0

enable\_zoom: bool

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaToolReferenceBlock { tool\_name, type }

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

class BetaToolReferenceBlockParam { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

source: String

title: String

type: :search\_result

Accepts one of the following:

:search\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_bm25

type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

Accepts one of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:tool\_search\_tool\_regex

type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

Accepts one of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolResultErrorParam { error\_code, type }

error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

class BetaToolSearchToolSearchResultBlockParam { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_search\_tool\_search\_result

class BetaToolTextEditor20241022 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20241022

Accepts one of the following:

:text\_editor\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolTextEditor20250124 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20250124

Accepts one of the following:

:text\_editor\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolTextEditor20250429 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250429

Accepts one of the following:

:text\_editor\_20250429

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolTextEditor20250728 { name, type, allowed\_callers, 5 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250728

Accepts one of the following:

:text\_editor\_20250728

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum1

strict: bool

BetaToolUnion = [BetaTool](api/beta.md) { input\_schema, name, allowed\_callers, 6 more }  | [BetaToolBash20241022](api/beta.md) { name, type, allowed\_callers, 4 more }  | [BetaToolBash20250124](api/beta.md) { name, type, allowed\_callers, 4 more }  | 15 more

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

Accepts one of the following:

class BetaTool { input\_schema, name, allowed\_callers, 6 more }

input\_schema: { type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

Accepts one of the following:

:object

properties: Hash[Symbol, untyped]

required: Array[String]

name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

type: :custom

Accepts one of the following:

:custom

class BetaToolBash20241022 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20241022

Accepts one of the following:

:bash\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolBash20250124 { name, type, allowed\_callers, 4 more }

name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:bash

type: :bash\_20250124

Accepts one of the following:

:bash\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaCodeExecutionTool20250522 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:code\_execution

type: :code\_execution\_20250522

Accepts one of the following:

:code\_execution\_20250522

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaCodeExecutionTool20250825 { name, type, allowed\_callers, 3 more }

name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:code\_execution

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolComputerUse20241022 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20241022

Accepts one of the following:

:computer\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum0

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaMemoryTool20250818 { name, type, allowed\_callers, 4 more }

name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:memory

type: :memory\_20250818

Accepts one of the following:

:memory\_20250818

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolComputerUse20250124 { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20250124

Accepts one of the following:

:computer\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum0

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaToolTextEditor20241022 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20241022

Accepts one of the following:

:text\_editor\_20241022

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolComputerUse20251124 { display\_height\_px, display\_width\_px, name, 8 more }

display\_height\_px: Integer

The height of the display in pixels.

minimum1

display\_width\_px: Integer

The width of the display in pixels.

minimum1

name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:computer

type: :computer\_20251124

Accepts one of the following:

:computer\_20251124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum0

enable\_zoom: bool

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

class BetaToolTextEditor20250124 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_editor

type: :text\_editor\_20250124

Accepts one of the following:

:text\_editor\_20250124

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolTextEditor20250429 { name, type, allowed\_callers, 4 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250429

Accepts one of the following:

:text\_editor\_20250429

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolTextEditor20250728 { name, type, allowed\_callers, 5 more }

name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:str\_replace\_based\_edit\_tool

type: :text\_editor\_20250728

Accepts one of the following:

:text\_editor\_20250728

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

minimum1

strict: bool

class BetaWebSearchTool20250305 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_search

type: :web\_search\_20250305

Accepts one of the following:

:web\_search\_20250305

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

exclusiveMinimum0

strict: bool

user\_location: { type, city, country, 2 more}

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

Accepts one of the following:

:approximate

city: String

The city of the user.

maxLength255

minLength1

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: String

The region of the user.

maxLength255

minLength1

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebFetchTool20250910 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_fetch

type: :web\_fetch\_20250910

Accepts one of the following:

:web\_fetch\_20250910

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

exclusiveMinimum0

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: bool

class BetaToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:tool\_search\_tool\_bm25

type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

Accepts one of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more }

name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:tool\_search\_tool\_regex

type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

Accepts one of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

class BetaMCPToolset { mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: String

Name of the MCP server to configure tools for

maxLength255

minLength1

type: :mcp\_toolset

Accepts one of the following:

:mcp\_toolset

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaToolUseBlockParam { id, input, name, 3 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaToolUsesKeep { type, value }

type: :tool\_uses

Accepts one of the following:

:tool\_uses

value: Integer

class BetaToolUsesTrigger { type, value }

type: :tool\_uses

Accepts one of the following:

:tool\_uses

value: Integer

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

class BetaWebFetchTool20250910 { name, type, allowed\_callers, 8 more }

name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_fetch

type: :web\_fetch\_20250910

Accepts one of the following:

:web\_fetch\_20250910

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

exclusiveMinimum0

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

exclusiveMinimum0

strict: bool

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

class BetaWebFetchBlockParam { content, type, url, retrieved\_at }

content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

Accepts one of the following:

class BetaBase64PDFSource { data, media\_type, type }

data: String

media\_type: :"application/pdf"

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

class BetaContentBlockSource { content, type }

content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

String

Array[[BetaContentBlockSourceContent](api/beta.md)]

Accepts one of the following:

class BetaTextBlockParam { text, type, cache\_control, citations }

text: String

type: :text

Accepts one of the following:

:text

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

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

Accepts one of the following:

:base64

class BetaURLImageSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileImageSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :image

Accepts one of the following:

:image

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:content

class BetaURLPDFSource { type, url }

type: :url

Accepts one of the following:

:url

url: String

class BetaFileDocumentSource { file\_id, type }

file\_id: String

type: :file

Accepts one of the following:

:file

type: :document

Accepts one of the following:

:document

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:web\_search\_result

url: String

class BetaWebSearchResultBlockParam { encrypted\_content, title, type, 2 more }

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

page\_age: String

class BetaWebSearchTool20250305 { name, type, allowed\_callers, 7 more }

name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

Accepts one of the following:

:web\_search

type: :web\_search\_20250305

Accepts one of the following:

:web\_search\_20250305

allowed\_callers: Array[:direct | :code\_execution\_20250825]

Accepts one of the following:

:direct

:code\_execution\_20250825

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

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

exclusiveMinimum0

strict: bool

user\_location: { type, city, country, 2 more}

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

Accepts one of the following:

:approximate

city: String

The city of the user.

maxLength255

minLength1

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

maxLength2

minLength2

region: String

The region of the user.

maxLength255

minLength1

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

maxLength255

minLength1

class BetaWebSearchToolRequestError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control }

content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl }

Create a cache control breakpoint at this content block.

type: :ephemeral

Accepts one of the following:

:ephemeral

ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

Accepts one of the following:

:"5m"

:"1h"

BetaWebSearchToolResultBlockParamContent = Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ] | [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type }

Accepts one of the following:

Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

class BetaWebSearchToolResultError { error\_code, type }

error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

BetaWebSearchToolResultErrorCode = :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 2 more

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

beta.messages.batches.create(\*\*kwargs) -> [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

post/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

beta.messages.batches.retrieve(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

get/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

beta.messages.batches.list(\*\*kwargs) -> Page<[BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more } >

get/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

beta.messages.batches.cancel(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatch](api/beta.md) { id, archived\_at, cancel\_initiated\_at, 7 more }

post/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

beta.messages.batches.delete(message\_batch\_id, \*\*kwargs) -> [BetaDeletedMessageBatch](api/beta.md) { id, type }

delete/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

beta.messages.batches.results(message\_batch\_id, \*\*kwargs) -> [BetaMessageBatchIndividualResponse](api/beta.md) { custom\_id, result }

get/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

class BetaDeletedMessageBatch { id, type }

id: String

ID of the Message Batch.

type: :message\_batch\_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Accepts one of the following:

:message\_batch\_deleted

class BetaMessageBatch { id, archived\_at, cancel\_initiated\_at, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

formatdate-time

cancel\_initiated\_at: Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

formatdate-time

created\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was created.

formatdate-time

ended\_at: Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

formatdate-time

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

Accepts one of the following:

:message\_batch

class BetaMessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

request\_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class BetaMessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

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

message: [BetaMessage](api/beta.md) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

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

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

request\_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class BetaMessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class BetaMessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

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

message: [BetaMessage](api/beta.md) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

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

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded

class BetaMessageBatchErroredResult { error, type }

error: [BetaErrorResponse](api/beta.md) { error, request\_id, type }

error: [BetaError](api/beta.md)

Accepts one of the following:

class BetaInvalidRequestError { message, type }

message: String

type: :invalid\_request\_error

Accepts one of the following:

:invalid\_request\_error

class BetaAuthenticationError { message, type }

message: String

type: :authentication\_error

Accepts one of the following:

:authentication\_error

class BetaBillingError { message, type }

message: String

type: :billing\_error

Accepts one of the following:

:billing\_error

class BetaPermissionError { message, type }

message: String

type: :permission\_error

Accepts one of the following:

:permission\_error

class BetaNotFoundError { message, type }

message: String

type: :not\_found\_error

Accepts one of the following:

:not\_found\_error

class BetaRateLimitError { message, type }

message: String

type: :rate\_limit\_error

Accepts one of the following:

:rate\_limit\_error

class BetaGatewayTimeoutError { message, type }

message: String

type: :timeout\_error

Accepts one of the following:

:timeout\_error

class BetaAPIError { message, type }

message: String

type: :api\_error

Accepts one of the following:

:api\_error

class BetaOverloadedError { message, type }

message: String

type: :overloaded\_error

Accepts one of the following:

:overloaded\_error

request\_id: String

type: :error

Accepts one of the following:

:error

type: :errored

Accepts one of the following:

:errored

class BetaMessageBatchCanceledResult { type }

type: :canceled

Accepts one of the following:

:canceled

class BetaMessageBatchExpiredResult { type }

type: :expired

Accepts one of the following:

:expired

class BetaMessageBatchSucceededResult { message, type }

message: [BetaMessage](api/beta.md) { id, container, content, 7 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

container: [BetaContainer](api/beta.md) { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.

formatdate-time

skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID

maxLength64

minLength1

type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

Accepts one of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version

maxLength64

minLength1

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

class BetaThinkingBlock { signature, thinking, type }

signature: String

thinking: String

type: :thinking

Accepts one of the following:

:thinking

class BetaRedactedThinkingBlock { data, type }

data: String

type: :redacted\_thinking

Accepts one of the following:

:redacted\_thinking

class BetaToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use

Accepts one of the following:

:tool\_use

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

class BetaServerToolUseBlock { id, caller\_, input, 2 more }

id: String

caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

Accepts one of the following:

class BetaDirectCaller { type }

Tool invocation directly from the model.

type: :direct

Accepts one of the following:

:direct

class BetaServerToolCaller { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825

Accepts one of the following:

:code\_execution\_20250825

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

Accepts one of the following:

:server\_tool\_use

class BetaWebSearchToolResultBlock { content, tool\_use\_id, type }

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

type: :web\_search\_tool\_result\_error

Accepts one of the following:

:web\_search\_tool\_result\_error

Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

Accepts one of the following:

:web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result

Accepts one of the following:

:web\_search\_tool\_result

class BetaWebFetchToolResultBlock { content, tool\_use\_id, type }

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

Accepts one of the following:

:web\_fetch\_tool\_result\_error

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

Accepts one of the following:

:"application/pdf"

type: :base64

Accepts one of the following:

:base64

class BetaPlainTextSource { data, media\_type, type }

data: String

media\_type: :"text/plain"

Accepts one of the following:

:"text/plain"

type: :text

Accepts one of the following:

:text

title: String

The title of the document

type: :document

Accepts one of the following:

:document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

Accepts one of the following:

:web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result

Accepts one of the following:

:web\_fetch\_tool\_result

class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Accepts one of the following:

class BetaCodeExecutionToolResultError { error\_code, type }

error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

Accepts one of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error

Accepts one of the following:

:code\_execution\_tool\_result\_error

class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

Accepts one of the following:

:code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result

Accepts one of the following:

:code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result

Accepts one of the following:

:code\_execution\_tool\_result

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

Accepts one of the following:

:bash\_code\_execution\_tool\_result\_error

class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more }

content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

Accepts one of the following:

:bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

Accepts one of the following:

:bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result

Accepts one of the following:

:bash\_code\_execution\_tool\_result

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

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result\_error

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

Accepts one of the following:

:text\_editor\_code\_execution\_view\_result

class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type }

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result

Accepts one of the following:

:text\_editor\_code\_execution\_create\_result

class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more }

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

Accepts one of the following:

:text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result

Accepts one of the following:

:text\_editor\_code\_execution\_tool\_result

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

Accepts one of the following:

:tool\_search\_tool\_result\_error

class BetaToolSearchToolSearchResultBlock { tool\_references, type }

tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

Accepts one of the following:

:tool\_reference

type: :tool\_search\_tool\_search\_result

Accepts one of the following:

:tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result

Accepts one of the following:

:tool\_search\_tool\_result

class BetaMCPToolUseBlock { id, input, name, 2 more }

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use

Accepts one of the following:

:mcp\_tool\_use

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

Accepts one of the following:

:char\_location

class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location

Accepts one of the following:

:page\_location

class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more }

cited\_text: String

document\_index: Integer

document\_title: String

end\_block\_index: Integer

file\_id: String

start\_block\_index: Integer

type: :content\_block\_location

Accepts one of the following:

:content\_block\_location

class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more }

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

Accepts one of the following:

:web\_search\_result\_location

url: String

class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: String

end\_block\_index: Integer

search\_result\_index: Integer

source: String

start\_block\_index: Integer

title: String

type: :search\_result\_location

Accepts one of the following:

:search\_result\_location

text: String

type: :text

Accepts one of the following:

:text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result

Accepts one of the following:

:mcp\_tool\_result

class BetaContainerUploadBlock { file\_id, type }

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload

Accepts one of the following:

:container\_upload

context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

Accepts one of the following:

class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

minimum0

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.

Accepts one of the following:

:clear\_tool\_uses\_20250919

class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

minimum0

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

minimum0

type: :clear\_thinking\_20251015

The type of context management edit applied.

Accepts one of the following:

:clear\_thinking\_20251015

model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101" | :"claude-opus-4-5" | :"claude-3-7-sonnet-latest" | 17 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

Accepts one of the following:

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-3-7-sonnet-latest"

High-performance model with early extended thinking

:"claude-3-7-sonnet-20250219"

High-performance model with early extended thinking

:"claude-3-5-haiku-latest"

Fastest and most compact model for near-instant responsiveness

:"claude-3-5-haiku-20241022"

Our fastest model

:"claude-haiku-4-5"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-haiku-4-5-20251001"

Hybrid model, capable of near-instant responses and extended thinking

:"claude-sonnet-4-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-0"

High-performance model with extended thinking

:"claude-4-sonnet-20250514"

High-performance model with extended thinking

:"claude-sonnet-4-5"

Our best model for real-world agents and coding

:"claude-sonnet-4-5-20250929"

Our best model for real-world agents and coding

:"claude-opus-4-0"

Our most capable model

:"claude-opus-4-20250514"

Our most capable model

:"claude-4-opus-20250514"

Our most capable model

:"claude-opus-4-1-20250805"

Our most capable model

:"claude-3-opus-latest"

Excels at writing and complex tasks

:"claude-3-opus-20240229"

Excels at writing and complex tasks

:"claude-3-haiku-20240307"

Our previous most fast and cost-effective

String

role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.

Accepts one of the following:

:assistant

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

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: :message

Object type.

For Messages, this is always `"message"`.

Accepts one of the following:

:message

usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

minimum0

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

minimum0

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

minimum0

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

minimum0

input\_tokens: Integer

The number of input tokens which were used.

minimum0

output\_tokens: Integer

The number of output tokens which were used.

minimum0

server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

minimum0

web\_search\_requests: Integer

The number of web search tool requests.

minimum0

service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

Accepts one of the following:

:standard

:priority

:batch

type: :succeeded

Accepts one of the following:

:succeeded

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

beta.files.upload(\*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 4 more }

post/v1/files

##### [List Files](api/beta/files/list.md)

beta.files.list(\*\*kwargs) -> Page<[FileMetadata](api/beta.md) { id, created\_at, filename, 4 more } >

get/v1/files

##### [Download File](api/beta/files/download.md)

beta.files.download(file\_id, \*\*kwargs) -> StringIO

get/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

beta.files.retrieve\_metadata(file\_id, \*\*kwargs) -> [FileMetadata](api/beta.md) { id, created\_at, filename, 4 more }

get/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

beta.files.delete(file\_id, \*\*kwargs) -> [DeletedFile](api/beta.md) { id, type }

delete/v1/files/{file\_id}

##### ModelsExpand Collapse

class DeletedFile { id, type }

id: String

ID of the deleted file.

type: :file\_deleted

Deleted object type.

For file deletion, this is always `"file_deleted"`.

Accepts one of the following:

:file\_deleted

class FileMetadata { id, created\_at, filename, 4 more }

id: String

Unique object identifier.

The format and length of IDs may change over time.

created\_at: Time

RFC 3339 datetime string representing when the file was created.

formatdate-time

filename: String

Original filename of the uploaded file.

maxLength500

minLength1

mime\_type: String

MIME type of the file.

maxLength255

minLength1

size\_bytes: Integer

Size of the file in bytes.

minimum0

type: :file

Object type.

For files, this is always `"file"`.

Accepts one of the following:

:file

downloadable: bool

Whether the file can be downloaded.

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

beta.skills.create(\*\*kwargs) -> [SkillCreateResponse](api/beta.md) { id, created\_at, display\_title, 4 more }

post/v1/skills

##### [List Skills](api/beta/skills/list.md)

beta.skills.list(\*\*kwargs) -> PageCursor<[SkillListResponse](api/beta.md) { id, created\_at, display\_title, 4 more } >

get/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

beta.skills.retrieve(skill\_id, \*\*kwargs) -> [SkillRetrieveResponse](api/beta.md) { id, created\_at, display\_title, 4 more }

get/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

beta.skills.delete(skill\_id, \*\*kwargs) -> [SkillDeleteResponse](api/beta.md) { id, type }

delete/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

beta.skills.versions.create(skill\_id, \*\*kwargs) -> [VersionCreateResponse](api/beta.md) { id, created\_at, description, 5 more }

post/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

beta.skills.versions.list(skill\_id, \*\*kwargs) -> PageCursor<[VersionListResponse](api/beta.md) { id, created\_at, description, 5 more } >

get/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

beta.skills.versions.retrieve(version, \*\*kwargs) -> [VersionRetrieveResponse](api/beta.md) { id, created\_at, description, 5 more }

get/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

beta.skills.versions.delete(version, \*\*kwargs) -> [VersionDeleteResponse](api/beta.md) { id, type }

delete/v1/skills/{skill\_id}/versions/{version}