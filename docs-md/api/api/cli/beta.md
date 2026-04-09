# Beta

Copy page

CLI

# Beta

##### ModelsExpand Collapse

beta\_api\_error: object { message, type }

message: string

type: "api\_error"

beta\_authentication\_error: object { message, type }

message: string

type: "authentication\_error"

beta\_billing\_error: object { message, type }

message: string

type: "billing\_error"

beta\_error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more

beta\_invalid\_request\_error: object { message, type }

message: string

type: "invalid\_request\_error"

beta\_authentication\_error: object { message, type }

message: string

type: "authentication\_error"

beta\_billing\_error: object { message, type }

message: string

type: "billing\_error"

beta\_permission\_error: object { message, type }

message: string

type: "permission\_error"

beta\_not\_found\_error: object { message, type }

message: string

type: "not\_found\_error"

beta\_rate\_limit\_error: object { message, type }

message: string

type: "rate\_limit\_error"

beta\_gateway\_timeout\_error: object { message, type }

message: string

type: "timeout\_error"

beta\_api\_error: object { message, type }

message: string

type: "api\_error"

beta\_overloaded\_error: object { message, type }

message: string

type: "overloaded\_error"

beta\_error\_response: object { error, request\_id, type }

error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more

beta\_invalid\_request\_error: object { message, type }

message: string

type: "invalid\_request\_error"

beta\_authentication\_error: object { message, type }

message: string

type: "authentication\_error"

beta\_billing\_error: object { message, type }

message: string

type: "billing\_error"

beta\_permission\_error: object { message, type }

message: string

type: "permission\_error"

beta\_not\_found\_error: object { message, type }

message: string

type: "not\_found\_error"

beta\_rate\_limit\_error: object { message, type }

message: string

type: "rate\_limit\_error"

beta\_gateway\_timeout\_error: object { message, type }

message: string

type: "timeout\_error"

beta\_api\_error: object { message, type }

message: string

type: "api\_error"

beta\_overloaded\_error: object { message, type }

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

beta\_gateway\_timeout\_error: object { message, type }

message: string

type: "timeout\_error"

beta\_invalid\_request\_error: object { message, type }

message: string

type: "invalid\_request\_error"

beta\_not\_found\_error: object { message, type }

message: string

type: "not\_found\_error"

beta\_overloaded\_error: object { message, type }

message: string

type: "overloaded\_error"

beta\_permission\_error: object { message, type }

message: string

type: "permission\_error"

beta\_rate\_limit\_error: object { message, type }

message: string

type: "rate\_limit\_error"

#### BetaModels

##### [List Models](api/beta/models/list.md)

$ ant beta:models list

GET/v1/models

##### [Get a Model](api/beta/models/retrieve.md)

$ ant beta:models retrieve

GET/v1/models/{model\_id}

##### ModelsExpand Collapse

beta\_capability\_support: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

beta\_context\_management\_capability: object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management capability details.

clear\_thinking\_20251015: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

beta\_effort\_capability: object { high, low, max, 2 more }

Effort (reasoning\_effort) capability details.

high: object { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: object { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: object { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: object { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

beta\_model\_capabilities: object { batch, citations, code\_execution, 6 more }

Model capability information.

batch: object { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: object { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code\_execution: object { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context\_management: object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management support and available strategies.

clear\_thinking\_20251015: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: object { high, low, max, 2 more }

Effort (reasoning\_effort) support and available levels.

high: object { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: object { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: object { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: object { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

image\_input: object { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf\_input: object { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured\_outputs: object { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: object { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: object { adaptive, enabled }

Supported thinking type configurations.

adaptive: object { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: object { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

beta\_model\_info: object { id, capabilities, created\_at, 4 more }

id: string

Unique model identifier.

capabilities: object { batch, citations, code\_execution, 6 more }

Model capability information.

batch: object { supported }

Whether the model supports the Batch API.

supported: boolean

Whether this capability is supported by the model.

citations: object { supported }

Whether the model supports citation generation.

supported: boolean

Whether this capability is supported by the model.

code\_execution: object { supported }

Whether the model supports code execution tools.

supported: boolean

Whether this capability is supported by the model.

context\_management: object { clear\_thinking\_20251015, clear\_tool\_uses\_20250919, compact\_20260112, supported }

Context management support and available strategies.

clear\_thinking\_20251015: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

clear\_tool\_uses\_20250919: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

compact\_20260112: object { supported }

Indicates whether a capability is supported.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

effort: object { high, low, max, 2 more }

Effort (reasoning\_effort) support and available levels.

high: object { supported }

Whether the model supports high effort level.

supported: boolean

Whether this capability is supported by the model.

low: object { supported }

Whether the model supports low effort level.

supported: boolean

Whether this capability is supported by the model.

max: object { supported }

Whether the model supports max effort level.

supported: boolean

Whether this capability is supported by the model.

medium: object { supported }

Whether the model supports medium effort level.

supported: boolean

Whether this capability is supported by the model.

supported: boolean

Whether this capability is supported by the model.

image\_input: object { supported }

Whether the model accepts image content blocks.

supported: boolean

Whether this capability is supported by the model.

pdf\_input: object { supported }

Whether the model accepts PDF content blocks.

supported: boolean

Whether this capability is supported by the model.

structured\_outputs: object { supported }

Whether the model supports structured output / JSON mode / strict tool schemas.

supported: boolean

Whether this capability is supported by the model.

thinking: object { supported, types }

Thinking capability and supported type configurations.

supported: boolean

Whether this capability is supported by the model.

types: object { adaptive, enabled }

Supported thinking type configurations.

adaptive: object { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: object { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

created\_at: string

RFC 3339 datetime string representing the time at which the model was released. May be set to an epoch value if the release date is unknown.

display\_name: string

A human-readable name for the model.

max\_input\_tokens: number

Maximum input context window size in tokens for this model.

max\_tokens: number

Maximum value for the `max_tokens` parameter when using this model.

type: "model"

Object type.

For Models, this is always `"model"`.

beta\_thinking\_capability: object { supported, types }

Thinking capability details.

supported: boolean

Whether this capability is supported by the model.

types: object { adaptive, enabled }

Supported thinking type configurations.

adaptive: object { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: object { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

beta\_thinking\_types: object { adaptive, enabled }

Supported thinking type configurations.

adaptive: object { supported }

Whether the model supports thinking with type 'adaptive' (auto).

supported: boolean

Whether this capability is supported by the model.

enabled: object { supported }

Whether the model supports thinking with type 'enabled'.

supported: boolean

Whether this capability is supported by the model.

#### BetaMessages

##### [Create a Message](api/beta/messages/create.md)

$ ant beta:messages create

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

$ ant beta:messages count-tokens

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse

beta\_all\_thinking\_turns: object { type }

type: "all"

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_bash\_code\_execution\_output\_block: object { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

beta\_bash\_code\_execution\_output\_block\_param: object { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

beta\_bash\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_cache\_control\_ephemeral: object { type, ttl }

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_config: object { enabled }

enabled: boolean

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citations\_config\_param: object { enabled }

enabled: optional boolean

beta\_citations\_delta: object { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_clear\_thinking\_20251015\_edit: object { type, keep }

type: "clear\_thinking\_20251015"

keep: optional [BetaThinkingTurns](api/beta.md) { type, value }  or [BetaAllThinkingTurns](api/beta.md) { type }  or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

beta\_thinking\_turns: object { type, value }

type: "thinking\_turns"

value: number

beta\_all\_thinking\_turns: object { type }

type: "all"

union\_member\_2: "all"

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

beta\_clear\_tool\_uses\_20250919\_edit: object { type, clear\_at\_least, clear\_tool\_inputs, 3 more }

type: "clear\_tool\_uses\_20250919"

clear\_at\_least: optional object { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number

clear\_tool\_inputs: optional boolean or array of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

union\_member\_0: boolean

union\_member\_1: array of string

exclude\_tools: optional array of string

Tool names whose uses are preserved from clearing

keep: optional object { type, value }

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number

trigger: optional [BetaInputTokensTrigger](api/beta.md) { type, value }  or [BetaToolUsesTrigger](api/beta.md) { type, value }

Condition that triggers the context management strategy

beta\_input\_tokens\_trigger: object { type, value }

type: "input\_tokens"

value: number

beta\_tool\_uses\_trigger: object { type, value }

type: "tool\_uses"

value: number

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_code\_execution\_output\_block: object { file\_id, type }

file\_id: string

type: "code\_execution\_output"

beta\_code\_execution\_output\_block\_param: object { file\_id, type }

file\_id: string

type: "code\_execution\_output"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_code\_execution\_tool\_20250522: object { name, type, allowed\_callers, 3 more }

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_code\_execution\_tool\_20250825: object { name, type, allowed\_callers, 3 more }

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_code\_execution\_tool\_20260120: object { name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_code\_execution\_tool\_result\_block\_content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

beta\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_code\_execution\_tool\_result\_block\_param\_content: [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_tool\_result\_error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_compact\_20260112\_edit: object { type, instructions, pause\_after\_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.

trigger: optional object { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

beta\_compaction\_block\_param: object { content, type, cache\_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_compaction\_content\_block\_delta: object { content, type }

content: string

type: "compaction\_delta"

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

beta\_container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

beta\_container\_params: object { id, skills }

Container parameters with skills to be loaded.

id: optional string

Container id

skills: optional array of [BetaSkillParams](api/beta.md) { skill\_id, type, version }

List of skills to load in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_container\_upload\_block\_param: object { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  or [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  or [BetaRedactedThinkingBlock](api/beta.md) { data, type }  or 12 more

Response model for a file uploaded to the container.

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

beta\_content\_block\_param: [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  or [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }  or 16 more

Regular text content.

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_request\_document\_block: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

beta\_search\_result\_block\_param: object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

beta\_thinking\_block\_param: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block\_param: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: string

type: "tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  or [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  or 2 more

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_search\_result\_block\_param: object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

beta\_request\_document\_block: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

beta\_tool\_reference\_block\_param: object { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

is\_error: optional boolean

beta\_server\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more }

content: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }  or [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type }

Result Block: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

beta\_web\_search\_tool\_request\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  or [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at }

beta\_web\_fetch\_tool\_result\_error\_block\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block\_param: object { content, type, url, retrieved\_at }

content: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_bash\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_text\_editor\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error\_param: object { error\_code, type, error\_message }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

beta\_text\_editor\_code\_execution\_view\_result\_block\_param: object { content, file\_type, type, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

beta\_text\_editor\_code\_execution\_create\_result\_block\_param: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block\_param: object { type, lines, new\_lines, 3 more }

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_tool\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block\_param: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_mcp\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_request\_mcp\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: string

type: "mcp\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_param\_content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

is\_error: optional boolean

beta\_container\_upload\_block\_param: object { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_compaction\_block\_param: object { content, type, cache\_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_content\_block\_source\_content: [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_context\_management\_config: object { edits }

edits: optional array of [BetaClearToolUses20250919Edit](api/beta.md) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  or [BetaClearThinking20251015Edit](api/beta.md) { type, keep }  or [BetaCompact20260112Edit](api/beta.md) { type, instructions, pause\_after\_compaction, trigger }

List of context management edits to apply

beta\_clear\_tool\_uses\_20250919\_edit: object { type, clear\_at\_least, clear\_tool\_inputs, 3 more }

type: "clear\_tool\_uses\_20250919"

clear\_at\_least: optional object { type, value }

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number

clear\_tool\_inputs: optional boolean or array of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

union\_member\_0: boolean

union\_member\_1: array of string

exclude\_tools: optional array of string

Tool names whose uses are preserved from clearing

keep: optional object { type, value }

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number

trigger: optional [BetaInputTokensTrigger](api/beta.md) { type, value }  or [BetaToolUsesTrigger](api/beta.md) { type, value }

Condition that triggers the context management strategy

beta\_input\_tokens\_trigger: object { type, value }

type: "input\_tokens"

value: number

beta\_tool\_uses\_trigger: object { type, value }

type: "tool\_uses"

value: number

beta\_clear\_thinking\_20251015\_edit: object { type, keep }

type: "clear\_thinking\_20251015"

keep: optional [BetaThinkingTurns](api/beta.md) { type, value }  or [BetaAllThinkingTurns](api/beta.md) { type }  or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

beta\_thinking\_turns: object { type, value }

type: "thinking\_turns"

value: number

beta\_all\_thinking\_turns: object { type }

type: "all"

union\_member\_2: "all"

beta\_compact\_20260112\_edit: object { type, instructions, pause\_after\_compaction, trigger }

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.

trigger: optional object { type, value }

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number

beta\_context\_management\_response: object { applied\_edits }

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

beta\_count\_tokens\_context\_management\_response: object { original\_input\_tokens }

original\_input\_tokens: number

The original token count before context management was applied

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_document\_block: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_input\_json\_delta: object { partial\_json, type }

partial\_json: string

type: "input\_json\_delta"

beta\_input\_tokens\_clear\_at\_least: object { type, value }

type: "input\_tokens"

value: number

beta\_input\_tokens\_trigger: object { type, value }

type: "input\_tokens"

value: number

beta\_iterations\_usage: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

beta\_json\_output\_format: object { schema, type }

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"

beta\_mcp\_tool\_config: object { defer\_loading, enabled }

Configuration for a specific tool in an MCP toolset.

defer\_loading: optional boolean

enabled: optional boolean

beta\_mcp\_tool\_default\_config: object { defer\_loading, enabled }

Default configuration for tools in an MCP toolset.

defer\_loading: optional boolean

enabled: optional boolean

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_mcp\_toolset: object { mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

configs: optional map[[BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: optional boolean

enabled: optional boolean

default\_config: optional object { defer\_loading, enabled }

Default configuration applied to all tools from this server

defer\_loading: optional boolean

enabled: optional boolean

beta\_memory\_tool\_20250818: object { name, type, allowed\_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_memory\_tool\_20250818\_command: [BetaMemoryTool20250818ViewCommand](api/beta.md) { command, path, view\_range }  or [BetaMemoryTool20250818CreateCommand](api/beta.md) { command, file\_text, path }  or [BetaMemoryTool20250818StrReplaceCommand](api/beta.md) { command, new\_str, old\_str, path }  or 3 more

beta\_memory\_tool\_20250818\_view\_command: object { command, path, view\_range }

command: "view"

Command type identifier

path: string

Path to directory or file to view

view\_range: optional array of number

Optional line range for viewing specific lines

beta\_memory\_tool\_20250818\_create\_command: object { command, file\_text, path }

command: "create"

Command type identifier

file\_text: string

Content to write to the file

path: string

Path where the file should be created

beta\_memory\_tool\_20250818\_str\_replace\_command: object { command, new\_str, old\_str, path }

command: "str\_replace"

Command type identifier

new\_str: string

Text to replace with

old\_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced

beta\_memory\_tool\_20250818\_insert\_command: object { command, insert\_line, insert\_text, path }

command: "insert"

Command type identifier

insert\_line: number

Line number where text should be inserted

insert\_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted

beta\_memory\_tool\_20250818\_delete\_command: object { command, path }

command: "delete"

Command type identifier

path: string

Path to the file or directory to delete

beta\_memory\_tool\_20250818\_rename\_command: object { command, new\_path, old\_path }

command: "rename"

Command type identifier

new\_path: string

New path for the file or directory

old\_path: string

Current path of the file or directory

beta\_memory\_tool\_20250818\_create\_command: object { command, file\_text, path }

command: "create"

Command type identifier

file\_text: string

Content to write to the file

path: string

Path where the file should be created

beta\_memory\_tool\_20250818\_delete\_command: object { command, path }

command: "delete"

Command type identifier

path: string

Path to the file or directory to delete

beta\_memory\_tool\_20250818\_insert\_command: object { command, insert\_line, insert\_text, path }

command: "insert"

Command type identifier

insert\_line: number

Line number where text should be inserted

insert\_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted

beta\_memory\_tool\_20250818\_rename\_command: object { command, new\_path, old\_path }

command: "rename"

Command type identifier

new\_path: string

New path for the file or directory

old\_path: string

Current path of the file or directory

beta\_memory\_tool\_20250818\_str\_replace\_command: object { command, new\_str, old\_str, path }

command: "str\_replace"

Command type identifier

new\_str: string

Text to replace with

old\_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced

beta\_memory\_tool\_20250818\_view\_command: object { command, path, view\_range }

command: "view"

Command type identifier

path: string

Path to directory or file to view

view\_range: optional array of number

Optional line range for viewing specific lines

beta\_message: object { id, container, content, 8 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](api/beta.md)

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

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: object { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

beta\_message\_delta\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_message\_param: object { content, role }

content: array of [BetaContentBlockParam](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_request\_document\_block: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

beta\_search\_result\_block\_param: object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

beta\_thinking\_block\_param: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block\_param: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: string

type: "tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  or [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  or 2 more

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_search\_result\_block\_param: object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

beta\_request\_document\_block: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

beta\_tool\_reference\_block\_param: object { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

is\_error: optional boolean

beta\_server\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more }

content: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }  or [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type }

Result Block: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

beta\_web\_search\_tool\_request\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  or [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at }

beta\_web\_fetch\_tool\_result\_error\_block\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block\_param: object { content, type, url, retrieved\_at }

content: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_bash\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_text\_editor\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error\_param: object { error\_code, type, error\_message }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

beta\_text\_editor\_code\_execution\_view\_result\_block\_param: object { content, file\_type, type, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

beta\_text\_editor\_code\_execution\_create\_result\_block\_param: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block\_param: object { type, lines, new\_lines, 3 more }

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_tool\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block\_param: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_mcp\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_request\_mcp\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: string

type: "mcp\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_param\_content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

is\_error: optional boolean

beta\_container\_upload\_block\_param: object { file\_id, type, cache\_control }

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_compaction\_block\_param: object { content, type, cache\_control }

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

content: string

Summary of previously compacted content, or null if compaction failed

type: "compaction"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

role: "user" or "assistant"

"user"

"assistant"

beta\_message\_tokens\_count: object { context\_management, input\_tokens }

context\_management: object { original\_input\_tokens }

Information about context management applied to the message.

original\_input\_tokens: number

The original token count before context management was applied

input\_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.

beta\_metadata: object { user\_id }

user\_id: optional string

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

beta\_output\_config: object { effort, format }

effort: optional "low" or "medium" or "high" or "max"

All possible effort levels.

"low"

"medium"

"high"

"max"

format: optional object { schema, type }

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_raw\_content\_block\_delta: [BetaTextDelta](api/beta.md) { text, type }  or [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  or [BetaCitationsDelta](api/beta.md) { citation, type }  or 3 more

beta\_text\_delta: object { text, type }

text: string

type: "text\_delta"

beta\_input\_json\_delta: object { partial\_json, type }

partial\_json: string

type: "input\_json\_delta"

beta\_citations\_delta: object { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

beta\_thinking\_delta: object { thinking, type }

thinking: string

type: "thinking\_delta"

beta\_signature\_delta: object { signature, type }

signature: string

type: "signature\_delta"

beta\_compaction\_content\_block\_delta: object { content, type }

content: string

type: "compaction\_delta"

beta\_raw\_content\_block\_delta\_event: object { delta, index, type }

delta: [BetaTextDelta](api/beta.md) { text, type }  or [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  or [BetaCitationsDelta](api/beta.md) { citation, type }  or 3 more

beta\_text\_delta: object { text, type }

text: string

type: "text\_delta"

beta\_input\_json\_delta: object { partial\_json, type }

partial\_json: string

type: "input\_json\_delta"

beta\_citations\_delta: object { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

beta\_thinking\_delta: object { thinking, type }

thinking: string

type: "thinking\_delta"

beta\_signature\_delta: object { signature, type }

signature: string

type: "signature\_delta"

beta\_compaction\_content\_block\_delta: object { content, type }

content: string

type: "compaction\_delta"

index: number

type: "content\_block\_delta"

beta\_raw\_content\_block\_start\_event: object { content\_block, index, type }

content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  or [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  or [BetaRedactedThinkingBlock](api/beta.md) { data, type }  or 12 more

Response model for a file uploaded to the container.

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

index: number

type: "content\_block\_start"

beta\_raw\_content\_block\_stop\_event: object { index, type }

index: number

type: "content\_block\_stop"

beta\_raw\_message\_delta\_event: object { context\_management, delta, type, usage }

context\_management: object { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

delta: object { container, stop\_details, stop\_reason, stop\_sequence }

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

type: "message\_delta"

usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

beta\_raw\_message\_start\_event: object { message, type }

message: object { id, container, content, 8 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](api/beta.md)

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

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: object { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "message\_start"

beta\_raw\_message\_stop\_event: object { type }

type: "message\_stop"

beta\_raw\_message\_stream\_event: [BetaRawMessageStartEvent](api/beta.md) { message, type }  or [BetaRawMessageDeltaEvent](api/beta.md) { context\_management, delta, type, usage }  or [BetaRawMessageStopEvent](api/beta.md) { type }  or 3 more

beta\_raw\_message\_start\_event: object { message, type }

message: object { id, container, content, 8 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](api/beta.md)

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

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: object { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "message\_start"

beta\_raw\_message\_delta\_event: object { context\_management, delta, type, usage }

context\_management: object { applied\_edits }

Information about context management strategies applied during the request

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

delta: object { container, stop\_details, stop\_reason, stop\_sequence }

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

type: "message\_delta"

usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 3 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The cumulative number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

beta\_raw\_message\_stop\_event: object { type }

type: "message\_stop"

beta\_raw\_content\_block\_start\_event: object { content\_block, index, type }

content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  or [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  or [BetaRedactedThinkingBlock](api/beta.md) { data, type }  or 12 more

Response model for a file uploaded to the container.

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

index: number

type: "content\_block\_start"

beta\_raw\_content\_block\_delta\_event: object { delta, index, type }

delta: [BetaTextDelta](api/beta.md) { text, type }  or [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  or [BetaCitationsDelta](api/beta.md) { citation, type }  or 3 more

beta\_text\_delta: object { text, type }

text: string

type: "text\_delta"

beta\_input\_json\_delta: object { partial\_json, type }

partial\_json: string

type: "input\_json\_delta"

beta\_citations\_delta: object { citation, type }

citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

type: "citations\_delta"

beta\_thinking\_delta: object { thinking, type }

thinking: string

type: "thinking\_delta"

beta\_signature\_delta: object { signature, type }

signature: string

type: "signature\_delta"

beta\_compaction\_content\_block\_delta: object { content, type }

content: string

type: "compaction\_delta"

index: number

type: "content\_block\_delta"

beta\_raw\_content\_block\_stop\_event: object { index, type }

index: number

type: "content\_block\_stop"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_redacted\_thinking\_block\_param: object { data, type }

data: string

type: "redacted\_thinking"

beta\_refusal\_stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

beta\_request\_document\_block: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

beta\_request\_mcp\_server\_tool\_configuration: object { allowed\_tools, enabled }

allowed\_tools: optional array of string

enabled: optional boolean

beta\_request\_mcp\_server\_url\_definition: object { name, type, url, 2 more }

name: string

type: "url"

url: string

authorization\_token: optional string

tool\_configuration: optional object { allowed\_tools, enabled }

allowed\_tools: optional array of string

enabled: optional boolean

beta\_request\_mcp\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: string

type: "mcp\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional string or array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_param\_content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

is\_error: optional boolean

beta\_search\_result\_block\_param: object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_usage: object { web\_fetch\_requests, web\_search\_requests }

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_signature\_delta: object { signature, type }

signature: string

type: "signature\_delta"

beta\_skill: object { skill\_id, type, version }

A skill that was loaded in a container (response model).

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

beta\_skill\_params: object { skill\_id, type, version }

Specification for a skill to be loaded in a container (request model).

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version

beta\_stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_text\_citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_text\_citation\_param: [BetaCitationCharLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  or [BetaCitationPageLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  or [BetaCitationContentBlockLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  or 2 more

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_text\_delta: object { text, type }

text: string

type: "text\_delta"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block\_param: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block\_param: object { type, lines, new\_lines, 3 more }

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error\_param: object { error\_code, type, error\_message }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

beta\_text\_editor\_code\_execution\_view\_result\_block\_param: object { content, file\_type, type, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

beta\_text\_editor\_code\_execution\_create\_result\_block\_param: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block\_param: object { type, lines, new\_lines, 3 more }

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_tool\_result\_error\_param: object { error\_code, type, error\_message }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_view\_result\_block\_param: object { content, file\_type, type, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_thinking\_block\_param: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_thinking\_config\_adaptive: object { type, display }

type: "adaptive"

display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"

beta\_thinking\_config\_disabled: object { type }

type: "disabled"

beta\_thinking\_config\_enabled: object { budget\_tokens, type, display }

budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

type: "enabled"

display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"

beta\_thinking\_config\_param: [BetaThinkingConfigEnabled](api/beta.md) { budget\_tokens, type, display }  or [BetaThinkingConfigDisabled](api/beta.md) { type }  or [BetaThinkingConfigAdaptive](api/beta.md) { type, display }

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

beta\_thinking\_config\_enabled: object { budget\_tokens, type, display }

budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

type: "enabled"

display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"

beta\_thinking\_config\_disabled: object { type }

type: "disabled"

beta\_thinking\_config\_adaptive: object { type, display }

type: "adaptive"

display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"

beta\_thinking\_delta: object { thinking, type }

thinking: string

type: "thinking\_delta"

beta\_thinking\_turns: object { type, value }

type: "thinking\_turns"

value: number

beta\_tool: object { input\_schema, name, allowed\_callers, 7 more }

input\_schema: object { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

"custom"

beta\_tool\_bash\_20241022: object { name, type, allowed\_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_bash\_20250124: object { name, type, allowed\_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_choice: [BetaToolChoiceAuto](api/beta.md) { type, disable\_parallel\_tool\_use }  or [BetaToolChoiceAny](api/beta.md) { type, disable\_parallel\_tool\_use }  or [BetaToolChoiceTool](api/beta.md) { name, type, disable\_parallel\_tool\_use }  or [BetaToolChoiceNone](api/beta.md) { type }

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

beta\_tool\_choice\_auto: object { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: "auto"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

beta\_tool\_choice\_any: object { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: "any"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

beta\_tool\_choice\_tool: object { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

beta\_tool\_choice\_none: object { type }

The model will not be allowed to use tools.

type: "none"

beta\_tool\_choice\_any: object { type, disable\_parallel\_tool\_use }

The model will use any available tools.

type: "any"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

beta\_tool\_choice\_auto: object { type, disable\_parallel\_tool\_use }

The model will automatically decide whether to use tools.

type: "auto"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.

beta\_tool\_choice\_none: object { type }

The model will not be allowed to use tools.

type: "none"

beta\_tool\_choice\_tool: object { name, type, disable\_parallel\_tool\_use }

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"

disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.

beta\_tool\_computer\_use\_20241022: object { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_computer\_use\_20250124: object { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_computer\_use\_20251124: object { display\_height\_px, display\_width\_px, name, 8 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20251124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_reference\_block: object { tool\_name, type }

tool\_name: string

type: "tool\_reference"

beta\_tool\_reference\_block\_param: object { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more }

tool\_use\_id: string

type: "tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  or [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  or 2 more

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_search\_result\_block\_param: object { content, source, title, 3 more }

content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

beta\_request\_document\_block: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

beta\_tool\_reference\_block\_param: object { tool\_name, type, cache\_control }

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

is\_error: optional boolean

beta\_tool\_search\_tool\_bm25\_20251119: object { name, type, allowed\_callers, 3 more }

name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_search\_tool\_regex\_20251119: object { name, type, allowed\_callers, 3 more }

name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_tool\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control }

content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block\_param: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_result\_error\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

beta\_tool\_search\_tool\_search\_result\_block\_param: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control }

tool\_name: string

type: "tool\_reference"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

beta\_tool\_text\_editor\_20241022: object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_text\_editor\_20250124: object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_text\_editor\_20250429: object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_text\_editor\_20250728: object { name, type, allowed\_callers, 5 more }

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

max\_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_union: [BetaTool](api/beta.md) { input\_schema, name, allowed\_callers, 7 more }  or [BetaToolBash20241022](api/beta.md) { name, type, allowed\_callers, 4 more }  or [BetaToolBash20250124](api/beta.md) { name, type, allowed\_callers, 4 more }  or 19 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

beta\_tool: object { input\_schema, name, allowed\_callers, 7 more }

input\_schema: object { type, properties, required }

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map[unknown]

required: optional array of string

name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

type: optional "custom"

"custom"

beta\_tool\_bash\_20241022: object { name, type, allowed\_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_bash\_20250124: object { name, type, allowed\_callers, 4 more }

name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_code\_execution\_tool\_20250522: object { name, type, allowed\_callers, 3 more }

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_code\_execution\_tool\_20250825: object { name, type, allowed\_callers, 3 more }

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_code\_execution\_tool\_20260120: object { name, type, allowed\_callers, 3 more }

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_computer\_use\_20241022: object { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_memory\_tool\_20250818: object { name, type, allowed\_callers, 4 more }

name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_computer\_use\_20250124: object { display\_height\_px, display\_width\_px, name, 7 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_text\_editor\_20241022: object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_computer\_use\_20251124: object { display\_height\_px, display\_width\_px, name, 8 more }

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.

name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20251124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_text\_editor\_20250124: object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_text\_editor\_20250429: object { name, type, allowed\_callers, 4 more }

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_text\_editor\_20250728: object { name, type, allowed\_callers, 5 more }

name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

max\_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_web\_search\_tool\_20250305: object { name, type, allowed\_callers, 7 more }

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional object { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

beta\_web\_fetch\_tool\_20250910: object { name, type, allowed\_callers, 8 more }

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_web\_search\_tool\_20260209: object { name, type, allowed\_callers, 7 more }

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional object { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

beta\_web\_fetch\_tool\_20260209: object { name, type, allowed\_callers, 8 more }

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_web\_fetch\_tool\_20260309: object { name, type, allowed\_callers, 9 more }

Web fetch tool with use\_cache parameter for bypassing cached content.

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

use\_cache: optional boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

beta\_tool\_search\_tool\_bm25\_20251119: object { name, type, allowed\_callers, 3 more }

name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_tool\_search\_tool\_regex\_20251119: object { name, type, allowed\_callers, 3 more }

name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_mcp\_toolset: object { mcp\_server\_name, type, cache\_control, 2 more }

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

configs: optional map[[BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: optional boolean

enabled: optional boolean

default\_config: optional object { defer\_loading, enabled }

Default configuration applied to all tools from this server

defer\_loading: optional boolean

enabled: optional boolean

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_tool\_use\_block\_param: object { id, input, name, 3 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_tool\_uses\_keep: object { type, value }

type: "tool\_uses"

value: number

beta\_tool\_uses\_trigger: object { type, value }

type: "tool\_uses"

value: number

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

beta\_user\_location: object { type, city, country, 2 more }

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

beta\_web\_fetch\_block\_param: object { content, type, url, retrieved\_at }

content: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

beta\_web\_fetch\_tool\_20250910: object { name, type, allowed\_callers, 8 more }

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_web\_fetch\_tool\_20260209: object { name, type, allowed\_callers, 8 more }

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

beta\_web\_fetch\_tool\_20260309: object { name, type, allowed\_callers, 9 more }

Web fetch tool with use\_cache parameter for bypassing cached content.

name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

use\_cache: optional boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more }

content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  or [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at }

beta\_web\_fetch\_tool\_result\_error\_block\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block\_param: object { content, type, url, retrieved\_at }

content: object { source, type, cache\_control, 3 more }

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

beta\_content\_block\_source: object { content, type }

content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string

beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)

beta\_text\_block\_param: object { text, type, cache\_control, citations }

text: string

type: "text"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional array of [BetaTextCitationParam](api/beta.md)

beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

start\_block\_index: number

type: "content\_block\_location"

beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

beta\_image\_block\_param: object { source, type, cache\_control }

source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type }

beta\_base64\_image\_source: object { data, media\_type, type }

data: string

media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"

beta\_url\_image\_source: object { type, url }

type: "url"

url: string

beta\_file\_image\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "image"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"

beta\_url\_pdf\_source: object { type, url }

type: "url"

url: string

beta\_file\_document\_source: object { file\_id, type }

file\_id: string

type: "file"

type: "document"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

citations: optional object { enabled }

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_tool\_result\_error\_block\_param: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_tool\_result\_error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

beta\_web\_search\_result\_block: object { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

beta\_web\_search\_result\_block\_param: object { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

beta\_web\_search\_tool\_20250305: object { name, type, allowed\_callers, 7 more }

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional object { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

beta\_web\_search\_tool\_20260209: object { name, type, allowed\_callers, 7 more }

name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"

allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

user\_location: optional object { type, city, country, 2 more }

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.

beta\_web\_search\_tool\_request\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block\_content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

beta\_web\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more }

content: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }  or [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type }

Result Block: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

beta\_web\_search\_tool\_request\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"

cache\_control: optional object { type, ttl }

Create a cache control breakpoint at this content block.

type: "ephemeral"

ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block\_param\_content: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }  or [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type }

Result Block: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string

beta\_web\_search\_tool\_request\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

beta\_web\_search\_tool\_result\_error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### BetaMessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

$ ant beta:messages:batches create

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

$ ant beta:messages:batches retrieve

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

$ ant beta:messages:batches list

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

$ ant beta:messages:batches cancel

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

$ ant beta:messages:batches delete

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

$ ant beta:messages:batches results

GET/v1/messages/batches/{message\_batch\_id}/results

##### ModelsExpand Collapse

beta\_deleted\_message\_batch: object { id, type }

id: string

ID of the Message Batch.

type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

beta\_message\_batch: object { id, archived\_at, cancel\_initiated\_at, 7 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: string

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.

ended\_at: string

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

expires\_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.

processing\_status: "in\_progress" or "canceling" or "ended"

Processing status of the Message Batch.

"in\_progress"

"canceling"

"ended"

request\_counts: object { canceled, errored, expired, 2 more }

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

results\_url: string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.

type: "message\_batch"

Object type.

For Message Batches, this is always `"message_batch"`.

beta\_message\_batch\_canceled\_result: object { type }

type: "canceled"

beta\_message\_batch\_errored\_result: object { error, type }

error: object { error, request\_id, type }

error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more

beta\_invalid\_request\_error: object { message, type }

message: string

type: "invalid\_request\_error"

beta\_authentication\_error: object { message, type }

message: string

type: "authentication\_error"

beta\_billing\_error: object { message, type }

message: string

type: "billing\_error"

beta\_permission\_error: object { message, type }

message: string

type: "permission\_error"

beta\_not\_found\_error: object { message, type }

message: string

type: "not\_found\_error"

beta\_rate\_limit\_error: object { message, type }

message: string

type: "rate\_limit\_error"

beta\_gateway\_timeout\_error: object { message, type }

message: string

type: "timeout\_error"

beta\_api\_error: object { message, type }

message: string

type: "api\_error"

beta\_overloaded\_error: object { message, type }

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"

beta\_message\_batch\_expired\_result: object { type }

type: "expired"

beta\_message\_batch\_individual\_response: object { custom\_id, result }

This is a single line in the response `.jsonl` file and does not represent the response as a whole.

custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.

result: [BetaMessageBatchSucceededResult](api/beta.md) { message, type }  or [BetaMessageBatchErroredResult](api/beta.md) { error, type }  or [BetaMessageBatchCanceledResult](api/beta.md) { type }  or [BetaMessageBatchExpiredResult](api/beta.md) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

beta\_message\_batch\_succeeded\_result: object { message, type }

message: object { id, container, content, 8 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](api/beta.md)

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

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: object { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "succeeded"

beta\_message\_batch\_errored\_result: object { error, type }

error: object { error, request\_id, type }

error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more

beta\_invalid\_request\_error: object { message, type }

message: string

type: "invalid\_request\_error"

beta\_authentication\_error: object { message, type }

message: string

type: "authentication\_error"

beta\_billing\_error: object { message, type }

message: string

type: "billing\_error"

beta\_permission\_error: object { message, type }

message: string

type: "permission\_error"

beta\_not\_found\_error: object { message, type }

message: string

type: "not\_found\_error"

beta\_rate\_limit\_error: object { message, type }

message: string

type: "rate\_limit\_error"

beta\_gateway\_timeout\_error: object { message, type }

message: string

type: "timeout\_error"

beta\_api\_error: object { message, type }

message: string

type: "api\_error"

beta\_overloaded\_error: object { message, type }

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"

beta\_message\_batch\_canceled\_result: object { type }

type: "canceled"

beta\_message\_batch\_expired\_result: object { type }

type: "expired"

beta\_message\_batch\_request\_counts: object { canceled, errored, expired, 2 more }

canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.

errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.

expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.

succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.

beta\_message\_batch\_result: [BetaMessageBatchSucceededResult](api/beta.md) { message, type }  or [BetaMessageBatchErroredResult](api/beta.md) { error, type }  or [BetaMessageBatchCanceledResult](api/beta.md) { type }  or [BetaMessageBatchExpiredResult](api/beta.md) { type }

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

beta\_message\_batch\_succeeded\_result: object { message, type }

message: object { id, container, content, 8 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](api/beta.md)

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

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: object { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "succeeded"

beta\_message\_batch\_errored\_result: object { error, type }

error: object { error, request\_id, type }

error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more

beta\_invalid\_request\_error: object { message, type }

message: string

type: "invalid\_request\_error"

beta\_authentication\_error: object { message, type }

message: string

type: "authentication\_error"

beta\_billing\_error: object { message, type }

message: string

type: "billing\_error"

beta\_permission\_error: object { message, type }

message: string

type: "permission\_error"

beta\_not\_found\_error: object { message, type }

message: string

type: "not\_found\_error"

beta\_rate\_limit\_error: object { message, type }

message: string

type: "rate\_limit\_error"

beta\_gateway\_timeout\_error: object { message, type }

message: string

type: "timeout\_error"

beta\_api\_error: object { message, type }

message: string

type: "api\_error"

beta\_overloaded\_error: object { message, type }

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"

beta\_message\_batch\_canceled\_result: object { type }

type: "canceled"

beta\_message\_batch\_expired\_result: object { type }

type: "expired"

beta\_message\_batch\_succeeded\_result: object { message, type }

message: object { id, container, content, 8 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

container: object { id, expires\_at, skills }

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.

skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version }

Skills loaded in the container

skill\_id: string

Skill ID

type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version

content: array of [BetaContentBlock](api/beta.md)

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

beta\_text\_block: object { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

beta\_thinking\_block: object { signature, thinking, type }

signature: string

thinking: string

type: "thinking"

beta\_redacted\_thinking\_block: object { data, type }

data: string

type: "redacted\_thinking"

beta\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

type: "tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_server\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: "web\_search" or "web\_fetch" or "code\_execution" or 4 more

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

beta\_web\_search\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more }

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller }

content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url }

beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 5 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"

beta\_web\_fetch\_block: object { content, retrieved\_at, type, url }

content: object { citations, source, title, type }

citations: object { enabled }

Citation configuration for the document

enabled: boolean

source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }

beta\_base64\_pdf\_source: object { data, media\_type, type }

data: string

media\_type: "application/pdf"

type: "base64"

beta\_plain\_text\_source: object { data, media\_type, type }

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"

caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type }

Tool invocation directly from the model.

beta\_direct\_caller: object { type }

Tool invocation directly from the model.

type: "direct"

beta\_server\_tool\_caller: object { tool\_id, type }

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"

beta\_server\_tool\_caller\_20260120: object { tool\_id, type }

tool\_id: string

type: "code\_execution\_20260120"

beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

beta\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"

beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"

beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more }

Code execution result with encrypted stdout for PFC + web\_search results.

content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"

beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }

beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"

beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more }

content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type }

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"

beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more }

beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"

beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more }

content: string

file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"

beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type }

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"

beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more }

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"

beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type }

content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type }

beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type }

error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"

beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type }

tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type }

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"

beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more }

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"

beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type }

content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type }

union\_member\_0: string

beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type }

citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"

beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"

beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more }

cited\_text: string

document\_index: number

document\_title: string

end\_block\_index: number

file\_id: string

start\_block\_index: number

type: "content\_block\_location"

beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more }

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string

beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more }

cited\_text: string

end\_block\_index: number

search\_result\_index: number

source: string

start\_block\_index: number

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"

beta\_container\_upload\_block: object { file\_id, type }

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"

beta\_compaction\_block: object { content, type }

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

type: "compaction"

context\_management: object { applied\_edits }

Context management response.

Information about context management strategies applied during the request.

applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type }

List of context management edits that were applied.

beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.

beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type }

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.

model: "claude-mythos-preview" or "claude-opus-4-6" or "claude-sonnet-4-6" or 13 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

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

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

"claude-opus-4-0"

Powerful model for complex tasks

"claude-opus-4-20250514"

Powerful model for complex tasks

"claude-sonnet-4-0"

High-performance model with extended thinking

"claude-sonnet-4-20250514"

High-performance model with extended thinking

"claude-3-haiku-20240307"

Fast and cost-effective model

role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.

stop\_details: object { category, explanation, type }

Structured information about a refusal.

category: "cyber" or "bio"

The policy category that triggered the refusal.

`null` when the refusal doesn't map to a named category.

"cyber"

"bio"

explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.

type: "refusal"

stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.

type: "message"

Object type.

For Messages, this is always `"message"`.

usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 7 more }

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.

iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a sampling iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration

beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }

Token usage for a compaction iteration.

cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens }

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration

output\_tokens: number

The number of output tokens which were used.

server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests }

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.

service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"

speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "succeeded"

#### BetaAgents

##### [Create Agent](api/beta/agents/create.md)

$ ant beta:agents create

POST/v1/agents

##### [List Agents](api/beta/agents/list.md)

$ ant beta:agents list

GET/v1/agents

##### [Get Agent](api/beta/agents/retrieve.md)

$ ant beta:agents retrieve

GET/v1/agents/{agent\_id}

##### [Update Agent](api/beta/agents/update.md)

$ ant beta:agents update

POST/v1/agents/{agent\_id}

##### [Archive Agent](api/beta/agents/archive.md)

$ ant beta:agents archive

POST/v1/agents/{agent\_id}/archive

##### ModelsExpand Collapse

beta\_managed\_agents\_agent: object { id, archived\_at, created\_at, 11 more }

A Managed Agents `agent`.

id: string

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

description: string

mcp\_servers: array of [BetaManagedAgentsMCPServerURLDefinition](api/beta.md) { name, type, url }

name: string

type: "url"

"url"

url: string

metadata: map[string]

model: object { id, speed }

Model identifier and configuration.

id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

updated\_at: string

A timestamp in RFC 3339 format

version: number

The agent's current version. Starts at 1 and increments when the agent is modified.

beta\_managed\_agents\_agent\_tool\_config: object { enabled, name, permission\_policy }

Configuration for a specific agent tool.

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

beta\_managed\_agents\_agent\_tool\_config\_params: object { name, enabled, permission\_policy }

Configuration override for a specific tool within a toolset.

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

enabled: optional boolean

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

beta\_managed\_agents\_agent\_toolset\_default\_config: object { enabled, permission\_policy }

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

beta\_managed\_agents\_agent\_toolset\_default\_config\_params: object { enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: optional boolean

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

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

beta\_managed\_agents\_agent\_toolset20260401\_params: object { type, configs, default\_config }

Configuration for built-in agent tools. Use this to enable or disable groups of tools available to the agent.

type: "agent\_toolset\_20260401"

"agent\_toolset\_20260401"

configs: optional array of [BetaManagedAgentsAgentToolConfigParams](api/beta.md) { name, enabled, permission\_policy }

Per-tool configuration overrides.

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

enabled: optional boolean

Whether this tool is enabled and available to Claude. Overrides the default\_config setting.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

default\_config: optional object { enabled, permission\_policy }

Default configuration for all tools in a toolset.

enabled: optional boolean

Whether tools are enabled and available to Claude by default. Defaults to true if not specified.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

beta\_managed\_agents\_anthropic\_skill: object { skill\_id, type, version }

A resolved Anthropic-managed skill.

skill\_id: string

type: "anthropic"

"anthropic"

version: string

beta\_managed\_agents\_anthropic\_skill\_params: object { skill\_id, type, version }

An Anthropic-managed skill.

skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").

type: "anthropic"

"anthropic"

version: optional string

Version to pin. Defaults to latest if omitted.

beta\_managed\_agents\_custom\_skill: object { skill\_id, type, version }

A resolved user-created custom skill.

skill\_id: string

type: "custom"

"custom"

version: string

beta\_managed\_agents\_custom\_skill\_params: object { skill\_id, type, version }

A user-created custom skill.

skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: "custom"

"custom"

version: optional string

Version to pin. Defaults to latest if omitted.

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

beta\_managed\_agents\_custom\_tool\_input\_schema: object { properties, required, type }

JSON Schema for custom tool input parameters.

properties: optional map[unknown]

JSON Schema properties defining the tool's input parameters.

required: optional array of string

List of required property names.

type: optional "object"

Must be 'object' for tool input schemas.

"object"

beta\_managed\_agents\_custom\_tool\_params: object { description, input\_schema, name, type }

A custom tool that is executed by the API client rather than the agent. When the agent calls this tool, an `agent.custom_tool_use` event is emitted and the session goes idle, waiting for the client to provide the result via a `user.custom_tool_result` event.

description: string

Description of what the tool does, shown to the agent to help it decide when to use the tool. 1-1024 characters.

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

Unique name for the tool. 1-128 characters; letters, digits, underscores, and hyphens.

type: "custom"

"custom"

beta\_managed\_agents\_mcp\_server\_url\_definition: object { name, type, url }

URL-based MCP server connection as returned in API responses.

name: string

type: "url"

"url"

url: string

beta\_managed\_agents\_mcp\_tool\_config: object { enabled, name, permission\_policy }

Resolved configuration for a specific MCP tool.

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

beta\_managed\_agents\_mcp\_tool\_config\_params: object { name, enabled, permission\_policy }

Configuration override for a specific MCP tool.

name: string

Name of the MCP tool to configure. 1-128 characters.

enabled: optional boolean

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

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

beta\_managed\_agents\_mcp\_toolset\_default\_config: object { enabled, permission\_policy }

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

beta\_managed\_agents\_mcp\_toolset\_default\_config\_params: object { enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: optional boolean

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

beta\_managed\_agents\_mcp\_toolset\_params: object { mcp\_server\_name, type, configs, default\_config }

Configuration for tools from an MCP server defined in `mcp_servers`.

mcp\_server\_name: string

Name of the MCP server. Must match a server name from the mcp\_servers array. 1-255 characters.

type: "mcp\_toolset"

"mcp\_toolset"

configs: optional array of [BetaManagedAgentsMCPToolConfigParams](api/beta.md) { name, enabled, permission\_policy }

Per-tool configuration overrides.

name: string

Name of the MCP tool to configure. 1-128 characters.

enabled: optional boolean

Whether this tool is enabled. Overrides the `default_config` setting.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

default\_config: optional object { enabled, permission\_policy }

Default configuration for all tools from an MCP server.

enabled: optional boolean

Whether tools are enabled by default. Defaults to true if not specified.

permission\_policy: optional [BetaManagedAgentsAlwaysAllowPolicy](api/beta.md) { type }  or [BetaManagedAgentsAlwaysAskPolicy](api/beta.md) { type }

Permission policy for tool execution.

beta\_managed\_agents\_always\_allow\_policy: object { type }

Tool calls are automatically approved without user confirmation.

type: "always\_allow"

"always\_allow"

beta\_managed\_agents\_always\_ask\_policy: object { type }

Tool calls require user confirmation before execution.

type: "always\_ask"

"always\_ask"

beta\_managed\_agents\_model\_config: object { id, speed }

Model identifier and configuration.

id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

beta\_managed\_agents\_model\_config\_params: object { id, speed }

An object that defines additional configuration control over model use

id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

beta\_managed\_agents\_skill\_params: [BetaManagedAgentsAnthropicSkillParams](api/beta.md) { skill\_id, type, version }  or [BetaManagedAgentsCustomSkillParams](api/beta.md) { skill\_id, type, version }

Skill to load in the session container.

beta\_managed\_agents\_anthropic\_skill\_params: object { skill\_id, type, version }

An Anthropic-managed skill.

skill\_id: string

Identifier of the Anthropic skill (e.g., "xlsx").

type: "anthropic"

"anthropic"

version: optional string

Version to pin. Defaults to latest if omitted.

beta\_managed\_agents\_custom\_skill\_params: object { skill\_id, type, version }

A user-created custom skill.

skill\_id: string

Tagged ID of the custom skill (e.g., "skill\_01XJ5...").

type: "custom"

"custom"

version: optional string

Version to pin. Defaults to latest if omitted.

beta\_managed\_agents\_url\_mcp\_server\_params: object { name, type, url }

URL-based MCP server connection.

name: string

Unique name for this server, referenced by mcp\_toolset configurations. 1-255 characters.

type: "url"

"url"

url: string

Endpoint URL for the MCP server.

#### BetaAgentsVersions

##### [List Agent Versions](api/beta/agents/versions/list.md)

$ ant beta:agents:versions list

GET/v1/agents/{agent\_id}/versions

#### BetaEnvironments

##### [Create Environment](api/beta/environments/create.md)

$ ant beta:environments create

POST/v1/environments

##### [List Environments](api/beta/environments/list.md)

$ ant beta:environments list

GET/v1/environments

##### [Get Environment](api/beta/environments/retrieve.md)

$ ant beta:environments retrieve

GET/v1/environments/{environment\_id}

##### [Update Environment](api/beta/environments/update.md)

$ ant beta:environments update

POST/v1/environments/{environment\_id}

##### [Delete Environment](api/beta/environments/delete.md)

$ ant beta:environments delete

DELETE/v1/environments/{environment\_id}

##### [Archive Environment](api/beta/environments/archive.md)

$ ant beta:environments archive

POST/v1/environments/{environment\_id}/archive

##### ModelsExpand Collapse

beta\_cloud\_config: object { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  or [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

beta\_unrestricted\_network: object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

beta\_limited\_network: object { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type

packages: object { apt, cargo, gem, 4 more }

Package manager configuration.

apt: array of string

Ubuntu/Debian packages to install

cargo: array of string

Rust packages to install

gem: array of string

Ruby packages to install

go: array of string

Go packages to install

npm: array of string

Node.js packages to install

pip: array of string

Python packages to install

type: optional "packages"

Package configuration type

"packages"

type: "cloud"

Environment type

beta\_cloud\_config\_params: object { type, networking, packages }

Request params for `cloud` environment configuration.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "cloud"

Environment type

networking: optional [BetaUnrestrictedNetwork](api/beta.md) { type }  or [BetaLimitedNetworkParams](api/beta.md) { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Network configuration policy. Omit on update to preserve the existing value.

beta\_unrestricted\_network: object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

beta\_limited\_network\_params: object { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers: optional boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: optional boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: optional array of string

Specifies domains the container can reach.

packages: optional object { apt, cargo, gem, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string

Ubuntu/Debian packages to install

cargo: optional array of string

Rust packages to install

gem: optional array of string

Ruby packages to install

go: optional array of string

Go packages to install

npm: optional array of string

Node.js packages to install

pip: optional array of string

Python packages to install

type: optional "packages"

Package configuration type

"packages"

beta\_environment: object { id, archived\_at, config, 6 more }

Unified Environment resource for both cloud and BYOC environments.

id: string

Environment identifier (e.g., 'env\_...')

archived\_at: string

RFC 3339 timestamp when environment was archived, or null if not archived

config: object { networking, packages, type }

`cloud` environment configuration.

networking: [BetaUnrestrictedNetwork](api/beta.md) { type }  or [BetaLimitedNetwork](api/beta.md) { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Network configuration policy.

beta\_unrestricted\_network: object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

beta\_limited\_network: object { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type

packages: object { apt, cargo, gem, 4 more }

Package manager configuration.

apt: array of string

Ubuntu/Debian packages to install

cargo: array of string

Rust packages to install

gem: array of string

Ruby packages to install

go: array of string

Go packages to install

npm: array of string

Node.js packages to install

pip: array of string

Python packages to install

type: optional "packages"

Package configuration type

"packages"

type: "cloud"

Environment type

created\_at: string

RFC 3339 timestamp when environment was created

description: string

User-provided description for the environment

metadata: map[string]

User-provided metadata key-value pairs

name: string

Human-readable name for the environment

type: "environment"

The type of object (always 'environment')

updated\_at: string

RFC 3339 timestamp when environment was last updated

beta\_environment\_delete\_response: object { id, type }

Response after deleting an environment.

id: string

Environment identifier

type: "environment\_deleted"

The type of response

beta\_limited\_network: object { allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts, type }

Limited network access.

allow\_mcp\_servers: boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array.

allow\_package\_managers: boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array.

allowed\_hosts: array of string

Specifies domains the container can reach.

type: "limited"

Network policy type

beta\_limited\_network\_params: object { type, allow\_mcp\_servers, allow\_package\_managers, allowed\_hosts }

Limited network request params.

Fields default to null; on update, omitted fields preserve the
existing value.

type: "limited"

Network policy type

allow\_mcp\_servers: optional boolean

Permits outbound access to MCP server endpoints configured on the agent, beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allow\_package\_managers: optional boolean

Permits outbound access to public package registries (PyPI, npm, etc.) beyond those listed in the `allowed_hosts` array. Defaults to `false`.

allowed\_hosts: optional array of string

Specifies domains the container can reach.

beta\_packages: object { apt, cargo, gem, 4 more }

Packages (and their versions) available in this environment.

apt: array of string

Ubuntu/Debian packages to install

cargo: array of string

Rust packages to install

gem: array of string

Ruby packages to install

go: array of string

Go packages to install

npm: array of string

Node.js packages to install

pip: array of string

Python packages to install

type: optional "packages"

Package configuration type

"packages"

beta\_packages\_params: object { apt, cargo, gem, 4 more }

Specify packages (and optionally their versions) available in this environment.

When versioning, use the version semantics relevant for the package manager, e.g. for `pip` use `package==1.0.0`. You are responsible for validating the package and version exist. Unversioned installs the latest.

apt: optional array of string

Ubuntu/Debian packages to install

cargo: optional array of string

Rust packages to install

gem: optional array of string

Ruby packages to install

go: optional array of string

Go packages to install

npm: optional array of string

Node.js packages to install

pip: optional array of string

Python packages to install

type: optional "packages"

Package configuration type

"packages"

beta\_unrestricted\_network: object { type }

Unrestricted network access.

type: "unrestricted"

Network policy type

#### BetaSessions

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

id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

id: "claude-opus-4-6" or "claude-sonnet-4-6" or "claude-haiku-4-5" or 5 more or string

The model that will power your agent.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

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

#### BetaSessionsEvents

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

#### BetaSessionsResources

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

#### BetaVaults

##### [Create Vault](api/beta/vaults/create.md)

$ ant beta:vaults create

POST/v1/vaults

##### [List Vaults](api/beta/vaults/list.md)

$ ant beta:vaults list

GET/v1/vaults

##### [Get Vault](api/beta/vaults/retrieve.md)

$ ant beta:vaults retrieve

GET/v1/vaults/{vault\_id}

##### [Update Vault](api/beta/vaults/update.md)

$ ant beta:vaults update

POST/v1/vaults/{vault\_id}

##### [Delete Vault](api/beta/vaults/delete.md)

$ ant beta:vaults delete

DELETE/v1/vaults/{vault\_id}

##### [Archive Vault](api/beta/vaults/archive.md)

$ ant beta:vaults archive

POST/v1/vaults/{vault\_id}/archive

##### ModelsExpand Collapse

beta\_managed\_agents\_deleted\_vault: object { id, type }

Confirmation of a deleted vault.

id: string

Unique identifier of the deleted vault.

type: "vault\_deleted"

"vault\_deleted"

beta\_managed\_agents\_vault: object { id, archived\_at, created\_at, 4 more }

A vault that stores credentials for use by agents during sessions.

id: string

Unique identifier for the vault.

archived\_at: string

A timestamp in RFC 3339 format

created\_at: string

A timestamp in RFC 3339 format

display\_name: string

Human-readable name for the vault.

metadata: map[string]

Arbitrary key-value metadata attached to the vault.

type: "vault"

"vault"

updated\_at: string

A timestamp in RFC 3339 format

#### BetaVaultsCredentials

##### [Create Credential](api/beta/vaults/credentials/create.md)

$ ant beta:vaults:credentials create

POST/v1/vaults/{vault\_id}/credentials

##### [List Credentials](api/beta/vaults/credentials/list.md)

$ ant beta:vaults:credentials list

GET/v1/vaults/{vault\_id}/credentials

##### [Get Credential](api/beta/vaults/credentials/retrieve.md)

$ ant beta:vaults:credentials retrieve

GET/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Update Credential](api/beta/vaults/credentials/update.md)

$ ant beta:vaults:credentials update

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Delete Credential](api/beta/vaults/credentials/delete.md)

$ ant beta:vaults:credentials delete

DELETE/v1/vaults/{vault\_id}/credentials/{credential\_id}

##### [Archive Credential](api/beta/vaults/credentials/archive.md)

$ ant beta:vaults:credentials archive

POST/v1/vaults/{vault\_id}/credentials/{credential\_id}/archive

##### ModelsExpand Collapse

beta\_managed\_agents\_credential: object { id, archived\_at, auth, 6 more }

A credential stored in a vault. Sensitive fields are never returned in responses.

id: string

Unique identifier for the credential.

archived\_at: string

A timestamp in RFC 3339 format

auth: [BetaManagedAgentsMCPOAuthAuthResponse](api/beta.md) { mcp\_server\_url, type, expires\_at, refresh }  or [BetaManagedAgentsStaticBearerAuthResponse](api/beta.md) { mcp\_server\_url, type }

Authentication details for a credential.

beta\_managed\_agents\_mcp\_oauth\_auth\_response: object { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

"mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional object { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type }

Token endpoint requires no client authentication.

type: "none"

"none"

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

"client\_secret\_basic"

beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

beta\_managed\_agents\_static\_bearer\_auth\_response: object { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

"static\_bearer"

created\_at: string

A timestamp in RFC 3339 format

metadata: map[string]

Arbitrary key-value metadata attached to the credential.

type: "vault\_credential"

"vault\_credential"

updated\_at: string

A timestamp in RFC 3339 format

vault\_id: string

Identifier of the vault this credential belongs to.

display\_name: optional string

Human-readable name for the credential.

beta\_managed\_agents\_deleted\_credential: object { id, type }

Confirmation of a deleted credential.

id: string

Unique identifier of the deleted credential.

type: "vault\_credential\_deleted"

"vault\_credential\_deleted"

beta\_managed\_agents\_mcp\_oauth\_auth\_response: object { mcp\_server\_url, type, expires\_at, refresh }

OAuth credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

"mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional object { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type }

Token endpoint requires no client authentication.

type: "none"

"none"

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

"client\_secret\_basic"

beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

beta\_managed\_agents\_mcp\_oauth\_create\_params: object { access\_token, mcp\_server\_url, type, 2 more }

Parameters for creating an MCP OAuth credential.

access\_token: string

OAuth access token.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "mcp\_oauth"

"mcp\_oauth"

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional object { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  or [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

beta\_managed\_agents\_token\_endpoint\_auth\_none\_param: object { type }

Token endpoint requires no client authentication.

type: "none"

"none"

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_param: object { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

"client\_secret\_basic"

beta\_managed\_agents\_token\_endpoint\_auth\_post\_param: object { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

beta\_managed\_agents\_mcp\_oauth\_refresh\_params: object { client\_id, refresh\_token, token\_endpoint, 3 more }

OAuth refresh token parameters for creating a credential with refresh support.

client\_id: string

OAuth client ID.

refresh\_token: string

OAuth refresh token.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneParam](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicParam](api/beta.md) { client\_secret, type }  or [BetaManagedAgentsTokenEndpointAuthPostParam](api/beta.md) { client\_secret, type }

Token endpoint requires no client authentication.

beta\_managed\_agents\_token\_endpoint\_auth\_none\_param: object { type }

Token endpoint requires no client authentication.

type: "none"

"none"

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_param: object { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

"client\_secret\_basic"

beta\_managed\_agents\_token\_endpoint\_auth\_post\_param: object { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

beta\_managed\_agents\_mcp\_oauth\_refresh\_response: object { client\_id, token\_endpoint, token\_endpoint\_auth, 2 more }

OAuth refresh token configuration returned in credential responses.

client\_id: string

OAuth client ID.

token\_endpoint: string

Token endpoint URL used to refresh the access token.

token\_endpoint\_auth: [BetaManagedAgentsTokenEndpointAuthNoneResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthBasicResponse](api/beta.md) { type }  or [BetaManagedAgentsTokenEndpointAuthPostResponse](api/beta.md) { type }

Token endpoint requires no client authentication.

beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type }

Token endpoint requires no client authentication.

type: "none"

"none"

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

"client\_secret\_basic"

beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

"client\_secret\_post"

resource: optional string

OAuth resource indicator.

scope: optional string

OAuth scope for the refresh request.

beta\_managed\_agents\_mcp\_oauth\_refresh\_update\_params: object { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: optional string

Updated OAuth refresh token.

scope: optional string

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_update\_param: object { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

"client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.

beta\_managed\_agents\_token\_endpoint\_auth\_post\_update\_param: object { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

"client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.

beta\_managed\_agents\_mcp\_oauth\_update\_params: object { type, access\_token, expires\_at, refresh }

Parameters for updating an MCP OAuth credential. The `mcp_server_url` is immutable.

type: "mcp\_oauth"

"mcp\_oauth"

access\_token: optional string

Updated OAuth access token.

expires\_at: optional string

A timestamp in RFC 3339 format

refresh: optional object { refresh\_token, scope, token\_endpoint\_auth }

Parameters for updating OAuth refresh token configuration.

refresh\_token: optional string

Updated OAuth refresh token.

scope: optional string

Updated OAuth scope for the refresh request.

token\_endpoint\_auth: optional [BetaManagedAgentsTokenEndpointAuthBasicUpdateParam](api/beta.md) { type, client\_secret }  or [BetaManagedAgentsTokenEndpointAuthPostUpdateParam](api/beta.md) { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_update\_param: object { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

"client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.

beta\_managed\_agents\_token\_endpoint\_auth\_post\_update\_param: object { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

"client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.

beta\_managed\_agents\_static\_bearer\_auth\_response: object { mcp\_server\_url, type }

Static bearer token credential details for an MCP server.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

"static\_bearer"

beta\_managed\_agents\_static\_bearer\_create\_params: object { token, mcp\_server\_url, type }

Parameters for creating a static bearer token credential.

token: string

Static bearer token value.

mcp\_server\_url: string

URL of the MCP server this credential authenticates against.

type: "static\_bearer"

"static\_bearer"

beta\_managed\_agents\_static\_bearer\_update\_params: object { type, token }

Parameters for updating a static bearer token credential. The `mcp_server_url` is immutable.

type: "static\_bearer"

"static\_bearer"

token: optional string

Updated static bearer token value.

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_param: object { client\_secret, type }

Token endpoint uses HTTP Basic authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_basic"

"client\_secret\_basic"

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_response: object { type }

Token endpoint uses HTTP Basic authentication with client credentials.

type: "client\_secret\_basic"

"client\_secret\_basic"

beta\_managed\_agents\_token\_endpoint\_auth\_basic\_update\_param: object { type, client\_secret }

Updated HTTP Basic authentication parameters for the token endpoint.

type: "client\_secret\_basic"

"client\_secret\_basic"

client\_secret: optional string

Updated OAuth client secret.

beta\_managed\_agents\_token\_endpoint\_auth\_none\_param: object { type }

Token endpoint requires no client authentication.

type: "none"

"none"

beta\_managed\_agents\_token\_endpoint\_auth\_none\_response: object { type }

Token endpoint requires no client authentication.

type: "none"

"none"

beta\_managed\_agents\_token\_endpoint\_auth\_post\_param: object { client\_secret, type }

Token endpoint uses POST body authentication with client credentials.

client\_secret: string

OAuth client secret.

type: "client\_secret\_post"

"client\_secret\_post"

beta\_managed\_agents\_token\_endpoint\_auth\_post\_response: object { type }

Token endpoint uses POST body authentication with client credentials.

type: "client\_secret\_post"

"client\_secret\_post"

beta\_managed\_agents\_token\_endpoint\_auth\_post\_update\_param: object { type, client\_secret }

Updated POST body authentication parameters for the token endpoint.

type: "client\_secret\_post"

"client\_secret\_post"

client\_secret: optional string

Updated OAuth client secret.

#### BetaFiles

##### [Upload File](api/beta/files/upload.md)

$ ant beta:files upload

POST/v1/files

##### [List Files](api/beta/files/list.md)

$ ant beta:files list

GET/v1/files

##### [Download File](api/beta/files/download.md)

$ ant beta:files download

GET/v1/files/{file\_id}/content

##### [Get File Metadata](api/beta/files/retrieve_metadata.md)

$ ant beta:files retrieve-metadata

GET/v1/files/{file\_id}

##### [Delete File](api/beta/files/delete.md)

$ ant beta:files delete

DELETE/v1/files/{file\_id}

##### ModelsExpand Collapse

beta\_file\_scope: object { id, type }

id: string

The ID of the scoping resource (e.g., the session ID).

type: "session"

The type of scope (e.g., `"session"`).

deleted\_file: object { id, type }

id: string

ID of the deleted file.

type: optional "file\_deleted"

Deleted object type.

For file deletion, this is always `"file_deleted"`.

"file\_deleted"

file\_metadata: object { id, created\_at, filename, 5 more }

id: string

Unique object identifier.

The format and length of IDs may change over time.

created\_at: string

RFC 3339 datetime string representing when the file was created.

filename: string

Original filename of the uploaded file.

mime\_type: string

MIME type of the file.

size\_bytes: number

Size of the file in bytes.

type: "file"

Object type.

For files, this is always `"file"`.

downloadable: optional boolean

Whether the file can be downloaded.

scope: optional object { id, type }

The scope of this file, indicating the context in which it was created (e.g., a session).

id: string

The ID of the scoping resource (e.g., the session ID).

type: "session"

The type of scope (e.g., `"session"`).

#### BetaSkills

##### [Create Skill](api/beta/skills/create.md)

$ ant beta:skills create

POST/v1/skills

##### [List Skills](api/beta/skills/list.md)

$ ant beta:skills list

GET/v1/skills

##### [Get Skill](api/beta/skills/retrieve.md)

$ ant beta:skills retrieve

GET/v1/skills/{skill\_id}

##### [Delete Skill](api/beta/skills/delete.md)

$ ant beta:skills delete

DELETE/v1/skills/{skill\_id}

#### BetaSkillsVersions

##### [Create Skill Version](api/beta/skills/versions/create.md)

$ ant beta:skills:versions create

POST/v1/skills/{skill\_id}/versions

##### [List Skill Versions](api/beta/skills/versions/list.md)

$ ant beta:skills:versions list

GET/v1/skills/{skill\_id}/versions

##### [Get Skill Version](api/beta/skills/versions/retrieve.md)

$ ant beta:skills:versions retrieve

GET/v1/skills/{skill\_id}/versions/{version}

##### [Delete Skill Version](api/beta/skills/versions/delete.md)

$ ant beta:skills:versions delete

DELETE/v1/skills/{skill\_id}/versions/{version}

---

*Copyright © Anthropic. All rights reserved.*
