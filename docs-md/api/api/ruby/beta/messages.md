# Messages

Copy page



Ruby

# Messages

##### [Create a Message](api/beta/messages/create.md)

beta.messages.create(\*\*kwargs) -> [BetaMessage](api/beta.md) { id, container, content, 9 more }

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

beta.messages.count\_tokens(\*\*kwargs) -> [BetaMessageTokensCount](api/beta.md) { context\_management, input\_tokens }

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result



class BetaAdvisorRedactedResultBlockParam { encrypted\_content, type, stop\_reason } 

encrypted\_content: String

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: :advisor\_redacted\_result

stop\_reason: String



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorResultBlockParam { text, type, stop\_reason } 

text: String

type: :advisor\_result

stop\_reason: String



class BetaAdvisorTool20260301 { model, name, type, 7 more } 



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



name: :advisor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :advisor\_20260301



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caching: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_tokens: Integer

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaAdvisorToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaAdvisorToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlockParam](api/beta.md) { text, type, stop\_reason }  | [BetaAdvisorRedactedResultBlockParam](api/beta.md) { encrypted\_content, type, stop\_reason } 

One of the following:



class BetaAdvisorToolResultErrorParam { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlockParam { text, type, stop\_reason } 

text: String

type: :advisor\_result

stop\_reason: String



class BetaAdvisorRedactedResultBlockParam { encrypted\_content, type, stop\_reason } 

encrypted\_content: String

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: :advisor\_redacted\_result

stop\_reason: String

tool\_use\_id: String

type: :advisor\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorToolResultErrorParam { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAllThinkingTurns { type } 

type: :all



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaBashCodeExecutionOutputBlock { file\_id, type } 

file\_id: String

type: :bash\_code\_execution\_output



class BetaBashCodeExecutionOutputBlockParam { file\_id, type } 

file\_id: String

type: :bash\_code\_execution\_output



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result



class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaCacheControlEphemeral { type, ttl } 

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaCacheCreation { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.



class BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :messages\_changed



class BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :model\_changed



class BetaCacheMissPreviousMessageNotFound { type } 

type: :previous\_message\_not\_found



class BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :system\_changed



class BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :tools\_changed



class BetaCacheMissUnavailable { type } 

type: :unavailable



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationConfig { enabled } 

enabled: bool



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationsConfigParam { enabled } 

enabled: bool



class BetaCitationsDelta { citation, type } 



citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

type: :citations\_delta



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaClearThinking20251015Edit { type, keep } 

type: :clear\_thinking\_20251015



keep: [BetaThinkingTurns](api/beta.md) { type, value }  | [BetaAllThinkingTurns](api/beta.md) { type }  | :all

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



class BetaThinkingTurns { type, value } 

type: :thinking\_turns

value: Integer



class BetaAllThinkingTurns { type } 

type: :all

Keep = :all



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



class BetaClearToolUses20250919Edit { type, clear\_at\_least, clear\_tool\_inputs, 3 more } 

type: :clear\_tool\_uses\_20250919



clear\_at\_least: [BetaInputTokensClearAtLeast](api/beta.md) { type, value } 

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: :input\_tokens

value: Integer



clear\_tool\_inputs: bool | Array[String]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

UnionMember0 = bool

UnionMember1 = Array[String]

exclude\_tools: Array[String]

Tool names whose uses are preserved from clearing



keep: [BetaToolUsesKeep](api/beta.md) { type, value } 

Number of tool uses to retain in the conversation

type: :tool\_uses

value: Integer



trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }  | [BetaToolUsesTrigger](api/beta.md) { type, value } 

Condition that triggers the context management strategy

One of the following:



class BetaInputTokensTrigger { type, value } 

type: :input\_tokens

value: Integer



class BetaToolUsesTrigger { type, value } 

type: :tool\_uses

value: Integer



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaCodeExecutionOutputBlock { file\_id, type } 

file\_id: String

type: :code\_execution\_output



class BetaCodeExecutionOutputBlockParam { file\_id, type } 

file\_id: String

type: :code\_execution\_output



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaCodeExecutionTool20250522 { name, type, allowed\_callers, 3 more } 



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250522



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250825 { name, type, allowed\_callers, 3 more } 



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250825



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260120 { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260120



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260521 { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence.



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260521



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



BetaCodeExecutionToolResultBlockContent = [BetaCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more }  | [BetaEncryptedCodeExecutionResultBlock](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result



class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



BetaCodeExecutionToolResultBlockParamContent = [BetaCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more }  | [BetaEncryptedCodeExecutionResultBlockParam](api/beta.md) { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



BetaCodeExecutionToolResultErrorCode = :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded



class BetaCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCompact20260112Edit { type, instructions, pause\_after\_compaction, trigger } 

Automatically compact older context when reaching the configured trigger threshold.

type: :compact\_20260112

instructions: String

Additional instructions for summarization.

pause\_after\_compaction: bool

Whether to pause after compaction and return the compaction block to the user.



trigger: [BetaInputTokensTrigger](api/beta.md) { type, value } 

When to trigger compaction. Defaults to 150000 input tokens.

type: :input\_tokens

value: Integer



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaCompactionBlockParam { type, cache\_control, content, encrypted\_content } 

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: :compaction



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

content: String

Summary of previously compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaCompactionContentBlockDelta { content, encrypted\_content, type } 

content: String

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction\_delta



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaContainer { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



class BetaContainerParams { id, skills } 

Container parameters with skills to be loaded.

id: String

Container id



skills: Array[[BetaSkillParams](api/beta.md) { skill\_id, type, version } ]

List of skills to load in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaContainerUploadBlockParam { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



BetaContentBlock = [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 14 more

Response model for a file uploaded to the container.

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback



BetaContentBlockParam = [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more }  | 19 more

Regular text content.

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaRequestDocumentBlock { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String



class BetaSearchResultBlockParam { content, source, title, 3 more } 



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool



class BetaThinkingBlockParam { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlockParam { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: String

type: :tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

One of the following:

String = String



Content = Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaSearchResultBlockParam { content, source, title, 3 more } 



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool



class BetaRequestDocumentBlock { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String



class BetaToolReferenceBlockParam { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

is\_error: bool



class BetaServerToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

One of the following:



ResultBlock = Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String



class BetaWebSearchToolRequestError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  | [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at } 

One of the following:



class BetaWebFetchToolResultErrorBlockParam { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlockParam { content, type, url, retrieved\_at } 



content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaAdvisorToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlockParam](api/beta.md) { text, type, stop\_reason }  | [BetaAdvisorRedactedResultBlockParam](api/beta.md) { encrypted\_content, type, stop\_reason } 

One of the following:



class BetaAdvisorToolResultErrorParam { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlockParam { text, type, stop\_reason } 

text: String

type: :advisor\_result

stop\_reason: String



class BetaAdvisorRedactedResultBlockParam { encrypted\_content, type, stop\_reason } 

encrypted\_content: String

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: :advisor\_redacted\_result

stop\_reason: String

tool\_use\_id: String

type: :advisor\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaBashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaTextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String



class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer



class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more } 

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultErrorParam { error\_code, type, error\_message } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

error\_message: String



class BetaToolSearchToolSearchResultBlockParam { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaMCPToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]

name: String

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: String

type: :mcp\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

One of the following:

String = String



BetaMCPToolResultBlockParamContent = Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

is\_error: bool



class BetaContainerUploadBlockParam { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaCompactionBlockParam { type, cache\_control, content, encrypted\_content } 

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: :compaction



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

content: String

Summary of previously compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaMidConversationSystemBlockParam { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

System instruction text blocks.

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

type: :mid\_conv\_system



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaFallbackBlockParam { from, to, type, trigger } 

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

from: [BetaFallbackInfoParam](api/beta.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfoParam](api/beta.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

type: :fallback

trigger: untyped

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



BetaContentBlockSourceContent = [BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control } 

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaContextManagementConfig { edits } 



edits: Array[[BetaClearToolUses20250919Edit](api/beta.md) { type, clear\_at\_least, clear\_tool\_inputs, 3 more }  | [BetaClearThinking20251015Edit](api/beta.md) { type, keep }  | [BetaCompact20260112Edit](api/beta.md) { type, instructions, pause\_after\_compaction, trigger } ]

List of context management edits to apply

One of the following:



class BetaClearToolUses20250919Edit { type, clear\_at\_least, clear\_tool\_inputs, 3 more } 

type: :clear\_tool\_uses\_20250919



clear\_at\_least: [BetaInputTokensClearAtLeast](api/beta.md) { type, value } 

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: :input\_tokens

value: Integer



clear\_tool\_inputs: bool | Array[String]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

UnionMember0 = bool

UnionMember1 = Array[String]

exclude\_tools: Array[String]

Tool names whose uses are preserved from clearing



keep: [BetaToolUsesKeep](api/beta.md) { type, value } 

Number of tool uses to retain in the conversation

type: :tool\_uses

value: Integer



trigger: [BetaInputTokensTrigger](api/beta.md) { type, value }  | [BetaToolUsesTrigger](api/beta.md) { type, value } 

Condition that triggers the context management strategy

One of the following:



class BetaInputTokensTrigger { type, value } 

type: :input\_tokens

value: Integer



class BetaToolUsesTrigger { type, value } 

type: :tool\_uses

value: Integer



class BetaClearThinking20251015Edit { type, keep } 

type: :clear\_thinking\_20251015



keep: [BetaThinkingTurns](api/beta.md) { type, value }  | [BetaAllThinkingTurns](api/beta.md) { type }  | :all

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



class BetaThinkingTurns { type, value } 

type: :thinking\_turns

value: Integer



class BetaAllThinkingTurns { type } 

type: :all

Keep = :all



class BetaCompact20260112Edit { type, instructions, pause\_after\_compaction, trigger } 

Automatically compact older context when reaching the configured trigger threshold.

type: :compact\_20260112

instructions: String

Additional instructions for summarization.

pause\_after\_compaction: bool

Whether to pause after compaction and return the compaction block to the user.



trigger: [BetaInputTokensTrigger](api/beta.md) { type, value } 

When to trigger compaction. Defaults to 150000 input tokens.

type: :input\_tokens

value: Integer



class BetaContextManagementResponse { applied\_edits } 



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



class BetaCountTokensContextManagementResponse { original\_input\_tokens } 

original\_input\_tokens: Integer

The original token count before context management was applied



class BetaDiagnostics { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :model\_changed



class BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :system\_changed



class BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :tools\_changed



class BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :messages\_changed



class BetaCacheMissPreviousMessageNotFound { type } 

type: :previous\_message\_not\_found



class BetaCacheMissUnavailable { type } 

type: :unavailable



class BetaDiagnosticsParam { previous\_message\_id } 

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

previous\_message\_id: String

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaDocumentBlock { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result



class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback



class BetaFallbackBlockParam { from, to, type, trigger } 

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

from: [BetaFallbackInfoParam](api/beta.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfoParam](api/beta.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

type: :fallback

trigger: untyped

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



class BetaFallbackInfo { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



class BetaFallbackInfoParam { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response



class BetaFallbackParam { model, max\_tokens, output\_config, 2 more } 

One entry in the `fallbacks` chain on a `/v1/messages` request.

`model` is required. The four override fields (`max_tokens`, `thinking`,
`output_config`, and `speed`) replace the corresponding top-level field
for this attempt only and are validated as if the request were made to
`model`. Any other key is rejected at parse time.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

max\_tokens: Integer



output\_config: [BetaOutputConfig](api/beta.md) { effort, format\_, task\_budget } 



effort: :low | :medium | :high | 2 more

All possible effort levels.

One of the following:

:low

:medium

:high

:xhigh

:max



format\_: [BetaJSONOutputFormat](api/beta.md) { schema, type } 

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema



task\_budget: [BetaTokenTaskBudget](api/beta.md) { total, type, remaining } 

User-configurable total token budget across contexts.

total: Integer

Total token budget across all contexts in the session.

type: :tokens

The budget type. Currently only 'tokens' is supported.

remaining: Integer

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



speed: :standard | :fast

One of the following:

:standard

:fast



thinking: [BetaThinkingConfigEnabled](api/beta.md) { budget\_tokens, type, display\_ }  | [BetaThinkingConfigDisabled](api/beta.md) { type }  | [BetaThinkingConfigAdaptive](api/beta.md) { type, display\_ } 

One of the following:



class BetaThinkingConfigEnabled { budget\_tokens, type, display\_ } 



budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled



display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

:summarized

:omitted



class BetaThinkingConfigDisabled { type } 

type: :disabled



class BetaThinkingConfigAdaptive { type, display\_ } 

type: :adaptive



display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

:summarized

:omitted



class BetaFallbackRefusalTrigger { category, type } 

The `from` model declined for policy reasons.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaInputJSONDelta { partial\_json, type } 

partial\_json: String

type: :input\_json\_delta



class BetaInputTokensClearAtLeast { type, value } 

type: :input\_tokens

value: Integer



class BetaInputTokensTrigger { type, value } 

type: :input\_tokens

value: Integer



BetaIterationsUsage = Array[[BetaMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  | [BetaCompactionIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more }  | [BetaAdvisorMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more }  | [BetaFallbackMessageIterationUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } ]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response



class BetaJSONOutputFormat { schema, type } 

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema



class BetaMCPToolConfig { defer\_loading, enabled } 

Configuration for a specific tool in an MCP toolset.

defer\_loading: bool

enabled: bool



class BetaMCPToolDefaultConfig { defer\_loading, enabled } 

Default configuration for tools in an MCP toolset.

defer\_loading: bool

enabled: bool



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]

name: String

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaMCPToolset { mcp\_server\_name, type, cache\_control, 2 more } 

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: String

Name of the MCP server to configure tools for

type: :mcp\_toolset



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



configs: Hash[Symbol, [BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: bool

enabled: bool



default\_config: [BetaMCPToolDefaultConfig](api/beta.md) { defer\_loading, enabled } 

Default configuration applied to all tools from this server

defer\_loading: bool

enabled: bool



class BetaMemoryTool20250818 { name, type, allowed\_callers, 4 more } 



name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :memory\_20250818



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



BetaMemoryTool20250818Command = [BetaMemoryTool20250818ViewCommand](api/beta.md) { command, path, view\_range }  | [BetaMemoryTool20250818CreateCommand](api/beta.md) { command, file\_text, path }  | [BetaMemoryTool20250818StrReplaceCommand](api/beta.md) { command, new\_str, old\_str, path }  | 3 more

One of the following:



class BetaMemoryTool20250818ViewCommand { command, path, view\_range } 

command: :view

Command type identifier

path: String

Path to directory or file to view

view\_range: Array[Integer]

Optional line range for viewing specific lines



class BetaMemoryTool20250818CreateCommand { command, file\_text, path } 

command: :create

Command type identifier

file\_text: String

Content to write to the file

path: String

Path where the file should be created



class BetaMemoryTool20250818StrReplaceCommand { command, new\_str, old\_str, path } 

command: :str\_replace

Command type identifier

new\_str: String

Text to replace with

old\_str: String

Text to search for and replace

path: String

Path to the file where text should be replaced



class BetaMemoryTool20250818InsertCommand { command, insert\_line, insert\_text, path } 

command: :insert

Command type identifier

insert\_line: Integer

Line number where text should be inserted

insert\_text: String

Text to insert at the specified line

path: String

Path to the file where text should be inserted



class BetaMemoryTool20250818DeleteCommand { command, path } 

command: :delete

Command type identifier

path: String

Path to the file or directory to delete



class BetaMemoryTool20250818RenameCommand { command, new\_path, old\_path } 

command: :rename

Command type identifier

new\_path: String

New path for the file or directory

old\_path: String

Current path of the file or directory



class BetaMemoryTool20250818CreateCommand { command, file\_text, path } 

command: :create

Command type identifier

file\_text: String

Content to write to the file

path: String

Path where the file should be created



class BetaMemoryTool20250818DeleteCommand { command, path } 

command: :delete

Command type identifier

path: String

Path to the file or directory to delete



class BetaMemoryTool20250818InsertCommand { command, insert\_line, insert\_text, path } 

command: :insert

Command type identifier

insert\_line: Integer

Line number where text should be inserted

insert\_text: String

Text to insert at the specified line

path: String

Path to the file where text should be inserted



class BetaMemoryTool20250818RenameCommand { command, new\_path, old\_path } 

command: :rename

Command type identifier

new\_path: String

New path for the file or directory

old\_path: String

Current path of the file or directory



class BetaMemoryTool20250818StrReplaceCommand { command, new\_str, old\_str, path } 

command: :str\_replace

Command type identifier

new\_str: String

Text to replace with

old\_str: String

Text to search for and replace

path: String

Path to the file where text should be replaced



class BetaMemoryTool20250818ViewCommand { command, path, view\_range } 

command: :view

Command type identifier

path: String

Path to directory or file to view

view\_range: Array[Integer]

Optional line range for viewing specific lines



class BetaMessage { id, container, content, 9 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [BetaContainer](api/beta.md) { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



content: Array[[BetaContentBlock](api/beta.md)]

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

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback



context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



diagnostics: [BetaDiagnostics](api/beta.md) { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :model\_changed



class BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :system\_changed



class BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :tools\_changed



class BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :messages\_changed



class BetaCacheMissPreviousMessageNotFound { type } 

type: :previous\_message\_not\_found



class BetaCacheMissUnavailable { type } 

type: :unavailable



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch



speed: :standard | :fast

The inference speed mode used for this request.

One of the following:

:standard

:fast



class BetaMessageDeltaUsage { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 4 more } 

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

input\_tokens: Integer

The cumulative number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The cumulative number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaMessageParam { content, role } 



content: String | Array[[BetaContentBlockParam](api/beta.md)]

One of the following:

String = String



UnionMember1 = Array[[BetaContentBlockParam](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaRequestDocumentBlock { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String



class BetaSearchResultBlockParam { content, source, title, 3 more } 



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool



class BetaThinkingBlockParam { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlockParam { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: String

type: :tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

One of the following:

String = String



Content = Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaSearchResultBlockParam { content, source, title, 3 more } 



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool



class BetaRequestDocumentBlock { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String



class BetaToolReferenceBlockParam { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

is\_error: bool



class BetaServerToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

One of the following:



ResultBlock = Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String



class BetaWebSearchToolRequestError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  | [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at } 

One of the following:



class BetaWebFetchToolResultErrorBlockParam { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlockParam { content, type, url, retrieved\_at } 



content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaAdvisorToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlockParam](api/beta.md) { text, type, stop\_reason }  | [BetaAdvisorRedactedResultBlockParam](api/beta.md) { encrypted\_content, type, stop\_reason } 

One of the following:



class BetaAdvisorToolResultErrorParam { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlockParam { text, type, stop\_reason } 

text: String

type: :advisor\_result

stop\_reason: String



class BetaAdvisorRedactedResultBlockParam { encrypted\_content, type, stop\_reason } 

encrypted\_content: String

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: :advisor\_redacted\_result

stop\_reason: String

tool\_use\_id: String

type: :advisor\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaCodeExecutionToolResultBlockParamContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlockParam { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaBashCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaBashCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlockParam](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultErrorParam { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlockParam { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlockParam](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaTextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String



class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer



class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more } 

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultErrorParam { error\_code, type, error\_message } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

error\_message: String



class BetaToolSearchToolSearchResultBlockParam { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaMCPToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]

name: String

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: String

type: :mcp\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

One of the following:

String = String



BetaMCPToolResultBlockParamContent = Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

is\_error: bool



class BetaContainerUploadBlockParam { file\_id, type, cache\_control } 

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: String

type: :container\_upload



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaCompactionBlockParam { type, cache\_control, content, encrypted\_content } 

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: :compaction



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

content: String

Summary of previously compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaMidConversationSystemBlockParam { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

System instruction text blocks.

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

type: :mid\_conv\_system



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaFallbackBlockParam { from, to, type, trigger } 

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

from: [BetaFallbackInfoParam](api/beta.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfoParam](api/beta.md) { model } 

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

type: :fallback

trigger: untyped

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



role: :user | :assistant | :system

One of the following:

:user

:assistant

:system



class BetaMessageTokensCount { context\_management, input\_tokens } 



context\_management: [BetaCountTokensContextManagementResponse](api/beta.md) { original\_input\_tokens } 

Information about context management applied to the message.

original\_input\_tokens: Integer

The original token count before context management was applied

input\_tokens: Integer

The total number of tokens across the provided list of messages, system prompt, and tools.



class BetaMetadata { user\_id } 



user\_id: String

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



class BetaMidConversationSystemBlockParam { content, type, cache\_control } 

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

System instruction text blocks.

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

type: :mid\_conv\_system



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaOutputConfig { effort, format\_, task\_budget } 



effort: :low | :medium | :high | 2 more

All possible effort levels.

One of the following:

:low

:medium

:high

:xhigh

:max



format\_: [BetaJSONOutputFormat](api/beta.md) { schema, type } 

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Hash[Symbol, untyped]

The JSON schema of the format

type: :json\_schema



task\_budget: [BetaTokenTaskBudget](api/beta.md) { total, type, remaining } 

User-configurable total token budget across contexts.

total: Integer

Total token budget across all contexts in the session.

type: :tokens

The budget type. Currently only 'tokens' is supported.

remaining: Integer

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



class BetaOutputTokensDetails { thinking\_tokens } 



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



BetaRawContentBlockDelta = [BetaTextDelta](api/beta.md) { text, type }  | [BetaInputJSONDelta](api/beta.md) { partial\_json, type }  | [BetaCitationsDelta](api/beta.md) { citation, type }  | 3 more

One of the following:



class BetaTextDelta { text, type } 

text: String

type: :text\_delta



class BetaInputJSONDelta { partial\_json, type } 

partial\_json: String

type: :input\_json\_delta



class BetaCitationsDelta { citation, type } 



citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

type: :citations\_delta



class BetaThinkingDelta { estimated\_tokens, thinking, type } 

estimated\_tokens: Integer

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: String

type: :thinking\_delta



class BetaSignatureDelta { signature, type } 

signature: String

type: :signature\_delta



class BetaCompactionContentBlockDelta { content, encrypted\_content, type } 

content: String

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction\_delta



class BetaRawContentBlockDeltaEvent { delta, index, type } 



delta: [BetaRawContentBlockDelta](api/beta.md)

One of the following:



class BetaTextDelta { text, type } 

text: String

type: :text\_delta



class BetaInputJSONDelta { partial\_json, type } 

partial\_json: String

type: :input\_json\_delta



class BetaCitationsDelta { citation, type } 



citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

type: :citations\_delta



class BetaThinkingDelta { estimated\_tokens, thinking, type } 

estimated\_tokens: Integer

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: String

type: :thinking\_delta



class BetaSignatureDelta { signature, type } 

signature: String

type: :signature\_delta



class BetaCompactionContentBlockDelta { content, encrypted\_content, type } 

content: String

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction\_delta

index: Integer

type: :content\_block\_delta



class BetaRawContentBlockStartEvent { content\_block, index, type } 



content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 14 more

Response model for a file uploaded to the container.

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback

index: Integer

type: :content\_block\_start



class BetaRawContentBlockStopEvent { index, type } 

index: Integer

type: :content\_block\_stop



class BetaRawMessageDeltaEvent { context\_management, delta, type, usage } 



context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits } 

Information about context management strategies applied during the request



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



delta: Delta{ container, stop\_details, stop\_reason, stop\_sequence}



container: [BetaContainer](api/beta.md) { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



stop\_reason: [BetaStopReason](api/beta.md)

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

type: :message\_delta



usage: [BetaMessageDeltaUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 4 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

input\_tokens: Integer

The cumulative number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The cumulative number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



class BetaRawMessageStartEvent { message, type } 



message: [BetaMessage](api/beta.md) { id, container, content, 9 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [BetaContainer](api/beta.md) { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



content: Array[[BetaContentBlock](api/beta.md)]

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

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback



context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



diagnostics: [BetaDiagnostics](api/beta.md) { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :model\_changed



class BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :system\_changed



class BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :tools\_changed



class BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :messages\_changed



class BetaCacheMissPreviousMessageNotFound { type } 

type: :previous\_message\_not\_found



class BetaCacheMissUnavailable { type } 

type: :unavailable



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch



speed: :standard | :fast

The inference speed mode used for this request.

One of the following:

:standard

:fast

type: :message\_start



class BetaRawMessageStopEvent { type } 

type: :message\_stop



BetaRawMessageStreamEvent = [BetaRawMessageStartEvent](api/beta.md) { message, type }  | [BetaRawMessageDeltaEvent](api/beta.md) { context\_management, delta, type, usage }  | [BetaRawMessageStopEvent](api/beta.md) { type }  | 3 more

One of the following:



class BetaRawMessageStartEvent { message, type } 



message: [BetaMessage](api/beta.md) { id, container, content, 9 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [BetaContainer](api/beta.md) { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



content: Array[[BetaContentBlock](api/beta.md)]

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

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback



context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



diagnostics: [BetaDiagnostics](api/beta.md) { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :model\_changed



class BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :system\_changed



class BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :tools\_changed



class BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :messages\_changed



class BetaCacheMissPreviousMessageNotFound { type } 

type: :previous\_message\_not\_found



class BetaCacheMissUnavailable { type } 

type: :unavailable



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch



speed: :standard | :fast

The inference speed mode used for this request.

One of the following:

:standard

:fast

type: :message\_start



class BetaRawMessageDeltaEvent { context\_management, delta, type, usage } 



context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits } 

Information about context management strategies applied during the request



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



delta: Delta{ container, stop\_details, stop\_reason, stop\_sequence}



container: [BetaContainer](api/beta.md) { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



stop\_reason: [BetaStopReason](api/beta.md)

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded

stop\_sequence: String

type: :message\_delta



usage: [BetaMessageDeltaUsage](api/beta.md) { cache\_creation\_input\_tokens, cache\_read\_input\_tokens, input\_tokens, 4 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Integer

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The cumulative number of input tokens read from the cache.

input\_tokens: Integer

The cumulative number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The cumulative number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



class BetaRawMessageStopEvent { type } 

type: :message\_stop



class BetaRawContentBlockStartEvent { content\_block, index, type } 



content\_block: [BetaTextBlock](api/beta.md) { citations, text, type }  | [BetaThinkingBlock](api/beta.md) { signature, thinking, type }  | [BetaRedactedThinkingBlock](api/beta.md) { data, type }  | 14 more

Response model for a file uploaded to the container.

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback

index: Integer

type: :content\_block\_start



class BetaRawContentBlockDeltaEvent { delta, index, type } 



delta: [BetaRawContentBlockDelta](api/beta.md)

One of the following:



class BetaTextDelta { text, type } 

text: String

type: :text\_delta



class BetaInputJSONDelta { partial\_json, type } 

partial\_json: String

type: :input\_json\_delta



class BetaCitationsDelta { citation, type } 



citation: [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

type: :citations\_delta



class BetaThinkingDelta { estimated\_tokens, thinking, type } 

estimated\_tokens: Integer

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: String

type: :thinking\_delta



class BetaSignatureDelta { signature, type } 

signature: String

type: :signature\_delta



class BetaCompactionContentBlockDelta { content, encrypted\_content, type } 

content: String

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction\_delta

index: Integer

type: :content\_block\_delta



class BetaRawContentBlockStopEvent { index, type } 

index: Integer

type: :content\_block\_stop



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaRedactedThinkingBlockParam { data, type } 

data: String

type: :redacted\_thinking



class BetaRefusalStopDetails { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



class BetaRequestDocumentBlock { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String



class BetaRequestMCPServerToolConfiguration { allowed\_tools, enabled } 

allowed\_tools: Array[String]

enabled: bool



class BetaRequestMCPServerURLDefinition { name, type, url, 2 more } 

name: String

type: :url

url: String

authorization\_token: String



tool\_configuration: [BetaRequestMCPServerToolConfiguration](api/beta.md) { allowed\_tools, enabled } 

allowed\_tools: Array[String]

enabled: bool



class BetaRequestMCPToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: String

type: :mcp\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

One of the following:

String = String



BetaMCPToolResultBlockParamContent = Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

is\_error: bool



class BetaSearchResultBlockParam { content, source, title, 3 more } 



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUsage { web\_fetch\_requests, web\_search\_requests } 

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaSignatureDelta { signature, type } 

signature: String

type: :signature\_delta



class BetaSkill { skill\_id, type, version } 

A skill that was loaded in a container (response model).

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



class BetaSkillParams { skill\_id, type, version } 

Specification for a skill to be loaded in a container (request model).

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



BetaStopReason = :end\_turn | :max\_tokens | :stop\_sequence | 5 more

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



BetaTextCitation = [BetaCitationCharLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationPageLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | [BetaCitationContentBlockLocation](api/beta.md) { cited\_text, document\_index, document\_title, 4 more }  | 2 more

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



BetaTextCitationParam = [BetaCitationCharLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | [BetaCitationPageLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | [BetaCitationContentBlockLocationParam](api/beta.md) { cited\_text, document\_index, document\_title, 3 more }  | 2 more

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaTextDelta { text, type } 

text: String

type: :text\_delta



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more } 

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaTextEditorCodeExecutionToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaTextEditorCodeExecutionViewResultBlockParam](api/beta.md) { content, file\_type, type, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlockParam](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlockParam](api/beta.md) { type, lines, new\_lines, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String



class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer



class BetaTextEditorCodeExecutionCreateResultBlockParam { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam { type, lines, new\_lines, 3 more } 

type: :text\_editor\_code\_execution\_str\_replace\_result

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionToolResultErrorParam { error\_code, type, error\_message } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

type: :text\_editor\_code\_execution\_tool\_result\_error

error\_message: String



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionViewResultBlockParam { content, file\_type, type, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

type: :text\_editor\_code\_execution\_view\_result

num\_lines: Integer

start\_line: Integer

total\_lines: Integer



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaThinkingBlockParam { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaThinkingConfigAdaptive { type, display\_ } 

type: :adaptive



display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

:summarized

:omitted



class BetaThinkingConfigDisabled { type } 

type: :disabled



class BetaThinkingConfigEnabled { budget\_tokens, type, display\_ } 



budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled



display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

:summarized

:omitted



BetaThinkingConfigParam = [BetaThinkingConfigEnabled](api/beta.md) { budget\_tokens, type, display\_ }  | [BetaThinkingConfigDisabled](api/beta.md) { type }  | [BetaThinkingConfigAdaptive](api/beta.md) { type, display\_ } 

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

One of the following:



class BetaThinkingConfigEnabled { budget\_tokens, type, display\_ } 



budget\_tokens: Integer

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](https://docs.claude.com/en/docs/build-with-claude/extended-thinking) for details.

minimum1024

type: :enabled



display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

:summarized

:omitted



class BetaThinkingConfigDisabled { type } 

type: :disabled



class BetaThinkingConfigAdaptive { type, display\_ } 

type: :adaptive



display\_: :summarized | :omitted

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

:summarized

:omitted



class BetaThinkingDelta { estimated\_tokens, thinking, type } 

estimated\_tokens: Integer

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: String

type: :thinking\_delta



class BetaThinkingTurns { type, value } 

type: :thinking\_turns

value: Integer



class BetaTokenTaskBudget { total, type, remaining } 

User-configurable total token budget across contexts.

total: Integer

Total token budget across all contexts in the session.

type: :tokens

The budget type. Currently only 'tokens' is supported.

remaining: Integer

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



class BetaTool { input\_schema, name, allowed\_callers, 7 more } 



input\_schema: InputSchema{ type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]



name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: bool

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

type: :custom



class BetaToolBash20241022 { name, type, allowed\_callers, 4 more } 



name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20241022



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolBash20250124 { name, type, allowed\_callers, 4 more } 



name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20250124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



BetaToolChoice = [BetaToolChoiceAuto](api/beta.md) { type, disable\_parallel\_tool\_use }  | [BetaToolChoiceAny](api/beta.md) { type, disable\_parallel\_tool\_use }  | [BetaToolChoiceTool](api/beta.md) { name, type, disable\_parallel\_tool\_use }  | [BetaToolChoiceNone](api/beta.md) { type } 

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



class BetaToolChoiceAuto { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: :auto



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class BetaToolChoiceAny { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: :any



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceTool { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceNone { type } 

The model will not be allowed to use tools.

type: :none



class BetaToolChoiceAny { type, disable\_parallel\_tool\_use } 

The model will use any available tools.

type: :any



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceAuto { type, disable\_parallel\_tool\_use } 

The model will automatically decide whether to use tools.

type: :auto



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class BetaToolChoiceNone { type } 

The model will not be allowed to use tools.

type: :none



class BetaToolChoiceTool { name, type, disable\_parallel\_tool\_use } 

The model will use the specified tool with `tool_choice.name`.

name: String

The name of the tool to use.

type: :tool



disable\_parallel\_tool\_use: bool

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolComputerUse20241022 { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.



name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20241022



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20250124 { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.



name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20250124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20251124 { display\_height\_px, display\_width\_px, name, 8 more } 

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.



name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20251124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: bool

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolReferenceBlock { tool\_name, type } 

tool\_name: String

type: :tool\_reference



class BetaToolReferenceBlockParam { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaToolResultBlockParam { tool\_use\_id, type, cache\_control, 2 more } 

tool\_use\_id: String

type: :tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



content: String | Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

One of the following:

String = String



Content = Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations }  | [BetaImageBlockParam](api/beta.md) { source, type, cache\_control }  | [BetaSearchResultBlockParam](api/beta.md) { content, source, title, 3 more }  | 2 more]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaSearchResultBlockParam { content, source, title, 3 more } 



content: Array[[BetaTextBlockParam](api/beta.md) { text, type, cache\_control, citations } ]

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

source: String

title: String

type: :search\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool



class BetaRequestDocumentBlock { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String



class BetaToolReferenceBlockParam { tool\_name, type, cache\_control } 

Tool reference block that can be included in tool\_result content.

tool\_name: String

type: :tool\_reference



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

is\_error: bool



class BetaToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more } 



name: :tool\_search\_tool\_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

One of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more } 



name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

One of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaToolSearchToolResultBlockParam { content, tool\_use\_id, type, cache\_control } 



content: [BetaToolSearchToolResultErrorParam](api/beta.md) { error\_code, type, error\_message }  | [BetaToolSearchToolSearchResultBlockParam](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultErrorParam { error\_code, type, error\_message } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

error\_message: String



class BetaToolSearchToolSearchResultBlockParam { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolResultErrorParam { error\_code, type, error\_message } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :tool\_search\_tool\_result\_error

error\_message: String



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result



class BetaToolSearchToolSearchResultBlockParam { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlockParam](api/beta.md) { tool\_name, type, cache\_control } ]

tool\_name: String

type: :tool\_reference



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :tool\_search\_tool\_search\_result



class BetaToolTextEditor20241022 { name, type, allowed\_callers, 4 more } 



name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20241022



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250124 { name, type, allowed\_callers, 4 more } 



name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250429 { name, type, allowed\_callers, 4 more } 



name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250429



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250728 { name, type, allowed\_callers, 5 more } 



name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250728



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: bool

When true, guarantees schema validation on tool names and inputs



BetaToolUnion = [BetaTool](api/beta.md) { input\_schema, name, allowed\_callers, 7 more }  | [BetaToolBash20241022](api/beta.md) { name, type, allowed\_callers, 4 more }  | [BetaToolBash20250124](api/beta.md) { name, type, allowed\_callers, 4 more }  | 21 more

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

One of the following:



class BetaTool { input\_schema, name, allowed\_callers, 7 more } 



input\_schema: InputSchema{ type, properties, required}

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: :object

properties: Hash[Symbol, untyped]

required: Array[String]



name: String

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description: String

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: bool

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs

type: :custom



class BetaToolBash20241022 { name, type, allowed\_callers, 4 more } 



name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20241022



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolBash20250124 { name, type, allowed\_callers, 4 more } 



name: :bash

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :bash\_20250124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250522 { name, type, allowed\_callers, 3 more } 



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250522



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250825 { name, type, allowed\_callers, 3 more } 



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20250825



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260120 { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260120



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260521 { name, type, allowed\_callers, 3 more } 

Code execution tool with REPL state persistence.



name: :code\_execution

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :code\_execution\_20260521



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20241022 { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.



name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20241022



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaMemoryTool20250818 { name, type, allowed\_callers, 4 more } 



name: :memory

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :memory\_20250818



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20250124 { display\_height\_px, display\_width\_px, name, 7 more } 

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.



name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20250124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20241022 { name, type, allowed\_callers, 4 more } 



name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20241022



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20251124 { display\_height\_px, display\_width\_px, name, 8 more } 

display\_height\_px: Integer

The height of the display in pixels.

display\_width\_px: Integer

The width of the display in pixels.



name: :computer

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :computer\_20251124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Integer

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: bool

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250124 { name, type, allowed\_callers, 4 more } 



name: :str\_replace\_editor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250124



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250429 { name, type, allowed\_callers, 4 more } 



name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250429



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250728 { name, type, allowed\_callers, 5 more } 



name: :str\_replace\_based\_edit\_tool

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :text\_editor\_20250728



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Array[Hash[Symbol, untyped]]

max\_characters: Integer

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaWebSearchTool20250305 { name, type, allowed\_callers, 7 more } 



name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20250305



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



user\_location: [BetaUserLocation](api/beta.md) { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20250910 { name, type, allowed\_callers, 8 more } 



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20250910



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaWebSearchTool20260209 { name, type, allowed\_callers, 7 more } 



name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20260209



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



user\_location: [BetaUserLocation](api/beta.md) { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20260209 { name, type, allowed\_callers, 8 more } 



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260209



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260309 { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260309



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

use\_cache: bool

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaAdvisorTool20260301 { model, name, type, 7 more } 



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



name: :advisor

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :advisor\_20260301



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caching: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_tokens: Integer

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolBm25\_20251119 { name, type, allowed\_callers, 3 more } 



name: :tool\_search\_tool\_bm25

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: :tool\_search\_tool\_bm25\_20251119 | :tool\_search\_tool\_bm25

One of the following:

:tool\_search\_tool\_bm25\_20251119

:tool\_search\_tool\_bm25



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolRegex20251119 { name, type, allowed\_callers, 3 more } 



name: :tool\_search\_tool\_regex

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: :tool\_search\_tool\_regex\_20251119 | :tool\_search\_tool\_regex

One of the following:

:tool\_search\_tool\_regex\_20251119

:tool\_search\_tool\_regex



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaMCPToolset { mcp\_server\_name, type, cache\_control, 2 more } 

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: String

Name of the MCP server to configure tools for

type: :mcp\_toolset



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



configs: Hash[Symbol, [BetaMCPToolConfig](api/beta.md) { defer\_loading, enabled } ]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: bool

enabled: bool



default\_config: [BetaMCPToolDefaultConfig](api/beta.md) { defer\_loading, enabled } 

Default configuration applied to all tools from this server

defer\_loading: bool

enabled: bool



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaToolUseBlockParam { id, input, name, 3 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaToolUsesKeep { type, value } 

type: :tool\_uses

value: Integer



class BetaToolUsesTrigger { type, value } 

type: :tool\_uses

value: Integer



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch



speed: :standard | :fast

The inference speed mode used for this request.

One of the following:

:standard

:fast



class BetaUserLocation { type, city, country, 2 more } 

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL



class BetaWebFetchBlockParam { content, type, url, retrieved\_at } 



content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved



class BetaWebFetchTool20250910 { name, type, allowed\_callers, 8 more } 



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20250910



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260209 { name, type, allowed\_callers, 8 more } 



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260209



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260309 { name, type, allowed\_callers, 9 more } 

Web fetch tool with use\_cache parameter for bypassing cached content.



name: :web\_fetch

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_fetch\_20260309



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

List of domains to allow fetching from

blocked\_domains: Array[String]

List of domains to block fetching from



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

Citations configuration for fetched documents. Citations are disabled by default.

enabled: bool

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Integer

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs

use\_cache: bool

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [BetaWebFetchToolResultErrorBlockParam](api/beta.md) { error\_code, type }  | [BetaWebFetchBlockParam](api/beta.md) { content, type, url, retrieved\_at } 

One of the following:



class BetaWebFetchToolResultErrorBlockParam { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlockParam { content, type, url, retrieved\_at } 



content: [BetaRequestDocumentBlock](api/beta.md) { source, type, cache\_control, 3 more } 



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type }  | [BetaContentBlockSource](api/beta.md) { content, type }  | 2 more

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text



class BetaContentBlockSource { content, type } 



content: String | Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:

String = String



BetaContentBlockSourceContent = Array[[BetaContentBlockSourceContent](api/beta.md)]

One of the following:



class BetaTextBlockParam { text, type, cache\_control, citations } 

text: String

type: :text



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: Array[[BetaTextCitationParam](api/beta.md)]

One of the following:



class BetaCitationCharLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocationParam { cited\_text, document\_index, document\_title, 3 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocationParam { cited\_text, document\_index, document\_title, 3 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationWebSearchResultLocationParam { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocationParam { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location



class BetaImageBlockParam { source, type, cache\_control } 



source: [BetaBase64ImageSource](api/beta.md) { data, media\_type, type }  | [BetaURLImageSource](api/beta.md) { type, url }  | [BetaFileImageSource](api/beta.md) { file\_id, type } 

One of the following:



class BetaBase64ImageSource { data, media\_type, type } 

data: String



media\_type: :"image/jpeg" | :"image/png" | :"image/gif" | :"image/webp"

One of the following:

:"image/jpeg"

:"image/png"

:"image/gif"

:"image/webp"

type: :base64



class BetaURLImageSource { type, url } 

type: :url

url: String



class BetaFileImageSource { file\_id, type } 

file\_id: String

type: :file

type: :image



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

type: :content



class BetaURLPDFSource { type, url } 

type: :url

url: String



class BetaFileDocumentSource { file\_id, type } 

file\_id: String

type: :file

type: :document



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



citations: [BetaCitationsConfigParam](api/beta.md) { enabled } 

enabled: bool

context: String

title: String

type: :web\_fetch\_result

url: String

Fetched content URL

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: String

type: :web\_fetch\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchToolResultErrorBlockParam { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



BetaWebFetchToolResultErrorCode = :invalid\_tool\_input | :url\_too\_long | :url\_not\_allowed | 6 more

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable



class BetaWebSearchResultBlock { encrypted\_content, page\_age, title, 2 more } 

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String



class BetaWebSearchResultBlockParam { encrypted\_content, title, type, 2 more } 

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String



class BetaWebSearchTool20250305 { name, type, allowed\_callers, 7 more } 



name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20250305



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



user\_location: [BetaUserLocation](api/beta.md) { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebSearchTool20260209 { name, type, allowed\_callers, 7 more } 



name: :web\_search

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: :web\_search\_20260209



allowed\_callers: Array[:direct | :code\_execution\_20250825 | :code\_execution\_20260120 | :code\_execution\_20260521]

One of the following:

:direct

:code\_execution\_20250825

:code\_execution\_20260120

:code\_execution\_20260521

allowed\_domains: Array[String]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Array[String]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"

defer\_loading: bool

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Integer

Maximum number of times the tool can be used in the API request.

strict: bool

When true, guarantees schema validation on tool names and inputs



user\_location: [BetaUserLocation](api/beta.md) { type, city, country, 2 more } 

Parameters for the user's location. Used to provide more relevant search results.

type: :approximate

city: String

The city of the user.

country: String

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: String

The region of the user.

timezone: String

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebSearchToolRequestError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



BetaWebSearchToolResultBlockContent = [BetaWebSearchToolResultError](api/beta.md) { error\_code, type }  | Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String



class BetaWebSearchToolResultBlockParam { content, tool\_use\_id, type, 2 more } 



content: [BetaWebSearchToolResultBlockParamContent](api/beta.md)

One of the following:



ResultBlock = Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String



class BetaWebSearchToolRequestError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error

tool\_use\_id: String

type: :web\_search\_tool\_result



cache\_control: [BetaCacheControlEphemeral](api/beta.md) { type, ttl } 

Create a cache control breakpoint at this content block.

type: :ephemeral



ttl: :"5m" | :"1h"

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`.

One of the following:

:"5m"

:"1h"



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



BetaWebSearchToolResultBlockParamContent = Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ] | [BetaWebSearchToolRequestError](api/beta.md) { error\_code, type } 

One of the following:



ResultBlock = Array[[BetaWebSearchResultBlockParam](api/beta.md) { encrypted\_content, title, type, 2 more } ]

encrypted\_content: String

title: String

type: :web\_search\_result

url: String

page\_age: String



class BetaWebSearchToolRequestError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



BetaWebSearchToolResultErrorCode = :invalid\_tool\_input | :unavailable | :max\_uses\_exceeded | 3 more

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

#### MessagesBatches

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



class BetaDeletedMessageBatch { id, type } 

id: String

ID of the Message Batch.



type: :message\_batch\_deleted

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.



class BetaMessageBatch { id, archived\_at, cancel\_initiated\_at, 7 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.

archived\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was archived and its results became unavailable.

cancel\_initiated\_at: Time

RFC 3339 datetime string representing the time at which cancellation was initiated for the Message Batch. Specified only if cancellation was initiated.

created\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch was created.



ended\_at: Time

RFC 3339 datetime string representing the time at which processing for the Message Batch ended. Specified only once processing ends.

Processing ends when every request in a Message Batch has either succeeded, errored, canceled, or expired.

formatdate-time

expires\_at: Time

RFC 3339 datetime string representing the time at which the Message Batch will expire and end processing, which is 24 hours after creation.



processing\_status: :in\_progress | :canceling | :ended

Processing status of the Message Batch.

One of the following:

:in\_progress

:canceling

:ended



request\_counts: [BetaMessageBatchRequestCounts](api/beta.md) { canceled, errored, expired, 2 more } 

Tallies requests within the Message Batch, categorized by their status.

Requests start as `processing` and move to one of the other statuses only once processing of the entire batch ends. The sum of all values always matches the total number of requests in the batch.



canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.



succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



results\_url: String

URL to a `.jsonl` file containing the results of the Message Batch requests. Specified only once processing ends.

Results in the file are not guaranteed to be in the same order as requests. Use the `custom_id` field to match results to requests.



type: :message\_batch

Object type.

For Message Batches, this is always `"message_batch"`.



class BetaMessageBatchCanceledResult { type } 

type: :canceled



class BetaMessageBatchErroredResult { error, type } 



error: [BetaErrorResponse](api/beta.md) { error, request\_id, type } 



error: [BetaError](api/beta.md)

One of the following:



class BetaInvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class BetaAuthenticationError { message, type } 

message: String

type: :authentication\_error



class BetaBillingError { message, type } 

message: String

type: :billing\_error



class BetaPermissionError { message, type } 

message: String

type: :permission\_error



class BetaNotFoundError { message, type } 

message: String

type: :not\_found\_error



class BetaRateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class BetaGatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class BetaAPIError { message, type } 

message: String

type: :api\_error



class BetaOverloadedError { message, type } 

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored



class BetaMessageBatchExpiredResult { type } 

type: :expired



class BetaMessageBatchIndividualResponse { custom\_id, result } 

This is a single line in the response `.jsonl` file and does not represent the response as a whole.



custom\_id: String

Developer-provided ID created for each request in a Message Batch. Useful for matching results to requests, as results may be given out of request order.

Must be unique for each request within the Message Batch.



result: [BetaMessageBatchResult](api/beta.md)

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



class BetaMessageBatchSucceededResult { message, type } 



message: [BetaMessage](api/beta.md) { id, container, content, 9 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [BetaContainer](api/beta.md) { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



content: Array[[BetaContentBlock](api/beta.md)]

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

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback



context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



diagnostics: [BetaDiagnostics](api/beta.md) { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :model\_changed



class BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :system\_changed



class BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :tools\_changed



class BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :messages\_changed



class BetaCacheMissPreviousMessageNotFound { type } 

type: :previous\_message\_not\_found



class BetaCacheMissUnavailable { type } 

type: :unavailable



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch



speed: :standard | :fast

The inference speed mode used for this request.

One of the following:

:standard

:fast

type: :succeeded



class BetaMessageBatchErroredResult { error, type } 



error: [BetaErrorResponse](api/beta.md) { error, request\_id, type } 



error: [BetaError](api/beta.md)

One of the following:



class BetaInvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class BetaAuthenticationError { message, type } 

message: String

type: :authentication\_error



class BetaBillingError { message, type } 

message: String

type: :billing\_error



class BetaPermissionError { message, type } 

message: String

type: :permission\_error



class BetaNotFoundError { message, type } 

message: String

type: :not\_found\_error



class BetaRateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class BetaGatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class BetaAPIError { message, type } 

message: String

type: :api\_error



class BetaOverloadedError { message, type } 

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored



class BetaMessageBatchCanceledResult { type } 

type: :canceled



class BetaMessageBatchExpiredResult { type } 

type: :expired



class BetaMessageBatchRequestCounts { canceled, errored, expired, 2 more } 



canceled: Integer

Number of requests in the Message Batch that have been canceled.

This is zero until processing of the entire Message Batch has ended.



errored: Integer

Number of requests in the Message Batch that encountered an error.

This is zero until processing of the entire Message Batch has ended.



expired: Integer

Number of requests in the Message Batch that have expired.

This is zero until processing of the entire Message Batch has ended.

processing: Integer

Number of requests in the Message Batch that are processing.



succeeded: Integer

Number of requests in the Message Batch that have completed successfully.

This is zero until processing of the entire Message Batch has ended.



BetaMessageBatchResult = [BetaMessageBatchSucceededResult](api/beta.md) { message, type }  | [BetaMessageBatchErroredResult](api/beta.md) { error, type }  | [BetaMessageBatchCanceledResult](api/beta.md) { type }  | [BetaMessageBatchExpiredResult](api/beta.md) { type } 

Processing result for this request.

Contains a Message output if processing was successful, an error response if processing failed, or the reason why processing was not attempted, such as cancellation or expiration.

One of the following:



class BetaMessageBatchSucceededResult { message, type } 



message: [BetaMessage](api/beta.md) { id, container, content, 9 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [BetaContainer](api/beta.md) { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



content: Array[[BetaContentBlock](api/beta.md)]

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

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback



context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



diagnostics: [BetaDiagnostics](api/beta.md) { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :model\_changed



class BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :system\_changed



class BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :tools\_changed



class BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :messages\_changed



class BetaCacheMissPreviousMessageNotFound { type } 

type: :previous\_message\_not\_found



class BetaCacheMissUnavailable { type } 

type: :unavailable



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch



speed: :standard | :fast

The inference speed mode used for this request.

One of the following:

:standard

:fast

type: :succeeded



class BetaMessageBatchErroredResult { error, type } 



error: [BetaErrorResponse](api/beta.md) { error, request\_id, type } 



error: [BetaError](api/beta.md)

One of the following:



class BetaInvalidRequestError { message, type } 

message: String

type: :invalid\_request\_error



class BetaAuthenticationError { message, type } 

message: String

type: :authentication\_error



class BetaBillingError { message, type } 

message: String

type: :billing\_error



class BetaPermissionError { message, type } 

message: String

type: :permission\_error



class BetaNotFoundError { message, type } 

message: String

type: :not\_found\_error



class BetaRateLimitError { message, type } 

message: String

type: :rate\_limit\_error



class BetaGatewayTimeoutError { message, type } 

message: String

type: :timeout\_error



class BetaAPIError { message, type } 

message: String

type: :api\_error



class BetaOverloadedError { message, type } 

message: String

type: :overloaded\_error

request\_id: String

type: :error

type: :errored



class BetaMessageBatchCanceledResult { type } 

type: :canceled



class BetaMessageBatchExpiredResult { type } 

type: :expired



class BetaMessageBatchSucceededResult { message, type } 



message: [BetaMessage](api/beta.md) { id, container, content, 9 more } 



id: String

Unique object identifier.

The format and length of IDs may change over time.



container: [BetaContainer](api/beta.md) { id, expires\_at, skills } 

Information about the container used in the request (for the code execution tool)

id: String

Identifier for the container used in this request

expires\_at: Time

The time at which the container will expire.



skills: Array[[BetaSkill](api/beta.md) { skill\_id, type, version } ]

Skills loaded in the container

skill\_id: String

Skill ID



type: :anthropic | :custom

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

:anthropic

:custom

version: String

Skill version or 'latest' for most recent version



content: Array[[BetaContentBlock](api/beta.md)]

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

One of the following:



class BetaTextBlock { citations, text, type } 



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text



class BetaThinkingBlock { signature, thinking, type } 

signature: String

thinking: String

type: :thinking



class BetaRedactedThinkingBlock { data, type } 

data: String

type: :redacted\_thinking



class BetaToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

type: :tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaServerToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]



name: :advisor | :web\_search | :web\_fetch | 5 more

One of the following:

:advisor

:web\_search

:web\_fetch

:code\_execution

:bash\_code\_execution

:text\_editor\_code\_execution

:tool\_search\_tool\_regex

:tool\_search\_tool\_bm25

type: :server\_tool\_use



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebSearchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebSearchToolResultBlockContent](api/beta.md)

One of the following:



class BetaWebSearchToolResultError { error\_code, type } 



error\_code: [BetaWebSearchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:max\_uses\_exceeded

:too\_many\_requests

:query\_too\_long

:request\_too\_large

type: :web\_search\_tool\_result\_error



UnionMember1 = Array[[BetaWebSearchResultBlock](api/beta.md) { encrypted\_content, page\_age, title, 2 more } ]

encrypted\_content: String

page\_age: String

title: String

type: :web\_search\_result

url: String

tool\_use\_id: String

type: :web\_search\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaWebFetchToolResultBlock { content, tool\_use\_id, type, caller\_ } 



content: [BetaWebFetchToolResultErrorBlock](api/beta.md) { error\_code, type }  | [BetaWebFetchBlock](api/beta.md) { content, retrieved\_at, type, url } 

One of the following:



class BetaWebFetchToolResultErrorBlock { error\_code, type } 



error\_code: [BetaWebFetchToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:url\_too\_long

:url\_not\_allowed

:url\_not\_in\_prior\_context

:url\_not\_accessible

:unsupported\_content\_type

:too\_many\_requests

:max\_uses\_exceeded

:unavailable

type: :web\_fetch\_tool\_result\_error



class BetaWebFetchBlock { content, retrieved\_at, type, url } 



content: [BetaDocumentBlock](api/beta.md) { citations, source, title, type } 



citations: [BetaCitationConfig](api/beta.md) { enabled } 

Citation configuration for the document

enabled: bool



source: [BetaBase64PDFSource](api/beta.md) { data, media\_type, type }  | [BetaPlainTextSource](api/beta.md) { data, media\_type, type } 

One of the following:



class BetaBase64PDFSource { data, media\_type, type } 

data: String

media\_type: :"application/pdf"

type: :base64



class BetaPlainTextSource { data, media\_type, type } 

data: String

media\_type: :"text/plain"

type: :text

title: String

The title of the document

type: :document

retrieved\_at: String

ISO 8601 timestamp when the content was retrieved

type: :web\_fetch\_result

url: String

Fetched content URL

tool\_use\_id: String

type: :web\_fetch\_tool\_result



caller\_: [BetaDirectCaller](api/beta.md) { type }  | [BetaServerToolCaller](api/beta.md) { tool\_id, type }  | [BetaServerToolCaller20260120](api/beta.md) { tool\_id, type } 

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller { type } 

Tool invocation directly from the model.

type: :direct



class BetaServerToolCaller { tool\_id, type } 

Tool invocation generated by a server-side tool.

tool\_id: String

type: :code\_execution\_20250825



class BetaServerToolCaller20260120 { tool\_id, type } 

tool\_id: String

type: :code\_execution\_20260120



class BetaAdvisorToolResultBlock { content, tool\_use\_id, type } 



content: [BetaAdvisorToolResultError](api/beta.md) { error\_code, type }  | [BetaAdvisorResultBlock](api/beta.md) { stop\_reason, text, type }  | [BetaAdvisorRedactedResultBlock](api/beta.md) { encrypted\_content, stop\_reason, type } 

One of the following:



class BetaAdvisorToolResultError { error\_code, type } 



error\_code: :max\_uses\_exceeded | :prompt\_too\_long | :too\_many\_requests | 4 more

One of the following:

:max\_uses\_exceeded

:prompt\_too\_long

:too\_many\_requests

:overloaded

:unavailable

:execution\_time\_exceeded

:model\_not\_found

type: :advisor\_tool\_result\_error



class BetaAdvisorResultBlock { stop\_reason, text, type } 

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: String

type: :advisor\_result



class BetaAdvisorRedactedResultBlock { encrypted\_content, stop\_reason, type } 

encrypted\_content: String

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: String

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: :advisor\_redacted\_result

tool\_use\_id: String

type: :advisor\_tool\_result



class BetaCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaCodeExecutionToolResultBlockContent](api/beta.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError { error\_code, type } 



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta.md)

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

type: :code\_execution\_tool\_result\_error



class BetaCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :code\_execution\_result



class BetaEncryptedCodeExecutionResultBlock { content, encrypted\_stdout, return\_code, 2 more } 

Code execution result with encrypted stdout for PFC + web\_search results.



content: Array[[BetaCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :code\_execution\_output

encrypted\_stdout: String

return\_code: Integer

stderr: String

type: :encrypted\_code\_execution\_result

tool\_use\_id: String

type: :code\_execution\_tool\_result



class BetaBashCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaBashCodeExecutionToolResultError](api/beta.md) { error\_code, type }  | [BetaBashCodeExecutionResultBlock](api/beta.md) { content, return\_code, stderr, 2 more } 

One of the following:



class BetaBashCodeExecutionToolResultError { error\_code, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:output\_file\_too\_large

type: :bash\_code\_execution\_tool\_result\_error



class BetaBashCodeExecutionResultBlock { content, return\_code, stderr, 2 more } 



content: Array[[BetaBashCodeExecutionOutputBlock](api/beta.md) { file\_id, type } ]

file\_id: String

type: :bash\_code\_execution\_output

return\_code: Integer

stderr: String

stdout: String

type: :bash\_code\_execution\_result

tool\_use\_id: String

type: :bash\_code\_execution\_tool\_result



class BetaTextEditorCodeExecutionToolResultBlock { content, tool\_use\_id, type } 



content: [BetaTextEditorCodeExecutionToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaTextEditorCodeExecutionViewResultBlock](api/beta.md) { content, file\_type, num\_lines, 3 more }  | [BetaTextEditorCodeExecutionCreateResultBlock](api/beta.md) { is\_file\_update, type }  | [BetaTextEditorCodeExecutionStrReplaceResultBlock](api/beta.md) { lines, new\_lines, new\_start, 3 more } 

One of the following:



class BetaTextEditorCodeExecutionToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | 2 more

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

:file\_not\_found

error\_message: String

type: :text\_editor\_code\_execution\_tool\_result\_error



class BetaTextEditorCodeExecutionViewResultBlock { content, file\_type, num\_lines, 3 more } 

content: String



file\_type: :text | :image | :pdf

One of the following:

:text

:image

:pdf

num\_lines: Integer

start\_line: Integer

total\_lines: Integer

type: :text\_editor\_code\_execution\_view\_result



class BetaTextEditorCodeExecutionCreateResultBlock { is\_file\_update, type } 

is\_file\_update: bool

type: :text\_editor\_code\_execution\_create\_result



class BetaTextEditorCodeExecutionStrReplaceResultBlock { lines, new\_lines, new\_start, 3 more } 

lines: Array[String]

new\_lines: Integer

new\_start: Integer

old\_lines: Integer

old\_start: Integer

type: :text\_editor\_code\_execution\_str\_replace\_result

tool\_use\_id: String

type: :text\_editor\_code\_execution\_tool\_result



class BetaToolSearchToolResultBlock { content, tool\_use\_id, type } 



content: [BetaToolSearchToolResultError](api/beta.md) { error\_code, error\_message, type }  | [BetaToolSearchToolSearchResultBlock](api/beta.md) { tool\_references, type } 

One of the following:



class BetaToolSearchToolResultError { error\_code, error\_message, type } 



error\_code: :invalid\_tool\_input | :unavailable | :too\_many\_requests | :execution\_time\_exceeded

One of the following:

:invalid\_tool\_input

:unavailable

:too\_many\_requests

:execution\_time\_exceeded

error\_message: String

type: :tool\_search\_tool\_result\_error



class BetaToolSearchToolSearchResultBlock { tool\_references, type } 



tool\_references: Array[[BetaToolReferenceBlock](api/beta.md) { tool\_name, type } ]

tool\_name: String

type: :tool\_reference

type: :tool\_search\_tool\_search\_result

tool\_use\_id: String

type: :tool\_search\_tool\_result



class BetaMCPToolUseBlock { id, input, name, 2 more } 

id: String

input: Hash[Symbol, untyped]

name: String

The name of the MCP tool

server\_name: String

The name of the MCP server

type: :mcp\_tool\_use



class BetaMCPToolResultBlock { content, is\_error, tool\_use\_id, type } 



content: String | Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]

One of the following:

String = String



BetaMCPToolResultBlockContent = Array[[BetaTextBlock](api/beta.md) { citations, text, type } ]



citations: Array[[BetaTextCitation](api/beta.md)]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_char\_index: Integer

file\_id: String

start\_char\_index: Integer

type: :char\_location



class BetaCitationPageLocation { cited\_text, document\_index, document\_title, 4 more } 

cited\_text: String

document\_index: Integer

document\_title: String

end\_page\_number: Integer

file\_id: String

start\_page\_number: Integer

type: :page\_location



class BetaCitationContentBlockLocation { cited\_text, document\_index, document\_title, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: Integer

document\_title: String



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

type: :content\_block\_location



class BetaCitationsWebSearchResultLocation { cited\_text, encrypted\_index, title, 2 more } 

cited\_text: String

encrypted\_index: String

title: String

type: :web\_search\_result\_location

url: String



class BetaCitationSearchResultLocation { cited\_text, end\_block\_index, search\_result\_index, 4 more } 



cited\_text: String

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: Integer

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: Integer

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: String

start\_block\_index: Integer

0-based index of the first cited block in the source's `content` array.

title: String

type: :search\_result\_location

text: String

type: :text

is\_error: bool

tool\_use\_id: String

type: :mcp\_tool\_result



class BetaContainerUploadBlock { file\_id, type } 

Response model for a file uploaded to the container.

file\_id: String

type: :container\_upload



class BetaCompactionBlock { content, encrypted\_content, type } 

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: String

Summary of compacted content, or null if compaction failed

encrypted\_content: String

Opaque metadata from prior compaction, to be round-tripped verbatim

type: :compaction



class BetaFallbackBlock { from, to, trigger, type } 

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

from: [BetaFallbackInfo](api/beta.md) { model } 

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



to: [BetaFallbackInfo](api/beta.md) { model } 

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



trigger: [BetaFallbackRefusalTrigger](api/beta.md) { category, type } 

What caused the `from` model to hand over at this hop.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction

type: :refusal

type: :fallback



context\_management: [BetaContextManagementResponse](api/beta.md) { applied\_edits } 

Context management response.

Information about context management strategies applied during the request.



applied\_edits: Array[[BetaClearToolUses20250919EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_tool\_uses, type }  | [BetaClearThinking20251015EditResponse](api/beta.md) { cleared\_input\_tokens, cleared\_thinking\_turns, type } ]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse { cleared\_input\_tokens, cleared\_tool\_uses, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_tool\_uses: Integer

Number of tool uses that were cleared.

type: :clear\_tool\_uses\_20250919

The type of context management edit applied.



class BetaClearThinking20251015EditResponse { cleared\_input\_tokens, cleared\_thinking\_turns, type } 

cleared\_input\_tokens: Integer

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: Integer

Number of thinking turns that were cleared.

type: :clear\_thinking\_20251015

The type of context management edit applied.



diagnostics: [BetaDiagnostics](api/beta.md) { cache\_miss\_reason } 

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: [BetaCacheMissModelChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissSystemChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | [BetaCacheMissToolsChanged](api/beta.md) { cache\_missed\_input\_tokens, type }  | 3 more

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :model\_changed



class BetaCacheMissSystemChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :system\_changed



class BetaCacheMissToolsChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :tools\_changed



class BetaCacheMissMessagesChanged { cache\_missed\_input\_tokens, type } 

cache\_missed\_input\_tokens: Integer

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: :messages\_changed



class BetaCacheMissPreviousMessageNotFound { type } 

type: :previous\_message\_not\_found



class BetaCacheMissUnavailable { type } 

type: :unavailable



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String



role: :assistant

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: [BetaRefusalStopDetails](api/beta.md) { category, explanation, fallback\_credit\_token, 3 more } 

Structured information about a refusal.



category: :cyber | :bio | :frontier\_llm | :reasoning\_extraction

The policy category that triggered a refusal.

One of the following:

:cyber

:bio

:frontier\_llm

:reasoning\_extraction



explanation: String

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: String

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

fallback\_has\_prefill\_claim: bool

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

recommended\_model: String

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: :refusal



stop\_reason: [BetaStopReason](api/beta.md)

The reason that we stopped.

This may be one the following values:

- `"end_turn"`: the model reached a natural stopping point
- `"max_tokens"`: we exceeded the requested `max_tokens` or the model's maximum
- `"stop_sequence"`: one of your provided custom `stop_sequences` was generated
- `"tool_use"`: the model invoked one or more tools
- `"pause_turn"`: we paused a long-running turn. You may provide the response back as-is in a subsequent request to let the model continue.
- `"refusal"`: when streaming classifiers intervene to handle potential policy violations

In non-streaming mode this value is always non-null. In streaming mode, it is null in the `message_start` event and non-null otherwise.

One of the following:

:end\_turn

:max\_tokens

:stop\_sequence

:tool\_use

:pause\_turn

:compaction

:refusal

:model\_context\_window\_exceeded



stop\_sequence: String

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: :message

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta.md) { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 8 more } 

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

inference\_geo: String

The geographic region where inference was performed for this request.

input\_tokens: Integer

The number of input tokens which were used.



iterations: [BetaIterationsUsage](api/beta.md) { , , ,  } 

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for a sampling iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :message

Usage for a sampling iteration



class BetaCompactionIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 3 more } 

Token usage for a compaction iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.

output\_tokens: Integer

The number of output tokens which were used.

type: :compaction

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for an advisor sub-inference iteration.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :advisor\_message

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage { cache\_creation, cache\_creation\_input\_tokens, cache\_read\_input\_tokens, 4 more } 

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: [BetaCacheCreation](api/beta.md) { ephemeral\_1h\_input\_tokens, ephemeral\_5m\_input\_tokens } 

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: Integer

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: Integer

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Integer

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Integer

The number of input tokens read from the cache.

input\_tokens: Integer

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Model = :"claude-fable-5" | :"claude-mythos-5" | :"claude-opus-4-8" | 12 more

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:

:"claude-fable-5"

Next generation of intelligence for the hardest knowledge work and coding problems

:"claude-mythos-5"

Most capable model for cybersecurity and biology research

:"claude-opus-4-8"

Frontier intelligence for long-running agents and coding

:"claude-opus-4-7"

Frontier intelligence for long-running agents and coding

:"claude-mythos-preview"

New class of intelligence, strongest in coding and cybersecurity

:"claude-opus-4-6"

Frontier intelligence for long-running agents and coding

:"claude-sonnet-4-6"

Best combination of speed and intelligence

:"claude-haiku-4-5"

Fastest model with near-frontier intelligence

:"claude-haiku-4-5-20251001"

Fastest model with near-frontier intelligence

:"claude-opus-4-5"

Premium model combining maximum intelligence with practical performance

:"claude-opus-4-5-20251101"

Premium model combining maximum intelligence with practical performance

:"claude-sonnet-4-5"

High-performance model for agents and coding

:"claude-sonnet-4-5-20250929"

High-performance model for agents and coding

:"claude-opus-4-1"

Exceptional model for specialized complex tasks

:"claude-opus-4-1-20250805"

Exceptional model for specialized complex tasks

String = String

output\_tokens: Integer

The number of output tokens which were used.

type: :fallback\_message

Usage for the fallback-model attempt that served the response

output\_tokens: Integer

The number of output tokens which were used.



output\_tokens\_details: [BetaOutputTokensDetails](api/beta.md) { thinking\_tokens } 

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: Integer

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: [BetaServerToolUsage](api/beta.md) { web\_fetch\_requests, web\_search\_requests } 

The number of server tool requests.

web\_fetch\_requests: Integer

The number of web fetch tool requests.

web\_search\_requests: Integer

The number of web search tool requests.



service\_tier: :standard | :priority | :batch

If the request used the priority, standard, or batch tier.

One of the following:

:standard

:priority

:batch



speed: :standard | :fast

The inference speed mode used for this request.

One of the following:

:standard

:fast

type: :succeeded

---

*Copyright © Anthropic. All rights reserved.*
