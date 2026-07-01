# Messages

Copy page



Python

# Messages

##### [Create a Message](api/beta/messages/create.md)

beta.messages.create(MessageCreateParams\*\*kwargs)  -> [BetaMessage](api/beta/messages.md)

POST/v1/messages

##### [Count tokens in a Message](api/beta/messages/count_tokens.md)

beta.messages.count\_tokens(MessageCountTokensParams\*\*kwargs)  -> [BetaMessageTokensCount](api/beta/messages.md)

POST/v1/messages/count\_tokens

##### ModelsExpand Collapse



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaAdvisorRedactedResultBlock: …

encrypted\_content: str

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: Literal["advisor\_redacted\_result"]



class BetaAdvisorRedactedResultBlockParam: …

encrypted\_content: str

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: Literal["advisor\_redacted\_result"]

stop\_reason: Optional[str]



class BetaAdvisorResultBlock: …

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: str

type: Literal["advisor\_result"]



class BetaAdvisorResultBlockParam: …

text: str

type: Literal["advisor\_result"]

stop\_reason: Optional[str]



class BetaAdvisorTool20260301: …



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



name: Literal["advisor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["advisor\_20260301"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caching: Optional[BetaCacheControlEphemeral]

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_tokens: Optional[int]

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaAdvisorToolResultBlock: …



content: Content

One of the following:



class BetaAdvisorToolResultError: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlock: …

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: str

type: Literal["advisor\_result"]



class BetaAdvisorRedactedResultBlock: …

encrypted\_content: str

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: Literal["advisor\_redacted\_result"]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



class BetaAdvisorToolResultBlockParam: …



content: Content

One of the following:



class BetaAdvisorToolResultErrorParam: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlockParam: …

text: str

type: Literal["advisor\_result"]

stop\_reason: Optional[str]



class BetaAdvisorRedactedResultBlockParam: …

encrypted\_content: str

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: Literal["advisor\_redacted\_result"]

stop\_reason: Optional[str]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaAdvisorToolResultError: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorToolResultErrorParam: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAllThinkingTurns: …

type: Literal["all"]



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaBashCodeExecutionOutputBlock: …

file\_id: str

type: Literal["bash\_code\_execution\_output"]



class BetaBashCodeExecutionOutputBlockParam: …

file\_id: str

type: Literal["bash\_code\_execution\_output"]



class BetaBashCodeExecutionResultBlock: …



content: List[[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]



class BetaBashCodeExecutionResultBlockParam: …



content: List[[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]



class BetaBashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlock: …



content: List[[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class BetaBashCodeExecutionToolResultBlockParam: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlockParam: …



content: List[[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaBashCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaCacheControlEphemeral: …

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaCacheCreation: …

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.



class BetaCacheMissMessagesChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["messages\_changed"]



class BetaCacheMissModelChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["model\_changed"]



class BetaCacheMissPreviousMessageNotFound: …

type: Literal["previous\_message\_not\_found"]



class BetaCacheMissSystemChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["system\_changed"]



class BetaCacheMissToolsChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["tools\_changed"]



class BetaCacheMissUnavailable: …

type: Literal["unavailable"]



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationConfig: …

enabled: bool



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationsConfigParam: …

enabled: Optional[bool]



class BetaCitationsDelta: …



citation: Citation

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["citations\_delta"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaClearThinking20251015Edit: …

type: Literal["clear\_thinking\_20251015"]



keep: Optional[Keep]

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



class BetaThinkingTurns: …

type: Literal["thinking\_turns"]

value: int



class BetaAllThinkingTurns: …

type: Literal["all"]

Literal["all"]



class BetaClearThinking20251015EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: int

Number of thinking turns that were cleared.

type: Literal["clear\_thinking\_20251015"]

The type of context management edit applied.



class BetaClearToolUses20250919Edit: …

type: Literal["clear\_tool\_uses\_20250919"]



clear\_at\_least: Optional[BetaInputTokensClearAtLeast]

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: Literal["input\_tokens"]

value: int



clear\_tool\_inputs: Optional[Union[bool, List[str], null]]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

bool

List[str]

exclude\_tools: Optional[List[str]]

Tool names whose uses are preserved from clearing



keep: Optional[BetaToolUsesKeep]

Number of tool uses to retain in the conversation

type: Literal["tool\_uses"]

value: int



trigger: Optional[Trigger]

Condition that triggers the context management strategy

One of the following:



class BetaInputTokensTrigger: …

type: Literal["input\_tokens"]

value: int



class BetaToolUsesTrigger: …

type: Literal["tool\_uses"]

value: int



class BetaClearToolUses20250919EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_tool\_uses: int

Number of tool uses that were cleared.

type: Literal["clear\_tool\_uses\_20250919"]

The type of context management edit applied.



class BetaCodeExecutionOutputBlock: …

file\_id: str

type: Literal["code\_execution\_output"]



class BetaCodeExecutionOutputBlockParam: …

file\_id: str

type: Literal["code\_execution\_output"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaCodeExecutionResultBlockParam: …



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaCodeExecutionTool20250522: …



name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250522"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250825: …



name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250825"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260120: …

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20260120"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260521: …

Code execution tool with REPL state persistence.



name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20260521"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionToolResultBlock: …



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



[BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]



class BetaCodeExecutionToolResultBlockParam: …



content: [BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlockParam: …



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



[BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlockParam: …



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"



class BetaCodeExecutionToolResultErrorParam: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCompact20260112Edit: …

Automatically compact older context when reaching the configured trigger threshold.

type: Literal["compact\_20260112"]

instructions: Optional[str]

Additional instructions for summarization.

pause\_after\_compaction: Optional[bool]

Whether to pause after compaction and return the compaction block to the user.



trigger: Optional[BetaInputTokensTrigger]

When to trigger compaction. Defaults to 150000 input tokens.

type: Literal["input\_tokens"]

value: int



class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: Optional[str]

Summary of compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction"]



class BetaCompactionBlockParam: …

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: Literal["compaction"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

content: Optional[str]

Summary of previously compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaCompactionContentBlockDelta: …

content: Optional[str]

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction\_delta"]



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaContainer: …

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



skills: Optional[List[[BetaSkill](api/beta/messages.md)]]

Skills loaded in the container

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version



class BetaContainerParams: …

Container parameters with skills to be loaded.

id: Optional[str]

Container id



skills: Optional[List[[BetaSkillParams](api/beta/messages.md)]]

List of skills to load in the container

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: Optional[str]

Skill version or 'latest' for most recent version



class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



class BetaContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: str

type: Literal["container\_upload"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



[BetaContentBlock](api/beta/messages.md)

Response model for a file uploaded to the container.

One of the following:



class BetaTextBlock: …



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaRedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class BetaToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaServerToolUseBlock: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebSearchToolResultBlock: …



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[BetaWebSearchResultBlock](api/beta/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlock: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlock: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlock: …



content: [BetaDocumentBlock](api/beta/messages.md)



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaAdvisorToolResultBlock: …



content: Content

One of the following:



class BetaAdvisorToolResultError: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlock: …

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: str

type: Literal["advisor\_result"]



class BetaAdvisorRedactedResultBlock: …

encrypted\_content: str

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: Literal["advisor\_redacted\_result"]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



class BetaCodeExecutionToolResultBlock: …



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BetaBashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlock: …



content: List[[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class BetaTextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class BetaTextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class BetaTextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class BetaToolSearchToolResultBlock: …



content: Content

One of the following:



class BetaToolSearchToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class BetaToolSearchToolSearchResultBlock: …



tool\_references: List[[BetaToolReferenceBlock](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class BetaMCPToolUseBlock: …

id: str

input: Dict[str, object]

name: str

The name of the MCP tool

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



class BetaMCPToolResultBlock: …



content: Union[str, List[[BetaTextBlock](api/beta/messages.md)]]

One of the following:

str



List[[BetaTextBlock](api/beta/messages.md)]



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

is\_error: bool

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: Optional[str]

Summary of compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction"]



class BetaFallbackBlock: …

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

from\_: [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"

type: Literal["refusal"]

type: Literal["fallback"]



[BetaContentBlockParam](api/beta/messages.md)

Regular text content.

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaRequestDocumentBlock: …



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]



class BetaSearchResultBlockParam: …



content: List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]



class BetaThinkingBlockParam: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaRedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]



class BetaToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaToolResultBlockParam: …

tool\_use\_id: str

type: Literal["tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



content: Optional[Union[str, List[Content], null]]

One of the following:

str



List[Content]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaSearchResultBlockParam: …



content: List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]



class BetaRequestDocumentBlock: …



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]



class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool\_result content.

tool\_name: str

type: Literal["tool\_reference"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

is\_error: Optional[bool]



class BetaServerToolUseBlockParam: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebSearchToolResultBlockParam: …



content: [BetaWebSearchToolResultBlockParamContent](api/beta/messages.md)

One of the following:



List[[BetaWebSearchResultBlockParam](api/beta/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]



class BetaWebSearchToolRequestError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlockParam: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlockParam: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlockParam: …



content: [BetaRequestDocumentBlock](api/beta/messages.md)



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaAdvisorToolResultBlockParam: …



content: Content

One of the following:



class BetaAdvisorToolResultErrorParam: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlockParam: …

text: str

type: Literal["advisor\_result"]

stop\_reason: Optional[str]



class BetaAdvisorRedactedResultBlockParam: …

encrypted\_content: str

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: Literal["advisor\_redacted\_result"]

stop\_reason: Optional[str]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaCodeExecutionToolResultBlockParam: …



content: [BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlockParam: …



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaBashCodeExecutionToolResultBlockParam: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlockParam: …



content: List[[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaTextEditorCodeExecutionToolResultBlockParam: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

error\_message: Optional[str]



class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

type: Literal["text\_editor\_code\_execution\_view\_result"]

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]



class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaToolSearchToolResultBlockParam: …



content: Content

One of the following:



class BetaToolSearchToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["tool\_search\_tool\_result\_error"]

error\_message: Optional[str]



class BetaToolSearchToolSearchResultBlockParam: …



tool\_references: List[[BetaToolReferenceBlockParam](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaMCPToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaRequestMCPToolResultBlockParam: …

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



content: Optional[Union[str, List[[BetaTextBlockParam](api/beta/messages.md)], null]]

One of the following:

str



List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

is\_error: Optional[bool]



class BetaContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: str

type: Literal["container\_upload"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaCompactionBlockParam: …

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: Literal["compaction"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

content: Optional[str]

Summary of previously compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaMidConversationSystemBlockParam: …

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: List[[BetaTextBlockParam](api/beta/messages.md)]

System instruction text blocks.

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["mid\_conv\_system"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaFallbackBlockParam: …

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

from\_: [BetaFallbackInfoParam](api/beta/messages.md)

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfoParam](api/beta/messages.md)

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

type: Literal["fallback"]

trigger: Optional[object]

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



[BetaContentBlockSourceContent](api/beta/messages.md)

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaContextManagementConfig: …



edits: Optional[List[Edit]]

List of context management edits to apply

One of the following:



class BetaClearToolUses20250919Edit: …

type: Literal["clear\_tool\_uses\_20250919"]



clear\_at\_least: Optional[BetaInputTokensClearAtLeast]

Minimum number of tokens that must be cleared when triggered. Context will only be modified if at least this many tokens can be removed.

type: Literal["input\_tokens"]

value: int



clear\_tool\_inputs: Optional[Union[bool, List[str], null]]

Whether to clear all tool inputs (bool) or specific tool inputs to clear (list)

One of the following:

bool

List[str]

exclude\_tools: Optional[List[str]]

Tool names whose uses are preserved from clearing



keep: Optional[BetaToolUsesKeep]

Number of tool uses to retain in the conversation

type: Literal["tool\_uses"]

value: int



trigger: Optional[Trigger]

Condition that triggers the context management strategy

One of the following:



class BetaInputTokensTrigger: …

type: Literal["input\_tokens"]

value: int



class BetaToolUsesTrigger: …

type: Literal["tool\_uses"]

value: int



class BetaClearThinking20251015Edit: …

type: Literal["clear\_thinking\_20251015"]



keep: Optional[Keep]

Number of most recent assistant turns to keep thinking blocks for. Older turns will have their thinking blocks removed.

One of the following:



class BetaThinkingTurns: …

type: Literal["thinking\_turns"]

value: int



class BetaAllThinkingTurns: …

type: Literal["all"]

Literal["all"]



class BetaCompact20260112Edit: …

Automatically compact older context when reaching the configured trigger threshold.

type: Literal["compact\_20260112"]

instructions: Optional[str]

Additional instructions for summarization.

pause\_after\_compaction: Optional[bool]

Whether to pause after compaction and return the compaction block to the user.



trigger: Optional[BetaInputTokensTrigger]

When to trigger compaction. Defaults to 150000 input tokens.

type: Literal["input\_tokens"]

value: int



class BetaContextManagementResponse: …



applied\_edits: List[AppliedEdit]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_tool\_uses: int

Number of tool uses that were cleared.

type: Literal["clear\_tool\_uses\_20250919"]

The type of context management edit applied.



class BetaClearThinking20251015EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: int

Number of thinking turns that were cleared.

type: Literal["clear\_thinking\_20251015"]

The type of context management edit applied.



class BetaCountTokensContextManagementResponse: …

original\_input\_tokens: int

The original token count before context management was applied



class BetaDiagnostics: …

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: Optional[CacheMissReason]

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["model\_changed"]



class BetaCacheMissSystemChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["system\_changed"]



class BetaCacheMissToolsChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["tools\_changed"]



class BetaCacheMissMessagesChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["messages\_changed"]



class BetaCacheMissPreviousMessageNotFound: …

type: Literal["previous\_message\_not\_found"]



class BetaCacheMissUnavailable: …

type: Literal["unavailable"]



class BetaDiagnosticsParam: …

Request-level diagnostics. Currently carries the previous response
id for prompt-cache divergence reporting.

previous\_message\_id: Optional[str]

The `id` (`msg_...`) from this client's previous /v1/messages response. The server compares that request's prompt fingerprint against this one and returns `diagnostics.cache_miss_reason` when the prompt-cache prefix could not be reused. Pass `null` on the first turn to opt in without a prior message to compare.



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaDocumentBlock: …



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]



class BetaFallbackBlock: …

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

from\_: [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"

type: Literal["refusal"]

type: Literal["fallback"]



class BetaFallbackBlockParam: …

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

from\_: [BetaFallbackInfoParam](api/beta/messages.md)

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfoParam](api/beta/messages.md)

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

type: Literal["fallback"]

trigger: Optional[object]

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



class BetaFallbackInfo: …

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



class BetaFallbackInfoParam: …

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response



class BetaFallbackParam: …

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

Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

max\_tokens: Optional[int]



output\_config: Optional[BetaOutputConfig]



effort: Optional[Literal["low", "medium", "high", 2 more]]

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"



format: Optional[BetaJSONOutputFormat]

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Dict[str, object]

The JSON schema of the format

type: Literal["json\_schema"]



task\_budget: Optional[BetaTokenTaskBudget]

User-configurable total token budget across contexts.

total: int

Total token budget across all contexts in the session.

type: Literal["tokens"]

The budget type. Currently only 'tokens' is supported.

remaining: Optional[int]

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



speed: Optional[Literal["standard", "fast"]]

One of the following:

"standard"

"fast"



thinking: Optional[Thinking]

One of the following:



class BetaThinkingConfigEnabled: …



budget\_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

type: Literal["enabled"]



display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



class BetaThinkingConfigDisabled: …

type: Literal["disabled"]



class BetaThinkingConfigAdaptive: …

type: Literal["adaptive"]



display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



class BetaFallbackRefusalTrigger: …

The `from` model declined for policy reasons.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"

type: Literal["refusal"]



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaInputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]



class BetaInputTokensClearAtLeast: …

type: Literal["input\_tokens"]

value: int



class BetaInputTokensTrigger: …

type: Literal["input\_tokens"]

value: int



Optional[List[BetaIterationsUsageItem]]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response



class BetaJSONOutputFormat: …

schema: Dict[str, object]

The JSON schema of the format

type: Literal["json\_schema"]



class BetaMCPToolConfig: …

Configuration for a specific tool in an MCP toolset.

defer\_loading: Optional[bool]

enabled: Optional[bool]



class BetaMCPToolDefaultConfig: …

Default configuration for tools in an MCP toolset.

defer\_loading: Optional[bool]

enabled: Optional[bool]



class BetaMCPToolResultBlock: …



content: Union[str, List[[BetaTextBlock](api/beta/messages.md)]]

One of the following:

str



List[[BetaTextBlock](api/beta/messages.md)]



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

is\_error: bool

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



class BetaMCPToolUseBlock: …

id: str

input: Dict[str, object]

name: str

The name of the MCP tool

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



class BetaMCPToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaMCPToolset: …

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: str

Name of the MCP server to configure tools for

type: Literal["mcp\_toolset"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



configs: Optional[Dict[str, [BetaMCPToolConfig](api/beta/messages.md)]]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: Optional[bool]

enabled: Optional[bool]



default\_config: Optional[BetaMCPToolDefaultConfig]

Default configuration applied to all tools from this server

defer\_loading: Optional[bool]

enabled: Optional[bool]



class BetaMemoryTool20250818: …



name: Literal["memory"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["memory\_20250818"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



[BetaMemoryTool20250818Command](api/beta/messages.md)

One of the following:



class BetaMemoryTool20250818ViewCommand: …

command: Literal["view"]

Command type identifier

path: str

Path to directory or file to view

view\_range: Optional[List[int]]

Optional line range for viewing specific lines



class BetaMemoryTool20250818CreateCommand: …

command: Literal["create"]

Command type identifier

file\_text: str

Content to write to the file

path: str

Path where the file should be created



class BetaMemoryTool20250818StrReplaceCommand: …

command: Literal["str\_replace"]

Command type identifier

new\_str: str

Text to replace with

old\_str: str

Text to search for and replace

path: str

Path to the file where text should be replaced



class BetaMemoryTool20250818InsertCommand: …

command: Literal["insert"]

Command type identifier

insert\_line: int

Line number where text should be inserted

insert\_text: str

Text to insert at the specified line

path: str

Path to the file where text should be inserted



class BetaMemoryTool20250818DeleteCommand: …

command: Literal["delete"]

Command type identifier

path: str

Path to the file or directory to delete



class BetaMemoryTool20250818RenameCommand: …

command: Literal["rename"]

Command type identifier

new\_path: str

New path for the file or directory

old\_path: str

Current path of the file or directory



class BetaMemoryTool20250818CreateCommand: …

command: Literal["create"]

Command type identifier

file\_text: str

Content to write to the file

path: str

Path where the file should be created



class BetaMemoryTool20250818DeleteCommand: …

command: Literal["delete"]

Command type identifier

path: str

Path to the file or directory to delete



class BetaMemoryTool20250818InsertCommand: …

command: Literal["insert"]

Command type identifier

insert\_line: int

Line number where text should be inserted

insert\_text: str

Text to insert at the specified line

path: str

Path to the file where text should be inserted



class BetaMemoryTool20250818RenameCommand: …

command: Literal["rename"]

Command type identifier

new\_path: str

New path for the file or directory

old\_path: str

Current path of the file or directory



class BetaMemoryTool20250818StrReplaceCommand: …

command: Literal["str\_replace"]

Command type identifier

new\_str: str

Text to replace with

old\_str: str

Text to search for and replace

path: str

Path to the file where text should be replaced



class BetaMemoryTool20250818ViewCommand: …

command: Literal["view"]

Command type identifier

path: str

Path to directory or file to view

view\_range: Optional[List[int]]

Optional line range for viewing specific lines



class BetaMessage: …



id: str

Unique object identifier.

The format and length of IDs may change over time.



container: Optional[BetaContainer]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



skills: Optional[List[[BetaSkill](api/beta/messages.md)]]

Skills loaded in the container

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version



content: List[[BetaContentBlock](api/beta/messages.md)]

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

class BetaTextBlock: …



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaRedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class BetaToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaServerToolUseBlock: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebSearchToolResultBlock: …



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[BetaWebSearchResultBlock](api/beta/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlock: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlock: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlock: …



content: [BetaDocumentBlock](api/beta/messages.md)



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaAdvisorToolResultBlock: …



content: Content

One of the following:



class BetaAdvisorToolResultError: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlock: …

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: str

type: Literal["advisor\_result"]



class BetaAdvisorRedactedResultBlock: …

encrypted\_content: str

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: Literal["advisor\_redacted\_result"]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



class BetaCodeExecutionToolResultBlock: …



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BetaBashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlock: …



content: List[[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class BetaTextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class BetaTextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class BetaTextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class BetaToolSearchToolResultBlock: …



content: Content

One of the following:



class BetaToolSearchToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class BetaToolSearchToolSearchResultBlock: …



tool\_references: List[[BetaToolReferenceBlock](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class BetaMCPToolUseBlock: …

id: str

input: Dict[str, object]

name: str

The name of the MCP tool

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



class BetaMCPToolResultBlock: …



content: Union[str, List[[BetaTextBlock](api/beta/messages.md)]]

One of the following:

str



List[[BetaTextBlock](api/beta/messages.md)]



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

is\_error: bool

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: Optional[str]

Summary of compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction"]



class BetaFallbackBlock: …

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

from\_: [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"

type: Literal["refusal"]

type: Literal["fallback"]



context\_management: Optional[BetaContextManagementResponse]

Context management response.

Information about context management strategies applied during the request.



applied\_edits: List[AppliedEdit]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_tool\_uses: int

Number of tool uses that were cleared.

type: Literal["clear\_tool\_uses\_20250919"]

The type of context management edit applied.



class BetaClearThinking20251015EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: int

Number of thinking turns that were cleared.

type: Literal["clear\_thinking\_20251015"]

The type of context management edit applied.



diagnostics: Optional[BetaDiagnostics]

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: Optional[CacheMissReason]

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["model\_changed"]



class BetaCacheMissSystemChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["system\_changed"]



class BetaCacheMissToolsChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["tools\_changed"]



class BetaCacheMissMessagesChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["messages\_changed"]



class BetaCacheMissPreviousMessageNotFound: …

type: Literal["previous\_message\_not\_found"]



class BetaCacheMissUnavailable: …

type: Literal["unavailable"]



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: Optional[BetaRefusalStopDetails]

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: Optional[str]

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

fallback\_has\_prefill\_claim: Optional[bool]

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

recommended\_model: Optional[str]

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: Literal["refusal"]



stop\_reason: Optional[BetaStopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: Literal["message"]

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.



iterations: Optional[BetaIterationsUsage]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response

output\_tokens: int

The number of output tokens which were used.



output\_tokens\_details: Optional[BetaOutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[BetaServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



speed: Optional[Literal["standard", "fast"]]

The inference speed mode used for this request.

One of the following:

"standard"

"fast"



class BetaMessageDeltaUsage: …

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.



iterations: Optional[BetaIterationsUsage]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response

output\_tokens: int

The cumulative number of output tokens which were used.



output\_tokens\_details: Optional[BetaOutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[BetaServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaMessageParam: …



content: Union[str, List[[BetaContentBlockParam](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockParam](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaRequestDocumentBlock: …



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]



class BetaSearchResultBlockParam: …



content: List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]



class BetaThinkingBlockParam: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaRedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]



class BetaToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaToolResultBlockParam: …

tool\_use\_id: str

type: Literal["tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



content: Optional[Union[str, List[Content], null]]

One of the following:

str



List[Content]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaSearchResultBlockParam: …



content: List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]



class BetaRequestDocumentBlock: …



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]



class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool\_result content.

tool\_name: str

type: Literal["tool\_reference"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

is\_error: Optional[bool]



class BetaServerToolUseBlockParam: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebSearchToolResultBlockParam: …



content: [BetaWebSearchToolResultBlockParamContent](api/beta/messages.md)

One of the following:



List[[BetaWebSearchResultBlockParam](api/beta/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]



class BetaWebSearchToolRequestError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlockParam: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlockParam: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlockParam: …



content: [BetaRequestDocumentBlock](api/beta/messages.md)



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaAdvisorToolResultBlockParam: …



content: Content

One of the following:



class BetaAdvisorToolResultErrorParam: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlockParam: …

text: str

type: Literal["advisor\_result"]

stop\_reason: Optional[str]



class BetaAdvisorRedactedResultBlockParam: …

encrypted\_content: str

Opaque blob produced by a prior response; must be round-tripped verbatim.

type: Literal["advisor\_redacted\_result"]

stop\_reason: Optional[str]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaCodeExecutionToolResultBlockParam: …



content: [BetaCodeExecutionToolResultBlockParamContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultErrorParam: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlockParam: …



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlockParam: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaBashCodeExecutionToolResultBlockParam: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlockParam: …



content: List[[BetaBashCodeExecutionOutputBlockParam](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaTextEditorCodeExecutionToolResultBlockParam: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

error\_message: Optional[str]



class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

type: Literal["text\_editor\_code\_execution\_view\_result"]

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]



class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaToolSearchToolResultBlockParam: …



content: Content

One of the following:



class BetaToolSearchToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["tool\_search\_tool\_result\_error"]

error\_message: Optional[str]



class BetaToolSearchToolSearchResultBlockParam: …



tool\_references: List[[BetaToolReferenceBlockParam](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaMCPToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaRequestMCPToolResultBlockParam: …

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



content: Optional[Union[str, List[[BetaTextBlockParam](api/beta/messages.md)], null]]

One of the following:

str



List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

is\_error: Optional[bool]



class BetaContainerUploadBlockParam: …

A content block that represents a file to be uploaded to the container
Files uploaded via this block will be available in the container's input directory.

file\_id: str

type: Literal["container\_upload"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaCompactionBlockParam: …

A compaction block containing summary of previous context.

Users should round-trip these blocks from responses to subsequent requests
to maintain context across compaction boundaries.

When content is None, the block represents a failed compaction. The server
treats these as no-ops. Empty string content is not allowed.

type: Literal["compaction"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

content: Optional[str]

Summary of previously compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim



class BetaMidConversationSystemBlockParam: …

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: List[[BetaTextBlockParam](api/beta/messages.md)]

System instruction text blocks.

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["mid\_conv\_system"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaFallbackBlockParam: …

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

from\_: [BetaFallbackInfoParam](api/beta/messages.md)

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfoParam](api/beta/messages.md)

Identifies one hop of a fallback transition.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

type: Literal["fallback"]

trigger: Optional[object]

The response block's `trigger`, echoed verbatim. Accepted and ignored by the server; any object or `null` is allowed.



role: Literal["user", "assistant", "system"]

One of the following:

"user"

"assistant"

"system"



class BetaMessageTokensCount: …



context\_management: Optional[BetaCountTokensContextManagementResponse]

Information about context management applied to the message.

original\_input\_tokens: int

The original token count before context management was applied

input\_tokens: int

The total number of tokens across the provided list of messages, system prompt, and tools.



class BetaMetadata: …



user\_id: Optional[str]

An external identifier for the user who is associated with the request.

This should be a uuid, hash value, or other opaque identifier. Anthropic may use this id to help detect abuse. Do not include any identifying information such as name, email address, or phone number.

maxLength512



class BetaMidConversationSystemBlockParam: …

System instructions that appear mid-conversation.

Use this block to provide or update system-level instructions at a specific
point in the conversation, rather than only via the top-level `system` parameter.



content: List[[BetaTextBlockParam](api/beta/messages.md)]

System instruction text blocks.

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["mid\_conv\_system"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaOutputConfig: …



effort: Optional[Literal["low", "medium", "high", 2 more]]

All possible effort levels.

One of the following:

"low"

"medium"

"high"

"xhigh"

"max"



format: Optional[BetaJSONOutputFormat]

A schema to specify Claude's output format in responses. See [structured outputs](build-with-claude/structured-outputs.md)

schema: Dict[str, object]

The JSON schema of the format

type: Literal["json\_schema"]



task\_budget: Optional[BetaTokenTaskBudget]

User-configurable total token budget across contexts.

total: int

Total token budget across all contexts in the session.

type: Literal["tokens"]

The budget type. Currently only 'tokens' is supported.

remaining: Optional[int]

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



class BetaOutputTokensDetails: …



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



[BetaRawContentBlockDelta](api/beta/messages.md)

One of the following:



class BetaTextDelta: …

text: str

type: Literal["text\_delta"]



class BetaInputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]



class BetaCitationsDelta: …



citation: Citation

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["citations\_delta"]



class BetaThinkingDelta: …

estimated\_tokens: Optional[int]

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: str

type: Literal["thinking\_delta"]



class BetaSignatureDelta: …

signature: str

type: Literal["signature\_delta"]



class BetaCompactionContentBlockDelta: …

content: Optional[str]

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction\_delta"]



class BetaRawContentBlockDeltaEvent: …



delta: [BetaRawContentBlockDelta](api/beta/messages.md)

One of the following:



class BetaTextDelta: …

text: str

type: Literal["text\_delta"]



class BetaInputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]



class BetaCitationsDelta: …



citation: Citation

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["citations\_delta"]



class BetaThinkingDelta: …

estimated\_tokens: Optional[int]

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: str

type: Literal["thinking\_delta"]



class BetaSignatureDelta: …

signature: str

type: Literal["signature\_delta"]



class BetaCompactionContentBlockDelta: …

content: Optional[str]

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction\_delta"]

index: int

type: Literal["content\_block\_delta"]



class BetaRawContentBlockStartEvent: …



content\_block: ContentBlock

Response model for a file uploaded to the container.

One of the following:



class BetaTextBlock: …



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaRedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class BetaToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaServerToolUseBlock: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebSearchToolResultBlock: …



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[BetaWebSearchResultBlock](api/beta/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlock: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlock: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlock: …



content: [BetaDocumentBlock](api/beta/messages.md)



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaAdvisorToolResultBlock: …



content: Content

One of the following:



class BetaAdvisorToolResultError: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlock: …

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: str

type: Literal["advisor\_result"]



class BetaAdvisorRedactedResultBlock: …

encrypted\_content: str

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: Literal["advisor\_redacted\_result"]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



class BetaCodeExecutionToolResultBlock: …



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BetaBashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlock: …



content: List[[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class BetaTextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class BetaTextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class BetaTextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class BetaToolSearchToolResultBlock: …



content: Content

One of the following:



class BetaToolSearchToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class BetaToolSearchToolSearchResultBlock: …



tool\_references: List[[BetaToolReferenceBlock](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class BetaMCPToolUseBlock: …

id: str

input: Dict[str, object]

name: str

The name of the MCP tool

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



class BetaMCPToolResultBlock: …



content: Union[str, List[[BetaTextBlock](api/beta/messages.md)]]

One of the following:

str



List[[BetaTextBlock](api/beta/messages.md)]



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

is\_error: bool

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: Optional[str]

Summary of compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction"]



class BetaFallbackBlock: …

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

from\_: [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"

type: Literal["refusal"]

type: Literal["fallback"]

index: int

type: Literal["content\_block\_start"]



class BetaRawContentBlockStopEvent: …

index: int

type: Literal["content\_block\_stop"]



class BetaRawMessageDeltaEvent: …



context\_management: Optional[BetaContextManagementResponse]

Information about context management strategies applied during the request



applied\_edits: List[AppliedEdit]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_tool\_uses: int

Number of tool uses that were cleared.

type: Literal["clear\_tool\_uses\_20250919"]

The type of context management edit applied.



class BetaClearThinking20251015EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: int

Number of thinking turns that were cleared.

type: Literal["clear\_thinking\_20251015"]

The type of context management edit applied.



delta: Delta



container: Optional[BetaContainer]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



skills: Optional[List[[BetaSkill](api/beta/messages.md)]]

Skills loaded in the container

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version



stop\_details: Optional[BetaRefusalStopDetails]

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: Optional[str]

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

fallback\_has\_prefill\_claim: Optional[bool]

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

recommended\_model: Optional[str]

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: Literal["refusal"]



stop\_reason: Optional[BetaStopReason]

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: Optional[str]

type: Literal["message\_delta"]



usage: [BetaMessageDeltaUsage](api/beta/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.



iterations: Optional[BetaIterationsUsage]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response

output\_tokens: int

The cumulative number of output tokens which were used.



output\_tokens\_details: Optional[BetaOutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[BetaServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



class BetaRawMessageStartEvent: …



message: [BetaMessage](api/beta/messages.md)



id: str

Unique object identifier.

The format and length of IDs may change over time.



container: Optional[BetaContainer]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



skills: Optional[List[[BetaSkill](api/beta/messages.md)]]

Skills loaded in the container

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version



content: List[[BetaContentBlock](api/beta/messages.md)]

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

class BetaTextBlock: …



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaRedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class BetaToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaServerToolUseBlock: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebSearchToolResultBlock: …



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[BetaWebSearchResultBlock](api/beta/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlock: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlock: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlock: …



content: [BetaDocumentBlock](api/beta/messages.md)



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaAdvisorToolResultBlock: …



content: Content

One of the following:



class BetaAdvisorToolResultError: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlock: …

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: str

type: Literal["advisor\_result"]



class BetaAdvisorRedactedResultBlock: …

encrypted\_content: str

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: Literal["advisor\_redacted\_result"]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



class BetaCodeExecutionToolResultBlock: …



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BetaBashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlock: …



content: List[[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class BetaTextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class BetaTextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class BetaTextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class BetaToolSearchToolResultBlock: …



content: Content

One of the following:



class BetaToolSearchToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class BetaToolSearchToolSearchResultBlock: …



tool\_references: List[[BetaToolReferenceBlock](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class BetaMCPToolUseBlock: …

id: str

input: Dict[str, object]

name: str

The name of the MCP tool

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



class BetaMCPToolResultBlock: …



content: Union[str, List[[BetaTextBlock](api/beta/messages.md)]]

One of the following:

str



List[[BetaTextBlock](api/beta/messages.md)]



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

is\_error: bool

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: Optional[str]

Summary of compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction"]



class BetaFallbackBlock: …

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

from\_: [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"

type: Literal["refusal"]

type: Literal["fallback"]



context\_management: Optional[BetaContextManagementResponse]

Context management response.

Information about context management strategies applied during the request.



applied\_edits: List[AppliedEdit]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_tool\_uses: int

Number of tool uses that were cleared.

type: Literal["clear\_tool\_uses\_20250919"]

The type of context management edit applied.



class BetaClearThinking20251015EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: int

Number of thinking turns that were cleared.

type: Literal["clear\_thinking\_20251015"]

The type of context management edit applied.



diagnostics: Optional[BetaDiagnostics]

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: Optional[CacheMissReason]

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["model\_changed"]



class BetaCacheMissSystemChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["system\_changed"]



class BetaCacheMissToolsChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["tools\_changed"]



class BetaCacheMissMessagesChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["messages\_changed"]



class BetaCacheMissPreviousMessageNotFound: …

type: Literal["previous\_message\_not\_found"]



class BetaCacheMissUnavailable: …

type: Literal["unavailable"]



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: Optional[BetaRefusalStopDetails]

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: Optional[str]

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

fallback\_has\_prefill\_claim: Optional[bool]

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

recommended\_model: Optional[str]

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: Literal["refusal"]



stop\_reason: Optional[BetaStopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: Literal["message"]

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.



iterations: Optional[BetaIterationsUsage]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response

output\_tokens: int

The number of output tokens which were used.



output\_tokens\_details: Optional[BetaOutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[BetaServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



speed: Optional[Literal["standard", "fast"]]

The inference speed mode used for this request.

One of the following:

"standard"

"fast"

type: Literal["message\_start"]



class BetaRawMessageStopEvent: …

type: Literal["message\_stop"]



[BetaRawMessageStreamEvent](api/beta/messages.md)

One of the following:



class BetaRawMessageStartEvent: …



message: [BetaMessage](api/beta/messages.md)



id: str

Unique object identifier.

The format and length of IDs may change over time.



container: Optional[BetaContainer]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



skills: Optional[List[[BetaSkill](api/beta/messages.md)]]

Skills loaded in the container

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version



content: List[[BetaContentBlock](api/beta/messages.md)]

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

class BetaTextBlock: …



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaRedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class BetaToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaServerToolUseBlock: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebSearchToolResultBlock: …



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[BetaWebSearchResultBlock](api/beta/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlock: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlock: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlock: …



content: [BetaDocumentBlock](api/beta/messages.md)



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaAdvisorToolResultBlock: …



content: Content

One of the following:



class BetaAdvisorToolResultError: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlock: …

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: str

type: Literal["advisor\_result"]



class BetaAdvisorRedactedResultBlock: …

encrypted\_content: str

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: Literal["advisor\_redacted\_result"]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



class BetaCodeExecutionToolResultBlock: …



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BetaBashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlock: …



content: List[[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class BetaTextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class BetaTextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class BetaTextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class BetaToolSearchToolResultBlock: …



content: Content

One of the following:



class BetaToolSearchToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class BetaToolSearchToolSearchResultBlock: …



tool\_references: List[[BetaToolReferenceBlock](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class BetaMCPToolUseBlock: …

id: str

input: Dict[str, object]

name: str

The name of the MCP tool

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



class BetaMCPToolResultBlock: …



content: Union[str, List[[BetaTextBlock](api/beta/messages.md)]]

One of the following:

str



List[[BetaTextBlock](api/beta/messages.md)]



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

is\_error: bool

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: Optional[str]

Summary of compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction"]



class BetaFallbackBlock: …

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

from\_: [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"

type: Literal["refusal"]

type: Literal["fallback"]



context\_management: Optional[BetaContextManagementResponse]

Context management response.

Information about context management strategies applied during the request.



applied\_edits: List[AppliedEdit]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_tool\_uses: int

Number of tool uses that were cleared.

type: Literal["clear\_tool\_uses\_20250919"]

The type of context management edit applied.



class BetaClearThinking20251015EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: int

Number of thinking turns that were cleared.

type: Literal["clear\_thinking\_20251015"]

The type of context management edit applied.



diagnostics: Optional[BetaDiagnostics]

Response envelope for request-level diagnostics. Present (possibly
null) whenever the caller supplied `diagnostics` on the request.



cache\_miss\_reason: Optional[CacheMissReason]

Explains why the prompt cache could not fully reuse the prefix from the request identified by `diagnostics.previous_message_id`. `null` means diagnosis is still pending — the response was serialized before the background comparison completed.

One of the following:



class BetaCacheMissModelChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["model\_changed"]



class BetaCacheMissSystemChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["system\_changed"]



class BetaCacheMissToolsChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["tools\_changed"]



class BetaCacheMissMessagesChanged: …

cache\_missed\_input\_tokens: int

Approximate number of input tokens that would have been read from cache had the prefix matched the previous request.

type: Literal["messages\_changed"]



class BetaCacheMissPreviousMessageNotFound: …

type: Literal["previous\_message\_not\_found"]



class BetaCacheMissUnavailable: …

type: Literal["unavailable"]



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



role: Literal["assistant"]

Conversational role of the generated message.

This will always be `"assistant"`.



stop\_details: Optional[BetaRefusalStopDetails]

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: Optional[str]

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

fallback\_has\_prefill\_claim: Optional[bool]

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

recommended\_model: Optional[str]

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: Literal["refusal"]



stop\_reason: Optional[BetaStopReason]

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

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



stop\_sequence: Optional[str]

Which custom stop sequence was generated, if any.

This value will be a non-null string if one of your custom stop sequences was generated.



type: Literal["message"]

Object type.

For Messages, this is always `"message"`.



usage: [BetaUsage](api/beta/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.



iterations: Optional[BetaIterationsUsage]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response

output\_tokens: int

The number of output tokens which were used.



output\_tokens\_details: Optional[BetaOutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[BetaServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



speed: Optional[Literal["standard", "fast"]]

The inference speed mode used for this request.

One of the following:

"standard"

"fast"

type: Literal["message\_start"]



class BetaRawMessageDeltaEvent: …



context\_management: Optional[BetaContextManagementResponse]

Information about context management strategies applied during the request



applied\_edits: List[AppliedEdit]

List of context management edits that were applied.

One of the following:



class BetaClearToolUses20250919EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_tool\_uses: int

Number of tool uses that were cleared.

type: Literal["clear\_tool\_uses\_20250919"]

The type of context management edit applied.



class BetaClearThinking20251015EditResponse: …

cleared\_input\_tokens: int

Number of input tokens cleared by this edit.

cleared\_thinking\_turns: int

Number of thinking turns that were cleared.

type: Literal["clear\_thinking\_20251015"]

The type of context management edit applied.



delta: Delta



container: Optional[BetaContainer]

Information about the container used in the request (for the code execution tool)

id: str

Identifier for the container used in this request

expires\_at: datetime

The time at which the container will expire.



skills: Optional[List[[BetaSkill](api/beta/messages.md)]]

Skills loaded in the container

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version



stop\_details: Optional[BetaRefusalStopDetails]

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: Optional[str]

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

fallback\_has\_prefill\_claim: Optional[bool]

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

recommended\_model: Optional[str]

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: Literal["refusal"]



stop\_reason: Optional[BetaStopReason]

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"

stop\_sequence: Optional[str]

type: Literal["message\_delta"]



usage: [BetaMessageDeltaUsage](api/beta/messages.md)

Billing and rate-limit usage.

Anthropic's API bills and rate-limits by token counts, as tokens represent the underlying cost to our systems.

Under the hood, the API transforms requests into a format suitable for the model. The model's output then goes through a parsing stage before becoming an API response. As a result, the token counts in `usage` will not match one-to-one with the exact visible content of an API request or response.

For example, `output_tokens` will be non-zero, even for an empty string response from Claude.

Total input tokens in a request is the summation of `input_tokens`, `cache_creation_input_tokens`, and `cache_read_input_tokens`.

cache\_creation\_input\_tokens: Optional[int]

The cumulative number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The cumulative number of input tokens read from the cache.

input\_tokens: Optional[int]

The cumulative number of input tokens which were used.



iterations: Optional[BetaIterationsUsage]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response

output\_tokens: int

The cumulative number of output tokens which were used.



output\_tokens\_details: Optional[BetaOutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[BetaServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



class BetaRawMessageStopEvent: …

type: Literal["message\_stop"]



class BetaRawContentBlockStartEvent: …



content\_block: ContentBlock

Response model for a file uploaded to the container.

One of the following:



class BetaTextBlock: …



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaRedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class BetaToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaServerToolUseBlock: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebSearchToolResultBlock: …



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[BetaWebSearchResultBlock](api/beta/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlock: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlock: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlock: …



content: [BetaDocumentBlock](api/beta/messages.md)



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaAdvisorToolResultBlock: …



content: Content

One of the following:



class BetaAdvisorToolResultError: …



error\_code: Literal["max\_uses\_exceeded", "prompt\_too\_long", "too\_many\_requests", 4 more]

One of the following:

"max\_uses\_exceeded"

"prompt\_too\_long"

"too\_many\_requests"

"overloaded"

"unavailable"

"execution\_time\_exceeded"

"model\_not\_found"

type: Literal["advisor\_tool\_result\_error"]



class BetaAdvisorResultBlock: …

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`). `max_tokens` indicates the advisor's output was truncated at the tool's `max_tokens` value or the advisor model's policy cap.

text: str

type: Literal["advisor\_result"]



class BetaAdvisorRedactedResultBlock: …

encrypted\_content: str

Opaque blob containing the advisor's output. Round-trip verbatim; do not inspect or modify.

stop\_reason: Optional[str]

The advisor sub-inference's stop reason (same values as the top-level message `stop_reason`).

type: Literal["advisor\_redacted\_result"]

tool\_use\_id: str

type: Literal["advisor\_tool\_result"]



class BetaCodeExecutionToolResultBlock: …



content: [BetaCodeExecutionToolResultBlockContent](api/beta/messages.md)

Code execution result with encrypted stdout for PFC + web\_search results.

One of the following:



class BetaCodeExecutionToolResultError: …



error\_code: [BetaCodeExecutionToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["code\_execution\_tool\_result\_error"]



class BetaCodeExecutionResultBlock: …



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["code\_execution\_result"]



class BetaEncryptedCodeExecutionResultBlock: …

Code execution result with encrypted stdout for PFC + web\_search results.



content: List[[BetaCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["code\_execution\_output"]

encrypted\_stdout: str

return\_code: int

stderr: str

type: Literal["encrypted\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["code\_execution\_tool\_result"]



class BetaBashCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaBashCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"output\_file\_too\_large"

type: Literal["bash\_code\_execution\_tool\_result\_error"]



class BetaBashCodeExecutionResultBlock: …



content: List[[BetaBashCodeExecutionOutputBlock](api/beta/messages.md)]

file\_id: str

type: Literal["bash\_code\_execution\_output"]

return\_code: int

stderr: str

stdout: str

type: Literal["bash\_code\_execution\_result"]

tool\_use\_id: str

type: Literal["bash\_code\_execution\_tool\_result"]



class BetaTextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class BetaTextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class BetaTextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class BetaToolSearchToolResultBlock: …



content: Content

One of the following:



class BetaToolSearchToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class BetaToolSearchToolSearchResultBlock: …



tool\_references: List[[BetaToolReferenceBlock](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class BetaMCPToolUseBlock: …

id: str

input: Dict[str, object]

name: str

The name of the MCP tool

server\_name: str

The name of the MCP server

type: Literal["mcp\_tool\_use"]



class BetaMCPToolResultBlock: …



content: Union[str, List[[BetaTextBlock](api/beta/messages.md)]]

One of the following:

str



List[[BetaTextBlock](api/beta/messages.md)]



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]

is\_error: bool

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



class BetaContainerUploadBlock: …

Response model for a file uploaded to the container.

file\_id: str

type: Literal["container\_upload"]



class BetaCompactionBlock: …

A compaction block returned when autocompact is triggered.

When content is None, it indicates the compaction failed to produce a valid
summary (e.g., malformed output from the model). Clients may round-trip
compaction blocks with null content; the server treats them as no-ops.

content: Optional[str]

Summary of compacted content, or null if compaction failed

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction"]



class BetaFallbackBlock: …

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

from\_: [BetaFallbackInfo](api/beta/messages.md)

The model whose output ends at this point — the model that declined at this hop. When the declining hop is the requested model, its `model` echoes the top-level `model` string the caller sent (alias or canonical); when the declining hop is a fallback model, its `model` is that model's canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



to: [BetaFallbackInfo](api/beta/messages.md)

The fallback model producing the content that follows this block. Its `model` is always the canonical id.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



trigger: [BetaFallbackRefusalTrigger](api/beta/messages.md)

What caused the `from` model to hand over at this hop.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"

type: Literal["refusal"]

type: Literal["fallback"]

index: int

type: Literal["content\_block\_start"]



class BetaRawContentBlockDeltaEvent: …



delta: [BetaRawContentBlockDelta](api/beta/messages.md)

One of the following:



class BetaTextDelta: …

text: str

type: Literal["text\_delta"]



class BetaInputJSONDelta: …

partial\_json: str

type: Literal["input\_json\_delta"]



class BetaCitationsDelta: …



citation: Citation

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

type: Literal["citations\_delta"]



class BetaThinkingDelta: …

estimated\_tokens: Optional[int]

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: str

type: Literal["thinking\_delta"]



class BetaSignatureDelta: …

signature: str

type: Literal["signature\_delta"]



class BetaCompactionContentBlockDelta: …

content: Optional[str]

encrypted\_content: Optional[str]

Opaque metadata from prior compaction, to be round-tripped verbatim

type: Literal["compaction\_delta"]

index: int

type: Literal["content\_block\_delta"]



class BetaRawContentBlockStopEvent: …

index: int

type: Literal["content\_block\_stop"]



class BetaRedactedThinkingBlock: …

data: str

type: Literal["redacted\_thinking"]



class BetaRedactedThinkingBlockParam: …

data: str

type: Literal["redacted\_thinking"]



class BetaRefusalStopDetails: …

Structured information about a refusal.



category: Optional[Literal["cyber", "bio", "frontier\_llm", 2 more]]

The policy category that triggered a refusal.

One of the following:

"cyber"

"bio"

"frontier\_llm"

"reasoning\_extraction"

"military\_weapons"



explanation: Optional[str]

Human-readable explanation of the refusal.

This text is not guaranteed to be stable. `null` when no explanation is available for the category.



fallback\_credit\_token: Optional[str]

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

fallback\_has\_prefill\_claim: Optional[bool]

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

recommended\_model: Optional[str]

The server's suggested retry target for this refusal. Populated when a fallback attempt could not be made (the fallback model's rate limit was exhausted, or it was overloaded); names the fallback model the caller can retry directly. Null otherwise.

type: Literal["refusal"]



class BetaRequestDocumentBlock: …



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]



class BetaRequestMCPServerToolConfiguration: …

allowed\_tools: Optional[List[str]]

enabled: Optional[bool]



class BetaRequestMCPServerURLDefinition: …

name: str

type: Literal["url"]

url: str

authorization\_token: Optional[str]



tool\_configuration: Optional[BetaRequestMCPServerToolConfiguration]

allowed\_tools: Optional[List[str]]

enabled: Optional[bool]



class BetaRequestMCPToolResultBlockParam: …

tool\_use\_id: str

type: Literal["mcp\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



content: Optional[Union[str, List[[BetaTextBlockParam](api/beta/messages.md)], null]]

One of the following:

str



List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

is\_error: Optional[bool]



class BetaSearchResultBlockParam: …



content: List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaServerToolUsage: …

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



class BetaServerToolUseBlock: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaServerToolUseBlockParam: …

id: str

input: Dict[str, object]



name: Literal["advisor", "web\_search", "web\_fetch", 5 more]

One of the following:

"advisor"

"web\_search"

"web\_fetch"

"code\_execution"

"bash\_code\_execution"

"text\_editor\_code\_execution"

"tool\_search\_tool\_regex"

"tool\_search\_tool\_bm25"

type: Literal["server\_tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaSignatureDelta: …

signature: str

type: Literal["signature\_delta"]



class BetaSkill: …

A skill that was loaded in a container (response model).

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: str

Skill version or 'latest' for most recent version



class BetaSkillParams: …

Specification for a skill to be loaded in a container (request model).

skill\_id: str

Skill ID



type: Literal["anthropic", "custom"]

Type of skill - either 'anthropic' (built-in) or 'custom' (user-defined)

One of the following:

"anthropic"

"custom"

version: Optional[str]

Skill version or 'latest' for most recent version



Literal["end\_turn", "max\_tokens", "stop\_sequence", 5 more]

One of the following:

"end\_turn"

"max\_tokens"

"stop\_sequence"

"tool\_use"

"pause\_turn"

"compaction"

"refusal"

"model\_context\_window\_exceeded"



class BetaTextBlock: …



citations: Optional[List[[BetaTextCitation](api/beta/messages.md)]]

Citations supporting the text block.

The type of citation returned will depend on the type of document being cited. Citing a PDF results in `page_location`, plain text results in `char_location`, and content document results in `content_block_location`.

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

text: str

type: Literal["text"]



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



[BetaTextCitation](api/beta/messages.md)

One of the following:



class BetaCitationCharLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

file\_id: Optional[str]

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocation: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

file\_id: Optional[str]

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

file\_id: Optional[str]

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationsWebSearchResultLocation: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocation: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



[BetaTextCitationParam](api/beta/messages.md)

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaTextDelta: …

text: str

type: Literal["text\_delta"]



class BetaTextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]



class BetaTextEditorCodeExecutionToolResultBlock: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class BetaTextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class BetaTextEditorCodeExecutionCreateResultBlock: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlock: …

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



class BetaTextEditorCodeExecutionToolResultBlockParam: …



content: Content

One of the following:



class BetaTextEditorCodeExecutionToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

error\_message: Optional[str]



class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

type: Literal["text\_editor\_code\_execution\_view\_result"]

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]



class BetaTextEditorCodeExecutionCreateResultBlockParam: …

is\_file\_update: bool

type: Literal["text\_editor\_code\_execution\_create\_result"]



class BetaTextEditorCodeExecutionStrReplaceResultBlockParam: …

type: Literal["text\_editor\_code\_execution\_str\_replace\_result"]

lines: Optional[List[str]]

new\_lines: Optional[int]

new\_start: Optional[int]

old\_lines: Optional[int]

old\_start: Optional[int]

tool\_use\_id: str

type: Literal["text\_editor\_code\_execution\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaTextEditorCodeExecutionToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

error\_message: Optional[str]

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]



class BetaTextEditorCodeExecutionToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", 2 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

"file\_not\_found"

type: Literal["text\_editor\_code\_execution\_tool\_result\_error"]

error\_message: Optional[str]



class BetaTextEditorCodeExecutionViewResultBlock: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]

type: Literal["text\_editor\_code\_execution\_view\_result"]



class BetaTextEditorCodeExecutionViewResultBlockParam: …

content: str



file\_type: Literal["text", "image", "pdf"]

One of the following:

"text"

"image"

"pdf"

type: Literal["text\_editor\_code\_execution\_view\_result"]

num\_lines: Optional[int]

start\_line: Optional[int]

total\_lines: Optional[int]



class BetaThinkingBlock: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaThinkingBlockParam: …

signature: str

thinking: str

type: Literal["thinking"]



class BetaThinkingConfigAdaptive: …

type: Literal["adaptive"]



display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



class BetaThinkingConfigDisabled: …

type: Literal["disabled"]



class BetaThinkingConfigEnabled: …



budget\_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

type: Literal["enabled"]



display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



[BetaThinkingConfigParam](api/beta/messages.md)

Configuration for enabling Claude's extended thinking.

When enabled, responses include `thinking` content blocks showing Claude's thinking process before the final answer. Requires a minimum budget of 1,024 tokens and counts towards your `max_tokens` limit.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

One of the following:



class BetaThinkingConfigEnabled: …



budget\_tokens: int

Determines how many tokens Claude can use for its internal reasoning process. Larger budgets can enable more thorough analysis for complex problems, improving response quality.

Must be ≥1024 and less than `max_tokens`.

See [extended thinking](build-with-claude/extended-thinking.md) for details.

minimum1024

type: Literal["enabled"]



display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



class BetaThinkingConfigDisabled: …

type: Literal["disabled"]



class BetaThinkingConfigAdaptive: …

type: Literal["adaptive"]



display: Optional[Literal["summarized", "omitted"]]

Controls how thinking content appears in the response. When set to `summarized`, thinking is returned normally. When set to `omitted`, thinking content is redacted but a signature is returned for multi-turn continuity. Defaults to `summarized`.

One of the following:

"summarized"

"omitted"



class BetaThinkingDelta: …

estimated\_tokens: Optional[int]

Per-frame increment of a coarse, running estimate of the tokens this thinking block has produced so far. Present whenever the `thinking-token-count-2026-05-13` beta is set; `null` unless `thinking.display` resolves to `"omitted"` and a count is due this frame. Sum the increments across `thinking_delta` frames on this block for a progress indicator. Each increment is a non-negative multiple of a fixed quantum and the cadence is rate-limited, so this is a deliberately lossy display hint, not a billable count; `usage.output_tokens` remains authoritative.

thinking: str

type: Literal["thinking\_delta"]



class BetaThinkingTurns: …

type: Literal["thinking\_turns"]

value: int



class BetaTokenTaskBudget: …

User-configurable total token budget across contexts.

total: int

Total token budget across all contexts in the session.

type: Literal["tokens"]

The budget type. Currently only 'tokens' is supported.

remaining: Optional[int]

Remaining tokens in the budget. Use this to track usage across contexts when implementing compaction client-side. Defaults to total if not provided.



class BetaTool: …



input\_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]



name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description: Optional[str]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: Optional[bool]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

type: Optional[Literal["custom"]]



class BetaToolBash20241022: …



name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["bash\_20241022"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolBash20250124: …



name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["bash\_20250124"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



[BetaToolChoice](api/beta/messages.md)

How the model should use the provided tools. The model can use a specific tool, any available tool, decide by itself, or not use tools at all.

One of the following:



class BetaToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal["auto"]



disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class BetaToolChoiceAny: …

The model will use any available tools.

type: Literal["any"]



disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal["tool"]



disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal["none"]



class BetaToolChoiceAny: …

The model will use any available tools.

type: Literal["any"]



disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolChoiceAuto: …

The model will automatically decide whether to use tools.

type: Literal["auto"]



disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output at most one tool use.



class BetaToolChoiceNone: …

The model will not be allowed to use tools.

type: Literal["none"]



class BetaToolChoiceTool: …

The model will use the specified tool with `tool_choice.name`.

name: str

The name of the tool to use.

type: Literal["tool"]



disable\_parallel\_tool\_use: Optional[bool]

Whether to disable parallel tool use.

Defaults to `false`. If set to `true`, the model will output exactly one tool use.



class BetaToolComputerUse20241022: …

display\_height\_px: int

The height of the display in pixels.

display\_width\_px: int

The width of the display in pixels.



name: Literal["computer"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["computer\_20241022"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Optional[int]

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20250124: …

display\_height\_px: int

The height of the display in pixels.

display\_width\_px: int

The width of the display in pixels.



name: Literal["computer"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["computer\_20250124"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Optional[int]

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20251124: …

display\_height\_px: int

The height of the display in pixels.

display\_width\_px: int

The width of the display in pixels.



name: Literal["computer"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["computer\_20251124"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Optional[int]

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: Optional[bool]

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolReferenceBlock: …

tool\_name: str

type: Literal["tool\_reference"]



class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool\_result content.

tool\_name: str

type: Literal["tool\_reference"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaToolResultBlockParam: …

tool\_use\_id: str

type: Literal["tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



content: Optional[Union[str, List[Content], null]]

One of the following:

str



List[Content]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaSearchResultBlockParam: …



content: List[[BetaTextBlockParam](api/beta/messages.md)]

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]

source: str

title: str

type: Literal["search\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]



class BetaRequestDocumentBlock: …



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]



class BetaToolReferenceBlockParam: …

Tool reference block that can be included in tool\_result content.

tool\_name: str

type: Literal["tool\_reference"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

is\_error: Optional[bool]



class BetaToolSearchToolBm25\_20251119: …



name: Literal["tool\_search\_tool\_bm25"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: Literal["tool\_search\_tool\_bm25\_20251119", "tool\_search\_tool\_bm25"]

One of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolRegex20251119: …



name: Literal["tool\_search\_tool\_regex"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: Literal["tool\_search\_tool\_regex\_20251119", "tool\_search\_tool\_regex"]

One of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolResultBlock: …



content: Content

One of the following:



class BetaToolSearchToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class BetaToolSearchToolSearchResultBlock: …



tool\_references: List[[BetaToolReferenceBlock](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



class BetaToolSearchToolResultBlockParam: …



content: Content

One of the following:



class BetaToolSearchToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["tool\_search\_tool\_result\_error"]

error\_message: Optional[str]



class BetaToolSearchToolSearchResultBlockParam: …



tool\_references: List[[BetaToolReferenceBlockParam](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["tool\_search\_tool\_search\_result"]

tool\_use\_id: str

type: Literal["tool\_search\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



class BetaToolSearchToolResultError: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

error\_message: Optional[str]

type: Literal["tool\_search\_tool\_result\_error"]



class BetaToolSearchToolResultErrorParam: …



error\_code: Literal["invalid\_tool\_input", "unavailable", "too\_many\_requests", "execution\_time\_exceeded"]

One of the following:

"invalid\_tool\_input"

"unavailable"

"too\_many\_requests"

"execution\_time\_exceeded"

type: Literal["tool\_search\_tool\_result\_error"]

error\_message: Optional[str]



class BetaToolSearchToolSearchResultBlock: …



tool\_references: List[[BetaToolReferenceBlock](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]

type: Literal["tool\_search\_tool\_search\_result"]



class BetaToolSearchToolSearchResultBlockParam: …



tool\_references: List[[BetaToolReferenceBlockParam](api/beta/messages.md)]

tool\_name: str

type: Literal["tool\_reference"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["tool\_search\_tool\_search\_result"]



class BetaToolTextEditor20241022: …



name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20241022"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250124: …



name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250124"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250429: …



name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250429"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250728: …



name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250728"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

max\_characters: Optional[int]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



[BetaToolUnion](api/beta/messages.md)

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).

One of the following:



class BetaTool: …



input\_schema: InputSchema

[JSON schema](https://json-schema.org/draft/2020-12) for this tool's input.

This defines the shape of the `input` that your tool accepts and that the model will produce.

type: Literal["object"]

properties: Optional[Dict[str, object]]

required: Optional[List[str]]



name: str

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

maxLength128

minLength1



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.



description: Optional[str]

Description of what this tool does.

Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform. You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

eager\_input\_streaming: Optional[bool]

Enable eager input streaming for this tool. When true, tool input parameters will be streamed incrementally as they are generated, and types will be inferred on-the-fly rather than buffering the full JSON output. When false, streaming is disabled for this tool even if the fine-grained-tool-streaming beta is active. When null (default), uses the default behavior based on beta headers.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

type: Optional[Literal["custom"]]



class BetaToolBash20241022: …



name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["bash\_20241022"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolBash20250124: …



name: Literal["bash"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["bash\_20250124"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250522: …



name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250522"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20250825: …



name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20250825"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260120: …

Code execution tool with REPL state persistence (daemon mode + gVisor checkpoint).



name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20260120"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaCodeExecutionTool20260521: …

Code execution tool with REPL state persistence.



name: Literal["code\_execution"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["code\_execution\_20260521"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20241022: …

display\_height\_px: int

The height of the display in pixels.

display\_width\_px: int

The width of the display in pixels.



name: Literal["computer"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["computer\_20241022"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Optional[int]

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaMemoryTool20250818: …



name: Literal["memory"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["memory\_20250818"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20250124: …

display\_height\_px: int

The height of the display in pixels.

display\_width\_px: int

The width of the display in pixels.



name: Literal["computer"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["computer\_20250124"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Optional[int]

The X11 display number (e.g. 0, 1) for the display.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20241022: …



name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20241022"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolComputerUse20251124: …

display\_height\_px: int

The height of the display in pixels.

display\_width\_px: int

The width of the display in pixels.



name: Literal["computer"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["computer\_20251124"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

display\_number: Optional[int]

The X11 display number (e.g. 0, 1) for the display.

enable\_zoom: Optional[bool]

Whether to enable an action to take a zoomed-in screenshot of the screen.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250124: …



name: Literal["str\_replace\_editor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250124"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250429: …



name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250429"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolTextEditor20250728: …



name: Literal["str\_replace\_based\_edit\_tool"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["text\_editor\_20250728"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

input\_examples: Optional[List[Dict[str, object]]]

max\_characters: Optional[int]

Maximum number of characters to display when viewing a file. If not specified, defaults to displaying the full file.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaWebSearchTool20250305: …



name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20250305"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



user\_location: Optional[BetaUserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20250910: …



name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20250910"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaWebSearchTool20260209: …



name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20260209"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



user\_location: Optional[BetaUserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20260209: …



name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260209"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260309: …

Web fetch tool with use\_cache parameter for bypassing cached content.



name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260309"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

use\_cache: Optional[bool]

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaWebSearchTool20260318: …



name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20260318"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.



response\_inclusion: Optional[Literal["full", "excluded"]]

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"

"excluded"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



user\_location: Optional[BetaUserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchTool20260318: …



name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260318"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.



response\_inclusion: Optional[Literal["full", "excluded"]]

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"

"excluded"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

use\_cache: Optional[bool]

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaAdvisorTool20260301: …



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str



name: Literal["advisor"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["advisor\_20260301"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caching: Optional[BetaCacheControlEphemeral]

Caching for the advisor's own prompt. When set, each advisor call writes a cache entry at the given TTL so subsequent calls in the same conversation read the stable prefix. When omitted, the advisor prompt is not cached.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_tokens: Optional[int]

Bounds the advisor's total output (thinking + text) per call. When the advisor hits this cap, the returned advisor\_result or advisor\_redacted\_result block carries stop\_reason='max\_tokens', and a truncation note is appended to the advice text the worker model sees (inside the encrypted blob in redacted mode). When set, the server also emits a remaining-tokens budget block in the advisor's prompt so the advisor self-shapes toward the cap. When omitted, the advisor model's default output cap applies and no budget block is emitted.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolBm25\_20251119: …



name: Literal["tool\_search\_tool\_bm25"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: Literal["tool\_search\_tool\_bm25\_20251119", "tool\_search\_tool\_bm25"]

One of the following:

"tool\_search\_tool\_bm25\_20251119"

"tool\_search\_tool\_bm25"



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaToolSearchToolRegex20251119: …



name: Literal["tool\_search\_tool\_regex"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.



type: Literal["tool\_search\_tool\_regex\_20251119", "tool\_search\_tool\_regex"]

One of the following:

"tool\_search\_tool\_regex\_20251119"

"tool\_search\_tool\_regex"



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaMCPToolset: …

Configuration for a group of tools from an MCP server.

Allows configuring enabled status and defer\_loading for all tools
from an MCP server, with optional per-tool overrides.

mcp\_server\_name: str

Name of the MCP server to configure tools for

type: Literal["mcp\_toolset"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



configs: Optional[Dict[str, [BetaMCPToolConfig](api/beta/messages.md)]]

Configuration overrides for specific tools, keyed by tool name

defer\_loading: Optional[bool]

enabled: Optional[bool]



default\_config: Optional[BetaMCPToolDefaultConfig]

Default configuration applied to all tools from this server

defer\_loading: Optional[bool]

enabled: Optional[bool]



class BetaToolUseBlock: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaToolUseBlockParam: …

id: str

input: Dict[str, object]

name: str

type: Literal["tool\_use"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaToolUsesKeep: …

type: Literal["tool\_uses"]

value: int



class BetaToolUsesTrigger: …

type: Literal["tool\_uses"]

value: int



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaUsage: …



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: Optional[int]

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: Optional[int]

The number of input tokens read from the cache.

inference\_geo: Optional[str]

The geographic region where inference was performed for this request.

input\_tokens: int

The number of input tokens which were used.



iterations: Optional[BetaIterationsUsage]

Per-iteration token usage breakdown.

Each entry represents one sampling iteration, with its own input/output token counts and cache statistics. This allows you to:

- Determine which iterations exceeded long context thresholds (>=200k tokens)
- Calculate the true context window size from the last iteration
- Understand token accumulation across server-side tool use loops

One of the following:



class BetaMessageIterationUsage: …

Token usage for a sampling iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["message"]

Usage for a sampling iteration



class BetaCompactionIterationUsage: …

Token usage for a compaction iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.

output\_tokens: int

The number of output tokens which were used.

type: Literal["compaction"]

Usage for a compaction iteration



class BetaAdvisorMessageIterationUsage: …

Token usage for an advisor sub-inference iteration.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["advisor\_message"]

Usage for an advisor sub-inference iteration



class BetaFallbackMessageIterationUsage: …

Token usage for the fallback-model attempt of a server-side fallback request.

Produced in place of a `message` entry for whichever hop served the
response. A declined hop produces the existing `message` entry. Whether
a fallback model served the response is signalled by the presence of this
entry in `usage.iterations`.



cache\_creation: Optional[BetaCacheCreation]

Breakdown of cached tokens by TTL

ephemeral\_1h\_input\_tokens: int

The number of input tokens used to create the 1 hour cache entry.

ephemeral\_5m\_input\_tokens: int

The number of input tokens used to create the 5 minute cache entry.

cache\_creation\_input\_tokens: int

The number of input tokens used to create the cache entry.

cache\_read\_input\_tokens: int

The number of input tokens read from the cache.

input\_tokens: int

The number of input tokens which were used.



model: [Model](api/messages.md)

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

One of the following:



Literal["claude-fable-5", "claude-mythos-5", "claude-opus-4-8", 12 more]

The model that will complete your prompt.

See [models](https://docs.anthropic.com/en/docs/models-overview) for additional details and options.

- `claude-fable-5` - Next generation of intelligence for the hardest knowledge work and coding problems
- `claude-mythos-5` - Most capable model for cybersecurity and biology research
- `claude-opus-4-8` - Frontier intelligence for long-running agents and coding
- `claude-opus-4-7` - Frontier intelligence for long-running agents and coding
- `claude-mythos-preview` - Deprecated: Will reach end-of-life on June 30, 2026. Please migrate to claude-mythos-5. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-6` - Frontier intelligence for long-running agents and coding
- `claude-sonnet-4-6` - Best combination of speed and intelligence
- `claude-haiku-4-5` - Fastest model with near-frontier intelligence
- `claude-haiku-4-5-20251001` - Fastest model with near-frontier intelligence
- `claude-opus-4-5` - Premium model combining maximum intelligence with practical performance
- `claude-opus-4-5-20251101` - Premium model combining maximum intelligence with practical performance
- `claude-sonnet-4-5` - High-performance model for agents and coding
- `claude-sonnet-4-5-20250929` - High-performance model for agents and coding
- `claude-opus-4-1` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.
- `claude-opus-4-1-20250805` - Deprecated: Will reach end-of-life on August 5, 2026. Please migrate to a newer model. Visit <https://docs.anthropic.com/en/docs/resources/model-deprecations> for more information.

One of the following:

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

str

output\_tokens: int

The number of output tokens which were used.

type: Literal["fallback\_message"]

Usage for the fallback-model attempt that served the response

output\_tokens: int

The number of output tokens which were used.



output\_tokens\_details: Optional[BetaOutputTokensDetails]

Breakdown of output tokens by category.

`output_tokens` remains the inclusive, authoritative total used for billing.
This object provides a read-only decomposition for observability — for example,
how many of the billed output tokens were spent on internal reasoning that may
have been summarized before being returned to you.



thinking\_tokens: int

Number of output tokens the model generated as internal reasoning, including
the thinking-block delimiter tokens.

Reflects the raw reasoning the model produced, not the (possibly shorter)
summarized thinking text returned in the response body. Computed by
re-tokenizing the raw reasoning text, so it may differ from the model's exact
generation count by a small number of tokens. Always ≤ `output_tokens`;
`output_tokens - thinking_tokens` approximates the non-reasoning output.

minimum0



server\_tool\_use: Optional[BetaServerToolUsage]

The number of server tool requests.

web\_fetch\_requests: int

The number of web fetch tool requests.

web\_search\_requests: int

The number of web search tool requests.



service\_tier: Optional[Literal["standard", "priority", "batch"]]

If the request used the priority, standard, or batch tier.

One of the following:

"standard"

"priority"

"batch"



speed: Optional[Literal["standard", "fast"]]

The inference speed mode used for this request.

One of the following:

"standard"

"fast"



class BetaUserLocation: …

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebFetchBlock: …



content: [BetaDocumentBlock](api/beta/messages.md)



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL



class BetaWebFetchBlockParam: …



content: [BetaRequestDocumentBlock](api/beta/messages.md)



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved



class BetaWebFetchTool20250910: …



name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20250910"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260209: …



name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260209"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



class BetaWebFetchTool20260309: …

Web fetch tool with use\_cache parameter for bypassing cached content.



name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260309"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

use\_cache: Optional[bool]

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaWebFetchTool20260318: …



name: Literal["web\_fetch"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_fetch\_20260318"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

List of domains to allow fetching from

blocked\_domains: Optional[List[str]]

List of domains to block fetching from



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

Citations configuration for fetched documents. Citations are disabled by default.

enabled: Optional[bool]

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_content\_tokens: Optional[int]

Maximum number of tokens used by including web page text content in the context. The limit is approximate and does not apply to binary content such as PDFs.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.



response\_inclusion: Optional[Literal["full", "excluded"]]

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"

"excluded"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs

use\_cache: Optional[bool]

Whether to use cached content. Set to false to bypass the cache and fetch fresh content. Only set to false when the user explicitly requests fresh content or when fetching rapidly-changing sources.



class BetaWebFetchToolResultBlock: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlock: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlock: …



content: [BetaDocumentBlock](api/beta/messages.md)



citations: Optional[BetaCitationConfig]

Citation configuration for the document

enabled: bool



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]

title: Optional[str]

The title of the document

type: Literal["document"]

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultBlockParam: …



content: Content

One of the following:



class BetaWebFetchToolResultErrorBlockParam: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchBlockParam: …



content: [BetaRequestDocumentBlock](api/beta/messages.md)



source: Source

One of the following:



class BetaBase64PDFSource: …

data: str

media\_type: Literal["application/pdf"]

type: Literal["base64"]



class BetaPlainTextSource: …

data: str

media\_type: Literal["text/plain"]

type: Literal["text"]



class BetaContentBlockSource: …



content: Union[str, List[[BetaContentBlockSourceContent](api/beta/messages.md)]]

One of the following:

str



List[[BetaContentBlockSourceContent](api/beta/messages.md)]

One of the following:



class BetaTextBlockParam: …

text: str

type: Literal["text"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[List[[BetaTextCitationParam](api/beta/messages.md)]]

One of the following:



class BetaCitationCharLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_char\_index: int

start\_char\_index: int

type: Literal["char\_location"]



class BetaCitationPageLocationParam: …

cited\_text: str

document\_index: int

document\_title: Optional[str]

end\_page\_number: int

start\_page\_number: int

type: Literal["page\_location"]



class BetaCitationContentBlockLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.

document\_index: int

document\_title: Optional[str]



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

type: Literal["content\_block\_location"]



class BetaCitationWebSearchResultLocationParam: …

cited\_text: str

encrypted\_index: str

title: Optional[str]

type: Literal["web\_search\_result\_location"]

url: str



class BetaCitationSearchResultLocationParam: …



cited\_text: str

The full text of the cited block range, concatenated.

Always equals the contents of `content[start_block_index:end_block_index]` joined together. The text block is the minimal citable unit; this field is never a substring of a single block. Not counted toward output tokens, and not counted toward input tokens when sent back in subsequent turns.



end\_block\_index: int

Exclusive 0-based end index of the cited block range in the source's `content` array.

Always greater than `start_block_index`; a single-block citation has `end_block_index = start_block_index + 1`.



search\_result\_index: int

0-based index of the cited search result among all `search_result` content blocks in the request, in the order they appear across messages and tool results.

Counted separately from `document_index`; server-side web search results are not included in this count.

minimum0

source: str

start\_block\_index: int

0-based index of the first cited block in the source's `content` array.

title: Optional[str]

type: Literal["search\_result\_location"]



class BetaImageBlockParam: …



source: Source

One of the following:



class BetaBase64ImageSource: …

data: str



media\_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

One of the following:

"image/jpeg"

"image/png"

"image/gif"

"image/webp"

type: Literal["base64"]



class BetaURLImageSource: …

type: Literal["url"]

url: str



class BetaFileImageSource: …

file\_id: str

type: Literal["file"]

type: Literal["image"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

type: Literal["content"]



class BetaURLPDFSource: …

type: Literal["url"]

url: str



class BetaFileDocumentSource: …

file\_id: str

type: Literal["file"]

type: Literal["document"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



citations: Optional[BetaCitationsConfigParam]

enabled: Optional[bool]

context: Optional[str]

title: Optional[str]

type: Literal["web\_fetch\_result"]

url: str

Fetched content URL

retrieved\_at: Optional[str]

ISO 8601 timestamp when the content was retrieved

tool\_use\_id: str

type: Literal["web\_fetch\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



class BetaWebFetchToolResultErrorBlock: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



class BetaWebFetchToolResultErrorBlockParam: …



error\_code: [BetaWebFetchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"url\_too\_long"

"url\_not\_allowed"

"url\_not\_in\_prior\_context"

"url\_not\_accessible"

"unsupported\_content\_type"

"too\_many\_requests"

"max\_uses\_exceeded"

"unavailable"

type: Literal["web\_fetch\_tool\_result\_error"]



Literal["invalid\_tool\_input", "url\_too\_long", "url\_not\_allowed", 6 more]

One of the following:

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

class BetaWebSearchResultBlock: …

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str



class BetaWebSearchResultBlockParam: …

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]



class BetaWebSearchTool20250305: …



name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20250305"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



user\_location: Optional[BetaUserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebSearchTool20260209: …



name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20260209"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



user\_location: Optional[BetaUserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebSearchTool20260318: …



name: Literal["web\_search"]

Name of the tool.

This is how the tool will be called by the model and in `tool_use` blocks.

type: Literal["web\_search\_20260318"]



allowed\_callers: Optional[List[Literal["direct", "code\_execution\_20250825", "code\_execution\_20260120", "code\_execution\_20260521"]]]

One of the following:

"direct"

"code\_execution\_20250825"

"code\_execution\_20260120"

"code\_execution\_20260521"

allowed\_domains: Optional[List[str]]

If provided, only these domains will be included in results. Cannot be used alongside `blocked_domains`.

blocked\_domains: Optional[List[str]]

If provided, these domains will never appear in results. Cannot be used alongside `allowed_domains`.



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"

defer\_loading: Optional[bool]

If true, tool will not be included in initial system prompt. Only loaded when returned via tool\_reference from tool search.

max\_uses: Optional[int]

Maximum number of times the tool can be used in the API request.



response\_inclusion: Optional[Literal["full", "excluded"]]

How this tool's result blocks appear in the API response when the result was consumed by a completed code\_execution call in the same turn. 'full' returns the complete content (default). 'excluded' drops the nested server\_tool\_use and result block pair entirely. Results from direct calls, or from code\_execution calls that paused before completing, are always returned in full so they can be sent back on the next turn.

One of the following:

"full"

"excluded"

strict: Optional[bool]

When true, guarantees schema validation on tool names and inputs



user\_location: Optional[BetaUserLocation]

Parameters for the user's location. Used to provide more relevant search results.

type: Literal["approximate"]

city: Optional[str]

The city of the user.

country: Optional[str]

The two letter [ISO country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) of the user.

region: Optional[str]

The region of the user.

timezone: Optional[str]

The [IANA timezone](https://nodatime.org/TimeZones) of the user.



class BetaWebSearchToolRequestError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



class BetaWebSearchToolResultBlock: …



content: [BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[BetaWebSearchResultBlock](api/beta/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



[BetaWebSearchToolResultBlockContent](api/beta/messages.md)

One of the following:



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



List[[BetaWebSearchResultBlock](api/beta/messages.md)]

encrypted\_content: str

page\_age: Optional[str]

title: str

type: Literal["web\_search\_result"]

url: str



class BetaWebSearchToolResultBlockParam: …



content: [BetaWebSearchToolResultBlockParamContent](api/beta/messages.md)

One of the following:



List[[BetaWebSearchResultBlockParam](api/beta/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]



class BetaWebSearchToolRequestError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]

tool\_use\_id: str

type: Literal["web\_search\_tool\_result"]



cache\_control: Optional[BetaCacheControlEphemeral]

Create a cache control breakpoint at this content block.

type: Literal["ephemeral"]



ttl: Optional[Literal["5m", "1h"]]

The time-to-live for the cache control breakpoint.

This may be one the following values:

- `5m`: 5 minutes
- `1h`: 1 hour

Defaults to `5m`. See [prompt caching pricing](build-with-claude/prompt-caching.md) for details.

One of the following:

"5m"

"1h"



caller: Optional[Caller]

Tool invocation directly from the model.

One of the following:



class BetaDirectCaller: …

Tool invocation directly from the model.

type: Literal["direct"]



class BetaServerToolCaller: …

Tool invocation generated by a server-side tool.

tool\_id: str

type: Literal["code\_execution\_20250825"]



class BetaServerToolCaller20260120: …

tool\_id: str

type: Literal["code\_execution\_20260120"]



[BetaWebSearchToolResultBlockParamContent](api/beta/messages.md)

One of the following:



List[[BetaWebSearchResultBlockParam](api/beta/messages.md)]

encrypted\_content: str

title: str

type: Literal["web\_search\_result"]

url: str

page\_age: Optional[str]



class BetaWebSearchToolRequestError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



class BetaWebSearchToolResultError: …



error\_code: [BetaWebSearchToolResultErrorCode](api/beta/messages.md)

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

type: Literal["web\_search\_tool\_result\_error"]



Literal["invalid\_tool\_input", "unavailable", "max\_uses\_exceeded", 3 more]

One of the following:

"invalid\_tool\_input"

"unavailable"

"max\_uses\_exceeded"

"too\_many\_requests"

"query\_too\_long"

"request\_too\_large"

#### MessagesBatches

##### [Create a Message Batch](api/beta/messages/batches/create.md)

beta.messages.batches.create(BatchCreateParams\*\*kwargs)  -> [BetaMessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches

##### [Retrieve a Message Batch](api/beta/messages/batches/retrieve.md)

beta.messages.batches.retrieve(strmessage\_batch\_id, BatchRetrieveParams\*\*kwargs)  -> [BetaMessageBatch](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}

##### [List Message Batches](api/beta/messages/batches/list.md)

beta.messages.batches.list(BatchListParams\*\*kwargs)  -> SyncPage[[BetaMessageBatch](api/beta/messages/batches.md)]

GET/v1/messages/batches

##### [Cancel a Message Batch](api/beta/messages/batches/cancel.md)

beta.messages.batches.cancel(strmessage\_batch\_id, BatchCancelParams\*\*kwargs)  -> [BetaMessageBatch](api/beta/messages/batches.md)

POST/v1/messages/batches/{message\_batch\_id}/cancel

##### [Delete a Message Batch](api/beta/messages/batches/delete.md)

beta.messages.batches.delete(strmessage\_batch\_id, BatchDeleteParams\*\*kwargs)  -> [BetaDeletedMessageBatch](api/beta/messages/batches.md)

DELETE/v1/messages/batches/{message\_batch\_id}

##### [Retrieve Message Batch results](api/beta/messages/batches/results.md)

beta.messages.batches.results(strmessage\_batch\_id, BatchResultsParams\*\*kwargs)  -> [BetaMessageBatchIndividualResponse](api/beta/messages/batches.md)

GET/v1/messages/batches/{message\_batch\_id}/results

---

*Copyright © Anthropic. All rights reserved.*
