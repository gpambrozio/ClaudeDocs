# Messages

Copy page



CLI

# Messages

##### [Create a Message](api/beta/messages/create.md)

$ ant beta:messages create

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

$ ant beta:messages count-tokens

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"



beta\_advisor\_redacted\_result\_block\_param: object { encrypted\_content, type, stop\_reason } 

encrypted\_content: string

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: "advisor\_redacted\_result"

stop\_reason: optional string



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_result\_block\_param: object { text, type, stop\_reason } 

text: string

type: "advisor\_result"

stop\_reason: optional string



beta\_advisor\_tool\_20260301: object { model, name, type, 7 more } 



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



name: "advisor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "advisor\_20260301"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caching: optional object { type, ttl } 

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_tokens: optional number

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_advisor\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaAdvisorToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlockParam](api/beta.md) { text, type, stop\_reason }  or [BetaAdvisorRedactedResultBlockParam](api/beta.md) { encrypted\_content, type, stop\_reason } 



beta\_advisor\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block\_param: object { text, type, stop\_reason } 

text: string

type: "advisor\_result"

stop\_reason: optional string



beta\_advisor\_redacted\_result\_block\_param: object { encrypted\_content, type, stop\_reason } 

encrypted\_content: string

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: "advisor\_redacted\_result"

stop\_reason: optional string

tool\_use\_id: string

type: "advisor\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_all\_thinking\_turns: object { type } 

type: "all"



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_bash\_code\_execution\_output\_block: object { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"



beta\_bash\_code\_execution\_output\_block\_param: object { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"



beta\_bash\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_cache\_control\_ephemeral: object { type, ttl } 

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.



beta\_cache\_miss\_messages\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



beta\_cache\_miss\_model\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



beta\_cache\_miss\_previous\_message\_not\_found: object { type } 

type: "previous\_message\_not\_found"



beta\_cache\_miss\_system\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



beta\_cache\_miss\_tools\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



beta\_cache\_miss\_unavailable: object { type } 

type: "unavailable"



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_config: object { enabled } 

enabled: boolean



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citations\_config\_param: object { enabled } 

enabled: optional boolean



beta\_citations\_delta: object { citation, type } 



citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_clear\_thinking\_20251015\_edit: object { type, keep } 

type: "clear\_thinking\_20251015"



keep: optional [BetaThinkingTurns](api/beta.md) { type, value }  or [BetaAllThinkingTurns](api/beta.md) { type }  or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.



beta\_thinking\_turns: object { type, value } 

type: "thinking\_turns"

value: number



beta\_all\_thinking\_turns: object { type } 

type: "all"

union\_member\_2: "all"



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



beta\_clear\_tool\_uses\_20250919\_edit: object { type, clear\_at\_least, clear\_tool\_inputs, 3 more } 

type: "clear\_tool\_uses\_20250919"



clear\_at\_least: optional object { type, value } 

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number



clear\_tool\_inputs: optional boolean or array of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

union\_member\_0: boolean

union\_member\_1: array of string

exclude\_tools: optional array of string

Tool names whose uses are preserved from clearing



keep: optional object { type, value } 

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number



trigger: optional [BetaInputTokensTrigger](api/beta.md) { type, value }  or [BetaToolUsesTrigger](api/beta.md) { type, value } 

Condition that triggers the context management strategy



beta\_input\_tokens\_trigger: object { type, value } 

type: "input\_tokens"

value: number



beta\_tool\_uses\_trigger: object { type, value } 

type: "tool\_uses"

value: number



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_code\_execution\_output\_block: object { file\_id, type } 

file\_id: string

type: "code\_execution\_output"



beta\_code\_execution\_output\_block\_param: object { file\_id, type } 

file\_id: string

type: "code\_execution\_output"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_code\_execution\_tool\_20250522: object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_code\_execution\_tool\_20250825: object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_code\_execution\_tool\_20260120: object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_code\_execution\_tool\_20260521: object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence.



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260521"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_code\_execution\_tool\_result\_block\_content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



beta\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_code\_execution\_tool\_result\_block\_param\_content: [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_tool\_result\_error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"



beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_compact\_20260112\_edit: object { type, instructions, pause\_after\_compaction, trigger } 

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.



trigger: optional object { type, value } 

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_compaction\_block\_param: object { type, cache\_control, content, encrypted\_content } 

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: "compaction"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional string

Summary of previously compacted content, or null if compaction failed

encrypted\_content: optional string

Opaque metadata from prior compaction, to be round-tripped verbatim



beta\_compaction\_content\_block\_delta: object { content, encrypted\_content, type } 

content: string

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction\_delta"



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



beta\_container\_params: object { id, skills } 

Container parameters with skills to be loaded.

id: optional string

Container id



skills: optional array of [BetaSkillParams](api/beta.md) { skill\_id, type, version } 

List of skills to load in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_container\_upload\_block\_param: object { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  or [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  or [BetaRedactedThinkingBlock](api/beta.md) { data, type }  or 14 more

Response model for a file uploaded to the container.



beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



beta\_content\_block\_param: [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  or [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }  or 19 more

Regular text content.



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_request\_document\_block: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string



beta\_search\_result\_block\_param: object { content, source, title, 3 more } 



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean



beta\_thinking\_block\_param: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block\_param: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



content: optional array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  or [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  or 2 more



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_search\_result\_block\_param: object { content, source, title, 3 more } 



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean



beta\_request\_document\_block: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string



beta\_tool\_reference\_block\_param: object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

is\_error: optional boolean



beta\_server\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more } 



content: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }  or [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type } 



Result Block: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



beta\_web\_search\_tool\_request\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more } 



content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  or [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at } 



beta\_web\_fetch\_tool\_result\_error\_block\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block\_param: object { content, type, url, retrieved\_at } 



content: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaAdvisorToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlockParam](api/beta.md) { text, type, stop\_reason }  or [BetaAdvisorRedactedResultBlockParam](api/beta.md) { encrypted\_content, type, stop\_reason } 



beta\_advisor\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block\_param: object { text, type, stop\_reason } 

text: string

type: "advisor\_result"

stop\_reason: optional string



beta\_advisor\_redacted\_result\_block\_param: object { encrypted\_content, type, stop\_reason } 

encrypted\_content: string

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: "advisor\_redacted\_result"

stop\_reason: optional string

tool\_use\_id: string

type: "advisor\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_bash\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_text\_editor\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error\_param: object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string



beta\_text\_editor\_code\_execution\_view\_result\_block\_param: object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number



beta\_text\_editor\_code\_execution\_create\_result\_block\_param: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block\_param: object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_tool\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error\_param: object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string



beta\_tool\_search\_tool\_search\_result\_block\_param: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_mcp\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_request\_mcp\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "mcp\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



content: optional string or array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_param\_content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

is\_error: optional boolean



beta\_container\_upload\_block\_param: object { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_compaction\_block\_param: object { type, cache\_control, content, encrypted\_content } 

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: "compaction"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional string

Summary of previously compacted content, or null if compaction failed

encrypted\_content: optional string

Opaque metadata from prior compaction, to be round-tripped verbatim



beta\_mid\_conversation\_system\_block\_param: object { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

System instruction text blocks.

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "mid\_conv\_system"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_fallback\_block\_param: object { from, to, type, trigger } 

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not
validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its
original position. The block marks the boundary between content produced
before and after a fallback hop, and the server relies on that boundary
to validate the turn: when thinking runs flank the boundary, omitting
the block merges them into one span the server cannot validate (the
request is rejected), and moving it into the middle of a single run is
likewise rejected; between non-thinking blocks the block's placement has
no validation effect.



from: object { model } 

Identifies one hop of a fallback transition.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

Identifies one hop of a fallback transition.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

type: "fallback"

trigger: optional unknown

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_content\_block\_source\_content: [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control } 



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_context\_management\_config: object { edits } 



edits: optional array of [BetaClearToolUses20250919Edit](api/beta.md) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  or [BetaClearThinking20251015Edit](api/beta.md) { type, keep }  or [BetaCompact20260112Edit](api/beta.md) { type, instructions, pause\_after\_compaction, trigger } 

List of context management edits to apply



beta\_clear\_tool\_uses\_20250919\_edit: object { type, clear\_at\_least, clear\_tool\_inputs, 3 more } 

type: "clear\_tool\_uses\_20250919"



clear\_at\_least: optional object { type, value } 

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: "input\_tokens"

value: number



clear\_tool\_inputs: optional boolean or array of string

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

union\_member\_0: boolean

union\_member\_1: array of string

exclude\_tools: optional array of string

Tool names whose uses are preserved from clearing



keep: optional object { type, value } 

Number of tool uses to retain in the conversation

type: "tool\_uses"

value: number



trigger: optional [BetaInputTokensTrigger](api/beta.md) { type, value }  or [BetaToolUsesTrigger](api/beta.md) { type, value } 

Condition that triggers the context management strategy



beta\_input\_tokens\_trigger: object { type, value } 

type: "input\_tokens"

value: number



beta\_tool\_uses\_trigger: object { type, value } 

type: "tool\_uses"

value: number



beta\_clear\_thinking\_20251015\_edit: object { type, keep } 

type: "clear\_thinking\_20251015"



keep: optional [BetaThinkingTurns](api/beta.md) { type, value }  or [BetaAllThinkingTurns](api/beta.md) { type }  or "all"

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.



beta\_thinking\_turns: object { type, value } 

type: "thinking\_turns"

value: number



beta\_all\_thinking\_turns: object { type } 

type: "all"

union\_member\_2: "all"



beta\_compact\_20260112\_edit: object { type, instructions, pause\_after\_compaction, trigger } 

Automatically compact older context when reaching the configured trigger threshold.

type: "compact\_20260112"

instructions: optional string

Additional instructions for summarization.

pause\_after\_compaction: optional boolean

Whether to pause after compaction and return the compaction block to the user.



trigger: optional object { type, value } 

When to trigger compaction. Defaults to 150000 input tokens.

type: "input\_tokens"

value: number



beta\_context\_management\_response: object { applied\_edits } 



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



beta\_count\_tokens\_context\_management\_response: object { original\_input\_tokens } 

original\_input\_tokens: number

The original token count before context management was applied



beta\_diagnostics: object { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



beta\_cache\_miss\_model\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



beta\_cache\_miss\_system\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



beta\_cache\_miss\_tools\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



beta\_cache\_miss\_messages\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



beta\_cache\_miss\_previous\_message\_not\_found: object { type } 

type: "previous\_message\_not\_found"



beta\_cache\_miss\_unavailable: object { type } 

type: "unavailable"



beta\_diagnostics\_param: object { previous\_message\_id } 

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

previous\_message\_id: optional string

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_document\_block: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



beta\_fallback\_block\_param: object { from, to, type, trigger } 

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not
validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its
original position. The block marks the boundary between content produced
before and after a fallback hop, and the server relies on that boundary
to validate the turn: when thinking runs flank the boundary, omitting
the block merges them into one span the server cannot validate (the
request is rejected), and moving it into the middle of a single run is
likewise rejected; between non-thinking blocks the block's placement has
no validation effect.



from: object { model } 

Identifies one hop of a fallback transition.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

Identifies one hop of a fallback transition.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

type: "fallback"

trigger: optional unknown

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



beta\_fallback\_info: object { model } 

Identifies one hop of a fallback transition.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



beta\_fallback\_info\_param: object { model } 

Identifies one hop of a fallback transition.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response



beta\_fallback\_param: object { model, max\_tokens, output\_config, 2 more } 

One entry in the `fallbacks` chain on a `/v1/messages` request.

`model` is required. The four override fields (`max_tokens`, `thinking`,
`output_config`, and `speed`) replace the corresponding top-level field
for this attempt only and are validated as if the request were made to
`model`. Any other key is rejected at parse time.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

max\_tokens: optional number



output\_config: optional object { effort, format, task\_budget } 



effort: optional "low" or "medium" or "high" or 2 more

All possible effort levels.

"low"

"medium"

"high"

"xhigh"

"max"



format: optional object { schema, type } 

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



task\_budget: optional object { total, type, remaining } 

User-configurable total token budget across contexts.

total: number

Total token budget across all contexts in the session.

type: "tokens"

The budget type. Currently only 'tokens' is supported.

remaining: optional number

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



speed: optional "standard" or "fast"

"standard"

"fast"



thinking: optional [BetaThinkingConfigEnabled](api/beta.md) { budget\_tokens, type, display }  or [BetaThinkingConfigDisabled](api/beta.md) { type }  or [BetaThinkingConfigAdaptive](api/beta.md) { type, display } 



beta\_thinking\_config\_enabled: object { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

type: "enabled"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"



beta\_thinking\_config\_disabled: object { type } 

type: "disabled"



beta\_thinking\_config\_adaptive: object { type, display } 

type: "adaptive"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"



beta\_fallback\_refusal\_trigger: object { category, type } 

The `from` model declined for policy reasons.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_input\_json\_delta: object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



beta\_input\_tokens\_clear\_at\_least: object { type, value } 

type: "input\_tokens"

value: number



beta\_input\_tokens\_trigger: object { type, value } 

type: "input\_tokens"

value: number



beta\_iterations\_usage: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response



beta\_json\_output\_format: object { schema, type } 

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



beta\_mcp\_tool\_config: object { defer\_loading, enabled } 

Configuration for a specific tool in an MCP toolset.

defer\_loading: optional boolean

enabled: optional boolean



beta\_mcp\_tool\_default\_config: object { defer\_loading, enabled } 

Default configuration for tools in an MCP toolset.

defer\_loading: optional boolean

enabled: optional boolean



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_mcp\_toolset: object { mcp\_server\_name, type, cache\_control, 2 more } 

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



configs: optional map[[BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: optional boolean

enabled: optional boolean



default\_config: optional object { defer\_loading, enabled } 

Default configuration applied to all tools from this server

defer\_loading: optional boolean

enabled: optional boolean



beta\_memory\_tool\_20250818: object { name, type, allowed\_callers, 4 more } 



name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_memory\_tool\_20250818\_command: [BetaMemoryTool20250818ViewCommand](api/beta.md) { command, path, view\_range }  or [BetaMemoryTool20250818CreateCommand](api/beta.md) { command, file\_text, path }  or [BetaMemoryTool20250818StrReplaceCommand](api/beta.md) { command, new\_str, old\_str, path }  or 3 more



beta\_memory\_tool\_20250818\_view\_command: object { command, path, view\_range } 

command: "view"

Command type identifier

path: string

Path to directory or file to view

view\_range: optional array of number

Optional line range for viewing specific lines



beta\_memory\_tool\_20250818\_create\_command: object { command, file\_text, path } 

command: "create"

Command type identifier

file\_text: string

Content to write to the file

path: string

Path where the file should be created



beta\_memory\_tool\_20250818\_str\_replace\_command: object { command, new\_str, old\_str, path } 

command: "str\_replace"

Command type identifier

new\_str: string

Text to replace with

old\_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced



beta\_memory\_tool\_20250818\_insert\_command: object { command, insert\_line, insert\_text, path } 

command: "insert"

Command type identifier

insert\_line: number

Line number where text should be inserted

insert\_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted



beta\_memory\_tool\_20250818\_delete\_command: object { command, path } 

command: "delete"

Command type identifier

path: string

Path to the file or directory to delete



beta\_memory\_tool\_20250818\_rename\_command: object { command, new\_path, old\_path } 

command: "rename"

Command type identifier

new\_path: string

New path for the file or directory

old\_path: string

Current path of the file or directory



beta\_memory\_tool\_20250818\_create\_command: object { command, file\_text, path } 

command: "create"

Command type identifier

file\_text: string

Content to write to the file

path: string

Path where the file should be created



beta\_memory\_tool\_20250818\_delete\_command: object { command, path } 

command: "delete"

Command type identifier

path: string

Path to the file or directory to delete



beta\_memory\_tool\_20250818\_insert\_command: object { command, insert\_line, insert\_text, path } 

command: "insert"

Command type identifier

insert\_line: number

Line number where text should be inserted

insert\_text: string

Text to insert at the specified line

path: string

Path to the file where text should be inserted



beta\_memory\_tool\_20250818\_rename\_command: object { command, new\_path, old\_path } 

command: "rename"

Command type identifier

new\_path: string

New path for the file or directory

old\_path: string

Current path of the file or directory



beta\_memory\_tool\_20250818\_str\_replace\_command: object { command, new\_str, old\_str, path } 

command: "str\_replace"

Command type identifier

new\_str: string

Text to replace with

old\_str: string

Text to search for and replace

path: string

Path to the file where text should be replaced



beta\_memory\_tool\_20250818\_view\_command: object { command, path, view\_range } 

command: "view"

Command type identifier

path: string

Path to directory or file to view

view\_range: optional array of number

Optional line range for viewing specific lines



beta\_message: object { id, container, content, 9 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



content: array of [BetaContentBlock](api/beta.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```





beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



context\_management: object { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



diagnostics: object { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



beta\_cache\_miss\_model\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



beta\_cache\_miss\_system\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



beta\_cache\_miss\_tools\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



beta\_cache\_miss\_messages\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



beta\_cache\_miss\_previous\_message\_not\_found: object { type } 

type: "previous\_message\_not\_found"



beta\_cache\_miss\_unavailable: object { type } 

type: "unavailable"



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"



speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"



beta\_message\_delta\_usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 4 more } 

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The cumulative number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_message\_param: object { content, role } 



content: array of [BetaContentBlockParam](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_request\_document\_block: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string



beta\_search\_result\_block\_param: object { content, source, title, 3 more } 



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean



beta\_thinking\_block\_param: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block\_param: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



content: optional array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  or [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  or 2 more



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_search\_result\_block\_param: object { content, source, title, 3 more } 



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean



beta\_request\_document\_block: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string



beta\_tool\_reference\_block\_param: object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

is\_error: optional boolean



beta\_server\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more } 



content: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }  or [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type } 



Result Block: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



beta\_web\_search\_tool\_request\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more } 



content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  or [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at } 



beta\_web\_fetch\_tool\_result\_error\_block\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block\_param: object { content, type, url, retrieved\_at } 



content: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaAdvisorToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlockParam](api/beta.md) { text, type, stop\_reason }  or [BetaAdvisorRedactedResultBlockParam](api/beta.md) { encrypted\_content, type, stop\_reason } 



beta\_advisor\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block\_param: object { text, type, stop\_reason } 

text: string

type: "advisor\_result"

stop\_reason: optional string



beta\_advisor\_redacted\_result\_block\_param: object { encrypted\_content, type, stop\_reason } 

encrypted\_content: string

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: "advisor\_redacted\_result"

stop\_reason: optional string

tool\_use\_id: string

type: "advisor\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block\_param: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_bash\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block\_param: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_text\_editor\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error\_param: object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string



beta\_text\_editor\_code\_execution\_view\_result\_block\_param: object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number



beta\_text\_editor\_code\_execution\_create\_result\_block\_param: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block\_param: object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_tool\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error\_param: object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string



beta\_tool\_search\_tool\_search\_result\_block\_param: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_mcp\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_request\_mcp\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "mcp\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



content: optional string or array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_param\_content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

is\_error: optional boolean



beta\_container\_upload\_block\_param: object { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: string

type: "container\_upload"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_compaction\_block\_param: object { type, cache\_control, content, encrypted\_content } 

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: "compaction"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

content: optional string

Summary of previously compacted content, or null if compaction failed

encrypted\_content: optional string

Opaque metadata from prior compaction, to be round-tripped verbatim



beta\_mid\_conversation\_system\_block\_param: object { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

System instruction text blocks.

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "mid\_conv\_system"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_fallback\_block\_param: object { from, to, type, trigger } 

A `fallback` block echoed back from a prior response.

Accepted in `messages[].content` and not rendered into the prompt; not
validated against the request's `fallbacks` chain or top-level `model`.

Echo the assistant turn back verbatim, including this block in its
original position. The block marks the boundary between content produced
before and after a fallback hop, and the server relies on that boundary
to validate the turn: when thinking runs flank the boundary, omitting
the block merges them into one span the server cannot validate (the
request is rejected), and moving it into the middle of a single run is
likewise rejected; between non-thinking blocks the block's placement has
no validation effect.



from: object { model } 

Identifies one hop of a fallback transition.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

Identifies one hop of a fallback transition.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

type: "fallback"

trigger: optional unknown

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



role: "user" or "assistant" or "system"

"user"

"assistant"

"system"



beta\_message\_tokens\_count: object { context\_management, input\_tokens } 



context\_management: object { original\_input\_tokens } 

Information about context management applied to the message.

original\_input\_tokens: number

The original token count before context management was applied

input\_tokens: number

The total number of tokens across the provided list of messages, system prompt, and tools.



beta\_metadata: object { user\_id } 



user\_id: optional string

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.



beta\_mid\_conversation\_system\_block\_param: object { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

System instruction text blocks.

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "mid\_conv\_system"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_output\_config: object { effort, format, task\_budget } 



effort: optional "low" or "medium" or "high" or 2 more

All possible effort levels.

"low"

"medium"

"high"

"xhigh"

"max"



format: optional object { schema, type } 

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: map[unknown]

The JSON schema of the format

type: "json\_schema"



task\_budget: optional object { total, type, remaining } 

User-configurable total token budget across contexts.

total: number

Total token budget across all contexts in the session.

type: "tokens"

The budget type. Currently only 'tokens' is supported.

remaining: optional number

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



beta\_output\_tokens\_details: object { thinking\_tokens } 



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_raw\_content\_block\_delta: [BetaTextDelta](api/beta.md) { text, type }  or [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  or [BetaCitationsDelta](api/beta.md) { citation, type }  or 3 more



beta\_text\_delta: object { text, type } 

text: string

type: "text\_delta"



beta\_input\_json\_delta: object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



beta\_citations\_delta: object { citation, type } 



citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"



beta\_thinking\_delta: object { estimated\_tokens, thinking, type } 

estimated\_tokens: number

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: string

type: "thinking\_delta"



beta\_signature\_delta: object { signature, type } 

signature: string

type: "signature\_delta"



beta\_compaction\_content\_block\_delta: object { content, encrypted\_content, type } 

content: string

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction\_delta"



beta\_raw\_content\_block\_delta\_event: object { delta, index, type } 



delta: [BetaTextDelta](api/beta.md) { text, type }  or [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  or [BetaCitationsDelta](api/beta.md) { citation, type }  or 3 more



beta\_text\_delta: object { text, type } 

text: string

type: "text\_delta"



beta\_input\_json\_delta: object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



beta\_citations\_delta: object { citation, type } 



citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"



beta\_thinking\_delta: object { estimated\_tokens, thinking, type } 

estimated\_tokens: number

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: string

type: "thinking\_delta"



beta\_signature\_delta: object { signature, type } 

signature: string

type: "signature\_delta"



beta\_compaction\_content\_block\_delta: object { content, encrypted\_content, type } 

content: string

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction\_delta"

index: number

type: "content\_block\_delta"



beta\_raw\_content\_block\_start\_event: object { content\_block, index, type } 



content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  or [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  or [BetaRedactedThinkingBlock](api/beta.md) { data, type }  or 14 more

Response model for a file uploaded to the container.



beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"

index: number

type: "content\_block\_start"



beta\_raw\_content\_block\_stop\_event: object { index, type } 

index: number

type: "content\_block\_stop"



beta\_raw\_message\_delta\_event: object { context\_management, delta, type, usage } 



context\_management: object { applied\_edits } 

Information about context management strategies applied during the request



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



delta: object { container, stop\_details, stop\_reason, stop\_sequence } 



container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

type: "message\_delta"



usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 4 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The cumulative number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



beta\_raw\_message\_start\_event: object { message, type } 



message: object { id, container, content, 9 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



content: array of [BetaContentBlock](api/beta.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```





beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



context\_management: object { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



diagnostics: object { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



beta\_cache\_miss\_model\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



beta\_cache\_miss\_system\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



beta\_cache\_miss\_tools\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



beta\_cache\_miss\_messages\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



beta\_cache\_miss\_previous\_message\_not\_found: object { type } 

type: "previous\_message\_not\_found"



beta\_cache\_miss\_unavailable: object { type } 

type: "unavailable"



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"



speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "message\_start"



beta\_raw\_message\_stop\_event: object { type } 

type: "message\_stop"



beta\_raw\_message\_stream\_event: [BetaRawMessageStartEvent](api/beta.md) { message, type }  or [BetaRawMessageDeltaEvent](api/beta.md) { context\_management, delta, type, usage }  or [BetaRawMessageStopEvent](api/beta.md) { type }  or 3 more



beta\_raw\_message\_start\_event: object { message, type } 



message: object { id, container, content, 9 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



content: array of [BetaContentBlock](api/beta.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```





beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



context\_management: object { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



diagnostics: object { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



beta\_cache\_miss\_model\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



beta\_cache\_miss\_system\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



beta\_cache\_miss\_tools\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



beta\_cache\_miss\_messages\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



beta\_cache\_miss\_previous\_message\_not\_found: object { type } 

type: "previous\_message\_not\_found"



beta\_cache\_miss\_unavailable: object { type } 

type: "unavailable"



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"



speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "message\_start"



beta\_raw\_message\_delta\_event: object { context\_management, delta, type, usage } 



context\_management: object { applied\_edits } 

Information about context management strategies applied during the request



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



delta: object { container, stop\_details, stop\_reason, stop\_sequence } 



container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: string

type: "message\_delta"



usage: object { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 4 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: number

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The cumulative number of input tokens read from the cache.

input\_tokens: number

The cumulative number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The cumulative number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



beta\_raw\_message\_stop\_event: object { type } 

type: "message\_stop"



beta\_raw\_content\_block\_start\_event: object { content\_block, index, type } 



content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  or [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  or [BetaRedactedThinkingBlock](api/beta.md) { data, type }  or 14 more

Response model for a file uploaded to the container.



beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"

index: number

type: "content\_block\_start"



beta\_raw\_content\_block\_delta\_event: object { delta, index, type } 



delta: [BetaTextDelta](api/beta.md) { text, type }  or [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  or [BetaCitationsDelta](api/beta.md) { citation, type }  or 3 more



beta\_text\_delta: object { text, type } 

text: string

type: "text\_delta"



beta\_input\_json\_delta: object { partial\_json, type } 

partial\_json: string

type: "input\_json\_delta"



beta\_citations\_delta: object { citation, type } 



citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

type: "citations\_delta"



beta\_thinking\_delta: object { estimated\_tokens, thinking, type } 

estimated\_tokens: number

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: string

type: "thinking\_delta"



beta\_signature\_delta: object { signature, type } 

signature: string

type: "signature\_delta"



beta\_compaction\_content\_block\_delta: object { content, encrypted\_content, type } 

content: string

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction\_delta"

index: number

type: "content\_block\_delta"



beta\_raw\_content\_block\_stop\_event: object { index, type } 

index: number

type: "content\_block\_stop"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_redacted\_thinking\_block\_param: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_refusal\_stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



beta\_request\_document\_block: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string



beta\_request\_mcp\_server\_tool\_configuration: object { allowed\_tools, enabled } 

allowed\_tools: optional array of string

enabled: optional boolean



beta\_request\_mcp\_server\_url\_definition: object { name, type, url, 2 more } 

name: string

type: "url"

url: string

authorization\_token: optional string



tool\_configuration: optional object { allowed\_tools, enabled } 

allowed\_tools: optional array of string

enabled: optional boolean



beta\_request\_mcp\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "mcp\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



content: optional string or array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_param\_content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

is\_error: optional boolean



beta\_search\_result\_block\_param: object { content, source, title, 3 more } 



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_usage: object { web\_fetch\_requests, web\_search\_requests } 

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_signature\_delta: object { signature, type } 

signature: string

type: "signature\_delta"



beta\_skill: object { skill\_id, type, version } 

A skill that was loaded in a container (response model).

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



beta\_skill\_params: object { skill\_id, type, version } 

Specification for a skill to be loaded in a container (request model).

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: optional string

Skill version or 'latest' for most recent version



beta\_stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_text\_citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  or 2 more



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_text\_citation\_param: [BetaCitationCharLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  or [BetaCitationPageLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  or [BetaCitationContentBlockLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  or 2 more



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_text\_delta: object { text, type } 

text: string

type: "text\_delta"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block\_param: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block\_param: object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error\_param: object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string



beta\_text\_editor\_code\_execution\_view\_result\_block\_param: object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number



beta\_text\_editor\_code\_execution\_create\_result\_block\_param: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block\_param: object { type, lines, new\_lines, 3 more } 

type: "text\_editor\_code\_execution\_str\_replace\_result"

lines: optional array of string

new\_lines: optional number

new\_start: optional number

old\_lines: optional number

old\_start: optional number

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_tool\_result\_error\_param: object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: "text\_editor\_code\_execution\_tool\_result\_error"

error\_message: optional string



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_view\_result\_block\_param: object { content, file\_type, type, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

type: "text\_editor\_code\_execution\_view\_result"

num\_lines: optional number

start\_line: optional number

total\_lines: optional number



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_thinking\_block\_param: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_thinking\_config\_adaptive: object { type, display } 

type: "adaptive"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"



beta\_thinking\_config\_disabled: object { type } 

type: "disabled"



beta\_thinking\_config\_enabled: object { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

type: "enabled"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"



beta\_thinking\_config\_param: [BetaThinkingConfigEnabled](api/beta.md) { budget\_tokens, type, display }  or [BetaThinkingConfigDisabled](api/beta.md) { type }  or [BetaThinkingConfigAdaptive](api/beta.md) { type, display } 

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.



beta\_thinking\_config\_enabled: object { budget\_tokens, type, display } 



budget\_tokens: number

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

type: "enabled"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"



beta\_thinking\_config\_disabled: object { type } 

type: "disabled"



beta\_thinking\_config\_adaptive: object { type, display } 

type: "adaptive"



display: optional "summarized" or "omitted"

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

"summarized"

"omitted"



beta\_thinking\_delta: object { estimated\_tokens, thinking, type } 

estimated\_tokens: number

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: string

type: "thinking\_delta"



beta\_thinking\_turns: object { type, value } 

type: "thinking\_turns"

value: number



beta\_token\_task\_budget: object { total, type, remaining } 

User-configurable total token budget across contexts.

total: number

Total token budget across all contexts in the session.

type: "tokens"

The budget type. Currently only 'tokens' is supported.

remaining: optional number

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



beta\_tool: object { input\_schema, name, allowed\_callers, 7 more } 



input\_schema: object { type, properties, required } 

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map[unknown]

required: optional array of string



name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



type: optional "custom"

"custom"



beta\_tool\_bash\_20241022: object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_bash\_20250124: object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_choice: [BetaToolChoiceAuto](api/beta.md) { type, disable\_parallel\_tool\_use }  or [BetaToolChoiceAny](api/beta.md) { type, disable\_parallel\_tool\_use }  or [BetaToolChoiceTool](api/beta.md) { name, type, disable\_parallel\_tool\_use }  or [BetaToolChoiceNone](api/beta.md) { type } 

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.



beta\_tool\_choice\_auto: object { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: "auto"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



beta\_tool\_choice\_any: object { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: "any"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



beta\_tool\_choice\_tool: object { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



beta\_tool\_choice\_none: object { type } 

The model will not be allowed to use tools.

type: "none"



beta\_tool\_choice\_any: object { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: "any"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



beta\_tool\_choice\_auto: object { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: "auto"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



beta\_tool\_choice\_none: object { type } 

The model will not be allowed to use tools.

type: "none"



beta\_tool\_choice\_tool: object { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: string

The name of the tool to use.

type: "tool"



disable\_parallel\_tool\_use: optional boolean

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



beta\_tool\_computer\_use\_20241022: object { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20241022"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_computer\_use\_20250124: object { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_computer\_use\_20251124: object { display\_height\_px, display\_width\_px, name, 8 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20251124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_reference\_block: object { tool\_name, type } 

tool\_name: string

type: "tool\_reference"



beta\_tool\_reference\_block\_param: object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_tool\_result\_block\_param: object { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: string

type: "tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



content: optional array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  or [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  or [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  or 2 more



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_search\_result\_block\_param: object { content, source, title, 3 more } 



content: array of [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

source: string

title: string

type: "search\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean



beta\_request\_document\_block: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string



beta\_tool\_reference\_block\_param: object { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: string

type: "tool\_reference"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

is\_error: optional boolean



beta\_tool\_search\_tool\_bm25\_20251119: object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_search\_tool\_regex\_20251119: object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_tool\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, cache\_control } 



content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  or [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error\_param: object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string



beta\_tool\_search\_tool\_search\_result\_block\_param: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_result\_error\_param: object { error\_code, type, error\_message } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "tool\_search\_tool\_result\_error"

error\_message: optional string



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"



beta\_tool\_search\_tool\_search\_result\_block\_param: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } 

tool\_name: string

type: "tool\_reference"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "tool\_search\_tool\_search\_result"



beta\_tool\_text\_editor\_20241022: object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_text\_editor\_20250124: object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_text\_editor\_20250429: object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_text\_editor\_20250728: object { name, type, allowed\_callers, 5 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

max\_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_union: [BetaTool](api/beta.md) { input\_schema, name, allowed\_callers, 7 more }  or [BetaToolBash20241022](api/beta.md) { name, type, allowed\_callers, 4 more }  or [BetaToolBash20250124](api/beta.md) { name, type, allowed\_callers, 4 more }  or 21 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



beta\_tool: object { input\_schema, name, allowed\_callers, 7 more } 



input\_schema: object { type, properties, required } 

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: "object"

properties: optional map[unknown]

required: optional array of string



name: string

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description: optional string

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: optional boolean

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



type: optional "custom"

"custom"



beta\_tool\_bash\_20241022: object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20241022"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_bash\_20250124: object { name, type, allowed\_callers, 4 more } 



name: "bash"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "bash\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_code\_execution\_tool\_20250522: object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250522"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_code\_execution\_tool\_20250825: object { name, type, allowed\_callers, 3 more } 



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20250825"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_code\_execution\_tool\_20260120: object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260120"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_code\_execution\_tool\_20260521: object { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence.



name: "code\_execution"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "code\_execution\_20260521"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_computer\_use\_20241022: object { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20241022"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_memory\_tool\_20250818: object { name, type, allowed\_callers, 4 more } 



name: "memory"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "memory\_20250818"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_computer\_use\_20250124: object { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_text\_editor\_20241022: object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20241022"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_computer\_use\_20251124: object { display\_height\_px, display\_width\_px, name, 8 more } 

display\_height\_px: number

The height of the display in pixels.

display\_width\_px: number

The width of the display in pixels.



name: "computer"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "computer\_20251124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: optional number

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: optional boolean

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_text\_editor\_20250124: object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_editor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250124"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_text\_editor\_20250429: object { name, type, allowed\_callers, 4 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250429"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_text\_editor\_20250728: object { name, type, allowed\_callers, 5 more } 



name: "str\_replace\_based\_edit\_tool"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "text\_editor\_20250728"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: optional array of map[unknown]

max\_characters: optional number

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_web\_search\_tool\_20250305: object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional object { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



beta\_web\_fetch\_tool\_20250910: object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_web\_search\_tool\_20260209: object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional object { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



beta\_web\_fetch\_tool\_20260209: object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_web\_fetch\_tool\_20260309: object { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

use\_cache: optional boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



beta\_advisor\_tool\_20260301: object { model, name, type, 7 more } 



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



name: "advisor"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "advisor\_20260301"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caching: optional object { type, ttl } 

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_tokens: optional number

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_search\_tool\_bm25\_20251119: object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_bm25"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_bm25\_20251119" or "tool\_search\_tool\_bm25"

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_tool\_search\_tool\_regex\_20251119: object { name, type, allowed\_callers, 3 more } 



name: "tool\_search\_tool\_regex"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: "tool\_search\_tool\_regex\_20251119" or "tool\_search\_tool\_regex"

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_mcp\_toolset: object { mcp\_server\_name, type, cache\_control, 2 more } 

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: string

Name of the MCP server to configure tools for

type: "mcp\_toolset"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



configs: optional map[[BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: optional boolean

enabled: optional boolean



default\_config: optional object { defer\_loading, enabled } 

Default configuration applied to all tools from this server

defer\_loading: optional boolean

enabled: optional boolean



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_tool\_use\_block\_param: object { id, input, name, 3 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_tool\_uses\_keep: object { type, value } 

type: "tool\_uses"

value: number



beta\_tool\_uses\_trigger: object { type, value } 

type: "tool\_uses"

value: number



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"



speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"



beta\_user\_location: object { type, city, country, 2 more } 

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL



beta\_web\_fetch\_block\_param: object { content, type, url, retrieved\_at } 



content: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved



beta\_web\_fetch\_tool\_20250910: object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20250910"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_web\_fetch\_tool\_20260209: object { name, type, allowed\_callers, 8 more } 



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



beta\_web\_fetch\_tool\_20260309: object { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: "web\_fetch"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_fetch\_20260309"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

List of domains to allow fetching from

blocked\_domains: optional array of string

List of domains to block fetching from



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: optional boolean

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: optional number

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs

use\_cache: optional boolean

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more } 



content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  or [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at } 



beta\_web\_fetch\_tool\_result\_error\_block\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block\_param: object { content, type, url, retrieved\_at } 



content: object { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  or [BetaContentBlockSource](api/beta.md) { content, type }  or 2 more



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"



beta\_content\_block\_source: object { content, type } 



content: string or array of [BetaContentBlockSourceContent](api/beta.md)

union\_member\_0: string



beta\_content\_block\_source\_content: array of [BetaContentBlockSourceContent](api/beta.md)



beta\_text\_block\_param: object { text, type, cache\_control, citations } 

text: string

type: "text"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional array of [BetaTextCitationParam](api/beta.md)



beta\_citation\_char\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location\_param: object { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citation\_web\_search\_result\_location\_param: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location\_param: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"



beta\_image\_block\_param: object { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  or [BetaURLImageSource](api/beta.md) { type, url }  or [BetaFileImageSource](api/beta.md) { file\_id, type } 



beta\_base64\_image\_source: object { data, media\_type, type } 

data: string



media\_type: "image/jpeg" or "image/png" or "image/gif" or "image/webp"

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: "base64"



beta\_url\_image\_source: object { type, url } 

type: "url"

url: string



beta\_file\_image\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "image"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

type: "content"



beta\_url\_pdf\_source: object { type, url } 

type: "url"

url: string



beta\_file\_document\_source: object { file\_id, type } 

file\_id: string

type: "file"

type: "document"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



citations: optional object { enabled } 

enabled: optional boolean

context: optional string

title: optional string

type: "web\_fetch\_result"

url: string

Fetched content URL

retrieved\_at: optional string

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_tool\_result\_error\_block\_param: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_tool\_result\_error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"



beta\_web\_search\_result\_block: object { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string



beta\_web\_search\_result\_block\_param: object { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



beta\_web\_search\_tool\_20250305: object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20250305"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional object { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



beta\_web\_search\_tool\_20260209: object { name, type, allowed\_callers, 7 more } 



name: "web\_search"

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: "web\_search\_20260209"



allowed\_callers: optional array of "direct" or "code\_execution\_20250825" or "code\_execution\_20260120" or "code\_execution\_20260521"

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: optional array of string

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: optional array of string

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"

defer\_loading: optional boolean

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: optional number

Maximum number of times the tool can be used in the API request.

strict: optional boolean

When true, guarantees schema validation on tool names and inputs



user\_location: optional object { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: "approximate"

city: optional string

The city of the user.

country: optional string

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: optional string

The region of the user.

timezone: optional string

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



beta\_web\_search\_tool\_request\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block\_content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string



beta\_web\_search\_tool\_result\_block\_param: object { content, tool\_use\_id, type, 2 more } 



content: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }  or [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type } 



Result Block: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



beta\_web\_search\_tool\_request\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"

tool\_use\_id: string

type: "web\_search\_tool\_result"



cache\_control: optional object { type, ttl } 

Create a cache control breakpoint at this content block.

type: "ephemeral"



ttl: optional "5m" or "1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

"5m"

"1h"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block\_param\_content: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more }  or [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type } 



Result Block: array of [BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } 

encrypted\_content: string

title: string

type: "web\_search\_result"

url: string

page\_age: optional string



beta\_web\_search\_tool\_request\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



beta\_web\_search\_tool\_result\_error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### MessagesBatches

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



beta\_deleted\_message\_batch: object { id, type } 

id: string

ID of the Message Batch.



type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



beta\_message\_batch: object { id, archived\_at, cancel\_initiated\_at, 7 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: string

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: string

RFC 3339 datetime string representing the time at which the Message Batch was created.



ended\_at: string

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

expires\_at: string

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



processing\_status: "in\_progress" or "canceling" or "ended"

Processing status of the Message Batch.

"in\_progress"

"canceling"

"ended"



request\_counts: object { canceled, errored, expired, 2 more } 

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.



succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



results\_url: string

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



type: "message\_batch"

Object type.

For Message Batches, this is always `"message_batch"`.



beta\_message\_batch\_canceled\_result: object { type } 

type: "canceled"



beta\_message\_batch\_errored\_result: object { error, type } 



error: object { error, request\_id, type } 



error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more



beta\_invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



beta\_authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



beta\_billing\_error: object { message, type } 

message: string

type: "billing\_error"



beta\_permission\_error: object { message, type } 

message: string

type: "permission\_error"



beta\_not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



beta\_rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



beta\_gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



beta\_api\_error: object { message, type } 

message: string

type: "api\_error"



beta\_overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



beta\_message\_batch\_expired\_result: object { type } 

type: "expired"



beta\_message\_batch\_individual\_response: object { custom\_id, result } 

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: string

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [BetaMessageBatchSucceededResult](api/beta.md) { message, type }  or [BetaMessageBatchErroredResult](api/beta.md) { error, type }  or [BetaMessageBatchCanceledResult](api/beta.md) { type }  or [BetaMessageBatchExpiredResult](api/beta.md) { type } 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.



beta\_message\_batch\_succeeded\_result: object { message, type } 



message: object { id, container, content, 9 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



content: array of [BetaContentBlock](api/beta.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```





beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



context\_management: object { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



diagnostics: object { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



beta\_cache\_miss\_model\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



beta\_cache\_miss\_system\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



beta\_cache\_miss\_tools\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



beta\_cache\_miss\_messages\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



beta\_cache\_miss\_previous\_message\_not\_found: object { type } 

type: "previous\_message\_not\_found"



beta\_cache\_miss\_unavailable: object { type } 

type: "unavailable"



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"



speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "succeeded"



beta\_message\_batch\_errored\_result: object { error, type } 



error: object { error, request\_id, type } 



error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more



beta\_invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



beta\_authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



beta\_billing\_error: object { message, type } 

message: string

type: "billing\_error"



beta\_permission\_error: object { message, type } 

message: string

type: "permission\_error"



beta\_not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



beta\_rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



beta\_gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



beta\_api\_error: object { message, type } 

message: string

type: "api\_error"



beta\_overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



beta\_message\_batch\_canceled\_result: object { type } 

type: "canceled"



beta\_message\_batch\_expired\_result: object { type } 

type: "expired"



beta\_message\_batch\_request\_counts: object { canceled, errored, expired, 2 more } 



canceled: number

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: number

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: number

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: number

Number of requests in the Message Batch that are processing.



succeeded: number

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



beta\_message\_batch\_result: [BetaMessageBatchSucceededResult](api/beta.md) { message, type }  or [BetaMessageBatchErroredResult](api/beta.md) { error, type }  or [BetaMessageBatchCanceledResult](api/beta.md) { type }  or [BetaMessageBatchExpiredResult](api/beta.md) { type } 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.



beta\_message\_batch\_succeeded\_result: object { message, type } 



message: object { id, container, content, 9 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



content: array of [BetaContentBlock](api/beta.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```





beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



context\_management: object { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



diagnostics: object { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



beta\_cache\_miss\_model\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



beta\_cache\_miss\_system\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



beta\_cache\_miss\_tools\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



beta\_cache\_miss\_messages\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



beta\_cache\_miss\_previous\_message\_not\_found: object { type } 

type: "previous\_message\_not\_found"



beta\_cache\_miss\_unavailable: object { type } 

type: "unavailable"



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"



speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "succeeded"



beta\_message\_batch\_errored\_result: object { error, type } 



error: object { error, request\_id, type } 



error: [BetaInvalidRequestError](api/beta.md) { message, type }  or [BetaAuthenticationError](api/beta.md) { message, type }  or [BetaBillingError](api/beta.md) { message, type }  or 6 more



beta\_invalid\_request\_error: object { message, type } 

message: string

type: "invalid\_request\_error"



beta\_authentication\_error: object { message, type } 

message: string

type: "authentication\_error"



beta\_billing\_error: object { message, type } 

message: string

type: "billing\_error"



beta\_permission\_error: object { message, type } 

message: string

type: "permission\_error"



beta\_not\_found\_error: object { message, type } 

message: string

type: "not\_found\_error"



beta\_rate\_limit\_error: object { message, type } 

message: string

type: "rate\_limit\_error"



beta\_gateway\_timeout\_error: object { message, type } 

message: string

type: "timeout\_error"



beta\_api\_error: object { message, type } 

message: string

type: "api\_error"



beta\_overloaded\_error: object { message, type } 

message: string

type: "overloaded\_error"

request\_id: string

type: "error"

type: "errored"



beta\_message\_batch\_canceled\_result: object { type } 

type: "canceled"



beta\_message\_batch\_expired\_result: object { type } 

type: "expired"



beta\_message\_batch\_succeeded\_result: object { message, type } 



message: object { id, container, content, 9 more } 



id: string

Unique object identifier.

The format and length of IDs may change over time.



container: object { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: string

Identifier for the container used in this request

expires\_at: string

The time at which the container will expire.



skills: array of [BetaSkill](api/beta.md) { skill\_id, type, version } 

Skills loaded in the container

skill\_id: string

Skill ID



type: "anthropic" or "custom"

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

"anthropic"

"custom"

version: string

Skill version or 'latest' for most recent version



content: array of [BetaContentBlock](api/beta.md)

Content generated by the model.

This is an array of content blocks, each of which has a `type` that determines its shape.

Example:

```shiki
[{"type": "text", "text": "Hi, I'm Claude."}]
```



If the request input `messages` ended with an `assistant` turn, then the response `content` will continue directly from that last turn. You can use this to constrain the model's output.

For example, if the input `messages` were:

```shiki
[
  {"role": "user", "content": "What's the Greek name for Sun? (A) Sol (B) Helios (C) Sun"},
  {"role": "assistant", "content": "The best answer is ("}
]
```



Then the response `content` might be:

```shiki
[{"type": "text", "text": "B)"}]
```





beta\_text\_block: object { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"



beta\_thinking\_block: object { signature, thinking, type } 

signature: string

thinking: string

type: "thinking"



beta\_redacted\_thinking\_block: object { data, type } 

data: string

type: "redacted\_thinking"



beta\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

type: "tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_server\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]



name: "advisor" or "web\_search" or "web\_fetch" or 5 more

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: "server\_tool\_use"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_search\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  or array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 



beta\_web\_search\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "max\_uses\_exceeded" or 3 more

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: "web\_search\_tool\_result\_error"



union\_member\_1: array of [BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: string

page\_age: string

title: string

type: "web\_search\_result"

url: string

tool\_use\_id: string

type: "web\_search\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_web\_fetch\_tool\_result\_block: object { content, tool\_use\_id, type, caller } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  or [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 



beta\_web\_fetch\_tool\_result\_error\_block: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "url\_too\_long" or "url\_not\_allowed" or 6 more

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: "web\_fetch\_tool\_result\_error"



beta\_web\_fetch\_block: object { content, retrieved\_at, type, url } 



content: object { citations, source, title, type } 



citations: object { enabled } 

Citation configuration for the document

enabled: boolean



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  or [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 



beta\_base64\_pdf\_source: object { data, media\_type, type } 

data: string

media\_type: "application/pdf"

type: "base64"



beta\_plain\_text\_source: object { data, media\_type, type } 

data: string

media\_type: "text/plain"

type: "text"

title: string

The title of the document

type: "document"

retrieved\_at: string

ISO 8601 timestamp when the content was retrieved

type: "web\_fetch\_result"

url: string

Fetched content URL

tool\_use\_id: string

type: "web\_fetch\_tool\_result"



caller: optional [BetaDirectCaller](api/beta.md) { type }  or [BetaServerToolCaller](api/beta.md) { tool\_id, type }  or [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.



beta\_direct\_caller: object { type } 

Tool invocation directly from the model.

type: "direct"



beta\_server\_tool\_caller: object { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: string

type: "code\_execution\_20250825"



beta\_server\_tool\_caller\_20260120: object { tool\_id, type } 

tool\_id: string

type: "code\_execution\_20260120"



beta\_advisor\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  or [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  or [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 



beta\_advisor\_tool\_result\_error: object { error\_code, type } 



error\_code: "max\_uses\_exceeded" or "prompt\_too\_long" or "too\_many\_requests" or 4 more

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: "advisor\_tool\_result\_error"



beta\_advisor\_result\_block: object { stop\_reason, text, type } 

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: string

type: "advisor\_result"



beta\_advisor\_redacted\_result\_block: object { encrypted\_content, stop\_reason, type } 

encrypted\_content: string

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: string

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: "advisor\_redacted\_result"

tool\_use\_id: string

type: "advisor\_tool\_result"



beta\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  or [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



beta\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: "code\_execution\_tool\_result\_error"



beta\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "code\_execution\_result"



beta\_encrypted\_code\_execution\_result\_block: object { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: array of [BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "code\_execution\_output"

encrypted\_stdout: string

return\_code: number

stderr: string

type: "encrypted\_code\_execution\_result"

tool\_use\_id: string

type: "code\_execution\_tool\_result"



beta\_bash\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  or [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 



beta\_bash\_code\_execution\_tool\_result\_error: object { error\_code, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: "bash\_code\_execution\_tool\_result\_error"



beta\_bash\_code\_execution\_result\_block: object { content, return\_code, stderr, 2 more } 



content: array of [BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } 

file\_id: string

type: "bash\_code\_execution\_output"

return\_code: number

stderr: string

stdout: string

type: "bash\_code\_execution\_result"

tool\_use\_id: string

type: "bash\_code\_execution\_tool\_result"



beta\_text\_editor\_code\_execution\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  or [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  or [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 



beta\_text\_editor\_code\_execution\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or 2 more

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: string

type: "text\_editor\_code\_execution\_tool\_result\_error"



beta\_text\_editor\_code\_execution\_view\_result\_block: object { content, file\_type, num\_lines, 3 more } 

content: string



file\_type: "text" or "image" or "pdf"

"text"

"image"

"pdf"

num\_lines: number

start\_line: number

total\_lines: number

type: "text\_editor\_code\_execution\_view\_result"



beta\_text\_editor\_code\_execution\_create\_result\_block: object { is\_file\_update, type } 

is\_file\_update: boolean

type: "text\_editor\_code\_execution\_create\_result"



beta\_text\_editor\_code\_execution\_str\_replace\_result\_block: object { lines, new\_lines, new\_start, 3 more } 

lines: array of string

new\_lines: number

new\_start: number

old\_lines: number

old\_start: number

type: "text\_editor\_code\_execution\_str\_replace\_result"

tool\_use\_id: string

type: "text\_editor\_code\_execution\_tool\_result"



beta\_tool\_search\_tool\_result\_block: object { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  or [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 



beta\_tool\_search\_tool\_result\_error: object { error\_code, error\_message, type } 



error\_code: "invalid\_tool\_input" or "unavailable" or "too\_many\_requests" or "execution\_time\_exceeded"

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: string

type: "tool\_search\_tool\_result\_error"



beta\_tool\_search\_tool\_search\_result\_block: object { tool\_references, type } 



tool\_references: array of [BetaToolReferenceBlock](api/beta.md) { tool\_name, type } 

tool\_name: string

type: "tool\_reference"

type: "tool\_search\_tool\_search\_result"

tool\_use\_id: string

type: "tool\_search\_tool\_result"



beta\_mcp\_tool\_use\_block: object { id, input, name, 2 more } 

id: string

input: map[unknown]

name: string

The name of the MCP tool

server\_name: string

The name of the MCP server

type: "mcp\_tool\_use"



beta\_mcp\_tool\_result\_block: object { content, is\_error, tool\_use\_id, type } 



content: string or array of [BetaTextBlock](api/beta.md) { citations, text, type } 

union\_member\_0: string



beta\_mcp\_tool\_result\_block\_content: array of [BetaTextBlock](api/beta.md) { citations, text, type } 



citations: array of [BetaTextCitation](api/beta.md)

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.



beta\_citation\_char\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_char\_index: number

file\_id: string

start\_char\_index: number

type: "char\_location"



beta\_citation\_page\_location: object { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: string

document\_index: number

document\_title: string

end\_page\_number: number

file\_id: string

start\_page\_number: number

type: "page\_location"



beta\_citation\_content\_block\_location: object { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: number

document\_title: string



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

type: "content\_block\_location"



beta\_citations\_web\_search\_result\_location: object { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: string

encrypted\_index: string

title: string

type: "web\_search\_result\_location"

url: string



beta\_citation\_search\_result\_location: object { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: string

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: number

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: number

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

source: string

start\_block\_index: number

0-based index of the first cited block in the source's `content` array.

title: string

type: "search\_result\_location"

text: string

type: "text"

is\_error: boolean

tool\_use\_id: string

type: "mcp\_tool\_result"



beta\_container\_upload\_block: object { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: string

type: "container\_upload"



beta\_compaction\_block: object { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: string

Summary of compacted content, or null if compaction failed

encrypted\_content: string

Opaque metadata from prior compaction, to be round-tripped verbatim

type: "compaction"



beta\_fallback\_block: object { from, to, trigger, type } 

Marks the point in `content` where one model's output gives way to the next.

One block appears per hop where a preceding model actually ran this turn and
declined. A turn where no preceding model ran and declined has no such
boundary and carries no block — the signal for whether a fallback model
served the response is the presence of a `fallback_message` entry in
`usage.iterations`, not this block.

The block is treated like a server-tool content block for streaming: it
arrives via the standard `content_block_start` / `content_block_stop`
pair and carries no deltas.



from: object { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



to: object { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



trigger: object { category, type } 

What caused the `from` model to hand over at this hop.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

type: "refusal"

type: "fallback"



context\_management: object { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: array of [BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  or [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

List of context management edits that were applied.



beta\_clear\_tool\_uses\_20250919\_edit\_response: object { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_tool\_uses: number

Number of tool uses that were cleared.

type: "clear\_tool\_uses\_20250919"

The type of context management edit applied.



beta\_clear\_thinking\_20251015\_edit\_response: object { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: number

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: number

Number of thinking turns that were cleared.

type: "clear\_thinking\_20251015"

The type of context management edit applied.



diagnostics: object { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  or 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.



beta\_cache\_miss\_model\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "model\_changed"



beta\_cache\_miss\_system\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "system\_changed"



beta\_cache\_miss\_tools\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "tools\_changed"



beta\_cache\_miss\_messages\_changed: object { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: number

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: "messages\_changed"



beta\_cache\_miss\_previous\_message\_not\_found: object { type } 

type: "previous\_message\_not\_found"



beta\_cache\_miss\_unavailable: object { type } 

type: "unavailable"



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks



role: "assistant"

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: object { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: "cyber" or "bio" or "frontier\_llm" or "reasoning\_extraction"

The policy category that triggered a refusal.

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"



explanation: string

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: string

Opaque code that refunds the cache-miss cost when retrying this refused
request on the fallback model. Pass it as `fallback_credit_token` on the
retry request. Expires 5 minutes after the refusal.

The retry is sent either with the same request body (`system`, `messages`,
`tools`, and other render-shaping fields), or with the same body plus one
appended `assistant` message whose content is the partial text (with any
trailing whitespace stripped from the final text block) and paired
server-tool blocks from this refusal — which also authorizes that
appended turn as an assistant-prefill continuation on models that otherwise
disallow prefill. A token minted mid-server-tool-loop whose partial content
was continuable may only be redeemed the second way — if a same-body retry
is rejected with a 400 saying the token must be redeemed by continuing the
partial response, retry the second way instead. Either way: same workspace,
same platform; a mismatch is a 400. Resending a token for an already-warm
prefix is permitted but yields no additional credit.

`null` when the refused model isn't eligible for a fallback credit.



fallback\_has\_prefill\_claim: boolean

Whether the accompanying `fallback_credit_token` may be redeemed with the
appended-assistant retry form. Only set when `fallback_credit_token` is
present.

`true`: retry by resending the same request body plus one appended
`assistant` message whose content is this response's `content` with any
trailing whitespace stripped from the final text block and unpaired
`tool_use` blocks omitted (the same appended-turn shape described on
`fallback_credit_token`), with the token attached. `false`: retry by
resending the original request body unchanged, with the token attached —
the appended-assistant form is not available for this refusal (no
continuable partial content, or the request uses `output_format` or a
`tool_choice` that forces tool use). One exception: when the request used
`output_format` or a forced `tool_choice` and the refusal arrived after
server tools (including MCP connector tools) had already executed, the
token may not be redeemable by either retry form; if the exact-body retry
is then rejected with a 400 saying the token must be redeemed by
continuing the partial response, discard the token and retry without it.

Advisory: if an appended-assistant retry is rejected with a 400 despite
`true`, fall back to resending the original request body with the token.

recommended\_model: string

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: "refusal"



stop\_reason: "end\_turn" or "max\_tokens" or "stop\_sequence" or 5 more

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: string

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: "message"

Object type.

For Messages, this is always `"message"`.



usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

inference\_geo: string

The geographic region where inference was performed for this request.

input\_tokens: number

The number of input tokens which were used.



iterations: array of [BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  or [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  or [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops



beta\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "message"

Usage for a sampling iteration



beta\_compaction\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.

output\_tokens: number

The number of output tokens which were used.

type: "compaction"

Usage for a compaction iteration



beta\_advisor\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "advisor\_message"

Usage for an advisor sub-inference iteration



beta\_fallback\_message\_iteration\_usage: object { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: object { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: number

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: number

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: number

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: number

The number of input tokens read from the cache.

input\_tokens: number

The number of input tokens which were used.



model: "claude-fable-5" or "claude-mythos-5" or "claude-opus-4-8" or 12 more or string

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

"claude-mythos-5"

Most capable model for cybersecurity and biology research

"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

"claude-sonnet-4-6"

Best combination of speed and intelligence

"claude-haiku-4-5"

Fastest model with near-frontier intelligence

"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

"claude-sonnet-4-5"

High-performance model for agents and coding

"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

"claude-opus-4-1"

Exceptional model for specialized complex tasks

"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

output\_tokens: number

The number of output tokens which were used.

type: "fallback\_message"

Usage for the fallback-model attempt that served the response

output\_tokens: number

The number of output tokens which were used.



output\_tokens\_details: object { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: number

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.



server\_tool\_use: object { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: number

The number of web fetch tool requests.

web\_search\_requests: number

The number of web search tool requests.



service\_tier: "standard" or "priority" or "batch"

If the request used the priority, standard, or batch tier.

"standard"

"priority"

"batch"



speed: "standard" or "fast"

The inference speed mode used for this request.

"standard"

"fast"

type: "succeeded"

---

*Copyright © Anthropic. All rights reserved.*
